from django.contrib import admin
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import OTPRequest

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(OTPRequest)
class OTPRequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'channel', 'receiver', 'password', 'created')
