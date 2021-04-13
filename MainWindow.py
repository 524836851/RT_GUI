#-*- coding:utf-8 -*-

import os
import queue
import socket as sk
import time
import threading
import json
from multiprocessing import Process
import subprocess as sub
import sys
from functools import partial
from utils import get_diff_data,blh2xyz,xyz2blh,get_diff
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QDialog
from PyQt5.QtCore import QObject,pyqtSignal,QPointF,QUrl,QMargins
from PyQt5.QtCore import QDateTime,Qt
from PyQt5.QtChart import QChart,QChartView,QValueAxis,QLineSeries,QScatterSeries
#from PyQt5.QtWebEngineWidgets import QWebEngineView
import Ui_main,Ui_close
from ChartView import ChartView
from TcpDecode import compare,TCP_Data
from WebMain import app,app_add
from Log import LogWidget
from Config import app_conf

class CloseView(QDialog):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_close.Ui_Dialog()
        self.ui.setupUi(self)

    def set_parent_e(self,e):
        self.e = e
        self.ignore = True

    def close_not_ignore(self):
        self.ignore = False
        self.close()
        
    def closeEvent(self,e):
        if self.ignore:
            self.e.ignore()
        super().closeEvent(e)
        



class MyMain(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.conf = app_conf(self.ui)
        self.conf.set_ui_conf()
        self.set_connect()
        #self.start_web()
       
    def start_web(self):
        self.ui.logView.write_data("Web Server Start...")
        web_log = open("web.log","w")
        self.app_run = threading.Thread(target=app.run)
        self.app_run.start()

    def init_UI(self):
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.charView={}
        self.add_Chart("enu_chart",self.ui.widget_4,["E","N","U","float_E","float_N","float_U"],self.ui.comboBox_2,self.ui.checkBox)
        self.add_Chart("SatNum",self.ui.widget_6,["SatNum"],self.ui.comboBox_3,self.ui.checkBox_2)
        self.add_Chart("PDOP",self.ui.widget_7,["PDOP"],self.ui.comboBox,self.ui.checkBox_3)
        self.add_Chart("Ratio",self.ui.widget_8,["Ratio"],self.ui.comboBox_4,self.ui.checkBox_4)
        # Web View
        #self.gridLayout_web = QtWidgets.QGridLayout(self.ui.widget_map)
        #self.gridLayout_web.setObjectName("gridLayout_web")
        #self.ui.webView = QWebEngineView(self.ui.widget_map)
        #self.gridLayout_web.addWidget(self.ui.webView,0,0,1,1)
        #self.gridLayout_web.setContentsMargins(QMargins(0,0,0,0))
        #self.ui.webView.setUrl(QUrl('http://127.0.0.1:5000/'))

        # Log View
        self.ui.logView = LogWidget(self.ui.centralwidget)
        self.ui.gridLayout_3.addWidget(self.ui.logView, 1, 0, 1, 1)

    def add_Chart(self,name,parent_view,s_key,button,checkbox):
        self.gridLayout_chart = QtWidgets.QGridLayout(parent_view)
        #self.gridLayout_chart.setObjectName("gridLayout_chart")
        self.ui.charView[name] = ChartView(parent_view,s_key=s_key)
        self.gridLayout_chart.addWidget(self.ui.charView[name],0,0,1,1)
        self.gridLayout_chart.setContentsMargins(QMargins(0,0,0,0))
        self.gridLayout_chart.setVerticalSpacing(0)
        self.ui.charView[name].set_button(button,checkbox)

    def close_all(self,e,save):
        if save:
            self.conf.write_conf()
        self.tcpdata1.close_data()
        self.tcpdata2.close_data()
        self.tcpdata1.write_temp.close()
        self.tcpdata2.write_temp.close()
        self.comp.write_temp.close()
        super().closeEvent(e)
      
    def closeEvent(self,e):
        close_view = CloseView()
        close_view.set_parent_e(e)
        close_view.ui.pushButton.clicked.connect(close_view.close_not_ignore)
        close_view.ui.pushButton.clicked.connect(partial(self.close_all,e,True))
        close_view.ui.pushButton_2.clicked.connect(close_view.close_not_ignore)
        close_view.ui.pushButton_2.clicked.connect(partial(self.close_all,e,False))
        close_view.ui.pushButton_3.clicked.connect(close_view.close)
        close_view.exec()

    def streambase_change(self):
        if self.ui.tabWidget_2.currentIndex() == 0:
            self.comp.set_static(False)
            self.ui.logView.write_data("Stream Base Using Dynamic Stream!")
        else:
            self.tcpdata1.close_data()
            self.comp.set_static(True)
            self.ui.logView.write_data("Stream Base Using Static Crd!")

    def set_write_temp(self):
        try:
            self.comp.set_write_temp()
            self.tcpdata1.set_write_temp(self.ui.lineEdit_base.text(),self.ui.lineEdit_select.text())
            self.tcpdata2.set_write_temp(self.ui.lineEdit_rover.text(),self.ui.lineEdit_select.text())
        except OSError as e:
            self.ui.logView.write_data(str(e))
            self.ui.logView.write_data("Settings write_temp Fail!")
            return
        self.ui.logView.write_data('Settings Write_temp Success')

    def btn_choose_dir(self):
        cwd = os.getcwd()
        dir_choose =  QFileDialog.getExistingDirectory(self,"Select",cwd)
        if dir_choose=="":
            return
        self.ui.lineEdit_select.setText(dir_choose)
        self.ui.logView.write_data(f"Set Save Diretory: {dir_choose}")
    

    def set_connect(self):
        self.comp = compare(self.ui,self.ui.textBrowser_3,self.ui.charView)
        self.tcpdata1 = TCP_Data(self.ui,[self.ui.lineEdit,self.ui.lineEdit_2,self.ui.textBrowser,self.ui.pushButton_4,self.ui.pushButton],partial(self.comp.add_data,0),partial(app_add,0))
        self.tcpdata2 = TCP_Data(self.ui,[self.ui.lineEdit_6,self.ui.lineEdit_5,self.ui.textBrowser_2,self.ui.pushButton_5,self.ui.pushButton_3],partial(self.comp.add_data,1),partial(app_add,1),show_otherinfo=True)
        self.set_write_temp()

        self.ui.pushButton.clicked.connect(self.tcpdata1.start_connect)
        self.ui.pushButton.clicked.connect(self.streambase_change)
        self.ui.pushButton_4.clicked.connect(self.tcpdata1.close_data)
        self.ui.pushButton_3.clicked.connect(self.tcpdata2.start_connect)
        self.ui.pushButton_5.clicked.connect(self.tcpdata2.close_data)
        self.ui.pushButton_static.clicked.connect(self.streambase_change)
        self.ui.pushButton_6.clicked.connect(self.set_write_temp)
        self.ui.pushButton_select.clicked.connect(self.btn_choose_dir)
        self.tcpdata1.data_received.connect(self.tcpdata1.show_data)
        self.tcpdata2.data_received.connect(self.tcpdata2.show_data)
        self.comp.data_received.connect(self.comp.show_diff)
        