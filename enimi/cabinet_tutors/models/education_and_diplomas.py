from django.db import models


class TutorEducationAndDiplomas(models.Model):
    institution = models.CharField(verbose_name='Учебное заведение', blank=True, null=True, max_length=200)
    speciality = models.CharField(verbose_name='Специальность', blank=True, null=True, max_length=200)
    degree = models.CharField(verbose_name='Полученная степень', blank=True, null=True, max_length=200)

