#!/bin/sh

# unset  LD_PRELOAD
# export CUDA_HOME=/opt/cuda
# export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CUDA_HOME}/lib64
# export PATH=${CUDA_HOME}/bin:$PATH

env_path='/home/mechanoid/.python_venv/avito_cp313'

source ${env_path}/bin/activate || exit -1

python3 app.py 
