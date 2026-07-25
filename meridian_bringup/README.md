# meridian_bringup

Launch-only bringup package that starts the full Meridian perception pipeline (all nine nodes).

## Nodes launched

| Package | Executable |
|---|---|
| meridian_sensor | sensor_node |
| meridian_seg | seg_node |
| meridian_clip | clip_node |
| meridian_slam | slam_node |
| meridian_geobuilder | geobuilder_node |
| meridian_geotracker | geotracker_node |
| meridian_associator | associator_node |
| meridian_updater | updater_node |
| meridian_graphcore | graphcore_node |

## Launch arguments

| Argument | Default | Description |
|---|---|---|
| dataset_dir | /home/adas/yun/meridian_ws/data/rgbd_dataset_freiburg1_xyz | Path to the TUM freiburg1_xyz dataset, passed to meridian_sensor/sensor_node |

## Build

From the workspace root:

```
colcon build
```

## Run

```
ROS_DOMAIN_ID=123 ros2 launch meridian_bringup meridian.launch.py [dataset_dir:=...]
```

The TUM freiburg1_xyz dataset is expected at the default `dataset_dir` path.
