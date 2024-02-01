#!/bin/bash
cleanup() {
  echo "Stopping ROS launch files..."
  # Terminate background processes
  kill -- -$$
  exit 0
}

# Trap Ctrl+C (SIGINT) signal and call the cleanup function
trap cleanup SIGINT

ros2 launch islington_amr_description gazebo.launch.py &
sleep 10 
ros2 launch islington_nav2 islington_bringup_launch.py 
# ros2 run islington_nav2 islington_nav_cmd.py &

wait
