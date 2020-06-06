#! /usr/bin/env/python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def translate(msg1):
    x_curr = msg1.pose.pose.position.x
    y_curr = msg1.pose.pose.position.y

    dist = (x_curr**2 + y_curr**2)**0.5

    if dist >= 5:
        vel.linear.x = 0
        pub.publish(vel)
    
    else:
        vel.linear.x = 0.22
        pub.publish(vel)

if __name__ == "__main__":
    try:
        rospy.init_node('move',anonymous=True)
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        rate = rospy.Rate(1)  #1hz
        
        while not rospy.is_shutdown():
            vel = Twist()
            sub = rospy.Subscriber('/odom',Odometry,translate)
            rate.sleep()
    
    except rospy.ROSInterruptException:
        pass
    