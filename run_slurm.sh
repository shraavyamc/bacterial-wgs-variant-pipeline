#!/bin/bash
#SBATCH --job-name=bacterial_pipeline
#SBATCH --output=results/slurm_%j.out
#SBATCH --error=results/slurm_%j.err
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=01:00:00
#SBATCH --account=c25064799       # your HPC account
#SBATCH --partition=dev       # valid partition for CPU jobs

module load BWA
module load SAMtools
module load Python

# install Python packages for your user only
pip install --user pyyaml pytest

# run your pipeline
python3 pipeline/run_pipeline.py
