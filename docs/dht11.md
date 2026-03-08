This device uses a DHT11 barometer.

## Installation

First, edit the firmware configuration:

`sudo nano /boot/firmware/config.txt`

At the very end, amend the following line. Don't forget to replace the GPIO with your own:

`dtoverlay=dht11,gpiopin=4`

Finally, reboot the device to activate the changes.

## Usage

To read the temperature, simply run:

`cat /sys/bus/iio/devices/iio:device0/in_temp_input`

To read the humidity, simply run:

`cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input`

Divide the result by 1000 to get the correct results.

## Troubleshooting

If you are experiencing timeout errors, check the wiring and the pin number.

If you are experiencing I/O errors try running a firmware upgrade:

`sudo rpi-update`

`sudo reboot now`

## Credits

Credits to @peppe9o [and his guide](https://peppe8o.com/raspberry-pi-dht11-sensor/).