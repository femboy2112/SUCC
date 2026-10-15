"""Independent 65-digit theta/xi/prime-current calibration; NOT proof authority.

The companion stdlib-only analytic_theta_tail gives a rigorous bound for the
omitted theta modes and time range, but this oracle's finite quadrature is
NOT interval certified. It does not scan nontrivial zero locations.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

import mpmath as mp
from fractions import Fraction as Q
from observational_succ.source_model_interaction import (
    analytic_theta_tail, xi_tail_envelopes, smooth_prime_theta_obstruction)

mp.mp.dps=65
N=4
T=16

def mpq(q:Q):
    return mp.mpf(q.numerator)/q.denominator


def finite_J(s,r=0):
    def integrand(t):
        psi=mp.fsum(mp.exp(-mp.pi*n*n*t) for n in range(1,N+1))
        u=t**(s/2-1)
        v=t**((1-s)/2-1)
        if r==0:
            return psi*(u+v)
        if r==1:
            return psi*mp.log(t)*(u-v)/2
        if r==2:
            return psi*mp.log(t)**2*(u+v)/4
        raise ValueError('r in {0,1,2}')
    return mp.quad(integrand,[1,2,4,8,T])


def xi_approx(s):
    J0=finite_J(s)
    J1=finite_J(s,1)
    return mp.mpf('0.5') + s*(s-1)*J0/2, (s-mp.mpf('0.5'))*J0 + s*(s-1)*J1/2


def xi_external(s):
    # Use the reflection for negative Re only to avoid cancellation at trivial zeros.
    if mp.re(s)<0:
        return xi_external(1-s)
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)/2


def xi_prime_external(s):
    if mp.re(s)<0:
        return -mp.diff(xi_external,1-s)
    return mp.diff(xi_external,s)


def theta_smooth(P, t, upper=300000):
    nums={1}
    for p in P:
        accum=set()
        for a in nums:
            x=a
            while x <= upper:
                accum.add(x)
                x*=p
        nums=accum
    return 1+2*mp.fsum(mp.exp(-mp.pi*t*n*n) for n in nums)


def run():
    box=xi_tail_envelopes(-2,3,10,N,T)
    e_xi=mpq(Q(box['xi_error_upper']))
    e_der=mpq(Q(box['xi_prime_error_upper']))
    cases=[('critical midpoint',mp.mpf('0.5')),
           ('Euler overlap 2',mp.mpf(2)),
           ('Euler overlap 3',mp.mpf(3)),
           ('trivial-zero completion -2',mp.mpf(-2)),
           ('critical line imaginary 7',mp.mpf('0.5')+7j),
           ('inside strip complex',mp.mpf('0.73')+4j),
           ('outside Euler real strip',mp.mpf('-1.25')+2j)]
    out=[]
    for label,s in cases:
        val,der=xi_approx(s)
        ref=xi_external(s)
        ref_der=xi_prime_external(s)
        err=abs(val-ref)
        err_d=abs(der-ref_der)
        assert err < e_xi + mp.mpf('1e-51'), (label,'xi tail disagreement',err,e_xi)
        assert err_d < e_der + mp.mpf('1e-51'), (label,'xi derivative tail disagreement',err_d,e_der)
        datum={'label':label,'s':mp.nstr(s,30),
               'xi_theta_approx':mp.nstr(val,35),'xi_reference':mp.nstr(ref,35),
               'xi_abs_error':mp.nstr(err,15),
               'xi_prime_abs_error':mp.nstr(err_d,15),
               'xi_rigorous_omitted_tail_bound':mp.nstr(e_xi,15),
               'xi_prime_rigorous_omitted_tail_bound':mp.nstr(e_der,15)}
        if s not in (mp.mpf(-2),) and s!=1:
            continued=-(der/val)+1/s+1/(s-1)+(mp.digamma(s/2)-mp.log(mp.pi))/2
            reference=-mp.diff(mp.zeta,s)/mp.zeta(s)
            difference=abs(continued-reference)
            assert difference< mp.mpf('1e-15'),(label,'meromorphic source mismatch',difference)
            datum['continued_prime_current']=mp.nstr(continued,35)
            datum['prime_current_error_vs_independent_zeta']=mp.nstr(difference,12)
        out.append(datum)
    contact=mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)
    logarithmic=2*mp.diff(mp.zeta,mp.mpf('0.5'))/mp.zeta(mp.mpf('0.5'))
    assert abs(contact-logarithmic)<mp.mpf('1e-54')
    P=(2,3,5)
    h=12
    t=mp.mpf(4)**(-h)
    actual=theta_smooth(P,t,2**(h+5))
    upper=mpq(Q(smooth_prime_theta_obstruction(P,h)['theta_P_near_zero_upper']))
    assert actual <=upper
    return {'status':'INDEPENDENT_NUMERICAL_ORACLE_NOT_INTERVAL_QUADRATURE',
            'numeric_precision_digits':65,'source':'integer lattice Gaussian; all-prime Euler in Re>1; no zeros',
            'N':N,'T':T,
            'xi_error_uniform_on_declared_strip_with_abs_s_at_most_10':mp.nstr(e_xi,20),
            'xi_derivative_error_same':mp.nstr(e_der,20),
            'cases':out,
            'critical_contact_C':mp.nstr(contact,45),
            'critical_contact_difference':mp.nstr(abs(contact-logarithmic),12),
            'finite_P_theta_tiny_t_check':{'primes':list(P),'h':h,
                                         'source_cutoff':2**(h+5),
                                         'normalized_actual':mp.nstr(actual/2**h,20),
                                         'normalized_rational_upper':mp.nstr(upper/2**h,20)},
            'completed_Weil_positive':False,'RH_proved':False,
            'nontrivial_zero_locations_input':False}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    result=run()
    out=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(out)
    else:
        print(out,end='')

if __name__=='__main__':
    main()
