from django.urls import path
from . import views

urlpattersns =[
  path('',views.index,name='index')
]