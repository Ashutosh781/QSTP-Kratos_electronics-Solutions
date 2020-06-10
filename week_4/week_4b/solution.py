#! /usr/bin/env python

import rospy
import tf
import tf2_ros
from geometry_msgs.msg import Transform,TransformStamped
import numpy as np

def msg_from_transform(T):
    msg1 = Transform()  #Declaring Transform object
    q = tf.transformations.quaternion_from_matrix(T)
    t = tf.transformations.translation_from_matrix(T)

    #Extracting elements from transform matrix
    msg1.translation.x = t[0]
    msg1.translation.y = t[1]
    msg1.translation.z = t[2]
    msg1.rotation.x = q[0]
    msg1.rotation.y = q[1]
    msg1.rotation.z = q[2]
    msg1.rotation.w = q[3]

    return msg1



def publish_transforms():
    T1 = tf.transformations.concatenate_matrices(
        tf.transformations.quaternion_matrix(tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)),
        tf.transformations.translation_matrix((0.0, 1.0, 1.0))
    ) #Base to camera
        

    T2 = tf.transformations.concatenate_matrices( 
        tf.transformations.quaternion_matrix(tf.transformations.quaternion_about_axis(1.5, (0,0,1))),
        tf.transformations.translation_matrix((0.0, 1.0, 0.0))
    ) #Camera to object


    final_tf = np.dot(T1,T2)  #Total transform from base to object
    final_tf_stamped = TransformStamped()
    final_tf_stamped.header.stamp = rospy.Time.now()
    final_tf_stamped.header.frame_id = 'base'
    final_tf_stamped.child_frame_id = 'object'
    final_tf_stamped.transform = msg_from_transform(final_tf)
    br.sendTransform(final_tf_stamped)  #passing to broadcaster



if __name__ == "__main__":
    rospy.init_node('solution', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(1)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(1)
        