"""Source-faithful chaotic observer quotients, exact on finite rational carriers.

Two intentionally different contracts:
  * r=4: a finite-window stochastic Markov PRESENTATION of the stationary
    Bernoulli symbolic process under the arcsine invariant logistic measure.
    The underlying source dynamics remain deterministic and chaotic.
  * 0<r<=4: finite rational SOURCE ENSEMBLES with evolving pushforward laws and
    Bayes-correct time-indexed inverse kernels. No natural invariant measure,
    chaos regime, or symbolic Markov property is assumed at generic r.

A formal mathematical source tag is not empirical instrument authentication.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Mapping, Sequence
from collections import defaultdict

from .logistic_observer_tree import Source


class ChaosQuotientError(ValueError):
    """Malformed source, unsupported parameter, stale/mismatched observation."""


def exact(value: int | F) -> F:
    if isinstance(value, bool) or not isinstance(value, (int, F)):
        raise ChaosQuotientError("Require exact integer/Fraction, not float or bool")
    return F(value)


def parameter(value: int | F) -> F:
    r = exact(value)
    if not 0 < r <= 4:
        raise ChaosQuotientError("Logistic parameter must be in (0,4]")
    return r


def logistic_r(r: int | F, x: int | F) -> F:
    r, x = parameter(r), exact(x)
    if not 0 <= x <= 1:
        raise ChaosQuotientError("Logistic state must lie in [0,1]")
    return r * x * (1 - x)


def postimage_interval(r: int | F) -> tuple[F, F]:
    """A forward invariant carrier after one iteration, NOT always onto itself."""
    return F(0), parameter(r) / 4


def postcritical_threshold(r: int | F) -> F:
    r = parameter(r)
    return logistic_r(r, r / 4)


def phantom_terminal_fraction(r: int | F) -> F:
    """Geometric fraction of [0,r/4] lacking the right inverse for 2<r<=4.

    This is a length ratio on a declared carrier, NOT the invariant measure
    or probability of an actual trajectory entering the region.
    """
    r = parameter(r)
    if r <= 2:
        raise ChaosQuotientError("The two-monotone-branch geometry needs 2<r<=4")
    return postcritical_threshold(r) / (r / 4)


def admissible_pair_from_witness(r: int | F, predecessor: int | F) -> dict:
    """Test inverse-branch admission using a verified rational source witness.

    The two algebraic roots x,1-x produce the same y=f_r(x).  Only roots in
    the declared post-first-image interval I_r=[0,r/4] are source-admissible.
    This is NOT the posterior for an unknown stochastic source prior.
    """
    r, x = parameter(r), exact(predecessor)
    hi = r / 4
    if not 0 <= x <= hi:
        raise ChaosQuotientError("Witness must inhabit post-first-image carrier")
    y = logistic_r(r, x)
    candidates = tuple(sorted({x, 1-x}))
    admissible = tuple(v for v in candidates if 0 <= v <= hi)
    if not admissible or any(logistic_r(r, v) != y for v in admissible):
        raise AssertionError("Invalid inverse-branch algebra")
    return {
        "parameter": r, "terminal": y, "carrier_upper": hi,
        "postcritical_threshold": postcritical_threshold(r),
        "algebraic_preimages": candidates,
        "source_admissible_preimages": admissible,
        "algebraic_equal_branch_mean": sum(candidates, F(0))/len(candidates),
        "admissible_equal_branch_mean": sum(admissible, F(0))/len(admissible),
        "has_phantom_branch": len(candidates) > len(admissible),
    }


def _normalize_law(law: Mapping[int, int | F], width: int) -> dict[int, F]:
    if not law:
        raise ChaosQuotientError("Source law must be nonempty")
    result: dict[int, F] = {}
    for state, value in law.items():
        if type(state) is not int or not 0 <= state < 1 << width:
            raise ChaosQuotientError("Window source key outside finite bit space")
        mass = exact(value)
        if mass < 0:
            raise ChaosQuotientError("Negative mass forbidden")
        result[state] = mass
    if sum(result.values(), F(0)) != 1:
        raise ChaosQuotientError("Finite source law must sum to one")
    return result


@dataclass(frozen=True)
class SymbolWindow:
    """Last-/next-word representation of fair Bernoulli itineraries at r=4.

    A state w encodes an m-bit future symbolic word.  On applying the true
    one-sided shift, w'=(2w+b) mod 2**m. The unknown *new* bit b has
    Bernoulli law, conditional on the observed word, under a specified source
    ensemble. For the logistic natural invariant law b is exactly fair.

    This is a conditional stochastic quotient, NOT a continuous deterministic
    factor f4 -> finite-state f_m, and NOT a measurement of true randomness.
    """
    width: int
    new_one_probability: F = F(1, 2)

    def __post_init__(self) -> None:
        if type(self.width) is not int or not 1 <= self.width <= 12:
            raise ChaosQuotientError("Window width must be 1..12 bits")
        p = exact(self.new_one_probability)
        if not 0 < p < 1:
            raise ChaosQuotientError("Full-support Bernoulli source needs 0<p<1")
        object.__setattr__(self, "new_one_probability", p)

    @property
    def size(self) -> int:
        return 1 << self.width

    def row(self, state: int) -> dict[int, F]:
        if type(state) is not int or not 0 <= state < self.size:
            raise ChaosQuotientError("Invalid source window")
        base = (state << 1) & (self.size - 1)
        return {base: 1 - self.new_one_probability,
                base + 1: self.new_one_probability}

    def push(self, law: Mapping[int, int | F], steps: int = 1) -> dict[int, F]:
        if type(steps) is not int or steps < 0:
            raise ChaosQuotientError("Nonnegative step count required")
        current = _normalize_law(law, self.width)
        for _ in range(steps):
            nxt: dict[int, F] = defaultdict(F)
            for word, mass in current.items():
                for successor, transition in self.row(word).items():
                    nxt[successor] += mass * transition
            current = dict(sorted(nxt.items()))
        return current

    def equilibrium(self) -> dict[int, F]:
        p = self.new_one_probability
        return {word: (p ** word.bit_count()) *
                ((1-p) ** (self.width - word.bit_count()))
                for word in range(self.size)}

    def causal_path_count(self, steps: int) -> int:
        """Number of distinct full transition paths from a known first word."""
        if type(steps) is not int or steps < 0:
            raise ChaosQuotientError("Nonnegative step count required")
        return 1 << steps

    def terminal_support_count(self, steps: int) -> int:
        """From any fixed initial word, given a full-support new-bit source."""
        if type(steps) is not int or steps < 0:
            raise ChaosQuotientError("Nonnegative step count required")
        return 1 << min(steps, self.width)

    def deterministic_factor_counterexample(self, word: int) -> tuple[int, int]:
        """Two legal futures with identical observed m-bit word, different next.

        Thus there cannot be a universal F_m with pi_m shift=F_m pi_m.
        This does not prohibit an exactly specified Markov projection in law.
        """
        row = self.row(word)
        outcomes = tuple(sorted(row))
        if len(outcomes) != 2 or outcomes[0] == outcomes[1]:
            raise AssertionError("Full-support bit successor branches collapsed")
        return outcomes

    def dual_common_information(self, lag: int) -> dict:
        """Exact DB1 common factor of current/future m-windows at lag n.

        Under the stationary iid full-support symbol source, their bipartite
        joint-support graph has 2**max(m-n,0) components, indexed by the
        OVERLAPPING original symbols. For a fair source, entropy and mutual
        information equal this number of shared bits, not just an analogy.
        General biased symbols have different numeric Shannon entropies.
        """
        if type(lag) is not int or lag < 0:
            raise ChaosQuotientError("Nonnegative lag required")
        overlap = max(self.width-lag, 0)
        return {
            "lag":lag, "shared_symbol_count":overlap,
            "maximal_common_deterministic_component_count":1<<overlap,
            "terminal_conditional_support_count":1<<min(lag,self.width),
            "fair_source_mutual_information_bits": overlap if self.new_one_probability==F(1,2) else None,
            "fair_source_conditional_entropy_bits": min(lag,self.width) if self.new_one_probability==F(1,2) else None,
        }

    def source_audit(self, steps: int) -> dict:
        if type(steps) is not int or not 0 <= steps <= 24:
            raise ChaosQuotientError("Audit step count must be 0..24")
        law = self.push({0: F(1)}, steps)
        invariant = self.equilibrium()
        return {
            "width": self.width,
            "new_bit_probability": self.new_one_probability,
            "terminal_support_count": len([v for v in law.values() if v]),
            "terminal_minimum_new_bits": min(steps,self.width),
            "causal_path_count": self.causal_path_count(steps),
            "full_path_minimum_new_bits": steps,
            "rank_one_completion_reached": law == invariant,
            "conditional_one_step_has_two_futures":
                len(self.deterministic_factor_counterexample(0)) == 2,
        }


@dataclass(frozen=True)
class FiniteLogisticSource:
    """Exact time-indexed source ensemble, with no unstated invariant prior.

    Initial atomic carrier labels are *separate from current values*.  This
    prevents source aliasing when the logistic map merges two states x,1-x.
    Source priors and all transition/conditional laws are exact rational.
    """
    source: Source
    r: F
    originals: tuple[F, ...]
    weights: tuple[F, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.source, Source):
            raise ChaosQuotientError("Declared original Source object required")
        r = parameter(self.r)
        object.__setattr__(self, "r", r)
        states = tuple(exact(v) for v in self.originals)
        ps = tuple(exact(v) for v in self.weights)
        if not states or len(states) != len(ps) or len(set(states)) != len(states):
            raise ChaosQuotientError("Distinct labeled starting states with probabilities required")
        if any(not 0 <= v <= 1 for v in states):
            raise ChaosQuotientError("Source state outside [0,1]")
        if any(p <= 0 for p in ps) or sum(ps, F(0)) != 1:
            raise ChaosQuotientError("Strictly positive normalized original prior required")
        object.__setattr__(self, "originals", states)
        object.__setattr__(self, "weights", ps)

    def orbit(self, steps: int) -> tuple[tuple[F, ...], ...]:
        if type(steps) is not int or not 0 <= steps <= 50:
            raise ChaosQuotientError("Finite rational orbit horizon must be 0..50")
        trajectory = [self.originals]
        for _ in range(steps):
            trajectory.append(tuple(logistic_r(self.r,x) for x in trajectory[-1]))
        return tuple(trajectory)

    def law(self, step: int) -> dict[F,F]:
        states = self.orbit(step)[-1]
        masses: dict[F,F] = defaultdict(F)
        for x, w in zip(states,self.weights):
            masses[x] += w
        return dict(sorted(masses.items()))

    def reverse_kernel(self, step: int) -> dict[F,dict[F,F]]:
        """K_t(x|y)=mu_t(x)/mu_{t+1}(y) for y=f(x), on ACTUAL support."""
        if type(step) is not int or not 0 <= step < 50:
            raise ChaosQuotientError("Reverse step must be 0..49")
        before, after = self.law(step), self.law(step+1)
        result: dict[F,dict[F,F]] = {}
        for y, nextmass in after.items():
            predecessors = {x: mass/nextmass for x,mass in before.items()
                            if logistic_r(self.r, x) == y}
            if sum(predecessors.values(),F(0)) != 1:
                raise AssertionError("Reverse Bayesian kernel failed normalization")
            result[y] = predecessors
        return result

    def backwards_target(self, targets: Sequence[int|F], steps: int) -> dict[F,F]:
        """Compose exact one-step K_t to get E[T(original)|X_steps=y]."""
        if len(targets) != len(self.originals):
            raise ChaosQuotientError("Original-source target dimension mismatch")
        values = {x: exact(v) for x,v in zip(self.originals,targets)}
        if type(steps) is not int or not 0 <= steps <= 50:
            raise ChaosQuotientError("Supported rational step count 0..50")
        for t in range(steps):
            kernel = self.reverse_kernel(t)
            values = {y: sum((p*values[x] for x,p in dist.items()),F(0))
                      for y,dist in kernel.items()}
        return values

    def direct_target(self, targets: Sequence[int|F], steps: int) -> dict[F,F]:
        """Independent direct source-index oracle, without reverse kernels."""
        if len(targets)!=len(self.originals):
            raise ChaosQuotientError("Original-source target dimension mismatch")
        vals = tuple(exact(v) for v in targets)
        current = self.orbit(steps)[-1]
        masses: dict[F,F] = defaultdict(F)
        numerators: dict[F,F] = defaultdict(F)
        for y,p,v in zip(current,self.weights,vals):
            masses[y] += p
            numerators[y] += p*v
        return {y: numerators[y]/masses[y] for y in sorted(masses)}

    def source_fiber(self, step: int, terminal: int | F,
                     chronology: Sequence[int] | None = None,
                     source: Source | None = None) -> tuple[F,...]:
        """Losslessly intersect original-source fibers with lawful branch history.

        chronology bit i is the side (<1/2 or >1/2) of the i-th observed state.
        Critical 1/2 is ambiguous and cannot be signed as either side.
        """
        if source is not None and source != self.source:
            raise ChaosQuotientError("Source/version mismatch in dual observer join")
        y=exact(terminal)
        if chronology is not None and (len(chronology)!=step or
             any(type(bit) is not int or bit not in (0,1) for bit in chronology)):
            raise ChaosQuotientError("Branch histories must match terminal time")
        path=self.orbit(step)
        result=[]
        for i,x in enumerate(self.originals):
            if path[-1][i] != y:
                continue
            if chronology is not None:
                seq=[stage[i] for stage in path[:-1]]
                if any(v==F(1,2) for v in seq):
                    raise ChaosQuotientError("Critical itinerary requires explicit convention")
                if tuple(int(v>F(1,2)) for v in seq)!=tuple(chronology):
                    continue
            result.append(x)
        return tuple(result)

    def claim_factors(self, targets: Sequence[int|F], step: int) -> bool:
        """SC1 exact source-fiber sufficiency for original target at time step."""
        if len(targets) != len(self.originals):
            raise ChaosQuotientError("Original-source target dimension mismatch")
        states = self.orbit(step)[-1]
        labels: dict[F,F] = {}
        for y,t in zip(states,targets):
            val=exact(t)
            if y in labels and labels[y] != val:
                return False
            labels[y] = val
        return True
