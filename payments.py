# Modules
import asyncio
import logging
import websockets
from time import sleep

# Functions and variables
from display import shutdown
from lnbits import get_payments
from screens import make_confirmation_screen, make_idlescreen, make_success_overlay
from trigger import pulse
from var import error, suceess_screen_expiry, ws_switch

####### VARIABLES ########


async def listener():
    logging.info(f"Listening on {ws_switch}")

async def listener():
    while True:
        global error
        try:
            async with websockets.connect(ws_switch) as websocket:
                logging.info(f"Connected to {ws_switch}. Listening for incoming payments.")
                error = False
                print(f"Setting ERROR to False")
                make_idlescreen(error)
                response_str = await websocket.recv()
                print(response_str)
                response = response_str.split("-")
                pin = response[0]
                duration = int(response[1])
                # Check for a comment
                global comment
                try:
                    response[2]
                except IndexError:
                    comment = ""
                    logging.debug("No comment submitted.")
                else:
                    comment = response[2]
                logging.debug(f"Incoming message: {response}")
                amount = get_payments()
                make_success_overlay()
                pulse(pin, duration)
                logging.debug(f"Waiting {suceess_screen_expiry}s")
                sleep(suceess_screen_expiry)
                make_confirmation_screen(amount, comment)
                logging.debug(f"Waiting {suceess_screen_expiry}s")
                sleep(suceess_screen_expiry)
        except websockets.exceptions.WebSocketException as e: 
            logging.error(f"ERROR: {e}")
            if error == False:
                error = e
                make_idlescreen(error)
            sleep(suceess_screen_expiry)
        except asyncio.CancelledError:
            shutdown()