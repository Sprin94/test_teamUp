from rest_framework.serializers import ModelSerializer, HiddenField, ValidationError, ListField, CharField, SerializerMethodField

from tests_app.models import TestEQ, Test, TestIQ
from tests_app.utils import TestDefault


class TestIQSerializer(ModelSerializer):
    test = HiddenField(default=TestDefault())

    class Meta:
        model = TestIQ
        fields = '__all__'

    def validate(self, attrs):
        test = attrs.get('test')
        if getattr(test, 'iq_test', None):
            raise ValidationError('IQ тест уже добавлен')
        return super().validate(attrs)


class TestEQSerializer(ModelSerializer):
    test = HiddenField(default=TestDefault())
    answer = ListField(child=CharField())

    class Meta:
        model = TestEQ
        fields = '__all__'

    def validate_answer(self, value):
        if value != sorted(set(('а', 'б', 'в', 'г', 'д'))):
            raise ValidationError('Неверный ответ')
        return value

    def validate(self, attrs):
        test = attrs.get('test')
        if getattr(test, 'eq_test', None):
            raise ValidationError('EQ тест уже добавлен')
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['answer'] = ''.join(validated_data['answer'])
        return super().create(validated_data)


class TestSerializer(ModelSerializer):
    eq_test = TestEQSerializer()
    iq_test = TestIQSerializer()

    class Meta:
        model = Test
        fields = ('login', 'eq_test', 'iq_test')
        read_only_fields = ('login', 'eq_test', 'iq_test')
