from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from app.flat.models import Flat, FlatImage
from app.flat.forms import FlatForm, FlatImageForm


class FlatCreateView(View):
    form_class = FlatForm
    image_form_class = FlatImageForm
    template_name = "flat/create.html"

    def get(self, request):

        return render(
            request,
            self.template_name,
            {
                "form": self.form_class(),
                "image_form": self.image_form_class(),
            },
        )


class FlatListView(ListView):
    model = Flat
    template_name = "flat/list.html"
    context_object_name = "flats"

    def get_queryset(self):
        return Flat.availible.all()


class FlatDetailView(DetailView):
    model = Flat
    template_name = "flat/detail.html"
    context_object_name = "flat"
