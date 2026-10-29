#!/usr/bin/env python3
"""Bounded endpoint-dual experiment; only an exact checked dual is evidence.

All alpha resonances and beta endpoint patterns are enumerated on the stated
even support. Odd velocities are reduced modulo lcm(Q), using the proved
contraction map. A floating LP only proposes nonnegative rational weights;
the separate integer/Fraction checks below decide certificate validity.
Failure to find a dual is not failure to find a local rule.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
import time


def endpoint_patterns(qs):
    cells = tuple((q, k, z) for q in qs for k in range(q)
                  if gcd(k, q//2) == 1 for z in (-1, 1))
    modulus = lcm(*qs)
    patterns = {}
    for v in (*qs, *range(1, modulus, 2)):
        resonances = {}
        for i, (q, k, z) in enumerate(cells):
            alpha = (-F(v*k, q)) % 1
            resonances.setdefault(alpha, []).append((i, -1-F(v*z, q), 1-F(v*z, q)))
        for alpha, intervals in resonances.items():
            endpoints = sorted({x for _, a, b in intervals for x in (a, b)})
            # A closed-endpoint pattern contains every neighbouring open-cell
            # pattern, so endpoints alone suffice for all nonnegative weights.
            for beta in endpoints:
                mask = tuple(i for i, a, b in intervals if a <= beta <= b)
                if mask and mask not in patterns:
                    patterns[mask] = (v, str(alpha), str(beta))
    return cells, patterns, modulus


def solve(qs, seconds):
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    started = time.monotonic()
    cells, patterns, modulus = endpoint_patterns(qs)
    rows, cols = [], []
    for row, pattern in enumerate(patterns):
        rows.extend([row]*len(pattern)); cols.extend(pattern)
    matrix = coo_matrix((np.ones(len(rows)), (rows, cols)),
                        shape=(len(patterns),len(cells))).tocsr()
    eq = np.array([[int(q == cell[0]) for cell in cells] for q in qs])
    print(f"support={qs} cells={len(cells)} patterns={len(patterns)} M={modulus}",flush=True)
    result = linprog(np.zeros(len(cells)), A_ub=matrix,
                     b_ub=np.ones(len(patterns)), A_eq=eq,
                     b_eq=np.ones(len(qs)), bounds=(0,None), method='highs',
                     options={'time_limit':seconds, 'threads':1})
    report = {'schema':'succ.lonely-runner.endpoint-dual-experiment.v1',
              'affected_family':qs,'odd_representatives_modulus':modulus,
              'cells':len(cells),'distinct_endpoint_patterns':len(patterns),
              'seconds':time.monotonic()-started,'solver_status':int(result.status),
              'solver_message':result.message, 'exact_dual_accepted':False,
              'authority':'floating LP proposal only until exact rational checks pass',
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if result.x is not None:
        weights = tuple(F(float(x)).limit_denominator(1000000) for x in result.x)
        nonnegative = all(x >= 0 for x in weights)
        masses = {q:sum(w for w,c in zip(weights,cells) if c[0]==q) for q in qs}
        capacities = [sum(weights[i] for i in mask) for mask in patterns]
        accepted = nonnegative and all(x==1 for x in masses.values()) and max(capacities)<=1
        report.update(exact_dual_accepted=accepted,
                      weights=[str(x) for x in weights],
                      exact_source_masses={str(q):str(x) for q,x in masses.items()},
                      exact_maximum_capacity=str(max(capacities)))
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cap',type=int,choices=(190,192),required=True)
    p.add_argument('--seconds',type=float,default=60)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if not 0<a.seconds<=120:p.error('seconds must be in (0,120]')
    qs=tuple(sorted({d*2**j for d in (1,3) for j in range(1,8) if d*2**j<=a.cap}))
    report=solve(qs,a.seconds)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='weights'},indent=2))


if __name__=='__main__':main()
