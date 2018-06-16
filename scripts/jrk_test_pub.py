#!/usr/bin/python

import rospy
import std_msgs
print("starting jrk_test_pub")

def talker():
    jrk_pub = rospy.Publisher('jrk_target', std_msgs.msg.UInt16, queue_size=1)
    rospy.init_node('test_jrk_pub')
    for i in [0, 800, 1200, 1500, 2000, 2500, 3000, 4000]:
        print(i)
        jrk_pub.publish(i)
        rospy.sleep(10)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass    