from django.urls import path
from .views import *


# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register('video', VideoAPI, basename="video"),
#
# urlpatterns = router.urls

#
#
urlpatterns = [
    path("video/", VideoAPI.as_view()),


]