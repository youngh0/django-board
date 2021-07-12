from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import User

admin.site.register(User)