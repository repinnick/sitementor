# Generated by Django 3.1 on 2020-08-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200824_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]
