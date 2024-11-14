from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    # Get share directory for turtlebot4_navigation
    tb4_nav_dir = get_package_share_directory('turtlebot4_navigation')
    
    # Get share directory for task_7
    view_robot_dir = get_package_share_directory('task_7')

    # Retrive launch file for SLAM
    slam_launch_path = os.path.join(tb4_nav_dir,'launch','localization.launch.py')
    
    # Retrieve launch file and map for RViz 
    view_robot_path = os.path.join(view_robot_dir,'launch','view_robot.launch.py')
    map_path = os.path.join(view_robot_dir, 'maps', 'classroom_map.yaml')

    # Launch SLAM with map
    slam_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(slam_launch_path),launch_arguments={'map': map_path}.items())
    
    # Launch RViz with map
    view_robot_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(view_robot_path),launch_arguments={'map': map_path}.items())
    
    return LaunchDescription([
        slam_launch,
        view_robot_launch,
        Node(
            package='task_7',
            executable='auto_navigator',
            namespace='/robot',
            output="screen"
        )
    ])