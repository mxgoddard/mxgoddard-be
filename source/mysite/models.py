from django.db import models

# Create your models here.
class Checklist(models.Model):
    task = models.CharField(max_length=150)
    severity = models.IntegerField(default=1)
    complete = models.BooleanField(default=False)
    added = models.DateTimeField()

    def __str__(self):
        return self.task

class Routine(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    day = models.IntegerField(null=False)
    date = models.DateField(null=False)
    pushups = models.IntegerField(default=0, null=False)
    notes = models.CharField(max_length=300, null=True)

    def __str__(self):
        return (self.day)

'''
python manage.py makemigrations mysite
python manage.py migrate
'''

'''
python manage.py shell
from mysite.models import Checklist
Checklist.objects.all()
'''
