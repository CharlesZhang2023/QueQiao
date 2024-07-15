# Ego-Task-Manager (QueQiao) 

Language🌍：  [English](./README.md)｜ [简体中文](./README_zh.md)

### Project Introduction

Ego-Task-Manager (QueQiao) is a global task manager for robots designed to enhance the extensibility and global planning capabilities of the Ego-Planner local path planner. Currently, it is mainly used for the FastLab aerial autonomous robot platform at Zhejiang University to quickly generate waypoints. In addition, with the rapid development of drone-related technologies such as trajectory planning, circling, return-to-home, SLAM, and target tracking in recent years, this project aims to provide a bridging platform for these projects and a user-friendly upper computer.

##### Main features:

> 1. Quickly generate waypoints that can be read by Ego-Planner
> 2. Generate circling trajectories: generate circling waypoints through rotation matrices and circle-cutting methods
> 3. Waypoint simulator: quickly calibrate global trajectories through the simulator and automatically generate waypoints.

### Ego-Task-Manager Project Structure

```
Ego-Task-Manager 
|-waypoint_generater.py # Simulator
|-hover.py # Circling trajectory generator, including rotation matrices and circle-cutting functions
|-outputFormater.py # Generates waypoints that can be read by Ego-planner and provides them to ROS
Output # Output
  |-finalWaypoints.txt # Waypoints readable by Ego-planner
  |-fixedPointsTemplet.txt # Template for Ego-planner
  |-wayPoints.txt # Waypoints generated by the upper computer
```

### Dependencies

1. Rospy for communication with the ROS server
2. Turtle for writing the simulator and connecting plugin functions
3. Currently, path planning and obstacle avoidance use EgoPlanner, SLAM uses Vins-mono. It's necessary to study these in advance, and the underlying executor is px4 flight control.

### Usage Instructions

1. Run waypoint_generater.py to automatically open the simulator.
2. Mouse click: Fly to the designated location.
   Press "C": Circle around a point 60 units from the current facing direction.
   Press "H": Return to the starting point.
   Press "E": Circle and return home.
3. After planning the trajectory, press Q to exit and automatically save the waypoints in ./output/waypoint.txt.
4. Run outputFormater to convert the waypoints into a format readable by Ego-planner and output them to ./final_waypoints.txt.
5. Copy the waypoints to the waypoint section of single-run-in-sim.launch under Ego-planner through remote connection and start the Ego-planner simulator.

### Development Plan

1. Write a ROS adapter to add a bidirectional data chain for ROS, enabling direct real-time communication with the drone without the need for copying.
2. Add a plugin extension manager and write a voice control plugin driven by a large language model.
3. Separate related setting parameters into a JSON or YAML parameter file.

 **This project is free software released under the MIT license.**