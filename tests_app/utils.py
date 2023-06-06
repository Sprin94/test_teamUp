from django.shortcuts import get_object_or_404

from tests_app.models import Test


class TestDefault:
    requires_context = True
    model = Test

    def __call__(self, serializer_field):
        view = serializer_field.context['view']
        login = view.kwargs.get(view.lookup_url_kwarg)
        return get_object_or_404(self.model, login=login)
