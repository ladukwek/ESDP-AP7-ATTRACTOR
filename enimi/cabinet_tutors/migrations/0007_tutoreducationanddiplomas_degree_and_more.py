# Generated by Django 4.1.4 on 2022-12-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_tutors', '0006_language_alter_abouttutor_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoreducationanddiplomas',
            name='degree',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Полученная степень'),
        ),
        migrations.AddField(
            model_name='tutoreducationanddiplomas',
            name='institution',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Учебное заведение'),
        ),
        migrations.AddField(
            model_name='tutoreducationanddiplomas',
            name='speciality',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Специальность'),
        ),
    ]