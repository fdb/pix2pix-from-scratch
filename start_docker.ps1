# Start a Docker session
# If Powershell complains that running scripts is disabled, open a Powershell as admin and type:
#     Set-ExecutionPolicy unrestricted
# Confirm with [y].

docker run -it --rm -v ${PWD}:/tf -w /tf -p 8888:8888 --gpus all tensorflow/tensorflow:latest-gpu-jupyter
