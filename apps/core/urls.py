"""
    This module contains urls for the core application
"""

from django.conf.urls import patterns, url

from apps.core.views import LoginView
from apps.core.views import LogoutView

urlpatterns = patterns(
    '',
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout')
)
