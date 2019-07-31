from django.db import models

# Create your models here.
class Routine(models.Model):
    day = models.IntegerField(null=False, primary_key=True, default=1)
    date = models.DateField(null=False)
    pushups = models.IntegerField(default=0, null=False)
    notes = models.CharField(max_length=300, blank=True, default="")

    def __str__(self):
        return (str(self.date))

'''
python manage.py makemigrations
python manage.py migrate
'''

'''
python manage.py shell
from mysite.models import Checklist
Checklist.objects.all()
'''
