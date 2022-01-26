import obspy
from obspy.core import UTCDateTime
import numpy as np



"""
make an obspy compatible trace object

input file name is the text file made by specfem

returns a trace object
"""

def makeTrace(fname='../OUTPUT_FILES/AA.S4500.BXX.semv'):
    time = UTCDateTime() #just assign the time to be now
    #load data 
    data=np.loadtxt(fname)
    dt =data[-1,0]-data[-2,0]
    #construct trace header
    header = {
        "delta":dt,
        "sampling_rate":int(np.reciprocal(dt)),
        "npts":data.shape[0],
        "location":fname.split('.')[2].split('/')[-1],
        "station":fname.split('.')[3],
        "channel":fname.split('.')[4],
        "starttime":time,
        "endtime":time+dt*data.shape[0]
        }
    return obspy.Trace(data=data[:,1],header=header)

#test code
#test = makeTrace('../OUTPUT_FILES/AA.S4500.BXX.semv')
#test.plot()



