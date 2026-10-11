#!/usr/bin/env python3
"""Verify content-addressed historical imports without contacting GitHub.

Git blobs are SHA-1("blob <byte-count>\0" + raw_content).
The source_commit and original paths are frozen in IMPORT_MANIFEST.json.
This establishes exact artifact identity, NOT intellectual authorship or
cryptographic attestation of a physical observation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def verify(repo: Path | None = None) -> dict:
    root = (repo or Path(__file__).resolve().parents[1]).resolve()
    manifest_path = root / "provenance/IMPORT_MANIFEST.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    records = data["entries"]
    if data["count"] != len(records) or len(records) < 65:
        raise ValueError("Historical provenance records incomplete")
    seen = set()
    untouched = 0
    translated = 0
    for item in records:
        rel = Path(item["destination_path"])
        if rel.is_absolute() or ".." in rel.parts or rel.as_posix() in seen:
            raise ValueError(f"Unsafe or duplicate manifest destination: {rel}")
        seen.add(rel.as_posix())
        current = (root / rel).read_bytes()
        sha = git_blob_sha(current)
        if sha != item["destination_git_blob_sha"]:
            raise ValueError(f"Changed historical imported artifact: {rel}")
        mode = item["transformation"]
        if mode == "verbatim":
            untouched += 1
            if sha != item["original_git_blob_sha"]:
                raise ValueError(f"Historical source document not byte-for-byte: {rel}")
        elif mode.startswith("literal textual namespace translation:"):
            translated += 1
        else:
            raise ValueError(f"Unrecognized migration transformation for: {rel}")
    if translated != 54 or untouched != 17:
        raise ValueError(f"Historical code/archive counts drifted: {translated}, {untouched}")
    return {
        "status": "SOURCE_PROVENANCE_VERIFIED",
        "source_commit": data["source_commit"],
        "items": len(records),
        "mechanical_namespace_migrations": translated,
        "byte_identical_research_archives": untouched,
        "establishes_mathematical_truth": False,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
