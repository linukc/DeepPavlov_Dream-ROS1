FROM ros:noetic-ros-core

#install required libs and packages
RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl python3-pip

RUN python3 -m pip install requests

ARG USER=docker_robot
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user

RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd && adduser ${USER} sudo
WORKDIR /home/${USER}
RUN mkdir -p catkin_ws && chown -R ${UID}:${GID} /home/${USER}
USER ${UID}:${GID}