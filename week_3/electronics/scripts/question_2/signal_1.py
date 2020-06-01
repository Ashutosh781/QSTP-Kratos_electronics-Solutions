#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def signal_1():
    pub = rospy.Publisher('s1',String,queue_size=10)
    rospy.init_node('S1',anonymous=True)
    rate = rospy.Rate(1) #1hz
    while not rospy.is_shutdown():
        for i in range(10):
            s1_msg = 'green'
            pub.publish(s1_msg)
            rate.sleep()
        for j in range(10):
            s1_msg = 'red'
            pub.publish(s1_msg)
            rate.sleep()


if __name__ == "__main__":
    try:
        signal_1()
    except rospy.ROSInterruptException:
        pass
