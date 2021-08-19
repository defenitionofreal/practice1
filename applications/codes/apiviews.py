from rest_framework import permissions, viewsets
from .serializers import ProductSerializer, MarkingCodeSerializer
from .models import Product, MarkingCode
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from rest_framework.response import Response
import json
from django.core import serializers
from django.http import JsonResponse


class ProductViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy Product View """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(company_id=user.company)


class MarkingCodeViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy Product View """
    serializer_class = MarkingCodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        return MarkingCode.objects.filter(company_id=user.company)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def fetch_unprinted(self, request):
        pass
