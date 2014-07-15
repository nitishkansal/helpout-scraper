from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^get-info/$', 'scraper.views.get_info'),
)
