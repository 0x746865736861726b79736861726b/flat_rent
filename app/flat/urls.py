from django.urls import path

from . import views

app_name = "flat"

urlpatterns = [
    path("create/", views.FlatCreateView.as_view(), name="create"),
    path("list/", views.FlatListView.as_view(), name="list"),
    path("<uuid:pk>/detail/", views.FlatDetailView.as_view(), name="detail"),
]
