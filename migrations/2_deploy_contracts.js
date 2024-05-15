const Discount10Coupon = artifacts.require("Discount10Coupon");
const Discount20Coupon = artifacts.require("Discount20Coupon");
const FreeShippingCoupon = artifacts.require("FreeShippingCoupon");
const BuyOneGetOneFreeCoupon = artifacts.require("BuyOneGetOneFreeCoupon");
var gfg = artifacts.require("gfg");

module.exports = function (deployer, accounts) {

  const initialOwnerAddress = accounts;
  const license = "0x5E2861EC76e3649b6b1fa9460B13BBbDFF04e5b0";
  deployer.deploy(Discount10Coupon, license);
  // deployer.deploy(Discount20Coupon, 0);
  // deployer.deploy(FreeShippingCoupon, 0);
  // deployer.deploy(BuyOneGetOneFreeCoupon, 0);
  deployer.deploy(gfg);
};
