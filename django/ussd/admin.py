from django.contrib import admin

from .models import UssdSession


@admin.register(UssdSession)
class UssdSessionAdmin(admin.ModelAdmin):
    list_display = ("created_at", "session_id", "user_phone", "user_input")
