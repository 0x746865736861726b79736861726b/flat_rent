from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.FlatCreateView.as_view(), name="create"),
]
