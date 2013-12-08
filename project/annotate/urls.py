from django.conf.urls import patterns, include, url

urlpatterns = patterns('annotate.views',
    url(r'^$', 'index'),
    url(r'^post/$', 'post', name='post_annotateddoc'),
    url(r'^get/$', 'get', name='get_annotateddoc'),
)
