#!/usr/bin/env python3

from std_srvs.srv import Trigger

import rospy



def occupancy_map_client():
    rospy.wait_for_service('reset_map')
    try:
        mapCallback_handler = rospy.ServiceProxy('reset_map', Trigger)
        resp = mapCallback_handler()
        return resp.success

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    occupancy_map_client()