from django.contrib import admin

from django.urls import path, include

from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('profile/<int:uid>/',views.profile,name='profile'),
    path('profile/modifyNickname/<int:uid>/',views.modify_nickname,name='modify_nickname'),
    path('profile/modifyPassword/<int:uid>/',views.modify_password,name='modify_password'),
    path('profile/delete/<int:uid>/',views.delete_user,name='delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.loginUser, name='login')

]