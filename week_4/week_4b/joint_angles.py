#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point
import math

def joint_angles(msg1):
    x = msg1.x
    y = msg1.y

    l1 = 1
    l2 = 1

    theta2 = math.acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
    theta1 = math.atan2(y,x) - math.atan2((l2*math.sin(theta2)),(l1 + l2*math.cos(theta2)))

    angles.x = theta1
    angles.y = theta2
    
    pub.publish(angles)

if __name__ == "__main__":
    try:
        rospy.init_node('joint_angles',anonymous=True)
        pub = rospy.Publisher('joint_angles',Point,queue_size=10)
        rate = rospy.Rate(1)  #1hz

        while not rospy.is_shutdown():
            angles = Point()
            sub = rospy.Subscriber('end_effector_position',Point,joint_angles)
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
