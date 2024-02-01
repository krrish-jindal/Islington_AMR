#!/bin/bash
xhost +local:root
docker run --gpus all --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
-it --rm --net=host --ipc=host \
--env="QT_X11_NO_MITSHM=1"  \
--env="DISPLAY"  \
my_image /bin/bash -c "cd src  && exec bash "
