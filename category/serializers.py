from rest_framework import serializers
from .models import *
from author.models import Author



class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model = Category
          fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
     class Meta:
          model = Author
          fields = ['full_name', 'bio', 'job']


class VideoSerializer(serializers.ModelSerializer):
     class Meta:
          model = Videos
          fields = ['name', 'videos']




class LessonSerializer(serializers.ModelSerializer):
     video = VideoSerializer(many=True)
     category = CategorySerializer()

     class Meta:
          model = Lessons
          fields = ['id', 'category', 'video']


