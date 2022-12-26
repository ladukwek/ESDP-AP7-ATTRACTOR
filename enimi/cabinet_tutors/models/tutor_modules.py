from django.contrib.auth import get_user_model
from django.db import models


class TutorModule(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to=get_user_model(),
        related_name='tutor_module',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    about_tutor = models.OneToOneField(
        verbose_name='О себе',
        to='cabinet_tutors.AboutTutor',
        related_name='about_tutor',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    education_and_diplomas = models.ManyToManyField(
        verbose_name='Образование и дипломы',
        to='cabinet_tutors.TutorEducationAndDiplomas',
        related_name='education_and_costs',
    )
    subjects_and_costs = models.ManyToManyField(
        verbose_name='Предметы и стоимость',
        to='cabinet_tutors.SubjectsAndCosts',
        related_name='subjects_and_costs',
    )
    study_formats = models.ManyToManyField(
        verbose_name='Формат обучения',
        to='cabinet_tutors.StudyFormats',
        related_name='study_formats',
    )

    def __str__(self):
        return f'{self.user}'
