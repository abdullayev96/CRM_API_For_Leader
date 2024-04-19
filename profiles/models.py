from django.db import models

from django.conf import settings




class UserProfile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
     full_name = models.CharField(max_length=200, verbose_name="To'liq ismi:")
     number = models.CharField(max_length=20, verbose_name="Telefon nomer:")
     created_at = models.DateTimeField(auto_now_add=True)


     def __str__(self):
         return self.full_name


     class Meta:
          verbose_name = "Foydalanuvchi Profile"



