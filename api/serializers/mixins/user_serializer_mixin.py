from rest_framework import serializers

from api.models import User


class UserSerializerMixin(serializers.Serializer):

    # https://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed/27586289
    def create(self, validated_data):
        """
        Args:
            validated_data: the candidate dictionary data

        Returns:
            Instance: a User instance
        """
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User(**user_data)
        if password is not None:
            user.set_password(password)
        user.save()
        instance = self.Meta.model(user=user, **validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Args:
            instance: the candidate instance
            validated_data: the candidate dictionary data

        Returns:
            Instance: a User instance
        """
        for attr, value in validated_data.items():
            if attr == 'user':
                user = instance.user
                for u_attr, u_value in value.items():
                    user.set_password(u_value) if u_attr == 'password' else setattr(user, u_attr, u_value)
                    user.save()
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    # https://stackoverflow.com/questions/12754024/onetoonefield-and-deleting
    def delete(self, *args, **kwargs):
        """
        Args:
            *args: list
            **kwargs: dict

        Returns:
            None ?
        """
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)
