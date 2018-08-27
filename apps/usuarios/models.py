from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    last_name_two = models.CharField(
        _('last name 2'), max_length=30, blank=True)

class Publicacion(models.Model):
	fecha = models.DateTimeField("fecha", auto_now_add=True)
	fecha_modificacion = models.DateTimeField("fecha", auto_now=True)


class Perfil(models.Model):
    pass
