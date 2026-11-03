"""Exact Q(i) Gamma tangent-field corrector for original BBP positive Mellin source.

This is an auxiliary positive Mellin probability model, NOT the selected
chronological Fourier/Weyl distribution of pi. Results are rational-algebraic
for finite q and rational Fourier frequency omega; limits use classical Gamma.
"""
from dataclasses import dataclass
from fractions import Fraction as F


@dataclass(frozen=True)
class GQ:
    re: F
    im: F=F(0)

    def __post_init__(self):
        object.__setattr__(self,'re',F(self.re))
        object.__setattr__(self,'im',F(self.im))

    def __add__(self,other):
        if not isinstance(other,GQ):return NotImplemented
        return GQ(self.re+other.re,self.im+other.im)

    def __sub__(self,other):
        return self+(-other)

    def __neg__(self):return GQ(-self.re,-self.im)

    def __mul__(self,other):
        if not isinstance(other,GQ):return NotImplemented
        a,b=self.re,self.im;c,d=other.re,other.im
        return GQ(a*c-b*d,a*d+b*c)

    def inverse(self):
        norm=self.norm2()
        if not norm:raise ZeroDivisionError('zero gaussian')
        return GQ(self.re/norm,-self.im/norm)

    def __truediv__(self,other):return self*other.inverse()

    def norm2(self):return self.re*self.re+self.im*self.im

    def __complex__(self):return complex(float(self.re),float(self.im))


ONE=GQ(1)
ZERO=GQ(0)


def r_at(z):
    """Original four signed rational BBP poles on Gaussian argument z."""
    if not isinstance(z,GQ):raise ValueError('Gaussian argument required')
    return (GQ(4)/((GQ(8)*z)-GQ(7))
            -GQ(2)/((GQ(8)*z)-GQ(4))
            -ONE/((GQ(8)*z)-GQ(3))
            -ONE/((GQ(8)*z)-GQ(2)))


def gamma_source_factor(q,omega):
    """Exact auxiliary positive BBP Mellin characteristic r(n-iω)/r(n), n=1/q."""
    q=F(q);omega=F(omega)
    if not 0<q<=1:raise ValueError('0<q<=1')
    base=GQ(1/q)
    return r_at(GQ(1/q,-omega))/r_at(base)


def gamma_shape2_factor(q,omega):
    """Gamma(shape2,rate=1/q) characteristic (1-iωq)^(-2)."""
    u=GQ(1,-F(omega)*F(q))
    return ONE/(u*u)


def tangent_corrector(q,omega):
    """EXACT stationary field update ratio, 1+O_ω(q²) as q->0."""
    q=F(q);omega=F(omega)
    if not 0<q<=1:raise ValueError('0<q<=1')
    u=GQ(1,-omega*q)
    return gamma_source_factor(q,omega)*(u*u)


def moving_clock(q):
    q=F(q)
    if not 0<q<=1:raise ValueError('0<q<=1')
    return q/(1+q)


@dataclass(frozen=True)
class GammaTangentObserver:
    """Static transfer in Q(i) with no explicitly updated n-index.

    State (q,z) updates by a rational-Gaussian source factor at current q.
    z converges to a nonzero limit for each fixed rational omega.
    Large exact rational numerators grow; this is fixed dimension, not bounded bits.
    """
    q: F=F(1)
    z: GQ=ONE

    def step(self,omega):
        u=tangent_corrector(self.q,omega)
        return GammaTangentObserver(moving_clock(self.q),self.z*u)


def product_corrected(n,omega):
    if type(n) is not int or n<0:raise ValueError('n>=0')
    o=GammaTangentObserver()
    for _ in range(n):o=o.step(omega)
    return o


def product_raw(n,omega):
    if type(n) is not int or n<0:raise ValueError('n>=0')
    q=F(1);p=ONE
    for _ in range(n):
        p=p*gamma_source_factor(q,omega)
        q=moving_clock(q)
    return p


def product_gamma2(n,omega):
    if type(n) is not int or n<0:raise ValueError('n>=0')
    q=F(1);p=ONE
    for _ in range(n):
        p=p*gamma_shape2_factor(q,omega)
        q=moving_clock(q)
    return p


def analytic_moment_source_coefficients():
    """r(s) ~ 15/(64s²); Gamma shape2 tangent is source derived."""
    taps=(F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0))
    return {'mass':sum(taps,F(0)),
            'first_moment':sum((j*x for j,x in enumerate(taps)),F(0)),
            'leading_laurent':F(15,64)}


if __name__=='__main__':
    for n in (1,2,4,8,16,24):
        o=product_corrected(n,F(1,2))
        print(n, 'q=',o.q,'z≈',complex(o.z),'mod=',float(o.z.norm2())**.5)
