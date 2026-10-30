"""Independent algebraic and analytic checks for selected BBP shrinking-target research.

Avoids importing the main probe. All finite arithmetic is rational; complex
integrals are diagnostic observations, never a proof of selected Weyl saving.
"""
from fractions import Fraction as Q
from math import floor, gcd, log, pi
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


def four_poles(n):
    a=8*n-7
    return Q(4,a)-Q(2,a+3)-Q(1,a+4)-Q(1,a+5)


def independent_tail(n, count=52):
    lo=Q()
    for k in range(1,count+1):lo += four_poles(n+k)/16**k
    return lo,lo+four_poles(n+count+1)/Q(15*16**count)


def independent_B(n,L,depth=52):
    tnlo,tnhi=independent_tail(n,depth)
    tllo,tlhi=independent_tail(n+L,depth)
    return (1+tllo)/Q(16**L)-tnhi,(1+tlhi)/Q(16**L)-tnlo


def direct_all_zero_threshold(n,L):
    """Independent bare-forward recursion: x_{n+j}=16^j x_n+R_j."""
    if L==0:return Q(1)
    offset=Q()
    boundaries=[]
    for j in range(1,L+1):
        offset=16*offset+four_poles(n+j)
        boundaries.append((1-offset)/Q(16**j))
    return min(boundaries)


def overlap(I,J,mult):
    """Exact Lebesgue intersection of I and preimages of J under x -> {mult*x}."""
    a,b=I;c,d=J
    lo=max(0,int(mult*a)-2)
    hi=min(mult-1,int(mult*b)+2)
    ans=Q()
    for k in range(lo,hi+1):
        u=max(a,(k+c)/mult)
        v=min(b,(k+d)/mult)
        if u<v:ans+=v-u
    return ans


def sympy_source_checks():
    n=sp.symbols('n',positive=True)
    r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
    assert sp.factor(r-15/(64*n**2)) != 0
    assert sp.factor(r-(6/((8*n-7)*(8*n-4))+4/((8*n-7)*(8*n-3))+5/((8*n-7)*(8*n-2))))==0
    a=sp.symbols('a',positive=True)
    R=4/a-2/(a+3)-1/(a+4)-1/(a+5)
    assert sp.factor(R)==(15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))
    # Exact leading source coefficient: 15/64.
    assert sp.limit(n**2*r,n,sp.oo)==sp.Rational(15,64)
    assert sp.limit(n**3*(r-sp.Rational(15,64)/n**2),n,sp.oo).is_rational
    return {'r_n2_limit':'15/64','r_n3_first_jet':str(sp.limit(n**3*(r-sp.Rational(15,64)/n**2),n,sp.oo))}


def run():
    report={'sympy':sympy_source_checks(), 'zero_word':[], 'pair_mix':[], 'signed_current':[], 'phase_pi':[]}
    mp.mp.dps=85
    for n in (4,16,32,64,256,1024):
        L=0
        while 16**(L+1)<=n*n:L+=1
        lo,hi=independent_B(n,L)
        direct=direct_all_zero_threshold(n,L)
        assert lo<direct<hi if L else direct==lo==hi
        assert lo>four_poles(n)
        assert hi<Q(1,16**L) if L else hi==1
        ratio=(lo+hi)/2/four_poles(n)
        theta=Q(n*n,16**L)
        guess=(64*theta-1)/15
        report['zero_word'].append({'n':n,'L':L,'conditional_event_given_zeros':float(1/ratio),'asymptotic_guess':float(1/guess)})
    # Haar two-event correlations are fixed by circle interval arithmetic,
    # independently of whether the actual pi seed has either event.
    for n,gap in ((16,1),(16,2),(32,2),(64,3),(64,5)):
        tlo,thi=independent_tail(n)
        m=n+gap
        ulo,uhi=independent_tail(m)
        I=((tlo+thi)/2,(tlo+thi)/2+four_poles(n))
        J=((ulo+uhi)/2,(ulo+uhi)/2+four_poles(m))
        q=16**gap
        joint=overlap(I,J,q)
        independent=four_poles(n)*four_poles(m)
        assert abs(joint-independent)<=Q(2)*four_poles(m)/q
        if gap <= int(log(n*n,16)+1e-10):
            # Using separately truncated Green-midpoints destroys the exact
            # shift identity by at most the enclosing tail interval errors.
            assert joint <= 4*((thi-tlo)+(uhi-ulo))
        report['pair_mix'].append({'n':n,'gap':gap,'joint':float(joint),'product':float(independent)})
    # Signed current: each underlying d-branch contributes the same
    # complex uniform interval integral. Check direct independent quadrature.
    for n in (3,16,64):
        r=mp.mpf(four_poles(n).numerator)/four_poles(n).denominator
        for h in (1,3,-2):
            J=mp.quad(lambda x:mp.exp(2j*mp.pi*h*x),[0,r])/16
            closed=(mp.exp(2j*mp.pi*h*r)-1)/(32j*mp.pi*h)
            assert abs(J-closed)<mp.mpf('1e-74')
            report['signed_current'].append({'n':n,'h':h,'real':float(mp.re(J)),'imag':float(mp.im(J))})
    # Independent 100-digit pi oracle for actual zero seed and coherent seed.
    mp.mp.dps=160
    from fractions import Fraction
    phase=Fraction(0)
    for n in range(1,65):
        phase=(16*phase+four_poles(n))%1
        if n>=2:
            x=mp.mpf(phase.numerator)/phase.denominator
            tlo,thi=independent_tail(n,60)
            tail=mp.mpf((tlo+thi).numerator)/((tlo+thi).denominator*2)
            y=mp.frac(mp.power(16,n-1)*mp.pi)
            assert abs(mp.mpf(mp.frac(x+tail))-y)<mp.mpf('1e-60')
            if n in (2,4,8,16,32,64):
                d=int(16*(phase-four_poles(n))%1) if False else None
                report['phase_pi'].append({'n':n,'pure_phase':mp.nstr(y,14),'circle_state':mp.nstr(x,14)})
    result=Path('/mnt/data/succ_kepler_selected_phase/independent_oracle_receipt.json')
    result.write_text(json.dumps(report,indent=2)+'\n')
    print('Independent oracle PASS',len(report['zero_word']),'word checks,',len(report['pair_mix']),'pair overlap checks,',len(report['signed_current']),'signed current complex checks')
    print('Receipt:',result)

if __name__=='__main__':run()
