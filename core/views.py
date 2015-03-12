from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django_redis import get_redis_connection
import requests, re, ast, random, HTMLParser
from core.models import UserMetrics
from django.core.exceptions import ObjectDoesNotExist

def custom_login(request):
    print request.path
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)


@login_required()
def cards(request):
    redis_con = get_redis_connection("default")
    # Unique Set per Network
    if request.user.email:
        network = request.user.email.split('@')[1]
    else:
        network = 'default'

    if redis_con.exists(network + '_users'):
        print "Cache Retrieved"
    else:
        print "Cache Loaded"
        users = []
        social = request.user.social_auth.get(provider='yammer')
        access_token = social.extra_data['access_token']

        response = requests.get(
            'https://www.yammer.com/api/v1/users.json?',
            headers={'Authorization': 'Bearer %s' % access_token['token']}
        )
        users.extend(response.json())

        pattern = re.compile('.+no_photo.png$')  # Filters out users with no photo
        for user in users:
            if not pattern.match(user['mugshot_url']):
                redis_con.sadd(user['network_name'] + '_users', {
                    'name': user['full_name'],
                    'mugshot': user['mugshot_url_template'],
                })
        redis_con.expire(network + '_users', 43200)  # Redis cache expiration set to 12hrs(43200s)

    user_round_matrix = [four_random_cards(redis_con, network) for x in range(5)]
    answer = random.choice(user_round_matrix[0])

    context = RequestContext(request, {'cards': user_round_matrix, 'answer': answer, 'round': 0, 'score': 0})
    return render_to_response('game.html', context_instance=context)


@login_required
def next_round(request):
    round = int(request.GET['round']) + 1
    score = int(request.GET['score'])

    card_matrix = HTMLParser.HTMLParser().unescape(request.GET['matrix'])
    card_matrix = ast.literal_eval(card_matrix)

    answer = random.choice(card_matrix[round])
    context = RequestContext(request, {'cards': card_matrix, 'round': round, 'answer': answer, 'score': score})

    return render_to_response('cards.html', context_instance=context)

@login_required
def results(request):
    try:
        metric = UserMetrics.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # This is here purely for backwards compatibility TODO remember to delete this line later
        metric = UserMetrics.objects.create(user=request.user).save()

    metric.times_won = request.GET['score']
    metric.save()

    return render(request, 'results.html')


def four_random_cards(redis_con, network):
    users = []
    while len(users) < 4:
        tmp = ast.literal_eval(redis_con.srandmember(network + '_users'))
        if tmp not in users:
            users.append(tmp)
    return users