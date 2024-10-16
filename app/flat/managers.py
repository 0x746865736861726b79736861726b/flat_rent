from django.db import models


class AvailableFlatManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_purchased=False)
