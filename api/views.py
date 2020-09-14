from django.views.generic import TemplateView

from django.shortcuts import render

from rest_framework import viewsets

from .serializers import (
    ItemSerializer,
)

from .models import (
    Item,
)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
