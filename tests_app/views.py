from rest_framework import generics

from tests_app.serializers import TestEQSerializer, TestIQSerializer, TestSerializer
from tests_app.models import Test, TestIQ, TestEQ


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    lookup_url_kwarg = 'login'
    lookup_field = 'login'


class TestEQCreateAPIView(generics.CreateAPIView):
    serializer_class = TestEQSerializer
    queryset = TestEQ.objects.all()
    lookup_url_kwarg = 'login'


class TestIQCreateAPIView(generics.CreateAPIView):
    serializer_class = TestIQSerializer
    queryset = TestIQ.objects.all()
    lookup_url_kwarg = 'login'
    lookup_field = 'login'
