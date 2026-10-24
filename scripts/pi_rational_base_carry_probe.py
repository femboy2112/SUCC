"""Deterministic rational BBP/11-10 carry probes, certified pi enclosure.

Finite calibration only. Do not infer a limit or a normality theorem.
"""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from math import comb
from observational_succ.pi_rational_base_carry import (
    bbp_forcing, bbp_source_states, bbp_newton_coefficient,
    successor_pascal_source, rational_base_digits, rational_base_value,
    prefix_from_residue, residue_from_prefix, pascal_additive_terms,
    binary_source_carry_stat, centered_phase)


def atan_interval(z: int, terms: int) -> tuple[Q,Q]:
    total=sum((Q((-1)**j, (2*j+1)*z**(2*j+1)) for j in range(terms)),Q())
    next_term=Q((-1)**terms, (2*terms+1)*z**(2*terms+1))
    return min(total,total+next_term),max(total,total+next_term)


def pi_interval(terms: int=420) -> tuple[Q,Q]:
    a,b=atan_interval(5,terms),atan_interval(239,terms)
    return 16*a[0]-4*b[1],16*a[1]-4*b[0]


def main(path: str) -> None:
    count=0
    p_lo,p_hi=pi_interval(560)
    assert p_lo < Q(22,7) and p_hi > Q(3)
    count += 2
    alpha_lo,alpha_hi=p_lo/16,p_hi/16
    decimal=[]
    for k in range(1,65):
        d=successor_pascal_source(k,10)
        lo=10**k*alpha_lo-d
        hi=10**k*alpha_hi-d
        if k%2==0:
            assert lo>0 and hi<Q(2,3)**k*alpha_hi
        else:
            assert hi<0 and -lo<Q(2,3)**k*alpha_hi
        decimal.append({'k':k,'sign':'positive' if k%2==0 else 'negative',
                        'bound_exponent':k,'valuation2':3*k-k.bit_count()-1})
        def _v2(n):
            power = 0
            while n and n % 2 == 0:
                power += 1
                n //= 2
            return power
        assert _v2(d.numerator)-_v2(d.denominator)==3*k-k.bit_count()-1
        count += 3
    assert p_hi-p_lo<Q(1,10**400)
    count += 1
    direct=[]
    for p,q in ((3,2),(11,10),(7,3),(5,4)):
        for N in range(0,180):
            word=rational_base_digits(N,p,q)
            assert rational_base_value(word,p,q)==N
            if p==q+1:
                assert sum(pascal_additive_terms(word,p,q),Q())==N
                count+=1
            for depth in range(1,4):
                assert residue_from_prefix(prefix_from_residue(N,p,q,depth),p,q)==N%(p**depth)
                count+=1
            count+=1
        direct.append({'p':p,'q':q,'integer_samples':180})
    rows=[]
    largest=4*((1153-1)//8)
    y,C=bbp_source_states(largest+1)
    for p in [73,137,281,521,1153]:
        m=(p-1)//8
        window=range(m+1,4*m+1)
        row=binary_source_carry_stat(y,window,11)
        ternary=tuple(prefix_from_residue(C[n],11,10,2) for n in window)
        assert all(residue_from_prefix(a,11,10)==C[n]%121 for n,a in zip(window,ternary))
        count+=len(window)
        rows.append({'prime':p,'first':m+1,'last':4*m,'N':row['size'],
                     'mod11_counts':list(row['residue']),
                     'residue_tv':str(row['residue_tv']),
                     'joint_vs_product_tv':str(row['joint_vs_product_tv']),
                     'mod121_distinct':len(set(ternary))})
    # Clock v_11(16^5-1)=1; all first 4 levels have exact predicted period.
    periods=[]
    for L in range(1,5):
        modulus=11**L
        order=5*11**(L-1)
        assert pow(16,order,modulus)==1
        if L>1:assert pow(16,order//11,modulus)!=1
        else:assert all(pow(16,j,modulus)!=1 for j in range(1,5))
        periods.append({'L':L,'order':order})
        count+=(5 if L==1 else 2)
    # Authentic selected zero-centered-carry gate split by the p=11 source label.
    # These calibration windows were selected for comparability, not as a blind holdout.
    pair_rows=[]
    rr=[None]+[bbp_forcing(n) for n in range(1,largest+2)]
    for p in (137,281,521):
        m=(p-1)//8
        indices=range(m+1,4*m+1)
        for tau in (Q(1,4),Q(1,16)):
            E=[0,0]; Z=[0,0]; offE=[0,0]; offZ=[0,0]
            for s in indices:
                for t in indices:
                    dp=centered_phase(y[t+1]-y[s+1])
                    if abs(dp)>tau:continue
                    delta=centered_phase(y[t]-y[s])
                    kappa=16*delta+rr[t+1]-rr[s+1]-dp
                    assert kappa.denominator==1
                    # At these selected radii, the central lift is the zero residue mod 16.
                    label=int(C[s]%11==C[t]%11)
                    E[label]+=1;Z[label]+=int(kappa==0)
                    if s!=t:
                        offE[label]+=1;offZ[label]+=int(kappa==0)
                    count+=1
            pair_rows.append({'prime':p,'tau':str(tau),
                              'same_mod11':{'E':E[1],'Z':Z[1],'offdiag_E':offE[1],'offdiag_Z':offZ[1]},
                              'different_mod11':{'E':E[0],'Z':Z[0],'offdiag_E':offE[0],'offdiag_Z':offZ[0]}})
    # Certified true-base-16 integer lift discrepancy check on the same windows.
    mismatches=[]
    for p in [73,137,281,521,1153]:
        m=(p-1)//8
        diff=0
        for n in range(m+1,4*m+1):
            lo=16**n*alpha_lo
            hi=16**n*alpha_hi
            f_lo=lo.numerator//lo.denominator
            f_hi=hi.numerator//hi.denominator
            assert f_lo==f_hi, 'insufficient Machin precision for independent true pi lift'
            diff+=(C[n]!=f_lo)
            count+=1
        mismatches.append({'p':p,'disagree_source_vs_true_pi_integer_lift':diff})
    root=Path(__file__).resolve().parents[1]
    module=root/'observational_succ/pi_rational_base_carry.py'
    tests=root/'tests/test_pi_rational_base_carry.py'
    receipt={'scope':'source-specific finite exact probes; no asymptotic pi normality inference',
             'source_initial_state':'U_0=0',
             'source':'four-pole BBP forcing',
             'module_sha256':hashlib.sha256(module.read_bytes()).hexdigest(),
             'tests_sha256':hashlib.sha256(tests.read_bytes()).hexdigest(),
             'pi_interval_width_lt':'1/10^400',
             'counted_exact_predicate_checks':count,
             'decimal_pascal':decimal,
             'rational_base_roundtrips':direct,
             'selected_source_windows':rows,
             'source_selected_joint_carry_gate':pair_rows,
             'source_pi_lift_discrepancies':mismatches,
             'prime11_clock':periods,
             'claim':'pi normality OPEN; all-scale real carry loss OPEN'}
    Path(path).write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print('counted exact predicate checks:',count)
    print('p11 window outputs:',[(r['prime'],r['N'],r['residue_tv']) for r in rows])
    print('source vs true pi lift:',mismatches)

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='/tmp/pi_rational_base_carry_receipt.json')
    args=parser.parse_args()
    main(args.output)
