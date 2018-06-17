#!/usr/bin/env python
# this program will subscribe to the joystick and output a target for the jrk motor controller to complete
import rospy
from sensor_msgs.msg import Joy

def get_target (msg):
    print msg.axes

rospy.init_node('my_jrk_joystick')
sub = rospy.Subscriber ('/joy', Joy, get_target)
r = rospy.Rate(1)  
while not rospy.is_shutdown():  
    r.sleep()