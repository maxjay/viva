import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
import json
from enum import Enum
from coupon import CouponManager, Coupon, CouponType


class BlockchainConnector:
    def __init__(self):
        load_dotenv()  # Load environment variables
        self.web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        self.web3.eth.account.enable_unaudited_hdwallet_features()
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # Necessary for Ganache

        # Set default account using mnemonic
        self.account = self.web3.eth.account.from_key("0x7b7bf3946dee309d6b891b8341131e5f2e4c7ce431b48e4bab52287998c99357")
        self.web3.eth.default_account = self.account.address
        self.contracts = {}
        for coupon_type in CouponType:
            abi = self.get_ca_abi(coupon_type.name.replace("_", ""))
            self.contracts[coupon_type] = self.web3.eth.contract(address=coupon_type.value, abi=abi)

    def get_contract(self, contract_address, abi):
        """
        Load a contract given an address and ABI.
        """
        return self.web3.eth.contract(address=contract_address, abi=abi)


    def get_ca_abi(self, contract_name):
        if contract_name == "GFG":
            thing = f"build/contracts/{contract_name}.json"
        else:
            thing = f"build/contracts/{contract_name}coupon.json"
        with open(thing) as f:
            contract_data = json.load(f)
            abi = contract_data['abi']
            return abi

    def __getitem__(self, key):
        return self.contracts[key]

    def mint_token(self, coupon):
        contract = self.contracts.get(coupon.type)
        if not contract:
            raise ValueError("Invalid coupon type")

        message = f"{coupon.owner_id}-{coupon.type.name}"
        message_hash = self.web3.keccak(text=message)

        tx = contract.functions.mint(
            coupon.owner_id,
            1,  # Assuming amount is always 1 for simplicity
            self.web3.to_hex(message_hash),
            coupon.signature
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': 200000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.web3.eth.default_account),
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account._private_key)
        tx_hash = self.web


# # Usage Example:
# connector = BlockchainConnector()
# discount_10_contract = connector[CouponType.DISCOUNT_10]
# discount_20_contract = connector[CouponType.DISCOUNT_20]
# free_shipping_contract = connector[CouponType.FREE_SHIPPING]
# bogo_contract = connector[CouponType.BUY_ONE_GET_ONE_FREE]
# burn_address = "0x69D6d9487a2F3d5dbD191203Bcb18C99361A117A"
# tx_hash = connector.mint_token(CouponType.DISCOUNT_10, burn_address, 100000000000000)
# print("Transaction Hash:", tx_hash)
