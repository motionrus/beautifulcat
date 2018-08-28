from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Cat


class IndexView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Cat.objects.all()
        return context
