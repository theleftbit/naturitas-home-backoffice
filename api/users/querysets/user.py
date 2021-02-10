from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """

        user = self.model(**kwargs)

        if 'password' in kwargs:
            user.set_password(kwargs['password'])
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs["is_staff"] = True

        return self.create_user(**kwargs)

    def exists_user_with_email(self, email):
        return self.filter(email=email).exists()
