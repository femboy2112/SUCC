"""A positive-entropy logistic carrier with a deterministic period-2 E factor.

At the first band-merge Misiurewicz parameter alpha, the unique root of
P(alpha)=alpha**3-2alpha**2-4alpha-8 in (3,4), the *exact algebraic*
postcritical orbit is
    1/2 -> alpha/4 -> 1/alpha -> 1-1/alpha -> fixed.

Its invariant Markov core has three cells A,B,C with A->C, B->C,
C->A/B.  The two-class phase A|B -> C -> A|B is deterministic (outside
boundary preorbits), while the genuine Markov graph has positive topological
entropy log(sqrt(2)).  A chosen Parry symbolic probability law realizes
entropy rate 1/2 bit per step. It is NOT identified with the physical acim.

All symbolic source and identity calculations are exact in Q[alpha]/(P).
Any displayed decimal isolation is a certified rational sign bracket, not a
floating-point proof of the identity. Source stamps are not authentication.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable, Mapping

from .logistic_observer_tree import Source


class MisiurewiczError(ValueError):
    """Bad exact algebra, source version, Markov path, or observation stage."""


def _q(x: int | F) -> F:
    if type(x) is bool or not isinstance(x, (int, F)):
        raise MisiurewiczError("Only exact integers/Fractions allowed")
    return F(x)


@dataclass(frozen=True)
class CubicElement:
    """Q[alpha]/(alpha^3-2alpha^2-4alpha-8), basis (1,a,a^2)."""
    coeffs: tuple[F, F, F]

    def __post_init__(self) -> None:
        if type(self.coeffs) is not tuple or len(self.coeffs)!=3:
            raise MisiurewiczError("Cubic algebra has exactly three basis coefficients")
        object.__setattr__(self, "coeffs", tuple(_q(x) for x in self.coeffs))

    @staticmethod
    def coerce(other: object) -> "CubicElement":
        if isinstance(other,CubicElement):
            return other
        return CubicElement((_q(other),F(0),F(0)))

    def __add__(self,other: object) -> "CubicElement":
        b=self.coerce(other)
        return CubicElement(tuple(a+c for a,c in zip(self.coeffs,b.coeffs)))

    def __radd__(self,other: object) -> "CubicElement":
        return self+other

    def __neg__(self) -> "CubicElement":
        return CubicElement(tuple(-x for x in self.coeffs))

    def __sub__(self,other: object) -> "CubicElement":
        return self+-self.coerce(other)

    def __rsub__(self,other: object) -> "CubicElement":
        return self.coerce(other)+-self

    def __mul__(self,other: object) -> "CubicElement":
        b=self.coerce(other)
        product=[F(0)]*5
        for i,a in enumerate(self.coeffs):
            for j,c in enumerate(b.coeffs):
                product[i+j]+=a*c
        for k in (4,3):
            h=product[k]
            product[k]=F(0)
            product[k-1]+=2*h
            product[k-2]+=4*h
            product[k-3]+=8*h
        return CubicElement(tuple(product[:3]))

    def __rmul__(self,other: object) -> "CubicElement":
        return self*other

    def __truediv__(self,other: int | F) -> "CubicElement":
        q=_q(other)
        if q==0:
            raise MisiurewiczError("Division by zero rational")
        return CubicElement(tuple(x/q for x in self.coeffs))

    def __pow__(self,exponent: int) -> "CubicElement":
        if type(exponent) is not int or exponent<0:
            raise MisiurewiczError("Only nonnegative integral powers")
        z=ONE
        base=self
        while exponent:
            if exponent&1:
                z=z*base
            exponent>>=1
            if exponent:
                base=base*base
        return z

    def as_strings(self) -> tuple[str,str,str]:
        return tuple(map(str,self.coeffs))


ZERO=CubicElement((F(0),F(0),F(0)))
ONE=CubicElement((F(1),F(0),F(0)))
ALPHA=CubicElement((F(0),F(1),F(0)))
INV_ALPHA=(ALPHA*ALPHA-2*ALPHA-4)/8
CRITICAL=ONE/2
MAXIMUM=ALPHA/4
LOW=INV_ALPHA
FIXED=ONE-INV_ALPHA
BOUNDARIES=(LOW,CRITICAL,FIXED,MAXIMUM)


def cubic_at(q: int | F) -> F:
    x=_q(q)
    return x*x*x-2*x*x-4*x-8


def isolate_alpha() -> tuple[F,F]:
    """Provably unique real root in this rational bracket by p'=(3x+2)(x-2)."""
    lo,hi=F(3678573510428,10**12),F(3678573510429,10**12)
    if not 3<lo<hi<4 or not cubic_at(lo)<0<cubic_at(hi):
        raise AssertionError("Rational root isolation certificate failed")
    return lo,hi


