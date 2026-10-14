"""Prime-form successor carrier, Gaussian heat, theta/Mellin and source controls.

CLASSICAL mathematical identities on declared Z, R, Gaussian Fourier and prime
sources. Not a physical measurement, an RH argument, nor a completed Weil sign.
All exact algebra uses Fraction; analytic probes are explicitly mpmath numerics.

The source carrier must retain (a) ordered affine p*q+b words; (b) lattice
spectral energy n^2; (c) true prime-power coefficients rather than generic
positional digits; (d) analytic Fourier/Mellin and domain certificates.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, factorial, isqrt, log
from typing import Sequence


class SourceHeatError(ValueError):
    """Invalid arithmetic source, unlicensed promotion or unsupported domain."""


def integer(v: int, minimum: int | None = None) -> int:
    if type(v) is not int or (minimum is not None and v < minimum):
        raise SourceHeatError("Expected exact integer in licensed domain")
    return v


def rational(v: int | Q) -> Q:
    if type(v) not in (int, Q):
        raise SourceHeatError("Expected exact int/Fraction; floats are not certificates")
    return Q(v)


def prime(n: int) -> bool:
    integer(n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


@dataclass(frozen=True)
class AffineSource:
    radix: int
    source_id: str = "integer_affine_source"
    basis_id: str = "base_p_digits"
    epoch: int = 0
    require_prime: bool = False

    def __post_init__(self) -> None:
        integer(self.radix, 2)
        integer(self.epoch, 0)
        if not self.source_id or not self.basis_id:
            raise SourceHeatError("Source and observation basis must be named")
        if self.require_prime and not prime(self.radix):
            raise SourceHeatError("Prime-jet label cannot be a composite radix")

    def step(self, q: int, b: int) -> int:
        integer(q)
        integer(b)
        if not 0 <= b < self.radix:
            raise SourceHeatError("Digit b must be inside complete residue system")
        return self.radix * q + b

    def inverse(self, n: int) -> tuple[int, int]:
        integer(n)
        q, b = divmod(n, self.radix)
        assert self.step(q,b) == n
        return (q,b)


def digits_apply(radices: Sequence[int], digits: Sequence[int], start: int = 0) -> int:
    integer(start)
    if len(radices) != len(digits) or len(radices)>12:
        raise SourceHeatError("One authorized digit per radix, depth<=12")
    x = start
    for p,b in zip(radices,digits):
        x = AffineSource(p).step(x,b)
    return x


def digit_inverse(radices: Sequence[int], end: int) -> tuple[int,tuple[int,...]]:
    integer(end)
    if len(radices)>12:
        raise SourceHeatError("Bounded exact readout")
    n = end
    out = []
    for p in reversed(radices):
        integer(p,2)
        n,b = divmod(n,p)
        out.append(b)
    return (n,tuple(reversed(out)))


def affine_commutator(p: int, b: int, q: int, c: int) -> int:
    """F_(p,b)∘F_(q,c) minus F_(q,c)∘F_(p,b), any integer input."""
    left=AffineSource(p);right=AffineSource(q)
    left.step(0,b);right.step(0,c)
    return (p-1)*c - (q-1)*b


def digit_isometry_image(p: int, b: int, n: int) -> int:
    """S_(p,b)e_n=e_(pn+b) on l2(Z) (exact index representation)."""
    return AffineSource(p).step(n,b)


def digit_isometry_adjoint(p: int, b: int, n: int) -> int | None:
    """S_(p,b)*e_n = e_q if n=pq+b; otherwise zero vector."""
    s=AffineSource(p)
    q,c=s.inverse(n)
    s.step(0,b)
    return q if c == b else None


def polynomial_heat(coeff: Sequence[int | Q], t: int | Q) -> tuple[Q,...]:
    """e^(t ∂_x²)P. A genuine inner even-degree grading operator."""
    time=rational(t)
    if time<0 or not coeff or len(coeff)>64:
        raise SourceHeatError("Nonnegative heat time and finite polynomial needed")
    out=[Q(0)]*len(coeff)
    for n,c in enumerate(coeff):
        for k in range(n//2+1):
            out[n-2*k] += rational(c)*Q(factorial(n),factorial(k)*factorial(n-2*k))*time**k
    return tuple(out)


def polynomial_translate(coeff: Sequence[int | Q], d: int | Q) -> tuple[Q,...]:
    """P(x+d); commuting unit SUCC, exact Pascal action on coefficients."""
    step=rational(d)
    if not coeff or len(coeff)>64:
        raise SourceHeatError("Finite polynomial required")
    out=[Q(0)]*len(coeff)
    for n,c in enumerate(coeff):
        for k in range(n+1):
            out[k] += rational(c)*comb(n,k)*step**(n-k)
    return tuple(out)


def gaussian_even_moment(n: int, t: int | Q) -> Q:
    """E[X^(2n)] for heat kernel with X~N(0,2t)."""
    integer(n,0)
    time=rational(t)
    if time<0 or n>31:
        raise SourceHeatError("Gaussian even moment domain")
    return Q(factorial(2*n),factorial(n))*time**n


def prime_powers_up_to(N: int) -> tuple[tuple[int,int,int], ...]:
    """Unique source-certified arithmetic jet (n,p,k), 2<=n<=N, n=p^k."""
    integer(N,2)
    if N>100000:
        raise SourceHeatError("Finite source guard N<=100000")
    rows=[]
    for p in range(2,N+1):
        if not prime(p):
            continue
        x=p;k=1
        while x<=N:
            rows.append((x,p,k))
            x*=p;k+=1
    return tuple(sorted(rows))


def prime_power_witness(n: int) -> tuple[int,int] | None:
    integer(n)
    if n<2:
        return None
    for p in range(2,isqrt(n)+2):
        if not prime(p) or n%p:
            continue
        cur=n;k=0
        while cur%p==0:
            cur//=p;k+=1
        return (p,k) if cur==1 else None
    return (n,1) if prime(n) else None


def prime_jet_exact_coefficients(N: int) -> tuple[tuple[int,int],...]:
    """Coefficients labelled (p^k,p): formal log(p), not a guessed float."""
    return tuple((n,p) for n,p,_ in prime_powers_up_to(N))


def tree_depth_dirichlet(p: int, depth: int, s: int, *, weighting: str) -> Q:
    """Raw p^k states vs normalized p^-k PER-STATE thermal functional.

    R(s) = sum_k p^k*p^(-s*k) (raw multiplicities)
    N(s) = sum_k p^k*p^-k*p^-s*k (normalized level mass).
    The weighted functional is NOT an unweighted Hilbert-space trace.
    """
    integer(p,2);integer(depth,0);integer(s,2)
    if depth>50 or weighting not in ("raw_count", "level_normalized"):
        raise SourceHeatError("Declared finite tree weighting required")
    expo=(1-s) if weighting=="raw_count" else -s
    return sum((Q(p)**(k*expo) for k in range(depth+1)),Q(0))


def tree_depth_limit(p: int,s: int,*,weighting: str) -> Q:
    integer(p,2);integer(s,2)
    if weighting not in ("raw_count","level_normalized"):
        raise SourceHeatError("Invalid source measure")
    expo=(1-s) if weighting=="raw_count" else -s
    return 1/(1-Q(p)**expo)


def tree_depth_remainder(p:int,depth:int,s:int,*,weighting:str)->Q:
    integer(depth,0)
    expo=(1-s) if weighting=="raw_count" else -s
    return Q(p)**((depth+1)*expo)*tree_depth_limit(p,s,weighting=weighting)


def local_radix_euler(p:int,s:int)->Q:
    """A local factor only for verified prime p, σ=s>1."""
    integer(p,2);integer(s,2)
    if not prime(p):
        raise SourceHeatError("Arithmetic Euler place requires a genuine prime")
    return 1/(1-Q(p)**(-s))


def prime_heat_dirichlet_tail_upper(N:int,s:int)->str:
    """Human-readable exact rigorous bound incl log; for N>=3, real σ>1.

    |sum_(n>N) Λ(n)n^-s| <= N^(1-σ) [log N/(σ-1)+1/(σ-1)^2].
    Complex s accepted in analytic derivation via σ=Re(s), not here.
    """
    integer(N,3);integer(s,2)
    return f"{N}**(1-{s})*(log({N})/({s}-1)+1/({s}-1)**2)"


def _mp():
    try:
        import mpmath as mp
    except ImportError as e:
        raise SourceHeatError("mpmath optional research dependency not installed") from e
    return mp


def _mp_time(v):
    mp=_mp()
    if type(v) in (int,Q):
        q=rational(v)
        return mp.mpf(q.numerator)/q.denominator
    return mp.mpf(v)


def _mp_complex(v):
    mp=_mp()
    if type(v) is Q:
        return mp.mpc(mp.mpf(v.numerator)/v.denominator)
    return mp.mpc(v)


def gaussian_arch_factor(s, scale: int | Q = 1, dps:int =50):
    """π^-s/2 Γ(s/2) c^-s/2 with Gaussian e^-π*c*x², Re(s)>0."""
    mp=_mp();mp.mp.dps=dps
    c=rational(scale)
    z=_mp_complex(s)
    if c<=0 or z.real<=0 or not 20<=dps<=150:
        raise SourceHeatError("Positive Gaussian scale and Re(s)>0 required")
    return (mp.pi*mp.mpf(c.numerator)/c.denominator)**(-z/2)*mp.gamma(z/2)


def gaussian_arch_integral(s,dps:int=50):
    """Numerical independent real-line Mellin integral, not a rigorous interval."""
    mp=_mp();mp.mp.dps=dps
    z=_mp_complex(s)
    if z.real<=0:
        raise SourceHeatError("Real Mellin local factor needs Re(s)>0")
    return 2*mp.quad(lambda x: mp.exp(-mp.pi*x*x)*mp.power(x,z-1),[0,mp.mpf('0.1'),1,mp.inf])


def prime_jet_heat(t, N:int=300,dps:int=50):
    mp=_mp();mp.mp.dps=dps
    time=_mp_time(t)
    if time<=0:
        raise SourceHeatError("Heat parameter t>0")
    return sum((mp.log(p)*mp.exp(-mp.pi*time*n*n) for n,p,_ in prime_powers_up_to(N)),mp.mpf(0))


def prime_jet_mellin_truncated(s,N:int=300,dps:int=50):
    mp=_mp();mp.mp.dps=dps
    z=_mp_complex(s)
    if z.real<=1:
        raise SourceHeatError("Absolute prime-jet Dirichlet identity requires Re(s)>1")
    return gaussian_arch_factor(z,dps=dps)*sum((mp.log(p)*mp.power(n,-z) for n,p,_ in prime_powers_up_to(N)),mp.mpc(0))


def prime_jet_log_derivative(s,dps:int=50):
    mp=_mp();mp.mp.dps=dps;z=_mp_complex(s)
    if z.real<=1:
        raise SourceHeatError("No claim of analytic identification outside Re(s)>1")
    return gaussian_arch_factor(z,dps=dps)*(-mp.diff(mp.zeta,z)/mp.zeta(z))


def prime_tail_upper_numeric(N:int,s:int,dps:int=50):
    mp=_mp();mp.mp.dps=dps
    integer(N,3);integer(s,2)
    return mp.power(N,1-s)*(mp.log(N)/(s-1)+1/mp.mpf((s-1)**2))


def coset_theta(p:int,b:int,t,cut:int=18,dps:int=50):
    """Exact formula Σ_q exp(-π t(pq+b)^2); cutoff is NUMERICAL."""
    mp=_mp();mp.mp.dps=dps
    integer(cut,0)
    src=AffineSource(p);src.step(0,b)
    tau=_mp_time(t)
    if tau<=0 or cut>200:
        raise SourceHeatError("Positive t, bounded numerical truncation")
    return sum((mp.exp(-mp.pi*tau*src.step(q,b)**2) for q in range(-cut,cut+1)),mp.mpf(0))


def coset_theta_fourier(p:int,b:int,t,cut:int=18,dps:int=50):
    """Poisson dual: 1/(p sqrt(t))Σ_m exp(-πm²/(p²t)) e^(2πi m b/p)."""
    mp=_mp();mp.mp.dps=dps
    integer(cut,0)
    src=AffineSource(p);src.step(0,b)
    tau=_mp_time(t)
    if tau<=0 or cut>200:
        raise SourceHeatError("Positive t, bounded numerical truncation")
    return sum((mp.exp(-mp.pi*m*m/(p*p*tau))*mp.exp(2j*mp.pi*m*b/p)
                for m in range(-cut,cut+1)),mp.mpc(0))/(p*mp.sqrt(tau))


def theta(t,cut:int=15,dps:int=50):
    mp=_mp();mp.mp.dps=dps;integer(cut,1)
    tau=_mp_time(t)
    if tau<=0 or cut>200:
        raise SourceHeatError("Positive Gaussian t")
    return 1+2*sum((mp.exp(-mp.pi*tau*n*n) for n in range(1,cut+1)),mp.mpf(0))


def theta_tail_upper(t,cut:int=15,dps:int=50):
    """Rigorous analytic formula for truncating Σ_{n∈Z} e^-πt n²."""
    mp=_mp();mp.mp.dps=dps;integer(cut,1)
    tau=_mp_time(t)
    if tau<=0:
        raise SourceHeatError("Positive Gaussian t")
    return 2*mp.exp(-mp.pi*tau*(cut+1)**2)/(1-mp.exp(-mp.pi*tau*(2*cut+3)))


def completed_lambda_split(s,cut:int=15,dps:int=50):
    """Zero-independent theta/Poisson meromorphic continuation.

    Λ(s)=1/[s(s−1)]+Σ_(n>=1) [(πn²)^(-s/2) Γ(s/2,πn²)
       +(πn²)^(-(1-s)/2) Γ((1-s)/2,πn²)].
    Analytic proof uses Poisson; finite sum evaluation here only numeric.
    """
    mp=_mp();mp.mp.dps=dps;integer(cut,1)
    z=_mp_complex(s)
    if z in (0,1) or cut>200:
        raise SourceHeatError("Meromorphic completed Lambda has poles at 0,1")
    out=1/(z*(z-1))
    for n in range(1,cut+1):
        x=mp.pi*n*n
        out+=mp.power(x,-z/2)*mp.gammainc(z/2,x,mp.inf)
        out+=mp.power(x,-(1-z)/2)*mp.gammainc((1-z)/2,x,mp.inf)
    return out


def completed_lambda_standard(s,dps:int=50):
    mp=_mp();mp.mp.dps=dps;z=_mp_complex(s)
    if z in (0,1):
        raise SourceHeatError("Λ(s) has meromorphic poles")
    return mp.power(mp.pi,-z/2)*mp.gamma(z/2)*mp.zeta(z)


def completed_lambda_split_tail_upper(cut:int,dps:int=50):
    """Bound sum n>cut in Λ split for 0<=Re(s)<=1; E1 integral <= bound.

    For t>=1: ω(t)<=e^-πt/(1-e^-3πt); both powers <=1 on strip.
    For the *n*-tail use ω_(>N)(t)<= e^-πt(N+1)^2 /(1-e^-πt(2N+3)),
    both powers <=1, integrate t>=1 and bound denominator at 1.
    """
    mp=_mp();mp.mp.dps=dps;integer(cut,1)
    N=cut+1
    return 2*mp.exp(-mp.pi*N*N)/(mp.pi*N*N*(1-mp.exp(-mp.pi*(2*cut+3))))


def spectral_depth_heat(p:int,t,depth:int,weighting:str="raw_count",dps:int=50):
    mp=_mp();mp.mp.dps=dps
    integer(p,2);integer(depth,0)
    if depth>30 or weighting not in ("raw_count","level_normalized"):
        raise SourceHeatError("Invalid heat depth or source weight")
    tau=_mp_time(t)
    if tau<=0:
        raise SourceHeatError("Positive heat time needed")
    return sum(( (p**k if weighting=="raw_count" else 1)*mp.exp(-mp.pi*tau*(p**k)**2)
                for k in range(depth+1)),mp.mpf(0))


def primary_radix_factor(m:int)->tuple[int,int]|None:
    """If m=p^a with p PRIME, return (p,a); otherwise None."""
    integer(m,2)
    return prime_power_witness(m)


def prime_jets_zero_coset(radix:int,N:int)->tuple[tuple[int,int,int],...]:
    """Source-authentic Λ support in {n≡0 mod m}; NOT all composite digits."""
    integer(radix,2)
    return tuple((n,p,k) for n,p,k in prime_powers_up_to(N) if n%radix==0)


def prime_zero_coset_mellin_local(m:int,s:int):
    """Exact algebraic local Mellin multiplier, stripped of log(p).

    ∑_(n=p^k,m|n) Λ(n)n^-s = log(p)*p^(-as)/(1-p^-s)
    if m=p^a, otherwise 0.  No zero location is used.
    Returns (prime p, rational multiplier) or None (identically zero).
    """
    integer(m,2);integer(s,2)
    fac=primary_radix_factor(m)
    if fac is None:
        return None
    p,a=fac
    return p, Q(p)**(-a*s)/(1-Q(p)**(-s))


def heat_affine_pullback(p:int,b:int,n:int,t:int|Q):
    """Two numeric evaluations of h_t(pn+b)=h_(p²t)(n+b/p)."""
    mp=_mp()
    source=AffineSource(p)
    value=source.step(n,b)
    tau=_mp_time(t)
    if tau<=0:
        raise SourceHeatError("Heat time strictly positive")
    direct=mp.exp(-mp.pi*tau*value*value)
    pulled=mp.exp(-mp.pi*tau*p*p*(n+mp.mpf(b)/p)**2)
    return direct,pulled


def residue_fourier_character(p:int,r:int,t:int|Q,cut:int=18,dps:int=50):
    """DFT of p residue heat channels: Σ_b e^(-2πirb/p)C_b(t)."""
    mp=_mp();mp.mp.dps=dps
    integer(p,2);integer(r,0)
    if r>=p:
        raise SourceHeatError("Fourier residue frequency outside mod p")
    return sum((mp.exp(-2j*mp.pi*r*b/p)*coset_theta(p,b,t,cut,dps=dps)
                for b in range(p)),mp.mpc(0))


def residue_fourier_character_dual(p:int,r:int,t:int|Q,cut:int=18,dps:int=50):
    """Exact Poisson transform: t^-1/2 Σ_k exp[-π(k+r/p)²/t]."""
    mp=_mp();mp.mp.dps=dps
    integer(p,2);integer(r,0)
    if r>=p:
        raise SourceHeatError("Invalid Fourier frequency")
    tau=_mp_time(t)
    if tau<=0:
        raise SourceHeatError("Positive real heat parameter")
    return sum((mp.exp(-mp.pi*(k+mp.mpf(r)/p)**2/tau)
                for k in range(-cut,cut+1)),mp.mpf(0))/mp.sqrt(tau)


def spectral_power_mellin_factor(s,power:int,scale:int|Q=1,dps:int=50):
    """Mellin heat kernel e^(-π*c*t*n^a): Γ(s/a)(πc)^(-s/a)n^-s.

    This explicit spectral-power mutation shows Gamma(s/2) requires a=2;
    the digit algebra itself does not select quadratic Archimedean energy.
    """
    mp=_mp();mp.mp.dps=dps
    integer(power,1)
    if power>12:
        raise SourceHeatError("Declared positive integer spectral energy power")
    c=rational(scale)
    z=_mp_complex(s)
    if c<=0 or z.real<=0:
        raise SourceHeatError("Positive source scale and Re(s)>0")
    return (mp.pi*_mp_time(c))**(-z/power)*mp.gamma(z/power)


def symmetric_pascal_character(N:int,t:int|Q,u:int|Q,dps:int=50):
    """E exp(iuX_N)=cos(u sqrt(2t/N))^N for N IID symmetric SUCCs."""
    mp=_mp();mp.mp.dps=dps
    integer(N,1)
    if N>1000000:
        raise SourceHeatError("Finite experiment bound")
    time=rational(t);freq=rational(u)
    if time<0:
        raise SourceHeatError("Gaussian heat time t>=0")
    z=_mp_time(freq)*mp.sqrt(2*_mp_time(time)/N)
    return mp.cos(z)**N


def symmetric_pascal_error_certificate(N:int,t:int|Q,u:int|Q)->Q:
    """EXACT all-N bound |cos(u√(2t/N))^N-e^(-t u²)|<=4t²u⁴/(3N).

    Domain x²=2tu²/N<=1/4 ensures |x|<=1/2. Proof uses
    f=-log cos x-x²/2, f''=tan²x<=4x²; hence 0<=f<=x⁴/3.
    Other cases are not licensed for this sharp/simple bound.
    """
    integer(N,1);tt=rational(t);uu=rational(u)
    if tt<0 or 8*tt*uu*uu>N:
        raise SourceHeatError("Valid certificate requires 8t u²<=N")
    return Q(4,3)*tt*tt*uu**4/N


def symmetric_pascal_correlated_character(N:int,t:int|Q,u:int|Q,dps:int=50):
    """NEGATIVE CONTROL: all N steps share one fair latent sign (not IID)."""
    mp=_mp();mp.mp.dps=dps
    integer(N,1);tt=rational(t);uu=rational(u)
    if tt<0:
        raise SourceHeatError("Nonnegative time")
    return mp.cos(_mp_time(uu)*mp.sqrt(2*_mp_time(tt)*N))


def digit_bulk_character(p:int,N:int,t:int|Q,u:int|Q,dps:int=50):
    """IID uniform radix-p centered digit walk, variance calibrated to 2t.

    This classical CLT route works for p=6 as well as primes; no arithmetic
    prime-sourcing follows from a Gaussian bulk limit by itself.
    """
    mp=_mp();mp.mp.dps=dps
    integer(p,2);integer(N,1)
    if p>16 or N>50000:
        raise SourceHeatError("Bounded numeric bulk")
    tt=rational(t);uu=rational(u)
    if tt<0:
        raise SourceHeatError("t>=0")
    v=Q(p*p-1,12)
    step=mp.sqrt(2*_mp_time(tt)/(N*_mp_time(v)))
    center=mp.mpf(p-1)/2
    one=sum((mp.exp(1j*_mp_time(uu)*step*(b-center)) for b in range(p)),mp.mpc(0))/p
    return one**N


def one_step_pascal_heat_on_polynomial(coeff:Sequence[int|Q],t:int|Q,N:int)->tuple[Q,...]:
    """One IID symmetric Pascal step on P, algebraic c²=2t/N.

    A_N P = [P(x+c)+P(x-c)]/2. On polynomials all odd terms vanish,
    and even powers of c are exact rational (2t/N)^j. No square roots.
    """
    integer(N,1);tt=rational(t)
    if tt<0 or not coeff or len(coeff)>40:
        raise SourceHeatError("Finite polynomial and nonnegative time")
    out=[Q(0)]*len(coeff)
    step2=2*tt/N
    for n,a in enumerate(coeff):
        for j in range(n//2+1):
            out[n-2*j]+=rational(a)*comb(n,2*j)*step2**j
    return tuple(out)


def iterated_pascal_heat_polynomial(coeff:Sequence[int|Q],t:int|Q,N:int)->tuple[Q,...]:
    integer(N,1)
    if N>10000:
        raise SourceHeatError("Finite resource cap")
    state=tuple(rational(c) for c in coeff)
    for _ in range(N):
        state=one_step_pascal_heat_on_polynomial(state,t,N)
    return state


def fourth_moment_pascal_limit(N:int,t:int|Q)->tuple[Q,Q,Q]:
    """Exact moment identity for x^4: 12t²-8t²/N vs Gaussian 12t².

    Based on E(Σ eps_i)^4 = N+6*C(N,2) =3N²-2N.
    Return finite moment, Gaussian moment, exact discrepancy.
    """
    integer(N,1);tt=rational(t)
    if tt<0:
        raise SourceHeatError("Nonnegative heat time")
    finite=Q(4)*tt**2*(3-Q(2,N))
    infinite=Q(12)*tt**2
    return finite,infinite,infinite-finite


def xi_from_theta(s,cut:int=15,dps:int=50):
    """Entire ξ(s)=s(s-1)Λ(s)/2 via zero-independent modular theta split.

    At s=0,1 the pole residues give ξ=1/2. Other points are evaluated
    from the positive t>=1 theta integral (upper incomplete Γ), not zeros.
    """
    mp=_mp();mp.mp.dps=dps
    z=_mp_complex(s)
    if z in (0,1):
        return mp.mpf('0.5')
    return z*(z-1)*completed_lambda_split(z,cut=cut,dps=dps)/2


def prime_mellin_heat_integral_numeric(s,N:int=30,dps:int=35):
    """Independent numerical ∫_0∞ J_N(t)t^(s/2-1)dt, Re(s)>1.

    Not a rigorous quadrature enclosure. The exact analytic identity is
    independently established in the research dossier by Tonelli/Fubini.
    """
    mp=_mp();mp.mp.dps=dps
    z=_mp_complex(s)
    if z.real<=1 or N>50:
        raise SourceHeatError("Bounded finite quadrature, Re(s)>1")
    rows=prime_powers_up_to(N)
    def integrand(t):
        h=sum((mp.log(p)*mp.exp(-mp.pi*t*n*n) for n,p,_ in rows),mp.mpf(0))
        return h*mp.power(t,z/2-1)
    return mp.quad(integrand,[0,mp.mpf('0.01'),mp.mpf('0.1'),1,mp.inf])
