#!/usr/bin/env python  

import roslib

roslib.load_manifest('learning_tf')

import rospy



import tf

import geometry_msgs.msg



def handle_coor_pose(msg):

    br = tf.TransformBroadcaster()

    br.sendTransform((3, -2, 0),

                     tf.transformations.quaternion_from_euler(-1.5708, 0.523599, 0.785398),

                     rospy.Time.now(),

                     "coordinate_A",

                     "coordinate_B")



if __name__ == '__main__':

    rospy.init_node('coordinates_tf_broadcaster')

    rospy.Subscriber('/coor_A/pose',

                     geometry_msgs.msg.PoseStamped,

                     handle_coor_pose)

    rospy.spin()
