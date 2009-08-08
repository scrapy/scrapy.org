from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # admin
    url(r'^admin/(.*)', admin.site.root),
    url(r"^docs/.*", 'django.views.generic.simple.redirect_to', {'url': '/doc/'}),
    url(r"^news/", include("scrapyorg.blog.urls")),
)


if settings.DEBUG: # devel
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:],
          'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),
    )

# last resort, it's an article
urlpatterns += patterns('',
    url(r"", include("scrapyorg.article.urls")),
)

