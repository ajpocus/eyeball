from django.db import models


class Task(models.Model):
    estimated_time = models.DecimalField(max_digits=14, decimal_places=2)
    actual_time = models.DecimalField(max_digits=14, decimal_places=2,
	blank=True, null=True)
    description = models.CharField(max_length=140)
    is_finished = models.BooleanField(default=False)

    def __unicode__(self):
	return self.description


