#!/usr/bin/env python3
"""Replay finite target/observation certificates; no physical source oracle."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import itertools as it
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.carrier_relative_targets import (
    Carrier, Instrument, Target, observable_algebra, behavioral_partition,
    static_fiber, resolve_target, plan_target, target_obstruction,
    first_step_erasure_obstruction,
)
from observational_succ.carrier_finite_part_observer import abel_finite_part


def generate():
    states = tuple(it.product((0, 1), repeat=3))
    eyes = Carrier("two-wavelengths", 8, (
        Instrument("red", "red-unit", tuple(Q(7+2*x) for x,y,h in states), tuple(range(8))),
        Instrument("infrared", "infrared-unit", tuple(Q(3*y-1) for x,y,h in states), tuple(range(8)))))
    target = Target(eyes.source, "xor", tuple(Q(x^y) for x,y,h in states))
    hidden = Target(eyes.source, "hidden-tag", tuple(Q(h) for x,y,h in states))
    fiber = static_fiber(eyes, ((eyes.source, "red", "red-unit", Q(9)),
                               (eyes.source, "infrared", "infrared-unit", Q(-1))))
    decision = resolve_target(eyes, target, fiber)
    algebra = observable_algebra(eyes)
    destructive = Carrier("erasing-source", 3, (
        Instrument("a", "a-unit", (Q(1),Q(0),Q(0)), (0,0,0)),
        Instrument("b", "b-unit", (Q(0),Q(1),Q(0)), (0,0,0))))
    predicate = Target(destructive.source, "is-C", (Q(0),Q(0),Q(1)))
    obstruction = first_step_erasure_obstruction(destructive, predicate)
    part = abel_finite_part(Q(1,32))
    assert decision.status == 'IDENTIFIED' and len(fiber) == 2
    assert len(algebra.rows) == 4 and algebra.express(eyes, target) is not None
    assert target_obstruction(eyes, hidden) is not None
    assert len(behavioral_partition(destructive)) == 3
    assert observable_algebra(destructive).express(destructive, predicate) is not None
    assert obstruction is not None and plan_target(destructive, predicate, 8).policy is None
    assert part.lower < Q(-1,12) < part.upper
    paths = ('observational_succ/carrier_relative_targets.py',
             'observational_succ/carrier_finite_part_observer.py')
    return {
        'schema': 'SUCC-carrier-relative-targets-v1',
        'parent_commit': '461942c0bf616518e668d236d1c6b1596665a7dd',
        'source_hashes': {p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'two_eyes': {'states':8, 'behavioral_classes':len(behavioral_partition(eyes)),
            'algebra_dimension':len(algebra.rows), 'surviving_states':list(fiber),
            'target_values':[str(v) for v in decision.values],
            'hidden_target_obstruction':list(target_obstruction(eyes, hidden)),
            'single_run_xor_cost':plan_target(eyes, target, 2).worst_cost},
        'destructive_source': {'behavioral_classes':3, 'target_in_observable_algebra':True,
            'all_horizon_single_copy_impossibility_witness':
            [[name,str(outcome),i,j,merged] for name,outcome,i,j,merged in obstruction]},
        'abel_two_scale': {'scale':str(part.scale), 'lower':str(part.lower),
            'upper':str(part.upper), 'width':str(part.upper-part.lower),
            'classical_finite_part_enclosed':'-1/12', 'ordinary_sum_redefined':False},
        'physical_source_attested':False, 'scalar_truth_score':None,
        'pi_normality_proved':False, 'RH_proved':False,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--verify', action='store_true')
    p.add_argument('--write', type=Path)
    p.add_argument('--receipt', type=Path, default=ROOT/'research/2026-10-25/CARRIER_TARGET_RECEIPT.json')
    args = p.parse_args()
    value = generate()
    if args.write:
        args.write.write_text(json.dumps(value, indent=2, sort_keys=True)+'\n')
    if args.verify and json.loads(args.receipt.read_text()) != value:
        raise SystemExit('receipt/source mismatch')
    print(json.dumps(value, indent=2, sort_keys=True))


if __name__ == '__main__': main()
