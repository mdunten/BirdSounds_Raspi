import RPi.GPIO as GPIO
import pygame
import time

# Define the button grid dimensions
rows = 3
columns = 7

# GPIO pins for buttons (7 inputs and 3 outputs)
button_input_pins = [2, 3, 4, 17, 27, 22, 10]
button_output_pins = [9, 11, 5]

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Initialize Pygame for sound
pygame.mixer.init()

# Load your sound files (adjust the filenames)
sound_files = [
    "sound1.wav",
    "sound2.wav",
    "sound3.wav",
    "sound4.wav",
    "sound5.wav",
    "sound6.wav",
    "sound7.wav",
    "sound8.wav",
    "sound9.wav",
    "sound10.wav",
    "sound11.wav",
    "sound12.wav",
    "sound13.wav",
    "sound14.wav",
    "sound15.wav",
]

sounds = [pygame.mixer.Sound(file) for file in sound_files]

# Setup GPIO for the button grid (inputs)
for button_pin in button_input_pins:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup GPIO for the button grid (outputs)
for output_pin in button_output_pins:
    GPIO.setup(output_pin, GPIO.OUT)
    GPIO.output(output_pin, GPIO.LOW)

# Variable to track simultaneous button press
combined_buttons_pressed = False

# Function to be called when a button is pressed
def button_pressed_callback(channel):
    global combined_buttons_pressed

    sound_index = button_input_pins.index(channel)
    if 0 <= sound_index < len(sounds):
        print(f"Playing sound {sound_index + 1}")
        sounds[sound_index].play()

    # Check for simultaneous button press
    if any(GPIO.input(pin) == GPIO.LOW for pin in button_input_pins) and combined_buttons_pressed is False:
        combined_buttons_pressed = True
        print("Simultaneous button press detected!")

# Add event detection for all input buttons
for button_pin in button_input_pins:
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_pressed_callback, bouncetime=300)

try:
    print("Press buttons to play sounds. Press Ctrl+C to exit.")
    while True:
        # Simulate scanning the rows and activating the outputs
        for row in range(rows):
            GPIO.output(button_output_pins[row], GPIO.HIGH)
            time.sleep(0.01)  # Allow time for the signal to stabilize
            GPIO.output(button_output_pins[row], GPIO.LOW)

        # Reset the combined_buttons_pressed variable in each iteration
        combined_buttons_pressed = False

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()