# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebRequest'
        db.create_table(u'requests_webrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'requests', ['WebRequest'])


    def backwards(self, orm):
        # Deleting model 'WebRequest'
        db.delete_table(u'requests_webrequest')


    models = {
        u'requests.webrequest': {
            'Meta': {'object_name': 'WebRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['requests']