"""parking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.views import Register,Login,Logout
from parking.views import CreateParkingView,Unparking,GetVehicle
from rest_framework.routers import DefaultRouter
from django.conf import settings

# Swagger imports 
from django.conf.urls import url
from django.urls import re_path
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view  
schema_view = get_swagger_view(title='Parking Lot System API')

# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="RCB Parking Lot System",
        default_version='v1',
        description="Welcome to RCB parking lot",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="#RCBForEver"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'search',GetVehicle)

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('api/', include('rest_framework.urls'),name="api"),
    path('register/', Register.as_view(),name="register"),
    path('login', Login,name="login"),
    path('logout', Logout,name="logout"),
    path('park', CreateParkingView.as_view(),name="parking"),
    path('unpark/', Unparking,name="unparking"),
    path('',include(router.urls))
] 

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
urlpatterns += [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  
]