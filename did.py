from eth_account import Account
from web3 import Web3

class DigitalIdentity:
    def __init__(self, private_key):
        self.private_key = private_key
        self.account = Account.from_key(private_key)
        self.address = self.account.address

    def sign_message(self, message):
        message_hash = Web3.keccak(text=message)
        signed_message = Account.signHash(message_hash, private_key=self.private_key)
        return signed_message.signature.hex()

    def verify_message(self, message, signature):
        message_hash = Web3.keccak(text=message)
        recovered_address = Account.recoverHash(message_hash, signature=signature)
        return recovered_address == self.address