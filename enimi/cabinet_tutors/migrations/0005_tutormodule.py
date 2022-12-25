# Generated by Django 4.1.4 on 2022-12-24 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cabinet_tutors', '0004_delete_tutormodule'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_tutor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_tutor', to='cabinet_tutors.abouttutor', verbose_name='О себе')),
                ('education_and_diplomas', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_and_costs', to='cabinet_tutors.tutoreducationanddiplomas', verbose_name='Образование и дипломы')),
                ('study_formats', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_formats', to='cabinet_tutors.studyformats', verbose_name='Формат обучения')),
                ('subjects_and_costs', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects_and_costs', to='cabinet_tutors.subjectsandcosts', verbose_name='Предметы и стоимость')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_module', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
