#include "ros/ros.h"

#include <hector_mapping/ResetMapping.h>
#include <nav_msgs/GetMap.h>
#include <iostream>

int main(int argc, char **argv){
    ros::init(argc, argv, "mapService_client_");
    ros::NodeHandle n;
    std::string file_path_;
    n.param<std::string>("file_path", file_path_, "occuMap.csv");

    ros::ServiceClient client = n.serviceClient<nav_msgs::GetMap>("mapCallback");
    nav_msgs::GetMap srv_map;
    // srv_map.request.initial_pose = resetPose;

    if (client.call(srv_map))
    {
      ROS_INFO("mapService_client_Node: Map service called successfully");
      const nav_msgs::OccupancyGrid& map(srv_map.response.map);
    }
    else
    {
        ROS_ERROR("Failed to save occu map...");
    }
    return 0;
}