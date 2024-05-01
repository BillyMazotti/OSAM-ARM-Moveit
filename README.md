V# OSAM-ARM-Moveit
This repo contains two packages that are used to simulate a custom robot arm desgin for on-orbit assembly and manufacturing tasks.


## Workstation Specs and Dependencies
* Ubuntu 20.04: 
* VMware Install ([VMware Workstation Player 17](https://www.vmware.com/products/workstation-player.html) for Windows | [VMWare Fusion Player](https://customerconnect.vmware.com/en/downloads/info/slug/desktop_end_user_computing/vmware_fusion/13_0)
13 for macOS)
* ROS1 Noetic: [install instructions](https://wiki.ros.org/noetic/Installation/Ubuntu)
* Moveit1 for Noetic: [install from source](https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html)


## Installation Steps
```
mkdir -p ws_osam_arm/src
cd ws_osam_arm
catkin init
cd src
git clone https://github.com/BillyMazotti/OSAM-ARM-Moveit
catkin build
```

## Run the arm in RVIZ
```
source ~/ws_osam_arm/devel/setup.bash
roslaunch moveit_osam_arm_sim demo.launch
```

Run the following comand to load up arm in rviz and gazebo, and enable the end effector to be servoed
```
roslaunch moveit_osam_arm_sim_v2 full_robot_arm_sim.launch
```

Run the folloiwng command to enable keyboard teleop servoing of the end effector
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/servo_server/delta_twist_cmds _stamped:=True
```


## TODO's
Add Python nodes to demo.launch file that write current joint angles to joints_positions.json file and read velocity inputs from ee_velocity.json. Both json file paths will be defined in comms_config.py.


## Steps for implenting custom robot arm
Followed YouTube tutorial to:
1. Created osam_arm_4_urdf_v2 package using ros + solidworks plugin (encountered exceptions)

Exceptions included:
* needed to manually decrease the mass of each link to prevent the manipulator from rubberbanding/shaking uncontrollably, resulting in failed initializations for executing trajectories.
* raised the manipulator off the group to prevent the collision with the gazebo enviornment's ground 

2. Generate the moveit_osam_arm_sim using moveit setup assistant (encountered exceptions)

Exceptions included:
* setup assistant did not automaticall generat the YOUR_PACKAGE_NAME_moveit_controller_manager.launch.xml file discussed, but rather generated ros_control_moveit_controller_manager.launch.xml. To successfullhy incorporate the controller I needed to ensure move_group.launch was calling ros_control_moveit_controller_manager.launch.xml rather than simple_moveit_controller_manager.launch.xml by changing "\<arg name="moveit_controller_manager" default="simple" />" to "\<arg name="moveit_controller_manager" default="ros_control" />"