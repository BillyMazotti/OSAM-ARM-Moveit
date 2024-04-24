V# OSAM-ARM-Moveit
This repo contains two packages that are used to simulate a custom robot arm desgin for on-orbit assembly and manufacturing tasks.


## Workstation Specs and Dependencies
* Ubuntu 20.04
* ROS1 Noetic ([install instructions](https://wiki.ros.org/noetic/Installation/Ubuntu))
* Moveit1 
    * Recommended: install from binary: `sudo apt install ros-noetic-moveit`
    * ([install from source](https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html))


## Installation Steps
For standalone workspace
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