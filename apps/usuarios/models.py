from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    last_name_two = models.CharField(
        _('last name 2'), max_length=30, blank=True)


class Perfil(models.Model):
    pass
