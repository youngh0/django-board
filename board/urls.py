from django.contrib import admin
from django.urls import path, include

import board
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.board_create, name = 'board_create'),
]