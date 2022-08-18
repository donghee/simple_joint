from launch import LaunchDescription

import launch.actions
import launch_ros.actions


def generate_launch_description():

    return LaunchDescription([
        launch_ros.actions.Node(
            package='simple_joint_description',
            executable='wheel_steer.py',
            output='screen',
            arguments=["0.5"]),
    ])