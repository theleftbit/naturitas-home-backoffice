import logging

from django.conf import settings

from users.models.naturitas_user import NaturitasUser


def create_superadmin_user():
    logging.getLogger('django').info('Creating superuser')

    if not NaturitasUser.objects.exists_user_with_email(settings.SUPERADMIN_EMAIL):
        NaturitasUser.objects.create_superuser(email=settings.SUPERADMIN_EMAIL, password=settings.SUPERADMIN_PASSWORD)
