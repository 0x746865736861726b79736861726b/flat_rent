from web3 import Web3
from loguru import logger
from eth_account.messages import encode_defunct

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()
w3 = Web3()


class MetaMaskBackend(BaseBackend):
    def authenticate(self, request, address=None, signature=None, message=None):
        if not address or not signature or not message:
            logger.warning("Missing required fields in authentication request")
            return None
        try:
            message_encoded = encode_defunct(text=message)
            signer = w3.eth.account.recover_message(
                message_encoded, signature=signature
            )

            if signer.lower() != address.lower():
                logger.warning("Signature verification failed")
                return None

            user, created = User.objects.get_or_create(public_key=address)
            return user
        except Exception as e:
            logger.error("Error during signature verification: {}".format(e))
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            logger.warning("User does not exist")
            return None
