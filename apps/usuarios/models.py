from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    last_name_two = models.CharField(
        _('last name 2'), max_length=30, blank=True)

class Publicacion(models.Model):
	fecha = models.DateTimeField("fecha", auto_now_add=True)
	fecha_modificacion = models.DateTimeField("fecha", auto_now=True)


class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return "Perfil UID: %d" % self.user_id
