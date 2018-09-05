# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:16:36 2018

@author: 2017VaioPro
"""

from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),              
   path('create', views.create, name='create'),     
   path('edit/<int:num>', views.edit, name='edit'),       
   path('delete/<int:num>', views.delete, name='delete'),      
   path('find', views.find, name='find'),     
   
]