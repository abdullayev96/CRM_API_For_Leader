from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from account.models import User
from rest_framework.generics import RetrieveUpdateAPIView



class ProfileAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
       permission_classes = []
       if self.action == 'create':
          permission_classes = [AllowAny]

       elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
          permission_classes = [IsLoggedInUserOrAdmin]

       elif self.action == 'list' or self.action == 'destroy':
         permission_classes = [IsAdminUser]

       return [permission() for permission in permission_classes]




# class UserProfileAPI(RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     queryset = CustomUser.objects.all()
#     permission_classes = [IsAdminUser]
#
#     def get_object(self):
#         return self.request.user