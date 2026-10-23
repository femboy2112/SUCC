"""Log-address half-density and exact limits of carry-to-Weil transport.

Universal statements are paper-proved in SOURCE_FAITHFUL_WEIL_AUDIT.md.
This module provides finite rational/interval witnesses, not an RH oracle.
The original completed Suzuki source is imported only after its frozen Git
blob and genuine arithmetic tape have been checked. No zero inputs occur.
"""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path

from .tate_suzuki_shorting import verify_original_suzuki_source


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact int/Fraction required")
    return Q(value)


def _positive_integer(value):
    if type(value) is not int or value < 1:
        raise ValueError("positive integer source label required")
    return value


def _source():
    verify_original_suzuki_source()
    from . import source_weil_hierarchy as source
    return source


def source_fingerprint():
    """Actual bytes, source normalization, and the unchanged sign boundary."""
    source = _source()
    result = verify_original_suzuki_source()
    result.update({
        "source_sha256": sha256(Path(source.__file__).read_bytes()).hexdigest(),
        "conductor": 1,
        "parity": 0,
        "root_number": 1,
        "completed_poles": (0, 1),
        "prime_sum_sign": -1,
        "RH_proved": False,
        "new_S4_sign_bound": False,
    })
    return result


def box_log_gram(n, m, alpha=Q(1, 2), *, width=Q(1)):
    """Outward Gram interval for n^-alpha/width 1_[log n,log n+width].

    Only alpha=0,1/2,1 is executable; the paper proves the threshold for all
    real alpha and all nonzero compactly supported L2 seeds. This box is a
    synthesis calibration, NOT an admissible smooth Weil test.
    """
    n, m = _positive_integer(n), _positive_integer(m)
    alpha = _rational(alpha)
    width = _rational(width)
    if width <= 0:
        raise ValueError("positive rational smoothing width required")
    if alpha not in (Q(0), Q(1, 2), Q(1)):
        raise ValueError("finite interval oracle supports alpha=0,1/2,1 only")
    source = _source()
    gap = source.log_iv(Q(max(n, m), min(n, m)))
    overlap = source.I(max(Q(), width-gap.hi), max(Q(), width-gap.lo))/width**2
    if alpha == 0:
        return overlap
    if alpha == 1:
        return overlap / (n*m)
    return overlap * source.sqrt_inverse(n*m)


def box_log_energy(coefficients, alpha=Q(1, 2)):
    """Rigorous finite L2 norm squared for a finitely supported rational input.

    Signs/cross terms are retained; this is not diagonal norm bookkeeping.
    """
    if not isinstance(coefficients, dict) or not coefficients:
        raise ValueError("nonempty finite coefficient dictionary required")
    rows = tuple((_positive_integer(n), _rational(a))
                 for n, a in coefficients.items())
    source = _source()
    total = source.iv(0)
    for n, a in rows:
        for m, b in rows:
            total += a*b*box_log_gram(n, m, alpha)
    return total


def unweighted_cluster_lower(N):
    """Unit source block on N..2N has image norm² >= 3(N+1)/10.

    The normalized coefficients need not be rational: the energy is the
    all-ones Gram sum divided by N+1. The bound uses the actual certified
    source log(2)<7/10 and every pair's exact ratio <=2.
    """
    N = _positive_integer(N)
    source = _source()
    if source.log2_iv().hi >= Q(7, 10):
        raise ArithmeticError("failed independent log(2) calibration")
    return Q(3*(N+1), 10)


def compact_seed_synthesis_bound(width, seed_norm_squared):
    """Theorem bound ||J_(1/2)||² <= (1+width)||seed||².

    Premise: seed supported in an interval of length width. Caller-supplied
    norm and support bounds are mathematical premises, not measured data.
    """
    width, norm2 = _rational(width), _rational(seed_norm_squared)
    if width <= 0 or norm2 < 0:
        raise ValueError("positive support width and nonnegative norm bound")
    return (1+width)*norm2


def regularized_prime_tape(cutoff):
    """Finite original prime-distribution coefficients for any chosen seed.

    Each row represents log(p)/sqrt(n) tau_log(n)(seed), n=p^r. Reflection
    supplies the negative log atom. The ORIGINAL Weil distribution uses the
    negative of that symmetric arithmetic sum. This is neither the Gamma
    completion nor a positive trace. No seed or Gaussian is silently chosen.
    """
    cutoff = _positive_integer(cutoff)
    if cutoff > 4096:
        raise ValueError("finite tape budget cutoff<=4096")
    source = _source()
    rows = []
    for n in range(2, cutoff+1):
        p = source.real_prime_power(n)
        if p is None:
            continue
        r, residue = 0, n
        while residue % p == 0:
            residue //= p
            r += 1
        if residue != 1:
            raise ArithmeticError("primitive prime-power source mismatch")
        rows.append({"n": n, "prime": p, "power": r,
                     "log_center": source.log_iv(n),
                     "weight": source.log_iv(p)*source.sqrt_inverse(n),
                     "source_input": p**(r-1)})
    return tuple(rows)


