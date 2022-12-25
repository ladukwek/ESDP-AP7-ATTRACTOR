from django.views.generic import DetailView

from accounts.models import Account
from cabinet_tutors.forms.about_tutor import AboutTutorForm


# Create your views here.
class TutorCabinetView(DetailView):
    template_name = 'tutor_cabinet.html'
    model = Account

    def get(self, request, *args, **kwargs):
        initial_languages_values = [i.get('id') for i in request.user.tutor_module.about_tutor.language.values()]
        self.extra_context = {'about_form': AboutTutorForm(), 'initial_languages': initial_languages_values}
        return super().get(request, *args, **kwargs)
