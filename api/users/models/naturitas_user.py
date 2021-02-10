from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.querysets.user import UserManager


class NaturitasUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
