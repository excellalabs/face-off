from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
#site header name
admin.site.site_header = "Excella Face It Administration"
#site title name
admin.site.site_title = "Excella Face It"


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls', namespace='core')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)