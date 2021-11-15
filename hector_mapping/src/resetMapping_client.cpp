#include "ros/ros.h"

#include <hector_mapping/ResetMapping.h>
#include <geometry_msgs/Pose.h>

int main(int argc, char **argv){
    ros::init(argc, argv, "resetMapping_client");
    ros::NodeHandle n;
    ros::ServiceClient client = n.serviceClient<hector_mapping::ResetMapping>("resetMapCallback");

    geometry_msgs::Pose resetPose;
    resetPose.position.x = 1;

    hector_mapping::ResetMapping srv;
    srv.request.initial_pose = resetPose;

    if (client.call(srv))
    {
        ROS_INFO("Successfully reset initial pose to xxx");
    }
    else
    {
        ROS_ERROR("Failed to reset initial pose");
    }
    return 0;
}