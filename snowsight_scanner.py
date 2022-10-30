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
    
    async for websocket in websockets.connect(
        uri="ws://avax.chainsight.dev:8595",
        ping_timeout=none,
    ):

        try:
            await websocket.send(
                json.dumps({"signed_key":
signed_message.signature.hex()})
            )
            resp = json.loads(await websocket.recv())
            print(resp)

            # If currently unathorized, make payment & loop
            if "unauthenticated" in resp["status"]:
                pay_sync()
                continue 

            if resp["status"] == "authenticated":

                while True:

                    tx_message = json.loads(
                        await asyncio.wait_for(
                            websocket.recv(),
                            timeout=30,
                        )
                    )

                    tx_to = tx_message["to"].lower()
                    # Filter for only desiered transactions
                    if tx_to not in [address.lower() for address in 
                                     ROUTERS.keys()]:
                        continue
                    else:
                        func, params = brownie.web3.eth.contract(

address=brownie.web3.toChecksumAddress(tx_to),
                            abi=ROUTERS[tx_to]["abi"],
                        ).decode_function_input(tx_message["input"])

                    # Show tx w/ 'path' arg
                    if params.get("path") in [
                        [cra.address, wavax.address],
                        [wavax.address, cra.address],
                    ]:

                        print()
                        print("=== Pending WAVX-CRA swap ===")
                        print(func.fn_name)
                        print(params)




async def main():


BROWNIE_NETWORK = "moralis-avax-main-websocket"
BROWNIE_ACCOUNT = ""

SNOWSIGHT_CONTRACT_ADDRESS = ""
CRA_CONTRACT_ADDRESS = ""
WAVAX_CONTRACT_ADDRESS = ""
TRADERJOE_LP_CRA_WAVAX_ADDRESS = ""
SNOWTRACE_API_KEY = ""


asyncio.run(main())
