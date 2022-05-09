
class IRSensor(object):
    """
    IR sensor instance for implementing various methods of IRSensor
    Note that the method here should be changed according to the method of the classmate who wrote the sensor.
    My idea is that each sensor is a separate thread responsible for reading and returning data.
    """

    def __init__(self, pin):
        self.current_read = 0  
        self.pin = pin

    # Read the function of IR_sensor
    # Call this every time the data is updated and store the data in self.current_read
    # Consider reading multiple data and taking the average
    def read_data(self):
        # TODO
        pass
