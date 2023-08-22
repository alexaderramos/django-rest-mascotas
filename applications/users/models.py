from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    document = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # no obligatory
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # rol fields
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_created=True, default=timezone.now, verbose_name='Fecha creación')
    updated_at = models.DateTimeField(auto_now=True)

    # field to auth by default
    USERNAME_FIELD = 'email'

    # field required
    REQUIRED_FIELDS = ['name', 'last_name', 'document']

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.get_full_name() + ' - ' + self.email)

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name + ' ' + self.last_name
