from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthBackend(object):
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user and check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
