from coupon import CouponManager, Coupon, CouponType
from tokeniser import BlockchainConnector
from enum import Enum
from coupon_licenser import CouponLicenser

coupon_type_to_ca = {
    CouponType.DISCOUNT_10: "0x48A9671BF094FBD326552998617ffDF3C941Fb93",
    CouponType.DISCOUNT_20: "0x0D615710654702550a371b31C3848525562C6BAc",
    CouponType.BUY_ONE_GET_ONE_FREE: "0x0B67858D3d0A52D7e3a45CA514D298E4647137F6",
    CouponType.FREE_SHIPPING: "0x86D65ce11F29A976B2F2B74134Bad7ed836B1F95",
    CouponType.GFG: "0xAdd49b8dB18D5999ACdb734b1C6795952072E6AC"
}

def fill_coupon_manager(coupon_manager):
    # lets have 3 accounts
    coupon_manager.add_coupon(Coupon(CouponType.BUY_ONE_GET_ONE_FREE, '0x98B584235012375da3A57dE1A7a4A4BE591F1481'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_10, '0x98B584235012375da3A57dE1A7a4A4BE591F1481'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_10, '0x98B584235012375da3A57dE1A7a4A4BE591F1481'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_20, '0x98B584235012375da3A57dE1A7a4A4BE591F1481'))
    coupon_manager.add_coupon(Coupon(CouponType.FREE_SHIPPING, '0x98B584235012375da3A57dE1A7a4A4BE591F1481'))
    coupon_manager.add_coupon(Coupon(CouponType.BUY_ONE_GET_ONE_FREE, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_10, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.DISCOUNT_20, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.FREE_SHIPPING, 'b'))
    coupon_manager.add_coupon(Coupon(CouponType.BUY_ONE_GET_ONE_FREE, 'b'))

# Initialize the BlockchainConnector and CouponLicenser
private_key = "0x7b7bf3946dee309d6b891b8341131e5f2e4c7ce431b48e4bab52287998c99357"
licenser = CouponLicenser(private_key)
connector = BlockchainConnector()

# Initialize the CouponManager
manager = CouponManager(connector=connector, licenser=licenser)

# Fill the CouponManager with some coupons
fill_coupon_manager(manager)
manager.print_balance()
# Tokenize a coupon
manager.tokenise_coupon('0x98B584235012375da3A57dE1A7a4A4BE591F1481', CouponType.DISCOUNT_10)
