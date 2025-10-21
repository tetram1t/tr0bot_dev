from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='async_slam_toolbox_node',
            output='screen',
            parameters=[{
                'slam_toolbox/ros__parameters': PathJoinSubstitution([
                    FindPackageShare('tr0bot'),  # измени на имя своего пакета
                    'config',
                    'mapper_params_online_async.yaml'
                ])
            }],
            arguments=['--ros-args'],
            remappings=[
                ('/scan', '/scan'),
            ]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_laser',
            output='screen',
            arguments=['-0.075', '0', '0.215', '0', '0', '0', 'base_link', 'laser_frame']
        )
    ])
