#!/usr/bin/env python
import rospy
#from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def translate(sensor_val, in_from, in_to, out_from, out_to):
    out_range = out_to - out_from
    in_range = in_to - in_from
    in_val = sensor_val - in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val

def get_target (msg):
    #joystick_output = msg.axes
    #rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
    #print msg.angular.z, type(msg.angular.z)
    #joystick_output = msg.angular.z
    target = translate(msg.angular.z, -1, 1, 4095, 0)
    print 'left - right', msg.angular.z, 'target', int(target)

rospy.init_node('my_jrk_joystick')
#sub = rospy.Subscriber ('/joy', Joy, get_target)
sub = rospy.Subscriber ('/cmd_vel', Twist, get_target)
r = rospy.Rate(1)
while not rospy.is_shutdown():
	r.sleep()