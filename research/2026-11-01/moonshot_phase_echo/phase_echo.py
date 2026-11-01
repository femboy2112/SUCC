"""Exact BBP phase echoes and certified signed probes. No normality theorem.

Pure stdlib. Fractions label phases modulo one, never floating 'certificates'.
The Hilbert-space claims and all-horizon bounds are proved in PROOFS.md.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt, lcm


def integer(n: int, minimum: int | None = None) -> int:
    if type(n) is not int or (minimum is not None and n < minimum):
        raise ValueError('exact integer outside domain')
    return n


def rational(x: int | F) -> F:
    if type(x) not in (int, F):
        raise TypeError('only exact integers/Fractions are accepted')
    return F(x)


def source(n: int) -> F:
    integer(n, 1)
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def states(N: int, seed: int | F = 0, *, circle: bool = False) -> tuple[F, ...]:
    integer(N, 0)
    x = rational(seed)
    out = [x % 1 if circle else x]
    for n in range(1, N+1):
        x = 16*x+source(n)
        if circle:
            x %= 1
        out.append(x)
    return tuple(out)


def tail_partial(n: int, depth: int) -> tuple[F, F]:
    """Exact lower/upper bounds for T_n from original monotone positive source."""
    integer(n, 0); integer(depth, 0)
    lower = sum((source(n+j)/16**j for j in range(1, depth+1)), F())
    return lower, lower + source(n+depth+1)/(15*16**depth)


def source_alpha(depth: int) -> tuple[F, F]:
    return tail_partial(0, depth)


def source_tail_budget(n: int) -> F:
    """T_n < 1/(64 n^2), n>=1; strict for authentic source."""
    integer(n, 1)
    return F(1, 64*n*n)


@dataclass(frozen=True)
class AffineWeyl:
    """e(phi) M_k W_(a,b), W psi(y)=a^-1/2 psi((y-b)/a).

    @ means operator composition, rightmost first. Exact affine/Weyl labels.
    The real phase is stored unwrapped; users may reduce it modulo one.
    """
    a: F = F(1)
    b: F = F(0)
    k: F = F(0)
    phi: F = F(0)

    def __post_init__(self):
        for name in ('a', 'b', 'k', 'phi'):
            object.__setattr__(self, name, rational(getattr(self, name)))
        if self.a <= 0:
            raise ValueError('positive affine dilation required')

    def __matmul__(self, other: AffineWeyl) -> AffineWeyl:
        if not isinstance(other, AffineWeyl):
            return NotImplemented
        return AffineWeyl(self.a*other.a, self.b+self.a*other.b,
                          self.k+other.k/self.a,
                          self.phi+other.phi-other.k*self.b/self.a)

    def inverse(self) -> AffineWeyl:
        return AffineWeyl(1/self.a, -self.b/self.a, -self.a*self.k,
                          -self.phi-self.k*self.b)

    def trace_argument(self, y: int | F) -> tuple[F, F]:
        """Argument and phase at y, omitting known positive half-density."""
        y = rational(y)
        return (y-self.b)/self.a, self.k*y+self.phi


def modulation(k: int | F) -> AffineWeyl:
    return AffineWeyl(k=rational(k))


def propagator(N: int, seed: int | F = 0) -> AffineWeyl:
    """Original forcing followed from declared initial translation seed."""
    integer(N, 0)
    out = AffineWeyl(b=rational(seed))
    for n in range(1, N+1):
        out = AffineWeyl(16, source(n)) @ out
    return out


def phase_echo(N: int, h: int, seed: int | F = 0) -> AffineWeyl:
    integer(h)
    if h == 0:
        raise ValueError('normality probes use nonzero h')
    p = propagator(N, seed)
    return p.inverse() @ modulation(h) @ p @ modulation(-h*p.a)


def odd_conductor(N: int) -> int:
    integer(N, 1)
    return lcm(*(source(n).denominator for n in range(1, N+1)))


def finite_register(N: int) -> tuple[int, tuple[int, ...]]:
    """Common odd denominator represents genuine real-circle phases, not Z2."""
    Q = odd_conductor(N)
    a, x = [], 0
    for n in range(1, N+1):
        force = source(n)*Q
        if force.denominator != 1:
            raise ArithmeticError('conductor does not bind the original source')
        x = (16*x+force.numerator) % Q
        a.append(x)
    return Q, tuple(a)


def scattering_error(N: int, derivative_norm: int | F) -> F:
    """H1 strong-wave-operator bound ||(T_A_N-T_alpha)psi||; N>=1."""
    integer(N, 1)
    d = rational(derivative_norm)
    if d < 0:
        raise ValueError('nonnegative norm')
    return d/(64*N*N*16**N)


def gaussian_prefix_error(h: int) -> F:
    """Uniform |sum z_n exp(-2pi²h² 16^(2(n-m))) - S_m| bound.

    m,N integers, 0<=m<=N; |z_n|<=1. Deliberately rational overestimate.
    """
    integer(h)
    if not h:
        raise ValueError('h nonzero')
    return 1+F(968*h*h,49*255)+F(1,4590*h*h)


def sobolev_resolution_budget(N: int, derivative_norm: int | F, h: int) -> F:
    """Upper bound N^-1 sum min(1,D/(pi |h|16^n)), using pi>3."""
    integer(N, 1); integer(h)
    if h == 0:
        raise ValueError('h nonzero')
    d = rational(derivative_norm)
    if d < 0:
        raise ValueError('nonnegative norm')
    return sum((min(F(1), d/(3*abs(h)*16**n)) for n in range(1,N+1)),F())/N


def fraction_sqrt_upper(x: F, bits: int = 70) -> F:
    x = rational(x); integer(bits, 1)
    if x < 0:
        raise ValueError('nonnegative radicand')
    scale = 1 << bits
    q = isqrt((x.numerator*scale*scale)//x.denominator)
    return F(q if F(q, scale)**2 == x else q+1, scale)


@lru_cache(maxsize=1)
def pi_interval() -> tuple[F, F]:
    """Machin identity and alternating rational remainders, independent of BBP."""
    def atan(q: int, count: int) -> tuple[F,F]:
        s = sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(count)),F())
        r = F((-1)**count,(2*count+1)*q**(2*count+1))
        return min(s,s+r), max(s,s+r)
    a,b = atan(5,48); c,d = atan(239,16)
    return 16*a-4*d, 16*b-4*c


def _ceil(x: F) -> int:
    return -((-x.numerator)//x.denominator)


def _div_interval(lo: int, hi: int, numerator: int, denominator: int) -> tuple[int,int]:
    if numerator < 0 or denominator <= 0 or lo > hi:
        raise ValueError('bad positive interval scaling')
    return lo*numerator//denominator, -((-hi*numerator)//denominator)


class PhaseEncloser:
    """Rational outward Taylor certificates. No float affects acceptance."""
    def __init__(self, bits: int = 90, terms: int = 30):
        integer(bits, 16); integer(terms, 8)
        self.scale, self.terms = 1 << bits, terms
        self.pilo, self.pihi = pi_interval()
        self.cosrem = _ceil(F(22,7)**(2*terms)/factorial(2*terms)*self.scale)
        self.sinrem = _ceil(F(22,7)**(2*terms+1)/factorial(2*terms+1)*self.scale)

    def pair(self, phase: F) -> tuple[tuple[F,F],tuple[F,F]]:
        phase = rational(phase) % 1
        if phase > F(1,2):
            phase -= 1
        # Pay an explicit phase-grid error before transcendental algebra.
        B = self.scale
        qp = (phase.numerator*B)//phase.denominator
        grid = F(qp,B)
        grid_error = F(0) if qp*phase.denominator == phase.numerator*B else F(1,B)
        x1, x2 = 2*grid*self.pilo, 2*grid*self.pihi
        safety = 2*self.pihi*grid_error
        lo, hi = min(x1,x2)-safety, max(x1,x2)+safety
        q = ((lo+hi)*B/2).__floor__()
        if abs(F(q,B)) > F(22,7):
            raise ArithmeticError('Taylor remainder domain')
        transfer = _ceil(max(abs(lo-F(q,B)),abs(hi-F(q,B)))*B)
        q2 = q*q
        cl = ch = B
        sl = sh = q
        ctotlo = ctothi = B
        stotlo = stothi = q
        for j in range(1,self.terms):
            a,b = _div_interval(cl,ch,q2,B*B*(2*j-1)*(2*j))
            cl,ch=-b,-a
            a,b = _div_interval(sl,sh,q2,B*B*(2*j)*(2*j+1))
            sl,sh=-b,-a
            ctotlo+=cl;ctothi+=ch;stotlo+=sl;stothi+=sh
        ce, se = self.cosrem+transfer, self.sinrem+transfer
        return ((max(F(-1),F(ctotlo-ce,B)), min(F(1),F(ctothi+ce,B))),
                (max(F(-1),F(stotlo-se,B)), min(F(1),F(stothi+se,B))))

    def cosine(self, phase: F) -> tuple[F,F]:
        return self.pair(phase)[0]


def sum_intervals(items) -> tuple[F,F]:
    a=b=F()
    for lo,hi in items:
        a+=lo;b+=hi
    return a,b


def abs_square_interval(re: tuple[F,F], im: tuple[F,F]) -> tuple[F,F]:
    def square(t):
        a,b=t
        return (F(0) if a<=0<=b else min(a*a,b*b),max(a*a,b*b))
    r,s=square(re),square(im)
    return r[0]+s[0],r[1]+s[1]


def lag_transport_budget(N: int, K: int, h: int) -> F:
    """Inherited clipped source-only bound; positivity is not signed saving."""
    integer(N,1);integer(K,1);integer(h)
    if K>N or h==0: raise ValueError('invalid lag probe')
    return F(2,K*N)*sum((F(K-k,K)*fraction_sqrt_upper(F(11*abs(h)*(16**k-1),14))
                         for k in range(1,K)),F())


def certified_scores(xs: tuple[F,...], N: int, K: int, h: int,
                     enc: PhaseEncloser | None = None, *,
                     seed: int | F = 0, verify_source: bool = True) -> dict:
    integer(N,1);integer(K,1);integer(h)
    if K>N or len(xs)<=N or not h: raise ValueError('probe size/domain')
    seed = rational(seed)
    if verify_source:
        if xs[0] % 1 != seed % 1:
            raise ValueError('declared initial seed does not match phase history')
        for n in range(1,N+1):
            if (xs[n]-16*xs[n-1]-source(n)) % 1:
                raise ValueError('phase history violates the original four-pole source')
    enc=enc or PhaseEncloser()
    pairs=[enc.pair((h*xs[n])%1) for n in range(1,N+1)]
    re=sum_intervals(x[0] for x in pairs);im=sum_intervals(x[1] for x in pairs)
    mean2=tuple(x/(N*N) for x in abs_square_interval(re,im))
    actual=[F(),F()];reduced=[F(),F()]
    for k in range(1,K):
        factor=F(2*(K-k),K*K*N)
        c=sum_intervals(enc.cosine(h*(xs[n+k]-xs[n])) for n in range(1,N-k+1))
        d=sum_intervals(enc.cosine(h*(16**k-1)*xs[n]) for n in range(1,N-k+1))
        for j in (0,1):
            actual[j]+=factor*c[j];reduced[j]+=factor*d[j]
    budget=lag_transport_budget(N,K,h) if verify_source else None
    scale=1+F(K-1,N)
    return {'N':N,'K':K,'h':h,'source_phase_authenticated':verify_source,'declared_seed':seed,'mean_real':tuple(x/N for x in re),
            'mean_imag':tuple(x/N for x in im),'mean_square':mean2,
            'actual_lag':tuple(actual),'reduced_lag':tuple(reduced),
            'transport_budget':budget,
            'vdc_actual_upper':scale*(F(1,K)+actual[1]),
            'vdc_reduced_upper':scale*(F(1,K)+reduced[1]+budget) if budget is not None else None}


def regulator_echo_coefficients(N: int, epsilon: int | F, hbar: int | F = 1) -> tuple[F,F]:
    """For angular kappa: E_eps=e^(i kappa U-i c kappa²) T_(-d kappa).

    c=hbar*epsilon*C_N/2; d=hbar*epsilon*C_N/16^N.
    Multiplication by e^(+i c kappa²) T_(+d kappa) cancels the regulator exactly.
    """
    integer(N,1);eps=rational(epsilon);hb=rational(hbar)
    if eps<0 or hb<=0:raise ValueError('epsilon>=0 and hbar>0 required')
    C=F(256**N-1,255)
    return hb*eps*C/2, hb*eps*C/16**N


def regulator_echo_band_bound(N:int, epsilon:int|F, angular_frequency:int|F,
                              bandwidth:int|F,hbar:int|F=1)->F:
    c,d=regulator_echo_coefficients(N,epsilon,hbar)
    k=rational(angular_frequency);K=rational(bandwidth)
    if K<0:raise ValueError('nonnegative Fourier bandwidth')
    return min(F(2),c*k*k+d*abs(k)*K)


def coherent_counterseed_score(N: int, h: int, depth: int = 24) -> dict:
    """Genuine fixed irrational seed 1/5-alpha, enclosed without pretending it rational.

    At integer n, U_n(s)=16^n/5-T_n, so modulo one the phase is h*(1/5-T_n).
    """
    integer(N,1);integer(h);integer(depth,1)
    if not h:raise ValueError('h nonzero')
    enc=PhaseEncloser();re=[F(),F()];im=[F(),F()]
    for n in range(1,N+1):
        lo,hi=tail_partial(n,depth);middle=(lo+hi)/2
        c,s=enc.pair(h*(F(1,5)-middle))
        error=F(22,7)*abs(h)*(hi-lo)
        re[0]+=c[0]-error;re[1]+=c[1]+error
        im[0]+=s[0]-error;im[1]+=s[1]+error
    re=tuple(x/N for x in re);im=tuple(x/N for x in im)
    return {'N':N,'h':h,'completed_q':F(1,5),'literal_zero_boundary':False,
            'seed':'1/5-alpha (irrational), not a rational seed mutation',
            'mean_real':re,'mean_imag':im,'mean_square':abs_square_interval(re,im),
            'all_horizon_mean_square_lower':max(F(),1-F(11*abs(h),56*N))**2}
