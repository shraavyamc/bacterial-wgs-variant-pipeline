import yaml
import subprocess
import os
import subprocess
from pathlib import Path

reference = "reference/ref.fa"
config = yaml.safe_load(open("config.yaml"))

for sample, reads in config["samples"].items():
    r1 = reads["R1"]
    r2 = reads["R2"]
    output_dir = f"results/{sample}"

    os.makedirs(output_dir, exist_ok=True)

    subprocess.run(
        f"bwa mem reference/ref.fa {r1} {r2} > {output_dir}/sample.sam",
        shell=True,
        check=True
    )

Path(output_dir).mkdir(parents=True, exist_ok=True)

# Alignment
subprocess.run(
    f"bwa mem {reference} {r1} {r2} > {output_dir}/sample.sam",
    shell=True,
    check=True
)

# Convert to BAM + sort
subprocess.run(
    f"samtools sort {output_dir}/sample.sam -o {output_dir}/sample.sorted.bam",
    shell=True,
    check=True
)

# Index
subprocess.run(
    f"samtools index {output_dir}/sample.sorted.bam",
    shell=True,
    check=True
)

# Variant calling
subprocess.run(
    f"bcftools mpileup -f {reference} {output_dir}/sample.sorted.bam | "
    f"bcftools call -mv -Ov -o {output_dir}/sample.vcf",
    shell=True,
    check=True
)
