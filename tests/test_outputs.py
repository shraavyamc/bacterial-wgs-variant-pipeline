from pathlib import Path

def test_vcf_exists():
    assert Path("results/sample1/sample.vcf").exists()
