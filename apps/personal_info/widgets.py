# -*- coding: utf-8 -*-

"""
    This module contains widgets for the personal_info app
"""

from django.forms.widgets import ClearableFileInput


class ImagePreviewWidget(ClearableFileInput):
    """ This class describes a widget for uploading an image
    With possibility to preview it """
    def render(self, name, value, *args, **kwargs):
        if value and value.url:
            url = value.url
        else:
            url = ''
        return '<p><img class="js-preview" src="' + \
            url + '" width="200px"></p>' + \
            super(ImagePreviewWidget, self).render(
                name, value, *args, **kwargs
            )
