# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Semester'
        db.create_table(u'mark_management_semester', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'mark_management', ['Semester'])

        # Adding model 'Year'
        db.create_table(u'mark_management_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('semester_1', self.gf('django.db.models.fields.related.OneToOneField')(related_name='semester_1', unique=True, to=orm['mark_management.Semester'])),
            ('semester_2', self.gf('django.db.models.fields.related.OneToOneField')(related_name='semester_2', unique=True, to=orm['mark_management.Semester'])),
            ('marks_interval_min', self.gf('django.db.models.fields.IntegerField')()),
            ('marks_interval_max', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mark_management', ['Year'])

        # Adding model 'Subject'
        db.create_table(u'mark_management_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('teacher', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mark_management.Year'])),
        ))
        db.send_create_signal(u'mark_management', ['Subject'])

        # Adding M2M table for field typs on 'Subject'
        m2m_table_name = db.shorten_name(u'mark_management_subject_typs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subject', models.ForeignKey(orm[u'mark_management.subject'], null=False)),
            ('typ', models.ForeignKey(orm[u'mark_management.typ'], null=False))
        ))
        db.create_unique(m2m_table_name, ['subject_id', 'typ_id'])

        # Adding model 'Typ'
        db.create_table(u'mark_management_typ', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('valence', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mark_management', ['Typ'])

        # Adding model 'Mark'
        db.create_table(u'mark_management_mark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('typ', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mark_management.Typ'])),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mark_management.Semester'])),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mark_management.Subject'])),
        ))
        db.send_create_signal(u'mark_management', ['Mark'])


    def backwards(self, orm):
        # Deleting model 'Semester'
        db.delete_table(u'mark_management_semester')

        # Deleting model 'Year'
        db.delete_table(u'mark_management_year')

        # Deleting model 'Subject'
        db.delete_table(u'mark_management_subject')

        # Removing M2M table for field typs on 'Subject'
        db.delete_table(db.shorten_name(u'mark_management_subject_typs'))

        # Deleting model 'Typ'
        db.delete_table(u'mark_management_typ')

        # Deleting model 'Mark'
        db.delete_table(u'mark_management_mark')


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