import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Initialize the Keyboard object
keyboard = Keyboard(usb_hid.devices)

# Wait
time.sleep(2)


# Open the Start Menu
keyboard.press(Keycode.WINDOWS)  # Windows Key
time.sleep(0.1)
keyboard.release_all()
time.sleep(0.5)

# Type 'regedit' to search for RegistryEditor
keyboard.press(Keycode.R)
keyboard.press(Keycode.E)
keyboard.press(Keycode.G)
keyboard.press(Keycode.E)
keyboard.press(Keycode.D)
keyboard.press(Keycode.I)
keyboard.press(Keycode.T)
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
time.sleep(1.5)

# Press Enter to open RegistryEditor
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)
