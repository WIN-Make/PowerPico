import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

keyboard.send(Keycode.GUI)
time.sleep(1.0)
keyboard_layout.write("powershell")
time.sleep(1.0)
keyboard.send(Keycode.RIGHT_ARROW)
time.sleep(1.0)
keyboard.send(Keycode.DOWN_ARROW)
time.sleep(1.0)
keyboard.send(Keycode.ENTER)
time.sleep(1.0)
keyboard.send(Keycode.LEFT_ARROW)
time.sleep(1.0)
keyboard.send(Keycode.ENTER)