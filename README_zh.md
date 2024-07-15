# Ego-Task-Manager 鹊桥

Language🌍：  [English ](./README)｜ [简体中文](./README_zh.md)

### 📒项目简介

Ego-Task-Manager(鹊桥) 是一款机器人全局目标管理器，旨在提高Ego-planner局部路径规划器的扩展性与全局规划能力，目前主要用于浙大FastLab空中自主机器人平台，快捷生成航点。此外，轨迹规划、盘旋、返航、SLAM、目标跟踪，近年来无人机相关技术蓬勃发展，本项目旨在为这些项目提供一个桥接平台并提供一个用户友好的上位机。

##### 主要功能如下:

> 1. 快速生成Ego-Planner可读取的航点
> 2. 生成盘旋轨迹： 通过旋转矩阵和割圆法生成盘旋航点
> 3. 航点模拟器，可以通过模拟器快速标定全局轨迹，并自动生成航点。

### Ego-Task-Manager 项目结构

```
Ego-Task-Manager 
|-waypoint_generater.py #模拟器
|-hover.py #盘旋轨迹生成器，包括旋转矩阵和割圆函数
|-outputFormater.py #生成Ego-planner可以读取的航点并提供给ROS
Output#输出
  |-finalWaypoints.txt #Ego-planner可读取的航点
  |-fixedPointsTemplet.txt #Ego—planner模版模板
  |-wayPoints.txt #上位记生成的航点
```

### 相关依赖

1. Rospy 用于负责和ROS服务器的通讯

2. Turtle 用于编写模拟器并连接插件函数
3. 目前路径规划于避障使用EgoPlanner，SLAM使用Vins-mono，需提前了解学习，底层执行器为px4飞控，

### 使用说明

1. 运行waypoint_generater.py 将自动打开模拟器

2. 鼠标点击：飞往制定地点

   按“C”:以其面对方向60单位为圆心盘旋一周

   按“H” 返航至出发点

   按“E”: 盘旋并返航

3. 规划完轨迹按Q退出并自动保存航点，保存在./output/waypoint.txt

4. 运行outputFormater将航点转化为Ego-planner可以读取的格式，并输出至./final_waypoints.txt

5. 通过远程连接将航点复制到Ego-planner下的single-run-in-sim.launch中的航点部分，并启动Ego-planner模拟器

### 开发计划

1. 编写ROSadapter，添加ROS的双向数据链可直接与无人机实时通讯，无需复制。
2. 添加插件扩展管理器，并编写一个大语言模型驱动的语音控制插件。
3. 将相关设置参数独立出来，编写为一个json或yaml参数文件

 **本项目为自由软件，在MIT许可证下发布**