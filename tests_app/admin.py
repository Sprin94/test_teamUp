from django.contrib import admin

from tests_app.models import Test, TestEQ, TestIQ

admin.site.register(Test)
admin.site.register(TestIQ)
admin.site.register(TestEQ)
