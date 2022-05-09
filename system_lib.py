import time
import RPi.GPIO as GPIO

from const import *
from Lib.Button import Button
from Lib.IRSensor import IRSensor
from Lib.StepperMotor import StepperMotor
from Lib.ServoMotor import ServoMotor
from Lib.ULSensor import ULSensor
from Lib.LED import LED


class System(object):
    """
    The main thread, reads the data of the sensors, 
    and controls the machine according to the data。
    """

    def __init__(self):
        # stack count initial 50 masks
        # Used to send the existing number of masks to the GUI.
        self.stack_count = 50

        # Setup the pins
        GPIO.setmode(GPIO.BOARD)

        # IR sensors
        # TODO Fill in the corresponding pin to control the corresponding sensor, note that I am not sure if some originals require more than two signal transmission pins.
        # TODO If there are two or more pins that need to be filled in, go to the corresponding lib and add more parameters in the parentheses of self.__init__()
        # TODO eg self.__init__(self, pin1, pin2)
        self.IR_sensor_1 = IRSensor('''pin''')
        self.IR_sensor_2 = IRSensor('''pin''')
        self.IR_sensor_3 = IRSensor('''pin''')
        self.IR_sensor_4 = IRSensor('''pin''')
        self.IR_sensor_5 = IRSensor('''pin''')

        # UL sensors
        self.UL_sensor_1 = ULSensor()

        # Stepper_motor
        self.Stepper_motor_0 = StepperMotor(stepper0_control_pins)
        self.Stepper_motor_1 = StepperMotor(stepper1_control_pins)

        # Servo_motor
        self.Servo_motor_0 = ServoMotor(servo_pin)

        # button
        self.reset_button = Button('''pin''')

        # TODO LED pin
        self.LED_PWR = LED('''pin''')
        self.LED_READY = LED('''pin''')
        self.LED_USER = LED('''pin''')
        self.LED_DISPENSING = LED('''pin''')
        self.LED_EMPTY = LED('''pin''')
        self.LED_FAULT = LED('''pin''')

        self.LED_100P = LED('''pin''')
        self.LED_75P = LED('''pin''')
        self.LED_50P = LED('''pin''')
        self.LED_25P = LED('''pin''')

    # reset all
    def reset(self):
        self.reset_stock_led()
        self.reset_report_led()

        # self.Stepper_motor_0.act('''init''')
        # self.Stepper_motor_1.act('''init''')

        self.close_door()
