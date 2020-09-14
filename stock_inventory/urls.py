from django.contrib import admin
from django.urls import path

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
