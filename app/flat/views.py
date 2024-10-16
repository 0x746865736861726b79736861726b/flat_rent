from django.views import View
from django.shortcuts import render

from flat.forms import FlatForm


class FlatCreateView(View):
    form_class = FlatForm
    template_name = "flat/create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )
