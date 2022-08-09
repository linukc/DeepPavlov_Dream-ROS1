docker build . \
        --build-arg UID=$(id -u) \
        --build-arg GID=$(id -g) \
        --build-arg NUM_THREADS=4 \
        -t noetic/robot_bot_navigation:latest