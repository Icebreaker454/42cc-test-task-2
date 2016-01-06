"""
    This module contains views for the core application
"""
import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic import RedirectView

from apps.core.forms import LoginForm

logger = logging.getLogger('core')


class LoginRequiredMixin(object):
    """
    Class that implements @login_required functionality
    into a class-based view
    """
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse('home')


class LoginView(FormView):
    """ This is the login class based view """
    template_name = 'login.html'
    form_class = LoginForm

    def get_form_kwargs(self):
        """ Passes the next url to redirect to into form """
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs['next'] = self.request.GET.get('next', '')
        return kwargs

    def form_valid(self, form):
        """ Logins the user """
        login(self.request, form.get_user())
        logger.info('User %s authenticated' % form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        """ Returns success url for the view """
        url = self.request.GET.get('next', '')
        if url:
            logger.info('Redirecting to: %s' % url)
            return url
        return reverse('home')
