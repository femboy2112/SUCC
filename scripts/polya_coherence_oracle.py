#!/usr/bin/env python3
"""Independent exact radical oracle for the source-marked coherent lift.

Standard native tests use rational Gram identities. This script instead
constructs actual radical amplitudes and verifies V.H*V and V*sqrt(mu).
SymPy is an oracle dependency, never an imported theorem or Lean axiom.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import sympy as s
from fractions import Fraction as F
from observational_succ.oily_prime_growth_compiler import (
    conditional_split, unique_local_birth_probability,
)


def q(value):
    return s.Rational(value.numerator, value.denominator)


def assert_zero(matrix):
    assert all(s.simplify(entry) == 0 for entry in matrix)


def nearest_neighbor_lift(mu, rates):
    """Build the actual row-environment amplitudes without the new implementation."""
    m = len(mu)
    nu = [s.Integer(0)] * (m+1)
    for k in range(m):
        nu[k] += mu[k]*(1-rates[k])
        nu[k+1] += mu[k]*rates[k]
    v = s.zeros(2*(m+1),m)
    for ell in range(m+1):
        x = mu[ell]*(1-rates[ell]) if ell<m else s.Integer(0)
        y = mu[ell-1]*rates[ell-1] if ell>0 else s.Integer(0)
        if ell<m:
            v[2*ell,ell] = x/s.sqrt(mu[ell]*nu[ell])
            v[2*ell+1,ell] = s.sqrt(x*y/(mu[ell]*nu[ell]))
        if ell>0:
            v[2*ell,ell-1] = y/s.sqrt(mu[ell-1]*nu[ell])
            v[2*ell+1,ell-1] = -s.sqrt(x*y/(mu[ell-1]*nu[ell]))
    return v,nu


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=pathlib.Path)
    args=parser.parse_args()
    checks=[]
    for x in (F(1,3),F(2,3),F(1)):
        for grade in range(6):
            mu=[q(conditional_split(x,grade,k)) for k in range(grade+1)]
            rates=[q(unique_local_birth_probability(x,grade,k)) for k in range(grade+1)]
            v,nu=nearest_neighbor_lift(mu,rates)
            assert_zero(v.H*v-s.eye(grade+1))
            marked=s.Matrix([s.sqrt(z) for z in mu])
            target=s.Matrix([item for z in nu for item in (s.sqrt(z),0)])
            assert_zero(v*marked-target)
            for ell,z in enumerate(nu):
                assert z==q(conditional_split(x,grade+1,ell))
            checks.append({'x':str(x),'grade':grade,'actual_radical_isometry':True,
                           'marked_source_transfer':True})
    spectra=[]
    for m in range(1,11):
        # Direct radical construction; characteristic polynomial, not a
        # shared Hahn-eigenvector implementation, supplies the second bearing.
        mu=[s.Rational(1,m)]*m
        rates=[s.Rational(k+1,m+1) for k in range(m)]
        v,_=nearest_neighbor_lift(mu,rates)
        k1=v.extract(list(range(1,2*(m+1),2)),list(range(m)))
        t=s.Symbol('t')
        actual=(k1.H*k1).charpoly(t).as_expr()
        expected=s.prod(t-s.Rational(r*(r+1),m*(m+1)) for r in range(m))
        assert s.expand(actual-expected)==0
        spectra.append({'dimension':m,'characteristic_polynomial_coefficients':
                        [str(c) for c in s.Poly(actual,t).all_coeffs()]})
    # The m=2 phase-flipped vector has nonzero source-ancilla
    # leakage, even though its input populations equal the marked source.
    v,_=nearest_neighbor_lift([s.Rational(1,2)]*2,[s.Rational(1,3),s.Rational(2,3)])
    phase=s.Matrix([1,-1])/s.sqrt(2)
    k0=v.extract([0,2,4],[0,1]); k1=v.extract([1,3,5],[0,1])
    u,z=k0*phase,k1*phase
    rho=u*u.H+z*z.H
    leakage=s.simplify((z.H*z)[0])
    purity=s.simplify(s.trace(rho*rho))
    assert leakage==s.Rational(1,3) and purity==s.Rational(5,9)
    source_paths=['observational_succ/oily_prime_growth_compiler.py',
                  'observational_succ/polya_coherent_observer.py','formal/PolyaCoherence.lean']
    result={'schema':'SUCC-polya-coherence-exact-oracle-v1',
            'authority':'EXACT FINITE SYMBOLIC CHECK; full proofs in dossier',
            'source_cases':checks,'spectra':spectra,
            'phase_flipped_m2':{'leakage':str(leakage),'reduced_purity':str(purity)},
            'sha256':{path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in source_paths}}
    output=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.write_text(output)
    else:
        print(output,end='')


if __name__=='__main__':
    main()
