"""Tate source profiles feeding the already-existing signed Weil/Suzuki machinery.

The Mellin/log-derivative identity is classical and restricted to Re(s)>1.
No zero data, positivity assumption, or spectral global limit is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .completed_weil_transport import von_mangoldt_labels, prime_heat_tail_bound
from .tate_local_contract import chi_mod3, gauss_sum_mod3


class TateWeilBridgeError(ValueError):
    """Missing/altered arithmetic source, completed arch profile, or test domain."""


@dataclass(frozen=True)
class TateWeilProfile:
    """Typed source-contract fingerprint, not a substitute for a Weil distribution.

    Field values cannot be arbitrarily mixed between zeta and chi_{-3}.
    Root numbers are imported classical Poisson/Gauss facts, not fitted.
    """
    kind: str
    conductor: int
    parity: int
    root_number: int
    has_completed_poles: bool
    half_density: Fraction

    def __post_init__(self):
        allowed = {
            'zeta': (1, 0, 1, True, Fraction(1, 2)),
            'chi_minus_3': (3, 1, 1, False, Fraction(1, 2)),
        }
        if (type(self.kind) is not str or self.kind not in allowed
                or (self.conductor, self.parity, self.root_number,
                    self.has_completed_poles, self.half_density) != allowed[self.kind]
                or type(self.conductor) is not int or type(self.parity) is not int
                or type(self.root_number) is not int
                or type(self.has_completed_poles) is not bool
                or type(self.half_density) is not Fraction):
            raise TateWeilBridgeError('Illegal source/Gamma/conductor/phase/pole/half-density substitution')

    @classmethod
    def canonical(cls, kind: str):
        if kind == 'zeta':
            return cls('zeta', 1, 0, 1, True, Fraction(1, 2))
        if kind == 'chi_minus_3':
            return cls('chi_minus_3', 3, 1, 1, False, Fraction(1, 2))
        raise TateWeilBridgeError('Only source-authenticated zeta and primitive chi_-3')

    def local_ramified_gauss(self):
        """Algebraic local Gauss phase at the genuine conductor 3, if present."""
        return gauss_sum_mod3(1) if self.kind == 'chi_minus_3' else None


def finite_log_derivative_tape(N: int, profile: TateWeilProfile):
    """(prime_power, primitive_prime, signed_multiplier) without log float weights.

    Each pair denotes multiplier * log(primitive_prime) / sqrt(prime_power)
    on the compact log-test, or * log(p) / prime_power**s on Re(s)>1.
    χ_-3(p^k) is 0 on the ramified factor p=3, not a new local place.
    """
    if not isinstance(profile, TateWeilProfile):
        raise TateWeilBridgeError('An authenticated source profile is required')
    if type(N) is not int or not 2 <= N <= 200000:
        raise TateWeilBridgeError('Exact positive finite prime-power horizon, 2<=N<=200000')
    tape = []
    for n, p in von_mangoldt_labels(N):
        phase = 1 if profile.kind == 'zeta' else chi_mod3(n)
        if phase:
            tape.append((n, p, phase))
    return tuple(tape)


def finite_completed_log_derivative(s, N: int, profile: TateWeilProfile, dps: int = 60):
    """Two Lambda'/Lambda from original Gamma+pole+prime-power sources.

    For zeta, Lambda refers to xi(s)=s(s-1)Gamma_R(s)zeta(s)/2.
    For primitive chi_-3, Lambda refers to (3/pi)^((s+1)/2)
    Gamma((s+1)/2)L(s,chi_-3), without an artificial pole.
    Only defined on Re(s)>1 by the actual convergent source germ.
    """
    if type(dps) is not int or not 30 <= dps <= 160:
        raise TateWeilBridgeError('Numeric calibration needs 30<=dps<=160')
    if type(s) is bool:
        raise TateWeilBridgeError('Analytic parameter must be complex/rational')
    try:
        import mpmath as mp
    except ImportError as exc:
        raise TateWeilBridgeError('mpmath research dependency required') from exc
    mp.mp.dps = dps
    ss = mp.mpc(s)
    if ss.real <= 1:
        raise TateWeilBridgeError('Original Euler source needs Re(s)>1')
    source = mp.fsum(mult * mp.log(p) * mp.power(n, -ss)
                     for n, p, mult in finite_log_derivative_tape(N, profile))
    completed_gamma = mp.log(mp.mpf(profile.conductor) / mp.pi) + mp.digamma((ss + profile.parity) / 2)
    if profile.has_completed_poles:
        completed_gamma += 2 / ss + 2 / (ss - 1)
    return completed_gamma - 2 * source


def analytic_source_tail_bound(sigma, N: int, profile: TateWeilProfile):
    """Mathematical majorant for TWO log derivatives on Re(s)=sigma>1.

    Uses abs(χ(p)^k)<=1 and ordinary Λ(n)<=log n. The expression's
    numerical mpmath value is NOT itself a certified directed interval.
    """
    if not isinstance(profile, TateWeilProfile):
        raise TateWeilBridgeError('Authenticated source profile required')
    if type(N) is not int or N < 3:
        raise TateWeilBridgeError('N>=3 required for monotone source tail')
    return 2 * prime_heat_tail_bound(sigma, N)
