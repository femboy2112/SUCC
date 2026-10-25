"""Exact separate SUCC mirror/Pascal and harmonic-vdC research controls."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path

from observational_succ.harmonic_mirror_succ import (
    harmonic,harmonic_pascal,harmonic_difference,source_rays,mirror_step,
    bbp_mirror_forcing,source_pole_moment,prime_fucc_log_bracket,
    counterfeit_mirror_force,counterfeit_mirror_tail,counterfeit_mirror_state,
)
from observational_succ.pi_harmonic_lag import (
    lag_kernel,mixture_weights,exact_vdc_mixture,naive_signed_harmonic_symbol_pi,
    alternating_spectral_symbol_pi,harmonic_source_error_bound,
    harmonic_exact_source_error_sum,critical_harmonic_lag_schedule,
    last_lag_weight_ratio,
)


def report() -> dict:
    n_assert=0
    for n in range(121):
        assert harmonic(n)==harmonic_pascal(n)
        n_assert+=1
    for n in range(31):
        for k in range(1,13):
            expected=sum((Q((-1)**(k-j)*comb(k,j))*harmonic(n+j)
                          for j in range(k+1)),Q())
            assert harmonic_difference(n,k)==expected
            n_assert+=1
    for n in range(1,513):
        source=bbp_mirror_forcing(n)
        assert source==Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
        assert source>0
        for c,point in zip((7,4,3,2),source_rays(n)):
            assert mirror_step(point,8)==Q(1,8*(n+1)-c)
            n_assert+=1
        n_assert+=2
    for k in range(11):
        assert source_pole_moment(k)==4*7**k-2*4**k-3**k-2**k
        n_assert+=1
    for n in range(1,129):
        assert counterfeit_mirror_force(n)==16*counterfeit_mirror_tail(n-1)-counterfeit_mirror_tail(n)
        assert counterfeit_mirror_state(n)==16*counterfeit_mirror_state(n-1)+counterfeit_mirror_force(n)
        n_assert+=2
    roots=((1,0),(-1,0),(0,1),(0,-1))
    gaussian_words=0
    for N in range(1,6):
        for word in product(roots,repeat=N):
            for K in range(1,N+1):
                left,e,upper=exact_vdc_mixture(word,K,1)
                assert Q(0)<=e and left<=upper
                n_assert+=1
            gaussian_words+=1
    for K in range(2,65):
        w=lag_kernel(K)
        assert w[0]+2*sum(w[1:])==1
        assert w[-1]==Q(1,K*K*K)/harmonic(K)
        assert alternating_spectral_symbol_pi(K)==w[0]+2*sum(
            ((-1)**k*w[k] for k in range(1,K)),Q())
        assert last_lag_weight_ratio(K)==Q(1,K)/harmonic(K)
        assert sum((16**k*w[k] for k in range(1,K)),Q()) <= Q(32*16**K,225*K**3)/harmonic(K)
        n_assert+=5
    for N,K in ((32,3),(64,4),(128,5),(256,6),(512,7)):
        for h in (1,2,5):
            assert harmonic_exact_source_error_sum(N,K,h)<harmonic_source_error_bound(N,K,h)
            n_assert+=1
    schedules={}
    for b in (2,4,8,16,32,64,128):
        N=16**b
        K=critical_harmonic_lag_schedule(N)
        assert K>=b and 16**K<=N*b**3 and K<=N
        schedules[str(b)]=K
        n_assert+=1
    assert naive_signed_harmonic_symbol_pi(4)==Q(-1,6)
    n_assert+=1
    source_dir=Path(__file__).resolve().parents[1]
    source_names=("observational_succ/harmonic_mirror_succ.py",
                  "observational_succ/pi_harmonic_lag.py",
                  "tests/test_harmonic_mirror_succ.py",
                  "tests/test_pi_harmonic_lag.py",
                  "tests/test_harmonic_mirror_repo_integration.py",
                  "scripts/harmonic_mirror_probe.py")
    hashes={p:hashlib.sha256((source_dir/p).read_bytes()).hexdigest() for p in source_names}
    return {
        "status":"EXACT_FINITE_ONLY_NOT_PI_NORMALITY",
        "assertions":n_assert,
        "gaussian_words":gaussian_words,
        "pascal_harmonic_depth":120,
        "independent_BBP_four_ray_depth":512,
        "naive_lag_symbol_at_pi_K4":str(naive_signed_harmonic_symbol_pi(4)),
        "mirror_source_pole_moments_0_to_3":[source_pole_moment(k) for k in range(4)],
        "counterfeit_alpha":str(counterfeit_mirror_tail(0)),
        "counterfeit_polarity":"eventually_zero_base_16_orbit",
        "harmonic_diagonal_at_16":str(lag_kernel(16)[0]),
        "harmonic_diagonal_at_64":str(lag_kernel(64)[0]),
        "critical_lag_examples_b_floorlog16N":schedules,
        "conditional_fourier_saving":"UNVERIFIED",
        "actual_pi_normality":"OPEN",
        "sha256_of_executed_sources":hashes,
        "local_environment":"partial isolated code/test checkout; full SUCC suite requires hosted CI"
    }


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=report()
    txt=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(txt,encoding="utf-8")
    print(txt,end="")

if __name__=="__main__":main()
