#-*-coding:utf-8-*-
import os
import datetime
import queue
import socket as sk
import time
import threading
import sys
import copy
from functools import partial
from utils import get_diff_data,blh2xyz,xyz2blh,get_diff,sow2hms
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject,pyqtSignal,QPointF
from PyQt5.QtCore import QDateTime,Qt,QTimer
from PyQt5.QtChart import QChart,QChartView,QValueAxis,QLineSeries,QScatterSeries
import Ui_main

class compare(QObject):
    
    data_received = pyqtSignal()
    def __init__(self,ui,textBrowser,charView):
        super().__init__()
        self.ui = ui
        self.charView=charView
        self.textBrowser = textBrowser
        self.Q = [queue.Queue(),queue.Queue()]
        self.Q_now=[None,None]
        self.static = False;
    
    def set_write_temp(self):
        now_t=datetime.datetime.utcnow()
        save_dir = self.ui.lineEdit_select.text()
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        name = self.ui.lineEdit_compare.text()
        tempfile_name = f"{save_dir}/{name}_{now_t.year}_{now_t.month}_{now_t.day}_{now_t.hour}_{now_t.minute}.log"
        self.write_temp = open(tempfile_name,"w")

    def set_static(self,b):
        self.static = b

    def add_data(self,idx,data):
        self.Q[idx].put(data)
        self.data_received.emit()

    def show_diff(self):
        if self.static:
            if self.Q[1].empty():
                return
            self.Q_now[1] = self.Q[1].get()
            self.Q_now[0] = copy.deepcopy(self.Q_now[1])
            self.Q_now[0][1] = (float(self.ui.lineEdit_x.text()),float(self.ui.lineEdit_y.text()),float(self.ui.lineEdit_z.text()))
        else:
            for i in range(2):
                if self.Q_now[i] is None and not self.Q[i].empty():
                    self.Q_now[i] = self.Q[i].get()
                if self.Q_now[i] is None:
                    return
            if (self.Q_now[0][0] < self.Q_now[1][0]):
                self.Q_now[0] = None
                return
            if (self.Q_now[0][0] > self.Q_now[1][0]):
                self.Q_now[1] = None
                return
        enuDiff= get_diff(self.Q_now[0][1],self.Q_now[1][1])
        diff_data = {"sow":self.Q_now[0][0],"E":float(enuDiff[0]),"N":float(enuDiff[1]),"U":float(enuDiff[2]),"UTC":sow2hms(self.Q_now[0][0])}
        if self.Q_now[0][2]=="Fixed":
            # add chart
            for k in self.charView["enu_chart"].s_key:
                self.charView["enu_chart"].add_data(k,(diff_data["sow"],diff_data[k]))
        else:
            self.ui.logView.write_data(f"Epoch: {diff_data['UTC']} base rover is float! Rmove...")
        # add textBrowswer
        str_diffdata = f"{diff_data['UTC']} E:{diff_data['E']:.2f} N:{diff_data['N']:.2f} U:{diff_data['U']:.2f}"
        self.textBrowser.append(str_diffdata)
        self.write_temp.write(str_diffdata+"\n")

        self.Q_now[0] = None
        self.Q_now[1] = None

class TCP_Data(QObject):

    data_received = pyqtSignal()

    def __init__(self,ui,ui_list,compare_add,app_add,show_otherinfo=False):
        super().__init__()
        self.ui = ui
        self.ui_list = ui_list
        self.q_result = queue.Queue()
        self.compare_add = compare_add
        self.app_add = app_add
        self.show_otherinfo =show_otherinfo
        self.sock = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        self.static = False

    def set_write_temp(self,name,dir_name="./log"):
        self.close_data()
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        now_t = datetime.datetime.utcnow()
        tempflie_name = f"{dir_name}/{name}_{now_t.year}_{now_t.month}_{now_t.day}_{now_t.hour}_{now_t.minute}.log"
        self.write_temp = open(tempflie_name,"w")
        
    def start_connect(self):
        sender = self.sender()
        self.ip = self.ui_list[0].text()
        self.port = int(self.ui_list[1].text())
        self.sock = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        try:
            self.sock.connect((self.ip,self.port))
        except ConnectionError as e:
            self.ui.logView.write_data(str(e))
            self.ui.logView.write_data(f"Connect {self.ip} {self.port} Fail!")
            return
        except OSError as e:
            self.ui.logView.write_data(str(e))
            self.ui.logView.write_data(f"Connect {self.ip} {self.port} Fail!")
            return
        self.ui.logView.write_data(f"{self.ip} {self.port} Connect Success")
        sender.setText("Connected")
        sender.setDisabled(True)
        self.ui_list[3].setDisabled(False)
        self.get_thread = threading.Thread(target=self.get_data)
        self.get_thread.start()

    def show_data(self):
        data = self.q_result.get()
        data = data.replace(","," ")
        data=data.split()

        sow = float(data[0])
        x,y,z = (float(data[1]),float(data[2]),float(data[3]))
        str_data = f"{sow2hms(sow)} {x:13.3f} {y:13.3f} {z:13.3f}"

        if (len(data) > 4):
            satNum=float(data[7])
            pdop=float(data[8])
            mode=data[9]
            ratio=float(data[10])
            str_data+=" ".join(data[7:])
            
        self.ui_list[2].append(str_data)
        self.write_temp.write(str_data+"\n")
        if self.show_otherinfo:
            self.ui.charView["SatNum"].add_data("SatNum",(sow,satNum))
            self.ui.charView["PDOP"].add_data("PDOP",(sow,pdop))
            self.ui.charView["Ratio"].add_data("Ratio",(sow,satNum))

    def get_data(self):
        if not self.static:
            while True:
                try:
                    data = self.sock.recv(2048).decode()
                    self.q_result.put(data)
                    self.data_received.emit()
                    data = data.replace(","," ")
                    data=data.split()
                    mode = data[9]
                    sow=float(data[0])  #second of week in GPST
                    xyz=[float(data[1]),float(data[2]),float(data[3])]
                    b,l,h=xyz2blh(float(data[1]),float(data[2]),float(data[3]))  
                    self.compare_add([sow,xyz,mode])
                    self.app_add([sow,xyz])
                except ConnectionError as e:
                    self.ui.logView.write_data(str(e))
                    break
                except OSError as e:
                    self.ui.logView.write_data(str(e))
                    break

    def close_data(self):
        try:
            self.sock.close()
        except Exception as e:
            self.ui.logView.write_data(str(e))
        self.ui_list[3].setDisabled(True)
        self.ui_list[4].setDisabled(False)