#!/bin/bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/usr/share/gazebo-11/models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$WORKSPACE/src/islington_packages/islington_amr_description/world/model

xhost +local:root
docker run --gpus all --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
docker run --name my_all_gpu_container --gpus all -t nvidia/cuda

-it --rm --net=host --ipc=host \
--env="QT_X11_NO_MITSHM=1"  \
--env="DISPLAY"  \
my_image
