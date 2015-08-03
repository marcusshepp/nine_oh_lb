from django.contrib import admin
from django.contrib.auth.models import User

from .models import PyManager

@admin.register(PyManager)
class HubAdmin(admin.ModelAdmin):
	pass