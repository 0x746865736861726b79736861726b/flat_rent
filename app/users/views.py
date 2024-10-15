import json

from loguru import logger

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class MetaMaskLogin(View):
    def get(self, request, *args, **kwargs):
        return render(request, "auth/login.html")

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            address = data.get("address")
            signature = data.get("signature")
            message = data.get("message")

            logger.info(
                f"Received data - address: {address}, signature: {signature}, message: {message}"
            )

            user = authenticate(
                request, address=address, signature=signature, message=message
            )

            if user is not None:
                login(request, user)
                return JsonResponse({"success": True})

            return JsonResponse(
                {"success": False, "error": "Invalid credentials"},
                status=401,
            )

        except json.JSONDecodeError as e:
            logger.error("Failed to decode JSON: {}".format(e))
            return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

        except Exception as e:
            logger.error("Unexpected error: {}".format(e))
            return JsonResponse(
                {"success": False, "error": "Unexpected error"}, status=500
            )


class CreateUserView(View):
    template_name = "users/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
