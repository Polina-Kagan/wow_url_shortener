from django.db import models
from django.contrib.auth.models import User
from . import views
from django.urls import path

urlpatterns = [
   path('', views.cutter, name='cutter'),
   path('<str:short_code>/', views.redirect_short_link, name='redirect_short_link'),

]