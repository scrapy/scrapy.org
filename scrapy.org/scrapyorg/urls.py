from django.conf import settings
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django.views.generic.simple',
    url(r"^$", 'direct_to_template', {'template': 'pages/home.html'}),
    url(r"^download/", 'direct_to_template', {'template': 'pages/download.html'}),
    url(r"^doc/", 'direct_to_template', {'template': 'pages/doc.html'}),
    url(r"^community/", 'direct_to_template', {'template': 'pages/community.html'}),
    url(r"^support/", 'direct_to_template', {'template': 'pages/support.html'}),
    url(r"^donate/", 'direct_to_template', {'template': 'pages/donate.html'}),
    url(r"^timeline/", 'direct_to_template', {'template': 'pages/timeline.html'}),
    url(r"^companies/", 'direct_to_template', {'template': 'pages/companies.html'}),
)

if settings.DEBUG: # devel
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:], \
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
