from django.urls import path
from .views import *


urlpatterns = [
          path("register/", RegisterAPI.as_view()),
          path("otp/", VerifyOTPAPI.as_view()),
          path("login/", LoginAPI.as_view()),


]


# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register('user', UserProfilesAPI, basename='profile'),
#
#
# urlpatterns += router.urls
