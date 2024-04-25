#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import String
import numpy as np
from sensor_msgs.msg import JointState
from write_json import write_to_json
import numpy as np
import math

from comms_config import joints_positions_json_path, ee_velocity_json_path

PI = math.pi

joint_positions = {
		"timestamp": 0.0,
		"joints" : np.zeros(8).tolist()}

def callback(data):
    
    joint_positions["timestamp"] = data.header.stamp.secs + 1e-9 * data.header.stamp.nsecs
    data_deg_mm = np.array(data.position)
    data_deg_mm[:7] *= 180.0/PI
    joint_positions["joints"] = l=data_deg_mm.tolist()
    write_to_json(joints_positions_json_path,joint_positions)

    rounded_joint_positions = [round(elem, 2) for elem in joint_positions["joints"]]
    print(f'Publishign path [{joint_positions["timestamp"]}]: {rounded_joint_positions}')
    
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