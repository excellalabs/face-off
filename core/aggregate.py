from core.models import UserMetrics, ColleagueGraph
from django.db.models import *


names = list(ColleagueGraph.objects.order_by('name').distinct('name').values_list('name', flat=True))

max_times_correct = 0;
max_times = {}
for name in names:
    times_corr = ColleagueGraph.objects.filter(name=name).aggregate(Sum('times_correct'))['times_correct__sum']
    if times_corr > max_times_correct:
        #print name + ' : ' + str(times_corr)
        max_times_correct = times_corr
        max_times.update({str(times_corr): [name]})
    elif times_corr == max_times_correct and max_times_correct > 1:
        max_times[str(times_corr)].append(name)

print 'Colleague guess most times correctly'
print max_times

