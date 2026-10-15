"""Source-indexed interaction of prime-place clocks and the real theta/Mellin model.

The mathematical construction is classical (Tate / Riemann / CRT / Ramanujan):
  - exact rational place and additive-character reciprocity,
  - prime-only finite place fibers and local finite Fourier fixed vectors,
  - CRT-coupled unit sieve and its Ramanujan Fourier transform,
  - a source-derived, meromorphic theta/Mellin continuation for ANY finite
    squarefree prime-set sieve without evaluating zeta outside Re(s)>1,
  - an entire theta model xi(s) available at any complex argument,
  - uniform compact-strip *rational* truncation certificates,
  - finite cyclic Fourier clocks converging to the Gaussian integral with
    *rational* aliasing and spatial-shell error bounds.

This is a theorem/proof-calibration laboratory on declared mathematical sources,
not an experimentally authenticated observer, an algorithmic RH proof, a full
formalization of Tate's adeles, or an everywhere convergent Euler product.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, prod
from typing import Iterable, Sequence

from .prime_form_heat import prime

Q = Fraction


class PlaceModelError(ValueError):
    """Invalid source contract, place, model or analytic evaluation domain."""


def _int(n, minimum=None):
    if type(n) is not int or (minimum is not None and n < minimum):
        raise PlaceModelError("Expected an exact integer in the declared domain")
    return n


def _rational(x):
    if type(x) not in (int, Q):
        raise PlaceModelError("Only exact int/Fraction source data are allowed")
    return Q(x)


def place_primes(primes: Iterable[int]) -> tuple[int, ...]:
    seq = tuple(primes)
    if not all(type(p) is int and prime(p) for p in seq):
        raise PlaceModelError("Local Euler places require genuine prime integers")
    if tuple(sorted(set(seq))) != seq:
        raise PlaceModelError("Unique sorted prime places are required")
    return seq


def factors(n: int) -> dict[int, int]:
    _int(n, 1)
    x, ans, p = n, {}, 2
    while p * p <= x:
        while x % p == 0:
            ans[p] = ans.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        ans[x] = ans.get(x, 0) + 1
    return ans


def valuation(n: int, p: int) -> int:
    _int(n)
    if n == 0 or not prime(p):
        raise PlaceModelError("Nonzero integer and genuine prime required")
    x, count = abs(n), 0
    while x % p == 0:
        x //= p
        count += 1
    return count


def rational_place_valuations(x: int | Q) -> dict[int, int]:
    f = _rational(x)
    if not f:
        raise PlaceModelError("Nonzero rational source is required")
    a = factors(abs(f.numerator)); b = factors(f.denominator)
    return {p: a.get(p, 0) - b.get(p, 0) for p in sorted(a.keys() | b.keys())}


def product_formula_rational(x: int | Q) -> Q:
    """Exact |x|_infty * prod_p |x|_p = 1, no infinite enumeration."""
    f = _rational(x)
    v = rational_place_valuations(f)
    return abs(f) * prod((Q(p) ** (-k) for p, k in v.items()), start=Q(1))


def local_fractional_part(x: int | Q, p: int) -> Q:
    """Fractional part in Q_p/Z_p, in [0,1) via inverse unit mod p^k."""
    f = _rational(x)
    if not prime(p):
        raise PlaceModelError("The local source must be a prime place")
    if not f:
        return Q(0)
    v = valuation(f.numerator, p) - valuation(f.denominator, p)
    if v >= 0:
        return Q(0)
    a = valuation(f.numerator, p)
    b = valuation(f.denominator, p)
    k = b - a
    mod = p**k
    numer = f.numerator // p**a
    denom = f.denominator // p**b
    residue = (numer * pow(denom, -1, mod)) % mod
    return Q(residue, mod)


def additive_character_integer_defect(x: int | Q) -> int:
    """Global psi_infty(x)*prod_p psi_p(x)=1 on diagonal Q.

    With psi_infty=e^(-2pi i x), psi_p=e^(2pi i {x}_p),
    x - sum_p {x}_p is an integer for a rational diagonal x.
    """
    f = _rational(x)
    if not f:
        return 0
    d = factors(f.denominator)
    remainder = f - sum((local_fractional_part(f, p) for p in d), Q(0))
    if remainder.denominator != 1:
        raise AssertionError("The certified diagonal additive character failed")
    return remainder.numerator


def prime_unit_shell_factor(p: int, s: int, depth: int | None = None) -> Q:
    """Integral_{Q_p^x} 1_{Z_p}(x)|x|_p^s d^x x (units mass=1).

    Exact for positive INTEGER s; optional partial shell 0<=k<=depth.
    Other complex s use the proved geometric series analytically.
    """
    if not prime(p):
        raise PlaceModelError("Composite radix is not a prime local Euler factor")
    _int(s, 1)
    if depth is None:
        return Q(p**s, p**s - 1)
    _int(depth, 0)
    return sum((Q(p)**(-s*k) for k in range(depth+1)), Q(0))


def primitive_self_dual_clock(p: int, depth: int, frequency: int) -> int:
    """Unit-ball projector on p^(-r) Z_p/p^r Z_p ≅ Z/p^(2r).

    Normalized Fourier of 1_{p^r Z/p^(2r)} equals itself: 0 or 1.
    Exact character orthogonality; composite p refused as a *place*.
    """
    if not prime(p):
        raise PlaceModelError("Non-prime labels are not independent places")
    _int(depth, 1); _int(frequency)
    if depth > 8:
        raise PlaceModelError("Bounded exact finite-clock representation")
    return int(frequency % (p**depth) == 0)


def crt_source(residues: Sequence[int], moduli: Sequence[int]) -> tuple[int, int]:
    """Construct diagonal integer observation from separately indexed local clocks."""
    if not moduli or len(residues) != len(moduli):
        raise PlaceModelError("Nonempty jointly source-indexed residue chart required")
    value, period = 0, 1
    for r, m in zip(residues, moduli):
        _int(m, 2); _int(r)
        if gcd(m, period) != 1:
            raise PlaceModelError("CRT factors must be pairwise coprime")
        k = ((r - value) * pow(period, -1, m)) % m
        value += period*k
        period *= m
    return (value % period, period)


def squarefree_modulus(primes: Sequence[int]) -> int:
    return prod(place_primes(primes), start=1)


def mobius(n: int) -> int:
    _int(n, 1)
    f=factors(n)
    return 0 if any(k>1 for k in f.values()) else (-1)**len(f)


def totient(n: int) -> int:
    _int(n, 1)
    out = n
    for p in factors(n):
        out = (out // p) * (p-1)
    return out


def divisors(n: int) -> tuple[int, ...]:
    _int(n, 1)
    d=[]
    for k in range(1, isqrt(n)+1):
        if n%k == 0:
            d.append(k)
            if n//k!=k:
                d.append(n//k)
    return tuple(sorted(d))


def ramanujan_exact(n: int, k: int) -> int:
    """The finite unit-residue Fourier phase sum, exactly via Mobius."""
    _int(n, 1);_int(k)
    return sum(d*mobius(n//d) for d in divisors(gcd(n,abs(k))))


def ramanujan_crt_factorized(primes: Sequence[int], k: int) -> int:
    ps=place_primes(primes)
    _int(k)
    return prod((p-1 if k%p == 0 else -1 for p in ps),start=1)


def unit_residue_labels(n: int) -> tuple[int,...]:
    _int(n, 1)
    return tuple(r for r in range(n) if gcd(r,n)==1)


def source_unit_sieve(n: int, upper: int) -> tuple[int,...]:
    """Actual mathematical original-source integers (not a new physical sensor)."""
    _int(n, 1);_int(upper,1)
    return tuple(k for k in range(1,upper+1) if gcd(k,n)==1)


def finite_sieved_dirichlet(n: int, sigma: int, upper: int) -> Q:
    _int(sigma, 2)
    return sum((Q(k)**(-sigma) for k in source_unit_sieve(n,upper)),Q(0))


def symmetric_model_mutant(samples: Sequence[Q|int], s: Q|int) -> Q:
    """Nonzero symmetric entire-polynomial mutant invisible at named finite samples.

    This IS NOT an analytic continuation of the authentic Euler germ: it shows
    functional symmetry plus finitely many probes do not certify that germ.
    """
    z=_rational(s)
    if not samples:
        raise PlaceModelError("Explicit finite sampled probes required")
    ans=Q(1)
    for t in samples:
        a=_rational(t)
        ans *= (z-a)*(z-(1-a))
    return ans


def _mp(dps:int):
    _int(dps, 20)
    if dps>160:
        raise PlaceModelError("Numeric laboratory uses bounded precision")
    try:
        import mpmath as mp
    except ImportError as exc:
        raise PlaceModelError("mpmath optional research dependency required") from exc
    mp.mp.dps=dps
    return mp


def theta_units_spatial(m: int, t: Q|int|float, cutoff: int, dps:int=50):
    """Theta over n ≠0 coprime to m, a REAL source projection."""
    _int(m, 1); _int(cutoff,1)
    mp=_mp(dps);tt=mp.mpf(str(t))
    if tt<=0:
        raise PlaceModelError("Positive heat parameter required")
    return 2*sum((mp.exp(-mp.pi*n*n*tt) for n in range(1,cutoff+1) if gcd(n,m)==1),mp.mpf(0))


def theta_units_spectral(m: int, t: Q|int|float, cutoff: int, dps:int=50):
    """Dual Poisson/Ramanujan series for a CRT-coupled integer source.

    Theta_m(t) = 1/(m sqrt(t)) sum_{k in Z} c_m(k)
                    exp(-pi*k*k/(m*m*t)) - 1_{m=1}.
    """
    _int(m,1);_int(cutoff,1)
    mp=_mp(dps);tt=mp.mpf(str(t))
    if tt<=0:
        raise PlaceModelError("Positive heat parameter required")
    rr=mp.mpf(totient(m))
    rr += 2*sum((ramanujan_exact(m,k)*mp.exp(-mp.pi*k*k/(m*m*tt)) for k in range(1,cutoff+1)),mp.mpf(0))
    return rr/(m*mp.sqrt(tt))-(1 if m==1 else 0)


def _incomplete_heat(mp, s, n: int):
    x=mp.pi*n*n
    return mp.power(x,-s/2)*mp.gammainc(s/2,x,mp.inf)


def _incomplete_dual(mp, s, m: int, k: int):
    x=mp.pi*k*k/(m*m)
    return mp.power(x,(s-1)/2)*mp.gammainc((1-s)/2,x,mp.inf)


def glued_completed_zeta(s, primal_cutoff:int=9, dual_cutoff:int=10, dps:int=50):
    """Completed Λ=Gamma_R ζ from theta gluing, not ζ(s) evaluation.

    Domain: C minus poles 0,1. Entire analytic continuation from a single
    original integer source, normalized Gaussian and Poisson lattice dual.
    """
    _int(primal_cutoff,1);_int(dual_cutoff,1)
    mp=_mp(dps);z=mp.mpc(s)
    if z==0 or z==1:
        raise PlaceModelError("Completed Lambda has pole at 0,1; use xi")
    return (1/(z*(z-1))
            +sum((_incomplete_heat(mp,z,n) for n in range(1,primal_cutoff+1)),mp.mpc(0))
            +sum((_incomplete_dual(mp,z,1,k) for k in range(1,dual_cutoff+1)),mp.mpc(0)))


def glued_xi(s, primal_cutoff:int=9, dual_cutoff:int=10, dps:int=50):
    """Entire ξ(s): stable even at s=0,1; zero locations never read."""
    _int(primal_cutoff,1);_int(dual_cutoff,1)
    mp=_mp(dps);z=mp.mpc(s)
    rest=(sum((_incomplete_heat(mp,z,n) for n in range(1,primal_cutoff+1)),mp.mpc(0))
          +sum((_incomplete_dual(mp,z,1,k) for k in range(1,dual_cutoff+1)),mp.mpc(0)))
    return mp.mpf('0.5')+z*(z-1)*rest/2


def glued_unit_sieve(m: int, s, primal_cutoff:int=9, dual_cutoff:int=28, dps:int=50):
    """Γ_R(s) ζ(s) ∏_{p|m}(1-p^-s), independently gluing residue and Fourier charts.

    m>=2; s any complex except genuine pole 1. Every term outside the
    explicit pole is ENTIRE in s (upper incomplete Gamma fixed x>0).
    No continuation of the Euler product is used in this evaluator.
    """
    _int(m,2);_int(primal_cutoff,1);_int(dual_cutoff,1)
    mp=_mp(dps);z=mp.mpc(s)
    if z==1:
        raise PlaceModelError("Unit sieve retains a simple pole at s=1")
    a=mp.mpf(totient(m))/(m*(z-1))
    b=sum((_incomplete_heat(mp,z,n) for n in range(1,primal_cutoff+1) if gcd(n,m)==1),mp.mpc(0))
    c=sum((ramanujan_exact(m,k)*_incomplete_dual(mp,z,m,k)/m for k in range(1,dual_cutoff+1)),mp.mpc(0))
    return a+b+c


def continuation_tail_rational(m:int, primal_cutoff:int, dual_cutoff:int, real_bound:int, power:int=24)->Q:
    """Uniform |error| bound on |Re(s)|<=real_bound; exact rational.

    Uses pi>3, sum_{n>K} e^{-a n²t} <=e^{-a K²t}/(2a K t),
    log t<=t-1, and exp(-x)<=(1+x/L)^(-L). The result holds
    independently of Im(s), including far outside Euler's domain.
    """
    _int(m,1);_int(primal_cutoff,1);_int(dual_cutoff,1)
    _int(real_bound,0);_int(power,1)
    c1=max(Q(real_bound,2)-1,Q(0))
    c2=max(Q(real_bound-1,2),Q(0))
    ap=Q(3)*primal_cutoff**2
    ad=Q(3, m*m)*dual_cutoff**2
    if ap<=c1 or ad<=c2:
        raise PlaceModelError("Cutoff too small for requested spectral/compact strip")
    def exponential_upper(x:Q)->Q:
        return (1+x/power)**(-power)
    first=(Q(1)/(2*3*primal_cutoff*(ap-c1)))*exponential_upper(ap)
    second=(Q(totient(m),1)/(2*m*Q(3,m*m)*dual_cutoff*(ad-c2)))*exponential_upper(ad)
    return first+second


def truncated_omega_zero_leading(primes:Sequence[int]) -> dict:
    """From theta residue Λ(s)= -1/s + O(1) at s=0 and genuine factors.

    Λ(s) prod_p(1-p^-s) = -(prod_p log p)*s^(r-1)+O(s^r).
    Returns order and primes; coefficient remains an explicit exact log expression.
    """
    ps=place_primes(primes)
    if not ps:
        raise PlaceModelError("This cancellation applies to at least one local place")
    return {"vanishing_order_at_0":len(ps)-1,
            "leading_coefficient":"-"+"*".join("log(%d)"%p for p in ps),
            "source_primes":list(ps)}


def fake_composite_source_contradiction(radix:int)->dict:
    """Fake one-place exclusion n divisible by radix vs genuine union of its primes."""
    _int(radix,2)
    fs=factors(radix)
    if len(fs)<2:
        raise PlaceModelError("Need a composite containing >=2 distinct primes")
    p=min(fs)
    return {"fake_radix":radix,"genuine_primes":list(fs),
            "counterexample_integer":p,
            "fake_excludes_integer":p%radix==0,
            "genuine_excludes_integer":gcd(p,radix)>1,
            "one_fake_log_leading":"-log(%d)"%radix,
            "genuine_zero_order_at_0":len(fs)-1}


@dataclass(frozen=True)
class SourceIndexedPlaceAtlas:
    """A model *contract*, not source authentication or a new sensor.

    Only primes are independent finite places of Q. The real Gaussian is
    retained exactly once and is shared by every finite stage. Epoch/basis
    identity is required for lawful finite-place joins.
    """
    source_id: str
    epoch: int
    basis: str
    primes: tuple[int, ...] = ()
    real_heat_scale: Q = Q(1)
    additive_orientation: int = 1

    def __post_init__(self):
        if not self.source_id or not self.basis:
            raise PlaceModelError("An original mathematical source and basis are required")
        _int(self.epoch, 0)
        place_primes(self.primes)
        if _rational(self.real_heat_scale) <= 0:
            raise PlaceModelError("Positive real Gaussian scale required")
        if self.additive_orientation not in (-1, 1):
            raise PlaceModelError("Additive Fourier orientation must be declared")

    def join(self, other: 'SourceIndexedPlaceAtlas') -> 'SourceIndexedPlaceAtlas':
        if (self.source_id!=other.source_id or self.epoch!=other.epoch or
            self.basis!=other.basis or self.real_heat_scale!=other.real_heat_scale or
            self.additive_orientation!=other.additive_orientation):
            raise PlaceModelError("Cross-model source/epoch/Haar/Fourier comparison unlicensed")
        if set(self.primes)&set(other.primes):
            raise PlaceModelError("Duplicating the same prime is not a new place")
        return SourceIndexedPlaceAtlas(self.source_id,self.epoch,self.basis,
                                       tuple(sorted(self.primes+other.primes)),
                                       self.real_heat_scale,self.additive_orientation)

    @property
    def sieve_modulus(self):
        return squarefree_modulus(self.primes)


def theta_refinement_residual(m:int,p:int,t,cutoff:int=25,dps:int=50):
    """Theta_{mp}(t)=Theta_m(t)-Theta_m(p^2t), p prime and p∤m.

    This is a REAL finite source-model interaction, valid for all t>0,
    not an Euler product continued into the critical strip.
    """
    _int(m,1)
    if not prime(p) or m%p==0:
        raise PlaceModelError("New independent prime must not already divide sieve")
    lhs=theta_units_spatial(m*p,t,cutoff,dps)
    rhs=theta_units_spatial(m,t,cutoff,dps)
    # The second theta needs original up to cutoff/p to model n=pq correctly:
    # using q up to cutoff is harmless for the infinite identity but introduces
    # finite truncation mismatch; compare on same real-state finite window.
    mp=_mp(dps);tt=mp.mpf(str(t))
    removed=2*sum((mp.exp(-mp.pi*n*n*tt) for n in range(p,cutoff+1,p) if gcd(n//p,m)==1),mp.mpf(0))
    return lhs-(rhs-removed)


def model_interaction_mellin_residual(m:int,p:int,s,cutoff:int=10,spectral_cutoff:int=65,dps:int=55):
    """Directly compare separately built meromorphic continuation charts."""
    _int(m,1)
    if not prime(p) or m%p==0:
        raise PlaceModelError("Distinct genuine prime required for model refinement")
    mp=_mp(dps);z=mp.mpc(s)
    if z==0 or z==1:
        raise PlaceModelError("Use limit theorem at poles/cancellation, not raw division")
    a=glued_unit_sieve(m*p,z,cutoff,spectral_cutoff,dps)
    b=(glued_completed_zeta(z,cutoff,spectral_cutoff,dps) if m==1
       else glued_unit_sieve(m,z,cutoff,spectral_cutoff,dps))
    return a-(1-mp.power(p,-z))*b


def two_prime_cube_membership(m:int,p:int,q:int,n:int)->int:
    """Exact mixed difference on admissible original integer n.

    (I - projector divisible by p)(I - projector divisible by q)
    applied to the m-unit source characteristic function.
    """
    _int(m,1);_int(n,1)
    if not prime(p) or not prime(q) or p==q or m%p==0 or m%q==0:
        raise PlaceModelError("Two independent fresh prime places required")
    base=int(gcd(n,m)==1)
    return base - base*int(n%p==0) - base*int(n%q==0)+base*int(n%(p*q)==0)


def theta_unit_sieve_mobius(m:int,t,cutoff:int=30,dps:int=50):
    """Independent inclusion-exclusion of the same original integer lattice."""
    _int(m,1);_int(cutoff,1)
    mp=_mp(dps);tt=mp.mpf(str(t))
    base=mp.mpf(0)
    for d in divisors(m):
        mu=mobius(d)
        base+=mu*2*sum((mp.exp(-mp.pi*(d*k)**2*tt) for k in range(1,cutoff//d+1)),mp.mpf(0))
    return base


def finite_sieve_source_zero_prediction(primes:Sequence[int]):
    """Exact symbolic 0-boundary zero order; no zeta evaluation."""
    ps=place_primes(primes)
    if not ps:
        return {"at_s_zero":"pole", "order":-1,"residue":-1}
    return {"at_s_zero":"nonzero" if len(ps)==1 else "zero",
            "order":len(ps)-1,
            "leading":"-"+"*".join(f"log({p})" for p in ps)}


def twisted_reflection_defect(m:int,s,primal_cutoff:int=10,dual_cutoff:int=70,dps:int=55):
    """Meromorphic finite-place-depleted functional equation (no zero division):

    Λ_m(1-s) prod_(p|m)(1-p^-s) ==
    Λ_m(s)   prod_(p|m)(1-p^(s-1)).

    NOT generally Λ_m(s)=Λ_m(1-s). Non-eigenvector finite model projection
    needs explicit source-place correction to transport across the center.
    """
    _int(m,2)
    mp=_mp(dps);z=mp.mpc(s)
    if z==0 or z==1:
        raise PlaceModelError("Cross-multiplied endpoint limits need separate treatment")
    forward=glued_unit_sieve(m,z,primal_cutoff,dual_cutoff,dps)
    reflected=glued_unit_sieve(m,1-z,primal_cutoff,dual_cutoff,dps)
    local=tuple(factors(m))
    return (reflected*prod((1-mp.power(p,-z) for p in local),start=mp.mpc(1))
            -forward*prod((1-mp.power(p,z-1) for p in local),start=mp.mpc(1)))


def finite_clock_gaussian_fourier(m:int,t:int|Q,resolution:int,k:int,
                                  spatial_shells:int=7,dps:int=55):
    """One *finite* SUCC cyclic observer's Gaussian Fourier coefficient.

    Carrier Z/(mR)Z, observed positions j/R, and a source-derived Gaussian
    periodization sum_(ell=-H)^H exp(-pi*t*(m*ell+j/R)^2). The normalized DFT
    is finite, unlike the target analytic Fourier integral.
    """
    _int(m,1);_int(resolution,1);_int(k);_int(spatial_shells,2)
    tt=_rational(t)
    if tt<=0 or m*resolution>2500 or spatial_shells>20:
        raise PlaceModelError("Positive rational heat, bounded finite cyclic observer")
    N=m*resolution
    if abs(k)*2>N:
        raise PlaceModelError("Use a frequency inside the Nyquist observational window")
    mp=_mp(dps);time=mp.mpf(tt.numerator)/tt.denominator
    acc=mp.mpc(0)
    for j in range(N):
        x=mp.mpf(j)/resolution
        state=sum((mp.exp(-mp.pi*time*(m*ell+x)**2)
                   for ell in range(-spatial_shells,spatial_shells+1)),mp.mpf(0))
        acc+=state*mp.exp(-2j*mp.pi*k*j/N)
    return acc/N


def analytic_gaussian_fourier(m:int,t:int|Q,k:int,dps:int=55):
    """Fourier integral c_k=(m sqrt(t))^-1 exp(-pi*k²/(m²t))."""
    _int(m,1);_int(k)
    tt=_rational(t)
    if tt<=0:
        raise PlaceModelError("Positive rational Gaussian source")
    mp=_mp(dps);time=mp.mpf(tt.numerator)/tt.denominator
    return mp.exp(-mp.pi*k*k/(m*m*time))/(m*mp.sqrt(time))


def finite_clock_gaussian_rational_bound(m:int,t:int|Q,resolution:int,k:int,
                                         spatial_shells:int=7,power:int=24)->Q:
    """Exact rational error for finite sampled DFT to Gaussian Fourier.

    Let N=mR and |k|<=N/2. Fourier alias frequencies k+l*N have
    Gaussian coefficients exp(-pi*(k+l*N)^2/(m²t))/(m sqrt(t)). Their
    tail is bounded by a geometric Gaussian majorant. The truncated
    periodization omits spatial tails ell>H, bounded independently.

    Uses pi>3, exp(-x)<=(1+x/L)^(-L), 1/sqrt(t)<=max(1,1/t).
    Thus the numerical c_k is within returned exact Fraction of the
    classical Gaussian Fourier integral (roundoff excluded).
    """
    _int(m,1);_int(resolution,1);_int(k);_int(spatial_shells,2);_int(power,1)
    tt=_rational(t)
    if tt<=0 or 2*abs(k)>m*resolution:
        raise PlaceModelError("Positive rational t and non-aliased frequency needed")
    N=m*resolution
    lower=Q(3)*(N-abs(k))**2/(m*m*tt)
    period=Q(3)*resolution*resolution/tt
    e_alias=(Q(2,m)*max(Q(1),1/tt)*(1+lower/power)**(-power)
             *(1+1/period))
    x=Q(3)*tt*m*m*(spatial_shells-1)**2
    e_spatial=(1+x/power)**(-power)/(3*tt*m*m*(spatial_shells-1))
    return e_alias+e_spatial
