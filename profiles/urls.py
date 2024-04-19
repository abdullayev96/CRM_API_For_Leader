from django.urls import path
from .views import *



# urlpatterns = [
#           path('<int:pk>', UserProfileAPI.as_view())
# ]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', ProfileAPI, basename='profile'),


urlpatterns = router.urls

