from django.db import models
from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MALE = 'male', 'Мужчина'
    FEMALE = 'female', 'Женщина'


class Language(models.Model):
    name = models.CharField(verbose_name="Язык", null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


# Create your models here.
class AboutTutor(models.Model):
    birthdate = models.CharField(
        verbose_name='Дата рождения',
        null=True, blank=True,
        max_length=50
    )
    gender = models.CharField(
        choices=GenderChoices.choices,
        default=None,
        verbose_name='Пол',
        null=True,
        blank=True,
        max_length=150
    )
    language = models.ManyToManyField(
        to='cabinet_tutors.Language',
        related_name='languages',
        verbose_name='Язык преподавания',
        blank=False,
    )
    about_me = models.TextField(verbose_name='Коротко о себе', null=True, blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Моя анкета'
