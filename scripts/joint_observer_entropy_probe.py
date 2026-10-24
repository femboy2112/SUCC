#!/usr/bin/env python3
"""Exact joint/trimmed entropy controls with independently enclosed BBP cells."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from math import lcm
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.joint_observer_entropy import (
    WordLaw, bbp_safe_start, collision_data_processing,
    conditional_collision_chain, one_cell_collision_transport,
    trimmed_entropy_budget,
)
from observational_succ.pi_source_genesis import machin_pi_interval


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return encode(asdict(value))
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def literal_source(last):
    """Independent four-pole recurrence, retaining the full rational lift."""
    values = [Q()]
    for n in range(1, last+1):
        r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        values.append(16*values[-1]+r)
    return values


def exact_log_sign(terms):
    common = lcm(*(coefficient.denominator for coefficient, _ in terms))
    value = Q(1)
    for coefficient, argument in terms:
        value *= argument**int(coefficient*common)
    return (value > 1)-(value < 1)


def main():
    counts = Counter()
    joint_rows = []
    for base, depth in ((2, 4), (3, 3), (5, 3), (16, 2)):
        words = tuple(product(range(base), repeat=depth))
        uniform = WordLaw(base, depth, tuple((w, Q(1, len(words))) for w in words))
        constrained = WordLaw(base, depth, tuple(
            (w, Q(1, base**(depth-1))) for w in words if sum(w) % base == 0))
        weights = {w: 1+sum((j+1)*a for j,a in enumerate(w)) for w in words}
        weighted = WordLaw(base, depth, tuple(
            (w, Q(m, sum(weights.values()))) for w,m in weights.items()))
        point = WordLaw(base, depth, (((0,)*depth, 1),))
        for name, law in (('uniform', uniform), ('sum_zero', constrained),
                          ('weighted', weighted), ('point', point)):
            chain = conditional_collision_chain(law)
            product_ratio = Q(1)
            for step in chain:
                product_ratio *= step.ratio
            assert product_ratio == law.collision
            counts['joint_chain_laws'] += 1
            counts['joint_chain_steps'] += len(chain)
            joint_rows.append(dict(base=base, depth=depth, law=name,
                                   collision=law.collision,
                                   conditional_ratios=[step.ratio for step in chain]))
        for omitted in range(depth):
            marginals = {}
            for w, mass in constrained.atoms:
                v = w[:omitted]+w[omitted+1:]
                marginals[v] = marginals.get(v,Q())+mass
            assert set(marginals.values()) == {Q(1, base**(depth-1))}
            counts['proper_coordinate_marginals'] += 1
        assert constrained.collision != 1
        counts['false_product_marginal_mutations_rejected'] += 1
        decoder = {w: sum(w) % base for w in words}
        decoded = collision_data_processing(constrained, uniform, decoder)
        assert decoded.before == decoded.after == base
        counts['visible_joint_decoders'] += 1

    correlated_reference = WordLaw(2, 2, (
        ((0, 0),Q(1,2)), ((0, 1),Q(1,4)),
        ((1, 0),Q(1,8)), ((1, 1),Q(1,8))))
    actual = WordLaw(2, 2, tuple((w,Q(1,4)) for w in product(range(2),repeat=2)))
    correlated_chain = conditional_collision_chain(actual, correlated_reference)
    assert [s.ratio for s in correlated_chain] == [Q(4,3),Q(33,32)]

    rare_rows = []
    for base in (2,3,5,16):
        for depth in (2,3):
            delta=Q(1,depth)
            law=WordLaw(base,depth,tuple(
                (w,(1-delta)/base**depth+(delta if not any(w) else 0))
                for w in product(range(base),repeat=depth)))
            assert law.collision == 1+delta**2*(base**depth-1)
            counts['rare_hotspot_mixtures'] += 1
            rare_rows.append(dict(base=base,depth=depth,discarded_mass=delta,
                                  full_collision=law.collision,retained_collision=1))

    entropy_rows=[]
    for base in (2,3,5):
        for depth,k in ((2,1),(3,1),(4,2)):
            horizon=12
            word=tuple((j*j+2*j+1)%base for j in range(horizon+depth-1))
            for retained in (tuple(range(horizon)),(0,2,5,9)):
                budget=trimmed_entropy_budget(word,horizon,depth,k,retained,base)
                terms=list(budget.log_terms)
                terms.extend((-mass,mass*base**k)
                             for _,mass in budget.original_short_law.atoms)
                sign=exact_log_sign(terms)
                assert sign>=0
                counts['integer_power_entropy_comparisons']+=1
                entropy_rows.append(dict(base=base,depth=depth,block_length=k,
                                         retained=len(retained),discarded_mass=budget.discarded_mass,
                                         collision=budget.retained_collision,
                                         exact_log_bound_sign=sign))

    values=literal_source(96)
    pi_lo,pi_hi=machin_pi_interval(160)
    source_rows=[]
    for depth in (1,2,3,4):
        cells=16**depth
        start=bbp_safe_start(depth)
        phases=[]
        shifts=[]
        certified_cells=[]
        for n in range(start,97):
            low=16**n*pi_lo/16
            high=16**n*pi_hi/16
            tail_lo,tail_hi=low-values[n],high-values[n]
            assert 0<tail_lo<tail_hi<Q(1,(8*n+1)*(8*n+2))<=Q(1,cells)
            lo_cell=int(cells*low)
            hi_cell=int(cells*high)
            assert lo_cell==hi_cell
            certified_cells.append(lo_cell%cells)
            phases.append(values[n]%1)
            shifts.append((tail_lo+tail_hi)/2)
            counts['independent_machin_true_cells']+=1
        transport=one_cell_collision_transport(phases,shifts,cells)
        literal_counts=Counter(certified_cells)
        literal_collision=Q(cells*sum(c*c for c in literal_counts.values()),len(phases)**2)
        assert transport.after==literal_collision
        assert transport.after<=2*transport.before
        counts['authentic_source_transport_rows']+=1
        source_rows.append(dict(depth=depth,cells=cells,start=start,
                                retained_positions=len(phases),
                                source_collision=transport.before,
                                certified_true_collision=transport.after,
                                observed_ratio=transport.after/transport.before))

    for depth in range(33):
        cutoff=bbp_safe_start(depth)
        assert (8*cutoff+1)*(8*cutoff+2)>=16**depth
        assert not cutoff or (8*cutoff-7)*(8*cutoff-6)<16**depth
        counts['integer_cutoff_minimality']+=1
    try:
        one_cell_collision_transport((0,Q(1,3),Q(2,3)),(Q(2,3),Q(1,3),0),3)
    except ValueError:
        counts['two_cell_mutation_rejected']+=1
    else:
        raise AssertionError('two-cell mutation was accepted')

    inputs=(
        'observational_succ/joint_observer_entropy.py',
        'tests/test_joint_observer_entropy.py',
        'scripts/joint_observer_entropy_probe.py',
        'observational_succ/pi_source_genesis.py',
        'research/2026-10-24/PI_TRIMMED_JOINT_ENTROPY.md',
        'research/2026-10-24/PI_HYPOTHESIS_A_HOLE_CONTRACT.md')
    result=dict(status='VERIFIED_EXACT_FINITE',pi_normality='OPEN',
                actual_source_asymptotic_collision_bound_proved=False,
                authority='elementary paper lemmas and finite exact calibration',
                held_out_base=5,counts=dict(sorted(counts.items())),
                joint_rows=joint_rows,correlated_reference_chain=correlated_chain,
                rare_hotspot_rows=rare_rows,trimmed_entropy_rows=entropy_rows,
                authentic_source_rows=source_rows,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    text=json.dumps(encode(result),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text,end='')


if __name__=='__main__':
    main()
