#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import String
import numpy as np
from sensor_msgs.msg import JointState
from read_write_json import write_to_json, read_json
import numpy as np
import math

from comms_config import joints_positions_json_path, ee_velocity_json_path
from geometry_msgs.msg import TwistStamped, Twist

import moveit_commander
import time

PI = math.pi

end_effector_speed = 1.5

joint_positions = {
		"timestamp": 0.0,
		"joints" : np.zeros(8).tolist()}

class OSAMArmCommunications:

    def __init__(self):
        self.pub_endeffector_velocity = rospy.Publisher("/servo_server/delta_twist_cmds", TwistStamped, queue_size = 10) # publish end-effecotr velocity
        self.sub_joint_angles = rospy.Subscriber("/joint_states",JointState,self.callback_joint_states)
        self.ue_command_timestamp = -1.0

        group_name = "endeffector"
        self.group = moveit_commander.MoveGroupCommander(group_name)
        self.gripper_state = 0    # 0 = open, 1 = closed

    # def execute_gripper(self, new_gripper_pose):
    #     joint_goal = self.group.get_current_joint_values()

    #     if new_gripper_pose:    # is closed pose
    #         joint_goal[0] = 0.04
    #         joint_goal[1] = 0.04
    #     else:
    #         joint_goal[0] = 0.0
    #         joint_goal[1] = 0.0

    #     self.group.go(joint_goal, wait=True)

        

    def callback_joint_states(self,data):

        # read the input velocity command
        velocity_commands = read_json(ee_velocity_json_path)
        if velocity_commands is not None:   # confirm we recieved velocity commands
            self.ue_command_timestamp = velocity_commands["timestamp"]
            new_velocity_command = TwistStamped()
            new_velocity_command.header.stamp = rospy.Time.now()
            new_velocity_command.twist.linear.x = velocity_commands["val1"] *end_effector_speed
            new_velocity_command.twist.linear.y = velocity_commands["val2"] *end_effector_speed
            new_velocity_command.twist.linear.z = velocity_commands["val3"] *end_effector_speed
            new_velocity_command.twist.angular.x = velocity_commands["val4"]*end_effector_speed
            new_velocity_command.twist.angular.y = velocity_commands["val5"]*end_effector_speed
            new_velocity_command.twist.angular.z = velocity_commands["val6"]*end_effector_speed
            self.pub_endeffector_velocity.publish(new_velocity_command)

            # execute gripper
            # if velocity_commands["val7"] is not self.gripper_state:
            #     print("from ue: ",velocity_commands["val7"])
            #     print("recorded status: ", self.gripper_state)
            #     self.execute_gripper(velocity_commands["val7"])
            #     self.gripper_state = velocity_commands["val7"]

        

        # write the most recent joint states
        joint_positions["timestamp"] = data.header.stamp.secs + 1e-9 * data.header.stamp.nsecs
        data_deg_mm = np.array(data.position)
        data_deg_mm[:7] *= 180.0/PI
        data_deg_mm[0] *= -1
        data_deg_mm[1] *= -1
        data_deg_mm[3] *= -1

        for joint_idx, joint_val in enumerate(data_deg_mm):
            joint_positions[f"joint{joint_idx+1}"] = joint_val

        write_to_json(joints_positions_json_path,joint_positions)

        # rounded_joint_positions = [round(elem, 2) for elem in data_deg_mm]
        # print(f'Publishign path [{joint_positions["timestamp"]}]: {rounded_joint_positions}')
    

if __name__ == '__main__':

    rospy.init_node('osam_comms', anonymous=True)
    OSAMArmCommunications()
    rospy.spin()