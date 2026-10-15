"""Independent 45-digit direct Suzuki g_J integration, NOT a proof certificate.

No zero locations, no scipy eigenvalue authority. Source is original Suzuki
(1.3): real pole, true prime-2 hinge, digamma/contact and J Gamma rungs.
Compare against independent rational Legendre/OU/hinge algebra.
"""
from pathlib import Path
import sys, json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_legendre_source import (
    source_ou_pair_affine, prime_hinge_integral_polynomial,
    poly_eval,poly_two_variable_cross,
)
from observational_succ.suzuki_moment_schur import low_inverse_neumann
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=55

def m(q):
    return mp.mpf(q.numerator)/q.denominator if isinstance(q,F) else mp.mpf(q)

a=F(1,2)
am=m(a)
b=mp.log(2)
Cg=mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)


def original_kernel(t,J):
    g=-4*(mp.exp(t/2)+mp.exp(-t/2)-2)
    if t>b:g+=b/mp.sqrt(2)*(t-b)
    g+=Cg*t/2
    for j in range(J):
        d=4*j+1
        g+=-4/mp.mpf(d*d)*(1-mp.exp(-mp.mpf(d)*t/2))
    return g


def source_direct_pair(i,j,J):
    rho=poly_two_variable_cross(i,j,a)
    def f(t):return original_kernel(t,J)*sum(m(v)*t**k for k,v in enumerate(rho))
    return mp.quad(f,[0,b,1])


def source_analytic_pair(i,j,J):
    K=low_inverse_neumann(a,max(i,j))[i-1][j-1]
    val=-Cg*m(K)
    poly=prime_hinge_integral_polynomial(i,j,a)
    val+=(b/mp.sqrt(2))*sum(m(v)*b**k for k,v in enumerate(poly))
    for t in range(J):
        d=4*t+1; alpha=F(d,2)
        A,B=source_ou_pair_affine(i,j,a,alpha)
        val+=mp.mpf(4)/d**2*(m(A)+m(B)*mp.exp(-d/2))
    # pole factor: ∫∫ -4(e^(|x-y|/2)+e^(-|x-y|/2)-2)ρ(t)dt
    rho=poly_two_variable_cross(i,j,a)
    val+=mp.quad(lambda t:-4*(mp.exp(t/2)+mp.exp(-t/2)-2)*sum(m(v)*t**k for k,v in enumerate(rho)),[0,1])
    return val


def run():
    rows=[]
    for J in (1,2,3):
        for i,j in ((1,1),(1,2),(1,3),(2,2),(2,4),(3,3)):
            x=source_direct_pair(i,j,J)
            y=source_analytic_pair(i,j,J)
            err=abs(x-y)
            assert err<mp.mpf('1e-37'), (i,j,J,err)
            rows.append({'J':J,'pair':[i,j], 'original_source_integral':mp.nstr(x,30),
                         'legendre_source_decomposition':mp.nstr(y,30),
                         'abs_error':mp.nstr(err,5)})
    return {'source':'ORIGINAL_SUZUKI_2026_EQ1_3_NO_ZEROS',
            'type':'NUMERICAL_DIAGNOSTIC_NOT_SIGN_PROOF',
            'precision_digits':55,'tolerance':'1e-37','window':'1/2',
            'rows':rows,'RH_proved':False}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
