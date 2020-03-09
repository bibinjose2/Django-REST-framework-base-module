from django.db import models

# Create your models here.
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class AuthUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **kwargs):
        if email is None:
            
            raise ValueError(
                'Users must have a username or an email address')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **kwargs)
        if email is not None:
            user.email = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=12, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = AuthUserManager()
    

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.now()
        self.save()
