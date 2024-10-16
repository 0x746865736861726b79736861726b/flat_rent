from django.urls import path

from . import views


urlpatterns = [
    path("auth/metamask/", views.MetaMaskLogin.as_view(), name="metamask_login"),
    path("", views.LoginPageView.as_view(), name="login"),
]
