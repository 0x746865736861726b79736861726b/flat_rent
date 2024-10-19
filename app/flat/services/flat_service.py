from loguru import logger


class FlatManager:
    def __init__(self, contract_client):
        """
        Initializes a FlatManager instance.

        :param contract_client: A contract client connected to the FlatsContract
        :type contract_client: eth_client.EthClient (your ContractClient)
        """
        self.contract_client = contract_client

    def register_apartment(
        self, name, location, description, price, account, private_key
    ):
        """
        Registers a new apartment with the given details.

        :param str name: The name of the apartment
        :param str location: The location of the apartment
        :param str description: The description of the apartment
        :param int price: The price of the apartment in wei
        :param str account: The Ethereum address of the sender (owner)
        :param str private_key: The private key to use for signing the transaction
        :return: The transaction receipt
        :rtype: dict
        """
        transaction = self.contract_client.build_transaction(
            "registerApartment", [name, location, description, price], account
        )
        receipt = self.contract_client.send_transaction(transaction, private_key)
        return receipt

    def get_apartment_details(self, apartment_id):
        """
        Returns the details of an apartment by its ID.

        :param int apartment_id: The ID of the apartment
        :return: A dictionary containing apartment details:
                 - name
                 - location
                 - description
                 - price
                 - isForSale
        :rtype: dict
        """
        details = self.contract_client.call_function(
            "getApartmentDetails", [apartment_id]
        )

        logger.info(f"Apartment details for ID {apartment_id}: {details}")

        return {
            "name": details[0],
            "location": details[1],
            "description": details[2],
            "price": details[3],
            "isForSale": details[4],
        }

    def get_all_apartments(self):
        """
        Returns all apartments registered in the contract.

        :return: A list of dictionaries, each containing the following keys:
                 - apartment_id
                 - name
                 - location
                 - price
                 - isForSale
        :rtype: list[dict]
        """
        apartments = []

        apartment_ids, names, locations, prices, is_for_sale = (
            self.contract_client.call_function("getAllApartments", [])
        )

        logger.info(
            f"Getting all apartments: {apartment_ids}, {names}, {locations}, {prices}, {is_for_sale}"
        )

        for apartment_id, name, location, price, is_for_sale in zip(
            apartment_ids, names, locations, prices, is_for_sale
        ):
            apartments.append(
                {
                    "apartment_id": apartment_id,
                    "name": name,
                    "location": location,
                    "price": price,
                    "isForSale": is_for_sale,
                }
            )

        return apartments

    def purchase_apartment(self, apartment_id, price, buyer_account, private_key):
        """
        Allows a user to purchase an apartment.

        :param int apartment_id: The ID of the apartment
        :param int price: The price of the apartment (in wei)
        :param str buyer_account: The Ethereum address of the buyer
        :param str private_key: The private key to use for signing the transaction
        :return: The transaction receipt
        :rtype: dict
        """
        transaction = self.contract_client.build_transaction(
            "purchaseApartment", [apartment_id], buyer_account
        )

        # Add value (price) to the transaction
        transaction["value"] = price

        receipt = self.contract_client.send_transaction(transaction, private_key)
        return receipt
