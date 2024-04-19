from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

from .manager import UserManager



class User(AbstractUser):
      username = models.CharField(max_length=300)
      email =  models.EmailField(unique=True, blank=True)
      otp = models.CharField(max_length=6, blank=True, null=True)
      active = models.BooleanField(default=True)
      staff = models.BooleanField(default=False)
      admin = models.BooleanField(default=False)



      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

      objects = UserManager()

      def __str__(self):
          return self.email




      def save(self, *args, **kwargs):
          try:
             if kwargs['password']:
                  self.set_password(kwargs['password'])
          except Exception:
                       pass
          finally:
                super(User, self).save(*args, **kwargs)



      class Meta:
          verbose_name = "Foydalanuvchi_"


