# custom authentication backend for authenticating user


from django.contrib.auth.backends import BaseBackend
from Users.models import User
from django.shortcuts import get_object_or_404


class CustomBackend(BaseBackend):

    # over riding default authenticate function
    def authenticate(self, request, username=None, password=None):
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            return user
        else:
            return None
