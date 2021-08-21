from rest_framework import permissions, viewsets
from .serializers import ProductSerializer, MarkingCodeSerializer
from .models import Product, MarkingCode
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action

from rest_framework.response import Response
import json
from django.core import serializers
from django.http import JsonResponse

from .utils.codes import (
    fetch_unprinted,
    mark_as_printed,
    scan_codes,
)
from .utils.exceptions import MyException


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

    @action(detail=False, methods=['get'])
    def fetch_unprinted(self, request):
        try:
            x = int(request.query_params.get('x'))
            codes = fetch_unprinted(x)
            serializer = MarkingCodeSerializer(codes, many=True)
            return Response(serializer.data)
        except MyException as e:
            return Response({"error": f"""{e}"""})

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def mark_as_printed(self, request):
        result_ok, error_text = mark_as_printed(request.data)
        if result_ok:
            return Response({"result": "success"})
        else:
            return Response({"error": error_text})

    @action(detail=False, methods=['post'])
    def scan_codes(self, request):
        result = scan_codes(request.data)
        if result == 'ok':
            return Response({"status": "ok"})
        elif result == 'not found':
            return Response({"status": "not found"})
        elif result == 'already scanned':
            return Response({"status": "already scanned"})
        else:
            return Response({"status": "Error"})
