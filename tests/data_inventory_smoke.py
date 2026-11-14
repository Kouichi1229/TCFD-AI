"""Repository data-file integrity checks for GitHub Actions."""

from pathlib import Path
import os
import tempfile

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "file_csv"


def main():
    csv_files = sorted(DATA_DIR.glob("*.csv"))
    if not csv_files:
        raise SystemExit("No CSV files found in file_csv/")

    failures = []
    for path in csv_files:
        try:
            frame = pd.read_csv(path)
            if frame.empty:
                failures.append(f"{path.name}: parsed successfully but contains no data rows")
            else:
                print(f"CSV passed: {path.name} ({len(frame)} rows, {len(frame.columns)} columns)")
        except Exception as exc:  # Report the exact file and parser error in CI logs.
            failures.append(f"{path.name}: {type(exc).__name__}: {exc}")

    if failures:
        raise SystemExit("\n".join(failures))

    # Verify the shared loader resolves its data directory independently of cwd.
    import sys

    sys.path.insert(0, str(ROOT))
    from data_loader import load_csv

    original_cwd = Path.cwd()
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            loaded = load_csv("201302 to 2020_all2.csv")
            if loaded.empty:
                raise SystemExit("Shared loader returned an empty integrated dataset.")
    finally:
        os.chdir(original_cwd)

    print(f"All {len(csv_files)} CSV files parsed successfully.")
    print("Shared CSV loader passed when called outside the repository working directory.")


if __name__ == "__main__":
    main()
