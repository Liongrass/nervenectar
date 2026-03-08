# Waveshare e-ink display

The 21UP machine uses a 3.52in e-ink display. The display can show a 480x280px image in white, black and red.

To show an image the machine would like to be presented with two BMP files in 1-bit mode, one for red, and one for black. All colors always have to be defined, even if they are not used in the final image. It takes about ~18s to show any image, and this cannot be sped up. This represents the primary frustrating with using the e-ink display.

The device supports a "partial refresh," which can be very useful when speed is an issue. However, the device is not properly wiped, meaning this should be tested thoroughly and cannot always be relied on.

The display consumes the following pins: `3.3V, GND, 10, 11, 8, 25, 17, 24`

## Prepare an image

To make suitable BMP images, I have found both [Gimp](https://www.gimp.org) and the python Pillow library useful.

### Python

In python we can use the function `img = img.convert("1")` in Pillow to convert any image to 1-bit format. As long as the canvas is a 480x280px frame, the e-ink screen should display it. We can also use the `Image.new` function to make a new image in 1-bit format, or load a bmp from disk.

```python
from PIL import Image
from waveshare_epd import epd3in52b

canvas = Image.new('1', (canvas_width, canvas_height), 'white')
UPForeverB = Image.open(os.path.join(picdir, '21UP_b.bmp'))

epd.display(epd.getbuffer(UPForeverB), epd.getbuffer(canvas))
```

### Gimp

In Gimp, you can change the color mode of any image to 1-bit by selecting Image > Mode > Indexed, then choose "Use black and white (1-bit) palette". 

I achieved the best results by generating a black/white image first, then applying the 1-bit index and not applying dithering at all. With dithering, my images always appeared grainy, no matter what I did.

Remember that you will have to generate two images, one where black represents black, and another where black represents red. Black and Red may overlap.

Finally, export your file as a `.bmp` file.

### Magick

## Install Magick

On a Raspberry Pi Magick has to be installed from source

`sudo apt install libjpeg62-turbo-dev:armhf libjpeg62-turbo-dev`
`sudo apt install libtiff-dev `

`git clone https://github.com/ImageMagick/ImageMagick.git`
`cd ImageMagick`
`./configure`
`make`
`sudo make install`
`sudo ldconfig /usr/local/lib`

## Use Magick

I also made experiences with [Magick](https://imagemagick.org), [this guide](https://learn.adafruit.com/preparing-graphics-for-e-ink-displays/command-line) and the following command:

`magick input.jpg -dither FloydSteinberg -define dither:diffusion-amount=85% -remap eink-2color.png -type truecolor -size 480x280 BMP3:output.bmp`
`magick 21UP_4G.png -dither FloydSteinberg -define dither:diffusion-amount=85% -remap eink___epaper_eink-4gray.png -type truecolor -size 280x480 BMP3:21UP_4G.bmp`
`magick 21UP_4G.png -remap eink___epaper_eink-4gray.png BMP3:21UP_4G.bmp`
