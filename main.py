# Modules
import asyncio
import logging

# Functions and variables
from display import check_display, shutdown
from payments import listener
from screens import make_idlescreen

####### MAIN ########

# The main function is run, showing the idle screen and waiting for incoming payments

async def main():
	try:
		logging.info("Starting Nakamoto's Numinous Nerve Nectar")
		check_display()
		await listener()

	except KeyboardInterrupt:
		shutdown()

asyncio.run(main())