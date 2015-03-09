from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'core.views.users', name='users'),
    url(r'^accounts/login/$', 'core.views.custom_login', name='login'),
)
