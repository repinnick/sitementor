# Generated by Django 3.1 on 2020-08-17 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_constructor', '0002_auto_20200809_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languageslist',
            options={'ordering': ['language_name'], 'verbose_name': 'Список языков', 'verbose_name_plural': 'Список языков'},
        ),
    ]
