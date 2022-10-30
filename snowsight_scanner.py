import asyncio
import json
import websockets
import os
import sys
import time
import requests
from brownie import accounts, network, Contract
from pprint import pprint

# Notice functions w/ '_sync' suffix are synchronous.

def pay_sync():
    """
    Retreive data from Snowsight contract. Calculate max payment,
    Submit payment to chainsight
    """

    snowsight_contract = 
brownie.Contract.from_explorer(SNOWSIGHT_CONTRACT_ADDRESS)
    
    block_payment = snowsight_contract.paymentPerBlock() * (
        brownie.chain.height
        + snowsight_contract.maximumPaymentBlocks()
        - snowsight_contract.payments(degenbot.address)[-1]
    )

    snowsight_contract.pay(
        {
            "from": degenbot,
            "value": min(
                block_payment,
                snowsight_contract.CalculateMaxPayment(),
            ),
            "priority_fee": 0,
        }
    )


async def watch_pending_transactions():

    signed_message = degenbot.sign_defunct_message(
        "Sign this message to authenticate your wallet with Snowsight."
    )


async def main():


BROWNIE_NETWORK = "moralis-avax-main-websocket"
BROWNIE_ACCOUNT = ""

SNOWSIGHT_CONTRACT_ADDRESS = ""
CRA_CONTRACT_ADDRESS = ""
WAVAX_CONTRACT_ADDRESS = ""
TRADERJOE_LP_CRA_WAVAX_ADDRESS = ""
SNOWTRACE_API_KEY = ""


asyncio.run(main())
