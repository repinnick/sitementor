# Generated by Django 3.1 on 2020-08-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profileuser_linked_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='about_you',
            field=models.TextField(blank=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, verbose_name='Номер телефона (9 цифр)'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='types',
            field=models.CharField(choices=[('M', 'Mentor'), ('S', 'Student'), ('ITS', 'IT-School')], max_length=50, verbose_name='Тип учетной записи'),
        ),
    ]