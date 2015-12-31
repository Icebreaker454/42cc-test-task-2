# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'personal_info_person')


    def backwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'personal_info_person', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=128, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'personal_info', ['Person'])


    models = {
        
    }

    complete_apps = ['personal_info']