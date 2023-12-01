import RPi.GPIO as GPIO
import time

# Define the number of rows and columns in the button grid
num_rows = 7
num_cols = 3

# Define GPIO input pins for rows and output pins for columns
input_pins = [2, 3, 4, 17, 27, 22, 10]
output_pins = [9, 11, 5]

# Set the GPIO mode and setup input and output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(output_pins, GPIO.OUT, initial=GPIO.LOW)

# Initialize a dictionary to store the state of each button
button_states = {(row, col): False for row in range(num_rows) for col in range(num_cols)}

def detect_button_press():
    for col in range(num_cols):
        # Activate the current column
        GPIO.output(output_pins[col], GPIO.HIGH)

        # Check each row in the current column
        for row in range(num_rows):
            button_key = (row, col)
            button_state = GPIO.input(input_pins[row]) == GPIO.LOW

            # Check for button state change
            if button_state != button_states[button_key]:
                if button_state:
                    # Button pressed, do something
                    print(f'Button pressed: Row {row + 1}, Column {col + 1}')
                else:
                    # Button released, do something else
                    print(f'Button released: Row {row + 1}, Column {col + 1}')

                # Update button state
                button_states[button_key] = button_state

        # Deactivate the current column
        GPIO.output(output_pins[col], GPIO.LOW)

try:
    while True:
        detect_button_press()

except KeyboardInterrupt:
    pass

finally:
    # Cleanup GPIO on program exit
    GPIO.cleanup()