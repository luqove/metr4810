import ULSensor_maynard

class ULSensor(object):
    """
    UI 传感器实例，用于实现ULSensor的各种方法
    注意，这里的方法要根据写sensor的同学的方法改。

    我的想法是每个传感器都是一个单独的线程，负责读取和返回数据。
    """

    def __init__(self):
        self.current_read = 0  # 目前的读数

    # 读取UL_sensor的函数
    # 每次更新数据就调用这个,并将数据储存到 self.current_read里
    # 这里你要和做sensor的组员协商
    # 可以考虑读取多个数据取平均值
    def read_data(self):
        # 这里我就调用你那个同学的超声波读取了。
        return ULSensor_maynard.distance()
