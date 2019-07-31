from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('pushups', views.GetRoutineData, name='Get routine data'),
    path('pushups/update', views.UpdateDay, name='Update day')
]
