from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def create_user(self, name, last_name, document, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, last_name, document, email, password, **extra_fields)

    def _create_user(self, name, last_name, document, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            name=name,
            last_name=last_name,
            document=document,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, last_name, document, email, password=None, **extra_fields):
        return self._create_user(name, last_name, document, email, password, True, True, **extra_fields)
