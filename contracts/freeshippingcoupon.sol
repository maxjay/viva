// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract FreeShippingCoupon is ERC20 {
    constructor(uint256 initialSupply) ERC20("FreeShippingCoupon", "FreeShippingCoupon") {
        _mint(msg.sender, initialSupply);
    }

    function redeem(uint256 amount) public {
        require(balanceOf(msg.sender) >= amount, "Not enough coupons to redeem");
        _burn(msg.sender, amount);
        emit Redeemed(msg.sender, amount);
    }

    event Redeemed(address indexed user, uint256 amount);
}
