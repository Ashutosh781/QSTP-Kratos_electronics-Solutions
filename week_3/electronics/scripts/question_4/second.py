#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def seconds():
    pub = rospy.Publisher('second',Int32,queue_size=10)
    rospy.init_node('seconds',anonymous=True)
    rate = rospy.Rate(1) #1hz
    while not rospy.is_shutdown():
        for i in range(1,61):
            pub.publish(i)
            rate.sleep()

if __name__ == "__main__":
    try:
        seconds()
    except rospy.ROSInterruptException:
        pass
