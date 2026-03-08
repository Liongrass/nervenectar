# Modules
import asyncio
import logging

# Functions and variables
from display import check_display, shutdown
from lnbits import define_switch, get_setup_method, get_switches
from payments import listener
from screens import make_idlescreen

####### MAIN ########

# The main function is run, showing the idle screen and waiting for incoming payments

async def main():
	try:
		logging.info("Starting Zapshutter")
		get_setup_method()
		check_display()
		await listener()

	except KeyboardInterrupt:
		shutdown()

asyncio.run(main())