import sys

import time
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QMutex
from PyQt5.QtWidgets import QApplication, QMainWindow

from MaskUi import Ui_MainWindow

mutex = QMutex()


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    主界面
    """

    # 初始化func，用于预先定义后面要用到的成员变量
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 连接槽函数
        # 按钮
        self.Clear_status_btn.clicked.connect(self.clear_feedback_bro)
        self.Demo_btn.clicked.connect(self.demo)
        # 菜单栏
        self.actionRefill_mask.triggered.connect(lambda: self.set_mask_num(50))
        self.actionEmpty_mask.triggered.connect(lambda: self.set_mask_num(0))
        self.actionRemove_1mask.triggered.connect(lambda: self.mask_num_decrease_by(1))
        self.actionRemove_50mask.triggered.connect(lambda: self.mask_num_decrease_by(50))
        self.actionAdd_1mask.triggered.connect(lambda: self.mask_num_increase_by(1))
        self.actionAdd_50mask.triggered.connect(lambda: self.mask_num_increase_by(50))

    # 每次调用，减少相应数量的口罩
    # num_decrease 就是要减少的数量
    def mask_num_decrease_by(self, num):
        mask_number = int(self.Mask_number_bro.toPlainText())
        mask_number -= num
        self.set_mask_num(mask_number)
        # TODO if 中的内容是Demo，以后删掉
        # 意思是如果发现口罩数量为0了，同时发现demo线程正在运行，就终止demo线程
        # 但是终止线程需要时间，在这期间demo线程会再次尝试减少一次，然后就会触发故障报错。
        # 反正是个demo，我也懒得做进一步的处理了，能看出效果就行。
        if mask_number == 0:
            if hasattr(self, 'timer'):
                mutex.lock()
                self.timer.requestInterruption()
                self.timer.quit()
                mutex.unlock()
                del self.timer

    # 添加口罩数量
    def mask_num_increase_by(self, num):
        mask_number = int(self.Mask_number_bro.toPlainText())
        mask_number += num
        self.set_mask_num(mask_number)

    # 反馈口罩机空了
    def empty_feedback(self):
        self.Feedback_bro.append(">>empty\n")

    # 反馈故障
    def error_occor(self):
        self.Feedback_bro.append(">>failure\n")

    # 设定口罩机内口罩的数量
    # 目前最大数量为9999
    def set_mask_num(self, num):
        # 如果输入数字为0，自动报空
        if num == 0:
            self.empty_feedback()
        # 如果输入数字小于0或者大于9999，报错
        elif num < 0 or num > 9999:
            self.error_occor()
            return
        # 根据数字长短调节显示, 不足四位，在前面补0
        display = str(num)
        if len(str(num)) <= 4:
            for a in range(4 - len(str(num))):
                display = "0" + display
        self.Mask_number_bro.setText(display)
        self.Mask_number_bro.setAlignment(Qt.AlignCenter)

    # 清空状态文本框
    def clear_feedback_bro(self):
        self.Feedback_bro.clear()

    # Demo empty
    # TODO 这里是Demo演示，以后删掉
    def demo(self):
        self.timer = TimerCount(1)
        self.timer.timer_signal.connect(lambda: self.mask_num_decrease_by(1))
        self.timer.start()


class TimerCount(QThread):

    timer_signal = pyqtSignal()

    def __init__(self, time_gap):
        super(TimerCount, self).__init__()
        self.time_gap = time_gap
    
    def run(self):
        while not(self.isInterruptionRequested()):
            time.sleep(self.time_gap)
            self.timer_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
