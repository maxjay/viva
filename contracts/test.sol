// SPDX-License-Identifier: MIT
pragma solidity >=0.5.0 <0.9.0;

contract gfg {
    string public constant name = "GeekToken";
    string public constant symbol = "GFG";
    uint8 public constant decimals = 18;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 amount);

    mapping(address => uint256) balances;

    uint256 totalSupply;

    // Return total supply of the token
    function getTotalSupply() public view returns (uint256) {
        return totalSupply;
    }

    // Return balance of a given account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Mint new tokens to a specified address
    function mint(address to, uint256 amount) public {
        require(to != address(0), "Mint to the zero address");

        totalSupply += amount;
        balances[to] += amount;
        emit Mint(to, amount);
        emit Transfer(address(0), to, amount);
    }

    // Simple message function
    function geeks() public pure returns (string memory) {
        return 'Hey there! I m learning from GeeksForGeeks!';
    }
}
