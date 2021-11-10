#!usr/bin/env python
'''ros utils'''
import rospy
from hector_mapping.msg import HectorDebugInfo, HectorIterData

'''math tool'''
import csv
import numpy as np
import time
import statistics

count = 0
latList = []
lonList= []

def cbCost(msg):
    global count, latList, lonList
    
    
    with open('/home/anny/HectorDebugCost.csv', 'a+') as csvfile: # or w
        writer = csv.writer(csvfile)
        if len(msg.iterData) > 1:
            tmp = msg.iterData[0]
            tmp1 = msg.iterData[1]
            tmp2 = msg.iterData[2]
            writer.writerow([ tmp.cost,tmp1.cost,tmp2.cost ])
        else: 
            writer.writerow([ -1,-1,-1 ])


if __name__ == "__main__":
    rospy.init_node("record_HectorDebugInfoProvider_node", anonymous=True)
    subGPS = rospy.Subscriber("hector_debug_info", HectorDebugInfo, cbCost)
    rospy.spin()
