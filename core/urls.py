from django.conf.urls import patterns, url
from views import RegistrationView

urlpatterns = patterns('',

    url(r'^$', 'core.views.cards', name='cards'),
    url(r'^login/$', 'core.views.custom_login', name='login'),
    url(r'^sign_in/$', 'django.contrib.auth.views.login'),
    url('^register/', RegistrationView.as_view(), name='register'),
    url(r'^rounds/$', 'core.views.next_round', name='rounds'),
    url(r'^results/$', 'core.views.results', name='results'),
    url(r'^metrics/$', 'core.views.metrics', name='metrics'),
    url(r'^ajax_suggestion/$', 'core.views.ajax_suggestion', name='ajax_suggestion'),
    url(r'^encountered/$', 'core.views.encountered', name='encountered'),
    url(r'^globally_known/$', 'core.views.globally_known', name='globally_known'),

)
