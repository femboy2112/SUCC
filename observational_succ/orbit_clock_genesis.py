"""Source-factored unary clocks, lawful fresh-clock splices, and LCM-jet genesis.

Finite exact observations only. A clock *constructed by an instrument* is not
thereby an equivariant quotient of the external source. True global source
statements are proved in the accompanying paper, not by finite tests.

No zero locations, gamma, signed Weil form, physical sensor, or prime labels
are inputs. This module uses ordinary Python integers in the METATHEORY.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, gcd, isqrt, lcm


class ClockSourceError(ValueError):
    """A purported source morphism, finite clock, or budget is not licensed."""


def _nat(value: object, name: str, minimum: int = 1, maximum: int = 10000) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise ClockSourceError(f"{name} must be an exact integer in [{minimum},{maximum}]")
    return value


@dataclass(frozen=True)
class FiniteUnarySource:
    """An actual finite deterministic source graph with a pointed root.

    States off the root's orbit are not used as imaginary observed evidence.
    The orbit has a finite transient prefix and a genuine eventually cyclic tail.
    """
    transitions: tuple[int, ...]
    root: int = 0
    source_id: str = "declared-finite-source"

    def __post_init__(self) -> None:
        t = self.transitions
        if type(t) is not tuple or not 1 <= len(t) <= 10000:
            raise ClockSourceError("finite nonempty transition tuple required")
        if type(self.root) is not int or not 0 <= self.root < len(t):
            raise ClockSourceError("pointed root absent from source")
        if not isinstance(self.source_id, str) or not self.source_id:
            raise ClockSourceError("nonempty source identity required")
        if any(type(k) is not int or not 0 <= k < len(t) for k in t):
            raise ClockSourceError("every deterministic transition must be an existing state")

    def orbit_signature(self) -> dict:
        """Proves tail/period by exhaustive traversal of actually visited states."""
        first: dict[int, int] = {}
        visited: list[int] = []
        state = self.root
        while state not in first:
            first[state] = len(visited)
            visited.append(state)
            state = self.transitions[state]
        transient = first[state]
        period = len(visited) - transient
        return {"preperiod": transient, "period": period,
                "visited": tuple(visited), "first_repeated_state": state,
                "unreachable_state_count": len(self.transitions) - len(visited),
                "has_free_infinite_orbit": False, "source_id": self.source_id}

    def can_factor_to(self, modulus: int) -> bool:
        """Pointed successor-equivariant factor exists iff modulus | true period."""
        _nat(modulus, "target quotient clock")
        return self.orbit_signature()["period"] % modulus == 0

    def factor_to(self, modulus: int) -> dict[int, int]:
        """Return and exhaustively check a lawful factor on the root orbit."""
        _nat(modulus, "target quotient clock")
        if not self.can_factor_to(modulus):
            raise ClockSourceError("invented quotient: target period fails true return relation")
        orbit = self.orbit_signature()["visited"]
        out = {state: step % modulus for step, state in enumerate(orbit)}
        if out[self.root] != 0 or any(
            out[self.transitions[state]] != (phase + 1) % modulus
            for state, phase in out.items()
        ):
            raise AssertionError("equivariance proof violated")
        return out


@dataclass(frozen=True)
class FreeUnaryRay:
    """A SYMBOLIC free term algebra S^n(root); not a finite observed source."""
    origin: str = "origin"

    def __post_init__(self):
        if type(self.origin) is not str or not self.origin:
            raise ClockSourceError("symbolic origin required")

    def state(self, exponent: int) -> tuple[str, int]:
        _nat(exponent, "free-ray exponent", minimum=0, maximum=10**9)
        return (self.origin, exponent)

    def successor(self, state: tuple[str, int]) -> tuple[str, int]:
        if (type(state) is not tuple or len(state) != 2 or
            state[0] != self.origin or type(state[1]) is not int or
            not 0 <= state[1] < 10**9):
            raise ClockSourceError("not a well-formed ray term")
        return self.state(state[1] + 1)

    def quotient(self, modulus: int, exponent: int) -> int:
        _nat(modulus, "clock modulus")
        return self.state(exponent)[1] % modulus


@dataclass(frozen=True)
class RootedCycle:
    """A freshly generated, genuinely connected rooted cyclic clock machine.

    Splicing is an INSTRUMENT CONSTRUCTION, never a hidden quotient map
    from the newly created C_(m+1) to the old C_m.
    """
    transition: tuple[int, ...]
    source_id: str = "constructed-instrument"

    def __post_init__(self) -> None:
        s = FiniteUnarySource(self.transition, 0, self.source_id).orbit_signature()
        if s["preperiod"] or s["period"] != len(self.transition):
            raise ClockSourceError("constructed clock must be one full connected cycle")

    @classmethod
    def initial(cls, source_id: str = "constructed-instrument") -> "RootedCycle":
        return cls((0,), source_id)

    @property
    def period(self) -> int:
        return len(self.transition)

    def splice(self, state_budget: int = 10000) -> "RootedCycle":
        """Insert a fresh state immediately before root, replay from root."""
        _nat(state_budget, "finite-state memory budget")
        m = self.period
        if m + 1 > state_budget:
            raise ClockSourceError("source machine has no budget for a fresh state")
        orbit = FiniteUnarySource(self.transition, 0, self.source_id).orbit_signature()["visited"]
        predecessor = orbit[-1]
        if self.transition[predecessor] != 0:
            raise AssertionError("invalid rooted predecessor")
        arrows = list(self.transition)
        arrows[predecessor] = m
        arrows.append(0)
        output = RootedCycle(tuple(arrows), self.source_id)
        if output.period != m + 1:
            raise AssertionError("new construction did not extend the clock")
        return output

    def quotient_to(self, smaller: "RootedCycle") -> dict[int, int]:
        """Genuine rooted equivariant map exists only for divisibility."""
        if not isinstance(smaller, RootedCycle):
            raise ClockSourceError("target must be an authenticated rooted cycle")
        return FiniteUnarySource(self.transition, 0, self.source_id).factor_to(smaller.period)


def periodic_shadow(prefix_length: int) -> dict:
    """Finite shadow indistinguishable from a free ray on a bounded path prefix."""
    _nat(prefix_length, "number of finite observed edges", minimum=0, maximum=9998)
    m = prefix_length + 2
    source = FiniteUnarySource(tuple((j+1) % m for j in range(m)),0,"periodic-shadow")
    sig = source.orbit_signature()
    return {"observed_edges": prefix_length,
            "states_before_horizon_all_distinct": len(sig["visited"]) > prefix_length,
            "actual_repetition_at": sig["period"],
            "free_orbit_certified": False,
            "shadow_period": sig["period"]}


def minimal_superclock(periods: tuple[int, ...]) -> dict:
    """Exact minimum period of a rooted cycle factoring all declared clocks."""
    if type(periods) is not tuple or not periods or len(periods) > 1024:
        raise ClockSourceError("finite nonempty tuple of period observations required")
    least = 1
    for period in periods:
        _nat(period, "observed actual return period", maximum=10000)
        least = lcm(least, period)
    return {"requested_periods": periods, "minimum_period": least,
            "all_quotient_maps_exist": all(least % m == 0 for m in periods),
            "rooted_superclock_state_lower_bound": least,
            "full_cartesian_product_not_required": True}


def minimal_clock_growth(horizon: int, *, materialized_clock_budget: int = 1024) -> tuple[dict, ...]:
    """Construct each C_m by edge splice; compute minimal common clock by lcm.

    Materialize and PROVE small C_m; record large L_m only as a symbolic exact
    consequence of divisibility, NOT an actually enumerated L_m-state machine.
    """
    _nat(horizon, "finite period horizon", maximum=600)
    _nat(materialized_clock_budget, "constructed clock state budget")
    if horizon > materialized_clock_budget:
        raise ClockSourceError("finite instrument budget cannot construct all requested clocks")
    c = RootedCycle.initial()
    least = 1
    rows = []
    for m in range(1,horizon + 1):
        if m > 1:
            c = c.splice(materialized_clock_budget)
        if c.period != m:
            raise AssertionError("observed period differs from clock constructor")
        next_least = lcm(least, c.period)
        q = next_least // least
        if q > 1:
            w = m
            depth = 0
            while w % q == 0:
                w //= q
                depth += 1
            # A jump occurring at m must be exactly a prime-power level.
            if w != 1 or depth < 1:
                raise AssertionError("unexpected non-prime-power capacity jump")
        else:
            depth = 0
        rows.append({"horizon":m, "new_clock_actual_period":c.period,
                     "minimum_joint_period":next_least, "prior_joint_period":least,
                     "new_capacity_factor":q, "jet_exponent":depth,
                     "new_observer_is_quotient_of_previous": (m==1 or m%(m-1)==0),
                     "joint_machine_materialized":False,
                     "finite_clock_constructed_and_verified":True})
        least=next_least
    return tuple(rows)


def join_irreducible_periods(horizon: int) -> tuple[int, ...]:
    """In the divisor/lcm lattice, n is join-irreducible iff no proper factors join to n.

    The observed horizons n <= H contain every join-irreducible from the
    FULL divisor lattice of L_H, as all such elements are prime powers <=H.
    This function deliberately uses no prime-number oracle.
    """
    _nat(horizon, "finite join-lattice horizon", maximum=400)
    found = []
    for n in range(2,horizon+1):
        proper = [d for d in range(1,n) if n % d == 0]
        if minimal_superclock(tuple(proper))["minimum_period"] < n:
            found.append(n)
    return tuple(found)


def period_jets(horizon: int) -> tuple[dict, ...]:
    """Per-epoch symbolic log-cost log(q), q=1 or an authentic prime source.

    A value `jet_base=1` means no prime-power impulse (Lambda(n)=0).
    No real transcendental logarithm is evaluated in this exact finite engine.
    """
    return tuple({"n":row["horizon"],"jet_base":row["new_capacity_factor"],
                  "jet_exponent":row["jet_exponent"],
                  "meaning":"log(jet_base) exact symbolic"}
                 for row in minimal_clock_growth(horizon))


def exact_log_current_coefficients(horizon: int, beta: int) -> dict[int, Fraction]:
    """Presents sum Lambda(n)/n^beta as a dictionary base-p -> rational weight.

    Output means: sum over p of coefficient[p] * log(p), no floats.
    This is a FINITE Dirichlet polynomial, not evaluation at critical line.
    """
    _nat(beta,"integer Dirichlet exponent",minimum=2,maximum=20)
    coeff:dict[int,Fraction]={}
    for j in period_jets(horizon):
        p=j["jet_base"]
        if p>1:
            coeff[p]=coeff.get(p,Fraction(0))+Fraction(1,j["n"]**beta)
    return dict(sorted(coeff.items()))


def central_binomial_state_bound(horizon: int) -> dict:
    """Elementary rigorous information/state-budget lower bound for joint clocks.

    The paper proves binom(H-1,k)|LCM(1..H) via Legendre valuations.
    Thus L_H >= max binom(H-1,k) >= 2^(H-1)/H.
    """
    _nat(horizon,"state-bound horizon",maximum=600)
    least = minimal_clock_growth(horizon)[-1]["minimum_joint_period"]
    maximum = max(comb(horizon-1,k) for k in range(horizon))
    if least % maximum != 0:
        # Divisibility is only guaranteed for each coefficient, not generally
        # for the maximum as a separate construction; this one is a coefficient.
        raise AssertionError("central binomial divisibility failed")
    if least*horizon < 2**(horizon-1):
        raise AssertionError("elementary lower bound failed")
    return {"horizon":horizon,"least_period":least,
            "central_binomial_coefficient":maximum,
            "elementary_exponential_bound_numerator":2**(horizon-1),
            "elementary_exponential_bound_denominator":horizon,
            "state_lower_bound":least,
            "binary_bits_needed":(least-1).bit_length(),
            "bound_checked_exactly":True}


def source_vs_instrument_no_ghost(source_period: int, instrument_period: int) -> dict:
    """New internal clock does not upgrade the source's real quotient spectrum."""
    _nat(source_period,"external source period",maximum=1000)
    _nat(instrument_period,"new instrument period",maximum=1000)
    src=FiniteUnarySource(tuple((i+1)%source_period for i in range(source_period)),source_id="external")
    instrument=RootedCycle.initial("internal")
    for _ in range(instrument_period-1):
        instrument=instrument.splice(state_budget=1000)
    actual=src.can_factor_to(instrument.period)
    return {"source_period":source_period,
            "instrument_constructed_period":instrument.period,
            "joint_synchronized_period":lcm(source_period,instrument.period),
            "instrument_is_source_factor":actual,
            "new_instrument_cannot_authenticate_new_source_prime": not actual,
            "distinct_source_id_preserved":True}
