from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_py',
            executable='turtle_tf2_broadcaster',
            name='turtle_tf2_broadcaster',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        )
    ])