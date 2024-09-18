import RPi.GPIO as GPIO
import tkinter as tk

# Set GPIO mode to BCM for the first set of LEDs
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the first set of LEDs (Red, Green, Blue)
RED_PIN_A = 11
GREEN_PIN_A = 20
BLUE_PIN_A = 25

# Configure the defined pins as output for controlling the LEDs
GPIO.setup(RED_PIN_A, GPIO.OUT)
GPIO.setup(GREEN_PIN_A, GPIO.OUT)
GPIO.setup(BLUE_PIN_A, GPIO.OUT)

# Function to turn off all LEDs in the first set
def turn_off_leds_a():
    GPIO.output(RED_PIN_A, GPIO.LOW)   # Turn off Red LED
    GPIO.output(GREEN_PIN_A, GPIO.LOW) # Turn off Green LED
    GPIO.output(BLUE_PIN_A, GPIO.LOW)  # Turn off Blue LED

# Function to light up the selected LED in the first set
# Based on the input, it will turn on the corresponding LED and turn off others
def light_up_led_a(led_option):
    turn_off_leds_a()  # Ensure all LEDs are off before lighting the selected one
    if led_option == 1:
        GPIO.output(RED_PIN_A, GPIO.HIGH)    # Turn on Red LED
    elif led_option == 2:
        GPIO.output(GREEN_PIN_A, GPIO.HIGH)  # Turn on Green LED
    elif led_option == 3:
        GPIO.output(BLUE_PIN_A, GPIO.HIGH)   # Turn on Blue LED

# Function to handle the selection of LED via radio buttons
def choose_led_a():
    selected_led = led_choice_a.get()  # Get the selected LED option (1, 2, or 3)
    light_up_led_a(selected_led)       # Call the function to light up the chosen LED

# Function to exit the application and clean up GPIO resources
def close_app_a():
    turn_off_leds_a()  # Turn off all LEDs before exiting
    GPIO.cleanup()     # Reset GPIO settings to default
    window.quit()      # Close the GUI window

# Create the main window for controlling the first set of LEDs
window = tk.Tk()
window.title("LED Controller 1")

# Variable to store the selected LED choice for the first set
led_choice_a = tk.IntVar()

# UI label for the LED controller window
label_a = tk.Label(window, text="LEDs control - First Set", font=("Arial", 20))
label_a.pack(pady=10)

# Radio buttons to select which LED (Red, Green, Blue) to control
led_radio_a1 = tk.Radiobutton(window, text="Red LED", variable=led_choice_a, value=1, command=choose_led_a)
led_radio_a2 = tk.Radiobutton(window, text="Green LED", variable=led_choice_a, value=2, command=choose_led_a)
led_radio_a3 = tk.Radiobutton(window, text="Blue LED", variable=led_choice_a, value=3, command=choose_led_a)

# Pack the radio buttons into the window
led_radio_a1.pack(anchor=tk.W, padx=20)
led_radio_a2.pack(anchor=tk.W, padx=20)
led_radio_a3.pack(anchor=tk.W, padx=20)

# Button to turn off all LEDs
reset_button_a = tk.Button(window, text="Turn Off All", command=turn_off_leds_a)
reset_button_a.pack(pady=10)

# Button to exit the application
exit_button_a = tk.Button(window, text="Exit", command=close_app_a)
exit_button_a.pack(pady=10)

# Start the GUI main loop
window.mainloop()
