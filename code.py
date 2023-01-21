#	Simple Macro Keyboard in CircuitPython
#	I bought a TKL (Tenkeyless) keyboard.
#	I use this keyboard in a KVM switch and (with Linux), it doesn't support
#	the media keys and the "hot swap" keys at the same time.
#	So I built a small macro keyboard using a Raspberry Pi Pico and a few buttons.
#	This adds back the volume keys and the calculator key.
#	Surprisingly, I've actually started liking the macro keyboard better than
#	the media keys on the keyboard anyway.
#
#	Made in 2022 by cbmeeks@gmail.com
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

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

key_volume_up = digitalio.DigitalInOut(board.GP19)
key_volume_up.switch_to_input(pull=digitalio.Pull.DOWN)

key_volume_down = digitalio.DigitalInOut(board.GP18)
key_volume_down.switch_to_input(pull=digitalio.Pull.DOWN)

key_calc = digitalio.DigitalInOut(board.GP20)
key_calc.switch_to_input(pull=digitalio.Pull.DOWN)


while True:
    if key_volume_up.value:
        keyboard.send(KEY_MEDIA_VOLUMEUP)
        led.value = True
        time.sleep(0.1)

    if key_volume_down.value:
        keyboard.send(KEY_MEDIA_VOLUMEDOWN)
        led.value = True
        time.sleep(0.1)

    if key_calc.value:
        keyboard.send(KEY_MEDIA_CALC)
        led.value = True
        time.sleep(0.1)

    time.sleep(0.1)
    led.value = False


