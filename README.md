# Nakamoto's Numinous Nerve Nectar

A beautiful Coca Cola vending machine serving only ice-cold, glass-bottled liquid candy.

## Prerequisites:

This guide and the code are optimized for Rasperry Pi OS (Bookworm).

Enable the SPI interface:

`sudo raspi-config`

Then select Interfacing Options -> SPI -> Yes to enable the SPI interface.

## Installation:

`git clone https://github.com/Liongrass/nevernectar.git`

`cd nevernectar`

`python -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

## Run Nerve Nectar:

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

### Persist Nerve Nectar

`pm2 start /home/user/nevernectar/main.py --interpreter /home/user/nevernectar/env/bin/python --name nevernectar --exp-backoff-restart-delay=100`

`pm2 startup`

This will give you a short command. Execute it to make Nerve Nectar run on startup.

Useful commands:

```
pm2 logs nevernectar
pm2 list
pm2 monit
pm2 restart nevernectar
```

### Further documentation

[E-ink display user manual](/docs/3.7inch_e-Paper_Specification.pdf)

[E-ink display circuit schema](/docs/3.7inch_e-Paper_Schematic.pdf)

[Display Guide](/docs/DISPLAY.md)

[Pin Inventory](/docs/pins.ods)

### Related Projects

[21UP](/https://github.com/Liongrass/21UP)

[Zapshutter](https://github.com/Liongrass/zapshutter)
