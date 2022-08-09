#!/bin/bash

docker exec --user "docker_robot" -it robot_bot_navigation_container \
    /bin/bash -c "source /opt/ros/noetic/setup.bash; cd /home/docker_robot/catkin_ws; /bin/bash"