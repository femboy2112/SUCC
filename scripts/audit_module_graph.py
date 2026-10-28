#!/usr/bin/env python3
"""Module-level dependency graph and structural health audit.

Builds a directed import graph over every ``observational_succ/*.py`` module,
then reports:

  1. Intra-package imports per module (``observational_succ.X`` and ``from .``
     relative forms).
  2. Import cycles (strongly connected components with >1 node, plus
     self-referential cycles).
  3. Orphan modules (import nothing intra-package and are imported by nothing,
     outside a small whitelist of entry-point / core modules).
  4. Duplicate-primitive clusters (modules whose top-level ``def`` / ``class``
     names overlap heavily, flagging likely copy-paste accretion).

Deterministic and pure-stdlib (``ast`` + ``os`` + ``json`` + ``collections`` +
``difflib``).  Emits two artifacts:

  * docs/math_memory/MODULE_DEPENDENCY_GRAPH.json
  * docs/math_memory/MODULE_STRUCTURE_AUDIT.md

This script is read-only with respect to the package: it only parses sources
and writes the two output documents under docs/math_memory/.
"""

from __future__ import annotations

import ast
import json
import os
from collections import defaultdict
from difflib import SequenceMatcher

PACKAGE = "observational_succ"
PACKAGE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), PACKAGE
)
OUT_JSON = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs",
    "math_memory",
    "MODULE_DEPENDENCY_GRAPH.json",
)
OUT_MD = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs",
    "math_memory",
    "MODULE_STRUCTURE_AUDIT.md",
)

# Modules that are entry points or the tiny certified core.  They are never
# reported as orphans even if nothing imports them, because they are the
# load-bearing spine the rest of the package stands on.
CORE_WHITELIST = {
    "core",
    "arithmetic",
    "engine",
    "__init__",
}

# Name-similarity threshold (0..1) for clustering duplicate primitives.
DUP_SIMILARITY = 0.62
# Minimum overlap count to consider two modules "duplicate".
DUP_MIN_OVERLAP = 2

# Top-level names that are near-universal micro-helpers across the package and
# therefore carry no signal about a module's identity.  Using them in the
# similarity computation collapses hundreds of modules into one meaningless
# cluster (e.g. ``_integer`` appears in 100+ modules).  We exclude any name
# that (a) is underscore-prefixed, or (b) is a single short lowercase token
# that reads as a local alias rather than a domain primitive.
_BOILERPLATE_PREFIX = "_"
_BOILERPLATE_EXACT = {
    "q", "rat", "exact", "add", "mul", "sub", "neg", "dot", "scale",
    "matrix", "transpose", "inverse", "divisors", "is_prime", "prime",
    "integer", "rational", "natural", "receipt", "valuation", "mobius",
    "pi_interval", "circle_distance", "depth", "index", "ceil", "floor",
    "positive", "frequency", "gcd", "lcm", "mod", "sq", "sqrt",
}


def is_boilerplate(name: str) -> bool:
    if name.startswith(_BOILERPLATE_PREFIX):
        return True
    if name in _BOILERPLATE_EXACT:
        return True
    return False


def signal_names(name_set: set[str]) -> set[str]:
    """Drop boilerplate names; keep only identity-carrying names."""
    return {n for n in name_set if not is_boilerplate(n)}


def module_name_from_path(path: str) -> str:
    """Return the bare module name (no .py) for a path under the package."""
    base = os.path.basename(path)
    if base.endswith(".py"):
        base = base[: -len(".py")]
    return base


def iter_module_paths() -> list[str]:
    """All .py files directly under observational_succ/ (sorted, deterministic)."""
    paths = [
        os.path.join(PACKAGE_DIR, f)
        for f in os.listdir(PACKAGE_DIR)
        if f.endswith(".py")
    ]
    return sorted(paths)


def extract_imports(path: str) -> tuple[list[str], list[str]]:
    """Return (imported_modules, top_level_defclass_names) for one module.

    ``imported_modules`` are the bare intra-package module names this module
    imports.  ``top_level_defclass_names`` are top-level ``def`` / ``class``
    (and ``async def``) names used for duplicate-primitive detection.
    """
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        # Should not happen (package compiles), but be defensive.
        return [], []

    imports: list[str] = []
    defclass: list[str] = []

    for node in ast.walk(tree):
        # --- imports -------------------------------------------------------
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                if name.startswith(PACKAGE + "."):
                    parts = name.split(".")
                    if len(parts) >= 2:
                        imports.append(parts[1])
        elif isinstance(node, ast.ImportFrom):
            if node.module is None:
                # "from . import x"
                if node.level == 1:
                    for alias in node.names:
                        if not alias.name.startswith("_"):
                            imports.append(alias.name)
                continue
            # node.module like "core", "arithmetic", "observational_succ.core",
            # or "observational_succ" for "from observational_succ import x".
            if node.level == 1:
                # "from .core import ..." -> module is "core"
                imports.append(node.module.split(".")[0])
            elif node.level == 0 and node.module.startswith(PACKAGE):
                # "from observational_succ.core import ..." or
                # "from observational_succ import ..." -> skip the bare package.
                parts = node.module.split(".")
                if len(parts) >= 2:
                    imports.append(parts[1])

    # --- top-level definitions (only at module body, not nested) -----------
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            defclass.append(node.name)

    return imports, defclass


