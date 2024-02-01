#!/usr/bin/env python3

from geometry_msgs.msg import PoseStamped, Twist
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
import yaml
import os
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
from nav_msgs.msg import Odometry
import time
from geometry_msgs.msg import Quaternion
from tf_transformations import quaternion_from_euler

class NavigationController(Node):

	def __init__(self):
		
		rclpy.init()  # Initialize rclpy here
		super().__init__('nav_dock')

		self.vel_pub = self.create_publisher(Twist, "/cmd_vel", 10)
		self.vel_msg = Twist()
		self.navigator = BasicNavigator()
		self.robot_pose = [0, 0]

	def nav_reach(self, goal):
		while not self.navigator.isTaskComplete():
			feedback = self.navigator.getFeedback()

			if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
				self.navigator.cancelTask()

		result = self.navigator.getResult()
		if result == TaskResult.SUCCEEDED:
			print(f'Goal {str(goal)} succeeded!')
		elif result == TaskResult.CANCELED:
			print('Goal was canceled!')
		elif result == TaskResult.FAILED:
			print('Goal failed!')
		else:
			print('Goal has an invalid return status!')

	def nav_theta(self,angle):		
		x,y,z,w=quaternion_from_euler(0,0,angle)
		return (x,y,z,w)
	
	def main(self):
		package_name = 'islington_nav2'
		config = "config/config.yaml"

		islington_nav2_dir = get_package_share_directory('islington_nav2')

		pkg_share = FindPackageShare(package=package_name).find(package_name)
		config_path = os.path.join(pkg_share, config)
		with open(config_path, 'r') as infp:
			pos_goal = infp.read()

		data_dict = yaml.safe_load(pos_goal)

		positions = data_dict['position']
		goal1_coordinates = positions[0]['goal1']
		goal2_coordinates = positions[1]['goal2']
		goal3_coordinates = positions[2]['goal3']

		goal_theta_1=self.nav_theta(goal1_coordinates[2])
		goal_theta_2=self.nav_theta(goal2_coordinates[2])
		goal_theta_3=self.nav_theta(goal3_coordinates[2])
		
		goal_list = ["goal1", "goal2", "goal3"]

		goal_pick_1 = PoseStamped()
		goal_pick_1.header.frame_id = 'map'
		goal_pick_1.header.stamp = self.navigator.get_clock().now().to_msg()
		goal_pick_1.pose.position.x = goal1_coordinates[0]
		goal_pick_1.pose.position.y = goal1_coordinates[1]
		goal_pick_1.pose.orientation.x = goal_theta_1[0]
		goal_pick_1.pose.orientation.y = goal_theta_1[1]
		goal_pick_1.pose.orientation.z = goal_theta_1[2]
		goal_pick_1.pose.orientation.w = goal_theta_1[3]
		
		
		goal_pick_2 = PoseStamped()
		goal_pick_2.header.frame_id = 'map'
		goal_pick_2.header.stamp = self.navigator.get_clock().now().to_msg()
		goal_pick_2.pose.position.x = goal2_coordinates[0]
		goal_pick_2.pose.position.y = goal2_coordinates[1]
		goal_pick_2.pose.orientation.x = goal_theta_2[0]
		goal_pick_2.pose.orientation.y = goal_theta_2[1]
		goal_pick_2.pose.orientation.z = goal_theta_2[2]
		goal_pick_2.pose.orientation.w = goal_theta_2[3]


		goal_pick_3 = PoseStamped()
		goal_pick_3.header.frame_id = 'map'
		goal_pick_3.header.stamp = self.navigator.get_clock().now().to_msg()
		goal_pick_3.pose.position.x = goal3_coordinates[0]
		goal_pick_3.pose.position.y = goal3_coordinates[1]
		goal_pick_3.pose.orientation.x = goal_theta_3[0]
		goal_pick_3.pose.orientation.y = goal_theta_3[1]
		goal_pick_3.pose.orientation.z = goal_theta_3[2]
		goal_pick_3.pose.orientation.w = goal_theta_3[3]



		# Define other drop goals...

		self.navigator.waitUntilNav2Active()
		self.navigator.goToPose(goal_pick_1)
		self.nav_reach(goal_list[0])

		self.navigator.goToPose(goal_pick_2)
		self.nav_reach(goal_list[1])
		
		self.navigator.goToPose(goal_pick_3)
		self.nav_reach(goal_list[2])

		exit(0)

if __name__ == '__main__':
	nav_controller = NavigationController()
	nav_controller.main()
