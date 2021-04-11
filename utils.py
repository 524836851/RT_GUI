#-*-coding:utf-8-*-
#!/usr/bin/python
# author: zhShen
import glv
import datetime
from math import *
from numpy import *
import numpy as np

def blh2xyz(B,L,H):
    sB = sin(B);
    cB = cos(B);
    sL = sin(L);
    cL = cos(L);
    N = glv.a/sqrt(1-glv.e2*sB**2);
    X = (N+H)*cB*cL;
    Y = (N+H)*cB*sL;
    Z = (N*(1-glv.e2)+H)*sB;
    return array([X,Y,Z]);

def xyz2blh(X,Y,Z):
    bell = glv.a*(1.0-1.0/glv.f);                          
    ss = sqrt(X*X+Y*Y);   
    zps   = Z/ss;
    theta = atan( (Z*glv.a) / (ss*glv.b) );
    sin3  = sin(theta) * sin(theta) * sin(theta);
    cos3  = cos(theta) * cos(theta) * cos(theta);
    
    #Closed formula
    B = atan((Z + glv.ep2 * glv.b * sin3) / (ss - glv.e2 * glv.a * cos3));
    L = atan2(Y,X);
    nn = glv.a/sqrt(1.0-glv.e2*sin(B)*sin(L));
    H = ss/cos(B) - nn;

    i=0;
    while i<=100:
        nn = glv.a/sqrt(1.0-glv.e2*sin(B)*sin(B));
        hOld = H;
        phiOld = B;
        H = ss/cos(B)-nn;
        B = atan(zps/(1.0-glv.e2*nn/(nn+H)));
        if abs(phiOld-B) <= 1.0e-11 and abs(hOld-H) <= 1.0e-5:
            # always convert longitude to 0-360
            if L < 0.0 :
                L += 2 * pi;
                break;

        i+=1;


    return array([B,L,H])



def xyz2enu(XYZ=[],XYZ_Ref=[]):

    [b,l,h]=xyz2blh(XYZ[0],XYZ[1],XYZ[2])

    r=[XYZ[0]-XYZ_Ref[0], XYZ[1]-XYZ_Ref[1], XYZ[2]-XYZ_Ref[2]]


    sinPhi = sin(b)
    cosPhi = cos(b)
    sinLam = sin(l)
    cosLam = cos(l)

    N = -sinPhi * cosLam * r[0] - sinPhi * sinLam * r[1] + cosPhi * r[2]
    E = -sinLam * r[0] + cosLam * r[1]
    U = +cosPhi * cosLam * r[0] + cosPhi * sinLam * r[1] + sinPhi * r[2]

    return np.array([E,N,U])

def sow2hms(sow):
    sow = float(sow)
    sod=sow%86400
    utc_time = datetime.datetime.utcnow() 
    h=int(sod/3600.0)
    m=int((sod-h*3600.0)/60.0)
    s=float(sod-h*3600-m*60)
    return f'{utc_time.year:4d}-{utc_time.month:02d}-{utc_time.day:2d} {h:02d}:{m:02d}:{s:04.1f}'

def sow2datetime(sow):
    sow = float(sow)
    sod=sow%86400
    utc_time = datetime.datetime.utcnow() 
    h=int(sod/3600.0)
    m=int((sod-h*3600.0)/60.0)
    s=int(sod-h*3600-m*60)
    return datetime.datetime(utc_time.year,utc_time.month,utc_time.day,h,m,s)


def get_diff(item1,item2):
    enuDiff = xyz2enu(item1,item2)
    return [ f"{item:.2f}" for item in enuDiff]

def get_diff_data(Q1,Q2):
    '''
    Q1: [sow,xyz]
    Q2: [sow,xyz]
    '''
    item1 = Q1.get()
    item2 = Q2.get()
    while True:
        if int(item1[0])==int(item2[0]):
            break
        if int(item1[0]) < int(item2[0]):
            item1 = Q1.get()
        else:
            item2 = Q2.get()
    sow = item1[0]
    enuDiff= get_diff(item1[1],item2[1])
    return {"sow":sow,"diffE":enuDiff[0],"diffN":enuDiff[1],"diffU":enuDiff[2]}