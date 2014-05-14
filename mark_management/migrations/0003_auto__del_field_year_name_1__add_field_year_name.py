# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Year.name_1'
        db.delete_column(u'mark_management_year', 'name_1')

        # Adding field 'Year.name'
        db.add_column(u'mark_management_year', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Name', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Year.name_1'
        db.add_column(u'mark_management_year', 'name_1',
                      self.gf('django.db.models.fields.CharField')(default='Name', max_length=255),
                      keep_default=False)

        # Deleting field 'Year.name'
        db.delete_column(u'mark_management_year', 'name')


    models = {
        u'mark_management.mark': {
            'Meta': {'object_name': 'Mark'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mark_management.Semester']"}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mark_management.Subject']"}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mark_management.Typ']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mark_management.semester': {
            'Meta': {'object_name': 'Semester'},
            'begin': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mark_management.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'teacher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'typs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mark_management.Typ']", 'symmetrical': 'False'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mark_management.Year']"})
        },
        u'mark_management.typ': {
            'Meta': {'object_name': 'Typ'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valence': ('django.db.models.fields.FloatField', [], {})
        },
        u'mark_management.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marks_interval_max': ('django.db.models.fields.IntegerField', [], {}),
            'marks_interval_min': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semester_1': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'semester_1'", 'unique': 'True', 'to': u"orm['mark_management.Semester']"}),
            'semester_2': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'semester_2'", 'unique': 'True', 'to': u"orm['mark_management.Semester']"})
        }
    }

    complete_apps = ['mark_management']