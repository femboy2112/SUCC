"""Cyclotomic SUCC origin-frame/twirl calculus, source-typed to BBP pi.

All structural oracles are exact integers/Fractions. The phase-energy identity
is proved algebraically in the paired research dossier; finite root-of-unity
DFT samples are symbolic and do not falsely imply pi normality.

Model separation: x in R/Z, coordinate-chart origin a, rational origin grid
a/q, actual base-16 forced-BBP sequence, and generic Fourier coefficients.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as Q
from math import gcd, lcm, comb

from .pi_source_genesis import forced_states, lag_transport_budget


def _nat(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"expected integer >= {minimum}")
    return value


def _integer(value: int) -> int:
    if type(value) is not int:
        raise ValueError("integer required")
    return value


def _base(base: int) -> int:
    return _nat(base, 2)


def divisors(n: int) -> tuple[int, ...]:
    _nat(n, 1)
    return tuple(j for j in range(1, n + 1) if n % j == 0)


@lru_cache(None)
def cyclotomic_value(base: int, index: int) -> int:
    """Phi_index(base) by exact divisor recursion: no polynomial float roots."""
    _base(base)
    _nat(index, 1)
    value = base**index - 1
    for d in divisors(index):
        if d != index:
            v = cyclotomic_value(base, d)
            if value % v:
                raise ArithmeticError("cyclotomic divisibility invariant violated")
            value //= v
    return value


def multiplicative_order(base: int, modulus: int) -> int:
    """Order of base in (Z/modulus Z)^*, not a heuristic time bound."""
    _base(base); _nat(modulus, 2)
    if gcd(base, modulus) != 1:
        raise ValueError("base must be invertible modulo clock modulus")
    term = 1
    for depth in range(1, modulus + 1):
        term = term * base % modulus
        if term == 1:
            return depth
    raise ArithmeticError("finite clock order contradiction")


def least_clock_modulus(base: int, period: int, maximum: int = 10000) -> int:
    """Smallest q<=maximum with order_q(base)=period; strict bounded search."""
    _base(base); _nat(period, 1); _nat(maximum, 2)
    for q in range(2, maximum + 1):
        if gcd(base, q) == 1 and pow(base, period, q) == 1:
            if all(pow(base, d, q) != 1 for d in divisors(period) if d != period):
                return q
    raise ValueError("no clock of the requested order within supplied limit")


def effective_frame_period(base: int, modulus: int, h: int) -> int:
    """Time class after Fourier aliasing h modulo q; h=0 has period 1."""
    _base(base); _nat(modulus, 2); _integer(h)
    reduced = modulus // gcd(modulus, abs(h))
    return 1 if reduced == 1 else multiplicative_order(base, reduced)


def gauge_chart_step(base: int, chart_origin: Q, coordinate: Q) -> Q:
    """R_-a T_b R_a coordinate: b*z+(b-1)*a (mod 1)."""
    _base(base)
    a,z = Q(chart_origin),Q(coordinate)
    return (base*z+(base-1)*a) % 1


def literal_chart_symmetry(base: int, chart_origin: Q) -> bool:
    """Same unmodified x->b*x law in both charts iff (b-1)*a=0 mod 1."""
    _base(base)
    return ((base-1)*Q(chart_origin)) % 1 == 0


def relative_path(base: int, first: Q, second: Q, time: int) -> Q:
    """Difference of two actual initial points, NOT change of coordinates."""
    _base(base); _nat(time)
    return (pow(base, time)*(Q(first)-Q(second))) % 1


def arc_distance(x: Q) -> Q:
    """A circle geodesic distance, <=1/2; not an unwrapped Lyapunov bound."""
    f=Q(x)%1
    return min(f,1-f)


def cyclotomic_frame_character(base: int, modulus: int,
                               h: int, time: int) -> int:
    """Exponent of zeta_modulus in e(h*b^time*a/modulus)."""
    _base(base); _nat(modulus, 2); _integer(h); _nat(time)
    return h*pow(base,time,modulus) % modulus


def twirl_entry(base: int, modulus: int, h: int, i: int, j: int) -> int:
    """Exact cyclic-origin average of a root-of-unity difference."""
    _nat(i); _nat(j)
    return int((cyclotomic_frame_character(base,modulus,h,i)
                -cyclotomic_frame_character(base,modulus,h,j))%modulus==0)


def twirl_mask(base: int, modulus: int, h: int, length: int
              ) -> tuple[tuple[int,...],...]:
    _nat(length)
    return tuple(tuple(twirl_entry(base,modulus,h,i,j)
                       for j in range(length)) for i in range(length))


def twirl_matrix(matrix, base: int, modulus: int, h: int):
    """Exact CP conditional expectation on entries; matrix may be rational."""
    rows=tuple(tuple(row) for row in matrix)
    n=len(rows)
    if any(len(row)!=n for row in rows):
        raise ValueError("square matrix required")
    mask=twirl_mask(base,modulus,h,n)
    return tuple(tuple(mask[i][j]*rows[i][j] for j in range(n))
                 for i in range(n))


def fusion_mask(base: int, q1: int, q2: int,
                h: int, length: int) -> bool:
    """E_q1 E_q2 = E_lcm(q1,q2) exactly (CRT if q1,q2 are coprime)."""
    first=twirl_mask(base,q1,h,length)
    second=twirl_mask(base,q2,h,length)
    fused=twirl_mask(base,lcm(q1,q2),h,length)
    return all(first[i][j]*second[i][j]==fused[i][j]
               for i in range(length) for j in range(length))


def period_class_sizes(length: int, period: int) -> tuple[int,...]:
    _nat(length); _nat(period,1)
    quo,rem=divmod(length,period)
    return tuple(quo+int(r<rem) for r in range(period))


def lag_index_pairs(length: int, period: int, lag_multiple: int
                    ) -> tuple[tuple[int,int],...]:
    """Exact phase-character terms for C_(lag_multiple*period)."""
    _nat(length); _nat(period,1); _nat(lag_multiple,1)
    lag=period*lag_multiple
    return tuple((j,j+lag) for j in range(max(length-lag,0)))


def harmonic_depth(length: int, period: int) -> int:
    """Max Laurent degree L=floor((N-1)/period), or zero for N=0."""
    _nat(length); _nat(period,1)
    return 0 if length==0 else (length-1)//period


def phase_modulation_samples(length: int, period: int) -> int:
    """Smallest universal alias-free DFT size 2L+1 for +/-L Fourier modes."""
    return 2*harmonic_depth(length,period)+1


def positive_energy_signature(length: int, period: int, h: int = 1) -> dict:
    """Exact Haar first/second moments (ONLY for nonzero Fourier h).

    This theorem averages over an independent Haar-random source x, NOT the
    rational origin-grid samples at one fixed source, and says nothing about pi.
    """
    _integer(h)
    if h==0:
        raise ValueError("Haar-variance formula requires h != 0")
    ns=period_class_sizes(length,period)
    pairs=sum(comb(n,2) for n in ns)
    fixed=sum(n*n for n in ns)
    return {
        "class_sizes":ns,
        "haar_mean":length,
        "haar_variance":2*pairs,
        "pairs":pairs,
        "fixed_point_energy":fixed,
        "maximum_energy":fixed,
        "harmonic_depth":harmonic_depth(length,period),
        "dft_samples":phase_modulation_samples(length,period),
    }


def direct_symbolic_lag_terms(length: int, period: int, ell: int
                             ) -> tuple[tuple[int,int],...]:
    """Positive Laurent exponent ell in root-grid twirled packet energy.

    Variables v_j are arbitrary unit complex phases; tuples (j,k) mean
    v_j*conjugate(v_k), preserving the SIGNED cross term exactly.
    """
    _nat(length); _nat(period,1); _nat(ell)
    if ell==0:
        return tuple((j,j) for j in range(length))
    return tuple((j+ell*period,j)
                 for j in range(max(length-ell*period,0)))


def twirled_laurent_terms(length: int, period: int
                         ) -> dict[int,tuple[tuple[int,int],...]]:
    """Symbolic exact positive-energy Laurent polynomial coefficient map."""
    _nat(length); _nat(period,1)
    L=harmonic_depth(length,period)
    positive={ell:direct_symbolic_lag_terms(length,period,ell)
              for ell in range(L+1)}
    negative={-ell:tuple((k,j) for j,k in positive[ell])
              for ell in range(1,L+1)}
    return {**negative,**positive}


def discrete_fourier_probe(length: int, period: int, ell: int,
                           sample_count: int | None = None
                           ) -> tuple[tuple[int,int],...]:
    """Exactly recover Laurent coefficient via root-of-unity DFT.

    Verifies 2L+1 alias separation, then collects all pairs whose Laurent
    phase exponent is congruent to ell modulo the sample count.
    """
    _nat(length);_nat(period,1)
    L=harmonic_depth(length,period)
    _nat(ell)
    if ell>L:
        raise ValueError("requested lag exceeds the observed packet")
    k=phase_modulation_samples(length,period) if sample_count is None else _nat(sample_count,1)
    if k<2*L+1:
        raise ValueError("temporal DFT could alias positive and negative lags")
    terms=twirled_laurent_terms(length,period)
    return tuple(pair for power,pairs in terms.items()
                 if (power-ell)%k==0 for pair in pairs)


def forced_lag_rational_phases(length: int, period: int, ell: int,
                              h: int=1) -> tuple[Q,...]:
    """Full signed phase inputs for actual BBP rational SUCC forcing."""
    _nat(length); _nat(period,1); _nat(ell,1); _integer(h)
    lag=ell*period
    if lag>=length:
        return ()
    y=forced_states(length)
    return tuple((h*(y[j+lag+1]-y[j+1]))%1 for j in range(length-lag))


def bbp_signed_lag_budget(length: int, period: int,
                          ell: int, h: int=1) -> Q:
    """Rational absolute C_(ell*d)(pi)-C_(ell*d)(BBP forced) upper bound."""
    _nat(length); _nat(period,1); _nat(ell,1); _integer(h)
    lag=ell*period
    if lag>=length:
        return Q()
    return lag_transport_budget(h,1,length-lag,lag)


def bbp_energy_budget(length: int, period: int, h: int=1) -> Q:
    """Rational all-horizon bound on |E(pi)-E(BBP forced)|.

    Energy=N+2*Re sum_{ell>=1} C_(ell*period). The signed-lag
    source transport is uniform in the actual cyclotomic lag.
    """
    _nat(length); _nat(period,1); _integer(h)
    return 2*sum((bbp_signed_lag_budget(length,period,ell,h)
                  for ell in range(1,harmonic_depth(length,period)+1)),Q())


def mobius(n: int) -> int:
    """Integer Moebius function by genuine prime divisors."""
    _nat(n,1)
    value=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p; value=-value
            if n%p==0:
                return 0
            while n%p==0:
                n//=p
        p+=1
    return -value if n>1 else value


def exact_period_point_count(base: int, period: int) -> int:
    """Points of EXACT T_base period d in R/Z (classical Mobius inversion)."""
    _base(base); _nat(period,1)
    return sum(mobius(period//e)*(base**e-1) for e in divisors(period))


def cyclic_necklace_count(base: int, period: int) -> int:
    """Primitive length-d periodic radix necklaces, excluding fixed 0 nuance."""
    n=exact_period_point_count(base,period)
    if n%period:
        raise ArithmeticError("period cycle count not integral")
    return n//period


def certified_origin_energy_interval(h: int, length: int, period: int,
                                     source: str = "bbp") -> tuple[Q,Q]:
    """Outward rational finite energy enclosure from authenticated pi oracles.

    E=N+2*Re sum_{ell>=1} C_(ell*period)(N).
    source='bbp' uses the genuine BBP pi interval, 'machin' an independent
    arctangent interval, and 'forced' the rational BBP SUCC shadow.
    No orbit equidistribution or asymptotic claim is attached.
    """
    from .pi_source_genesis import correlation_interval
    _integer(h); _nat(length); _nat(period,1)
    if source not in ("bbp","machin","forced"):
        raise ValueError("unrecognized authenticated finite source")
    if h==0:
        fixed=positive_energy_signature(length,period,1)["fixed_point_energy"]
        return Q(fixed),Q(fixed)
    if length==0:
        return Q(),Q()
    lo=hi=Q(length)
    for ell in range(1,harmonic_depth(length,period)+1):
        lag=ell*period
        box=correlation_interval(h,length,lag,source=source)
        lo+=2*box.real_low
        hi+=2*box.real_high
    return max(Q(),lo),hi
