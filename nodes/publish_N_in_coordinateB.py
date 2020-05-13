#!/usr/bin/env python  

import roslib

roslib.load_manifest('robomaster_test1')

import rospy

import math

import tf

import geometry_msgs.msg



if __name__ == '__main__':

    rospy.init_node('publish_N_in_coordinateB')



    listener = tf.TransformListener()


    coordinate_B_vel = rospy.Publisher('coor_B/pose', geometry_msgs.msg.PoseStamped,queue_size=1)


    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():

        try:

            (trans,rot) = listener.lookupTransform('/coordinate_A', '/coordinate_B', rospy.Time(0))

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):

            continue


        cmd = geometry_msgs.msg.PoseStamped()

        cmd.header.frame_id="frame_id"

        cmd.pose.position.x = 1-trans[0]
        cmd.pose.position.y = 1-trans[1]
        cmd.pose.position.z = 1-trans[2]

        cmd.pose.orientation.x = -rot[0]
        cmd.pose.orientation.y = -rot[1]
        cmd.pose.orientation.z = -rot[2]
        cmd.pose.orientation.w = -rot[3]


        coordinate_B_vel.publish(cmd)


        rate.sleep()