def tarjan_scc(nodes: list[str], edges: dict[str, list[str]]) -> list[list[str]]:
    """Tarjan's strongly connected components over the import graph."""
    index: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    on_stack: dict[str, bool] = {n: False for n in nodes}
    stack: list[str] = []
    counter = [0]
    result: list[list[str]] = []

    def strongconnect(v: str) -> None:
        index[v] = counter[0]
        lowlink[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        for w in edges.get(v, []):
            if w not in index:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack.get(w, False):
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            comp: list[str] = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp.append(w)
                if w == v:
                    break
            result.append(comp)

    for n in nodes:
        if n not in index:
            strongconnect(n)
    return result


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def name_similarity(a: str, b: str) -> float:
    if a == b:
        return 1.0
    return SequenceMatcher(None, a, b).ratio()


def cluster_duplicates(
    modules: list[str], names: dict[str, set[str]]
) -> list[list[str]]:
    """Greedy clustering of modules with heavy public-name overlap.

    Two modules are "similar" if (a) they share at least DUP_MIN_OVERLAP
    identical names, or (b) their overall name set Jaccard similarity is high
    and a name-level cosine-style overlap is present.  We build an undirected
    similarity graph and emit its connected components of size >= 2.
    """
    # Similarity between every unordered pair of modules with >=1 def/class.
    adj: dict[str, set[str]] = defaultdict(set)
    # Use only identity-carrying (non-boilerplate) names for similarity.
    signal = {m: signal_names(names.get(m, set())) for m in modules}
    keys = [m for m in modules if signal.get(m)]

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            na, nb = signal[a], signal[b]
            exact = na & nb
            jac = jaccard(na, nb)
            # Cosine-style overlap on top of Jaccard for a soft signal.
            cosine = 0.0
            if na and nb:
                cosine = len(exact) / (len(na) ** 0.5 * len(nb) ** 0.5)
            similar = False
            if len(exact) >= DUP_MIN_OVERLAP:
                similar = True
            elif jac >= DUP_SIMILARITY and cosine >= DUP_SIMILARITY:
                similar = True
            if similar:
                adj[a].add(b)
                adj[b].add(a)

    # Connected components (union-find for determinism).
    parent = {m: m for m in keys}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: str, y: str) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    for a in adj:
        for b in adj[a]:
            union(a, b)

    comps: dict[str, list[str]] = defaultdict(list)
    for m in sorted(keys):
        comps[find(m)].append(m)

    clusters = [sorted(v) for v in comps.values() if len(v) >= 2]
    clusters.sort()
    return clusters


def main() -> None:
    paths = iter_module_paths()
    modules = [module_name_from_path(p) for p in paths]

    imports: dict[str, list[str]] = {}
    names: dict[str, set[str]] = {}
    for p, m in zip(paths, modules):
        imp, dc = extract_imports(p)
        # Keep only intra-package targets that actually exist as modules.
        imp = [x for x in imp if x in set(modules)]
        # Deduplicate while preserving first-seen order.
        seen: set[str] = set()
        dedup: list[str] = []
        for x in imp:
            if x not in seen:
                seen.add(x)
                dedup.append(x)
        imports[m] = dedup
        names[m] = set(dc)

    # Reverse graph (imported_by).
    imported_by: dict[str, list[str]] = defaultdict(list)
    for m, deps in imports.items():
        for d in deps:
            imported_by[d].append(m)

    # Sort every reverse list for determinism.
    for m in imported_by:
        imported_by[m] = sorted(imported_by[m])

    # --- cycles ------------------------------------------------------------
    sccs = tarjan_scc(modules, imports)
    cycles = [sorted(c) for c in sccs if len(c) > 1]
    self_cycles = [
        m for m in modules if m in imports.get(m, [])
    ]
    cycles.sort(key=lambda c: (-len(c), c))

    # --- orphans -----------------------------------------------------------
    orphans = [
        m
        for m in modules
        if m not in CORE_WHITELIST
        and not imports.get(m)
        and not imported_by.get(m)
    ]
    orphans.sort()

    # --- duplicate clusters ------------------------------------------------
    dup_clusters = cluster_duplicates(modules, names)

    # --- summary -----------------------------------------------------------
    with_imports = [m for m in modules if imports.get(m)]
    summary = {
        "total_modules": len(modules),
        "modules_with_intra_package_imports": len(with_imports),
        "modules_with_no_intra_package_imports": len(modules) - len(with_imports),
        "total_intra_package_import_edges": sum(len(v) for v in imports.values()),
        "import_cycles": len(cycles),
        "largest_cycle_sizes": [len(c) for c in cycles[:10]],
        "self_referential_cycles": len(self_cycles),
        "orphan_modules": len(orphans),
        "duplicate_clusters": len(dup_clusters),
        "modules_in_duplicate_clusters": sum(len(c) for c in dup_clusters),
    }

    # --- build report ------------------------------------------------------
    nodes = [
        {
            "module": m,
            "imports": imports[m],
            "imported_by": imported_by.get(m, []),
            "top_level_defclass_names": sorted(names[m]),
        }
        for m in modules
    ]

    report = {
        "package": PACKAGE,
        "summary": summary,
        "nodes": nodes,
        "import_cycles": [
            {"size": len(c), "modules": c} for c in cycles
        ],
        "self_referential_cycles": self_cycles,
        "orphans": orphans,
        "duplicate_clusters": [
            {"size": len(c), "modules": c} for c in dup_clusters
        ],
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, sort_keys=True)
        fh.write("\n")

    write_markdown(report, summary)

    # --- console summary ---------------------------------------------------
    print("Module graph audit complete.")
    print(f"  total modules:                          {summary['total_modules']}")
    print(f"  modules with intra-package imports:     {summary['modules_with_intra_package_imports']}")
    print(f"  intra-package import edges:             {summary['total_intra_package_import_edges']}")
    print(f"  import cycles (SCC size >1):            {summary['import_cycles']}")
    print(f"  largest cycle sizes:                    {summary['largest_cycle_sizes']}")
    print(f"  self-referential cycles:                {summary['self_referential_cycles']}")
    print(f"  orphan modules:                         {summary['orphan_modules']}")
    print(f"  duplicate clusters:                     {summary['duplicate_clusters']}")
    print(f"  modules in duplicate clusters:          {summary['modules_in_duplicate_clusters']}")
    print(f"  wrote: {OUT_JSON}")
    print(f"  wrote: {OUT_MD}")


