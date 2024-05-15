from eth_account import Account
from web3 import Web3

class CouponLicenser:
    def __init__(self, private_key):
        self.private_key = private_key
        self.account = Account.from_key(private_key)
        self.address = self.account.address

    def sign_coupon(self, coupon):
        message = f"{coupon.owner_id}-{coupon.type.name}"
        message_hash = Web3.keccak(text=message)
        signed_message = Account.signHash(message_hash, private_key=self.private_key)
        coupon.signature = signed_message.signature.hex()
        return coupon.signature

    def verify_coupon(self, coupon):
        message = f"{coupon.owner_id}-{coupon.type.name}"
        message_hash = Web3.keccak(text=message)
        recovered_address = Account._recover_hash(message_hash, signature=coupon.signature)
        return recovered_address == self.address
