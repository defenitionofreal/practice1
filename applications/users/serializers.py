from rest_framework import serializers
from .models import Сertificate, JwtToken, Nonce


class СertificateSerializer(serializers.ModelSerializer):
    """ Сertificate Serializer """

    class Meta:
        model = Сertificate
        fields = ('id', 'company', 'id_certificate', 'status')


class JwtTokenSerializer(serializers.ModelSerializer):
    """ Сertificate Serializer """

    class Meta:
        model = JwtToken
        fields = ('id', 'company', 'token', 'status', 'field')


class NonceSerializer(serializers.ModelSerializer):
    """ Сertificate Serializer """

    class Meta:
        model = Nonce
        fields = ('id', 'company', 'guid', 'data', 'signed_nonce', 'is_signed', 'nonce')