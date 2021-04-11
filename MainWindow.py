#-*- coding:utf-8 -*-

import queue
import socket as sk
import time
import threading
from multiprocessing import Process
import subprocess as sub
import sys
from functools import partial
from utils import get_diff_data,blh2xyz,xyz2blh,get_diff
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject,pyqtSignal,QPointF,QUrl
from PyQt5.QtCore import QDateTime,Qt,QTimer
from PyQt5.QtChart import QChart,QChartView,QValueAxis,QLineSeries,QScatterSeries
from PyQt5.QtWebEngineWidgets import *
import Ui_main
from ChartView import ChartView
from TcpDecode import compare,TCP_Data
from WebMain import app,app_add
from Log import LogWidget


class MyMain(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.set_connect()
        self.start_web()
       
    def start_web(self):
        self.ui.logView.write_data("Web Server Start...")
        web_log = open("web.log","w")
        self.app_run = threading.Thread(target=app.run)
        self.app_run.start()
        #self.app_run = sub.Popen("python WebMain.py",stdout=web_log,stderr=web_log)

    def init_UI(self):
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.charView={}
        self.add_Chart("enu_chart",self.ui.widget_4,["E","N","U"],self.ui.comboBox_2,self.ui.checkBox)
        self.add_Chart("SatNum",self.ui.widget_6,["SatNum"],self.ui.comboBox_3,self.ui.checkBox_2)
        self.add_Chart("PDOP",self.ui.widget_7,["PDOP"],self.ui.comboBox,self.ui.checkBox_3)
        self.add_Chart("Ratio",self.ui.widget_8,["Ratio"],self.ui.comboBox_4,self.ui.checkBox_4)
        # Web View
        self.gridLayout_web = QtWidgets.QGridLayout(self.ui.widget_map)
        self.gridLayout_web.setObjectName("gridLayout_web")
        self.ui.webView = QWebEngineView(self.ui.widget_map)
        self.gridLayout_web.addWidget(self.ui.webView,0,0,1,1)
        self.ui.webView.setUrl(QUrl('http://127.0.0.1:5000/'))

        # Log View
        self.ui.logView = LogWidget(self.ui.tab)

    def add_Chart(self,name,parent_view,s_key,button,checkbox):
        self.gridLayout_chart = QtWidgets.QGridLayout(parent_view)
        #self.gridLayout_chart.setObjectName("gridLayout_chart")
        self.ui.charView[name] = ChartView(parent_view,s_key=s_key)
        self.gridLayout_chart.addWidget(self.ui.charView[name],0,0,1,1)
        self.ui.charView[name].set_button(button,checkbox)

       
    def closeEvent(self,e):
        self.tcpdata1.close_data()
        self.tcpdata2.close_data()
        self.tcpdata1.write_temp.close()
        self.tcpdata2.write_temp.close()
        self.comp.write_temp.close()
        self.app_run.kill()
        self.close()

    def streambase_change(self):
        if self.ui.tabWidget_2.currentIndex() == 0:
            self.comp.set_static(False)
        else:
            self.tcpdata1.close_data()
            self.comp.set_static(True)

    def set_write_temp(self,obj,line_obj):
        obj.set_write_temp(line_obj.text())

    def set_connect(self):
        self.comp = compare(self.ui,self.ui.textBrowser_3,self.ui.charView)
        self.tcpdata1 = TCP_Data(self.ui,[self.ui.lineEdit,self.ui.lineEdit_2,self.ui.textBrowser,self.ui.pushButton_4,self.ui.pushButton],partial(self.comp.add_data,0),partial(app_add,0))
        self.tcpdata2 = TCP_Data(self.ui,[self.ui.lineEdit_6,self.ui.lineEdit_5,self.ui.textBrowser_2,self.ui.pushButton_5,self.ui.pushButton_3],partial(self.comp.add_data,1),partial(app_add,1),show_otherinfo=True)
        self.tcpdata1.set_write_temp(self.ui.lineEdit_base.text())
        self.tcpdata2.set_write_temp(self.ui.lineEdit_rover.text())
        self.ui.pushButton.clicked.connect(self.tcpdata1.start_connect)
        self.ui.pushButton.clicked.connect(self.streambase_change)
        self.ui.pushButton_4.clicked.connect(self.tcpdata1.close_data)
        self.ui.pushButton_3.clicked.connect(self.tcpdata2.start_connect)
        self.ui.pushButton_5.clicked.connect(self.tcpdata2.close_data)
        self.ui.pushButton_static.clicked.connect(self.streambase_change)
        self.ui.pushButton_6.clicked.connect(self.comp.set_write_temp)
        self.ui.pushButton_6.clicked.connect(partial(self.set_write_temp,self.tcpdata1,self.ui.lineEdit_base))
        self.ui.pushButton_6.clicked.connect(partial(self.set_write_temp,self.tcpdata2,self.ui.lineEdit_rover))
        self.tcpdata1.data_received.connect(self.tcpdata1.show_data)
        self.tcpdata2.data_received.connect(self.tcpdata2.show_data)
        self.comp.data_received.connect(self.comp.show_diff)
        