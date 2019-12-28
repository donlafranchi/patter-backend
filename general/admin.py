from django.contrib import admin

from general.models import *


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'owner')


@admin.register(Event)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'venue', 'date', 'reach')
