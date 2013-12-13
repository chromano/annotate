from django.conf.urls import patterns, include, url

urlpatterns = patterns('annotate.views',
    url(r'^$', 'index'),
    url(r'^new/$', 'new', name="new_annotateddoc"),
    url(r'^post/$', 'post', name='post_annotateddoc'),
    url(r'^get/(?P<doc_hash>[\w\d+-.@]+)/$', 'get', name='get_annotateddoc'),
    url(r'^list/$', 'list', name='list_annotateddocs'),
    url(r'^view/(?P<doc_hash>[\w\d+-.@]+)/$', 'view', name='view_annotateddoc'),
    url(r'^edit/(?P<doc_hash>[\w\d+-.@]+)/$', 'edit', name='edit_annotateddoc'),
)
