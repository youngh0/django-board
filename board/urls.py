from django.contrib import admin
from django.urls import path, include

import board
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:board_id>/', views.detail, name="detail"),
    path('delete/<int:content_id>/', views.content_delete, name="delete"),
    path('update/<int:content_id>/', views.content_update, name="update"),
    path('content/create/<int:board_id>/', views.content_create, name="content_create"),
    path('create/', views.board_create, name = 'board_create'),
    path('content/<int:content_id>', views.content_detail, name = 'content_detail'),
    path('create/<int:content_id>', views.comment_create, name = 'comment_create'),
    path('update/<int:comment_id>', views.comment_update, name = 'comment_update'),
    path('delete/<int:comment_id>', views.comment_delete, name = 'comment_delete'),
]