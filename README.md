# Production-Ready Illumina Bacterial WGS Variant Pipeline

A reproducible, multi-sample capable Illumina whole-genome sequencing (WGS) variant calling pipeline for bacterial genomes. Designed for Linux environments, containerised with Docker, and HPC-ready using SLURM.

This project demonstrates practical implementation of short-read alignment, variant calling, and workflow modularisation suitable for microbial genomics analysis.

---

## Project Objective

To implement a production-style bacterial WGS variant calling pipeline that:

- Supports multi-sample processing
- Runs reproducibly using Docker
- Scales on HPC clusters using SLURM
- Uses configuration-driven execution
- Produces standard VCF outputs and summary statistics

Test dataset:
Illumina paired-end reads from SRR28000075 (Staphylococcus aureus WGS).

Reference genome:
Staphylococcus aureus complete genome (RefSeq assembly such as N315 or USA300).

---

## Tools Used

- BWA (read alignment)
- SAMtools (BAM processing and indexing)
- BCFtools (variant calling)
- Python (pipeline orchestration)
- Docker (containerisation)
- SLURM (HPC execution)

---

## Workflow Overview

1. FASTQ input (paired-end Illumina reads)
2. Alignment to reference genome using BWA-MEM
3. SAM → sorted BAM conversion
4. BAM indexing
5. Variant calling using bcftools mpileup + call
6. Variant statistics generation

Output:
- Sorted BAM files
- Indexed BAM files (.bai)
- Raw VCF file
- Variant statistics summary

---

## Repository Structure


- docker/ # Dockerfile and container setup
- pipeline/ # Core Python workflow scripts
- reference/ # Reference genome files
- tests/ # Test utilities
- config.yaml # Configurable pipeline parameters
- run_slurm.sh # SLURM batch execution script


---

## Reproducibility Features

- Fully containerised environment
- Config-driven execution via `config.yaml`
- Modular Python workflow design
- HPC-compatible execution
- Clean separation of data, scripts, and environment

---

## Running with Docker

Build the container:

`docker build -t bacterial-pipeline -f docker/Dockerfile .`


Run the pipeline:

`docker run -v $(pwd):/app bacterial-pipeline python3 pipeline/run_pipeline.py`


---

## Running on HPC (SLURM)

Submit batch job: `sbatch run_slurm.sh`

---

## Skills Demonstrated

- Illumina WGS processing
- Short-read alignment and variant calling
- Linux-based bioinformatics workflows
- Containerisation for reproducibility
- HPC job scheduling (SLURM)
- Git-based version control
