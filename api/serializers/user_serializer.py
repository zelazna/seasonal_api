from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('email', 'password', 'first_name', 'last_name')

    # https://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed/27586289
    def create(self, validated_data):
        """
        @Override
        Args:
            validated_data: the user dictionary data

        Returns:
            User: a user
        """
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, user, validated_data):
        """
        @Override
        Args:
            user: the user user
            validated_data: the user dictionary data

        Returns:
            User: a user
        """
        for attr, value in validated_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()
        return user
