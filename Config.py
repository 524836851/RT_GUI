#-*- coding:utf-8 -*-

import os
import json

def create_json_emptyfile(filename):
    if not os.path.exists(filename):
        with open(filename,"w") as myfile:
            json.dump({},myfile)
        

class app_conf:
    def __init__(self,ui):
        self.ui = ui
        self.init_conf()
        self.conf_name = ".temp_rt_gui.json"
        create_json_emptyfile(self.conf_name)
        with open(self.conf_name) as myfile:
            self.conf_data = json.load(myfile)

    def init_conf(self):
        self.kv_list = {}
        self.kv_list["static_crd_x"] = [self.ui.lineEdit_x,"0"]
        self.kv_list["static_crd_y"] = [self.ui.lineEdit_y,"0"]
        self.kv_list["static_crd_z"] = [self.ui.lineEdit_z,"0"]
        self.kv_list["Base_ip"] = [self.ui.lineEdit,"localhost"]
        self.kv_list["Base_port"] = [self.ui.lineEdit_2,"12345"]
        self.kv_list["Rover_ip"] = [self.ui.lineEdit_6,"localhost"]
        self.kv_list["Rover_port"] = [self.ui.lineEdit_5,"12346"]
        self.kv_list["Base_save_name"] = [self.ui.lineEdit_base,"Base"]
        self.kv_list["Rover_save_name"] = [self.ui.lineEdit_rover,"Rover"]
        self.kv_list["Compare_save_name"] = [self.ui.lineEdit_compare,"Compare"]
        self.kv_list["Save_dir"] = [self.ui.lineEdit_select,os.getcwd()+"./log"]

    def set_ui_conf(self):
        for k in self.kv_list.keys():
            # get from config or  default
            text_data = self.conf_data.get(k,self.kv_list[k][1])
            self.kv_list[k][0].setText(text_data)

    def update_conf(self):
        for k in self.kv_list.keys():
            # get from ui or default
            text_data = self.kv_list[k][0].text()
            text_data = text_data.strip()
            if not text_data:
                text_data = self.kv_list[k][1]
            self.conf_data[k] = text_data

    def write_conf(self):
        self.update_conf()
        with open(self.conf_name,"w") as myfile:
            json.dump(self.conf_data,myfile,indent=4)