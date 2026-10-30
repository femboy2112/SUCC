"""Independent high-precision quadrature holdouts; not proof certificates.

Requires mpmath (the stdlib exact tests do not). The original four-pole
polynomial and the reduced order-statistic source are evaluated separately.
"""
from __future__ import annotations
import mpmath as mp


def main():
    mp.mp.dps=65
    lam=(mp.sqrt(5)-1)/2
    omega=lam-mp.euler
    golden_first=6*lam-mp.mpf(19)/2
    mutation_second=5+6*lam**3

    def original(x):
        return (4-2*x**3-x**4-x**5)/(16-x**8)

    def reduced(x):
        return (1-x)/((2-x*x)*(x*x-2*x+2))

    # Independent pi/16 integral and source-form comparison on holdouts.
    t0=mp.quad(original,[0,mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1])
    assert abs(16*t0-mp.pi)<mp.mpf('1e-52')
    for x in [mp.mpf(k)/97 for k in range(98)]:
        assert abs(original(x)-reduced(x))<mp.mpf('1e-58')
    print('INDEPENDENT_FOUR_POLE_PI_INTEGRAL',mp.nstr(16*t0,35))
    print('OILY_CONSTANT',mp.nstr(omega,35))
    print('FIRST_CORRECTION',mp.nstr(golden_first,35))
    print('MUTATION_SECOND_COEFFICIENT',mp.nstr(mutation_second,35))

    def expectation(a, eps=0):
        a=mp.mpf(a)
        eps=mp.mpf(eps)
        def base(y):
            if y==0:
                return mp.mpf(0)
            x=1-y/a
            t=y/a
            return y*(1-y/a)**a/((2-x*x)*(x*x-2*x+2))*(1-eps*t*t)
        points=[0,1,4,12,a/2,a]
        points=sorted(set(p for p in points if 0<=p<=a))
        den=mp.quad(base,points)
        num=mp.quad(lambda y:base(y)*(mp.log(y)-mp.exp(-lam*y)),points)
        return num/den,den/(a*a)

    exact_r=lambda k:mp.mpf(4)/(8*k-7)-mp.mpf(2)/(8*k-4)-mp.mpf(1)/(8*k-3)-mp.mpf(1)/(8*k-2)
    tail=t0
    for n in range(1,7):
        tail=16*tail-exact_r(n)
        _,via_integral=expectation(8*n)
        assert abs(tail-via_integral)<mp.mpf('1e-48')
    print('TAIL_RECURRENCE_6_TERMS_PASS')

    values={}
    for n in [2,4,8,16,32,64]:
        a=8*n
        F,T=expectation(a)
        values[n]=F
        print('SOURCE_HOLDOUT n=%d a=%d F=%s a(F-Omega)=%s' %
              (n,a,mp.nstr(F,22),mp.nstr(a*(F-omega),17)))
    assert abs(512*(values[64]-omega)-golden_first)<mp.mpf('0.07')
    for n in [8,16,32,64]:
        a=8*n
        eps=mp.mpf('.5')
        F0=values[n]
        Fe,_=expectation(a,eps)
        scaled=a*a*(Fe-F0)
        print('MUTANT_HOLDOUT n=%d a2delta=%s predicted=%s' %
              (n,mp.nstr(scaled,20),mp.nstr(-eps*mutation_second,20)))
    print('NUMERICAL_HOLDOUT_PASS (high precision, not formal certification)')


if __name__=='__main__':
    main()
