cmake_minimum_required(VERSION 2.8.3)

project(osam_arm_urdf)

find_package(catkin REQUIRED COMPONENTS
	message_generation
	roscpp
	rospy
	std_msgs
	geometry_msgs
	urdf
	xacro
	message_generation	
)

catkin_package(
	CATKIN_DEPENDS
		roscpp
		rospy
		std_msgs
		geometry_msgs
)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)