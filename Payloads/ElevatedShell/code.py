import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Initialize the Keyboard object
keyboard = Keyboard(usb_hid.devices)

# susus
time.sleep(2)


# Open the Start Menu
keyboard.press(Keycode.WINDOWS)  # Windows Key
time.sleep(0.1)
keyboard.release_all()
time.sleep(0.5)

# Type 'cmd' to search for Command Prompt
keyboard.press(Keycode.C)
keyboard.press(Keycode.M)
keyboard.press(Keycode.D)
keyboard.release_all()
time.sleep(0.5)

# Sus
keyboard.press(Keycode.RIGHT_ARROW)
keyboard.release_all()
time.sleep(0.5)

# Susa
keyboard.press(Keycode.DOWN_ARROW)
keyboard.release_all()
time.sleep(0.5)

# Susb
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)

# Susc
keyboard.press(Keycode.LEFT_ARROW)
keyboard.release_all()
time.sleep(1)

# Press Enter to open Command Prompt
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)
