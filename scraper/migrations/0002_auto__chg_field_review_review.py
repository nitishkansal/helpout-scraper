# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Review.review'
        db.alter_column(u'scraper_review', 'review', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Review.review'
        db.alter_column(u'scraper_review', 'review', self.gf('django.db.models.fields.CharField')(max_length=255))

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
            'review': ('django.db.models.fields.TextField', [], {}),
            'reviewer_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'scraper.searchterm': {
            'Meta': {'object_name': 'SearchTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['scraper']