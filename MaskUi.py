# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaskUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Mask_number_bro = QtWidgets.QTextBrowser(self.centralwidget)
        self.Mask_number_bro.setMinimumSize(QtCore.QSize(400, 210))
        self.Mask_number_bro.setMaximumSize(QtCore.QSize(16777215, 210))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(72)
        self.Mask_number_bro.setFont(font)
        self.Mask_number_bro.setObjectName("Mask_number_bro")
        self.horizontalLayout.addWidget(self.Mask_number_bro)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Feedback_bro = QtWidgets.QTextBrowser(self.centralwidget)
        self.Feedback_bro.setObjectName("Feedback_bro")
        self.verticalLayout.addWidget(self.Feedback_bro)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.Clear_status_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_status_btn.setObjectName("Clear_status_btn")
        self.horizontalLayout_2.addWidget(self.Clear_status_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefill_mask = QtWidgets.QAction(MainWindow)
        self.actionRefill_mask.setObjectName("actionRefill_mask")
        self.actionEmpty_mask = QtWidgets.QAction(MainWindow)
        self.actionEmpty_mask.setObjectName("actionEmpty_mask")
        self.actionAdd_50mask = QtWidgets.QAction(MainWindow)
        self.actionAdd_50mask.setObjectName("actionAdd_50mask")
        self.actionMax_mask = QtWidgets.QAction(MainWindow)
        self.actionMax_mask.setObjectName("actionMax_mask")
        self.actionAdd_1mask = QtWidgets.QAction(MainWindow)
        self.actionAdd_1mask.setObjectName("actionAdd_1mask")
        self.actionRemove_1mask = QtWidgets.QAction(MainWindow)
        self.actionRemove_1mask.setObjectName("actionRemove_1mask")
        self.actionRemove_50mask = QtWidgets.QAction(MainWindow)
        self.actionRemove_50mask.setObjectName("actionRemove_50mask")
        self.menu.addAction(self.actionRefill_mask)
        self.menu.addAction(self.actionEmpty_mask)
        self.menu.addAction(self.actionAdd_50mask)
        self.menu.addAction(self.actionAdd_1mask)
        self.menu.addAction(self.actionRemove_50mask)
        self.menu.addAction(self.actionRemove_1mask)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mask vending machine UI"))
        self.Mask_number_bro.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'AcadEref\'; font-size:72pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0050</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Status Display:"))
        self.Clear_status_btn.setText(_translate("MainWindow", "Clear Status"))
        self.menu.setTitle(_translate("MainWindow", "TestMenu"))
        self.actionRefill_mask.setText(_translate("MainWindow", "Refill_mask"))
        self.actionEmpty_mask.setText(_translate("MainWindow", "Empty_mask"))
        self.actionAdd_50mask.setText(_translate("MainWindow", "Add_50mask"))
        self.actionMax_mask.setText(_translate("MainWindow", "Max_mask"))
        self.actionAdd_1mask.setText(_translate("MainWindow", "Add_1mask"))
        self.actionRemove_1mask.setText(_translate("MainWindow", "Remove_1mask"))
        self.actionRemove_50mask.setText(_translate("MainWindow", "Remove_50mask"))