def write_markdown(report: dict, summary: dict) -> None:
    lines: list[str] = []
    lines.append("# Module Structure Audit — observational_succ")
    lines.append("")
    lines.append("Auto-generated by `scripts/audit_module_graph.py`. "
                 "Deterministic, pure-stdlib. Read-only with respect to the package.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---|")
    rows = [
        ("Total modules", summary["total_modules"]),
        ("Modules with intra-package imports", summary["modules_with_intra_package_imports"]),
        ("Modules with no intra-package imports", summary["modules_with_no_intra_package_imports"]),
        ("Intra-package import edges", summary["total_intra_package_import_edges"]),
        ("Import cycles (SCC size > 1)", summary["import_cycles"]),
        ("Self-referential cycles", summary["self_referential_cycles"]),
        ("Orphan modules", summary["orphan_modules"]),
        ("Duplicate clusters", summary["duplicate_clusters"]),
        ("Modules in duplicate clusters", summary["modules_in_duplicate_clusters"]),
    ]
    for k, v in rows:
        lines.append(f"| {k} | {v} |")
    lines.append("")

    if summary["largest_cycle_sizes"]:
        lines.append("Largest cycle sizes (top 10 SCCs): "
                     + ", ".join(str(x) for x in summary["largest_cycle_sizes"]))
        lines.append("")

    # --- cycles ---
    lines.append("## Import Cycles")
    lines.append("")
    if report["import_cycles"]:
        for cyc in report["import_cycles"]:
            lines.append(f"### SCC size {cyc['size']}")
            lines.append("")
            lines.append("```")
            lines.append("\n".join(cyc["modules"]))
            lines.append("```")
            lines.append("")
    else:
        lines.append("_None._")
        lines.append("")

    # --- self cycles ---
    lines.append("## Self-Referential Cycles")
    lines.append("")
    if report["self_referential_cycles"]:
        lines.append("```")
        lines.append("\n".join(report["self_referential_cycles"]))
        lines.append("```")
    else:
        lines.append("_None._")
    lines.append("")

    # --- orphans ---
    lines.append("## Orphan Modules")
    lines.append("")
    lines.append("Modules that import no intra-package module and are imported by "
                 "none (excluding whitelisted core/entry-point modules).")
    lines.append("")
    if report["orphans"]:
        lines.append("```")
        lines.append("\n".join(report["orphans"]))
        lines.append("```")
    else:
        lines.append("_None._")
    lines.append("")

    # --- duplicate clusters ---
    lines.append("## Duplicate-Primitive Clusters")
    lines.append("")
    lines.append("Clusters of modules whose top-level `def` / `class` names overlap "
                 "heavily (identical names, or high Jaccard + cosine name-set "
                 "similarity), flagging likely copy-paste accretion.")
    lines.append("")
    if report["duplicate_clusters"]:
        for i, cl in enumerate(report["duplicate_clusters"], 1):
            lines.append(f"### Cluster {i} (size {cl['size']})")
            lines.append("")
            lines.append("```")
            lines.append("\n".join(cl["modules"]))
            lines.append("```")
            lines.append("")
    else:
        lines.append("_None._")
        lines.append("")

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
