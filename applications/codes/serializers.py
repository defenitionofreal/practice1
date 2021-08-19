from rest_framework import serializers
from .models import Product, MarkingCode


class ProductSerializer(serializers.ModelSerializer):
    """ Product Serializer """

    class Meta:
        model = Product
        fields = ('id', 'company', 'title', 'code')

class MarkingCodeSerializer(serializers.ModelSerializer):
    """ Marking Code Serializer """

    class Meta:
        model = MarkingCode
        fields = ('id', 'company', 'product', 'value', 'status', 'timestamp_get', 'timestamp_circulation')

