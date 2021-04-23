from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions
from django.urls import path


schema_view = get_schema_view(
   openapi.Info(
      title="Polls' API",
      default_version='v1',
      description="Describes available API for Polls",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pimenovmikhail@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]