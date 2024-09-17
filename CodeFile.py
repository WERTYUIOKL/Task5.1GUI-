import RPi.GPIO as GPIO
import tkinter as tk

# Set up GPIO for the first set of LEDs
GPIO.setmode(GPIO.BCM)
RED_PIN_A = 17
GREEN_PIN_A = 22
BLUE_PIN_A = 27

# Configure the pins as output for the first set
GPIO.setup(RED_PIN_A, GPIO.OUT)
GPIO.setup(GREEN_PIN_A, GPIO.OUT)
GPIO.setup(BLUE_PIN_A, GPIO.OUT)

# Function to turn off all LEDs in the first set
def turn_off_leds_a():
    GPIO.output(RED_PIN_A, GPIO.LOW)
    GPIO.output(GREEN_PIN_A, GPIO.LOW)
    GPIO.output(BLUE_PIN_A, GPIO.LOW)

# Function to turn on the selected LED in the first set
def light_up_led_a(led_option):
    turn_off_leds_a()  # Turn off all LEDs first
    if led_option == 1:
        GPIO.output(RED_PIN_A, GPIO.HIGH)
    elif led_option == 2:
        GPIO.output(GREEN_PIN_A, GPIO.HIGH)
    elif led_option == 3:
        GPIO.output(BLUE_PIN_A, GPIO.HIGH)

# Handle the selection from the radio buttons for the first set
def choose_led_a():
    selected_led = led_choice_a.get()
    light_up_led_a(selected_led)

# Exit the application and clean up GPIO for the first set
def close_app_a():
    turn_off_leds_a()
    GPIO.cleanup()
    window.quit()

# Create the main window for the first set of LEDs
window = tk.Tk()
window.title("First LED Controller")

# Variable to store the selected LED for the first set
led_choice_a = tk.IntVar()

# Create the UI for the first set of LEDs
label_a = tk.Label(window, text="Control LEDs - First Set", font=("Arial", 20))
label_a.pack(pady=10)

led_radio_a1 = tk.Radiobutton(window, text="Red LED", variable=led_choice_a, value=1, command=choose_led_a)
led_radio_a2 = tk.Radiobutton(window, text="Green LED", variable=led_choice_a, value=2, command=choose_led_a)
led_radio_a3 = tk.Radiobutton(window, text="Blue LED", variable=led_choice_a, value=3, command=choose_led_a)

led_radio_a1.pack(anchor=tk.W, padx=20)
led_radio_a2.pack(anchor=tk.W, padx=20)
led_radio_a3.pack(anchor=tk.W, padx=20)

reset_button_a = tk.Button(window, text="Turn Off All", command=turn_off_leds_a)
reset_button_a.pack(pady=10)

exit_button_a = tk.Button(window, text="Exit", command=close_app_a)
exit_button_a.pack(pady=10)
