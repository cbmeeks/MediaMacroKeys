#	Simple Macro Keyboard in CircuitPython
#	I bought a TKL (Tenkeyless) keyboard.
#	I use this keyboard in a KVM switch and (with Linux), it doesn't support
#	the media keys and the "hot swap" keys at the same time.
#	So I built a small macro keyboard using a Raspberry Pi Pico and a few buttons.
#	This adds back the volume keys and the calculator key.
#	Surprisingly, I've actually started liking the macro keyboard better than
#	the media keys on the keyboard anyway.
#
#	TODO:  Add MUTE button support
#
#	Made in 2022 by Cecil Meeks, cbmeeks@gmail.com
#	Updates in 2023 by Cecil Meeks, cbmeeks@gmail.com
#
import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

KEY_MEDIA_VOLUMEUP		= 0xed
KEY_MEDIA_VOLUMEDOWN	= 0xee
KEY_MEDIA_MUTE			= 0xef
KEY_MEDIA_CALC			= 0xfb

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

# onboard led of Pico
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# colored led
red_led = digitalio.DigitalInOut(board.GP12)
red_led.direction = digitalio.Direction.OUTPUT

grn_led = digitalio.DigitalInOut(board.GP11)
grn_led.direction = digitalio.Direction.OUTPUT

blu_led = digitalio.DigitalInOut(board.GP10)
blu_led.direction = digitalio.Direction.OUTPUT

# setup media keys
key_volume_up = digitalio.DigitalInOut(board.GP19)
key_volume_up.switch_to_input(pull=digitalio.Pull.DOWN)

key_volume_down = digitalio.DigitalInOut(board.GP18)
key_volume_down.switch_to_input(pull=digitalio.Pull.DOWN)

key_calc = digitalio.DigitalInOut(board.GP20)
key_calc.switch_to_input(pull=digitalio.Pull.DOWN)


# loop forever
while True:
    if key_volume_up.value:
        keyboard.send(KEY_MEDIA_VOLUMEUP)
        led.value = True
        red_led.value = True
        blu_led.value = True
        time.sleep(0.1)

    if key_volume_down.value:
        keyboard.send(KEY_MEDIA_VOLUMEDOWN)
        led.value = True
        grn_led.value = True
        time.sleep(0.1)

    if key_calc.value:
        keyboard.send(KEY_MEDIA_CALC)
        led.value = True
        blu_led.value = True
        time.sleep(0.25)		# short pause to "debounce" calc key

    time.sleep(0.1)

    # turn off leds
    led.value = False
    red_led.value = False
    grn_led.value = False
    blu_led.value = False


