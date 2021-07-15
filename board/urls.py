from django.contrib import admin
from django.urls import path, include

import board
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:board_id>/', views.detail, name="detail"),
    path('delete/<int:content_id>/', views.content_delete, name="delete"),
    path('content/create/<int:board_id>/', views.content_create, name="content_create"),
    path('create/', views.board_create, name = 'board_create'),
]