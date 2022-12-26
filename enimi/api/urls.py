from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views.education_and_diplomas import EducationAndDiplomasView

router = routers.DefaultRouter()
router.register('educations-and-diplomas', EducationAndDiplomasView)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
