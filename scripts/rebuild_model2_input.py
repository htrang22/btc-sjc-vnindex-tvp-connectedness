"""Rebuild the Model 2 volatility input without modifying the submitted repo."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument(
    "source_repo",
    type=Path,
    help="Local path to the submitted btc-sjc-vnindex-risk-analysis repo",
)
args = parser.parse_args()

source_repo = args.source_repo.resolve()
target_repo = Path(__file__).resolve().parents[1]
source_notebook = source_repo / "btc-sjc-vnindex-volatility.ipynb"
target_csv = target_repo / "data/model2_conditional_volatility.csv"

notebook = nbformat.read(source_notebook, as_version=4)
export_cells = 0

for cell in notebook.cells:
    if cell.cell_type != "code":
        continue
    if "%pip install" in cell.source:
        cell.source = "# Dependencies are provided by the active environment."
    if "dy_volatility.to_csv(output_file" in cell.source:
        cell.source = cell.source.replace(
            'output_dir = Path("outputs")',
            f'output_dir = Path(r"{target_csv.parent}")',
        )
        export_cells += 1

if export_cells != 1:
    raise RuntimeError(f"Expected one Model 2 export cell, found {export_cells}")

client = NotebookClient(
    notebook,
    timeout=1800,
    kernel_name="python3",
    resources={"metadata": {"path": str(source_repo)}},
)
client.execute()

if not target_csv.exists():
    raise RuntimeError("The source notebook completed without producing the target CSV")

print(f"Rebuilt: {target_csv}")
print(f"SHA-256: {sha256(target_csv)}")
