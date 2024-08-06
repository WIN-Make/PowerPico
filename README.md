# PowerPico
PowerPico is a USB device emulating a keyboard using a Raspberry Pi Pico. This guide is for educational purposes only.

# How to Set Up
Prepare Your Raspberry Pi Pico:

Connect the Raspberry Pi Pico to your computer while holding down the BOOTSEL button.
When it appears as a removable storage device, release the BOOTSEL button.
Flash Nuke:

Open the Flash_Nuke folder from the files provided.
Copy the flash_nuke.uf2 file to the Raspberry Pi Pico. Wait until it restarts. This process clears the existing firmware.
Install CircuitPython:

Open the CircuitPython folder.
Copy the adafruit-circuitpython-raspberry_pi_pico-en_US-9.1.1.uf2 file to your Raspberry Pi Pico. Wait until it restarts.
After restarting, the Pico should appear as a drive named CIRCUITPY.
Install Adafruit HID Library:

Open the lib folder on the CIRCUITPY drive.
Copy the adafruit_hid library folder into the lib folder on your Pico.
Congratulations! Your PowerPico is set up and ready to go.

# How to Add a Payload
Prepare the Payload:

Open the Payload folder from the files provided.
Select the desired folder within Payload, then copy code.py from that folder to the root directory of your CIRCUITPY drive on the Pico. Replace any existing code.py file if prompted.
Run the Payload:

WARNING: The payload will execute as soon as the Pico is connected. Ensure you are ready to handle the effects of the payload before plugging it in.
# Payload Converter (BETA)
Convert a Ducky Script:

Open the PayloadConverter (BETA) folder from the files provided.
Paste your Ducky script into payload.txt and save the file.
Run the DD to PY.py script to convert the Ducky script into a code.py file.
Or open PayloadConverterOnline.html and paste your code and click convert to python then download your code.py.

Deploy the Converted Payload:

A code.py file will be created. Copy this file to the root directory of your CIRCUITPY drive on the Pico, replacing any existing code.py.
Execute the Payload:

WARNING: As with direct payloads, the converted payload will run immediately upon connection. Handle with caution.
