from django.contrib import admin

from .models import Match


# @admin.register(Match)
# class HubAdmin(admin.ModelAdmin):
#     date_hierarchy = 'date_created'
#     list_display = (
#     	'champion',
#     	'lane',
#     	'cs',
#     	'date_created',
# 	)