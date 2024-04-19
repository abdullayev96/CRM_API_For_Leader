from django.db import models
from author.models import Author
from baseapp.models import BaseModel
from profiles.models import UserProfile




class Category(BaseModel):
      name = models.CharField(max_length=300, verbose_name="Kategoriya nomi:")

      def __str__(self):
          return self.name

      class Meta:
          verbose_name = "Kategoriya_"


class Videos(BaseModel):
      name = models.CharField(max_length=300, verbose_name="Video nomi:")
      videos = models.FileField(upload_to="video/", verbose_name="Video joylash:")
      text = models.TextField()



      def __str__(self):
          return self.name

      class Meta:
           verbose_name = "Videolar_"


class Lessons(BaseModel):
      category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
      video = models.ManyToManyField(Videos,  related_name='video')
      #author  = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")


      def __str__(self):
          return str(self.category)

      class Meta:
          verbose_name  = "Darslik videolar_"






