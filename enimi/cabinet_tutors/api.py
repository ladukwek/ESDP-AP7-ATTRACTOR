from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


def save(request: WSGIRequest, *args, **kwargs):
    date = request.POST.get('date')
    request.user.tutor_module.about_tutor.birthdate = date

    gender = request.POST.get('gender')
    print(gender)
    request.user.tutor_module.about_tutor.gender = gender

    request.user.tutor_module.about_tutor.language.clear()
    languages = request.POST.get('languages').strip('[]').split(',')
    for language in languages:
        request.user.tutor_module.about_tutor.language.add(language.strip('"'))

    about_me = request.POST.get('about_me')
    request.user.tutor_module.about_tutor.about_me = about_me

    request.user.tutor_module.about_tutor.save()

    if request.method == 'POST' and request.body:
        response_data = {
            'success': request.user.tutor_module.about_tutor.birthdate
        }
        response = JsonResponse(response_data)
        response.status_code = 201
    else:
        response_data = {
            'error': 'error'
        }
        response = JsonResponse(response_data)
        response.status_code = 400
    return response
