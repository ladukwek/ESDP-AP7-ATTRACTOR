import json

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers.about_tutor import AboutTutorSerializer
from api.serializers.education_and_diplomas import TutorEducationAndDiplomasSerializer
from cabinet_tutors.models import TutorEducationAndDiplomas, AboutTutor


# class IsAllowed(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
#             pk = view.kwargs['pk']
#             post = get_object_or_404(Post, pk=pk)
#             return user == post.author
#         return True


class AboutTutorView(ModelViewSet):
    # permission_classes = [IsAuthenticated, IsAllowed]
    queryset = AboutTutor.objects.all()
    serializer_class = AboutTutorSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     author = request.user
    #     AboutTutorSerializer.author = author
    #     serializer = TutorEducationAndDiplomasSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(AboutTutor, pk=pk)
        post_serializer = TutorEducationAndDiplomasSerializer(instance, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
