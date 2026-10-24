#!/usr/bin/env python3
"""Adaptive exact checks of the inverse-branch lemma, not its open premise.

The prime/radius choices below are post-derivation checks. They were not part
of the original preregistered source-energy measurements. No fitted branch
fraction or asymptotic conclusion is returned.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_source_collision import bbp_forcing, bbp_states


def centered(x):
    return (x + Q(1, 2)) % 1 - Q(1, 2)


def main():
    rows = []
    pair_checks = 0
    zero_branch_checks = 0
    for p in (41, 97, 257):
        m = (p-1)//8
        a, b = m+1, 4*m
        n = b-a
        states = bbp_states(b)
        eps = bbp_forcing(a+1)-bbp_forcing(b)
        assert 0 < eps < Q(15, (p+8)*(p+9))
        radii = (Q(1, 4), Q(1, 16), Q(1, 64))
        assert all(eps < tau <= Q(1, 4) for tau in radii)
        counters = [dict(current=0, successor=0, small_current=0,
                         zero_branch=0, literal_carry_differences=0)
                    for _ in radii]
        for s in range(a, b):
            for t in range(a, b):
                delta = centered(states[t]-states[s])
                nxt = centered(states[t+1]-states[s+1])
                forcing_delta = bbp_forcing(t+1)-bbp_forcing(s+1)
                kappa = 16*delta+forcing_delta-nxt
                assert abs(forcing_delta) <= eps and kappa.denominator == 1
                literal = ((16*states[t]+bbp_forcing(t+1))//1
                           -(16*states[s]+bbp_forcing(s+1))//1)
                pair_checks += 1
                for tau, counter in zip(radii, counters):
                    current_close = abs(delta) <= tau
                    next_close = abs(nxt) <= tau
                    small = abs(delta) <= (tau-eps)/16
                    zero = abs(delta) <= Q(1, 32) and next_close
                    assert not small or zero
                    if zero:
                        assert kappa == 0
                        zero_branch_checks += 1
                    counter['current'] += current_close
                    counter['successor'] += next_close
                    counter['small_current'] += small
                    counter['zero_branch'] += zero
                    counter['literal_carry_differences'] += zero and literal != 0
        for tau, counter in zip(radii, counters):
            assert counter['small_current'] <= counter['zero_branch']
            assert abs(counter['current']-counter['successor']) <= 2*n
            rows.append(dict(prime=p, window_length=n, radius=str(tau),
                             forcing_drift=str(eps), **counter))

    # Enlarging the central branch to 1/16 would admit a nonzero centered carry.
    mutant_delta, mutant_next, mutant_forcing = Q(1, 16), Q(0), Q(0)
    mutant_carry = 16*mutant_delta+mutant_forcing-mutant_next
    assert abs(mutant_delta) > Q(1, 32) and mutant_carry == 1
    paths = ['scripts/twisted_inverse_branch_oracle.py',
             'observational_succ/pi_source_collision.py']
    result = dict(
        status='VERIFIED_FINITE', pi_normality='OPEN',
        sampling_scope='adaptive post-derivation checks; no branch fraction fitted',
        open_nonmonopolization_premise_proved=False,
        pair_recurrence_checks=pair_checks,
        zero_centered_carry_checks=zero_branch_checks,
        enlarged_branch_mutation_detected=True,
        rows=rows,
        source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                       for p in paths})
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
