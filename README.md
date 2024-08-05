# PowerPico
PowerPico is a bad USB device made from a Raspberry Pi Pico.
All the files needed are in my repo.
This is just for educational purposes.

# How To Make
First, take your Raspberry Pi Pico and plug it into your device while holding the BOOTSEL button.
When it appears on your device, release the button and open the `Flash_Nuke` folder. Copy the `flash_nuke.uf2` file to the Raspberry Pi Pico and wait until it restarts.
Now, open the `CircuitPython` folder and copy `adafruit-circuitpython-raspberry_pi_pico-en_US-9.1.1.uf2` to your Raspberry Pi Pico and wait until it restarts.
After it restarts, it should be named `CIRCUITPY`. Now, copy `adafruit_hid` to your Raspberry Pi Pico's `lib` folder.

Congratulations! PowerPico is ready!

# How To Put A Payload On Your PowerPico
Open the `Payload` folder and choose a folder that you like, then open it and copy `code.py` to your PowerPico and press replace file in the destination.  
*WARNING: The payload will run immediately, so unplug it immediately.*
