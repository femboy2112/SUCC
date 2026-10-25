#!/usr/bin/env python3
"""Independent symbolic/rational checks of the dyadic source proof identities.

The all-input analytic theorem is proved in PI_DYADIC_SOURCE_ISOMETRY.md;
this finite oracle cannot replace its convergence or analytic-domain argument.
It deliberately does not import the production dyadic-source implementation.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.prime_base_carry import CoverPoint, transport_cover


def original_r(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def valuation2(integer):
    integer=abs(integer)
    if integer==0:
        raise ValueError('zero valuation is infinite')
    return (integer & -integer).bit_length()-1


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    x,y=sp.symbols('x y')
    numerator=120*x*x-89*x+16
    denominator=(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
    forcing=4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)
    quadratic=1-2*x+2*x*x
    mobius=(1-x)/(1-2*x)
    generating=(-4*x**6+2*x**3+x*x+x)/(1-16*x**8)
    factored=x*(1-x)/((1-2*x*x)*quadratic)
    primitive_derivative=sp.diff(-sp.log(1-2*x*x)/8+sp.log(quadratic)/8,x)+1/(4*quadratic)
    identities={
        'original_forcing_collapses':forcing-numerator/denominator,
        'generating_integrand_factorization':generating-factored,
        'mobius_derivative':sp.diff(mobius,x)-1/(1-2*x)**2,
        'mobius_quadratic_transport':quadratic.subs(x,mobius)-quadratic/(1-2*x)**2,
        'primitive_derivative':primitive_derivative-factored,
    }
    results={name:sp.cancel(value)==0 for name,value in identities.items()}
    assert all(results.values())
    quotient=sp.cancel((numerator*denominator.subs(x,y)-numerator.subs(x,y)*denominator)/(x-y))
    unit_quotient=sp.Poly(quotient,x,y,modulus=2).as_expr()==1
    assert unit_quotient
    zero_checks=[]
    for bits in (257,511,1024):
        modulus=1<<bits
        residue=0
        mutated=0
        for j in range((bits+3)//4):
            value=original_r(-j)
            assert value.denominator%2==1
            residue=(residue+(1<<(4*j))*value.numerator*pow(value.denominator,-1,modulus))%modulus
            bad=value+Q(2,-8*j-3)  # flip the third original source coefficient
            mutated=(mutated+(1<<(4*j))*bad.numerator*pow(bad.denominator,-1,modulus))%modulus
        assert residue==0 and mutated!=0
        zero_checks.append(dict(bits=bits,exact_residue=residue,sign_mutation_rejected=True))
    unwrapped=[Q(0)]
    for n in range(1,513):
        value=16*unwrapped[-1]+original_r(n)
        assert value.denominator%2==1
        assert valuation2(value.numerator)==valuation2(n)
        unwrapped.append(value)
    pairs=0
    for s in (0,1,2,7,16,31,64,127,128,255,256,511):
        for t in (3,11,32,65,129,257,512):
            if s==t:
                continue
            diff=unwrapped[s]-unwrapped[t]
            assert diff.denominator%2==1
            assert valuation2(diff.numerator)==valuation2(s-t)
            pairs+=1
    # Connect the abstract common cover to the actual rational source,
    # retaining its real fractional state AND cumulative integer carry.
    def lift(value,modulus):
        carry=value.__floor__()
        return CoverPoint(value-carry,carry%modulus,modulus)
    source_cover_checks=0
    for n in (1,2,3,7,16,31,64,127,128,255,256,511,512):
        for modulus in (2,4,16,9,27,11,13,720):
            point=lift(unwrapped[n],modulus)
            assert point.circle_point==(unwrapped[n]/modulus)%1
            previous=lift(unwrapped[n-1],modulus)
            raw=16*previous.root+original_r(n)
            carry=raw.__floor__()
            assert CoverPoint(raw-carry,(16*previous.label+carry)%modulus,modulus)==point
            for q in (2,3,5,7,11,13,16):
                assert transport_cover(point,q)==lift(q*unwrapped[n],modulus)
                source_cover_checks+=1
    # Independent canonical primary-fraction decomposition of authentic U_3.
    value=unwrapped[3]
    assert value==Q(615863723,765765)
    primary={}
    for prime,exponent in sp.factorint(value.denominator).items():
        power=int(prime**exponent)
        residue=value.numerator*pow(value.denominator//power,-1,power)%power
        primary[int(prime)]=Q(residue,power)
    assert (sum(primary.values(),Q(0))-value)%1==0
    small=sum((part for prime,part in primary.items() if prime<16),Q(0))%1
    assert small==Q(499,45045)
    assert (value-small)%1==primary[17]==Q(4,17)
    primary_witness=dict(index=3,unwrapped=str(value),real_phase=str(value%1),
        small_prime_phase=str(small),omitted_17_phase=str(primary[17]),
        all_components={str(p):str(v) for p,v in primary.items()})
    paths=['scripts/pi_dyadic_analytic_oracle.py','observational_succ/prime_base_carry.py',
           'research/2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md']
    result=dict(status='VERIFIED_FINITE',analytic_infinite_authority='paper proof, not these checks',
        symbolic_identities=results,forcing_difference_quotient_mod2_is_one=bool(unit_quotient),
        reversed_zero_checks=zero_checks,exact_source_indices_checked=512,
        exact_pair_valuation_checks=pairs,authentic_source_cover_checks=source_cover_checks,
        authentic_first_17_birth=primary_witness,
        pi_normality='OPEN',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=result['status'],source_indices=512,pair_checks=pairs,
                         symbolic_identities=len(results),pi_normality='OPEN')))


if __name__=='__main__':
    main()
