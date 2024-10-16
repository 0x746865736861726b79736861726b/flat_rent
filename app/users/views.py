import json

from loguru import logger

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect

from users.factory import get_user_manager
from users.services.auth.auth import MetaMaskAuthService


@method_decorator(csrf_exempt, name="dispatch")
class MetaMaskLogin(View):

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            result = MetaMaskAuthService.authenticate_and_login(data, request)

            if result.get("success"):
                return JsonResponse({"success": True, "redirect_url": "/dashboard/"})

            return JsonResponse(result, status=401)

        except json.JSONDecodeError as e:
            logger.error("Failed to decode JSON: {}".format(e))
            return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

        except Exception as e:
            logger.error("Unexpected error: {}".format(e))
            return JsonResponse(
                {"success": False, "error": "Unexpected error"}, status=500
            )


class LoginPageView(View):
    template_name = "auth/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserListView(View):
    def get(self, request):
        """
        GET request handler.

        Returns a rendered page with a list of all users in the UsersContract.
        """
        user_manager = get_user_manager()
        users = user_manager.get_all_users()

        return render(
            request,
            "users/list.html",
            {
                "users": users,
            },
        )
