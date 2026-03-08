# Modules
import logging
import os
from PIL import Image, ImageDraw, ImageFont
import qrcode
from time import sleep

# Functions and variables
from var import currency, coke_animation, fontA, fontB, fontBL, lnurl, picdir, price, suceess_screen_expiry, suggested_wallets
from display import display_overlay, display_screen, epd, initialize
from waveshare_epd import epd3in7

canvas_width = epd3in7.EPD_WIDTH
canvas_height = epd3in7.EPD_HEIGHT

#canvas = Image.new('1', (canvas_width, canvas_height), 'white')

def canvas():
    canvas = Image.new('1', (canvas_width, canvas_height), 'white')
    return canvas

def coordinates(img):
    x_center = (canvas_width - img.width) // 2
    y_center = (canvas_height - img.height) // 2
    qr_offset = 60
    global paste_box
    paste_box = (x_center, y_center + qr_offset, x_center + img.width, y_center + img.height + qr_offset)
    return paste_box

def make_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=1,
        )
    qr.add_data(lnurl.upper())
    qr.make(fit=True)
    global qr_img
    qr_img = qr.make_image(fill_color='black', back_color='white')
    qr_img = qr_img.convert("1")
    qr_coordinates = coordinates(qr_img)
    logging.debug(f"QR coordinates: {qr_coordinates}")
    global qr_width
    qr_width = qr_img.width
    logging.debug(f"QR Code Width: {qr_width}")
    return qr_img

def make_idlescreen(error):
    initialize()
    global idle_img
    #idle_img = Image.open(os.path.join(picdir, '21UP_h.bmp'))
    idle_img = canvas()
    display_screen(idle_img)
    draw = ImageDraw.Draw(idle_img)
    draw.text((140, 20), "Pay with Lightning", font = fontB, anchor="ma")
    display_overlay(idle_img)

    for i in suggested_wallets:
        load_pics(i, 40)
        idle_img.paste(pic_img_s, (35, 70 + suggested_wallets.index(i) * 50))
        draw.text((85, 90 + suggested_wallets.index(i) * 50), i, font = fontA, anchor="lm")
        display_overlay(idle_img)
    if error == False:
        draw.text((140, 215 + 6*40), f"ANY POP", font = fontA, anchor="ma")
        display_overlay(idle_img)
        draw.text((140, 175 + 5*40), f"{price} {currency}", font = fontBL, anchor="ma")
        display_overlay(idle_img)
        make_qrcode()
        idle_img.paste(qr_img, paste_box)
        display_overlay(idle_img)
    else:
        draw.text((140, 205 + 6*40), "CONNECTION ERROR", font = fontB, anchor="ma")

    logging.debug(idle_img)
    display_overlay(idle_img)
    epd.sleep()

def make_success_overlay():
    initialize()
    orig_img = Image.open(os.path.join(picdir, 'tick_200x200.bmp'))
    img = orig_img.resize((qr_width, qr_width))
    logging.debug(f"Overlay coordinates: {coordinates(img)}")
    overlay_img = idle_img
    overlay_img.paste(img, paste_box)
    draw = ImageDraw.Draw(overlay_img)
    #draw.text((140, 205 + 6*40), "Payment Received!", font = fontB, anchor="ma")
    logging.debug(overlay_img)
    logging.debug("Showing success overlay")
    display_overlay(overlay_img)

def load_pics(i, pic_size):
    pic_img = Image.open(os.path.join(picdir, i + '_100x100.bmp'))
    global pic_img_s
    pic_img_s = pic_img.resize((pic_size, pic_size))
    return pic_img_s

def make_confirmation_screen(amount, comment):
    conf_img = canvas()
    draw = ImageDraw.Draw(conf_img)
    draw.text((140, 20), "Payment Received!", font = fontB, anchor="ma")
    display_screen(conf_img)
    #draw.text((20, 80), str(price) + " " + currency, font = fontB, anchor="lm")
    #draw.text((20, 100), str(amount) + " satoshi", font = fontA, anchor="lm")
    if comment != "":
        draw.text((20, 70), "Your comment:", font = fontA, anchor="lm")
        draw.text((20, 95), comment, font = fontA, anchor="lm")
    display_overlay(conf_img)
    sleep(1)
    draw.text((140, 80 + 0*40), "1) OPEN FRIDGE", font = fontB, anchor="ma")
    display_overlay(conf_img)
    sleep(1)
    draw.text((140, 80 + 1*40), "2) PULL BOTTLE", font = fontB, anchor="ma")
    display_overlay(conf_img)
    sleep(1)
    draw.text((140, 80 + 2*40), "3) SIP AND ENJOY", font = fontB, anchor="ma")
    display_overlay(conf_img)
    sleep(1)

    for i in coke_animation:
        load_pics(i, 200)
        conf_img.paste(pic_img_s, (-40 + coke_animation.index(i) * 50, 100 + coke_animation.index(i) * 60))
        display_overlay(conf_img)
        print(conf_img)

    epd.sleep()