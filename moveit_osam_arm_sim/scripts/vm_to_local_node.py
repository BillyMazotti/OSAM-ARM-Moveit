#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import String
import numpy as np
from sensor_msgs.msg import JointState
from write_json import write_to_json

joint_positions = {
		"timestamp": 0.0,
		"joints" : np.zeros(8)}

def callback(data):
    
    json_path = "/run/user/1000/gvfs/sftp:host=billys-macbook-pro-5.local/Users/billymazotti/github/DataComms/selected_json_file.json"
    joint_positions["timestamp"] = data.header.stamp.secs + 1e-9 * data.header.stamp.nsecs
    joint_positions["joints"] = list(data.position)
    # print(joint_positions)
    write_to_json(json_path,joint_positions)

    # write_to_json()
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, callback)

    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()