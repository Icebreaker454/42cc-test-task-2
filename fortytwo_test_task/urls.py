from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('apps.personal_info.urls')),
    url(
        r'^$',
        RedirectView.as_view(url='/home/', permanent=False),
        name='index'
    ),
)
