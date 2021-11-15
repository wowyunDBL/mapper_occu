#!/usr/bin/env python3

from __future__ import print_function

import nav_msgs.GetMap.srv  
import rospy



def occupancy_map_client():
    rospy.wait_for_service('mapCallback')
    try:
        mapCallback_handler = rospy.ServiceProxy('mapCallback', GetMap)
        map = mapCallback_handler()
        

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    occupancy_map_client()