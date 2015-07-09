import requests, re, ast, random, HTMLParser, json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django_redis import get_redis_connection
from core.models import UserMetrics, ColleagueGraph
from django.core.exceptions import ObjectDoesNotExist
from core.forms import SuggestionForm, ResultForm, UserProfileForm, UserAuthenticationForm
from django.views.generic import CreateView
import django.contrib.auth.views
from django.contrib.auth import authenticate, login
from django.conf import settings

class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserProfileForm
    success_url = '/'

    def get_success_url(self):
        user = self.object
        user.set_password(user.password)
        user.is_custom_user = True
        user.save()

        return '/'



def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    elif request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

    return django.contrib.auth.views.login(request, extra_context={'userAuthForm': UserAuthenticationForm()})

@login_required()
def cards(request):
    redis_con = get_redis_connection("default")

    # Yammer Authenticated Game
    if not request.user.is_custom_user:
        if request.user.email:
            network = str(request.user.email.split('@')[1]) + '_users'
        else:
            network = 'default_users'

        if not redis_con.exists(network):
            users = yammer_user_restcall(request)
            load_users_to_cache(redis_con, users, network)

        user_round_matrix = [four_random_cards(redis_con, network, request.user) for x in range(5)]
        answer = random.choice(user_round_matrix[0])
        stars = []

        context = RequestContext(request, {'cards': user_round_matrix, 'answer': answer,
                                           'round': 0, 'score': 0, 'stars': stars})
        return render_to_response('game.html', context_instance=context)
    else:
        context = RequestContext(request)
        return render_to_response('custom_game.html', context)


@login_required
def next_round(request):
    round_num = int(request.POST['round'])
    score = int(request.POST['score'])
    answer_id = int(request.POST['answer_id'])
    correct = ast.literal_eval(str(request.POST['correct']))
    stars = request.POST.getlist('stars[]')
    stars.append(str(correct))
    stars = json.dumps(stars)


    card_matrix = HTMLParser.HTMLParser().unescape(request.POST['matrix'])
    card_matrix = ast.literal_eval(card_matrix)

    # Sets the Winner of the round to the cardMatrix
    update_results_list(card_matrix, answer_id, round_num, correct)

    # Prepares data for next round
    round += 1
    answer = filter_previously_used_answer(card_matrix, round_num)


    context = RequestContext(request, {'cards': card_matrix, 'round': round_num, 'answer': answer,
                                       'score': score, 'stars': stars, 'resultsForm': ResultForm()})

    return render_to_response('cards.html', context_instance=context)


@login_required
def results(request):
    metric = UserMetrics.objects.get(user=request.user)

    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            results = ast.literal_eval(HTMLParser.HTMLParser().unescape(form.cleaned_data['results']))
            answer_id = form.cleaned_data['answer_id']
            correct = ast.literal_eval(str(form.cleaned_data['correct']))
            update_results_list(results, answer_id, 4, correct)  # 4 representing the last round (zero-based)

            if form.cleaned_data['mode'] != 'easy':
                metric.times_won = form.cleaned_data['score']
                metric.save()
                save_metric_results(results, request.user)

            context = RequestContext(request, {'score': form.cleaned_data['score'], 'cards': results})
            return render_to_response('results.html', context_instance=context)


@login_required
def metrics(request):
     # Colleagues you should get to know
    most_incorrect_colleagues = ColleagueGraph.objects.order_by('-times_incorrect').filter(user=request.user)[:5]

    context = RequestContext(request, {'leastknown': most_incorrect_colleagues})

    return render_to_response('metrics.html', context_instance=context)

@login_required
def encountered(request):
    # Colleagues Encountered Data
    encountered = ColleagueGraph.objects.filter(user=request.user).order_by('name')
    correct_arr = []
    incorrect_arr = []
    for colleague in encountered:
        correct_arr.append({"label": str(colleague.name), "value": colleague.times_correct})
        incorrect_arr.append({"label": str(colleague.name), "value": (colleague.times_incorrect * -1)})

    times_known = {"key": "Guessed Correctly", "color": 'red', "values": correct_arr}
    times_not_known = {"key": "Guessed Incorrectly", "color": "blue", "values": incorrect_arr}
    jsondata = [times_known, times_not_known]

    return HttpResponse(json.dumps(jsondata), content_type="application/json")

