from django.shortcuts import render
from django.views.generic import TemplateView

from glossary.models import Term


class GlossaryView(TemplateView):
    template_name = "glossary/glossary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        term = Term.objects.filter(parent=None)[0]
        context["glossary"] = term.to_dict_recursive()
        return context

