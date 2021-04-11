#-*- coding:utf-8 -*-


import datetime
import queue
from PyQt5 import QtWidgets
from PyQt5 import QtCore


class LogWidget(QtWidgets.QTextBrowser):

    logdata_recived = QtCore.pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #self.gridLayout = QtWidgets.QGridLayout(self.parent())
        #self.gridLayout.addWidget(self,0,0,1,1)
        self.q_log=queue.Queue()
        self.logdata_recived.connect(self.flush_data)

    def write_data(self,str_log):
        if str_log[-1] == "\n":
            str_log=str_log[:-1]
        self.q_log.put(str_log)
        self.logdata_recived.emit()

    def flush_data(self):
        str_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        str_info = f"[{str_time}]: {self.q_log.get()}"
        self.append(str_info)