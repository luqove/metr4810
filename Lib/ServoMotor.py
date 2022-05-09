from MotorControl import servo


class Servo(object):
    """
    舵机控制
    """

    def __init__(self):
        # 记录目前的角度，可以根据这个判断门的开关。
        self.angle = 0

    # 实现转动，来达成开门，或者转动皮带
    # 参数是输入的脉冲。
    def act(self, angle):
        servo.act(angle)
        self.angle = angle
