from django import forms
from tinymce.widgets import TinyMCE

from flat.models import Flat


class FlatForm(forms.ModelForm):
    image = forms.ImageField()
    name = forms.CharField(max_length=256)
    address = forms.CharField(max_length=256)
    description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Flat
        fields = ["name", "address", "description"]
