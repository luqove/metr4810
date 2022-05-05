# Import Raspberry Pi pin library and time library
import RPi.GPIO as GPIO
import time

# Setup the pins
GPIO.setmode(GPIO.BOARD)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('This is a stepper motor test')
    stepper(0, 64)  # 1 Revolution

    dispense_mask()

