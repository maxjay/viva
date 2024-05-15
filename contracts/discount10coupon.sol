// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Discount10Coupon is ERC20 {
    address public licenser;

    event Minted(address indexed to, uint256 amount);
    event Redeemed(address indexed user, uint256 amount);

    constructor(address _licenser)
        ERC20("Discount10Coupon", "Discount10Coupon")
    {
        licenser = _licenser;
        _mint(msg.sender, 0);
    }

    // Function to redeem coupons
    function redeem(uint256 amount) public {
        require(balanceOf(msg.sender) >= amount, "Not enough coupons to redeem");
        _burn(msg.sender, amount);
        emit Redeemed(msg.sender, amount);
    }

    // Mint function with signature verification
    function mint(address to, uint256 amount, bytes32 messageHash, bytes memory signature) public {
        require(verifySignature(messageHash, signature, licenser), "Invalid signature");
        _mint(to, amount);
        emit Minted(to, amount);
    }

    // Function to verify signatures
    function verifySignature(bytes32 messageHash, bytes memory signature, address expectedSigner) public pure returns (bool) {
        bytes32 r;
        bytes32 s;
        uint8 v;
        (v, r, s) = splitSignature(signature);

        return ecrecover(messageHash, v, r, s) == expectedSigner;
    }

    // Function to split the signature into v, r, and s components
    function splitSignature(bytes memory sig)
        internal
        pure
        returns (uint8 v, bytes32 r, bytes32 s)
    {
        require(sig.length == 65, "Invalid signature length");

        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }

        return (v, r, s);
    }
}
