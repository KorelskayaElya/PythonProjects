"""api_with_restrictions URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advertisements.views import AdvertisementViewSet

router = DefaultRouter()
# TODO: подключите `AdvertisementViewSet`
router.register('advertisements', AdvertisementViewSet, basename='advertisement')

urlpatterns = [
    path('api/', include((router.urls, 'advertisement'), namespace='advertisement')),
    path('admin/', admin.site.urls),
]
"""
admin 4ac2f4b7cb8d90abd783dbb543deb08846245471
user2 e64d148b7ebfbfceedf90f5b8bd8f2ccc878abd8
user1 3ebf1f1563c9a9636a5da869d065e6c3768f1ceb
superuser password 123 admin panel
"""

