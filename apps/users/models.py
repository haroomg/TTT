from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **estra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **estra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, username, email, name, last_name, password=None, **estra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **estra_fields)
    
    def create_superuser(self, username, email, name, last_name, password=None, **estra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **estra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField("email", max_length=256, unique=True)
    name = models.CharField("name", max_length=50, unique=True)
    last_name = models.CharField("last_name", max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historial = HistoricalRecords()
    objects = UserManager()
    
    class Meta:
        
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def natural_key(self):
        return (self.username)

    def __str__(self):
        return "{0}".format(self.username)