from django.db import models
from tinymce import models as tinymce_models
from base.models import BaseModel


class Flat(BaseModel):
    image = models.ImageField()
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    description = tinymce_models.HTMLField()

    def __str__(self):
        return self.name
