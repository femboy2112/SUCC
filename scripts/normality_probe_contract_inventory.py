"""Inventory every available SUCC test and probe, without guessing theorem status.

This is a discovery/triage tool, not theorem certification. It NEVER promotes a
probe's status from file-name/AST matches. Output is deterministic JSON with
source SHA-256, test names, imports, and candidate families for human audit.
No CI/web access needed. Run from repo: python scripts/normality_probe_contract_inventory.py
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from pathlib import Path

CANDIDATE_FLAGS = {
    "normality_fourier": r"normal|weyl|haar|fourier|pinbed|spectral|digit|parity",
    "time_lag": r"lag|fejer|correl|collision|pair|tensor|coerc|purity",
    "source_identity": r"bbp|source|orig|selected|carry|seed|orbit|green",
    "gauge_transport": r"gauge|holonom|transport|covarian|fibr|relativ|homotop|chart",
    "boundary_probe": r"tomograph|oracle|certificate|proof|boundary|inverse|probe",
    "rh_weil": r"weil|zeta|suzuki|schur|tate|connes|rh_|gamma",
    "goldbach": r"goldbach",
    "collatz": r"collatz|black_sun",
}


def extract(path: Path, root: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=path.as_posix())
        tests = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name.startswith('test_')]
        doc = ast.get_docstring(tree) or ''
        error = None
    except SyntaxError as exc:
        tests, doc, error = [], '', f'{exc.msg} at {exc.lineno}:{exc.offset}'
    basename=path.stem.lower()
    flags=[f for f,pat in CANDIDATE_FLAGS.items() if re.search(pat, basename)]
    return {
        "path": path.relative_to(root).as_posix(),
        "sha256": hashlib.sha256(text.encode('utf-8')).hexdigest(),
        "ast_test_functions": sorted(tests),
        "module_docstring": doc[:300],
        "candidate_flags_from_FILENAME_only": flags,
        "ast_parse_error": error,
        "theorem_status": "UNREVIEWED - metadata cannot certify mathematics",
    }


def build(root: Path) -> dict:
    root=root.resolve()
    paths=sorted([*root.glob('tests/test_*.py'), *root.glob('scripts/*.py')])
    data=[extract(p,root) for p in paths]
    n_tests=sum(p['path'].startswith('tests/') for p in data)
    n_scripts=len(data)-n_tests
    counts={k:sum(k in e['candidate_flags_from_FILENAME_only'] for e in data) for k in CANDIDATE_FLAGS}
    return {
        "method": "static path and AST inventory; no theorem status inferred",
        "root_name": root.name,
        "test_modules": n_tests,
        "scripts": n_scripts,
        "test_function_definitions": sum(len(e['ast_test_functions']) for e in data),
        "candidate_flag_counts_NONEXCLUSIVE": counts,
        "entries": data,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--output',type=Path,default=None)
    args=p.parse_args()
    s=json.dumps(build(args.root), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(s,encoding='utf-8')
    else:
        print(s,end='')


if __name__=='__main__':
    main()
