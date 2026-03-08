# Modules
import logging
from gpiozero import OutputDevice
from time import sleep

# Functions and variables
from var import production

def pulse(pin, duration):
	device = OutputDevice(pin, active_high=production, initial_value=False)
	device.on()
	logging.info(f"Triggering pin {pin}")
	logging.debug(f"waiting {duration/1000}s")
	sleep(duration/1000)
	device.off()
	logging.info(f"Done triggering pin {pin}")