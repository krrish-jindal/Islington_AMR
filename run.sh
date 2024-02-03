#!/bin/bash
xhost +local:root

# Check if NVIDIA Container Toolkit is installed
if command -v nvidia-container-toolkit &> /dev/null; then
    # If available, use GPU resources
    docker run --gpus all --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
    -it --rm --net=host --ipc=host \
    --env="QT_X11_NO_MITSHM=1" \
    --env="DISPLAY" \
    my_image /bin/bash -c "cd src  && exec bash "
else
    # If not available, run without GPU support
    docker run --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
    -it --rm --net=host --ipc=host \
    --env="QT_X11_NO_MITSHM=1" \
    --env="DISPLAY" \
    my_image /bin/bash -c "cd src  && exec bash "
fi
