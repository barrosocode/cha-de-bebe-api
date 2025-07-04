"""
URL configuration for cha_de_bebe_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from app.api import viewsets
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'users', viewsets.UserViewSet, basename='users')
router.register(r'convidados', viewsets.ConvidadoViewSet, basename='convidados')
router.register(r'mensagens', viewsets.MensagemViewSet, basename='mensagens')
router.register(r'tamanhos', viewsets.TamanhoViewSet, basename='tamanhos')
router.register(r'fraldas', viewsets.FraldaViewSet, basename='fraldas')
router.register(r'fraldasConvidados', viewsets.Fralda_ConvidadoViewSet, basename='fraldasConvidados')
router.register(r'presentes', viewsets.PresenteViewSet, basename='presentes')
router.register(r'presentesConvidados', viewsets.Presente_ConvidadoViewSet, basename='presentesConvidados')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token, name='obtain_token'),
    path('', include(router.urls))
]
