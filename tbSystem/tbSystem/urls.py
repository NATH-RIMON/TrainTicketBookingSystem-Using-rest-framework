
from django.contrib import admin
from django.urls import path,include

from tbcore import urls as tbcore_urls
from tstation import urls as tstation_urls
from tbauth import urls as tbauth_urls
from tbticketService import urls as tbticketService_urls
from tbPlatform import urls as tbPlatform_urls 

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
   path('admin/', admin.site.urls),
   path('tbcore/api/', include(tbcore_urls)),
   path('tstation/api/',include(tstation_urls)),
   path('tbauth/api/',include(tbauth_urls) ),
   path('tbticketService/api/',include(tbticketService_urls) ),
   path('tbPlatform/api/',include(tbPlatform_urls) ),
]


schema_view = get_schema_view(
   openapi.Info(
      title="Train Booking System App API",
      default_version='v1.0.0',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="contact@snippets.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
   path('tbsystem/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('tbsystem/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('tbsystem/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
]

urlpatterns+=swagger_urlpatterns
