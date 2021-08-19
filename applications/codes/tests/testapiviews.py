from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status, serializers
from ..models import Product, MarkingCode
from ..serializers import ProductSerializer, MarkingCodeSerializer
from rest_framework.test import APIRequestFactory
from ..apiviews import MarkingCodeViewSet
from django.contrib.auth import get_user_model
from ...users.models import Company
import datetime
import pytest

User = get_user_model()

class MarkingCodeAPITest(APITestCase):

    def setUp(self):
        self.company_1 = Company.objects.create(
            title='yandex'
        )

        self.user_1 = User.objects.create(
            username='testuser',
            company=self.company_1
        )

        self.product_1 = Product.objects.create(
            company=self.company_1,
            title='Yandex Station',
            code='code123'
        )

        self.marking_code_1 = MarkingCode.objects.create(
            company=self.company_1,
            product=self.product_1,
            value='testvalue',
            status=MarkingCode.SENT,
            timestamp_get=datetime.datetime.now(),
            timestamp_circulation=datetime.datetime.now()
        )

        self.marking_code_2 = MarkingCode.objects.create(
            company=self.company_1,
            product=self.product_1,
            value='testvalue2',
            status=MarkingCode.SENT,
            timestamp_get=datetime.datetime.now(),
            timestamp_circulation=datetime.datetime.now()
        )

        self.factory = APIRequestFactory()
        self.view = MarkingCodeViewSet.as_view({'get': 'list',
                                         'post': 'create', })

    def test_get_list(self):
        #marking = MarkingCode.objects.all()
        #serializer = MarkingCodeSerializer(marking, many=True).data
        #request = self.factory.get(reverse("marking-code:marking-code-list"))
        #response = self.view(request)
        #self.assertEqual(response.data, serializer)
        self.assertEqual(MarkingCode.objects.count(), 2)
        #self.assertEqual(response.status_code, status.HTTP_200_OK)


