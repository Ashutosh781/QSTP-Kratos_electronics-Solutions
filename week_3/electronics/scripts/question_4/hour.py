#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('hours',anonymous=True)
h = 0

def hours(m):
    global h
    if m.data == 60:
        h+=1
    if h == 24:
        h = 0
    
    pub.publish(h)

sub = rospy.Subscriber('minute',Int32,hours)
pub = rospy.Publisher('hour',Int32,queue_size=10)
rospy.spin()