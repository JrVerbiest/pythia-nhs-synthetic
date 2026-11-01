"""
Script to download the dataset for the Pythia NHS Synthetic project.
"""

import argparse
from pathlib import Path

from huggingface_hub import snapshot_download

REPO_ID = "NHSEDataScience/synthetic_clinical_notes"


def download(dest: Path) -> Path:
    """Download the full dataset repo into `dest` and return the local path."""
    dest.mkdir(parents=True, exist_ok=True) # Ensure the destination directory exists
    local_path = snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",  # without this, the Hub looks for a *model* repo
        local_dir=dest,
    )
    return Path(local_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path("data/synthetic_clinical_notes"),
        help="Directory to download into (default: %(default)s)",
    )
    args = parser.parse_args()

    path = download(args.dest)
    print(f"Downloaded to: {path}")
    for f in sorted(path.rglob("*")):
        if f.is_file() and ".cache" not in f.parts:
            print(f"  {f.relative_to(path)}  ({f.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()