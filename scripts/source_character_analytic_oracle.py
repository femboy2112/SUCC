"""Independent high-precision χ4 parity/conductor theta oracle; NOT proof authority."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import mpmath as mp
from fractions import Fraction as Q
from observational_succ.source_character_interaction import (
    character_four, signed_theta_tail,
)

mp.mp.dps=60
CHI=[0,1,0,-1]
N=15
T=26


def theta(t,limit=N):
    return 2*mp.fsum(n*character_four(n)*mp.exp(-mp.pi*n*n*t/4)
                     for n in range(1,limit+1))


def completed_integral(s):
    f=lambda t:theta(t)*(t**((s-1)/2)+t**(-s/2))/2
    return mp.quad(f,[1,2,4,8,16,T])


def reference(s):
    if mp.re(s)<0:
        return reference(1-s)
    return mp.power(4/mp.pi,(s+1)/2)*mp.gamma((s+1)/2)*mp.dirichlet(s,CHI)


def mpq(q):return mp.mpf(q.numerator)/q.denominator


def run():
    b=mpq(Q(signed_theta_tail(-3,4,N,T)['rational_upper']))
    theta_cases=[]
    for t in [mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf(2),mp.mpf(5)]:
        lhs=theta(t,120)
        rhs=t**(-mp.mpf('1.5'))*theta(1/t,120)
        err=abs(lhs-rhs)
        assert err<mp.mpf('1e-40'),(t,err)
        theta_cases.append({'t':mp.nstr(t,8),'relative_modular_error':mp.nstr(err,12)})
    test=[('Euler 2',mp.mpf(2)),('Euler 3',mp.mpf(3)),
          ('critical half',mp.mpf('0.5')),
          ('outside Euler negative one',mp.mpf(-1)),
          ('outside Euler negative three',mp.mpf(-3)),
          ('critical imaginary 7',mp.mpf('0.5')+7j),
          ('noncentral complex',mp.mpf('0.82')+3j)]
    cases=[]
    for label,s in test:
        z=completed_integral(s)
        exact=reference(s)
        err=abs(z-exact)
        assert err<b+mp.mpf('1e-45'),(label,err,b)
        cases.append({'label':label,'s':mp.nstr(s,16),
                      'theta_completed':mp.nstr(z,34),
                      'reference_completed':mp.nstr(exact,34),
                      'error':mp.nstr(err,14),
                      'rigorous_omitted_tail_upper_only':mp.nstr(b,14)})
    G=mp.dirichlet(2,CHI)
    der=mp.diff(lambda s:mp.dirichlet(s,CHI),-1)
    assert abs(der-2*G/mp.pi)<mp.mpf('1e-50')
    assert abs(2*mp.pi*der-4*G)<mp.mpf('1e-50')
    return {'status':'INDEPENDENT_NUMERICAL_ORACLE_CLASSICAL_CHI4',
            'precision':60,'theta_modular':theta_cases,'analytic_mellin':cases,
            'prime_source':'primitive odd Dirichlet chi4, genuine Euler, conductor4',
            'tail_envelope_is_rational_but_finite_quadrature_not_certified':True,
            'Catalan_beta_2':mp.nstr(G,40),
            'beta_prime_minus_one':mp.nstr(der,40),
            'chiral_origin_equals_2pi_beta_prime':True,
            'RH_proved':False,'GRH_proved':False,'nontrivial_zero_inputs':False}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    out=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(out)
    else:print(out,end='')

if __name__=='__main__':main()
