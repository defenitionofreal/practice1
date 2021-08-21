from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status, serializers
from ..models import Nonce
from ..serializers import NonceSerializer
from rest_framework.test import APIRequestFactory
from ..apiviews import NonceViewSet
from django.contrib.auth import get_user_model
from ...users.models import Company
from ..utils.nonce import save_signed
import datetime
import base64
import pytest

client = APIClient()
auth_headers = {
           'HTTP_AUTHORIZATION': 'Basic ' +
                base64.b64encode(b'username:password').decode("ascii")
       }
from django.contrib import auth
user = auth.get_user(client)
User = get_user_model()

#NONCE_SAVE_SIGN_URL = reverse('users:nonce-detail/pk/save_signed/')


def test_save_signed(self):
    """ test save_signed method """
    try:
        result = save_signed(5, 1)
        self.assertEqual(result, 'Вы создали подпись')
    except Exception as e:
        result = e
        self.assertEqual(result, Exception)


class NonceAPITest(APITestCase):

    def setUp(self):
        self.company_1 = Company.objects.create(
            title='yandex'
        )

        self.user_1 = User.objects.create(
            username='testuser',
            company=self.company_1
        )

        self.nonce_1 = Nonce.objects.create(
            company=self.company_1,
            guid='some',
            data='some',
            signed_nonce=b'',
            nonce=b'20',
            is_signed=True,
            created_date=datetime.datetime.now()
        )

        self.nonce_2 = Nonce.objects.create(
            company=self.company_1,
            guid='some2',
            data='some2',
            signed_nonce=b'',
            nonce=b'20',
            is_signed=True,
            created_date=datetime.datetime.now()
        )

        self.factory = APIRequestFactory()
        self.view = NonceViewSet.as_view({'get': 'list',
                                         'post': 'create', })

    def test_get_list(self):
        response = client.get(reverse('users:nonce-list'))
        nonces = Nonce.objects.filter(company_id=self.user.company)
        serializer = NonceSerializer(nonces, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #marking = MarkingCode.objects.all()
        #serializer = MarkingCodeSerializer(marking, many=True).data
        #request = self.factory.get(reverse("marking-code:marking-code-list"))
        #response = self.view(request)
        #self.assertEqual(response.data, serializer)
        #self.assertEqual(Nonce.objects.count(), 2)
        #self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_save_signed(self):
    #     """ test save_signed method """
    #     payload = {
    #
    #     }
    #     nonce = Nonce.objects.all()
    #     self.assertEqual(
    #         nonce.save_signed(),
    #     )


