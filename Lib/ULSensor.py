from Lib.ULSensor_maynard import distance


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
    
    def read_data(self):
        self.current_read = distance()
        # Here I call ultrasound reading.
        return self.current_read
