"""Claim-namespace registry: fully-qualified claim IDs and a collision guard.

Several SUCC supplement files were minted independently and reuse the same bare
claim prefix for DIFFERENT, disjoint-meaning families (e.g. bare ``PH-`` is both
Profinite Hilbert and Prime Form Heat). Bare IDs stay valid inside their own
supplement file and are never renamed; this module reads the additive registry
(``docs/CLAIM_NAMESPACE_REGISTRY.json``) and mints a stable, globally-unique
fully-qualified ID (FQID) per namespace.

The FQID is the key a downstream SUCC->YEAN proof-extraction pipeline can rely on:
one namespace, one ``fq_prefix``, forever. A bare ``PH-01`` is ambiguous; the FQIDs
``PH.PROF-01`` and ``PH.PFH-01`` are not. Everything here is pure stdlib, determin-
istic, and sorted -- a registry you can diff, not a registry you have to trust.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

# The registry lives next to the docs, one directory up from this package.
REGISTRY_PATH = Path(__file__).resolve().parent.parent / "docs" / "CLAIM_NAMESPACE_REGISTRY.json"

# Repo root: the registry's supplement_files are repo-relative, so resolve against this.
_REPO_ROOT = REGISTRY_PATH.parent.parent

# A claim-ID table row: first cell is a claim ID and nothing else. Capture the
# alphabetic (+ optional trailing digits) prefix that precedes the first -<number>.
# Example matches: "| PH-01 |", "| ZCR-04 |", "| AMW-06B |".
_BARE_PREFIX = r"[A-Z]{2,6}[0-9]*(?:-[A-Z]{2,6}[0-9]*)*"
_CLAIM_ROW_RE = re.compile(r"^\|\s*(" + _BARE_PREFIX + r")-[0-9]+[A-Z]?\s*\|")


def load_registry():
    """Load and return the parsed registry JSON object."""
    with REGISTRY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def _namespace_map(registry=None):
    """Return {namespace_name: namespace_object} for quick, exact lookup."""
    if registry is None:
        registry = load_registry()
    return {entry["namespace"]: entry for entry in registry["namespaces"]}


def fqid(namespace, bare_id):
    """Map a namespace + bare claim ID to its fully-qualified ID.

    ``fqid("PROFINITE_HILBERT", "PH-01") == "PH.PROF-01"``. The numeric part is
    zero-padded to width 2. Raises ``KeyError`` on an unknown namespace and
    ``ValueError`` on a bare ID whose shape we cannot parse -- a malformed ID is a
    diseased input, not something to paper over with a silent default.
    """
    entry = _namespace_map().get(namespace)
    if entry is None:
        raise KeyError(f"unknown namespace: {namespace!r}")
    if type(bare_id) is not str:
        raise ValueError("bare claim ID must be a string")
    raw = bare_id.strip()
    match = re.fullmatch(r"(" + _BARE_PREFIX + r")-([0-9]+)([A-Z]?)", raw)
    if match is None:
        raise ValueError(f"unparseable bare claim ID: {bare_id!r}")
    if match.group(1) != entry["bare_prefix"]:
        raise ValueError(
            f"claim {raw!r} has wrong bare prefix for namespace {namespace!r}"
        )
    # Crucial authority gate: a namespace prefix does NOT grant the authority to
    # mint arbitrary numbered claims. The exact bare ID must occur as the first
    # Markdown table cell of an assigned, registered supplement file.
    row = re.compile(r"^\|\s*" + re.escape(raw) + r"\s*\|", re.MULTILINE)
    if not any(
        row.search((_REPO_ROOT / rel).read_text(encoding="utf-8"))
        for rel in entry["supplement_files"]
    ):
        raise ValueError(f"claim {raw!r} is not declared in namespace {namespace!r}")
    number = int(match.group(2))
    suffix = match.group(3)
    return f"{entry['fq_prefix']}-{number:02d}{suffix}"


def _supplement_files():
    """Sorted list of every docs/CLAIM_SUPPLEMENT_*.md path (repo-relative, posix)."""
    docs = _REPO_ROOT / "docs"
    return sorted(
        path.relative_to(_REPO_ROOT).as_posix()
        for path in docs.glob("CLAIM_SUPPLEMENT_*.md")
    )


def scan_supplement_prefixes():
    """Census of bare claim prefixes across all supplement files.

    Returns ``{bare_prefix: [sorted supplement files that contain >=1 claim-ID row
    with that prefix]}``. Prefixes are read ONLY from markdown table rows whose
    first cell is a claim ID -- prose mentions do not count.
    """
    found: dict[str, set[str]] = {}
    for rel_path in _supplement_files():
        text = (_REPO_ROOT / rel_path).read_text(encoding="utf-8")
        for line in text.splitlines():
            match = _CLAIM_ROW_RE.match(line)
            if match is not None:
                found.setdefault(match.group(1), set()).add(rel_path)
    return {prefix: sorted(files) for prefix, files in sorted(found.items())}


def unregistered_prefix_collisions():
    """Future-collision guard: cross-file bare prefixes the registry does NOT cover.

    Returns the sorted list of bare prefixes that appear in >=2 distinct supplement
    files but are NOT fully accounted for by the registry. A prefix is covered iff
    (a) the union of ``supplement_files`` over all registry namespaces carrying that
    bare prefix includes every file where the prefix actually appears, AND (b) if two
    or more distinct namespaces carry it, there is a ``resolved_collisions`` entry for
    that bare prefix. Anything else is an unregistered collision -- an open wound a
    future PR left for someone else to find. Empty today; it fails loudly the moment a
    new cross-file prefix collision is introduced without being registered here.
    """
    registry = load_registry()

    files_by_prefix: dict[str, set[str]] = {}
    namespaces_by_prefix: dict[str, set[str]] = {}
    for entry in registry["namespaces"]:
        prefix = entry["bare_prefix"]
        files_by_prefix.setdefault(prefix, set()).update(entry["supplement_files"])
        namespaces_by_prefix.setdefault(prefix, set()).add(entry["namespace"])

    resolved_prefixes = {rc["bare_prefix"] for rc in registry.get("resolved_collisions", [])}

    scanned = scan_supplement_prefixes()
    offenders = []
    for prefix, files in scanned.items():
        if len(files) < 2:
            continue  # single-file prefixes cannot be cross-file collisions
        covered_files = files_by_prefix.get(prefix, set())
        fully_covered = set(files) <= covered_files
        multi_namespace = len(namespaces_by_prefix.get(prefix, set())) >= 2
        has_resolution = prefix in resolved_prefixes
        if not fully_covered or (multi_namespace and not has_resolution):
            offenders.append(prefix)
    return sorted(offenders)
