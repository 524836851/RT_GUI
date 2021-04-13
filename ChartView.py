#-*-coding:utf-8-*-
import datetime
import queue
import socket as sk
import time
import threading
import sys
from functools import partial
from utils import get_diff_data,blh2xyz,xyz2blh,get_diff,sow2hms,sow2datetime
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter,QBrush,QColor,QPen
from PyQt5.QtWidgets import QMainWindow,QPushButton,QComboBox
from PyQt5.QtCore import QObject,pyqtSignal,QPointF
from PyQt5.QtCore import QDateTime,Qt,QTimer
from PyQt5.QtChart import QChart,QChartView,QValueAxis,QLineSeries,QScatterSeries,QDateTimeAxis

class ChartView(QChartView,QChart):
    data_updated= pyqtSignal()
    def __init__(self, *args,**kwargs):
        s_key = kwargs["s_key"]
        kwargs.pop("s_key")
        super(ChartView, self).__init__(*args, **kwargs)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.q_point={}
        self.chart_init(s_key)

    def set_button(self,comboBox,checkbox):
        self.comboBox= comboBox
        self.checkbox = checkbox
        self.comboBox.currentIndexChanged.connect(self.set_yaxis_range)
        self.checkbox.stateChanged.connect(self.set_yaxis_range)
        self.set_yaxis_range()

    def set_yaxis_range(self):
        max_v = float(self.comboBox.currentText())
        min_v = -max_v
        fromzero = self.checkbox.isChecked()
        if fromzero:
            min_v = 0
        self.y_Aix.setMin(min_v)
        self.y_Aix.setMax(max_v)

    def add_data(self,k,point):
        """
        point:[sow,value]
        """
        sow,value = point
        cur_t  = sow2datetime(sow)
        cur_time = QDateTime().fromSecsSinceEpoch(cur_t.timestamp())
        self.series_list[k].append(cur_time.toMSecsSinceEpoch(),value)

        if self.series_list[k].count() > 2700:
            self.series_list[k].removePoints(0,self.series_list[k].count()-2700)
        min_time = QDateTime().fromMSecsSinceEpoch(self.series_list[k].at(0).x())
        max_time = cur_time.addSecs(10)
        self.x_Aix.setMin(min_time)
        self.x_Aix.setMax(max_time)

    def chart_init(self,s_key):
        self.chart = QChart()
        self.x_Aix = QDateTimeAxis()#定义x轴，实例化
        #self.x_Aix.setRange(52665,52765)
        #self.x_Aix.setLabelFormat("%0.2f")
        self.x_Aix.setFormat("hh:mm:ss")
        self.x_Aix.setTickCount(6)
        #self.x_Aix.setTickCount(6)
        #self.x_Aix.setMinorTickCount(0)

        self.y_Aix = QValueAxis()#定义y轴
        #self.y_Aix.setRange(-50,50)
        self.y_Aix.setLabelFormat("%0.2f")
        #self.y_Aix.setTickCount(6)
        self.y_Aix.setMinorTickCount(0)

        self.chart.addAxis(self.x_Aix,Qt.AlignBottom)
        self.chart.addAxis(self.y_Aix,Qt.AlignLeft)

        self.s_key = s_key
        self.series_list={}
        color_list = [QColor("blue"),QColor("green"),QColor("red"),QColor(152,245,255),QColor(84,255,159),QColor(255,193,193)]
        for k,c in zip(self.s_key,color_list):
            self.q_point[k] = queue.Queue()
            self.series_list[k] = QScatterSeries()
            self.series_list[k].setMarkerSize(7.0)
            self.series_list[k].setColor(QColor(c))
            self.series_list[k].setPen(QPen(QtCore.Qt.PenStyle.NoPen))
            self.chart.addSeries(self.series_list[k])
            self.series_list[k].setName(k)
            self.series_list[k].attachAxis(self.x_Aix)
            self.series_list[k].attachAxis(self.y_Aix)

        self.setChart(self.chart)