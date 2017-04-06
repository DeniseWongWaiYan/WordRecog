from django.contrib import admin
from .models import Profile, Connection, Test

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth', 'profile_picture']
    inlines = ['ProfileImageAdmin',]


admin.site.register(Profile, ProfileAdmin)


class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['user_from', 'user_to']

admin.site.register(Connection, ConnectionAdmin)

class ProfileImageAdmin(admin.TabularInLine):
    model = photototesseractform
    extra = 50
    
