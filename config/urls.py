from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.conf.urls.static import static
from django.conf import settings



schema_view = get_schema_view(
   openapi.Info(
      title="Arxiv API",
      default_version='developer96',
      description="note",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/account/', include("account.urls")),
    path('api/profile/', include("profiles.urls")),
    path('api/lesson/', include("category.urls")),
    path('api/author/', include("author.urls")),
    path ('api/drf-auth/' , include('rest_framework.urls')),

    path('api/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#####  real@gmail.com
###    12345.