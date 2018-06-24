#!/usr/bin/env python
import rospy
from ackermann_msgs.msg import AckermannDriveStamped
'''
The physical characteristics of my steering and angle sensor potentiometer are such that a hard 
right turn equals a target value of 2400.  Straight or middle is a target of 1450 and 
hard left is a target of 450.  Therefore my mapping will be 2400 - 1450 when turning right and 
1450 - 450 when turning left. When msg.drive.steering_angle is ?? the joystick is pushed left and when 
msg.drive.steering_angle is ?? the joystick is pushed right.

TODO: 
1. Using the joystick as input the steering_angle output does not make sense.  Mostly I get 0 as the output.  Sometimes the output is c-1.55 - need to fix
2. Add logic to translate values for when the joystick is pushed left or right and map to my physical configuration
   There will be a mapping to use when turning left and a slightly different mapping when turning right.

'''
def translate(sensor_val, in_from, in_to, out_from, out_to):  # not used yet, until I resolve understanding the output of msg.drive.steering_angle
    out_range = out_to - out_from
    in_range = in_to - in_from
    in_val = sensor_val - in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val

def get_target (msg):
    print 'left - right', msg.drive.steering_angle

rospy.init_node('my_jrk_joystick_ackermann')
sub = rospy.Subscriber ('/ackermann_cmd', AckermannDriveStamped, get_target)
r = rospy.Rate(1)
while not rospy.is_shutdown():
	r.sleep()