def sign_algebraic(value: CubicElement | int | F) -> int:
    """Sound sign of a quadratic expression in the unique real cubic root.

    Uses exact rational interval bounds, bisection of p(alpha)=0, and never
    floating-point root approximations. Raises if a sign is not certified.
    """
    v=CubicElement.coerce(value)
    if v==ZERO:
        return 0
    lo,hi=isolate_alpha()
    for _ in range(128):
        bounds=[]
        for coefficient,lower,upper in zip(v.coeffs,
            (F(1),lo,lo*lo),(F(1),hi,hi*hi)):
            bounds.append((coefficient*lower,coefficient*upper) if coefficient>=0
                          else (coefficient*upper,coefficient*lower))
        minimum=sum((x[0] for x in bounds),F(0))
        maximum=sum((x[1] for x in bounds),F(0))
        if minimum>0:
            return 1
        if maximum<0:
            return -1
        mid=(lo+hi)/2
        mid_sign=cubic_at(mid)
        if mid_sign==0:
            exact_value=sum((c*mid**i for i,c in enumerate(v.coeffs)),F(0))
            return (exact_value>0)-(exact_value<0)
        if mid_sign<0:
            lo=mid
        else:
            hi=mid
    raise MisiurewiczError("Algebraic sign not isolated within declared proof budget")


def compare_algebraic(a: CubicElement | int | F,
                      b: CubicElement | int | F) -> int:
    return sign_algebraic(CubicElement.coerce(a)-CubicElement.coerce(b))


def classify_actual_cell(state: CubicElement | int | F) -> int:
    """Exact source classifier on J, refusing shared Markov boundaries."""
    x=CubicElement.coerce(state)
    signs=tuple(compare_algebraic(x,endpoint) for endpoint in BOUNDARIES)
    if 0 in signs:
        raise MisiurewiczError("Markov boundary / eventually fixed source ambiguity")
    for i in range(3):
        if signs[i]==1 and signs[i+1]==-1:
            return i
    raise MisiurewiczError("Actual source outside certified invariant core J")


def actual_source_cells(initial: CubicElement | int | F,
                        steps: int) -> tuple[int,...]:
    """Replay a genuine original algebraic logistic state, not just a graph walk."""
    if type(steps) is not int or not 0<=steps<=30:
        raise MisiurewiczError("Exact replay horizon must be 0..30")
    x=CubicElement.coerce(initial)
    result=[]
    for _ in range(steps+1):
        result.append(classify_actual_cell(x))
        x=f(x)
    if not legal_path(result):
        raise AssertionError("Actual source orbit violated exact Markov graph")
    return tuple(result)


def f(x: CubicElement) -> CubicElement:
    if not isinstance(x,CubicElement):
        raise MisiurewiczError("Only exact algebraic source states allowed")
    return ALPHA*x*(ONE-x)


def postcritical_orbit_certificate() -> dict:
    """Exact Q(alpha) identities, independent of float root iteration."""
    p=ALPHA**3-2*ALPHA**2-4*ALPHA-8
    orbit=(CRITICAL, f(CRITICAL), f(f(CRITICAL)),
           f(f(f(CRITICAL))),f(f(f(f(CRITICAL)))))
    expected=(CRITICAL,MAXIMUM,LOW,FIXED,FIXED)
    if p!=ZERO or orbit!=expected or ALPHA*INV_ALPHA!=ONE:
        raise AssertionError("Postcritical orbit or quotient-reduction mismatch")
    return {"minimum_polynomial_remainder_zero":p==ZERO,
            "inverse_alpha_exact":ALPHA*INV_ALPHA==ONE,
            "postcritical_positions":tuple(x.as_strings() for x in orbit),
            "position_aliases":("critical","maximum","1/alpha","fixed","fixed"),
            "isolating_bracket":tuple(map(str,isolate_alpha())),
            "root_unique_on_3_to_4_by_positive_derivative":True}


