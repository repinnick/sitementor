from django.contrib import admin
from .models import LanguagesList



class LanguagesListAdmin(admin.ModelAdmin):
    list_display = ('language_name', 'language_photo')



admin.site.register(LanguagesList, LanguagesListAdmin)