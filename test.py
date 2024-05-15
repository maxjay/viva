
# Python program to call the 
# smart contract
import json
from web3 import Web3, HTTPProvider
 
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
 
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address)) 
 
web3.eth.defaultAccount = web3.eth.accounts[0]
 
# Setting the default account (so we don't need 
#to set the "from" for every transaction call)
 
# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/gfg.json'
 
# Deployed contract address (see `migrate` command output: 
# `contract address`)
# Do Not Copy from here, contract address will be different 
# for different contracts.
deployed_contract_address = '0x0D615710654702550a371b31C3848525562C6BAc'
 
# load contract info as JSON
with open(compiled_contract_path) as file:
    contract_json = json.load(file)  
     
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']
 
# Fetching deployed contract reference
contract = web3.eth.contract(
    address = deployed_contract_address, abi = contract_abi)
 
# Calling contract function (this is not persisted 
# to the blockchain)
output = contract.functions.geeks().call()
 
print(output)
