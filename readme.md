Detector server for ROS
===

This node listens for specific datagram on any link on port 21337. 

Client has to send UDP datagram containing `ROS`, then server checks from which network client send request. Then it responds with `ACK` followed by IP address and port of rosbridge server.

Instalation
===

To install this node do the following:
1. Go to catkin workspace and clone repository into __src__ folder
```
git clone https://github.com/hasashin/ros-detector-server
```

2. Then install required packages:
```
sudo sudo apt install python3-catkin-pkg-modules
sudo apt install python3-rospkg-modules
```

3. Next go to root of catkin workspace and run:
```
catkin_make
```
4. After successful make run:
    - for __bash__ - `source devel/setup.bash`
    - for __zsh__ - `source devel/setup.zsh`

5. Run server with:
```
roslaunch ros-detector-server server.launch
```