from api.models import Candidate, User
from api.serializers import UserSerializer
from rest_framework import serializers


class CandidateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = (
            'user',
            'year_exp',
            'available_at',
            'profile_view_count',
            'wage_claim',
            'profile_picture_url',
            'description',
            'job'
        )

    # https://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed/27586289
    def create(self, validated_data):
        """
        @Override
        Args:
            validated_data: the candidate dictionary data

        Returns:
            Candidates: a list a candidates
        """
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User(**user_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return Candidate.objects.create(user=user, **validated_data)

    # TODO
    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user')
    #     for attr, value in user_data.items():
    #         if attr == 'password':
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, attr, value)
    #     instance.save()
    #     return instance
