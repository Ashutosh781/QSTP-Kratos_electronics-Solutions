#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub  = rospy.Publisher('new',String,queue_size=10)
    rospy.init_node('hello_world_pub',anonymous=True)
    rate = rospy.Rate(15)  #15hz
    while not rospy.is_shutdown():
        msg1 = 'Hello World!'
        pub.publish(msg1)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass