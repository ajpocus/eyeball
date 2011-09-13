# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Task'
        db.create_table('tasks_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estimated_time', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('actual_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('tasks', ['Task'])


    def backwards(self, orm):
        
        # Deleting model 'Task'
        db.delete_table('tasks_task')


    models = {
        'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'actual_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'estimated_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tasks']
