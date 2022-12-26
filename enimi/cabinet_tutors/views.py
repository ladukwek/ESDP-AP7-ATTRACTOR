from django.views.generic import DetailView

from accounts.models import Account
from cabinet_tutors.forms.about_tutor import AboutTutorForm
from cabinet_tutors.forms.education_and_diplomas import EducationAndDiplomasForm


# Create your views here.
class TutorCabinetView(DetailView):
    template_name = 'tutor_cabinet.html'
    model = Account

    def get(self, request, *args, **kwargs):
        initial_languages_values = [i.get('id') for i in request.user.tutor_module.about_tutor.language.values()]
        education_and_diplomas = [i.get('id') for i in request.user.tutor_module.education_and_diplomas.values()]
        self.extra_context = {
            'about_form': AboutTutorForm(),
            'education_form': EducationAndDiplomasForm(),
            'initial_languages': initial_languages_values,
            'education_and_diplomas': education_and_diplomas,
        }
        return super().get(request, *args, **kwargs)
