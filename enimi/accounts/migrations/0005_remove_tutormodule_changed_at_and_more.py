# Generated by Django 4.1.4 on 2022-12-24 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_tutors', '0001_initial'),
        ('accounts', '0004_account_birthday_account_parent_alter_account_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutormodule',
            name='changed_at',
        ),
        migrations.RemoveField(
            model_name='tutormodule',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tutormodule',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='tutormodule',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='tutormodule',
            name='place_of_study',
        ),
        migrations.RemoveField(
            model_name='tutormodule',
            name='working_place',
        ),
        migrations.AddField(
            model_name='tutormodule',
            name='about_tutor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_tutor', to='cabinet_tutors.abouttutor', verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='tutormodule',
            name='education_and_diplomas',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_and_costs', to='cabinet_tutors.tutoreducationanddiplomas', verbose_name='Образование и дипломы'),
        ),
        migrations.AddField(
            model_name='tutormodule',
            name='study_formats',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_formats', to='cabinet_tutors.studyformats', verbose_name='Формат обучения'),
        ),
        migrations.AddField(
            model_name='tutormodule',
            name='subjects_and_costs',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects_and_costs', to='cabinet_tutors.subjectsandcosts', verbose_name='Предметы и стоимость'),
        ),
    ]