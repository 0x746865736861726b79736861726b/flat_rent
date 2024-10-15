from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


# Register your models here.
