"""Exact source-typed BBP causal-volume rewriting calculus.

The input is the *declared* polynomial Mellin forcing grammar, not a
claim about arbitrary physical signals, statistical normality or RH.
Every result is exact Fraction arithmetic. The original four-pole BBP
passport is the named, zero-seeded instance; other grammars are controls.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import factorial

Q = Fraction


def _rat(a):
    if type(a) not in (int, Fraction):
        raise ValueError("Exact integer/Fraction coefficients only")
    return Q(a)


def poly(*terms):
    """Ascending rational coefficients, remove trailing zeros."""
    if not terms:
        return (Q(0),)
    xs = [_rat(x) for x in terms]
    while len(xs) > 1 and xs[-1] == 0:
        xs.pop()
    return tuple(xs)


def padd(a, b):
    return poly(*(
        (a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
        for i in range(max(len(a), len(b)))))


def pscale(a, f):
    f = _rat(f)
    return poly(*(v*f for v in a))


def pmul(a, b):
    out = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return poly(*out)


def pcompose(a, b):
    """Return polynomial a(b(t)); preserves exact rational source charts."""
    out=poly(0)
    for coef in reversed(a):
        out=padd(pmul(out,b),poly(coef))
    return out


def peval(a, x):
    x = _rat(x)
    t = Q(0)
    for c in reversed(a):
        t = t*x + c
    return t


def pderiv(a):
    return poly(*(i*a[i] for i in range(1,len(a))))


def pdivmod(a, b):
    if b == (Q(0),):
        raise ZeroDivisionError("zero polynomial")
    a = poly(*a); b=poly(*b)
    rem = list(a)
    quot = [Q(0)] * max(1,len(a)-len(b)+1)
    while len(rem)>=len(b) and any(rem):
        exponent=len(rem)-len(b)
        coef=rem[-1]/b[-1]
        quot[exponent]+=coef
        for i,bi in enumerate(b):
            rem[i+exponent]-=coef*bi
        rem=list(poly(*rem))
    return poly(*quot), poly(*rem)


def pgcd(a,b):
    a=poly(*a);b=poly(*b)
    if a==(Q(0),) and b==(Q(0),):
        raise ValueError("Both polynomials zero")
    while b != (Q(0),):
        a,b=b,pdivmod(a,b)[1]
    return pscale(a,1/a[-1])


def integral_monomial_product(a, degree=0):
    """Exact integral ∫_0^1 t^degree * a(t) dt, degree >=0 integer."""
    if type(degree) is not int or degree<0:
        raise ValueError("Nonnegative integer Mellin moment needed")
    return sum((c/Q(degree+j+1) for j,c in enumerate(a)),Q(0))


def from_sparse(terms):
    terms = tuple(terms)
    if not terms:
        return poly(0)
    out = [Q(0)]*(max(e for _,e in terms)+1)
    for c,e in terms:
        if type(e) is not int or e<0:
            raise ValueError("Nonnegative polynomial exponent")
        out[e]+=_rat(c)
    return poly(*out)


@dataclass(frozen=True)
class CausalVolumeGrammar:
    """r(n)=∫t^(a*(n-1)) Q(t)dt, zero seed, radix b>1."""
    radix: int
    stride: int
    numerator: tuple[Q,...]

    def __post_init__(self):
        if type(self.radix) is not int or self.radix<2:
            raise ValueError("Radix must be integer >=2")
        if type(self.stride) is not int or self.stride<1:
            raise ValueError("Mellin stride must be positive integer")
        if not isinstance(self.numerator,tuple):
            raise ValueError("Polynomial source must be tuple")
        p=poly(*self.numerator)
        if p==(Q(0),):
            raise ValueError("Nonzero polynomial source required")
        object.__setattr__(self,"numerator",p)

    @property
    def denominator(self):
        d=[Q(0)]*(self.stride+1)
        d[0]=Q(self.radix);d[-1]=-Q(1)
        return poly(*d)

    @property
    def reduced_kernel(self):
        g=pgcd(self.numerator,self.denominator)
        top,remainder=pdivmod(self.numerator,g)
        bot,rem2=pdivmod(self.denominator,g)
        assert remainder==(Q(0),) and rem2==(Q(0),)
        return top,bot

    def forcing(self,n):
        if type(n) is not int or n<1:
            raise ValueError("n>=1")
        return integral_monomial_product(self.numerator,self.stride*(n-1))

    def volume_polynomial(self,n):
        """(b^n-t^(a*n))/(b-t^a), an exact finite polynomial."""
        if type(n) is not int or n<0:
            raise ValueError("n>=0")
        if n==0:
            return poly(0)
        out=[Q(0)]*(self.stride*(n-1)+1)
        for j in range(n):
            out[self.stride*j]=Q(self.radix**(n-1-j))
        return poly(*out)

    def state(self,n):
        """Construct selected U_n from zero using only finite algebra."""
        return integral_monomial_product(pmul(self.numerator,self.volume_polynomial(n)))

    def state_by_successor(self,n):
        if type(n) is not int or n<0:
            raise ValueError("n>=0")
        v=Q(0)
        for k in range(1,n+1):
            v=self.radix*v+self.forcing(k)
        return v

    def prefix(self,n):
        return self.state(n)/self.radix**n

    def truncated_green(self,n,depth):
        if type(n) is not int or n<0 or type(depth) is not int or depth<0:
            raise ValueError("n,depth>=0")
        return sum((self.forcing(n+j)/self.radix**j for j in range(1,depth+1)),Q(0))

    def finite_volume_residual(self,n):
        """Polynomial residual (b-t^a)V_n - (b^n-t^(a*n))."""
        if type(n) is not int or n<0:
            raise ValueError("n>=0")
        lhs=pmul(self.denominator,self.volume_polynomial(n))
        rhs=[Q(0)]*(self.stride*n+1)
        rhs[0]+=self.radix**n
        rhs[-1]-=1
        return padd(lhs,pscale(poly(*rhs),-1))

    def pointwise_cancellation(self):
        """Q * finite-volume == b^n - t^(a*n), after denominator clearing."""
        top,bot=self.reduced_kernel
        return pmul(top,self.denominator)==pmul(bot,self.numerator)

    def origin_equalizer(self):
        return self.state(0)==0 and self.volume_polynomial(0)==poly(0)

    def source_moment_integrand(self,n):
        """Integrand for r(n+1)=b T_n-T_(n+1), after cancellation."""
        if type(n) is not int or n<0:
            raise ValueError("n>=0")
        return pmul(self.numerator,poly(*([Q(0)]*(self.stride*n)+[Q(1)])))

    def endpoint_order_and_coefficient(self):
        """If R=(1-t)^k H, return k and H(1). The Gamma shape is k+1.

        Does not assert positivity; caller must authenticate H>0 at endpoint.
        """
        d=self.numerator
        k=0
        while peval(d,1)==0:
            k+=1
            d=pderiv(d)
            if d==(Q(0),):
                raise AssertionError("Nonzero polynomial lost all derivatives")
        coefficient=Q((-1)**k,factorial(k))*peval(d,1)/Q(self.radix-1)
        return k,coefficient


BBP=CausalVolumeGrammar(16,8,from_sparse(((4,0),(-2,3),(-1,4),(-1,5))))

# Hostile grammar has the SAME zero origin, radix/stride, positive Gamma(2)
# endpoint behavior, but its completed real is exactly rational 1/2.
ALT_POLY=pmul(BBP.denominator,poly(1,-1))
RATIONAL_NONNORMAL=CausalVolumeGrammar(16,8,ALT_POLY)


def bbp_tail_interval(n,depth):
    """Source-verified monotone four-pole tail; not for generic grammar."""
    if type(n) is not int or n<0 or type(depth) is not int or depth<0:
        raise ValueError("n,depth>=0")
    lo=BBP.truncated_green(n,depth)
    # Since r is positive decreasing, each omitted r(n+j) <= r(n+depth+1).
    hi=lo+BBP.forcing(n+depth+1)*Q(1,15*16**depth)
    return lo,hi


def bbp_completed_interval(depth):
    return bbp_tail_interval(0,depth)


def bbp_forcing_pole_decomposition(n):
    if type(n) is not int or n<1:
        raise ValueError("n>=1")
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def jacobian_gauge_pullback(t, a, b):
    """For t=a+(b-a)u, return typed t and dt/du; not an invariant by itself."""
    return a+(b-a)*t,b-a


def fixed_n_shift_crosscheck(n,depth):
    """Finite rational identity between two source completion truncations.

    b^n * P_(n+depth) - U_n = T_(n,depth).
    """
    if type(n) is not int or n<0 or type(depth) is not int or depth<0:
        raise ValueError("n,depth>=0")
    return (16**n*BBP.prefix(n+depth)-BBP.state(n)
            -BBP.truncated_green(n,depth))


def phase_frequency_ladder_residual(n,h):
    """e(hU_(n+1)) = e(b*h U_n)*e(h*r(n+1)), exact real lift."""
    if type(h) is not int or h==0:
        raise ValueError("Nonzero integer frequency")
    return Q(h)*(BBP.state(n+1)-16*BBP.state(n)-BBP.forcing(n+1))


def finite_moment_positive_mutant(max_observed_moment):
    """Target-equivalent, source-different positive kernel matched at 8k, k<=M.

    Builds f=d^L/dt^L[t^(L+2)*(1-t)^(L+2)], L=8M+1.
    Integration by parts gives ∫t^(8k) f = 0 for k<=M.
    f vanishes quadratically at both endpoints; a small exact epsilon
    preserves positivity and the Gamma(2) endpoint coefficient.
    This changes the polynomial forcing and must NEVER be passed off as
    the authentic four-pole BBP source.
    """
    M=max_observed_moment
    if type(M) is not int or M<0 or M>3:
        raise ValueError("Finite exact synthetic-mutation budget 0..3")
    L=8*M+1
    h=pmul(poly(*([Q(0)]*(L+2)+[Q(1)])),_one_minus_t_power(L+2))
    f=h
    for _ in range(L):
        f=pderiv(f)
    fm1,rem=pdivmod(f,poly(1,-1))
    assert rem==(Q(0),)
    fm2,rem=pdivmod(fm1,poly(1,-1))
    assert rem==(Q(0),)
    magnitude=sum(map(abs,fm1),Q(0))
    epsilon=Q(1,8*(1+magnitude))
    newQ=padd(BBP.numerator,pscale(pmul(BBP.denominator,f),epsilon))
    result=CausalVolumeGrammar(16,8,newQ)
    return result, f, epsilon


def _one_minus_t_power(power):
    if type(power) is not int or power<0:
        raise ValueError("power>=0")
    p=poly(1)
    for _ in range(power):
        p=pmul(p,poly(1,-1))
    return p


def finite_difference_forcing(n,k,grammar=BBP):
    """(-1)^k Δ^k r(n+1), by exact binomial difference."""
    from math import comb
    if type(n) is not int or n<0 or type(k) is not int or k<0:
        raise ValueError("n,k>=0")
    return sum((Q((-1)**j*comb(k,j))*grammar.forcing(n+1+j)
                for j in range(k+1)),Q(0))


def finite_difference_integrand(n,k,grammar=BBP):
    """Polynomial t^(a*n)(1-t^a)^k * Q(t), integrates to the same signed Δ^k r."""
    if type(n) is not int or n<0 or type(k) is not int or k<0:
        raise ValueError("n,k>=0")
    power=poly(*([Q(0)]*(grammar.stride*n)+[Q(1)]))
    one_minus=poly(*([Q(1)]+[Q(0)]*(grammar.stride-1)+[Q(-1)]))
    for _ in range(k):
        power=pmul(power,one_minus)
    return pmul(power,grammar.numerator)


def approximate_green_difference(n,k,depth=32):
    """Certified positive kth difference of authentic T_n by direct series.

    Sum_{j>=1} b^-j (-1)^k Δ^k r(n+j) is nonnegative; the tail
    is bounded by monotonicity of the original r sequence, so return
    rigorous rational bounds for the exact continuous-volume moment.
    """
    if type(n) is not int or n<0 or type(k) is not int or k<0:
        raise ValueError("n,k>=0")
    if type(depth) is not int or depth<0:
        raise ValueError("depth>=0")
    terms=sum((Q(1,16**j)*finite_difference_forcing(n+j-1,k)
               for j in range(1,depth+1)),Q(0))
    # Each finite difference moment is <= r(n+depth+1) for positive Q.
    # Positive monotone sequence: r(m) decreases as m increases.
    residual=Q(1,15*16**depth)*BBP.forcing(n+depth+1)
    return terms,terms+residual


def bbp_integer_lift_carry(n):
    """Literal floor carry of the exact selected rational unwrapped orbit."""
    if type(n) is not int or n<1:
        raise ValueError("carry n>=1")
    a=BBP.state(n)
    b=BBP.state(n-1)
    return a.numerator//a.denominator-16*(b.numerator//b.denominator)


def gamma_phase_bound(m, lam_abs):
    """All-source rational upper bound for moving Mellin twist, m>=14.

    |M(m(1+iλ))/M(m) - (1+iλ)^(-2)| <= (14+12|λ|)/m + 2m²/2^m.
    Input |λ| is exact nonnegative rational, output a rational bound.
    This uses source's positive R and the all-m 7/m TV Gamma bound.
    """
    if type(m) is not int or m<14:
        raise ValueError("m>=14 is required for I_m >=1/(2m²)")
    lam_abs=_rat(lam_abs)
    if lam_abs<0:
        raise ValueError("|lambda| must be nonnegative")
    return (Q(14)+Q(12)*lam_abs)/m+Q(2*m*m,2**m)

# The original Oily two-stage transfer, now in the SAME source variable t.
OILY_U=poly(0,1,Q(-1,2))
OILY_V=poly(0,0,Q(1,2))
OILY_DEN=pscale(pmul(padd(poly(1),pscale(OILY_U,-1)),
                         padd(poly(1),pscale(OILY_V,-1))),4)


def oily_two_register_resolvent_entry(t):
    """First entry of (I - [[u,1],[0,v]])^(-1) e2 at t; rational."""
    t=_rat(t)
    if not Q(0)<=t<=Q(1):
        raise ValueError("0<=t<=1")
    u=peval(OILY_U,t);v=peval(OILY_V,t)
    return Q(1)/((1-u)*(1-v))


def oily_packet(t,j):
    """Authentic source positive grade p_j(t), not a physical iid signal."""
    t=_rat(t)
    if not Q(0)<=t<=Q(1) or type(j) is not int or j<0:
        raise ValueError("0<=t<=1 and j>=0")
    u=peval(OILY_U,t);v=peval(OILY_V,t)
    return (1-t)*sum((u**k*v**(j-k) for k in range(j+1)),Q(0))/4


def oily_packet_partial(t,N):
    if type(N) is not int or N<0:
        raise ValueError("N>=0")
    return sum((oily_packet(t,j) for j in range(N+1)),Q(0))


def oily_packet_tail_budget(t,N):
    """Rigorous old WOC bound on sum_{j>N}p_j(t) for 0<=t<=1."""
    t=_rat(t)
    if not Q(0)<=t<=Q(1) or type(N) is not int or N<0:
        raise ValueError("0<=t<=1,N>=0")
    return (1-t)*Q(N+3,2**(N+2))
