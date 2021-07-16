
from django.contrib import admin
from django.urls import path, include


from comment import views

app_name = 'comments'

urlpatterns = [
    path('create/<int:content_id>', views.create, name = 'create'),
    # path('update/<int:comment_id>', views.update, name = 'update'),
    path('delete/<int:comment_id>', views.delete, name = 'delete'),
]
