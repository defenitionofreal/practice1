import base64
import pprint

from django.views.decorators.csrf import csrf_exempt
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status, serializers, HTTP_HEADER_ENCODING
from ..models import Product, MarkingCode
from ..serializers import ProductSerializer, MarkingCodeSerializer
from rest_framework.test import APIRequestFactory, force_authenticate
from ..apiviews import MarkingCodeViewSet
from django.contrib.auth import get_user_model

from ..utils.codes import fetch_unprinted, mark_as_printed, scan_codes, check_marking_code
from ..utils.exceptions import MyException
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
            company=self.company_1,
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

        self.marking_code_3 = MarkingCode.objects.create(
            company=self.company_1,
            product=self.product_1,
            value='testvalue3',
            status=MarkingCode.SCANNED,
            timestamp_get=datetime.datetime.now(),
            timestamp_circulation=datetime.datetime.now()
        )

        self.marking_code_3 = MarkingCode.objects.create(
            company=self.company_1,
            product=self.product_1,
            value='testvalue4',
            status=MarkingCode.LOST_AFTER,
            timestamp_get=datetime.datetime.now(),
            timestamp_circulation=datetime.datetime.now()
        )

        self.factory = APIRequestFactory()
        self.view = MarkingCodeViewSet.as_view({'get': 'list',
                                                'post': 'create', })

    # def test_get_list(self):
    #    # marking = MarkingCode.objects.all()
    #    # serializer = MarkingCodeSerializer(marking, many=True).data
    # request = self.factory.get(reverse("marking-code:marking-code-list"))
    # response = self.view(request)
    # self.assertEqual(response.data, serializer)
    #    self.assertEqual(MarkingCode.objects.count(), 2)
    # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetch_unprinted_error(self):
        try:
            result = fetch_unprinted(101)
        except MyException as e:
            result = e
        self.assertIsInstance(result, MyException)

    def test_fetch_unprinted_status_changed(self):
        try:
            result = fetch_unprinted(10)
            for item in result:
                self.assertEqual(item.status, 'Отдан на печать')
        except MyException as e:
            result = e
        self.assertNotEqual(type(result), MyException)

    def test_mark_as_printed_error(self):
        try:
            result = mark_as_printed([])
        except MyException as e:
            result = e
        self.assertIsInstance(result, MyException)

    def test_mark_as_printed_status_changed(self):
        try:
            ListOfMark = [1, 2, 3]
            result = mark_as_printed(ListOfMark)
            self.assertEqual(result[0], True)
            changed = MarkingCode.objects.filter(pk__in=ListOfMark)
            for item in changed:
                self.assertEqual(item.status, MarkingCode.SUCCESSFULL)
        except MyException as e:
            result = e
        self.assertNotEqual(type(result), MyException)

    def test_check_marking_code(self):
        try:
            result = check_marking_code('jhfilvuhowiugthoiw')
            self.assertEqual(result, 'not found')

            result = check_marking_code('testvalue')
            self.assertEqual(result, 'ok')
            self.assertEqual(self.marking_code_1.status, MarkingCode.SCANNED)

            result = check_marking_code('testvalue3')
            self.assertEqual(result, 'already scanned')

            result = check_marking_code('testvalue4')
            self.assertEqual(result, 'error')
        except Exception as e:
            print(f"{e}")

    def test_create_todo(self):
        self.client.enforce_csrf_checks = False
        self.client.login(username=self.user_1.username, password=self.user_1.password)
        response = self.client.post(
            '/api/v1/codes/marking-code/scan_codes/',
            data=["sfadljfsdf"],
            content_type="application/json",
        )
        print(response.POST)
        self.assertEqual(200, response.status_code)