def high_split_inverse(e, f, g, b, c):
    """Exact real two-sector inverse energy, explicitly SYNTHETIC finite data.

    D=[[e,f],[f,g]]>0, source coupling=(b,c). The forgotten sector correction
    is nonnegative and must not be discarded from an upper inverse bound.
    """
    e, f, g, b, c = map(_rational, (e, f, g, b, c))
    determinant = e*g-f*f
    if e <= 0 or determinant <= 0:
        raise ValueError("positive definite high operator required")
    visible = b*b/e
    residual = c-f*b/e
    hidden_metric = g-f*f/e
    defect = residual*residual/hidden_metric
    direct = (g*b*b-2*f*b*c+e*c*c)/determinant
    if direct != visible+defect:
        raise ArithmeticError("inverse block identity failed")
    return {"visible": visible, "defect": defect, "total": direct,
            "residual": residual, "hidden_metric": hidden_metric,
            "scope": "SYNTHETIC_FINITE_OPERATOR_NOT_SUZUKI"}


def phase_blind_schur_counterexample():
    """Same D and component magnitudes, opposite Schur signs at A=1."""
    plus = high_split_inverse(2, 1, 2, 1, 1)
    minus = high_split_inverse(2, 1, 2, 1, -1)
    return {"D": ((Q(2), Q(1)), (Q(1), Q(2))),
            "A": Q(1), "coupling_norm_squared": Q(2),
            "plus_S": 1-plus["total"],
            "minus_S": 1-minus["total"],
            "plus": plus, "minus": minus,
            "original_Weil_counterexample": False}


def genuine_prime_two_negative_atom():
    """Isolated original -E_2 on a positive C² autocorrelation is negative.

    f(x)=(1-x²)^3 on [-1,1], zero outside. For 0<b=log2<7/10,
    integrate f(x)f(x-b) over x in [0,3/10]. Both factors >=(1-(7/10)²)^3,
    so h(b)>=3/10*(51/100)^6. Thus -2w h(b) is STRICTLY negative.
    This is only the arithmetic atom, not the completed Weil form.
    """
    source = _source()
    b = source.log2_iv()
    if not (b.lo > Q(3, 10) and b.hi < Q(7, 10)):
        raise ArithmeticError("source log2 failed bump-support calibration")
    h_lower = Q(3, 10)*Q(51, 100)**6
    w = b*source.sqrt_inverse(2)
    return {"autocorrelation_lower": h_lower,
            "atom_upper": -2*w.lo*h_lower,
            "weight_interval": w,
            "test_regularity": "C_c^2 autocorrelation",
            "completed_Weil_sign_inferred": False}


def completion_mutation_differences(r=Q(2), J=4):
    """Signed g_J mutant-minus-authentic witnesses on the PINNED source.

    Every returned interval describes an explicit changed source, not a
    permissible correction to the authentic form. Gamma shift changes the
    first d=1 rung to d=3; fake6 adds log(6)/sqrt(6); pole mutation flips BOTH
    completed pole channels; contact mutation raises C by one.
    """
    r = _rational(r)
    if not 0 < r <= 2 or type(J) is not int or not 1 <= J <= 128:
        raise ValueError("source domain 0<r<=2 and 1<=J<=128")
    source = _source()
    source.screw_interval(r, J)  # authenticate the actual source evaluator too
    one = source.iv(1)
    pole = -4*(source.exp_pos(r/2)+source.exp_neg(r/2)-2)
    first_gamma = -4*(one-source.exp_neg(r/2))
    shifted_gamma = -Q(4, 9)*(one-source.exp_neg(3*r/2))

    def hinge(n, p):
        displacement = source.positive_part_interval(source.iv(r)-source.log_iv(n))
        return source.log_iv(p)*source.sqrt_inverse(n)*displacement

    w2wrong = source.log2_iv()/2-source.log2_iv()*source.sqrt_inverse(2)
    return {
        "fake_composite_6": hinge(6, 6),
        "missing_prime_power_4": -hinge(4, 2),
        "non_euler_double_prime_2": hinge(2, 2),
        "wrong_half_density_prime_2": w2wrong*source.positive_part_interval(
            source.iv(r)-source.log2_iv()),
        "shifted_first_gamma": shifted_gamma-first_gamma,
        "wrong_completed_pole_signs": -2*pole,
        "contact_plus_one": source.iv(r/2),
    }
