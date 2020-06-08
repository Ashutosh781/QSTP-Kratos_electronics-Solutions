#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

def rotate(msg1):
    orientation_q = msg1.pose.pose.orientation
    orientation = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]

    global roll,pitch,yaw

    (roll,pitch,yaw) = euler_from_quaternion(orientation)  #transformation

    if yaw >= angle:
        vel.angular.z = 0
        pub.publish(vel)

    else:
        vel.angular.z = 1
        pub.publish(vel)

if __name__ == "__main__":
    try:
        rospy.init_node('rotate',anonymous=True)
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        rate = rospy.Rate(1)

        r = float(input('Enter Angle in 0 to 180 degree : '))

        angle = r*math.pi/180  #conversion to radians

        while not rospy.is_shutdown():
            vel = Twist()
            sub = rospy.Subscriber('/odom',Odometry,rotate)
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
