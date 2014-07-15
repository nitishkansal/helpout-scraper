# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchTerm'
        db.create_table(u'scraper_searchterm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'scraper', ['SearchTerm'])

        # Adding model 'Helpout'
        db.create_table(u'scraper_helpout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraper.SearchTerm'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('helpout_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('available', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('about_provider', self.gf('django.db.models.fields.TextField')()),
            ('image_link', self.gf('django.db.models.fields.TextField')()),
            ('video_link', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'scraper', ['Helpout'])

        # Adding model 'Review'
        db.create_table(u'scraper_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('helpout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraper.Helpout'])),
            ('reviewer_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('review', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'scraper', ['Review'])


    def backwards(self, orm):
        # Deleting model 'SearchTerm'
        db.delete_table(u'scraper_searchterm')

        # Deleting model 'Helpout'
        db.delete_table(u'scraper_helpout')

        # Deleting model 'Review'
        db.delete_table(u'scraper_review')


    models = {
        u'scraper.helpout': {
            'Meta': {'object_name': 'Helpout'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'about_provider': ('django.db.models.fields.TextField', [], {}),
            'available': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'helpout_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'search_term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scraper.SearchTerm']"}),
            'video_link': ('django.db.models.fields.TextField', [], {})
        },
        u'scraper.review': {
            'Meta': {'object_name': 'Review'},
            'helpout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scraper.Helpout']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'reviewer_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'scraper.searchterm': {
            'Meta': {'object_name': 'SearchTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['scraper']