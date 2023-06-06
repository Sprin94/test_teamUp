import string
import random

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def generate_random_string():
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(10))
    return random_string


def answer_validator(value):
    pass


class Test(models.Model):
    login = models.CharField(
        'Логин',
        unique=True,
        max_length=10,
        default=generate_random_string
    )


class TestIQ(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE, related_name='iq_test')
    points = models.IntegerField(
        'Баллы',
        validators=(MinValueValidator(0), MaxValueValidator(50)),
    )
    time = models.DateTimeField(auto_now_add=True)


class TestEQ(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE, related_name='eq_test')
    answer = models.CharField('Ответ', max_length=5)
    time = models.DateTimeField(auto_now_add=True)
