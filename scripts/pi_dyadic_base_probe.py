#!/usr/bin/env python3
"""Exact probes frozen in PI_DYADIC_BASE_PREREGISTRATION.md.

No finite outcome certifies asymptotic tripling invariance or pi normality.
Large fractions are summarized with rigorous enclosures and binary hashes.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt, lcm, prod
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.bbp_two_adic import (
    forcing_mod, particular_mod, residue_collision_count, time_transport_mod,
)
from observational_succ.pi_source_collision import bbp_forcing, bbp_states, small_ball_pairs
from observational_succ.pi_binary_branch import (
    binary_branch_profile, reconstruct_carry_law_mod_11_13, residue_marginal,
)
from observational_succ.pi_base_transport import (
    cantor_two_digit_sample, multiplication_coupling, outward_decimal,
    sorted_multiplication_coupling, source_successor_transport_bound,
    source_to_pi_coupling_budget,
)


def fraction_digest(value):
    value = Q(value)
    def encode(integer):
        sign = b'-' if integer < 0 else b'+'
        integer = abs(integer)
        data = integer.to_bytes(max(1, (integer.bit_length()+7)//8), 'big')
        return sign + len(data).to_bytes(8, 'big') + data
    return hashlib.sha256(encode(value.numerator)+encode(value.denominator)).hexdigest()


def enclosure(value):
    value = Q(value)
    lo, hi = outward_decimal(value)
    return dict(lower=str(lo), upper=str(hi), width=str(hi-lo),
                exact_binary_fraction_sha256=fraction_digest(value),
                numerator_bits=abs(value.numerator).bit_length(),
                denominator_bits=value.denominator.bit_length())


def integer_branch_profiles(current, successor, forcing, radii):
    """Independent common-denominator/literal-carry oracle, diagonal included."""
    denominator = lcm(*(x.denominator for x in (*current, *successor)))
    assert denominator % 2 == 1
    xs = [x.numerator*(denominator//x.denominator) for x in current]
    ys = [y.numerator*(denominator//y.denominator) for y in successor]
    literal = [(16*x+f).__floor__() for x, f in zip(current, forcing)]
    counters = [Counter() for _ in radii]
    for s in range(len(xs)):
        for t in range(len(xs)):
            raw, raw_next = xs[t]-xs[s], ys[t]-ys[s]
            wrap = (2*raw+denominator)//(2*denominator)
            wrap_next = (2*raw_next+denominator)//(2*denominator)
            d_next = raw_next-wrap_next*denominator
            carry = literal[t]-literal[s]-16*wrap+wrap_next
            for tau, counter in zip(radii, counters):
                if abs(d_next)*tau.denominator <= tau.numerator*denominator:
                    assert -8 <= carry <= 8
                    counter[carry] += 1
    return counters


def clock_rows():
    rows = []
    for bits in range(1, 13):
        modulus = 1 << bits
        r = [forcing_mod(n, bits) for n in range(modulus)]
        f = [particular_mod(n, bits) for n in range(modulus)]
        assert sorted(r) == sorted(f) == list(range(modulus))
        if bits > 1:
            assert all(f[n] % (modulus//2) == particular_mod(n, bits-1)
                       for n in range(modulus))
        rows.append(dict(bits=bits, modulus=modulus,
                         forcing_permutation=True, source_permutation=True,
                         zero_value=f[0], reduction_compatible=True))
    zero_bits = (4, 8, 12, 16, 20, 24, 32, 48, 64, 100, 128)
    assert all(particular_mod(0, k) == 0 for k in zero_bits)
    transport = []
    for bits in (4, 7, 10):
        modulus = 1 << bits
        for q in (3, 5, 7, 11, 13):
            perm = [time_transport_mod(q, n, bits) for n in range(modulus)]
            assert sorted(perm) == list(range(modulus))
            assert all(particular_mod(j, bits) == q*particular_mod(n, bits) % modulus
                       for n, j in enumerate(perm))
            assert all(time_transport_mod(pow(q,-1,modulus), perm[n], bits) == n
                       for n in range(modulus))
            transport.append(dict(bits=bits, multiplier=q, permutation=True,
                                  source_congruence=True, inverse_verified=True))
        assert all(time_transport_mod(3,time_transport_mod(5,n,bits),bits)
                   == time_transport_mod(15,n,bits) for n in range(modulus))
    bits = 10  # held-out real test; 4/8-bit checks preceded preregistration
    states = bbp_states((1 << bits)-1)
    perm = [time_transport_mod(3,n,bits) for n in range(1 << bits)]
    coupling = multiplication_coupling(states,3,perm)
    return dict(complete_quotients=rows,zero_checked_bits=list(zero_bits),
                odd_time_transports=transport,composition_3_5=True,
                heldout_modular_transport_real_cost=dict(bits=bits,
                    cost=enclosure(coupling.cost),normality_inference=False))


def branch_rows(source, a, b, p):
    current, successor = source[a:b], source[a+1:b+1]
    forcing = [bbp_forcing(k+1) for k in range(a,b)]
    epsilon = forcing[0]-forcing[-1]
    radii, tau = [], Q(1,4)
    for _ in range(4):
        if tau <= epsilon:
            break
        radii.append(tau)
        tau = (tau-epsilon)/16
    tables = integer_branch_profiles(current,successor,forcing,radii)
    entries = []
    for depth,(tau,table) in enumerate(zip(radii,tables)):
        nested = [sum(c for k,c in table.items() if k % (1<<j)==0) for j in range(5)]
        ratios = [Q(v,u) for u,v in zip(nested,nested[1:])]
        assert prod(ratios) == Q(table[0],nested[0])
        assert nested[0] == small_ball_pairs(successor,tau)
        assert nested[4] == table[0]
        assert sum(c for k,c in table.items() if k % 9==0) == table[0]
        rebuilt = reconstruct_carry_law_mod_11_13(
            residue_marginal(table,11),residue_marginal(table,13))
        assert rebuilt == tuple(Q(table.get(k,0)) for k in range(-8,9))
        if p in (73,193):
            direct = binary_branch_profile(current,forcing,tau,successor=successor)
            assert direct.nested_counts == tuple(nested)
            assert dict(direct.signed_counts) == dict(table)
        entries.append(dict(depth=depth,radius=str(tau),
            signed_carry_counts={str(k):table.get(k,0) for k in range(-8,9)},
            nested_binary_counts=nested,conditional_retentions=[str(v) for v in ratios],
            zero_retention=str(Q(table[0],nested[0])),
            half_allowances_per_sample=[str(max(Q(0),Q(2*v-u,2*len(current))))
                                      for u,v in zip(nested,nested[1:])],
            diagonal_included=len(current),mod9_identifies_zero=True,
            separate_11_13_reconstruction=True))
    return dict(overlap_length=len(current),forcing_span=str(epsilon),
                radii_are_diagnostic_not_asymptotic_schedule=True,
                direct_fraction_crosscheck=p in (73,193),rows=entries)


def source_rows():
    rows = []
    branch_primes = (73,193,353,577,1153,1601)
    for p in branch_primes+(2081,4129):
        assert p % 8 == 1 and all(p % q for q in range(2,isqrt(p)+1))
        m = (p-1)//8
        a,b = m+1,4*m
        source = bbp_states(b)
        values = source[a:b+1]
        n = len(values)
        sorted_coupling = sorted_multiplication_coupling(values,3)
        same = multiplication_coupling(values,3,tuple(range(n)))
        automatic = multiplication_coupling(values,16,tuple(range(1,n))+(0,))
        automatic_bound = source_successor_transport_bound(a,n)
        assert automatic.cost <= automatic_bound
        row = dict(prime=p,source_start=a,source_end=b,full_length=n,
            holdout_for_this_instrument=p in (1153,1601),
            sorting_tripling_cost=enclosure(sorted_coupling.cost),
            tripling_observable_lower=enclosure(sorted_coupling.observable_lower_bound),
            same_index_tripling_cost=enclosure(same.cost),
            source_to_pi_tripling_budget=enclosure(source_to_pi_coupling_budget(a,n,3)),
            automatic_times16_cost=enclosure(automatic.cost),
            automatic_times16_bound=enclosure(automatic_bound))
        prescribed_m = 1
        while (16*prescribed_m)**5 <= p*p:
            prescribed_m *= 16
        real_pairs = small_ball_pairs(values,Q(1,16))
        padic_pairs = residue_collision_count(n,4)
        row['collision_comparison'] = dict(prescribed_M=prescribed_m,diagnostic_M=16,
            real_ordered_pairs=real_pairs,dyadic_ordered_pairs=padic_pairs,
            real_scaled=str(Q(16*real_pairs,n*n)),
            dyadic_scaled=str(Q(16*padic_pairs,n*n)),
            real_to_dyadic_ratio=str(Q(real_pairs,padic_pairs)))
        if p in branch_primes:
            row['branch_diagnostics'] = branch_rows(source,a,b,p)
        rows.append(row)
    return rows


def control_rows():
    grid = tuple(Q(n,257) for n in range(257))
    assert sorted_multiplication_coupling(grid,3).cost == 0
    cantor = sorted_multiplication_coupling(cantor_two_digit_sample(8),3)
    assert cantor.cost == cantor.observable_lower_bound == (1-Q(1,16**8))/15
    return dict(uniform_grid=dict(size=257,sorted_tripling_cost='0'),
        cantor_changed_source=dict(depth=8,cost=enclosure(cantor.cost),
            exact_formula='(1-16^-8)/15',
            positive_collision_dimension_does_not_imply_tripling=True),
        rejected_mutations=['nonbijective matching','marginal-halves multiplied',
            'uniform odd-prime carry marginals','dropped carry memory',
            '2-adic congruence treated as real closeness'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = dict(status='VERIFIED_FINITE',pi_normality='OPEN',
        half_retention_proved_for_real_source=False,
        tripling_invariance_proved_for_real_source=False,
        half_and_one_sixteenth_refinement_proved_for_dyadic_unwrapped_source=True,
        precision='exact integer/Fraction decisions; decimal summaries outward rounded',
        clock=clock_rows(),source_windows=source_rows(),controls=control_rows())
    files = ['scripts/pi_dyadic_base_probe.py','observational_succ/bbp_two_adic.py',
        'observational_succ/pi_binary_branch.py','observational_succ/pi_base_transport.py',
        'observational_succ/pi_source_collision.py',
        'research/2026-10-24/PI_DYADIC_BASE_PREREGISTRATION.md']
    result['source_sha256'] = {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=result['status'],output=str(args.output),
        source_windows=len(result['source_windows']),
        branch_scale_rows=sum(len(r.get('branch_diagnostics',{}).get('rows',[]))
                              for r in result['source_windows']),pi_normality='OPEN')))


if __name__=='__main__':
    main()
