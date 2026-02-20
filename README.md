# Bacterial WGS Variant Calling Pipeline

A reproducible whole-genome sequencing variant calling pipeline built using:

- BWA
- SAMtools
- BCFtools
- Python
- Docker

## Workflow

1. Read alignment with BWA
2. SAM to sorted BAM conversion
3. BAM indexing
4. Variant calling using bcftools
5. Variant statistics generation

## How to Run (Docker)

docker build -t bacterial-pipeline -f docker/Dockerfile .

docker run -v $(pwd):/app bacterial-pipeline python3 pipeline/run_pipeline.py
