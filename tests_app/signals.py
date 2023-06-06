from django.dispatch import receiver
from django.db.models.signals import post_save

from tests_app.models import Test, TestIQ, TestEQ


@receiver(post_save, sender=Test)
def create_tests(self, **kwargs):
    if False:
        iq_test = TestIQ.objects.create()
        eq_test = TestEQ.objects.create()
