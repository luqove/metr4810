import time

from const import *
from Lib.Button import Button
from Lib.IRSensor import IRSensor
from Lib.ACTMotor import ACTMotor
from Lib.ULSensor import ULSensor
from Lib.LED import LED


class System(object):
    """
    主线程，读取sensors的数据，根据数据控制机器。
    """

    def __init__(self):
        # stack count 初始50个口罩
        # 用于向GUI发送现有的口罩数量。
        self.stack_count = 50

        # IR sensors
        # TODO 填入相应的pin脚来控制相应的sensor，注意，我不确定是否有些原件需要两个以上的信号传输pin脚。
        # TODO 如果有两个及以上的pin需要填写，就去相应的lib中，在 self.__init__() 的括号中添加更多的参数
        # TODO 例如 self.__init__(self, pin1, pin2)
        self.IR_sensor_1 = IRSensor('''这里填入相应的pin''')
        self.IR_sensor_2 = IRSensor('''这里填入相应的pin''')
        self.IR_sensor_3 = IRSensor('''这里填入相应的pin''')
        self.IR_sensor_4 = IRSensor('''这里填入相应的pin''')
        self.IR_sensor_5 = IRSensor('''这里填入相应的pin''')

        # UL sensors
        # UL sensor不需要填入pin，因为只有一个，而且实现的同学已经把pin写到distance里面了。
        self.UL_sensor_1 = ULSensor()

        # ACT_motor
        self.ACT_motor_1 = ACTMotor('''这里填入相应的pin''')
        self.ACT_motor_2 = ACTMotor('''这里填入相应的pin''')
        self.ACT_motor_3 = ACTMotor('''这里填入相应的pin''')

        # button
        self.reset_button = Button('''这里填入相应的pin''')

        # LED
        self.LED_PWR = LED('''这里填入相应的pin''')
        self.LED_READY = LED('''这里填入相应的pin''')
        self.LED_USER = LED('''这里填入相应的pin''')
        self.LED_DISPENSING = LED('''这里填入相应的pin''')
        self.LED_EMPTY = LED('''这里填入相应的pin''')
        self.LED_FAULT = LED('''这里填入相应的pin''')

        self.LED_100P = LED('''这里填入相应的pin''')
        self.LED_75P = LED('''这里填入相应的pin''')
        self.LED_50P = LED('''这里填入相应的pin''')
        self.LED_25P = LED('''这里填入相应的pin''')

    # 重置一切参数
    def reset(self):
        self.reset_stock_led()
        self.reset_report_led()

        # TODO 这里根据实际情况改
        # 注意 '''_''' 是多行注释符，记得删除
        self.ACT_motor_1.rotate('''这里填步进电机应有的初始值''')
        self.ACT_motor_2.rotate('''这里填步进电机应有的初始值''')
        self.ACT_motor_3.rotate('''这里填步进电机应有的初始值''')

        self.IR_sensor_1.current_read = IR_LOW
        self.IR_sensor_2.current_read = IR_LOW
        self.IR_sensor_3.current_read = IR_LOW
        self.IR_sensor_4.current_read = IR_LOW
        self.IR_sensor_5.current_read = IR_LOW

        # TODO 这里根据实际情况改
        self.UL_sensor_1.current_read = 0

    # 剩余口罩led显示重置
    def reset_stock_led(self):
        self.turn_off_led(LED_25P)
        self.turn_off_led(LED_50P)
        self.turn_off_led(LED_75P)
        self.turn_off_led(LED_100P)

    # 重置empty,ready,fault,DISPENSING 的led，全部熄灭
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
        # 将其余的led全部关闭
        self.reset_report_led()
        # 打开fLED_EMPTY
        self.turn_on_led(LED_EMPTY)
        # TODO 要向主线程发送的信号，括号里的信号回头商量
        self.notify_control_centre('''信号''')

    # Turn on fault LED and notify control centre
    def report_fault(self):
        # 将其余的led全部关闭
        self.reset_report_led()
        # 打开LED_FAULT
        self.turn_on_led(LED_FAULT)
        # TODO 要向主线程发送的信号
        self.notify_control_centre('''信号''')

    # notify control centre
    # 参数就是要发送的信号
    def notify_control_centre(self, signal):
        # TODO 如果使用多线程，则这个函数就是向主线程发送信号。
        pass

    # what is the stack level?
    def display_stack_level(self):
        # 更新IR_sensor1的读书
        self.IR_sensor_2.read_data()
        self.IR_sensor_3.read_data()
        self.IR_sensor_4.read_data()
        # 将之前的剩余量显示重置
        self.reset_stock_led()
        # TODO 下面的条件判断根据实际情况自己修正
        # 0-25%剩余
        if self.IR_sensor_2.current_read == IR_LOW:
            self.turn_on_led(LED_25P)
        # 25-50%剩余
        elif self.IR_sensor_2.current_read == IR_HIGH and self.IR_sensor_3 == IR_LOW:
            self.turn_on_led(LED_50P)
        # 50-75%剩余
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
        # TODO 这里不确定是LOW还是HIGH表示空
        if self.IR_sensor_1.current_read == IR_LOW:
            return True
        else:
            return False
        # 其实if,else可以简化为下面这种形式, 是不过没有上面简单易懂。
        # return self.IR_sensor_1.current_read == IR_LOW
        # 后面的if,else全部同理

    # Is a mask in transit?
    def is_mask_in_transit(self):
        # 更新IR_sensor5的读数
        self.IR_sensor_5.read_data()
        # TODO 下面的条件判断根据实际情况自己修正
        if self.IR_sensor_5.current_read > 0:
            return True
        # 然后调用这个func的线程自行判断接下来要干的事情。
        # 根据流程图里，接下来是 self.report_fault()
        else:
            return False
        # 根据流程图里，接下来是 Turn on "Ready" LED

    # Is mask requested
    def is_mask_requested(self):
        self.UL_sensor_1.read_data()
        # # TODO 1000是我随便写的 ULsensor的读数判断要根据实际值取修改
        if self.UL_sensor_1.current_read < 1000:
            return True
        else:
            return False

    # Is a mask in the waiting position?
    def is_mask_in_waiting_position(self):
        self.IR_sensor_5.read_data()
        # TODO 这里不确定是 IR_HIGH 还是 IR_LOW 表示maks正在等待
        if self.IR_sensor_5.current_read == IR_HIGH:
            return True
        else:
            return False

    # dispensing mask
    # 将口罩从stack中取出来
    def dispensing_mask(self):
        self.reset_report_led()
        self.turn_on_led(LED_DISPENSING)
        # TODO
        self.ACT_motor_1.rotate('''这里填入partially slide mask out of stack 需要的脉冲''')
        self.ACT_motor_2.rotate('''这里填入pull the mask completely out of stack 需要的脉冲''')
        self.turn_off_led(LED_DISPENSING)

    # Open door
    def open_door(self):
        # TODO 具体实现方法根据实际情况写
        self.ACT_motor_1.rotate('''这里填入开门需要的脉冲''')

    # Close door
    def close_door(self):
        # TODO 具体实现方法根据实际情况写
        self.ACT_motor_1.rotate('''这里填入关门需要的脉冲''')

    # Release the mask partially
    # 将口罩部分推出机器等待客人拿取
    def release_mask_partially(self):
        # TODO
        self.ACT_motor_2.rotate('''这里填入move the mask partially out of the door需要的脉冲''')

    # Release the mask totally
    # 将口罩彻底推出机器
    # 这里是简化使用。可能只需要partially就可以了。看情况删除。
    def release_mask_totally(self):
        # TODO
        self.ACT_motor_2.rotate('''这里填入move the mask totally out of the door需要的脉冲''')

    # Is a mask in the collection position?
    # 这里我理解为，如果客人长时间没有取口罩，就强行将口罩彻底推出去。
    def is_mask_still_waiting_collection(self):
        # TODO 这里不确定是 IR_HIGH 还是 IR_LOW 表示maks正在等待
        if self.IR_sensor_5.current_read == IR_HIGH:
            return True
        else:
            return False

    # Turn on fault LED and
    # notify control centre
    # 参数led就是告知函数去开启哪一个led。
    # 例如，要打开empty led，就调用 self.turn_on_led(LED_EMPTY)
    # LED_EMPTY 是定义在const中的常数，数值不重要，就是一种定义。
    def turn_on_led(self, led):
        if led == LED_EMPTY:
            # TODO 实现开启led
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
            # TODO 实现关闭led
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

    # HALT 系统待命，不做任何事情直到reset_button 被按下
    def HALT(self):
        while not self.reset_button.is_pushed():
            # 每0.1秒轮询检测一次reset按钮是否按下
            time.sleep(0.1)

    # Wait_request 系统待命，不做任何事情直到有客户来买口罩
    def wait_request(self):
        while not self.is_mask_requested():
            # 每0.1秒轮询检测一次是否有客户发出 Mask request
            time.sleep(0.1)

    # Open door and move mask into collection position.
    # Wait "x" seconds for user to collect the mask
    def release_mask_partially_and_wait(self):
        self.open_door()
        self.release_mask_partially()
        # TODO 和组员讨论要等到的时间
        time.sleep(5)

    # TODO 向GUI发送现有的口罩数量
    # 具体实现方式和你的组员讨论
    def send_current_stack_count(self):
        pass
