from rest_framework import serializers

from cabinet_tutors.models import TutorEducationAndDiplomas


class TutorEducationAndDiplomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorEducationAndDiplomas
        fields = (
            'id',
            'institution',
            'speciality',
            'degree'
        )
        read_only_fields = (
            'id',
        )

    def update(self, instance, validated_data):
        instance.institution = validated_data.get('institution')
        instance.speciality = validated_data.get('speciality')
        instance.degree = validated_data.get('degree')
        instance.save()
        return instance

    def create(self, validated_data, author=None):
        tutorEducationAndDiplomas = TutorEducationAndDiplomas.objects.create(**validated_data, author=self.author)
        return tutorEducationAndDiplomas
