# OSAM-ARM-Moveit

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







