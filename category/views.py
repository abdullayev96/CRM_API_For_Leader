from django.shortcuts import render
from .serializers import *
from .models import *
from account.tasks import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import status
from account.models import User
from rest_framework.viewsets import ModelViewSet
from .permissions import *
from rest_framework.permissions import AllowAny, IsAuthenticated

#
# class VideoAPI(ModelViewSet):
#     queryset = Lessons.objects.all()
#     serializer_class = LessonSerializer
#
#
#
#     def get_permissions(self):
#           permission_classes = []
#           if self.action == 'create':
#                 permission_classes = [AllowAny]
#
#           elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
#                 permission_classes = [IsLoggedInUserOrAdmin]
#
#           elif self.action == 'list' or self.action == 'destroy':
#                 permission_classes = [IsAdminUser]
#
#           return [permission() for permission in permission_classes]

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
#           return Response({"status": status.HTTP_404_NOT_FOUND}


class VideoAPI(ListAPIView):
     queryset = Lessons.objects.all()
     permission_classes = [IsAdminUser]
     serializer_class = LessonSerializer



