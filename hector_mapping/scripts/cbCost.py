#! /usr/bin/env python3

'''ros utils'''
import rospy
from hector_mapping.msg import HectorDebugInfo, HectorIterData
from nav_msgs.msg import Odometry

'''math tool'''
import csv
import numpy as np
import time
import statistics

count = 0
latList = []
lonList= []
timestamp = 0

def cbCost(msg):
    global count, latList, lonList, timestamp
    
    with open('/home/ncslaber/HectorDebugCost.csv', 'a+') as csvfile: # or w
        writer = csv.writer(csvfile)
        if len(msg.iterData) > 1:
            tmp = msg.iterData[0]
            tmp1 = msg.iterData[1]
            tmp2 = msg.iterData[2]
            writer.writerow([ timestamp, tmp.cost,tmp1.cost,tmp2.cost, tmp.eflag,tmp1.eflag,tmp2.eflag ])
        else: 
            writer.writerow([ timestamp, -1,-1,-1,-1,-1,-1 ])

def cbOdom(msg):
    global timestamp
    timestamp = msg.header.stamp.secs + msg.header.stamp.nsecs*1e-9

if __name__ == "__main__":
    rospy.init_node("record_HectorDebugInfoProvider_node", anonymous=True)
    subGPS = rospy.Subscriber("hector_debug_info", HectorDebugInfo, cbCost) 
    subOdom = rospy.Subscriber("/outdoor_waypoint_nav/odometry/filtered_map", Odometry, cbOdom)
    
    rospy.spin()
