from django.conf import settings

from app.utils.loader import ABImanager
from app.utils.connector import BlockchainConnector
from app.users.services.chain.user_manager import UserManager
from app.common.services.chain.contract_client import ContractClient


def get_user_manager():
    """
    Return an instance of UserManager, which wraps the ContractClient and
    provides services for managing users.
    """
    abi_manager = ABImanager(settings.CONTRACT_ABI_PATH)
    contract_abi = abi_manager.get_abi()
    blockchain_connector = BlockchainConnector(settings.ETHEREUM_NODE_URL)
    contract_client = ContractClient(
        blockchain_connector, settings.CONTRACT_ADDRESS, contract_abi
    )
    return UserManager(contract_client)
