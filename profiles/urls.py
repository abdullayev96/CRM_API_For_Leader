from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', ProfileAPI, basename='profile'),


urlpatterns = router.urls

##### buy@gmail.com
#### 12345
