#!/usr/bin/env python3
"""Deterministically pack new census JSON, retaining verified external originals."""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def deterministic_gzip(data):
    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0, compresslevel=9) as stream:
        stream.write(data)
    return output.getvalue()


def verify(directory):
    directory = Path(directory)
    index = json.loads((directory/"receipts-index.json").read_text())
    for row in index["files"]:
        packed = (directory/row["compressed_file"]).read_bytes()
        raw = gzip.decompress(packed)
        if (sha(raw) != row["raw_sha256"] or sha(packed) != row["compressed_sha256"]
                or len(raw) != row["raw_bytes"] or len(packed) != row["compressed_bytes"]):
            raise ValueError(f"receipt integrity mismatch: {row['raw_file']}")
    return index


def pack(directory, archive, *, remove_raw=False):
    directory, archive = Path(directory).resolve(), Path(archive).resolve()
    files = sorted(set(directory.glob("census-n*.json")) | set(directory.glob("fraction-n*.json")))
    if not files:
        raise ValueError("no new census/Fraction raw JSON receipts found")
    archive.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in files:
        if remove_raw and path.is_relative_to(ROOT):
            tracked = subprocess.run(["git", "ls-files", "--error-unmatch", str(path.relative_to(ROOT))],
                                     cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if tracked.returncode == 0:
                raise ValueError(f"refusing to remove tracked archive/source: {path}")
        raw = path.read_bytes()
        saved = archive/path.name
        if saved.exists() and saved.read_bytes() != raw:
            raise ValueError(f"external archive conflict: {saved}")
        saved.write_bytes(raw)
        packed = deterministic_gzip(raw)
        if gzip.decompress(packed) != raw or saved.read_bytes() != raw:
            raise ArithmeticError("receipt round trip or external preservation failed")
        packed_path = path.with_suffix(path.suffix+".gz")
        packed_path.write_bytes(packed)
        rows.append({"raw_file": path.name, "compressed_file": packed_path.name,
                     "raw_bytes": len(raw), "compressed_bytes": len(packed),
                     "raw_sha256": sha(raw), "compressed_sha256": sha(packed)})
    index = {"schema": "SUCC-deterministic-census-gzip-v1", "gzip_mtime": 0,
             "gzip_filename": "", "compression_level": 9,
             "raw_bytes": sum(x["raw_bytes"] for x in rows),
             "compressed_bytes": sum(x["compressed_bytes"] for x in rows),
             "file_count": len(rows), "files": rows,
             "authority": "byte preservation and replay integrity, not a mathematical proof"}
    (directory/"receipts-index.json").write_text(json.dumps(index, indent=2, sort_keys=True)+"\n")
    verify(directory)
    if remove_raw:
        for path in files:
            path.unlink()
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pack", type=Path)
    group.add_argument("--verify", type=Path)
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--remove-raw", action="store_true")
    args = parser.parse_args()
    if args.pack:
        if args.archive is None:
            parser.error("--pack requires --archive")
        index = pack(args.pack, args.archive, remove_raw=args.remove_raw)
    else:
        if args.remove_raw:
            parser.error("--remove-raw is only valid with --pack")
        index = verify(args.verify)
    print(json.dumps({k: index[k] for k in ("file_count", "raw_bytes", "compressed_bytes")}))


if __name__ == "__main__":
    main()
