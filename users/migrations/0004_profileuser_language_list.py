# Generated by Django 3.1 on 2020-08-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_constructor', '0003_auto_20200817_1922'),
        ('users', '0003_remove_profileuser_language_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='language_list',
            field=models.ManyToManyField(blank=True, null=True, to='site_constructor.LanguagesList'),
        ),
    ]