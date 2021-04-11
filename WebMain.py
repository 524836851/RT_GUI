import queue
import numpy as np
from flask import Flask,jsonify,render_template,request
from utils import xyz2blh
app = Flask(__name__)
Q_list=[queue.Queue(),queue.Queue()]

def app_add(idx,data):
    Q_list[idx].put(data)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route("/get_rtppp_data",methods=["POST"])
def get_rtppp_data():
    sow,data = Q_list[0].get()
    #xyz=[float(data[1]),float(data[2]),float(data[3])]
    b,l,h=xyz2blh(float(data[0]),float(data[1]),float(data[2]))  
    blh= {"sow":sow,"lat": float(b)*180.0/np.pi, "lng": float(l)*180.0/np.pi}
    return jsonify(blh)

@app.route("/get_great_data",methods=["POST"])
def get_great_data():
    sow,data = Q_list[1].get()
    #xyz=[float(data[1]),float(data[2]),float(data[3])]
    b,l,h=xyz2blh(float(data[0]),float(data[1]),float(data[2]))  
    blh= {"sow":sow,"lat": float(b)*180.0/np.pi, "lng": float(l)*180.0/np.pi}
    return jsonify(blh)
 
if __name__ == "__main__":
    app.debug=True
    #app.run("127.0.0.1","5000")
    app.run()