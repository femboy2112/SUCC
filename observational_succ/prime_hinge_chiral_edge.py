"""Exact arithmetic for a *single* authentic-form prime-hinge source channel.

The source-conditioned theorem is for the isolated symmetric kernel
    H_b(x,y) = w * (abs(x-y)-b)_+
on (-a,a), with a < b < 2*a.  It is NOT the complete signed Weil
kernel, does not establish first-window positivity or RH, and does not
construct a new physical observer/sensor.  Only int/Fraction inputs are
accepted; the true prime2 parameters are separately authenticated via the
existing immutable SUCC source adapter.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb


class HingeError(ValueError):
    pass


def exact(v):
    if type(v) not in (int, Q):
        raise HingeError("exact integer/Fraction required; no float/bool")
    return Q(v)


def poly(values):
    if not isinstance(values, tuple):
        raise HingeError("polynomial coefficients must be immutable tuple")
    z = tuple(exact(x) for x in values)
    while len(z) > 1 and z[-1] == 0:
        z = z[:-1]
    return z or (Q(0),)


def add(a, b):
    a, b = poly(a), poly(b)
    return poly(tuple((a[i] if i < len(a) else Q(0)) +
                      (b[i] if i < len(b) else Q(0))
                      for i in range(max(len(a), len(b)))))


def scale(a, k):
    k = exact(k)
    return poly(tuple(k*x for x in poly(a)))


def mul(a, b):
    a, b = poly(a), poly(b)
    z = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    return poly(tuple(z))


def pow_poly(a, n):
    if type(n) is not int or n < 0 or n > 60:
        raise HingeError("nonnegative in-budget degree required")
    out = (Q(1),)
    for _ in range(n):
        out = mul(out, a)
    return out


def deriv(a, times=1):
    if type(times) is not int or times < 0:
        raise HingeError("nonnegative derivative order required")
    out = poly(a)
    for _ in range(times):
        out = poly(tuple(i*out[i] for i in range(1, len(out))))
    return out


def primitive(a, constant=0):
    a = poly(a)
    return poly((exact(constant),)+tuple(v/Q(i+1) for i, v in enumerate(a)))


def eval_poly(a, x):
    x, out = exact(x), Q(0)
    for c in reversed(poly(a)):
        out = out*x+c
    return out


def integrate(a, lo, hi):
    lo, hi = exact(lo), exact(hi)
    if hi < lo:
        raise HingeError("ordered integration endpoints required")
    p = primitive(a)
    return eval_poly(p, hi)-eval_poly(p, lo)


def translate(a, shift):
    """Return coefficients of p(t+shift)."""
    a, shift = poly(a), exact(shift)
    z = [Q(0)]*len(a)
    for k, c in enumerate(a):
        for i in range(k+1):
            z[i] += c*comb(k, i)*shift**(k-i)
    return poly(tuple(z))


@dataclass(frozen=True)
class EdgeHinge:
    radius: Q
    log_time: Q
    weight: Q

    def __post_init__(self):
        a, b, w = map(exact, (self.radius, self.log_time, self.weight))
        if not 0 < a < b < 2*a:
            raise HingeError("two disjoint edge windows require 0<a<b<2a")
        object.__setattr__(self, 'radius', a)
        object.__setattr__(self, 'log_time', b)
        object.__setattr__(self, 'weight', w)

    @property
    def width(self):
        return 2*self.radius-self.log_time

    def hs_squared(self):
        """True FULL-L2 Hilbert-Schmidt norm squared of the isolated kernel."""
        return self.weight**2*self.width**4/Q(6)

    def energy(self, left, right):
        """Exact K-geometry on F(-a+t)=L(t), F(b-a+t)=R(t), 0<t<delta.

        Caller must separately ensure any represented F is zero elsewhere,
        H_0^1, and its derivative satisfies the desired moment constraints.
        """
        left, right = poly(left), poly(right)
        d = self.width
        l2 = integrate(mul(left,left), 0, d)
        r2 = integrate(mul(right,right), 0, d)
        overlap = integrate(mul(left,right), 0, d)
        k = l2+r2
        q = -2*self.weight*overlap
        if q*q > self.weight**2*k*k:
            raise ArithmeticError("K-relative Cauchy/AM-GM inequality failed")
        return {'left_L2_squared':l2, 'right_L2_squared':r2,
                'edge_inner_product':overlap, 'K_energy':k,
                'prime_quadratic':q,
                'K_relative_bound':abs(self.weight)*k,
                'full_L2_HS_norm_squared':self.hs_squared(),
                'complete_Weil_source':False, 'RH_proved':False}


def moment_annihilating_edge(order, width):
    """phi = d^order/dt^order [t^(order+1)(width-t)^(order+1)].

    Its endpoints vanish; integral t^j phi(t) dt = 0 for all j<order.
    """
    if type(order) is not int or not 0 <= order <= 10:
        raise HingeError("finite exact moment order 0..10 required")
    width=exact(width)
    if width <= 0:
        raise HingeError("strictly positive edge width required")
    p = mul(pow_poly((Q(0),Q(1)),order+1),
            pow_poly((width, Q(-1)),order+1))
    q = deriv(p,order)
    if eval_poly(q,0) or eval_poly(q,width):
        raise ArithmeticError("boundary jet construction did not vanish")
    for j in range(order):
        if integrate(mul(q, (Q(0),)*j+(Q(1),)),0,width):
            raise ArithmeticError("constructed profile violates moment zero")
    return q


def high_moment_chiral_certificate(hinge:EdgeHinge, low_cut:int, *, sign:int=1):
    """Finite algebraic witness of sharp +/-|weight| on Q_m in K geometry.

    The left/right edge restrictions of primitive F are phi, sign*phi.
    Because the first low_cut shifted moments vanish, u=F' is orthogonal
    to all polynomial modes up to degree low_cut, including constants.
    """
    if not isinstance(hinge,EdgeHinge) or type(low_cut) is not int or not 0 <= low_cut <= 10:
        raise HingeError("exact hinge and nonnegative finite low cutoff required")
    if type(sign) is not int or sign not in (-1,1):
        raise HingeError("chiral sign must be +/-1")
    phi=moment_annihilating_edge(low_cut,hinge.width)
    certificate=hinge.energy(phi,scale(phi,sign))
    assert certificate['K_energy'] > 0
    # The two edge copies have derivative energy 2 * int |phi'|^2.
    # Its ratio to K energy is explicitly 2(2m+1)(2m+5)/delta^2
    # by the Legendre Sturm-Liouville relation (proved in the dossier).
    physical_L2=2*integrate(mul(deriv(phi),deriv(phi)),0,hinge.width)
    gradient_cost=physical_L2/certificate['K_energy']
    expected_cost=Q(2*(2*low_cut+1)*(2*low_cut+5),1)/hinge.width**2
    if gradient_cost != expected_cost:
        raise ArithmeticError('explicit Jacobi/Legendre gradient-cost formula failed')
    assert certificate['prime_quadratic'] == -sign*hinge.weight*certificate['K_energy']
    # For u=F', moments degree j=1..m are -j int x^(j-1) F.
    # Each of two translated edge profiles individually has vanishing moments.
    for j in range(low_cut):
        for origin in (-hinge.radius,hinge.log_time-hinge.radius):
            p = pow_poly((origin,Q(1)),j)
            if integrate(mul(p,phi),0,hinge.width):
                raise ArithmeticError("original u=F' high moment condition fails")
    return {'low_cut':low_cut, 'chirality':sign,
            'edge_width':hinge.width, 'weight':hinge.weight,
            'profile':phi, 'sharp_ratio': -sign*hinge.weight,
            'source_L2_energy': physical_L2,
            'gradient_to_K_cost': gradient_cost,
            'certificate':certificate,
            'source_authentication': 'requires frozen original signed Weil source',
            'RH_proved':False}


def polynomial_prime_derivative_gram(hinge:EdgeHinge, source_polynomials):
    """Exact Gram of ONLY the hinge contribution (H_b v)' for mean-zero polynomials.

    In two disjoint edge strips its derivative equals weight times a shifted
    primitive of v. Does NOT include gamma, contact, poles or other primes.
    """
    if not isinstance(hinge,EdgeHinge) or not isinstance(source_polynomials,tuple):
        raise HingeError('typed finite source polynomial family required')
    a, b, w = hinge.radius,hinge.log_time,hinge.weight
    fs=[]
    for p in source_polynomials:
        p=poly(p)
        if integrate(p,-a,a):
            raise HingeError('source input must be exactly mean-zero')
        F=primitive(p)
        F=add(F,(-eval_poly(F,-a),))
        if eval_poly(F,a):
            raise ArithmeticError('primitive endpoint failed')
        fs.append(F)
    matrix=[]
    for x in fs:
        matrix.append(tuple(w*w*(integrate(mul(x,y),-a,a-b)
                                 +integrate(mul(x,y),b-a,a)) for y in fs))
    return tuple(matrix)



def polynomial_prime_quadratic(hinge:EdgeHinge, left_input, right_input):
    """Exact sesquilinear REAL prime-hinge form on two mean-zero polynomials.

    By two integrations by parts this is
      -w int_(b-a)^a [Fp(x) Fq(x-b) + Fq(x) Fp(x-b)] dx.
    No source completion, Gamma or pole channel is included.
    """
    if not isinstance(hinge, EdgeHinge):
        raise HingeError("typed hinge required")
    a, b, w = hinge.radius, hinge.log_time, hinge.weight
    fs=[]
    for p in (left_input, right_input):
        p=poly(p)
        if integrate(p,-a,a):
            raise HingeError("mean-zero polynomial required")
        prim=primitive(p)
        prim=add(prim,(-eval_poly(prim,-a),))
        assert eval_poly(prim,a)==0
        fs.append(prim)
    fp,fq=fs
    f=add(mul(fp,translate(fq,-b)),mul(fq,translate(fp,-b)))
    return -w*integrate(f,b-a,a)

def authentic_prime2_interval_gate():
    """Verify that this theorem's b,w correspond to the REAL n=2 source.

    This authenticates the specific original source module and checks
    a<b<2a using verified rational intervals. It does not return exact b,w
    as Fraction or certify a sign for the full G source.
    """
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .source_weil_hierarchy import (authenticated_prime_wavefront,
                                       log2_iv, sqrt_inverse)
    verification=verify_original_suzuki_source()
    if authenticated_prime_wavefront(Q(1,2)) != ((2,2),):
        raise HingeError("frozen prime2 wavefront mismatch")
    b=log2_iv()
    inv=sqrt_inverse(2)
    if not Q(1,2)<b.lo<=b.hi<Q(1) or inv.lo<=0:
        raise HingeError("authentic prime2 edge order/amplitude gate failed")
    return {'source_verified':True,
            'source_receipt':verification,
            'prime_jet':(2,2),
            'radius':'1/2',
            'b_interval':(str(b.lo),str(b.hi)),
            'w_interval':(str(b.lo*inv.lo),str(b.hi*inv.hi)),
            'claim':'isolated genuine n=2 hinge ONLY',
            'all_source_positive':False, 'RH_proved':False}
