# Modules
import logging
import os
import sys

# Functions and variables
from var import show_display
from waveshare_epd import epd3in7

epd = epd3in7.EPD()

def check_display():
	if show_display == True:
		logging.info("Display is enabled.")
		logging.debug("epd3in7")
	else:
		logging.info("Display is disabled.")

def initialize():
	if show_display == True:
		try:
			logging.info("Starting display init")
			epd.init(0)
		except IOError as e:
			logging.error(e)

def display_overlay(overlay_img):
	if show_display == True:
		epd.display_1Gray(epd.getbuffer(overlay_img))

def display_screen(screen_img):
	if show_display == True:
		epd.display_4Gray(epd.getbuffer_4Gray(screen_img))

def shutdown():
	if show_display == True:
		logging.info("Shutting down screen")
		epd.init(0)
		epd.Clear(0xFF, 0)
		epd3in7.epdconfig.module_exit(cleanup=True)
	exit()