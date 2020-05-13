#!/usr/bin/env python  

import roslib

roslib.load_manifest('robomaster_test1')

import rospy

import tf

import geometry_msgs.msg

import std_msgs.msg

if __name__=='__main__':

    rospy.init_node('publish_M_in_coordinateA')

    coordinateA_vel = rospy.Publisher('coor_A/pose', geometry_msgs.msg.PoseStamped,queue_size=1)

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():

        cmd=geometry_msgs.msg.PoseStamped()


        cmd.header.frame_id="frame_id"

        cmd.pose.position.x=1
        cmd.pose.position.y=1
        cmd.pose.position.z=1

        coordinateA_vel.publish(cmd)

        rate.sleep()



