from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'core.views.cards', name='cards'),
    url(r'^login/$', 'core.views.custom_login', name='login'),
    url(r'^rounds/$', 'core.views.next_round', name='rounds'),
    url(r'^results/$', 'core.views.results', name='results'),
)