#
        self.IR_sensor_1.current_read = IR_LOW
        self.IR_sensor_2.current_read = IR_LOW
        self.IR_sensor_3.current_read = IR_LOW
        self.IR_sensor_4.current_read = IR_LOW
        self.IR_sensor_5.current_read = IR_LOW

    # Remaining masks led display reset
    def reset_stock_led(self):
        self.turn_off_led(LED_25P)
        self.turn_off_led(LED_50P)
        self.turn_off_led(LED_75P)
        self.turn_off_led(LED_100P)

    # Reset empty, ready, fault, DISPENSING leds, all off
    def reset_report_led(self):
        self.turn_off_led(LED_EMPTY)
        self.turn_off_led(LED_DISPENSING)
        self.turn_off_led(LED_FAULT)
        self.turn_off_led(LED_READY)
        self.turn_off_led(LED_PWR)
        self.turn_off_led(LED_USER)

    # Turn on red "empty" LED and
    # notify control centre
    def report_empty(self):
        # turn off the rest of the leds
        self.reset_report_led()
        # turn on LED_EMPTY
        self.turn_on_led(LED_EMPTY)

    # Turn on fault LED and notify control centre
    def report_fault(self):
        # turn off the rest of the leds
        self.reset_report_led()
        # turn on LED_FAULT
        self.turn_on_led(LED_FAULT)

    # what is the stack level?
    def display_stack_level(self):
        # 
        self.IR_sensor_2.read_data()
        self.IR_sensor_3.read_data()
        self.IR_sensor_4.read_data()
        # restet
        self.reset_stock_led()
        # TODO 
        # 0-25%
        if self.IR_sensor_2.current_read == IR_LOW:
            self.turn_on_led(LED_25P)
        # 25-50%
        elif self.IR_sensor_2.current_read == IR_HIGH and self.IR_sensor_3 == IR_LOW:
            self.turn_on_led(LED_50P)
        # 50-75%
        elif (self.IR_sensor_2.current_read == IR_HIGH and
              self.IR_sensor_3.current_read == IR_HIGH and
              self.IR_sensor_4.current_read == IR_LOW):
            self.turn_on_led(LED_75P)
        # 75-100%
        elif (self.IR_sensor_2.current_read == IR_HIGH and
              self.IR_sensor_3.current_read == IR_HIGH and
              self.IR_sensor_4.current_read == IR_HIGH):
            self.turn_on_led(LED_100P)

    # Is mask tray empty?
    def is_mask_tray_empty(self):
        self.IR_sensor_1.read_data()
        # TODO Not sure if LOW or HIGH means empty here
        if self.IR_sensor_1.current_read == IR_LOW:
            return True
        else:
            return False

    # Is a mask in transit?
    def is_mask_in_transit(self):
        # update IR_sensor5
        self.IR_sensor_5.read_data()
        # TODO
        if self.IR_sensor_5.current_read > 0:
            return True
        else:
            return False
        

    # Is mask requested
    def is_mask_requested(self):
        self.UL_sensor_1.read_data()
        # TODO According to  if the distance is less than 40cm, user detected
        if self.UL_sensor_1.current_read < 40:
            return True
        else:
            return False

    # Is a mask in the waiting position?
    def is_mask_in_waiting_position(self):
        self.IR_sensor_5.read_data()
        # TODONot sure here if IR_HIGH or IR_LOW means maks are waiting
        if self.IR_sensor_5.current_read == IR_HIGH:
            return True
        else:
            return False

    # dispensing mask
    # Take the mask out of the stack
    def dispensing_mask(self):
        self.reset_report_led()
        self.turn_on_led(LED_DISPENSING)
        self.Stepper_motor_0.act(2, "ccw")   # partially slide mask out of stack
        # TODO Should there be a time gap between two motor moves
        self.Stepper_motor_1.act(1, "ccw")   # pull the mask completely out of stack
        self.turn_off_led(LED_DISPENSING)

    # Open door
    def open_door(self):
        self.Servo_motor_0.act(100)

    # Close door
    def close_door(self):
        self.Servo_motor_0.act(0)

    # Release the mask partially
    def release_mask_partially(self):
        self.Stepper_motor_1.act(2, "ccw")

    # Release the mask totally
    # Here is simplified usage. Delete depending on the situation.
    def release_mask_totally(self):
        self.Stepper_motor_1.act(2, "ccw")

    # Is a mask in the collection position?
    def is_mask_still_waiting_collection(self):
        # TODO Not sure here if IR_HIGH or IR_LOW means maks are waiting
        if self.IR_sensor_5.current_read == IR_HIGH:
            return True
        else:
            return False

    # Turn on fault LED and
    # notify control centre
    def turn_on_led(self, led):
        if led == LED_EMPTY:
            self.LED_EMPTY.light_up()
        elif led == LED_DISPENSING:
            self.LED_DISPENSING.light_up()
        elif led == LED_PWR:
            self.LED_PWR.light_up()
        elif led == LED_USER:
            self.LED_USER.light_up()
        elif led == LED_READY:
            self.LED_READY.light_up()
        elif led == LED_FAULT:
            self.LED_FAULT.light_up()
        elif led == LED_25P:
            self.LED_25P.light_up()
        elif led == LED_50P:
            self.LED_50P.light_up()
        elif led == LED_75P:
            self.LED_75P.light_up()
        elif led == LED_100P:
            self.LED_100P.light_up()

    def turn_off_led(self, led):
        if led == LED_EMPTY:
            self.LED_EMPTY.turn_off()
        elif led == LED_DISPENSING:
            self.LED_DISPENSING.turn_off()
        elif led == LED_PWR:
            self.LED_PWR.turn_off()
        elif led == LED_USER:
            self.LED_USER.turn_off()
        elif led == LED_READY:
            self.LED_READY.turn_off()
        elif led == LED_FAULT:
            self.LED_FAULT.turn_off()
        elif led == LED_25P:
            self.LED_25P.turn_off()
        elif led == LED_50P:
            self.LED_50P.turn_off()
        elif led == LED_75P:
            self.LED_75P.turn_off()
        elif led == LED_100P:
            self.LED_100P.turn_off()

    # HALT The system stands by and does nothing until reset_button is pressed
    def HALT(self):
        while not self.reset_button.is_pushed():
            time.sleep(1)

    # Wait_request 
    def wait_request(self):
        while not self.is_mask_requested():
            # Poll every 0.1 seconds to check whether a client sends a Mask request
            time.sleep(1)

    # Open door and move mask into collection position.
    # Wait 3 seconds for user to collect the mask
    def release_mask_partially_and_wait(self):
        self.open_door()
        self.release_mask_partially()
        time.sleep(3)

    # TODO
    def send_current_stack_count(self):
        pass
