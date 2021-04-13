import sys
import numpy as np
from flask import Flask,jsonify,render_template,request,current_app
from utils import xyz2blh
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route("/get_rtppp_data",methods=["POST"])
def get_rtppp_data():
    sow,data = current_app._get_current_object().Q_list[0].get()
    b,l,h=xyz2blh(float(data[0]),float(data[1]),float(data[2]))  
    blh= {"sow":sow,"lat": float(b)*180.0/np.pi, "lng": float(l)*180.0/np.pi}
    return jsonify(blh)

@app.route("/get_great_data",methods=["POST"])
def get_great_data():
    sow,data = current_app._get_current_object().Q_list[1].get()
    b,l,h=xyz2blh(float(data[0]),float(data[1]),float(data[2]))  
    blh= {"sow":sow,"lat": float(b)*180.0/np.pi, "lng": float(l)*180.0/np.pi}
    return jsonify(blh)

def web_main(q):
    with open("web.log","w") as logstdout:
        sys.stderr = logstdout
        sys.stdout = logstdout
        app.Q_list=q
        app.run()

if __name__ == "__main__":
    app.debug=True
    app.run()