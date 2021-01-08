from django.contrib import admin
from .models import ProfileUser


class UserListAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'types', 'is_active')

admin.site.register(ProfileUser, UserListAdmin)

