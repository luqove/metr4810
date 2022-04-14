import time
import threading    # if we use multithreading
from const import *


class System(object):
    """
    main thread，read sensor data，control the machine。
    """

    def __init__(self):
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

    # Turn on red "empty" LED and
    # notify control centre
    def report_empty(self):
        # turn on fault LED
        self.turn_on_led(LED_EMPTY)
        # TODO send signal to the main thread，
        self.notify_control_centre('''signal''')

    # Turn on fault LED and
    # notify control centre
    def report_fault(self):
        # turn on fault LED
        self.turn_on_led(LED_FAULT)
        # TODO send the signal to the main thread
        self.notify_control_centre('''signal''')

    # notify control centre

    def notify_control_centre(self, signal):
        # TODO If use multithreading，this function send signal to the main function
        pass

    # what is the stack level?
    def get_stack_level(self):
        # update sensor 1 value
        self.IR_sensor_2.read_data()
        self.IR_sensor_3.read_data()
        self.IR_sensor_4.read_data()
        # TODO adjust accoriding to remaing mask
        # 0-25%
        if self.IR_sensor_2.current_read == 0:
            self.turn_on_led(LED_25P)
        # 25-50%
        elif self.IR_sensor_2.current_read > 0 and self.IR_sensor_3 == 0:
            self.turn_on_led(LED_50P)
        # 50-75%
        elif (self.IR_sensor_2.current_read > 0 and
            self.IR_sensor_3.current_read > 0 and
            self.IR_sensor_4.current_read < 0):
            self.turn_on_led(LED_75P)
        # 75-100%
        elif (self.IR_sensor_2.current_read > 0 and
              self.IR_sensor_3.current_read>0 and
              self.IR_sensor_4.current_read > 0):
            self.turn_on_led(LED_100P)

    # Is a mask in transit?
    def is_mask_in_transit(self):
        # update sensor 5 reading
        self.IR_sensor_5.read_data()
        # TODO adjust according to mask level
        if self.IR_sensor_5.current_read > 0:
            return True

        #  self.report_fault()
        else:
            return False
        # Turn on "Ready" LED

    # Is mask requested
    def mask_requested(self):
        self.UL_sensor_1.read_data()
        # TODO accroding to mask level
        if self.UL_sensor_1.current_read < 1000:
            return True

    # Turn on fault LED and
    # notify control centre
    # turn on which led
    # eg.empty led，call self.turn_on_led(LED_EMPTY)

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
            # TODO turn off led
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

    #

    # main thread
    def run(self):
        pass


class IRSensor(object):
    """
    IR sensor instance for implementing various methods of IRSensor

    Could be that each sensor
    is a separate thread responsible for reading and returning data.
    """

    def __init__(self):
        self.current_read = 0   # current value

    '''
    Function to read IR_sensor
    Call this every time the data is updated and store the data in self.current_read
    Consider reading multiple data and taking the average
    '''

    def read_data(self):
        # TODO
        pass


class ULSensor(object):
    """
    UI sensor instance for implementing various methods of ULSensor
    the method here should be
    changed according to the sensor.

    Could be that each sensor is a separate thread
    responsible for reading and returning data
    """

    def __init__(self):
        self.current_read = 0   # current value

    '''
    # Function to read UL_sensor
    # Call this every time the data is updated and store the data in self.current_read
    # Here you have to negotiate with the team members who are sensors
    # Consider reading multiple data and taking the average
    '''

    def read_data(self):
        # TODO
        pass


class ACTMotor(object):
    """
    ACT motor
    """
    def __init__(self):
        # Record the current angle,
        # could be judged the opening and closing of the door according to this.
        self.angle = 0

    # Realize the rotation to achieve the door opening, or turn the belt
    # parameter is the input pulse.
    def rotate(self, pulse):

        pass

    # update angle
    def update_angle(self, pulse):
        const = 1   # This constant is the angle that the stepper motor rotates in a single pulse
        self.angle += pulse * const  # Number of pulses * single pulse angle

