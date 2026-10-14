"""Optional independent numerical checks; mpmath is NOT proof authority.

Compare original Weil functional, reconstructed Gamma jump energy, direct
Carleman/Laplace integrals and Fourier Gamma spectrum. No nontrivial-zero inputs.
Run from repo root; optional mpmath dependency is used only in this script.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import mpmath as mp
from observational_succ.suzuki_markov_gluing import rate_affine_pi, derivative_tail_bound
mp.mp.dps = 55
TOL = mp.mpf('1e-32')


def rational(q):
    return mp.mpf(q.numerator)/q.denominator


def original_and_glued(a, j):
    w = j*mp.pi/(2*a)
    L = 2*a
    def corr(t):
        return ((L-t)*mp.cos(w*t)+mp.sin(w*t)/w)/2
    def original_gamma(t):
        if abs(t)<mp.mpf('1e-20'):
            return a/2 + (a/8-a*w*w/2)*t
        return (corr(t)*mp.exp(t/2)-a)/mp.sinh(t)
    def levy(t):
        if abs(t)<mp.mpf('1e-20'):
            return a*w*w*t/2
        return 2*mp.exp(-t/2)*(a-corr(t))/(-mp.expm1(-2*t))
    pole = 4*mp.quad(lambda t:corr(t)*mp.cosh(t/2), [0,L])
    prime = -2*mp.log(2)/mp.sqrt(2)*corr(mp.log(2)) if L>mp.log(2) else mp.mpf(0)
    original = pole+prime-(mp.log(4*mp.pi)+mp.euler)*a-mp.quad(original_gamma,[0,L])+2*a*mp.atanh(mp.exp(-L))
    gamma_energy = mp.quad(levy,[0,L])+2*a*(mp.atanh(mp.exp(-a))+mp.atan(mp.exp(-a)))
    C = mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)
    reconstructed = gamma_energy-C*a+pole+prime
    chiral = mp.pi*a-mp.quad(lambda t:corr(t)/mp.cosh(t/2),[0,L])
    err = abs(original-reconstructed)
    assert err<TOL, ('Weil reconstruction', a,j,err)
    assert abs(prime)<=chiral/5+TOL
    assert chiral+prime>=2*a-TOL
    tails=[]
    for K in (2,8,24):
        prefix=mp.mpf(0)
        for k in range(K):
            aa, bb = rate_affine_pi(k)
            rate = rational(aa)+bb*mp.pi
            prefix += rate*a-mp.quad(lambda t,k=k:mp.exp(-k*t)*corr(t)/mp.cosh(t/2),[0,L])
        tail=gamma_energy-prefix
        bound=rational(derivative_tail_bound(K))*w*w*a
        assert -TOL<=tail<=bound+TOL
        tails.append({'K':K,'positive_tail':mp.nstr(tail,20),'H1_upper':mp.nstr(bound,20)})
    return {'a':mp.nstr(a,20),'j':j,'original_Weil_Rayleigh':mp.nstr(original/a,25),
            'source_reconstruction_error':mp.nstr(err,8),'abs_prime_over_E0':mp.nstr(abs(prime)/chiral,20),
            'single_layer_substitution_Rayleigh':mp.nstr((chiral-C*a+pole+prime)/a,20),
            'H1_tail_checks':tails}


def run():
    # A prior analytic claim, not a fitted tolerance: exact identities should agree.
    target=mp.pi/2-1
    carleman=mp.pi*mp.quad(lambda r:mp.exp(-2*r),[0,mp.inf])-mp.quad(lambda t:1/(1+t)**2,[0,mp.inf])
    spectral=mp.quad(lambda x:mp.pi*(1-mp.sech(mp.pi*x))*abs(mp.gamma(mp.mpf('0.5')+1j*x))**2,[0,mp.inf])/mp.pi
    assert abs(carleman-target)<TOL and abs(spectral-target)<TOL
    rates=[]
    for k in (0,1,2,7,20):
        aa,bb=rate_affine_pi(k)
        direct=mp.quad(lambda t:mp.exp(-k*t)/mp.cosh(t/2),[0,mp.inf])
        err=abs(direct-rational(aa)-bb*mp.pi)
        assert err<TOL
        rates.append({'layer':k,'error':mp.nstr(err,8)})
    rows=[original_and_glued(a,j) for a in (mp.mpf(1)/4,mp.log(2)/2,3*mp.log(2)/5,mp.mpf('0.54')) for j in (1,2,5)]
    return {'status':'NUMERICAL_CROSS_CHECK_NOT_PROOF','precision_digits':55,'declared_identity_tolerance':'1e-32',
            'Carleman_Laplace_error':mp.nstr(abs(carleman-target),8),'Carleman_Gamma_Fourier_error':mp.nstr(abs(spectral-target),8),
            'rate_checks':rates,'source_cases':rows,'RH_proved':False,'nontrivial_zero_inputs':False,
            'source_family':'Suzuki arXiv:2606.09096v3 explicit formula, no zero-side evaluation'}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
