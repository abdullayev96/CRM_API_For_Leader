from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import status
from account.models import CustomUser
from rest_framework.viewsets import ModelViewSet
from .permissions import *
from rest_framework.permissions import AllowAny, IsAuthenticated

#
# class VideoAPI(ModelViewSet):
#     queryset = Lessons.objects.all()
#     serializer_class = LessonSerializer
#
#
#     def get_permissions(self):
#        permission_classes = []
#
#        if self.action == 'list':
#           permission_classes  = [IsAdminUser]
#           #permission_classes = [IsLoggedInUserOrAdmin]
#
#        elif self.action == 'update' or self.action == 'destroy':
#          permission_classes = [IsAdminUser]
#
#        return [permission() for permission in permission_classes]
#
# class VideoAPI(ModelViewSet):
#     queryset = Lessons.objects.all()
#     serializer_class = LessonSerializer
#
#     def get_permissions(self):
#           permission_classes = []
#
#           if self.action == 'list':
#               permission_classes = [IsAdminUser]
#                     # permission_classes = [IsLoggedInUserOrAdmin]
#
#           elif self.action == 'update' or self.action == 'destroy':
#               permission_classes = [IsAdminUser]
#
#           return [permission() for permission in permission_classes]
#
#
# #


#
# class VideoAPI(APIView):
#     def get(self, request):
#           try:
#               user = CustomUser.objects.get(username=request.user)
#               if user.is_staff ==True:
#                  video = Lessons.objects.all()
#                  serializers = LessonSerializer(video, many=True, context = {"request":self.request})
#                  return Response({"data": serializers.data})
#
#               elif user.is_staff ==False:
#                    return Response({"data": "Siz to'lovni amalga oshirmagansiz!!! "})
#
#           except Exception as e:
#                     print(e)
#
#           return Response({"status": status.HTTP_404_NOT_FOUND})


class VideoAPI(APIView):
    def get(self, request):
          try:
              video = Lessons.objects.all()
              serializers = LessonSerializer(video, many=True, context = {"request":self.request})
              return Response({"data": serializers.data})

          except Exception as e:
                    print(e)

          return Response({"status": status.HTTP_404_NOT_FOUND})

