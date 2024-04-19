from django.db import models
from baseapp.models import BaseModel



class Author(BaseModel):
     full_name = models.CharField(max_length=300, verbose_name="To'liq ism sharifi:")
     bio  = models.TextField()
     job = models.CharField(max_length=200, verbose_name="Kasbi va yonalishi")

     def __str__(self):
         return self.full_name


     class Meta:
          verbose_name = "Avtor haqida_"




