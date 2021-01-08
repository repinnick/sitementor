from django.db import models
from django.contrib.auth.models import AbstractUser

from site_constructor.models import LanguagesList




USER_TYPES = [
    ("M", "Mentor"),
    ("S", "Student"),
    ("ITS", "IT-School"),
]

class ProfileUser(AbstractUser):
    types = models.CharField(max_length=50, choices=USER_TYPES, verbose_name="Тип учетной записи")
    language_list = models.ManyToManyField(LanguagesList, blank=True, null=True)
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона (9 цифр)", blank=True)
    about_you = models.TextField(blank=True, verbose_name='О себе')
    user_photo = models.ImageField(upload_to='profile_icons/%Y%m%d/', verbose_name='Фото', blank=True)
    linked_in = models.CharField(max_length=250, blank=True)
    is_published = models.BooleanField(verbose_name="Опубликовать", default=True)
#    language_list = models.ForeignKey(LanguagesList, on_delete=models.CASCADE)
