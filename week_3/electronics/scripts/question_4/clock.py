#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

rospy.init_node('clock1',anonymous=True)
rate = rospy.Rate(1) #1hz
r1 = 0
r2 = 0
r3 = 0
def seconds(s):
    global r1
    r1 = s.data
    if s.data == 60:
        r1 = 0
def minutes(m):
    global r2
    r2 = m.data
    if m.data == 60:
        r2 = 0
def hours(h):
    global r3
    r3 = h.data
    if h.data == 24:
        r3 = 0

while not rospy.is_shutdown():
    rospy.Subscriber('second',Int32,seconds)
    rospy.Subscriber('minute',Int32,minutes)
    rospy.Subscriber('hour',Int32,hours)

    time = "{}:{}:{}".format(r3,r2,r1)
    pub = rospy.Publisher('clock1',String,queue_size=10)
    pub.publish(time)
    rate.sleep()
