workspace_dir=$PWD

docker run -it -d --rm \
        --ipc host \
        --network host \
        --privileged \
        --name robot_bot_navigation_container \
        -v $workspace_dir/../..:/home/docker_robot/catkin_ws/src:rw \
        noetic/robot_bot_navigation:latest