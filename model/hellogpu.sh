#!/bin/bash -l
#SBATCH --output=/scratch/users/%u/%j.out
#SBATCH --job-name=gpu
#SBATCH --gres=gpu
echo "Begin Run! From $HOSTNAME"
nvidia-debugdump -l






python3 train.py










echo "The task is finished! From $HOSTNAME"





