import time
import threading  # we can use multithreading if we want
from const import *
from component_lib import *



class System(object):
    """
    The main thread, reads the data of the sensors,
    and controls the machine according to the data.
    """

    def __init__(self):
        # stack count initial 50 masks
        # stack count initial 50 masks
        self.stack_count = 50

        # IR sensors
        self.IR_sensor_1 = IRSensor()
        self.IR_sensor_2 = IRSensor()
        self.IR_sensor_3 = IRSensor()
        self.IR_sensor_4 = IRSensor()
        self.IR_sensor_5 = IRSensor()

        # UL sensors
        self.UL_sensor_1 = ULSensor()

        # ACT_motor
        self.ACT_motor_1 = ACTMotor()
        self.ACT_motor_2 = ACTMotor()
        self.ACT_motor_3 = ACTMotor()

        # button
        self.reset_button = Button()

    # reset all parameters
    def reset(self):
        self.reset_stock_led()
        self.reset_report_led()

        # TODO Here, according to the actual situation
        # Note that '''_'''
        # is a multi-line comment, remember to delete it
        self.ACT_motor_1.rotate('''Fill in the initial value that the stepper motor should have here''')
        self.ACT_motor_2.rotate('''Fill in the initial value that the stepper motor should have here''')
        self.ACT_motor_3.rotate('''Fill in the initial value that the stepper motor should have here''')

        self.IR_sensor_1.current_read = IR_LOW
        self.IR_sensor_2.current_read = IR_LOW
        self.IR_sensor_3.current_read = IR_LOW
        self.IR_sensor_4.current_read = IR_LOW
        self.IR_sensor_5.current_read = IR_LOW

        # TODO Here, according to the actual situation
        self.UL_sensor_1.current_read = 0

    # Remaining masks led display reset
    def reset_stock_led(self):
        self.turn_off_led(LED_25P)
        self.turn_off_led(LED_50P)
        self.turn_off_led(LED_75P)
        self.turn_off_led(LED_100P)

    # reset empty,ready,fault,DISPENSING led，all turn off
    def reset_report_led(self):
        self.turn_off_led(LED_EMPTY)
        self.turn_off_led(LED_DISPENSING)
        self.turn_off_led(LED_FAULT)
        self.turn_off_led(LED_READY)

    # Turn on red "empty" LED and
    # notify control centre
    def report_empty(self):
        # turn off the rest of the leds
        self.reset_report_led()
        # turn on fLED_EMPTY
        self.turn_on_led(LED_EMPTY)
        # TODO The signal to be sent to the main thread,
        #  the signal in parentheses is negotiated back
        self.notify_control_centre('''signal''')

    # Turn on fault LED and notify control centre
    def report_fault(self):
        # turn off the rest of the leds
        self.reset_report_led()
        # turn on LED_FAULT
        self.turn_on_led(LED_FAULT)
        # TODO The signal to send to the main thread
        self.notify_control_centre('''signal''')

    # notify control centre
    # The parameter is the signal to send
    def notify_control_centre(self, signal):
        # TODO If multithreading is used,
        #  this function sends a signal to the main thread.
        pass

    # what is the stack level?
    def display_stack_level(self):
        # Update the reading of IR_sensor1
        self.IR_sensor_2.read_data()
        self.IR_sensor_3.read_data()
        self.IR_sensor_4.read_data()
        # Reset the previous remaining amount display
        self.reset_stock_led()
        # TODO The following conditions are judged
        #  to be corrected according to the actual situation
        # 0-25% remaining
        if self.IR_sensor_2.current_read == IR_LOW:
            self.turn_on_led(LED_25P)
        # 25-50% remaining
        elif self.IR_sensor_2.current_read == IR_HIGH and self.IR_sensor_3 == IR_LOW:
            self.turn_on_led(LED_50P)
        # 50-75% remaining
        elif (self.IR_sensor_2.current_read == IR_HIGH and
              self.IR_sensor_3.current_read == IR_HIGH and
              self.IR_sensor_4.current_read == IR_LOW):
            self.turn_on_led(LED_75P)
        # 75-100%剩余
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
        # In fact, if, else can be simplified to the following form, but it is not as easy to understand as above.
        # return self.IR_sensor_1.current_read == IR_LOW
        # The following if and else are all the same

    # Is a mask in transit?
    def is_mask_in_transit(self):
        # Update the reading of IR_sensor5
        self.IR_sensor_5.read_data()
        # TODO The following conditions are
        #  judged to be corrected according to the actual situation
        if self.IR_sensor_5.current_read > 0:
            return True
        # Then the thread calling this func decides what to do next.
        # According to the flowchart, the next is self.report_fault()
        else:
            return False
        # According to the flow chart, the next step is Turn on "Ready" LED

    # Is mask requested
    def is_mask_requested(self):
        self.UL_sensor_1.read_data()
        #  TODO 1000 is what I wrote casually.
        #   The reading judgment of ULsensor should be modified according to the actual value.
        if self.UL_sensor_1.current_read < 1000:
            return True
        else:
            return False

    # Is a mask in the waiting position?
    def is_mask_in_waiting_position(self):
        self.IR_sensor_5.read_data()
        # TODO Not sure here if IR_HIGH or IR_LOW means maks are waiting
        if self.IR_sensor_5.current_read == IR_HIGH:
            return True
        else:
            return False

    # dispensing mask
    # Take the mask out of the stack
    def dispensing_mask(self):
        self.reset_report_led()
        self.turn_on_led(LED_DISPENSING)
        # TODO
        self.ACT_motor_1.rotate('''Fill in the pulse required for partially slide mask out of stack here''')
        self.ACT_motor_2.rotate('''Fill in the pulse needed to pull the mask completely out of stack here''')
        self.turn_off_led(LED_DISPENSING)

    # Open door
    def open_door(self):
        # TODO The specific implementation method
        #  is written according to the actual situation
        self.ACT_motor_1.rotate('''Fill in the pulse required to open the door here''')

    # Close door
    def close_door(self):
        # TODO The specific implementation method
        #  is written according to the actual situation
        self.ACT_motor_1.rotate('''Fill in the pulse required to close the door here''')

    # Release the mask partially
    # Push the mask part out of the machine and wait for the customer to pick it up
    def release_mask_partially(self):
        # TODO
        self.ACT_motor_2.rotate('''Fill in the pulses needed to move the mask partially out of the door here''')

    # Release the mask totally
    # Push the mask completely out of the machine
    # Here is simplified usage. It may only be necessary to partially do it.
    # Delete depending on the situation.
    def release_mask_totally(self):
        # TODO
        self.ACT_motor_2.rotate('''Fill in the pulses needed to move the mask totally out of the door here''')

    # Is a mask in the collection position?
    # Here I understand that if the guest does not take the mask for a long time,
    # the mask will be forced out completely.
    def is_mask_still_waiting_collection(self):
        # TODO Not sure here if IR_HIGH or IR_LOW means maks are waiting
        if self.IR_sensor_5.current_read == IR_HIGH:
            return True
        else:
            return False

    # Turn on fault LED and
    # notify control centre
    # The parameter led is to tell the function which led to turn on.
    # For example, to turn on empty led, call self.turn_on_led(LED_EMPTY)
    # LED_EMPTY is a constant defined in const,
    # the value is not important, it is a definition.
    def turn_on_led(self, led):
        if led == LED_EMPTY:
            # TODO turn on led
            pass
        elif led == LED_DISPENSING:
            pass
        elif led == LED_READY:
            pass
        elif led == LED_FAULT:
            pass
        elif led == LED_25P:
            pass
        elif led == LED_50P:
            pass
        elif led == LED_75P:
            pass
        elif led == LED_100P:
            pass

    def turn_off_led(self, led):
        if led == LED_EMPTY:
            # TODO implement turn off led
            pass
        elif led == LED_DISPENSING:
            pass
        elif led == LED_READY:
            pass
        elif led == LED_FAULT:
            pass
        elif led == LED_25P:
            pass
        elif led == LED_50P:
            pass
        elif led == LED_75P:
            pass
        elif led == LED_100P:
            pass

    # HALT system on standby, do nothing until reset_button is pressed
    def HALT(self):
        while not self.reset_button.is_pushed():
            # Poll every 0.1 seconds to detect whether the reset button is pressed
            time.sleep(0.1)

    # Wait_request The system is on standby
    # and does nothing until a customer comes to buy a mask
    def wait_request(self):
        while not self.is_mask_requested():
            # Poll every 0.1 seconds to
            # check whether a client sends a Mask request
            time.sleep(0.1)

    # Open door and move mask into collection position.
    # Wait "x" seconds for user to collect the mask
    def release_mask_partially_and_wait(self):
        self.open_door()
        self.release_mask_partially()
        # TODO Discuss with team members the time to wait
        time.sleep(5)

    # TODO Send the existing number of masks to the GUI
    # Discuss the specific implementation method with your team members
    def send_current_stack_count(self):
        pass


