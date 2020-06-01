#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('S2',anonymous=True)

def signal_2(s1_msg):
    if s1_msg.data == 'green':
        s2_msg = 'red'
        pub.publish(s2_msg)
    
    else:
        s2_msg = 'green'
        pub.publish(s2_msg)

sub = rospy.Subscriber('s1',String,signal_2)
pub = rospy.Publisher('s2',String,queue_size=10)
rospy.spin()
