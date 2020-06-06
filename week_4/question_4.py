#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('rotate',anonymous=True)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
rate = rospy.Rate(1)  #1hz

R = float(input('Enter the radius of the circle for turtlebot in m : '))

V = 0.22   #linear velocity of robot in m/sec
W_z = V/R  #angular velocity of robot in rad/sec

vel = Twist()
vel.linear.x = V
vel.angular.z = W_z

rest = Twist()
rest.linear.x = 0
rest.angular.z = 0

try:
    while not rospy.is_shutdown():
        pub.publish(vel)
        rate.sleep()
except rospy.ROSInterruptException:
    pub.publish(rest)