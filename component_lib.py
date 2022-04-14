
class IRSensor(object):
    """
    IR sensor instance for implementing various methods of IRSensor
     Note that the method here should be changed according to the method of the classmate who wrote the sensor.

     My idea is that each sensor is a separate thread responsible for reading and returning data.
    """

    def __init__(self):
        self.current_read = 0  # current reading

    # Read the function of IR_sensor
    # Call this every time the data is updated and store the data in self.current_read
    # Consider reading multiple data and taking the average
    def read_data(self):
        # TODO
        pass


class ULSensor(object):
    """
    UI sensor instance for implementing various methods of ULSensor
    Note that the method here should be changed according to the method of the classmate who wrote the sensor.

     My idea is that each sensor is a separate thread responsible for reading and returning data.
    """

    def __init__(self):
        self.current_read = 0  # current reading

    # Function to read UL_sensor
    # Call this every time the data is updated and store the data in self.current_read
    # Here you have to negotiate with the team members who are sensors
    # Consider reading multiple data and taking the average
    def read_data(self):
        # TODO
        pass


class ACTMotor(object):
    """
    ACT stepper motor control class

    """

    def __init__(self):
        # Record the current angle,
        # you can judge the opening and closing of the door according to this.
        self.angle = 0

    # To achieve rotation, to achieve door opening, or to rotate the belt
    # The parameter is the input pulse.
    def rotate(self, pulse):
        pass

    # update angle
    def update_angle(self, pulse):
        const = 1  # This constant is the angle that
        # the stepper motor rotates in a single pulse
        self.angle += pulse * const  # Number of pulses * single pulse angle


class Button(object):
    """
    button class
    """

    def __init__(self):
        pass

    # TODO Here's how to implement button press detection.
    # Probably detect the corresponding GPIO input
    # Might need to do button stabilization, but it's not pi coding
    def is_pushed(self):
        return True

    def is_released(self):
        return True