CELLS=((LOW,CRITICAL),(CRITICAL,FIXED),(FIXED,MAXIMUM))
# A,B = left phase (0); C = right phase (1).
EXPECTED_A=((0,0,1),(0,0,1),(1,1,0))
PARRY_ROWS=({2:F(1)},{2:F(1)},{0:F(1,2),1:F(1,2)})
PARRY_PRIOR=(F(1,4),F(1,4),F(1,2))


def markov_adjacency() -> tuple[tuple[int,int,int],...]:
    """Build adjacency FROM image endpoints in the established strict order.

    Exact endpoint identities plus 1/alpha < c < (1-1/alpha) < alpha/4
    and logistic monotonicity on each side of c certify the whole image.
    """
    rows=[]
    for lower,upper in CELLS:
        images=(f(lower),f(upper))
        try:
            mapped=tuple(BOUNDARIES.index(t) for t in images)
        except ValueError as e:
            raise AssertionError("Image escaped true Markov endpoints") from e
        lo,hi=min(mapped),max(mapped)
        rows.append(tuple(int(lo<=i<hi) for i in range(3)))
    result=tuple(rows)
    if result!=EXPECTED_A:
        raise AssertionError("Exact source images disagree with declared graph")
    return result


def phase(cell: int) -> int:
    if type(cell) is not int or cell not in (0,1,2):
        raise MisiurewiczError("Cell must be A=0, B=1 or C=2")
    return int(cell==2)


def legal_path(cells: Iterable[int]) -> bool:
    seq=tuple(cells)
    if not seq:
        raise MisiurewiczError("Need at least one observed state")
    for c in seq:
        phase(c)
    a=markov_adjacency()
    return all(a[x][y]==1 for x,y in zip(seq,seq[1:]))


def path_count(start_cell: int, steps: int) -> int:
    phase(start_cell)
    if type(steps) is not int or not 0<=steps<=1000:
        raise MisiurewiczError("Step count must be 0..1000")
    counts=[0,0,0]
    counts[start_cell]=1
    a=markov_adjacency()
    for _ in range(steps):
        counts=[sum(counts[i]*a[i][j] for i in range(3)) for j in range(3)]
    return sum(counts)


def path_entropy_bits(start_cell: int, steps: int) -> int:
    """Under Parry choices, every source-path branch choice has one fair bit."""
    phase(start_cell)
    if type(steps) is not int or steps<0:
        raise MisiurewiczError("Need nonnegative steps")
    return (steps+1)//2 if start_cell==2 else steps//2


def alternate_stationary_symbolic_source(prob_A: int | F) -> dict:
    """Ablate fair Parry choices, retain the same source-derived phase law.

    This defines an ALTERNATE symbolic Markov measure on the certified graph,
    not the logistic map's unknown natural acim. Conditional C->A has mass p,
    C->B has mass 1-p. The stationary phase is always balanced, whereas the
    microscopic information rate is (1/2)*H_binary(p), which varies with p.
    Endpoint p=0 or 1 loses microscopic metric entropy, not topological entropy.
    """
    p=_q(prob_A)
    if not F(0)<=p<=F(1):
        raise MisiurewiczError("C->A source probability must lie in [0,1]")
    transition=(
        (F(0),F(0),F(1)),
        (F(0),F(0),F(1)),
        (p,F(1)-p,F(0)),
    )
    stationary=(p/2,(F(1)-p)/2,F(1,2))
    if any(sum(row,F(0))!=1 for row in transition):
        raise AssertionError("Mutated transition not stochastic")
    evolved=tuple(sum((stationary[i]*transition[i][j]
                       for i in range(3)),F(0)) for j in range(3))
    if evolved!=stationary or stationary[0]+stationary[1]!=F(1,2):
        raise AssertionError("Mutated source does not preserve phase balance")
    return {
       "chosen_C_to_A_probability":p,
       "transition_matrix":transition,
       "stationary_prior":stationary,
       "stationary_phase_probabilities":(F(1,2),F(1,2)),
       "phase_covariance_lag_even":F(1,4),
       "phase_covariance_lag_odd":-F(1,4),
       "microscopic_conditional_entropy_rate_bits_formula":"H_binary(p)/2",
       "microscopic_entropy_strictly_positive":F(0)<p<F(1),
       "source_law_is_identified_natural_acim":False,
    }


