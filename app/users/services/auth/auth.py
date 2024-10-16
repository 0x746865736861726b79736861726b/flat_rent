from loguru import logger
from django.contrib.auth import authenticate, login


class MetaMaskAuthService:
    @staticmethod
    def authenticate_and_login(data, request):
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
            return {"success": True}
        return {"success": False, "error": "Invalid credentials"}
