from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    dataset_dir_arg = DeclareLaunchArgument(
        'dataset_dir',
        default_value='/home/adas/yun/meridian_ws/data/rgbd_dataset_freiburg1_xyz')

    return LaunchDescription([
        dataset_dir_arg,

        Node(
            package='meridian_sensor',
            executable='sensor_node',
            output='screen',
            parameters=[{'dataset_dir': LaunchConfiguration('dataset_dir')}]),

        Node(
            package='meridian_seg',
            executable='seg_node',
            output='screen'),

        Node(
            package='meridian_clip',
            executable='clip_node',
            output='screen'),

        Node(
            package='meridian_slam',
            executable='slam_node',
            output='screen'),

        Node(
            package='meridian_geobuilder',
            executable='geobuilder_node',
            output='screen'),

        Node(
            package='meridian_geotracker',
            executable='geotracker_node',
            output='screen'),

        Node(
            package='meridian_associator',
            executable='associator_node',
            output='screen'),

        Node(
            package='meridian_updater',
            executable='updater_node',
            output='screen'),

        Node(
            package='meridian_graphcore',
            executable='graphcore_node',
            output='screen'),
    ])
