#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point

def publisher():
    pub = rospy.Publisher('end_effector_position',Point,queue_size=10)
    rospy.init_node('ee_pose_pub',anonymous=True)
    rate =rospy.Rate(1)  #1hz
    while not rospy.is_shutdown():
        ee_pose = Point()
        ee_pose.x = 1
        ee_pose.y = 1

        pub.publish(ee_pose)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass