from django.urls import path

from tests_app.views import (TestCreateAPIView, TestEQCreateAPIView, TestIQCreateAPIView, TestRetrieveAPIView)

app_name = 'tests'

urlpatterns = [
    path('tests/', TestCreateAPIView.as_view()),
    path('tests/<str:login>/', TestRetrieveAPIView.as_view()),
    path('tests/<str:login>/iq/', TestIQCreateAPIView.as_view()),
    path('tests/<str:login>/eq/', TestEQCreateAPIView.as_view()),
]
