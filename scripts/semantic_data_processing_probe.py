#!/usr/bin/env python3
"""Reproduce exact semantic information loss for a finite quantum observer."""
from __future__ import annotations

import json
from observational_succ.operational_semantics import measurement_semantic_probe


def main():
    report=measurement_semantic_probe()
    assert report["status"]=="EXACT_SEMANTIC_DATA_PROCESSING"
    assert report["Z_outcomes_0_vs_1_TV"]=="1"
    assert report["X_outcomes_0_vs_1_TV"]=="0"
    assert report["Z_forgotten_TV"]=="0"
    assert not report["source_causal_records_erased"]
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
