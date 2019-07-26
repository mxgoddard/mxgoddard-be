from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('joke', views.Joke, name='Joke'),
    path('json', views.Json, name='Json'),
    path('helper', views.Helper, name='Helper'),
    path('fact', views.Fact, name='Fact'),
    path('shopping-list', views.ShoppingList, name='Shopping List')
]