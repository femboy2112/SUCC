"""Source passports, exact nested projections, and forced coherence gaps.

The complete-period identity is inherited from MP-04, not a new normality
theorem. New finite instruments retain its integer lift and prove the
three orthogonal sectors exactly in Q[Q/Z]. The forced gap tends to ZERO;
it excludes perfect coherence, not asymptotic nonzero resonance.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, lcm

from .bbp_source_memory import forcing
from .bbp_prime_window_projection import window_parameters, circular_distance
from .bbp_cyclotomic_birth import p_primary_phase
from .succ_internal_matrix_walk import PhasePoly


def _integer(x, minimum=None):
    if type(x) is not int or (minimum is not None and x < minimum):
        raise ValueError("ordinary integer in the declared domain required")
    return x


@dataclass(frozen=True)
class SourcePassport:
    p: int
    m: int
    n0: int
    delta: int
    order: int
    h: int
    prefix: tuple[Q, ...]
    primary: tuple[Q, ...]
    complement: tuple[Q, ...]
    source: str = "original-four-pole-BBP; U0=0; unwrapped rational lift"

    @property
    def states(self):
        return self.prefix[self.n0:]

    def validate(self):
        """Recompute source law and boundary; a label never authenticates data."""
        _integer(self.h)
        if not self.h:
            raise ValueError("nonzero Fourier frequency required")
        m, order, delta, _ = window_parameters(self.p)
        if (self.m, self.n0, self.delta, self.order) != (m, m+1, delta, order):
            raise ValueError("forged prime-window metadata")
        if len(self.prefix) != 4*m+1 or self.prefix[0] != 0:
            raise ValueError("authentic zero-initial full prefix required")
        if any(type(x) is not Q for x in self.prefix+self.primary+self.complement):
            raise ValueError("exact Fraction source coordinates required")
        for n in range(1, len(self.prefix)):
            if self.prefix[n] != 16*self.prefix[n-1]+forcing(n):
                raise ValueError("changed original source or integer lift")
            if self.prefix[n].denominator % 2 == 0:
                raise ValueError("original odd conductor lost")
        if len(self.primary) != delta or len(self.complement) != delta:
            raise ValueError("incomplete prime window")
        for t, (state, a, w) in enumerate(zip(self.states, self.primary, self.complement)):
            if a != Q(4*pow(16, t, self.p) % self.p, self.p):
                raise ValueError("changed p-primary history")
            if p_primary_phase(state, self.p) != a*self.p:
                raise ValueError("primary extraction disagrees with original lift")
            if not 0 <= w < 1 or w.denominator % self.p == 0 or (state-a-w) % 1:
                raise ValueError("invalid p-free complementary source")
        return True


def source_passport(p, h=1):
    _integer(h)
    if h == 0:
        raise ValueError("nonzero Fourier frequency required")
    m, order, delta, _ = window_parameters(p)
    prefix = [Q()]
    for n in range(1, 4*m+1):
        prefix.append(16*prefix[-1]+forcing(n))
    primary = tuple(Q(4*pow(16, t, p) % p, p) for t in range(delta))
    complement = tuple((prefix[m+1+t]-a) % 1 for t, a in enumerate(primary))
    passport = SourcePassport(p, m, m+1, delta, order, h, tuple(prefix), primary, complement)
    passport.validate()
    return passport


def project_period(values, period):
    """Real symmetric conditional expectation on t mod period; period|N."""
    values = tuple(values)
    _integer(period, 1)
    if not values or len(values) % period:
        raise ValueError("synchronized nonempty finite window required")
    if any(type(v) is not PhasePoly for v in values):
        raise ValueError("formal rational character polynomials required")
    repeats = len(values)//period
    means = tuple(sum(values[r::period], PhasePoly.zero())/repeats for r in range(period))
    return tuple(means[t % period] for t in range(len(values)))


def pairing(first, second, hermitian=False):
    first, second = tuple(first), tuple(second)
    if not first or len(first) != len(second):
        raise ValueError("equal nonempty vectors required")
    return sum(((a.star() if hermitian else a)*b for a, b in zip(first, second)), PhasePoly.zero())/len(first)


def projection_certificate(passport, d=1):
    """v=Q_g v+(Q_L-Q_g)v+(I-Q_L)v, g=gcd(d,L).

    All three sectors are pairwise orthogonal. The last is invisible to
    the p-clock, the first has inherited BGK control under its hypotheses,
    and the middle carries the selected signed interaction J_d=J_g. Its energy
    upper bound improves the full PSC dispersion, but its decay is OPEN.
    """
    passport.validate()
    D, L, h = passport.delta, passport.order, passport.h
    _integer(d, 1)
    if D % d:
        raise ValueError("d must divide the complete prime window")
    R, g = lcm(d, L), gcd(d, L)
    u = tuple(PhasePoly.monomial(h*a) for a in passport.primary)
    v = tuple(PhasePoly.monomial(h*w) for w in passport.complement)
    low = project_period(v, g)
    retained = project_period(v, L)
    resonant = tuple(a-b for a, b in zip(retained, low))
    invisible = tuple(a-b for a, b in zip(v, retained))
    low_u = project_period(u, g)
    full = pairing(u, v)
    low_sum = pairing(low_u, low)
    high_sum = pairing(u, resonant)
    zero = PhasePoly.zero()
    if project_period(u, L) != u or pairing(u, invisible) != zero:
        raise AssertionError("prime-period invisibility failed")
    if project_period(u, d) != low_u:
        raise AssertionError("gcd collapse of the local clock failed")
    if project_period(project_period(v, d), L) != low:
        raise AssertionError("commuting gcd projections failed")
    if low_sum != pairing(project_period(u, d), project_period(v, d)):
        raise AssertionError("original PSC low term differs from compressed low term")
    if full != low_sum+high_sum:
        raise AssertionError("signed source decomposition failed")
    sectors = (low, resonant, invisible)
    for i in range(3):
        for j in range(i+1, 3):
            if pairing(sectors[i], sectors[j], True) != zero:
                raise AssertionError("conditional expectation orthogonality failed")
    energies = tuple(pairing(a, a, True) for a in sectors)
    if sum(energies, zero) != PhasePoly.one():
        raise AssertionError("exact source Pythagoras failed")
    clock_high = tuple(a-b for a, b in zip(u, low_u))
    return {"period": L, "low_period": g, "coset_period": R,
            "suborder": L//g, "repeats": D//L, "coset_repeats": D//R,
            "compressed": retained[:L],
            "full": full, "low": low_sum, "interaction": high_sum,
            "invisible_pairing": zero, "energies": energies,
            "clock_high_energy": pairing(clock_high, clock_high, True),
            "bound_status": "|J|^2 <= clock_high_energy * resonant_energy; no decay asserted"}


def forced_coherence_gap(p, h=1):
    """Exact lower bound on 1-|mean e(h X_n)| for ANY initial state.

    X has the authentic BBP forcing on n=m+1,...,4m, D=3m.
    The bound is 8/(289 D(D-1)) times the sum of squared circular
    distances between its D-1 forcing phases. It can vanish for finite
    p/h aliases. For fixed h and growing m it is of order m^-4.
    """
    _integer(h)
    if not h:
        raise ValueError("nonzero Fourier frequency required")
    m, _, D, _ = window_parameters(p)
    phases = tuple(h*forcing(n) for n in range(m+2, 4*m+1))
    squares = sum((circular_distance(a-b)**2 for i, a in enumerate(phases)
                   for b in phases[i+1:]), Q())
    return Q(8, 289*D*(D-1))*squares


def uniform_coherence_gap_floor(p, h=1):
    """Explicit h²/(1331712 m⁴) floor when m>=11 and m²>=|h|.

    Paper proof uses m early and m late forcing samples and the existing
    all-n source inequality from IMW-04. No complex numerical evaluation.
    """
    _integer(h)
    m, _, _, _ = window_parameters(p)
    if h == 0 or m < 11 or m*m < abs(h):
        raise ValueError("requires h!=0, m>=11, m²>=|h|")
    return Q(h*h, 1331712*m**4)
