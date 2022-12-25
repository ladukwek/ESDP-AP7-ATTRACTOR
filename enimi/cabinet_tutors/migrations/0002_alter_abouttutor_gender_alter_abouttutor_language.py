# Generated by Django 4.1.4 on 2022-12-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_tutors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouttutor',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужчина'), ('female', 'Женщина')], default=None, max_length=150, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='abouttutor',
            name='language',
            field=models.CharField(blank=True, choices=[('kazakh', 'Казахский'), ('russian', 'Русский'), ('english', 'Английский')], default=None, max_length=150, null=True, verbose_name='Язык преподавания'),
        ),
    ]
