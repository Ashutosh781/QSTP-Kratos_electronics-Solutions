#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def print_it(msg1):
    print(msg1.data)

def subscriber():
    rospy.init_node('hello_world_sub',anonymous=True)
    rospy.Subscriber('new',String,print_it)
    rospy.spin()

if __name__ == "__main__":
    subscriber()