@login_required
def globally_known(request):
    # Global Known Colleagues
    globally_known = globally_known_colleagues()
    names = []
    times_correct = []

    for metric in globally_known:
        names.append(str(metric.name))
        times_correct.append(metric.times_correct)

    known = {
        'names': names,
        'times_correct': times_correct
    }
    return HttpResponse(json.dumps(known), content_type="application/json")

# Helper Functions
def yammer_user_restcall(request):
    users = []
    social = request.user.social_auth.get(provider='yammer')
    access_token = social.extra_data['access_token']
    page = 1

    while True:
        response = requests.get(
            'https://www.yammer.com/api/v1/users.json?page=%d' % page,
            headers={'Authorization': 'Bearer %s' % access_token['token']}
        )
        if not response.json():
            break
        users.extend(response.json())
        page += 1

    return users


def load_users_to_cache(redis_con, users, network):
    pattern = re.compile('.+no_photo.png$')  # Filters out users with no photo
    for user in users:
        if not pattern.match(user['mugshot_url']):
            redis_con.sadd(network, {
                'id': user['id'],
                'name': user['full_name'],
                'mugshot': user['mugshot_url_template'],
                'user_url': user['web_url'],
                'network': user['network_name'],
            })
    redis_con.expire(network, 43200)  # Redis cache expiration set to 12hrs(43200s)


def filter_previously_used_answer(card_matrix, round):
    answer = random.choice(card_matrix[round])
    unique_answer = False
    # Checks for previously used answer
    while not unique_answer:
        check_again = False
        for i in range(0, round):
            if card_matrix[i]['id'] == answer['id']:
                answer = random.choice(card_matrix[round])
                check_again = True
                break

        if not check_again:
            unique_answer = True

    return answer


def save_metric_results(results, user):
    for result in results:
        if result:
            try:
                metric = ColleagueGraph.objects.get(user=user, yammer_id=result['id'])
            except ObjectDoesNotExist:
                metric = ColleagueGraph.objects.create(user=user, yammer_id=result['id'],
                                                       name=result['name'], img_url=result['mugshot'],
                                                       yammer_url=result['user_url'])
            finally:
                if 'wrong' in result:
                    metric.times_incorrect += 1
                else:
                    metric.times_correct += 1
                metric.save()


def update_results_list(card_matrix, answer_id, round, correct):
    for i in range(0, 4):
        if card_matrix[round][i]['id'] == answer_id:
            if not correct:
                card_matrix[round][i]['wrong'] = True
                card_matrix[round] = card_matrix[round][i]
            else:
                card_matrix[round] = card_matrix[round][i]

            return card_matrix


def four_random_cards(redis_con, network, current_user):
    users = []

    while len(users) < 4:
        val = ast.literal_eval(redis_con.srandmember(network))
        if current_user.get_full_name() != val['name'] and val not in users:
            users.append(val)

    return users


def globally_known_colleagues():
    top_scores = (ColleagueGraph.objects.order_by('-times_correct')
                  .values_list('times_correct', flat=True)
                  .distinct())[:10]

    filtered_by_name = (ColleagueGraph.objects.order_by('name', '-times_correct')
                .filter(times_correct__in=top_scores))\
                .distinct('name')

    top_10_known_colleagues = sorted(filtered_by_name,
                                     key=lambda ColleagueGraph: ColleagueGraph.times_correct,
                                     reverse=True)[:10]
    return top_10_known_colleagues


def ajax_suggestion(request):
    if request.method == 'POST' and request.is_ajax():
        form = SuggestionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            suggestion = data['suggestion']
            email = data['email']
            form.save(commit=True)

            # Sends an email to the site administrators
            send_mail('New Suggestion for Face-Off from ' + first_name + " " + last_name, suggestion, email,
                      [email for (name, email) in settings.ADMINS])

            return HttpResponse("Thank you for your suggestion!")
        else:
            return HttpResponse("Invalid Data!")

    else:
        return HttpResponse('Service unavailable')
