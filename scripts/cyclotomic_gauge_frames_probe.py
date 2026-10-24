#!/usr/bin/env python3
"""Independent integer-pair oracle for cyclotomic SUCC time frames.

Reconstructs orthogonality from a direct modular character computation
rather than calling the reusable twirl/DFT utilities. No pi digits or
simulation inference; all receipts below are exact integer identities.
"""
import json
from fractions import Fraction
from math import gcd

from observational_succ.cyclotomic_gauge_frames import (
    bbp_signed_lag_budget, bbp_energy_budget,
    certified_origin_energy_interval, least_clock_modulus
)


def manual_order(b, q):
    for d in range(1,q+1):
        if pow(b,d,q)==1:
            return d
    raise ArithmeticError("no modular order")


def independent_probe(base=16, period=3, length=10, modulus=7):
    assert type(base) is int and base>=2
    assert type(period) is int and period>=1
    assert type(length) is int and length>=1
    assert type(modulus) is int and modulus>=2
    assert gcd(base,modulus)==1
    assert manual_order(base,modulus)==period

    # Treat every v_j * conj(v_k) as a DIFFERENT formal indeterminate.
    # Thus agreeing pair sets is stronger than matching a sampled float.
    group_terms={}
    for j in range(length):
        for k in range(length):
            spatial_exponent=(pow(base,j,modulus)-pow(base,k,modulus))%modulus
            if spatial_exponent!=0:
                continue
            assert (j-k)%period==0
            harmonic=j//period-k//period
            group_terms.setdefault(harmonic,set()).add((j,k))

    maximum=(length-1)//period
    assert set(group_terms)==set(range(-maximum,maximum+1))
    for ell in range(0,maximum+1):
        expected={(k+ell*period,k)
                  for k in range(length-ell*period)}
        assert group_terms[ell]==expected

    K=2*maximum+1
    dft_samples={}
    for ell in range(maximum+1):
        # Independent cyclic group algebra projector:
        # sum_m zeta_K^(m*(power-ell))/K equals a Kronecker delta.
        recovered=set()
        for power,pairs in group_terms.items():
            if (power-ell)%K==0:
                recovered|=pairs
        expected={(j+ell*period,j)
                  for j in range(length-ell*period)}
        assert recovered==expected
        dft_samples[str(ell)]=len(recovered)

    nclass=[sum(j%period==r for j in range(length))
            for r in range(period)]
    unordered_pairs=[(j,k) for j in range(length)
                     for k in range(j)
                     if (j-k)%period==0]
    freqs=[base**j-base**k for j,k in unordered_pairs]
    assert len(set(freqs))==len(freqs)
    haar_variance=2*len(unordered_pairs)
    fixed_energy=sum(n*n for n in nclass)
    assert fixed_energy==length+haar_variance

    # Intentionally wrong reference-frame invariant: without chart drift,
    # base*(x-a) would equal base*x-a for arbitrary a. Directly refute it.
    bad_origin=Fraction(1,7)
    wrong=(base*(Fraction(2,7)-bad_origin))%1
    correct=(base*Fraction(2,7)-bad_origin)%1
    assert wrong!=correct

    if base==16 and modulus==7 and period==3 and length==10:
        assert least_clock_modulus(16,3,100)==7
        assert (fixed_energy,haar_variance,K)==(34,24,7)
        assert gcd(15,273)==3
        assert manual_order(16,119)==6
        assert manual_order(16,17)==2
        assert manual_order(16,11)==5

    bound=bbp_energy_budget(length,period,1)
    assert 0<=bound
    report={
        "base":base,"period":period,"modulus":modulus,"horizon":length,
        "source_branch":"pi-source-genesis #253; cycloframe child",
        "time_classes":nclass,
        "character_orthogonality":"EXACT MODULAR",
        "cyclic_dft_inverse":"EXACT GROUP ALGEBRA",
        "positive_laurent_coefficient_term_counts":dft_samples,
        "alias_free_temporal_phases":K,
        "haar_expectation":length,
        "haar_variance":haar_variance,
        "periodic_counterexample_energy":fixed_energy,
        "wrong_chart_mutant":"REJECTED",
        "cyclotomic_factor_coprime_mutant":"REJECTED",
        "bbp_signed_energy_transport_budget":str(bound),
        "pi_normality":"OPEN",
    }
    return report


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    a=parser.parse_args()
    result=independent_probe()
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if a.output:
        from pathlib import Path
        Path(a.output).write_text(text,encoding="utf-8")
    else:
        print(text,end="")
