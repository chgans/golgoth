
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       )

#
# http://django-debug-toolbar.readthedocs.org/en/1.2/installation.html#quick-setup
#
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^debug_toolbar/', include(debug_toolbar.urls)),
                            )

#
# http://django-authtools.readthedocs.org/en/latest/intro.html#quick-setup
#
urlpatterns += patterns('',
                        url(r'^accounts/', include('authtools.urls')),
                        )
