"""Deterministic exact finite Yang--Mills/SUCC gauge-oracle receipt.

Run from checkout root: python scripts/yang_mills_gauge_oracle_probe.py
This is NOT a replication of the external million-line Lean proof.
"""
from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction as Q
from itertools import product

from observational_succ.yang_mills_gauge_oracle import (
    AbelianGaugeGraph, Torus4D, wilson_orbit_energy,
    two_state_reflection_eigenvalues, transfer_spectral_ratio,
    gap_lower_from_ratio, quadratic_mass_upper, finite_cutoff_twins,
    nonabelian_trace_counterexample, S3GaugeGraph, S3_ELEMENTS,
    S3_ID, s3_subdivision_square, compose_s3,
)

SUCC_MAIN = 'db9fb4b84672050efa79b13377f1e73364598a14'
OPENAI_YM = '3456e5e75cf8d4cd558955a5c7638fba2d68f464'
ASSESSMENT = '55ba9fc36293b3f4d52c6b1f813169a0be76ee98'


def ratio(x: Q) -> str:
    return f'{x.numerator}/{x.denominator}'


def run() -> dict:
    g=AbelianGaugeGraph(('a','b','c','d'),
        (('a','b'),('b','c'),('c','d'),('d','a'),('a','c')),3)
    counts=Counter(g.holonomies(x) for x in product(range(3),repeat=5))
    s3graph=S3GaugeGraph(('u','v'),(('u','v'),('u','v'),('u','v')))
    s3classes=Counter(s3graph.orbit_key(x) for x in product(S3_ELEMENTS,repeat=3))
    assert len(s3classes)==11
    t=Torus4D(2,3)
    flat=t.flat_nontrivial()
    vacuum=t.zero()
    a=Q(1,16)
    zero=t.curvature_signature(vacuum)
    field=t.curvature_signature(flat)
    assert zero==field and len(field)==96 and all(v==0 for v in field)
    assert all(t.cube_bianchi(flat,x,*axes)==0
        for x in t.sites for axes in ((0,1,2),(0,1,3),(0,2,3),(1,2,3)))
    assert t.wilson_cycle(flat,(0,0,0,0),0)==1
    assert len(counts)==g.orbit_count and set(counts.values())=={g.orbit_size}
    assert finite_cutoff_twins(7,9)[0]==finite_cutoff_twins(7,9)[1]
    assert finite_cutoff_twins(16,9)[0]!=finite_cutoff_twins(16,9)[1]
    return {
        'status': 'CERTIFIED_FINITE_EXACT_ONLY',
        'clay_yang_mills_mass_gap': 'OPEN',
        'openai_wightman_existence': 'EXTERNAL_FORMAL_AND_ASSESSED_NOT_REPLAYED_HERE',
        'original_public_sources': {
            'succ_main_commit': SUCC_MAIN,
            'openai_yang_mills_submission_commit': OPENAI_YM,
            'yang_mills_group_assessment_commit': ASSESSMENT,
        },
        'abelian_gauge_orbits': {
            'group':'Z/3Z', 'vertices':4,'edges':5,'cycle_rank':g.cycle_rank,
            'configurations':3**5,'gauge_orbits':g.orbit_count,
            'configurations_per_orbit':g.orbit_size,
            'orbit_distribution_energy_under_uniform_enumeration':ratio(
                wilson_orbit_energy(g,tuple(product(range(3),repeat=5)))),
        },
        'four_torus': {
            'dimension':4,'side':2,'gauge':'Z/3Z',
            'vertices':len(t.sites),'links':t.link_count,'plaquettes':t.plaquette_count,
            'zero_local_curvature_both':True,
            'distinct_global_wilson_holonomy':[0,t.wilson_cycle(flat,(0,0,0,0),0)],
            'discrete_bianchi_satisfied':True,
        },
        'two_state_transfer_control': {
            'mesh':ratio(a), 'quadratic_spectral_ratio':ratio(transfer_spectral_ratio(a,'quadratic')),
            'linear_spectral_ratio':ratio(transfer_spectral_ratio(a,'linear')),
            'quadratic_physical_mass_upper_bound':ratio(quadratic_mass_upper(a)),
            'linear_physical_mass_lower_bound':ratio(gap_lower_from_ratio(a,transfer_spectral_ratio(a,'linear'))),
            'entrywise_positive_kernel_that_is_not_psd_eigenvalues':[
                ratio(v) for v in two_state_reflection_eigenvalues(Q(1),Q(2))],
        },
        'nonabelian_S3_quotient': {'link_configurations':6**3,'joint_conjugacy_orbits':len(s3classes),
            'mixed_trace_control':nonabelian_trace_counterexample(),
            'oriented_two_link_gauge_square_cases':6**5,
            'sample_gauge_square_commutes':s3_subdivision_square((1,0,2),(0,2,1),
                S3_ID,(0,2,1),(1,0,2))['commutes'],
            'noncommuting_order_mutation_rejected':compose_s3((1,0,2),(0,2,1)) !=
                compose_s3((0,2,1),(1,0,2))},
        'forbidden_inference': 'finite gauge completeness, reflection-like PSD and nonzero finite gaps do not prove four-dimensional continuum Yang-Mills existence or its mass gap',
    }


def main() -> None:
    print(json.dumps(run(),indent=2,sort_keys=True))

if __name__=='__main__':
    main()
