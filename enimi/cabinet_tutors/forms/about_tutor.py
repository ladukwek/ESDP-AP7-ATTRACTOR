from django import forms
from django.forms import TextInput, Textarea, Select, CheckboxSelectMultiple, SelectMultiple

from cabinet_tutors.models.about_tutor import AboutTutor


class AboutTutorForm(forms.ModelForm):
    class Meta:
        model = AboutTutor
        fields = ('birthdate', 'gender', 'language', 'about_me')
        widgets = {
            'birthdate': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px; height: 26px;',
                'type': 'date'
            }),
            'gender': Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px;  height: 36px;',
            }),
            'language': SelectMultiple(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px;  height: 90px;',
            }),
            'description': Textarea(attrs={
                'rows': 3,
                'cols': 80,
                'placeholder': 'Опишите публикацию',
                'class': 'border-0 border-top',
                'style': 'padding-right: 150px; outline:0px none transparent; overflow:auto; resize:none',
            }),

        }
