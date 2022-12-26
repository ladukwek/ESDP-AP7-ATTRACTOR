import json

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers.education_and_diplomas import TutorEducationAndDiplomasSerializer
from cabinet_tutors.models import TutorEducationAndDiplomas


# class IsAllowed(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
#             pk = view.kwargs['pk']
#             post = get_object_or_404(Post, pk=pk)
#             return user == post.author
#         return True


class EducationAndDiplomasView(ModelViewSet):
    # permission_classes = [IsAuthenticated, IsAllowed]
    queryset = TutorEducationAndDiplomas.objects.all()
    serializer_class = TutorEducationAndDiplomasSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     author = request.user
    #     TutorEducationAndDiplomasSerializer.author = author
    #     serializer = TutorEducationAndDiplomasSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(TutorEducationAndDiplomas, pk=pk)
        post_serializer = TutorEducationAndDiplomasSerializer(instance, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
