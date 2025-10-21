from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='laser_to_base_link',
            arguments=['0.1', '0.0', '0.15', '0.0', '0.0', '0.0', 'base_link', 'laser_frame']
        ),
    ])