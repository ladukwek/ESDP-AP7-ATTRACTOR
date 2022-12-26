from rest_framework import serializers

from cabinet_tutors.models import TutorEducationAndDiplomas, AboutTutor


class AboutTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTutor
        fields = (
            'id',
            'birthdate',
            'gender',
            'language',
            'about_me'
        )
        read_only_fields = (
            'id',
        )

    # def update(self, instance, validated_data):
    #     instance.birthdate = validated_data.get('birthdate')
    #     instance.gender = validated_data.get('gender')
    #     instance.language = validated_data.get('language')
    #     instance.about_me = validated_data.get('about_me')
    #     instance.save()
    #     return instance

    # def create(self, validated_data, author=None):
    #     about_tutor = AboutTutor.objects.create(**validated_data, author=self.author)
    #     return about_tutor
