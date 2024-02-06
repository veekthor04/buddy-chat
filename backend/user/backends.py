from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username=str, password=str, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(str(password)):
                return user
        return None
