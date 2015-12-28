# -*- coding: utf-8 -*-

"""
    This module contains models for the requests app
"""

from django.db import models


class WebRequest(models.Model):
    """ This is the WebRequest model """
    class Meta:
        verbose_name = "Web request"
        verbose_name_plural = "Web requests"

    path = models.SlugField()
    method = models.CharField(max_length=10)
    status_code = models.PositiveSmallIntegerField(default=200)
    user_agent = models.CharField(max_length=256, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    is_secure = models.BooleanField(default=False)
    is_ajax = models.BooleanField(default=False)

    def __unicode__(self):
        """ Model's string representation """
        return "%s %s" % (self.method, self.path)
