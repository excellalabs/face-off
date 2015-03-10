from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'core.views.users', name='users'),
    url(r'^login/$', 'core.views.custom_login', name='login'),
   # url(r'^round/$', 'core.views.next_round', name='round'),
)
