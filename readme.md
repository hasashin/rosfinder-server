RosFinder server for ROS
===

## Reason
While creating custom VR application for engineer's thesis. I needed solution to find which machine in the network is running ROS. ROS didn't provide discovery services so this custom one was created.

## How it works

This node listens for specific datagram on any link on port 21337. 

Client has to send UDP datagram containing `ROS`, then server checks from which network client send request. Then it responds with `ACK` followed by IP address and port of rosbridge server.

## Instalation

To install this node do the following:
1. Go to catkin workspace and clone repository into __src__ folder
```
git clone https://github.com/hasashin/rosfinder-server
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
roslaunch rosfinder-server server.launch
```
