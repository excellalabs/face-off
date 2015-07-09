from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
admin.site.site_header = "Excella Face It Administration"
admin.site.site_title = "Excella Face It"

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('core.urls', namespace='core')),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^s3direct/', include('s3direct.urls')),
                      )
