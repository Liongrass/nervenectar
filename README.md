# Zapshutter

A simple point of sale devices leveraging LNbits' Bitcoin Switch extension.

## Prerequisites:

This guide and the code are optimized for Rasperry Pi OS (Bookworm).

Enable the SPI interface:

`sudo raspi-config`

Then select Interfacing Options -> SPI -> Yes to enable the SPI interface

## Installation:

`git clone https://github.com/Liongrass/zapshutter.git`

`cd zapshutter`

`python -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

## Run Zapshutter:

To run the machine, first copy the example configuration file.

`cp .env.example .env`

Most importantly, a valid websockets URL and LNURL need to be defined.
These can be obtained from the Bitcoin Switch extension on your LNbits instance.
Variables pre-fixed with a `#` sign have defaults and do not need to be set.

`nano .env`

Run the machine:

`python main.py`

## Deploying as a service

To make the code run on startup and restart after a crash, we are using the PM2 utility.

### Install PM2

Prerequisites:

`sudo apt install npm`

`sudo npm install -g pm2`

### Persist Zapshutter

`pm2 start /home/user/zapshutter/main.py --interpreter /home/user/zapshutter/env/bin/python --name zapshutter --exp-backoff-restart-delay=100`

`pm2 startup`

This will give you a short command. Execute it to make Zapshutter run on startup.

Useful commands:

```
pm2 logs zapshutter
pm2 list
pm2 monit
pm2 restart zapshutter
```

### Further documentation

[E-ink display user manual](/docs/3.7inch_e-Paper_Specification.pdf)

[E-ink display circuit schema](/docs/3.7inch_e-Paper_Schematic.pdf)

[Display Guide](/docs/DISPLAY.md)

[Pin Inventory](/docs/pins.ods)
