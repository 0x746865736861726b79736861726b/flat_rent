from django.db import models
from tinymce import models as tinymce_models

from common.models import BaseModel
from flat.managers import AvailableFlatManager


class Flat(BaseModel):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    description = tinymce_models.HTMLField()
    is_purchased = models.BooleanField(default=False)

    objects = models.Manager()
    availible = AvailableFlatManager()

    def __str__(self):
        return self.name


class FlatImage(BaseModel):
    image = models.ImageField(upload_to="media/")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.flat.name
