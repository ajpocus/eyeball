import decimal

from django import forms
from tasks.models import Task

class TaskAddForm(forms.Form):
    description = forms.CharField(max_length=140)
    estimated_hours = forms.IntegerField()
    estimated_minutes = forms.IntegerField()

    def process(self):
	data = self.cleaned_data
	hours = data['estimated_hours']
	minutes = data['estimated_minutes']
	estimate = ((hours * 60 * 60) + (minutes * 60))
	Task.objects.create(description=data['description'],
	    estimated_time=decimal.Decimal(estimate))
	
