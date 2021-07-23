from django.urls import path
from . import views

urlpatterns = [
  #path('', views.index, name='index')
  path('', views.form, name='form'),
  path('counter', views.counter, name='counter'),
  path('api1', views.api1, name='api1'),
  path('onepage', views.onepage, name='onepage')
]