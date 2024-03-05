from django.db import models
from account.models import CustomUser



class UserProfile(models.Model):
     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='profile')
     full_name = models.CharField(max_length=200, verbose_name="To'liq ismi:")
     img = models.ImageField(upload_to="img/", verbose_name="rasm:")
     city = models.CharField(max_length=50, verbose_name="Qayerda yashaysiz:")
     created_at = models.DateField()


     def __str__(self):
         return self.full_name


     class Meta:
          verbose_name = "Foydalanuvchi Profile"



