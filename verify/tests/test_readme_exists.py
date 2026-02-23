from pathlib import Path

def test_readme():
    assert Path("README.md").exists()
