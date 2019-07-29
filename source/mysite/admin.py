from django.contrib import admin

# Register your models here.
from .models import Checklist, Routine

admin.site.register(Checklist)
admin.site.register(Routine)
