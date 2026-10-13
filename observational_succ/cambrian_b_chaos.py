"""Exact bounded witnesses for Cambrian chaos assignments 07--12.

Sparse Chebyshev algebra, certified parameter isolation, and finite observation
channels. Infinite-dimensional theorems are proved in the companion dossier;
these rational computations do not stand in for those proofs.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import comb
from typing import Mapping, Sequence

from .logistic_observer_tree import inverse_word
from .misiurewicz_phase_quotient import ALPHA, sign_algebraic


class CambrianChaosError(ValueError):
    pass


def _q(value: int | F) -> F:
    if type(value) is bool or not isinstance(value, (int, F)):
        raise CambrianChaosError("Exact integer or Fraction required")
    return F(value)


def _n(value: int) -> int:
    if type(value) is not int or value < 0:
        raise CambrianChaosError("Nonnegative integer required")
    return value


def modes(values: Mapping[int, int | F]) -> dict[int, F]:
    """c_k coordinates in T_k(1-2x), without expanding high degrees."""
    return { _n(k): _q(v) for k, v in values.items() if _q(v) }


def transfer(values: Mapping[int, int | F], depth: int) -> dict[int, F]:
    divisor = 1 << _n(depth)
    return {k // divisor: v for k, v in modes(values).items()
            if k % divisor == 0}


def koopman(values: Mapping[int, int | F], advance: int) -> dict[int, F]:
    multiplier = 1 << _n(advance)
    return {k * multiplier: v for k, v in modes(values).items()}


def l2_norm_square(values: Mapping[int, int | F]) -> F:
    """Arcsine orthogonality: ||T_0||²=1, ||T_k||²=1/2 for k>0."""
    return sum((v*v / (1 if k == 0 else 2)
                for k, v in modes(values).items()), F(0))


def advancing(values: Mapping[int, int | F], depth: int, advance: int) -> dict[int, F]:
    return transfer(koopman(values, advance), depth)


def geometric_lacunary(ratio: int | F, depth: int) -> dict:
    """Closed exact formulas for g=sum_{j>=0} ratio^j T_{2^j}.

    For 0<ratio<1, uniform convergence and Lg=ratio*g are paper proofs.
    The returned rational values use those proved formulas, not a truncation.
    """
    r = _q(ratio)
    _n(depth)
    if not 0 < r < 1:
        raise CambrianChaosError("Positive summable ratio strictly below one required")
    return {"ratio": r, "depth": depth,
            "initial_sup_norm": 1/(1-r),
            "residual_sup_norm": r**depth/(1-r),
            "initial_l2_norm_squared": 1/(2*(1-r*r)),
            "residual_l2_norm_squared": r**(2*depth)/(2*(1-r*r)),
            "finite_exact_completion": False}


def alpha_two_cycle_multiplier() -> dict:
    m = -ALPHA*ALPHA + 2*ALPHA + 4
    if sign_algebraic(-m-2) != 1:
        raise AssertionError("Periodic multiplier obstruction is not strict")
    return {"signed_multiplier_coefficients": m.as_strings(),
            "absolute_multiplier_exceeds_2": True,
            "maximum_entropy_required_two_step_multiplier": F(2),
            "classical_theorem_application_conditional_on":
            "Misiurewicz (1981) Theorem 8.1 hypotheses and acim component support",
            "natural_acim_constructed": False}


def pf_constant_cell_obstruction() -> dict:
    """On alpha left phase unique C preimage supplies nonconstant Jacobian.

    Values 17/20 and 9/10 are interior C source points. Both images are in
    A, with unequal positive |f'|; a positive constant C-density therefore
    cannot push to a constant A-density. Exact algebra proves the signs.
    """
    points = (F(17,20), F(9,10))
    ys = tuple(ALPHA*x*(1-x) for x in points)
    derivatives = tuple(ALPHA*(2*x-1) for x in points)
    from .misiurewicz_phase_quotient import FIXED, MAXIMUM, LOW, CRITICAL
    for x,y,d in zip(points,ys,derivatives):
        if not (sign_algebraic(x-FIXED)>0 and sign_algebraic(MAXIMUM-x)>0
                and sign_algebraic(y-LOW)>0 and sign_algebraic(CRITICAL-y)>0
                and sign_algebraic(d)>0):
            raise AssertionError("Witness outside required exact source cells")
    if derivatives[0] == derivatives[1]:
        raise AssertionError("Distinct Jacobians collapsed")
    return {"source_points_in_C": points,
            "images_in_A_coefficients": tuple(y.as_strings() for y in ys),
            "jacobian_coefficients": tuple(d.as_strings() for d in derivatives),
            "constant_positive_density_on_three_cells_is_invariant": False,
            "does_not_refute_arbitrary_nonconstant_density_with_equal_cell_masses": True}


def poly_add(a: Sequence[F], b: Sequence[F]) -> tuple[F,...]:
    return tuple((a[k] if k<len(a) else F(0)) +
                 (b[k] if k<len(b) else F(0)) for k in range(max(len(a),len(b))))


def poly_multiply(a: Sequence[F], b: Sequence[F]) -> tuple[F,...]:
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def critical_return_polynomial(period: int) -> tuple[F,...]:
    if type(period) is not int or not 1 <= period <= 4:
        raise CambrianChaosError("Bounded critical return period must be 1..4")
    x = (F(1,2),)
    for _ in range(period):
        x = (F(0),) + poly_multiply(x, poly_add((F(1),), tuple(-v for v in x)))
    return poly_add(x,(F(-1,2),))


def poly_at(coeffs: Sequence[F], x: F) -> F:
    total = F(0)
    for c in reversed(coeffs):
        total = total*x+c
    return total


def centered_polynomial_interval(coeffs: Sequence[F], lo: F, hi: F) -> tuple[F,F]:
    """Sound Taylor interval around rational midpoint, avoiding cancellations."""
    mid, radius = (lo+hi)/2, (hi-lo)/2
    shifted = tuple(sum((coeffs[k]*comb(k,j)*mid**(k-j)
                         for k in range(j,len(coeffs))),F(0))
                    for j in range(len(coeffs)))
    error = sum((abs(shifted[j])*radius**j for j in range(1,len(shifted))),F(0))
    return shifted[0]-error, shifted[0]+error


def superstable_three_certificate() -> dict:
    p = critical_return_polynomial(3)
    lo, hi = F(383,100), F(96,25)
    dp = tuple(k*p[k] for k in range(1,len(p)))
    derivative = centered_polynomial_interval(dp,lo,hi)
    vals = (poly_at(p,lo),poly_at(p,hi))
    if vals[0]*vals[1]>=0 or not (derivative[0]>0 or derivative[1]<0):
        raise AssertionError("Unique critical-return root not certified")
    # f(c)=r/4>c; f²(c)=r²(4-r)/16<c on this bracket.
    f2 = (F(0),F(0),F(1,4),F(-1,16))
    second = centered_polynomial_interval(f2,lo,hi)
    if not lo/4>F(1,2) or not 0<second[0]<=second[1]<F(1,2):
        raise AssertionError("Critical kneading C,R,L,C not certified")
    return {"critical_return_polynomial": tuple(map(str,p)),
            "root_bracket": (lo,hi), "endpoint_polynomial_values": vals,
            "derivative_interval": derivative, "unique_root_in_bracket": True,
            "critical_itinerary": "C,R,L,C", "prime_period": 3,
            "cycle_multiplier": F(0),
            "stationary_cycle_source_weights": (F(1,3),)*3,
            "cycle_phase_entropy_rate_bits": F(0),
            "full_parameter_window_classified": False}


def periodic_extension(period: int, steps: int) -> dict:
    """Explicit (phase, one-sided fair tape), increment phase and shift tape.

    Product law uniform phase x iid fair tape. Phase factor zero entropy;
    source tape has one fresh bit per step, hence positive metric entropy.
    """
    _n(steps)
    if type(period) is not int or period<1:
        raise CambrianChaosError("Positive period required")
    phase_paths = tuple(tuple((phase+t)%period for t in range(steps+1))
                        for phase in range(period))
    return {"period":period, "steps":steps,
            "phase_paths":phase_paths, "phase_history_count":period,
            "source_bit_history_count_per_phase":1<<steps,
            "source_entropy_rate_bits":F(1), "phase_entropy_rate_bits":F(0)}


def noisy_phase_joint(error_first: int | F, error_second: int | F,
                      odd_delay_probability: int | F) -> dict[tuple[int,int],F]:
    """Same fair source phase, independent BSC errors and unknown lag parity.

    First phase X is fair; B=X xor parity xor second_error. First report
    A=X xor first_error. Independence is an explicit hypothesis.
    """
    a,b,d = map(_q,(error_first,error_second,odd_delay_probability))
    if any(not 0<=p<=1 for p in (a,b,d)):
        raise CambrianChaosError("Channel probabilities must lie in [0,1]")
    out = {(x,y):F(0) for x,y in product((0,1),repeat=2)}
    for x,e0,e1,parity in product((0,1),repeat=4):
        mass = F(1,2)*(a if e0 else 1-a)*(b if e1 else 1-b)*(d if parity else 1-d)
        out[(x^e0,x^parity^e1)] += mass
    return out


def noisy_phase_covariance(error_first: int | F, error_second: int | F,
                           odd_delay_probability: int | F) -> F:
    a,b,d = map(_q,(error_first,error_second,odd_delay_probability))
    noisy_phase_joint(a,b,d)  # typed validation
    return (1-2*a)*(1-2*b)*(1-2*d)/4


def partial_history_intervals(word: Sequence[int | None], lo: int | F,
                              hi: int | F) -> tuple[tuple[F,F],...]:
    """Union of exact compatible inverse cylinders with k missing histories.

    Each interval width (hi-lo)/2^n, total length 2^k*(hi-lo)/2^n.
    No source authentication, prior, or individual trajectory inference.
    """
    a,b = _q(lo),_q(hi)
    if not 0<a<=b<1 or len(word)>14 or any(
            v is not None and (type(v) is not int or v not in (0,1)) for v in word):
        raise CambrianChaosError("Interior endpoint interval and <=14 valid history symbols required")
    unknown = tuple(i for i,v in enumerate(word) if v is None)
    intervals=[]
    for chosen in product((0,1),repeat=len(unknown)):
        filled=list(word)
        for i,v in zip(unknown,chosen):
            filled[i]=v
        x,y=inverse_word(filled,a),inverse_word(filled,b)
        intervals.append((min(x,y),max(x,y)))
    return tuple(sorted(intervals))


def bounded_dynamical_error(lipschitz: int | F, initial_error: int | F,
                            per_step_error: int | F, steps: int) -> F:
    """Finite Gronwall bound; both compared trajectories stay in [0,1].

    Requires a supplied VALID Lipschitz constant and additive per-step error
    bound. The module does not certify arbitrary user-supplied map constants.
    """
    a,d,e = map(_q,(lipschitz,initial_error,per_step_error))
    _n(steps)
    if a<0 or d<0 or e<0:
        raise CambrianChaosError("Nonnegative error and Lipschitz bounds required")
    return min(F(1), a**steps*d + e*sum((a**j for j in range(steps)),F(0)))
