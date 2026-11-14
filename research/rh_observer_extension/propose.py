#!/usr/bin/env python3
"""Floating proposals only. Exact acceptance requires certify.py.

Uses the forced Mobius head and a single tail-moment constraint. No zero data.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from math import lcm
from pathlib import Path
import numpy as np
from scipy.special import digamma
from certify import mobius, prefix_direct, prefix_mobius


def gram(K: int) -> np.ndarray:
    G = np.zeros((K, K))
    for i, k in enumerate(range(2, K+2)):
        for j, ell in enumerate(range(2, k+1)):
            period = lcm(k, ell)
            r = np.arange(1, period+1, dtype=float)
            w = (digamma((r+1)/period)-digamma(r/period))/period
            G[i, j] = G[j, i] = np.dot((r % k)/k*(r % ell)/ell, w)
    return G


def propose(N: int, K: int, G: np.ndarray | None = None) -> tuple[dict, dict]:
    if not 1 <= N <= K:
        raise ValueError('Require 1 <= N <= K')
    G = gram(K) if G is None else G[:K, :K]
    a = np.array([-mobius(k) for k in range(2, N+1)], dtype=float)
    H, g = G[N-1:, N-1:], G[N-1:, :N-1] @ a
    e = 1/np.arange(N+1, K+2, dtype=float)
    moment = sum((F(mobius(k), k) for k in range(1, N+1)), F())
    u, v = np.linalg.solve(H, g), np.linalg.solve(H, e)
    tail = -u + ((float(moment)+e@u)/(e@v))*v
    c = {k: F(-mobius(k)) for k in range(2, N+1)}
    for k in range(N+2, K+2):
        c[k] = F(round(float(tail[k-N-1])*(1 << 20)), 1 << 20)
    c[N+1] = (N+1)*(moment-sum((c[k]/k for k in range(N+2, K+2)), F()))
    if not prefix_direct(c, N) or not prefix_mobius(c, N):
        raise ArithmeticError('Exact repair failed')
    cf = np.array([float(c[k]) for k in range(2, K+2)])
    record = {'name': f'tail_extension_N{N}_K{K}', 'prefix_length': N,
              'coefficients': {str(k): str(x) for k, x in c.items() if x}}
    diagnostic = {'name': record['name'], 'floating_norm_squared': float(cf@G@cf),
                  'warning': 'Proposal diagnostic, not a certified optimum or acceptance'}
    return record, diagnostic


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--N', type=int, required=True)
    p.add_argument('--K', type=int, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    record, diagnostic = propose(args.N, args.K)
    args.output.write_text(json.dumps([record], indent=2)+'\n')
    print(json.dumps(diagnostic, indent=2))


if __name__ == '__main__':
    main()
