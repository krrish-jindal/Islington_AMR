# Docker and NVIDIA Toolkit Setup for Islington_AMR

## Installing and Configuring Docker:

1. Follow the official Docker installation guide for Ubuntu [here](https://docs.docker.com/engine/install/ubuntu/).
2. Perform post-installation steps as outlined [here](https://docs.docker.com/engine/install/linux-postinstall/).

## Installing NVIDIA Toolkit:

- Refer to the NVIDIA Container Toolkit installation guide [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) to install the toolkit on your host system.

## Cloning Git Repository:

1. Clone the Islington_AMR Git repository and navigate to the project directory:

   ```bash
   git clone git@github.com:krrish-jindal/Islington_AMR.git
   cd Islington_AMR
   ```
## Build the Docker image

   ```bash
docker build -t my_image .
```

## Run the provided script

   ```bash
./run.sh
```

## Inside the container, execute

   ```bash
./new.sh
```
## Open new terminal and run this

```bash

docker ps 
docker exec -it <Containter_ID_From_Above> bash
```

## To run point-to-point navigation run this

   ```bash
ros2 run islington_nav2 islington_nav_cmd.py
```

