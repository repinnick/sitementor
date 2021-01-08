from django.db import models
# from ..users.models import ProfileUser


class LanguagesList(models.Model):
    language_name = models.CharField(max_length=100, verbose_name='Название языка')
    language_photo = models.ImageField(upload_to='language_icon/%Y%m%d/', verbose_name='Иконки', blank=True)

    class Meta:
        verbose_name = 'Список языков'
        verbose_name_plural = 'Список языков'
        ordering = ['language_name']

    def __str__(self):
        return self.language_name



#     в профиле нам нужна информация из users
#     - логин
#     - имя
#     - фамилия
#     - емэйл
#     - фото
#     - описание(о себе)
#     - языки (foreign key LanguagesList)
#     - цена
#     - комментарии (поженить с формой)