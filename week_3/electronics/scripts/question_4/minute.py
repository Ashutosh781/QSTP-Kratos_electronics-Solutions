#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('minutes',anonymous=True)
m = 0

def minutes(s):
    global m
    if s.data == 60:
        m+=1
    if m == 60:
        m = 0
    
    pub.publish(m)

sub = rospy.Subscriber('second',Int32,minutes)
pub = rospy.Publisher('minute',Int32,queue_size=10)
rospy.spin()