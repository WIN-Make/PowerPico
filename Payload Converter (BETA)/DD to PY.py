import time
import re

# Mapping Ducky Script commands to Adafruit HID Keycode
keycode_map = {
    "ENTER": "Keycode.ENTER",
    "GUI": "Keycode.GUI",
    "SHIFT": "Keycode.SHIFT",
    "CTRL": "Keycode.CONTROL",
    "ALT": "Keycode.ALT",
    "TAB": "Keycode.TAB",
    "ESC": "Keycode.ESCAPE",
    "SPACE": "Keycode.SPACEBAR",
    "DELETE": "Keycode.DELETE",
    "BACKSPACE": "Keycode.BACKSPACE",
    "UP": "Keycode.UP_ARROW",
    "DOWN": "Keycode.DOWN_ARROW",
    "LEFT": "Keycode.LEFT_ARROW",
    "RIGHT": "Keycode.RIGHT_ARROW",
    "CAPSLOCK": "Keycode.CAPS_LOCK",
    "F1": "Keycode.F1",
    "F2": "Keycode.F2",
    "F3": "Keycode.F3",
    "F4": "Keycode.F4",
    "F5": "Keycode.F5",
    "F6": "Keycode.F6",
    "F7": "Keycode.F7",
    "F8": "Keycode.F8",
    "F9": "Keycode.F9",
    "F10": "Keycode.F10",
    "F11": "Keycode.F11",
    "F12": "Keycode.F12",
    "NUMLOCK": "Keycode.NUM_LOCK",
    "SCROLLLOCK": "Keycode.SCROLL_LOCK",
    "SPACEBAR": "Keycode.SPACEBAR",
    # Add more mappings as needed
}

# Define mappings for custom commands
custom_command_map = {
    "DEFINE": "# Custom command DEFINE placeholder",
    "ATTACK_F": "# Custom command ATTACK_F placeholder",
    "ATTACK_T": "# Custom command ATTACK_T placeholder",
    "ATTACK_R": "# Custom command ATTACK_R placeholder",
    "ATTACK_RC": "# Custom command ATTACK_RC placeholder",
    "SET-MPPREFERENCE": "# Custom command SET-MPPREFERENCE placeholder",
    "NEW-ITEMPROPERTY": "# Custom command NEW-ITEMPROPERTY placeholder",
    "REMOVE-ITEM": "# Custom command REMOVE-ITEM placeholder",
    "GET-PSREADLINEOPTION": "# Custom command GET-PSREADLINEOPTION placeholder",
    "WINDOWS-SICHERHEIT": "# Custom command WINDOWS-SICHERHEIT placeholder",
    "VAR": "# Custom command VAR placeholder",
    "CLEAN": "# Custom command CLEAN placeholder",
    "ATTACKMODE": "# Custom command ATTACKMODE placeholder",
    "STRINGLN": "# Custom command STRINGLN placeholder",
    "IF": "# Custom command IF placeholder",
    "ELSE": "# Custom command ELSE placeholder",
    "END_IF": "# Custom command END_IF placeholder",
    "END_FUNCTION": "# Custom command END_FUNCTION placeholder",
    "FUNCTION": "# Custom command FUNCTION placeholder",
    "ENDFUNCTION": "# Custom command ENDFUNCTION placeholder",
    "CALL": "# Custom command CALL placeholder",
}

def convert_ducky_to_python(ducky_script):
    python_script = [
        "import time",
        "import usb_hid",
        "from adafruit_hid.keyboard import Keyboard",
        "from adafruit_hid.keycode import Keycode",
        "from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS",
        "",
        "# Initialize the keyboard",
        "keyboard = Keyboard(usb_hid.devices)",
        "keyboard_layout = KeyboardLayoutUS(keyboard)",
        ""
    ]

    def parse_keycode(key):
        return keycode_map.get(key.upper(), f'Keycode.{key.upper()}')

    def parse_keys(parts):
        return ', '.join(parse_keycode(part) for part in parts)

    lines = ducky_script.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0].upper()

        if command == "DELAY":
            delay_time = int(parts[1]) / 1000.0
            python_script.append(f"time.sleep({delay_time})")
        
        elif command == "STRING":
            string_content = ' '.join(parts[1:])
            python_script.append(f'keyboard_layout.write("{string_content}")')
        
        elif command == "REM":
            # REM is a comment in Ducky Script
            comment_content = ' '.join(parts[1:])
            python_script.append(f"# {comment_content}")
        
        elif command in keycode_map:
            keys_str = parse_keys(parts)
            python_script.append(f"keyboard.send({keys_str})")
        
        elif command in custom_command_map:
            # Placeholder for custom command handling
            python_script.append(custom_command_map[command])
        
        elif command == "IF":
            condition = ' '.join(parts[1:])
            python_script.append(f"if {condition}:")
        
        elif command == "ELSE":
            python_script.append("else:")
        
        elif command == "ENDIF":
            python_script.append("# End of IF block")
        
        elif command == "FUNCTION":
            function_name = ' '.join(parts[1:])
            python_script.append(f"def {function_name}:")
        
        elif command == "ENDFUNCTION":
            python_script.append("# End of function")
        
        elif command == "CALL":
            function_name = ' '.join(parts[1:])
            python_script.append(f"{function_name}()")
        
        else:
            # Handling other key presses and combinations
            keys_str = parse_keys(parts)
            python_script.append(f"keyboard.send({keys_str})")

    return '\n'.join(python_script)

# Read Ducky Script from the file named "payload.txt"
try:
    with open("payload.txt", "r") as file:
        ducky_script = file.read()
except FileNotFoundError:
    print("Error: 'payload.txt' file not found.")
    exit(1)

# Convert the Ducky Script to Python
converted_python_script = convert_ducky_to_python(ducky_script)

# Write the converted script to a file named "code.py"
with open("code.py", "w") as file:
    file.write(converted_python_script)

print("Converted script has been written to code.py")
