"""Independent arithmetic/polynomial oracle; no import of the principal module."""
from fractions import Fraction as F
import math
import cmath


def r_poly(n):
    n=F(n)
    return (120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def r_fake(n):
    return F(15,(8*n-7)**2)


def fan_integral_float(n,z):
    """Independent genuine positive integral, not the binomial/pole formula."""
    from scipy.integrate import quad
    a=8*n-7
    def q(x):
        return -2*math.expm1(-3*x)-math.expm1(-4*x)-math.expm1(-5*x)
    def integrand(x):
        f=math.exp(-8*x)
        return math.exp(-a*x)*q(x)*(f+(1-f)*z)**n
    return quad(integrand,0,math.inf,epsabs=1e-12,epsrel=1e-12)[0]/(47/15)


def fan_pole_float(n,z):
    return float(sum(F(math.comb(n,k))*F(z)**(n-k)*(1-F(z))**k*r_poly(n+k)
                     for k in range(n+1))/F(47,15))


def time_cusp_oracle(t,N):
    """Truncated Fourier cusp with a rigorously bounded O(1/N) series tail."""
    # Difference can be computed without complex Lerch or divergent single-pole pieces.
    total=0j
    for n in range(1,N+1):
        total+=float(r_poly(n)/F(47,15))*cmath.expm1(1j*(n-1)*t) if hasattr(cmath,'expm1') else float(r_poly(n)/F(47,15))*(cmath.exp(1j*(n-1)*t)-1)
    return total


def run():
    assert r_poly(1)==F(47,15)
    for n in range(1,100):
        a=8*n-7
        r4=F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)
        assert r4==r_poly(n)
    for n in (1000,10000,100000):
        h=1-r_poly(n+1)/r_poly(n)
        hf=1-r_fake(n+1)/r_fake(n)
        assert abs(float(n*n*(h-F(2,n)))-float(-F(209,120))) < 3/n
        assert abs(float(n*n*(hf-F(2,n)))-float(-F(5,4))) < 3/n
        assert abs(float(n*n*(h-hf))-float(-F(59,120))) < 3/n
    for n in (2,4,8):
        for z in (-1,0,F(1,2),1):
            assert abs(fan_pole_float(n,z)-fan_integral_float(n,float(z)))<1e-10,(n,z)
    # Independent mixed time x grade coefficient checks from the positive integral.
    c=225/3008
    for n in (40,80,160):
        for z in (-1,0.5,1):
            actual=n*n*fan_integral_float(n,z)
            predicted=c/(2-z)**2
            assert abs(actual-predicted)<0.003,(n,z,actual,predicted)
    # The n-dependent grade Fourier coefficient tends to C/(2-z)^2
    # and the inherited O(1/n) TV bound upgrades it to the time cusp.
    # Fourier cusp: partial sums are absolutely convergent; tail of
    # (e^{int}-1) weighted by p_n is at most ~ 2C/N.
    t=0.02
    N=40000
    d=time_cusp_oracle(t,N)
    ratio=d.imag/(t*math.log(1/t))
    c=225/3008
    assert abs(ratio-c)<0.005,(ratio,c)
    return {'source_identity':'PASS (99 independent polynomial cases)',
            'hazard_original_n2':'-209/120',
            'hazard_fake_n2':'-5/4',
            'hazard_defect_n2':'-59/120',
            'integral_holdouts':'12/12','independent_mixed_coefficient_checks':'9/9',
            'cusp_ratio':ratio,'expected_cusp':c,'status':'PASS'}

if __name__=='__main__':
    print(run())
