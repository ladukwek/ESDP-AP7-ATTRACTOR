from django.urls import path

from cabinet_tutors.api import save
from cabinet_tutors.views import TutorCabinetView

urlpatterns = [
    path('tutor/<int:pk>/', TutorCabinetView.as_view(), name='tutor_cabinet'),
    path('profile/save/', save, name='divide')
]
