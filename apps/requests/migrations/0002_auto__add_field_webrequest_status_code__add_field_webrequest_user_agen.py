# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WebRequest.status_code'
        db.add_column(u'requests_webrequest', 'status_code',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=200),
                      keep_default=False)

        # Adding field 'WebRequest.user_agent'
        db.add_column(u'requests_webrequest', 'user_agent',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WebRequest.is_secure'
        db.add_column(u'requests_webrequest', 'is_secure',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'WebRequest.is_ajax'
        db.add_column(u'requests_webrequest', 'is_ajax',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WebRequest.status_code'
        db.delete_column(u'requests_webrequest', 'status_code')

        # Deleting field 'WebRequest.user_agent'
        db.delete_column(u'requests_webrequest', 'user_agent')

        # Deleting field 'WebRequest.is_secure'
        db.delete_column(u'requests_webrequest', 'is_secure')

        # Deleting field 'WebRequest.is_ajax'
        db.delete_column(u'requests_webrequest', 'is_ajax')


    models = {
        u'requests.webrequest': {
            'Meta': {'object_name': 'WebRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ajax': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_secure': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '200'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['requests']