def propagate_parry(initial: Mapping[int,int|F], steps:int) -> tuple[F,F,F]:
    if type(steps) is not int or steps<0 or steps>1000:
        raise MisiurewiczError("Step count must be 0..1000")
    distribution=[F(0),F(0),F(0)]
    if not initial:
        raise MisiurewiczError("Empty initial law")
    for state,mass in initial.items():
        phase(state)
        weight=_q(mass)
        if weight<0:
            raise MisiurewiczError("Negative source weight")
        distribution[state]=weight
    if sum(distribution)!=1:
        raise MisiurewiczError("Source law must normalize to one")
    for _ in range(steps):
        new=[F(0),F(0),F(0)]
        for i,row in enumerate(PARRY_ROWS):
            for j,p in row.items():
                new[j]+=distribution[i]*p
        distribution=new
    return tuple(distribution)


def phase_parry_receipt(steps:int) -> dict:
    if type(steps) is not int or steps<0 or steps>1000:
        raise MisiurewiczError("Step count 0..1000")
    a=markov_adjacency()
    if any(phase(i)==phase(j) for i,row in enumerate(a)
           for j,allowed in enumerate(row) if allowed):
        raise AssertionError("Phase flip source-square failed")
    stationary=propagate_parry(dict(enumerate(PARRY_PRIOR)),steps)
    if stationary!=PARRY_PRIOR:
        raise AssertionError("Parry stationary source failed")
    return {
        "markov_matrix":a,
        "parry_rows":tuple(tuple(row.get(j,F(0)) for j in range(3)) for row in PARRY_ROWS),
        "parry_stationary_prior":stationary,
        "phase_transition":((0,1),(1,0)),
        "stationary_phase_masses":(sum(stationary[:2]),stationary[2]),
        "two_step_from_A":propagate_parry({0:F(1)},2),
        "two_step_from_C":propagate_parry({2:F(1)},2),
        "phase_alternates_for_every_legal_nondisputed_path":True,
        "expected_fresh_symbol_bits_per_step":F(1,2),
        "coarse_phase_entropy_rate_bits":F(0),
        "path_count_from_A":path_count(0,steps),
        "path_count_from_C":path_count(2,steps),
        "full_source_boundary_orbits_excluded":True,
    }


def dual_phase_correlation(lag: int) -> dict:
    """Exact E/E'' correlations after source-declared lag-parity transport.

    Under the stationary Parry symbolic source, P(phase0=0)=P(phase0=1)=1/2
    and phase_t=phase0 XOR (t%2). Raw phase covariance is (-1)^lag / 4.
    Transport later back with the *declared* parity orientation and the
    reconstructed Boolean phase has +1/4 covariance for every lag.
    This is classical periodic-source correlation, NOT a quantum phasor.
    """
    if type(lag) is not int or lag<0:
        raise MisiurewiczError("Require a nonnegative integer lag")
    return {
        "lag":lag,
        "phase0_masses":(F(1,2),F(1,2)),
        "raw_phase_covariance":F(1 if lag%2==0 else -1,4),
        "parity_transport_sign":1 if lag%2==0 else -1,
        "transported_phase_covariance":F(1,4),
        "raw_phase_mutual_information_bits":1,
        "phase_entropy_rate_bits":F(0),
        "conditional_micro_entropy_rate_bits_under_Parry":F(1,2),
    }


@dataclass(frozen=True)
class PhaseReceipt:
    source: Source
    step: int
    cell: int

    def __post_init__(self) -> None:
        if not isinstance(self.source,Source):
            raise MisiurewiczError("Mathematical source identity required")
        if type(self.step) is not int or self.step<0:
            raise MisiurewiczError("Nonnegative receipt stage required")
        phase(self.cell)


def verify_E_Eprime_phase(first: PhaseReceipt, later: PhaseReceipt) -> dict:
    """Necessary quotient agreement, not full source history verification.

    A phase-valid pair need not independently prove the interior trajectory.
    """
    if first.source!=later.source or later.step<first.step:
        raise MisiurewiczError("Different original source/version or reversed time")
    lag=later.step-first.step
    expected=phase(first.cell)^(lag&1)
    if phase(later.cell)!=expected:
        raise MisiurewiczError("Dual E reports violate source Markov phase law")
    return {"source":first.source,"lag":lag,"phase_valid":True,
            "complete_micro_path_recovered":False,
            "physical_source_authenticated":False}
