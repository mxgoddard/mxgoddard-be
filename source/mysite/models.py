from django.db import models

# Create your models here.
class Checklist(models.Model):
    task = models.CharField(max_length=150)
    severity = models.IntegerField(default=1)
    complete = models.BooleanField(default=False)
    added = models.DateTimeField()

    def __str__(self):
        return self.task

class ShoppingList(models.Model):
    item = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.item, self.cost)

'''
python manage.py makemigrations mysite
python manage.py migrate
'''

'''
python manage.py shell
from mysite.models import Checklist
Checklist.objects.all()
'''