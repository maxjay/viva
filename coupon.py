from enum import Enum

class CouponType(Enum):
    DISCOUNT_10 = "0x48A9671BF094FBD326552998617ffDF3C941Fb93"
    DISCOUNT_20 = "0x0D615710654702550a371b31C3848525562C6BAc"
    FREE_SHIPPING = "0x0B67858D3d0A52D7e3a45CA514D298E4647137F6"
    BUY_ONE_GET_ONE_FREE = "0x86D65ce11F29A976B2F2B74134Bad7ed836B1F95"
    GFG = "0xAdd49b8dB18D5999ACdb734b1C6795952072E6AC"

class Coupon:
    def __init__(self, coupon_type, owner_id, owner_signature=None):
        if not isinstance(coupon_type, CouponType):
            raise ValueError("Invalid coupon type provided.")
        self.type = coupon_type
        self.owner_id = owner_id
        self.owner_signature = owner_signature

    def __repr__(self):
        return f"<Coupon(type={self.type.name}, owner={self.owner_id}, owner_signature={self.owner_signature})>"

class CouponManager:
    def __init__(self, connector, licenser, identity):
        self.coupons = []
        self.blockchain_connector = connector
        self.licenser = licenser
        self.identity = identity

    def add_coupon(self, coupon):
        if not isinstance(coupon, Coupon):
            raise ValueError("Only Coupon instances can be added.")
        if not coupon.owner_signature:
            message = f"{coupon.owner_id}-{coupon.type.name}"
            coupon.owner_signature = self.identity.sign_message(message)
        self.coupons.append(coupon)

    def find_coupons_by_owner(self, owner_id):
        return [coupon for coupon in self.coupons if coupon.owner_id == owner_id]

    def transfer_coupon(self, coupon, new_owner_id):
        if coupon in self.coupons:
            coupon.owner_id = new_owner_id
            message = f"{coupon.owner_id}-{coupon.type.name}"
            coupon.owner_signature = self.identity.sign_message(message)
        else:
            raise ValueError("Coupon does not exist in the manager.")

    def use_coupon(self, owner_id, coupon_type: CouponType):
        coupons = self.find_coupons_by_owner(owner_id)
        for c in coupons:
            if c.type == coupon_type:
                self.coupons.remove(c)
                return c
        raise Exception('Owner does not have specificed coupon')

    def print_balance(self):
        for coupon in self.coupons:
            print(coupon)

    def tokenise_coupon(self, owner_id, coupon_type: CouponType):
        coupon = self.use_coupon(owner_id, coupon_type)
        message = f"{coupon.owner_id}-{coupon.type.name}"
        if not self.identity.verify_message(message, coupon.owner_signature):
            raise ValueError("Invalid owner signature")
        if not self.licenser.verify_coupon(coupon):
            raise ValueError("Invalid coupon signature")
        tx_hash = self.blockchain_connector.mint_token(coupon)
        print(f"Minted coupon: {tx_hash}")

def fill_coupon_manager(coupon_manager):
    # lets have 3 accounts
    coupon_manager.add_coupon(Coupon(CouponType.BUY_ONE_GET_ONE_FREE, '0x5Ae3E212aE49998d942194467857a37f8F9B31Ac'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_10, '0x5Ae3E212aE49998d942194467857a37f8F9B31Ac'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_20, '0x5Ae3E212aE49998d942194467857a37f8F9B31Ac'))
    coupon_manager.add_coupon(Coupon(CouponType.FREE_SHIPPING, '0x5Ae3E212aE49998d942194467857a37f8F9B31Ac'))
    coupon_manager.add_coupon(Coupon(CouponType.BUY_ONE_GET_ONE_FREE, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_10, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_20, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.FREE_SHIPPING, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.BUY_ONE_GET_ONE_FREE, 'b'))


# manager = CouponManager()
# fill_coupon_manager(manager)
# manager.print_balance()