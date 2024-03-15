# OSAM-ARM-Moveit
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








