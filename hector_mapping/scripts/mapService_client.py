#!/usr/bin/env python3

from std_srvs.srv import Trigger

import rospy



def occupancy_map_client():
    rospy.wait_for_service('/reset_map')
    print("here")
    try:
        mapCallback_handler = rospy.ServiceProxy('/reset_map', Trigger)
        print("here")
        resp = mapCallback_handler()
        print("here")
        return resp.success

    except rospy.ServiceException as e:
        print("Service call failed: %s \n"%e)

if __name__ == "__main__":
    print("ok? " + occupancy_map_client())