# Generated by Django 3.1 on 2020-08-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profileuser_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='linked_in',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
