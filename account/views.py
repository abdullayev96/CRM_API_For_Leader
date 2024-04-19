from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import User
from .serializers import *
from .utils import *
from rest_framework.viewsets import ModelViewSet

from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser


class RegisterAPI(GenericAPIView):
      queryset = User.objects.all()
      serializer_class = RegisterSerializer

      def post(self, request):
              try:
                    serializer = self.get_serializer(data=request.data)
                    if serializer.is_valid():
                          serializer.save()
                          send_otp_email.delay(serializer.data['email'])
                          return Response({"status": status.HTTP_201_CREATED})

                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                               "message": "try again It is wrong ",
                               "data": serializer.errors})


              except Exception as e:
                    print(e)


              return Response({"status":"Not Found nothing"})

# class RegisterAPI(APIView):
#       def post(self, request):
#           try:
#              data = request.data
#              serializer = RegisterSerializer(data=data)
#              if serializer.is_valid():
#                 serializer.save()
#                 send_otp_email(serializer.data['email'])
#                 #return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#                 return Response({"status": status.HTTP_201_CREATED,
#                                  "message": "successfully registration check email",
#                                  "data": serializer.data})
#
#              return Response({"status": status.HTTP_400_BAD_REQUEST,
#                               "message": "try again It is wrong ",
#                               "data": serializer.errors})
#
#
#
#
#           except Exception as e:
#                     print(e)
#
#           return Response({"status":status.HTTP_404_NOT_FOUND})
#
#


class VerifyOTPAPI(APIView):

    def post(self, request):
        try:
            data=request.data
            serializer = VerifySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "message": "Try again IT is wrong ",
                                     "data": "Invalid OTP or email"})


                if not user[0].otp != otp:
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "message": "Try again It is wrong ",
                                     "data": "wrong  OTP "})


                user = user.first()
                user.staff = True
                user.save()

                return Response({"status": status.HTTP_201_CREATED,
                                 "message": "Your account activate",
                                 "data": serializer.data})


            return Response({"status": status.HTTP_404_NOT_FOUND})


        except Exception as e:
            print(e)

        return Response({"status": "Not Found nothing"})






def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }



class LoginAPI(APIView):
    def post(self,request):
        try:
           serializer = LoginSerializer(data = request.data)
           if serializer.is_valid():
              email = serializer.validated_data["email"]
              password = serializer.validated_data["password"]

              user = authenticate(request, email=email, password=password)

              data = get_tokens_for_user(user)
              return Response({'data': data})

        except Exception as e:
            print(e)


        return Response({'status': status.HTTP_404_NOT_FOUND})

