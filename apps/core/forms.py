"""
    This module contains forms for the core application
"""

from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class LoginForm(AuthenticationForm):
    """ This is the form for user login """
    def __init__(self, next, *args, **kwargs):
        """ Initialization method """
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = '%s?next=%s' % (
            reverse('login'),
            next
        )
        self.helper.form_method = 'POST'
        self.helper.form_class = 'login-form'

        self.helper.label_class = 'form-label'

        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(
                Submit(
                    name='login',
                    value='Login',
                    css_class='btn-link done-button'
                )
            )
        )
