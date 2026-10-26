"""Typed value/operator duality and exact BBP inverse-branch Fourier firewall.

Stacked research on PR #310; the original four-pole BBP forcing is IMPORTED,
never modified. Koopman and Perron operators are standard classical dynamics.
Curry/uncurry reuses the repo's finite-set map type, not a second category.

The exact 16-branch Fourier annihilation is for UNIFORM inverse sampling.
The original zero-seeded trajectory selects exactly ONE preimage at a time.
The conditional chi-squared criterion below is equivalent (with the source
shift law) to the still-OPEN selected π normality problem, not its proof.
This is NOT a physical virtual-particle interpretation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import isqrt, lcm

from .beck_chevalley_source import FiniteMap, finite_map, check_carrier
from .succ_internal_matrix_walk import authentic_r, circle


RADIX = 16


class DualityDomainError(ValueError):
    """A type, source history, categorical map or finite observation is illegal."""


def exact_int(x, name, low=None, high=None):
    if type(x) is not int or (low is not None and x < low) or (high is not None and x > high):
        raise DualityDomainError(f"{name} requires a bounded exact integer")
    return x


def fraction(x):
    if type(x) is int or isinstance(x, Q):
        return Q(x)
    raise DualityDomainError("exact integer/Fraction required, not float or bool")


# 1. Ordinary FinSet exponential / typed Church numerals, using canonical FiniteMap.
def exponential_object(X, Y, max_functions=4096):
    X, Y = check_carrier(tuple(X)), check_carrier(tuple(Y))
    if not X or not Y or len(Y) ** len(X) > max_functions:
        raise DualityDomainError("finite exponential requires a nonempty bounded carrier")
    return tuple(product(Y, repeat=len(X)))


def evaluation_arrow(X, Y):
    X, Y = check_carrier(tuple(X)), check_carrier(tuple(Y))
    exp = exponential_object(X, Y)
    return finite_map(tuple((f, x) for f in exp for x in X), Y,
                      lambda pair: pair[0][X.index(pair[1])])


def curry_arrow(f: FiniteMap, A, X, Y):
    """Finite uncurried f:A×X→Y becomes a value of Y^X at each a."""
    A, X, Y = tuple(A), tuple(X), tuple(Y)
    if not isinstance(f, FiniteMap) or f.domain != tuple(product(A, X)) or f.codomain != Y:
        raise DualityDomainError("source/target of the arrow do not match the exponential")
    exp = exponential_object(X, Y)
    return finite_map(A, exp, lambda a: tuple(f.apply((a, x)) for x in X))


def uncurry_arrow(g: FiniteMap, A, X, Y):
    A, X, Y = tuple(A), tuple(X), tuple(Y)
    if not isinstance(g, FiniteMap) or g.domain != A or g.codomain != exponential_object(X, Y):
        raise DualityDomainError("source/target of the curried arrow do not match")
    return finite_map(tuple(product(A, X)), Y,
                      lambda ax: g.apply(ax[0])[X.index(ax[1])])


@dataclass(frozen=True)
class ChurchIterator:
    """A typed Church numeral: n is an action on a chosen endomorphism.

    This is an interface for finite actions, NOT a lambda-calculus interpreter
    and NOT an assertion that nonautonomous BBP forcing is one fixed map.
    """
    n: int

    def __post_init__(self):
        exact_int(self.n, "Church count", 0, 2000)

    def apply(self, endomap: FiniteMap, x):
        if not isinstance(endomap, FiniteMap) or endomap.domain != endomap.codomain:
            raise DualityDomainError("Church iteration requires a typed endomorphism")
        if x not in endomap.domain:
            raise DualityDomainError("initial object missing from endomorphism domain")
        for _ in range(self.n):
            x = endomap.apply(x)
        return x


# 2. Rational 16th cyclotomic field, represented by Q[zeta]/(zeta^8+1).
# Formal Q[Q/Z] must NOT be used to assert root-of-unity relations.
@dataclass(frozen=True)
class Cyclo16:
    coefficients: tuple[Q, ...]

    def __post_init__(self):
        if len(self.coefficients) != 8 or any(type(v) is not Q for v in self.coefficients):
            raise DualityDomainError("Cyclo16 needs eight exact rational coordinates")

    @classmethod
    def zero(cls):
        return cls((Q(0),) * 8)

    @classmethod
    def one(cls):
        return cls((Q(1),) + (Q(0),) * 7)

    @classmethod
    def zeta(cls, exponent):
        exact_int(exponent, "root exponent")
        e = exponent % RADIX
        a = [Q(0)] * 8
        a[e % 8] = Q(-1 if e >= 8 else 1)
        return cls(tuple(a))

    def __add__(self, other):
        if not isinstance(other, Cyclo16):
            return NotImplemented
        return Cyclo16(tuple(a + b for a, b in zip(self.coefficients, other.coefficients)))

    def __neg__(self):
        return Cyclo16(tuple(-v for v in self.coefficients))

    def __sub__(self, other):
        if not isinstance(other, Cyclo16):
            return NotImplemented
        return self + (-other)

    def __mul__(self, other):
        if type(other) is int or isinstance(other, Q):
            return Cyclo16(tuple(fraction(other)*v for v in self.coefficients))
        if not isinstance(other, Cyclo16):
            return NotImplemented
        out = [Q(0)] * 8
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                k = i + j
                out[k % 8] += (-1 if k >= 8 else 1)*a*b
        return Cyclo16(tuple(out))

    def __rmul__(self, other):
        return self * other

    def conjugate(self):
        z = Cyclo16.zero()
        for i, c in enumerate(self.coefficients):
            z = z + Cyclo16.zeta(-i)*c
        return z

    def evaluation(self):
        """Numerical diagnostic ONLY; exact source is rational coordinates."""
        import cmath
        return sum(float(c)*cmath.exp(2j*cmath.pi*i/16)
                   for i, c in enumerate(self.coefficients))


def branch_fourier(weights, frequency):
    """Exact value sum_{j=0}^15 weights_j*zeta16^(frequency*j)."""
    exact_int(frequency, "frequency")
    if type(weights) not in (tuple, list) or len(weights) != RADIX:
        raise DualityDomainError("one rational weight for each of 16 branches")
    out = Cyclo16.zero()
    for j, w in enumerate(weights):
        if type(w) not in (int, Q):
            raise DualityDomainError("branch weights must be exact rationals")
        out = out + Cyclo16.zeta(j*frequency)*fraction(w)
    return out


def uniform_inverse_character(frequency):
    """P_r chi_h=0 unless 16|h; this is only the root factor."""
    return branch_fourier((Q(1, RADIX),) * RADIX, frequency)


def packet_fold_mod16():
    """Endpoint PR #310 grade w_j=(j+1)/2^(j+2) folded modulo 16.

    These are SOURCE-PACKET GRADES, not the authentic conditional inverse
    branch law of the deterministic BBP orbit. They must not be substituted.
    """
    a = Q(1, 2**RADIX)
    w = tuple(Q(1, 2**(j+2)) *
              (Q(j+1)/(1-a) + RADIX*a/(1-a)**2)
              for j in range(RADIX))
    if sum(w) != 1:
        raise ArithmeticError("packet endpoint weights have wrong mass")
    return w


def primitive_packet_fold_mod16():
    """Condition packet J on odd grades (primitive mod 2^k), not BBP inverse lifts."""
    mass = Q(4, 9)
    w = packet_fold_mod16()
    out = tuple((w[j]/mass if j % 2 else Q(0)) for j in range(RADIX))
    if sum(out) != 1:
        raise ArithmeticError("primitive packet conditioning failed")
    return out


def fourier_parseval_defect(weights):
    """Exact sum_{h=1}^{15} |F(h)|² for probability weights on Z/16.

    F(h)=sum_j p_j*zeta^(hj).  Parseval gives 16 sum p_j²-1,
    a finite Chi² distance to Haar. No signed selected-Weyl saving.
    """
    if type(weights) not in (tuple, list) or len(weights) != RADIX:
        raise DualityDomainError("16 rational probability weights required")
    w = tuple(fraction(x) for x in weights)
    if min(w) < 0 or sum(w) != 1:
        raise DualityDomainError("nonnegative probability weights of mass one required")
    return RADIX*sum((x*x for x in w), Q())-1


# 2b. Exact Fourier coordinates for classical Koopman/Perron duality.
@dataclass(frozen=True)
class FourierCharacter:
    frequency: int
    phase: Q

    def __post_init__(self):
        exact_int(self.frequency, "character frequency")
        if type(self.phase) is not Q or not Q(0) <= self.phase < 1:
            raise DualityDomainError("character phase must be a canonical rational turn")


def koopman_character(character: FourierCharacter, forcing):
    """K_r[e(phase)chi_h] = e(phase+h*r)chi_(16h), exactly."""
    if not isinstance(character, FourierCharacter):
        raise DualityDomainError("typed Fourier character required")
    r = fraction(forcing)
    return FourierCharacter(RADIX*character.frequency,
                            circle(character.phase + character.frequency*r))


def perron_character(character: FourierCharacter, forcing):
    """Haar-normalized 16-preimage averaging; None represents zero.

    Crucial: equal branch mass is a NEW measure, not the BBP selected path.
    """
    if not isinstance(character, FourierCharacter):
        raise DualityDomainError("typed Fourier character required")
    if character.frequency % RADIX:
        return None
    r = fraction(forcing)
    k = character.frequency // RADIX
    return FourierCharacter(k, circle(character.phase-k*r))


def exact_koopman_perron_square(h, forcing):
    """P_r K_r = Id; K_r P_r projects onto frequencies divisible by 16."""
    exact_int(h, "frequency")
    r = fraction(forcing)
    chi = FourierCharacter(h, Q(0))
    pk = perron_character(koopman_character(chi, r), r)
    kp_first = perron_character(chi, r)
    kp = None if kp_first is None else koopman_character(kp_first, r)
    if pk != chi or kp != (chi if h % RADIX == 0 else None):
        raise ArithmeticError("exact inside-out Koopman/Perron law failed")
    return {"frequency":h, "forcing":r, "perron_after_koopman":pk,
            "koopman_after_perron":kp, "uniform_branch_operator_only":True,
            "selected_weyl_saving_proved":False}


# 3. Source history: exactly one inverse branch, with its 2-adic carry retained.
@dataclass(frozen=True)
class BranchWitness:
    digit: int
    remainder: Q
    source_index: int
    forcing: Q
    current: Q
    successor: Q
    literal_carry: int
    conductor: int


def original_history(count):
    exact_int(count, "source history length", 1, 2000)
    u, out = Q(0), []
    for n in range(1, count+1):
        u = 16*u + authentic_r(n)
        out.append(u)
    return tuple(out)


def verify_original_history(states):
    """Fail closed if zero seed or the real four-pole source is altered."""
    if not isinstance(states, tuple) or not states:
        return False
    u = Q(0)
    for n, v in enumerate(states, 1):
        if type(v) is not Q or v != 16*u + authentic_r(n):
            return False
        u = v
    return True


def witness_selected_branches(states):
    """Actual x_n=(j_n+t_n)/16, t_n={x_(n+1)-r(n+1)}.

    This is a SOURCE-AUTHENTIC single history: not 16 independent inverses.
    Index n starts at 1, so requires states n and n+1.
    """
    if not verify_original_history(states):
        raise DualityDomainError("selected branches require exact authentic zero-seed source")
    ans = []
    conductor = authentic_r(1).denominator
    for n in range(1, len(states)):
        x = circle(states[n-1])
        y = circle(states[n])
        r = authentic_r(n+1)
        conductor = lcm(conductor, r.denominator)
        j = (16*x).numerator // (16*x).denominator
        t = circle(16*x)
        if not x == (j+t)/16 or t != circle(y-r):
            raise ArithmeticError("actual selected preimage/source map failed")
        prev = states[n-1]
        nxt = states[n]
        carry = nxt.numerator//nxt.denominator - 16*(prev.numerator//prev.denominator)
        shift = (t+r).numerator//(t+r).denominator
        if carry != j + shift:
            raise ArithmeticError("literal BBP integer carry differs from selected lift")
        ans.append(BranchWitness(j, t, n, r, x, y, carry, conductor))
    return tuple(ans)


# 4. A strictly conditional finite inverse-branch mixing criterion.
@dataclass(frozen=True)
class BranchDefect:
    observations: int
    bins: int
    counts: tuple[tuple[int, ...], ...]
    chi_squared: Q

    def conditional_mode_energy(self, h):
        """Exact Q(zeta16) conditional |branch character|² for the h mode.

        This is a true source-history statistic, not a packet character and
        not a prior all-N estimate; Fourier modes retain cross-bin signs.
        Sum h=1..15 equals chi_squared exactly by DFT Parseval.
        """
        exact_int(h, "frequency")
        result = Cyclo16.zero()
        for row in self.counts:
            count = sum(row)
            if count:
                f = branch_fourier(tuple(Q(c, count) for c in row), h)
                result = result + (f*f.conjugate())*Q(count, self.observations)
        return result

    def exact_parity_energy(self):
        """Mode h=8: EXACT rational Z/16 -> Z/2 conditional parity energy.

        E_N,M(8)=sum_b (even_b-odd_b)^2/(N*n_b).
        This is a true signed source-history statistic, not a proof it tends 0.
        """
        ans = Q(0)
        for row in self.counts:
            n = sum(row)
            if n:
                signed = sum((v if j%2==0 else -v for j,v in enumerate(row)))
                ans += Q(signed*signed,self.observations*n)
        if self.conditional_mode_energy(8) != Cyclo16.one()*ans:
            raise ArithmeticError("dyadic parity character not source-compatible")
        return ans

    def exact_upper_for_primitive_h(self, h, precision_bits=32):
        """Rational upper bound, valid for any h not divisible by 16.

        |N^-1 sum e(h x_n)| <= sqrt(chi_squared) + pi |h|/(16 M).
        Use integer-certified sqrt upper and pi<22/7. This is a bound
        from the OBSERVED orbit counts, not a prior source-theorem estimate.
        """
        exact_int(h, "Fourier frequency")
        exact_int(precision_bits, "sqrt precision bits", 4, 128)
        if h % RADIX == 0:
            raise DualityDomainError("h divisible by 16: use the authentic shift law")
        scale = 1 << precision_bits
        q = self.chi_squared
        # The floor-square-root followed by +1 is strictly above sqrt(q).
        root = Q(isqrt((q.numerator*scale*scale)//q.denominator)+1, scale)
        return root + Q(22*abs(h), 7*RADIX*self.bins)


def branch_defect(states, bins=4, *, authenticate=True):
    """Exact conditional Chi² of digit j=floor(16{x}) given tail {16x}.

    delta=16/N sum_{b:n_b>0} sum_j(n_bj-n_b/16)^2/n_b.
    By finite-group Parseval equals total nontrivial conditional
    inverse-character energy. The q_16 packet distribution is NOT used.
    """
    exact_int(bins, "tail bin count", 1, 4096)
    if not isinstance(states, tuple) or not states or len(states) > 100000:
        raise DualityDomainError("nonempty finite exact state tuple required")
    if authenticate and not verify_original_history(states):
        raise DualityDomainError("history is not the authentic zero-anchored four-pole source")
    matrix = [[0 for _ in range(RADIX)] for _ in range(bins)]
    for u in states:
        x = circle(fraction(u))
        j = (16*x).numerator // (16*x).denominator
        t = circle(16*x)
        b = (bins*t).numerator // (bins*t).denominator
        if not (0 <= j < RADIX and 0 <= b < bins):
            raise ArithmeticError("finite branch index escaped its source fiber")
        matrix[b][j] += 1
    N = len(states)
    delta = Q(0)
    for row in matrix:
        nb = sum(row)
        if nb:
            delta += Q(16, N*nb)*sum(((Q(v)-Q(nb,16))**2 for v in row), Q())
    return BranchDefect(N, bins, tuple(tuple(x) for x in matrix), delta)


def authenticated_shift_budget(N, h):
    """Rigorous rational normalized difference |A_N(16h)-A_N(h)| upper.

    Exact source U_(n+1)=16U_n+r_(n+1), sum_{n>=1}r(n) <= 15.
    Use 2 pi <= 44/7 and the endpoint telescope 2/N.
    This is only approximate invariant-measure compatibility, NOT Haar.
    """
    exact_int(N, "horizon", 1, 10**8)
    exact_int(h, "frequency")
    return Q(2, N) + Q(660*abs(h), 7*N)


def source_shift_actual_N_budget(N, h):
    """Tighter, still exact, finite source correction without infinite input."""
    exact_int(N, "horizon", 1, 100000)
    exact_int(h, "frequency")
    return Q(2, N) + Q(44*abs(h), 7*N)*sum((authentic_r(n+1) for n in range(1,N+1)), Q())


def selected_weyl_upper_from_branch_defect(defect, h):
    """Exact rational upper on original |N^-1 sum e(hU_n)|.

    For h=16^k h0, 16∤h0, apply the primitive conditional Chi²
    inequality to h0 and pay k authentic nonautonomous shift errors.
    This is a SOURCE-DATA-DEPENDENT a posteriori certificate, not an
    independently proved small defect or a π-normality result.
    """
    if not isinstance(defect, BranchDefect):
        raise DualityDomainError("a source-history BranchDefect is required")
    exact_int(h, "nonzero Fourier frequency")
    if h == 0:
        raise DualityDomainError("nonzero Fourier frequency required")
    primitive = h
    k = 0
    while primitive % RADIX == 0:
        primitive //= RADIX
        k += 1
    upper = defect.exact_upper_for_primitive_h(primitive)
    for exponent in range(k):
        upper += authenticated_shift_budget(defect.observations,
                                            primitive*(RADIX**exponent))
    return upper


def status_flags():
    return {"typed_lambda_interface": True, "uniform_branch_fourier_orthogonality": True,
            "authentic_source_selected_branch_in_hierarchy": True,
            "conditional_chi2_normality_saving_proved": False,
            "source_max_entropy_estimate_proved": False,
            "pi_base16_normality_proved": False, "RH_proved": False}
