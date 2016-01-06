from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

from django.views.generic.base import RedirectView

from fortytwo_test_task.settings import common as settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('apps.personal_info.urls')),
    url(r'^requests/', include('apps.requests.urls')),
    url(
        r'^$',
        RedirectView.as_view(url='/home/', permanent=False),
        name='redirect_index'
    ),

    url(r'^', include('apps.core.urls'))

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
