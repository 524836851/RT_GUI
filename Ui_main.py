# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\project\RT_GUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout.setContentsMargins(1, 1, 1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.tab_10)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 210))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_7 = QtWidgets.QLabel(self.tab_9)
        self.label_7.setObjectName("label_7")
        self.gridLayout_13.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_13.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_9)
        self.label_4.setObjectName("label_4")
        self.gridLayout_13.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_13.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_13.addWidget(self.pushButton_3, 2, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_13.addWidget(self.pushButton_5, 3, 0, 1, 2)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.gridLayout_7.addWidget(self.tabWidget_3, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_base = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_base.setObjectName("lineEdit_base")
        self.gridLayout_5.addWidget(self.lineEdit_base, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)
        self.lineEdit_rover = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_rover.setObjectName("lineEdit_rover")
        self.gridLayout_5.addWidget(self.lineEdit_rover, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 2, 0, 1, 1)
        self.lineEdit_compare = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_compare.setObjectName("lineEdit_compare")
        self.gridLayout_5.addWidget(self.lineEdit_compare, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 3, 0, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 3, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label = QtWidgets.QLabel(self.tab_7)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_11.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_7)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_11.addWidget(self.pushButton, 2, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_11.addWidget(self.pushButton_4, 3, 0, 1, 2)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_3 = QtWidgets.QLabel(self.tab_8)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_z = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.gridLayout_12.addWidget(self.lineEdit_z, 2, 1, 1, 1)
        self.lineEdit_y = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.gridLayout_12.addWidget(self.lineEdit_y, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_8)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 2, 0, 1, 1)
        self.lineEdit_x = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.gridLayout_12.addWidget(self.lineEdit_x, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_12.addWidget(self.label_8, 1, 0, 1, 1)
        self.pushButton_static = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_static.setObjectName("pushButton_static")
        self.gridLayout_12.addWidget(self.pushButton_static, 3, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.gridLayout_7.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.tab_10)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setContentsMargins(1, 5, 1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_4.addWidget(self.textBrowser_2, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_4.addWidget(self.textBrowser_3, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_draw = QtWidgets.QWidget()
        self.tab_draw.setObjectName("tab_draw")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_draw)
        self.gridLayout_8.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_draw)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 4)
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(636, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_6.addWidget(self.checkBox_2, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(636, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.tab_4)
        self.widget_6.setEnabled(True)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_6.addWidget(self.widget_6, 1, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_9.addWidget(self.checkBox_3, 0, 3, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.tab_5)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_9.addWidget(self.widget_7, 1, 0, 1, 4)
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_9.addWidget(self.comboBox, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(636, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_13 = QtWidgets.QLabel(self.tab_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(630, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_10.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_4.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_4, 0, 2, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.tab_6)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_10.addWidget(self.widget_8, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_draw, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_14.setContentsMargins(0, 1, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.widget_map = QtWidgets.QWidget(self.tab_11)
        self.widget_map.setObjectName("widget_map")
        self.gridLayout_14.addWidget(self.widget_map, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_11, "")
        self.gridLayout_3.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.widget_log = QtWidgets.QWidget(self.centralwidget)
        self.widget_log.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_log.setMaximumSize(QtCore.QSize(16777215, 250))
        self.widget_log.setObjectName("widget_log")
        self.gridLayout_3.addWidget(self.widget_log, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsdfsdfsdf = QtWidgets.QAction(MainWindow)
        self.actionsdfsdfsdf.setObjectName("actionsdfsdfsdf")

        self.retranslateUi(MainWindow)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(2)
        self.comboBox_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RTShow"))
        self.label_7.setText(_translate("MainWindow", "IP"))
        self.lineEdit_6.setText(_translate("MainWindow", "localhost"))
        self.label_4.setText(_translate("MainWindow", "PORT"))
        self.lineEdit_5.setText(_translate("MainWindow", "12346"))
        self.pushButton_3.setText(_translate("MainWindow", "Connect"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Dynamic"))
        self.label_15.setText(_translate("MainWindow", "Base Result"))
        self.lineEdit_base.setText(_translate("MainWindow", "Base"))
        self.label_16.setText(_translate("MainWindow", "Rover Result"))
        self.lineEdit_rover.setText(_translate("MainWindow", "Rover"))
        self.label_17.setText(_translate("MainWindow", "Compare Result"))
        self.lineEdit_compare.setText(_translate("MainWindow", "Compare"))
        self.pushButton_6.setText(_translate("MainWindow", "SAVE"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.lineEdit.setText(_translate("MainWindow", "localhost"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.lineEdit_2.setText(_translate("MainWindow", "12345"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.pushButton_4.setText(_translate("MainWindow", "Stop"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Dynamic"))
        self.label_3.setText(_translate("MainWindow", "X_CRD"))
        self.label_14.setText(_translate("MainWindow", "Z_CRD"))
        self.label_8.setText(_translate("MainWindow", "Y_CRD"))
        self.pushButton_static.setText(_translate("MainWindow", "Set"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Static"))
        self.label_18.setText(_translate("MainWindow", "Stream Base Settings"))
        self.label_19.setText(_translate("MainWindow", "Stream Rover Settings"))
        self.label_20.setText(_translate("MainWindow", "Result FileName Settings"))
        self.label_10.setText(_translate("MainWindow", "Stream Rover Result"))
        self.label_9.setText(_translate("MainWindow", "Stream Base Result"))
        self.label_11.setText(_translate("MainWindow", "Compare Result"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("MainWindow", "Main"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "0.1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "0.5"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "30"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "50"))
        self.checkBox.setText(_translate("MainWindow", "FromZero"))
        self.label_5.setText(_translate("MainWindow", "YAxis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ENUPlot"))
        self.checkBox_2.setText(_translate("MainWindow", "FromZero"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "20"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "30"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "50"))
        self.label_6.setText(_translate("MainWindow", "YAxis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "SatNum"))
        self.checkBox_3.setText(_translate("MainWindow", "FromZero"))
        self.comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox.setItemText(1, _translate("MainWindow", "10"))
        self.label_12.setText(_translate("MainWindow", "YAxis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "PDOP"))
        self.label_13.setText(_translate("MainWindow", "FYAxis"))
        self.checkBox_4.setText(_translate("MainWindow", "FromZero"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "30"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "50"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "100"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Ratio"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_draw), _translate("MainWindow", "Draw"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("MainWindow", "Map"))
        self.actionsdfsdfsdf.setText(_translate("MainWindow", "sdfsdfsdf"))
