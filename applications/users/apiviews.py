from rest_framework import permissions, viewsets
from .serializers import СertificateSerializer, JwtTokenSerializer, NonceSerializer
from .models import Сertificate, JwtToken, Nonce

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .utils.nonce import save_signed


class СertificateViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy Сertificate View """
    serializer_class = СertificateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        return Сertificate.objects.filter(company_id=user.company)


class JwtTokenViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy JwtToken View """
    serializer_class = JwtTokenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        return JwtToken.objects.filter(company_id=user.company)


class NonceViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy Nonce View """
    serializer_class = NonceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    #queryset = Nonce.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Nonce.objects.filter(company_id=user.company)

    @action(detail=True, methods=['post', 'get'],
            permission_classes=[IsAuthenticated])
    def save_signed(self, request, pk=None):
        save_signed(10, pk)
        return Response({'status': 'Вы создали подпись'})