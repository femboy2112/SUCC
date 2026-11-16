"""Exact bounded instruments for the source-attached all-mode detector.

The Poisson energy itself is inherited (SCE-01, 2026-10-24).  This module
implements its shifted Gamma--Poisson frequency law, finite tail accounting,
phase-fixture readout, original-source transfer cost, and a declared report
experiment's alias costs.  It never certifies normality from finite data.

All inputs are integers/Fractions; phase fixtures are exact rational points
on the unit circle.  They are not silently labelled as original BBP phases.
Budgets bound dimensions and powers, not the bit sizes of input rationals.
"""

from dataclasses import dataclass
from fractions import Fraction as Q

from observational_succ.bbp_echo_delay_transport import filter_symbol


def _integer(value, name, minimum=0, maximum=4096):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{name} must be an integer in [{minimum}, {maximum}]")
    return value


def _rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _unit_point(value):
    if not isinstance(value, (tuple, list)) or len(value) != 2:
        raise ValueError("a rational unit point has two coordinates")
    x, y = map(_rational, value)
    if x * x + y * y != 1:
        raise ValueError("unit norm required")
    return x, y


def frequency_weight(h):
    """Pr(H=h)=2^-h for H=1+Poisson(T), T~Gamma(1,scale=1)."""
    return Q(1, 1 << _integer(h, "frequency", 1))


def frequency_tail(cutoff):
    """Exact omitted probability Pr(H>cutoff), including cutoff zero."""
    return Q(1, 1 << _integer(cutoff, "cutoff"))


def gamma_poisson_weight(k):
    """Gamma integral k!/[k! 2^(k+1)], with H=k+1."""
    return frequency_weight(_integer(k, "Poisson count", 0, 4095) + 1)


def pair_kernel(cosine):
    """Sum_(h>=1) 2^-h cos(h theta), given exact cosine=cos(theta)."""
    c = _rational(cosine)
    if not -1 <= c <= 1:
        raise ValueError("cosine outside [-1,1]")
    return (2 * c - 1) / (5 - 4 * c)


def mixed_pair_click(cosine):
    return (1 - pair_kernel(cosine)) / 2


@dataclass(frozen=True)
class EnergyInterval:
    lower: Q
    upper: Q

    def __post_init__(self):
        lo, hi = _rational(self.lower), _rational(self.upper)
        if not 0 <= lo <= hi <= 1:
            raise ValueError("energy interval must lie in [0,1]")
        object.__setattr__(self, "lower", lo)
        object.__setattr__(self, "upper", hi)

    @property
    def click_interval(self):
        return (1 - self.upper) / 2, (1 - self.lower) / 2


def prefix_energy_interval(mode_squared_means):
    """Input is the consecutive |W(h)|^2 values, h=1,...,cutoff.

    An arbitrary valid list need not be realizable by a common source.
    This function supplies the conditional tail bound, not authentication.
    """
    if not isinstance(mode_squared_means, (tuple, list)):
        raise ValueError("a finite tuple/list is required")
    cutoff = _integer(len(mode_squared_means), "cutoff")
    values = tuple(map(_rational, mode_squared_means))
    if any(not 0 <= x <= 1 for x in values):
        raise ValueError("squared means must lie in [0,1]")
    lower = sum((frequency_weight(h) * x for h, x in enumerate(values, 1)), Q())
    return EnergyInterval(lower, min(Q(1), lower + frequency_tail(cutoff)))


def energy_from_unit_points(points):
    """Exact complete-mode energy on 1..64 rational-circle fixtures.

    Ordered pairs include the diagonal: I and J are independent uniform
    draws with replacement.  Removing the diagonal changes the experiment.
    """
    if not isinstance(points, (tuple, list)):
        raise ValueError("a finite tuple/list is required")
    size = _integer(len(points), "point count", 1, 64)
    z = tuple(map(_unit_point, points))
    energy = sum((pair_kernel(x * u + y * v)
                  for x, y in z for u, v in z), Q()) / (size * size)
    if not 0 <= energy <= 1:
        raise ArithmeticError("positive Fourier-energy invariant failed")
    return energy


@dataclass(frozen=True)
class GreenTransferBudget:
    shell_start: int
    energy_error_upper: Q
    click_error_upper: Q


def original_source_transfer(shell_start):
    """Original-source bound only: T_n<1/(64n^2), pi<22/7.

    Sum h*2^-h=2 gives |E_U-E_Y|<=8*pi*mean(T)<pi/(8B^2).
    This does not certify a digit indicator or a changed forcing law.
    """
    b = _integer(shell_start, "shell start", 1, 1_000_000)
    bound = Q(11, 28 * b * b)
    return GreenTransferBudget(b, bound, bound / 2)


def completed_lag_benchmark(coefficients):
    """Haar initial-phase mean for a fixed finite integer lag character.

    Uses the inherited exact P(16) normal form.  A resonant word has
    response 1, even under normality; other fixed words have target 0.
    No growing-lag uniform limit is asserted.
    """
    return int(filter_symbol(coefficients) == 0)


@dataclass(frozen=True)
class PeriodicAliasReport:
    period: int
    energy: Q
    click_rate: Q
    labelled_chi_squared: Q
    unlabelled_chi_squared: Q

    @property
    def labelled_trials_strict_lower(self):
        """For equal-prior error <=1/4; uses ln(2)>2/3."""
        return Q(2, 3) / self.labelled_chi_squared

    @property
    def unlabelled_trials_strict_lower(self):
        return Q(2, 3) / self.unlabelled_chi_squared


def periodic_alias_report(period):
    """Declared invariant laws with |W(h)|^2=1 iff period divides h.

    For genuine radix-16 coset cycles, period=3^a*5^b with a,b>=0.
    Other periods describe the corresponding uniform polygon law only.
    The report retains (H,click) or just click, not clocks/full phases.
    """
    m = _integer(period, "period", 1)
    eps = Q(1, (1 << m) - 1)
    return PeriodicAliasReport(m, eps, (1 - eps) / 2, eps, eps * eps)


def report_product_chi_squared(period, trials, *, retain_frequency):
    if type(retain_frequency) is not bool:
        raise ValueError("retain_frequency must be Boolean")
    n = _integer(trials, "trials", 0, 256)
    report = periodic_alias_report(period)
    x = report.labelled_chi_squared if retain_frequency else report.unlabelled_chi_squared
    return (1 + x) ** n - 1


def haar_only_event_miss(period, trials):
    """Haar miss probability; a resonant-frequency click is control-impossible."""
    n = _integer(trials, "trials", 0, 256)
    return (1 - periodic_alias_report(period).energy / 2) ** n
