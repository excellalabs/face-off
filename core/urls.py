from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^$', 'home', name='home'),
    url(r'^$', 'core.views.users', name='users'),
    #url(r'login/$', 'django.contrib.auth.views.login',
    #    {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/login/$', 'core.views.custom_login', name='login'),
)
