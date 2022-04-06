import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from MaskUi import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    主界面
    """

    # 初始化func，用于预先定义后面要用到的成员变量
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 连接槽函数
        self.Clear_status_btn.clicked.connect(self.clear_feedback_bro)
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

    # 添加口罩数量
    def mask_num_increase_by(self, num):
        mask_number = int(self.Mask_number_bro.toPlainText())
        mask_number += num
        self.set_mask_num(mask_number)

    # 反馈口罩机空了
    def empty_feedback(self):
        self.Feedback_bro.append(">>empty, please refill mask\n")

    # 反馈故障
    def error_occor(self):
        self.Feedback_bro.append(">>Error!\n")

    # 设定口罩机内口罩的数量
    # 目前最大数量为9999
    def set_mask_num(self, num):
        # 如果输入数字为0，自动报空
        if num == 0:
            self.empty_feedback()
        # 如果输入数字小于0，报错
        elif num < 0 or num > 99:
            self.error_occor()
            return
        # 根据数字长短调节显示, 不足四位，在前面补0
        display = str(num)
        if len(str(num)) <= 4:
            for a in range(4 - len(str(num))):
                display = "remaining mask: 0" + display
        self.Mask_number_bro.setText(display)
        self.Mask_number_bro.setAlignment(Qt.AlignCenter)

    # 清空状态文本框
    def clear_feedback_bro(self):
        self.Feedback_bro.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
