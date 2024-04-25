#!/usr/bin/env python3
import sys
import subprocess
import rospy

def change_controller_configuration(controller_to_use):

    if controller_to_use == "velocity":
        controller_to_start = "joint_group_position_controller"
        controller_to_stop = "arm_controller"
    
    elif controller_to_use == "position":
        controller_to_stop = "joint_group_position_controller"
        controller_to_start = "arm_controller"
    
    else:
        rospy.logerr(f"controller_to_use value of '{controller_to_use}' is invalid input to change_controller_configuration()")
        return

    controller_conf = f"start_controllers: [{controller_to_start}] \
                        \nstop_controllers: [{controller_to_stop}] \
                        \nstrictness: 1 \
                        \nstart_asap: false \
                        \ntimeout: 0.0"

    subprocess.run(["rosservice", "call", "/controller_manager/switch_controller", controller_conf])


if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print(sys.argv)
        rospy.logerr(f"chagne_controller.py requires 'position' or 'velocity' as the first and only argument")
    else:
        controller_type_to_use = sys.argv[1]
        change_controller_configuration(controller_type_to_use)