from __future__ import division
from core.models import UserMetrics, ColleagueGraph, UserProfile
from django.db.models import *


names = list(ColleagueGraph.objects.order_by('name')
             .distinct('name').values_list('name', flat=True))

max_times_correct = 0
max_times = {}

for name in names:

    times_corr = ColleagueGraph.objects.filter(name=name)\
        .aggregate(Sum('times_correct'))['times_correct__sum']
    if times_corr > max_times_correct:
        max_times_correct = times_corr
        max_times.update({str(times_corr): [name]})
    elif not str(times_corr) in max_times and times_corr > 1:
        max_times.update({str(times_corr): [name]})
    elif times_corr > 1:
        max_times[str(times_corr)].append(name)

print 'Colleagues guessed most times correctly'
print sorted(max_times.items())


usernames = UserProfile.objects.order_by('username').values_list('username', flat=True)
time_played = {}

for name in usernames:
    times_corr = ColleagueGraph.objects.filter(user__username=name)\
        .aggregate(Sum('times_correct'))['times_correct__sum']
    times_wrong = ColleagueGraph.objects.filter(user__username=name)\
        .aggregate(Sum('times_incorrect'))['times_incorrect__sum']
    time_played.update({name:str(times_corr + times_wrong)})

print 'Colleagues Played the Most'
print sorted(time_played.items())


usernames = UserProfile.objects.order_by('username').values_list('username', flat=True)
time_played = {}

for name in usernames:
    times_corr = ColleagueGraph.objects.filter(user__username=name)\
        .aggregate(Sum('times_correct'))['times_correct__sum']
    times_wrong = ColleagueGraph.objects.filter(user__username=name)\
        .aggregate(Sum('times_incorrect'))['times_incorrect__sum']
    time_played.update({name:str(times_corr/(times_corr+times_wrong))})

print 'Colleagues most likely to know you'
print sorted(time_played.items())