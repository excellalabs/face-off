from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
import requests
import random
import re


def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)


@login_required
def users(request):
    social = request.user.social_auth.get(provider='yammer')
    access_token = social.extra_data['access_token']
    response = None
    users = []
    page = 1

    # TODO this caching is badly executed!!!!!
    # cache expiration should be tweaked
    # key should be something like '<org-key>-photo_users'
    photo_users = cache.get('photo_users')
    if photo_users:
        print "GOT CACHE"
    if not photo_users:
        print "NO CACHE"
        social = request.user.social_auth.get(provider='yammer')
        access_token = social.extra_data['access_token']
        response = None
        users = []
        page = 1

        while True:
            response = requests.get(
                'https://www.yammer.com/api/v1/users.json?page=%d' % page,
                headers = {'Authorization': 'Bearer %s' % access_token['token']}
            )
            if response.json() == []:
                break
            users.extend(response.json())
            page += 1

        photo_users = []
        pattern = re.compile('.+no_photo.png$')
        for user in users:
            if not pattern.match(user['mugshot_url']):
                photo_users.append(user)

        cache.set('users', users, 6000)
        cache.set('photo_users', photo_users, 6000)

    for user in photo_users:
        if user['state'] != 'active':
            print user['full_name'] + " " + user['state']
    length = len(photo_users)

    user_array = []
    for sample in random.sample(range(length), 4):
        user = photo_users[sample]
        user_array.append(user)
    answer = random.choice(user_array)

    context = RequestContext(request, {'users': user_array, 'answer': answer})
    return render_to_response('users.html', context_instance=context)
