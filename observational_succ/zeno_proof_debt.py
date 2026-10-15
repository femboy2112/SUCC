"""Zeno proof debt: source-typed finite data and honest global certificates.

All arithmetic here is Fraction-exact.  Infinite-dimensional/compactness and
computability claims are paper theorems, NOT verified by finitely many tests.
Existing SUCC Stamp is reused; source, epoch, basis, domain must agree.

This module has NO predicate that declares RH true and NO access to zeta zeros.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable

from .zeno_certificate import Stamp, ZenoTypeError, rational, natural


class ProofDebtError(ZenoTypeError):
    """An invalid source law, certificate, stage, or missing mathematical gate."""


def rat(value: F | int) -> F:
    try:
        return rational(value)
    except ZenoTypeError as exc:
        raise ProofDebtError(str(exc)) from exc


def _named(value: str, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProofDebtError(f"nonempty {label} is required")
    return value


def _compatible(left: Stamp, right: Stamp) -> None:
    if left != right:
        raise ProofDebtError("SOURCE_EPOCH_BASIS_DOMAIN_MISMATCH")


@dataclass(frozen=True)
class ProofEvent:
    """Accounting statement; not a claim that a physical event occurred."""
    stamp: Stamp
    target: str
    index: int
    born: F
    discharged: F
    elapsed: F
    resource: F
    receipt: str

    def __post_init__(self):
        _named(self.target, "target")
        _named(self.receipt, "receipt")
        natural(self.index)
        for field in ("born", "discharged", "elapsed", "resource"):
            if rat(getattr(self, field)) < 0:
                raise ProofDebtError("proof/debt/time/resource entries must be nonnegative")


@dataclass(frozen=True)
class ProofDebtLedger:
    """Records birth and discharge, never erasing historical obligations.

    The ledger is about a mathematically declared target and source, not a
    physical event stream.  Actual event authorization is a separate SUCC
    NO-GHOST instrument contract, never manufactured here.
    """
    stamp: Stamp
    target: str
    initial: F
    events: tuple[ProofEvent, ...] = ()

    def __post_init__(self):
        _named(self.target, "target")
        if rat(self.initial) < 0:
            raise ProofDebtError("initial proof debt must be nonnegative")
        if not isinstance(self.events, tuple):
            raise ProofDebtError("immutable event-history tuple required")
        debt = rat(self.initial)
        for i, event in enumerate(self.events):
            _compatible(self.stamp, event.stamp)
            if self.target != event.target or i != event.index:
                raise ProofDebtError("SOURCE_OR_TARGET_HISTORY_DRIFT")
            debt += rat(event.born) - rat(event.discharged)
            if debt < 0:
                raise ProofDebtError("cannot discharge more outstanding obligations")

    @property
    def outstanding(self) -> F:
        return rat(self.initial) + sum((rat(e.born)-rat(e.discharged) for e in self.events), F(0))

    @property
    def elapsed(self) -> F:
        return sum((rat(e.elapsed) for e in self.events), F(0))

    @property
    def resource(self) -> F:
        return sum((rat(e.resource) for e in self.events), F(0))

    def append(self, event: ProofEvent) -> "ProofDebtLedger":
        return ProofDebtLedger(self.stamp, self.target, rat(self.initial), self.events+(event,))

    def snapshots(self) -> tuple[F, ...]:
        debt = rat(self.initial)
        out=[debt]
        for e in self.events:
            debt += rat(e.born)-rat(e.discharged)
            out.append(debt)
        return tuple(out)


@dataclass(frozen=True)
class AmortizedContract:
    """Source law: D_(n+1) <= q D_n + C r^n for ALL n>=0.

    A finite audited history checks only its own stages.  Extrapolation uses
    the separately declared universal source law, not those finite checks.
    """
    stamp: Stamp
    target: str
    d0_cap: F
    q: F
    birth_cap: F
    birth_ratio: F
    source_universal_law: bool = False

    def __post_init__(self):
        _named(self.target, "target")
        for f in ("d0_cap", "q", "birth_cap", "birth_ratio"):
            rat(getattr(self, f))
        if not (rat(self.d0_cap) >= 0 and rat(self.birth_cap)>=0):
            raise ProofDebtError("nonnegative initial/birth envelope required")
        if not (0<=rat(self.q)<1 and 0<=rat(self.birth_ratio)<1):
            raise ProofDebtError("strictly contracting q and r required")
        if type(self.source_universal_law) is not bool:
            raise ProofDebtError("universal premise must be explicit bool")

    def exact_upper(self, n: int) -> F:
        """D0*q^n+C*sum_(j<n)q^(n-1-j)r^j; valid CONDITIONAL on all stages."""
        natural(n)
        q,r,C=rat(self.q),rat(self.birth_ratio),rat(self.birth_cap)
        return rat(self.d0_cap)*q**n+C*sum((q**(n-1-j)*r**j for j in range(n)),F(0))

    def geometric_envelope(self) -> tuple[F,F]:
        """Universal K,rho with D_n<=K*rho^n for all n (source premise)."""
        m=max(rat(self.q),rat(self.birth_ratio))
        rho=(1+m)/2
        k=rat(self.d0_cap)+rat(self.birth_cap)*rho/(rho-m)**2
        return (k,rho)

    def horizon(self, tolerance: F, *, max_search: int=100000) -> tuple[int,F]:
        """Certificate for ALL subsequent n; requires universal source law.

        max_search is a computational budget.  Exhaustion is reported rather
        than being mistaken for an obstruction to mathematical convergence.
        """
        if not self.source_universal_law:
            raise ProofDebtError("UNVERIFIED_UNIVERSAL_SUCCESSOR_LAW")
        t=rat(tolerance)
        if t<=0:
            raise ProofDebtError("strictly positive tolerance required")
        natural(max_search,1)
        k,r=self.geometric_envelope()
        z=k
        for n in range(max_search+1):
            if z<=t:
                return (n,z)
            z*=r
        raise ProofDebtError("RESOURCE_BUDGET_EXHAUSTED_NOT_THEOREM_REFUTATION")

    def replay_observed(self, ledger: ProofDebtLedger) -> bool:
        _compatible(self.stamp,ledger.stamp)
        if ledger.target!=self.target or ledger.initial>self.d0_cap:
            raise ProofDebtError("debt contract mismatch")
        debt=rat(ledger.initial)
        for n,e in enumerate(ledger.events):
            next_debt=debt+rat(e.born)-rat(e.discharged)
            if next_debt>rat(self.q)*debt+rat(self.birth_cap)*rat(self.birth_ratio)**n:
                return False
            debt=next_debt
        return True


@dataclass(frozen=True)
class SourceFibre:
    """Full declared ORIGINAL-source target table and lawful finite report filters."""
    stamp: Stamp
    target: str
    sources: tuple[str, ...]
    values: tuple[F, ...]
    live: tuple[int, ...] | None = None
    history: tuple[tuple[str,str], ...] = ()

    def __post_init__(self):
        _named(self.target,"target")
        if not self.sources or len(self.sources)!=len(self.values):
            raise ProofDebtError("complete nonempty original source/value table required")
        if len(set(self.sources))!=len(self.sources) or any(not isinstance(s,str) or not s for s in self.sources):
            raise ProofDebtError("unique nonempty source labels required")
        for v in self.values:
            rat(v)
        if self.live is not None:
            if not self.live or len(set(self.live))!=len(self.live) or any(type(i) is not int or not 0<=i<len(self.sources) for i in self.live):
                raise ProofDebtError("nonempty original-source fiber required")

    def indices(self) -> tuple[int,...]:
        return self.live if self.live is not None else tuple(range(len(self.sources)))

    @property
    def width(self) -> F:
        values=[rat(self.values[i]) for i in self.indices()]
        return max(values)-min(values)

    @property
    def range(self) -> tuple[F,F]:
        a=[rat(self.values[i]) for i in self.indices()]
        return min(a),max(a)

    def witness(self):
        inds=self.indices()
        l,r=self.range
        return (self.sources[next(i for i in inds if rat(self.values[i])==l)],
                self.sources[next(i for i in inds if rat(self.values[i])==r)])

    def observe(self, instrument: str, reports: tuple[str,...], outcome: str, *,stamp: Stamp) -> "SourceFibre":
        _compatible(self.stamp,stamp)
        _named(instrument,"instrument")
        _named(outcome,"observed outcome")
        if len(reports)!=len(self.sources) or any(not isinstance(s,str) or not s for s in reports):
            raise ProofDebtError("full original-source report table required")
        surviving=tuple(i for i in self.indices() if reports[i]==outcome)
        if not surviving:
            raise ProofDebtError("IMPOSSIBLE_ACTUAL_REPORT_NO_GHOST")
        return SourceFibre(self.stamp,self.target,self.sources,self.values,surviving,
                           self.history+((instrument,outcome),))


@dataclass(frozen=True)
class MovingTarget:
    """A finite source class with an explicitly controlled moving target law."""
    stamp: Stamp
    source_labels: tuple[str,...]
    current_values: tuple[F,...]
    live: tuple[int,...]
    stage: int=0
    checks: tuple[F,...]=()

    def __post_init__(self):
        natural(self.stage)
        if not self.source_labels or len(self.current_values)!=len(self.source_labels):
            raise ProofDebtError("complete original-source target table required")
        if len(set(self.source_labels))!=len(self.source_labels) or any(not isinstance(s,str) or not s for s in self.source_labels):
            raise ProofDebtError("unique original-source labels required")
        if not self.live or len(set(self.live))!=len(self.live) or any(type(i) is not int or not 0<=i<len(self.source_labels) for i in self.live):
            raise ProofDebtError("nonempty valid source fiber required")
        for v in self.current_values:rat(v)
        for v in self.checks:
            if rat(v)<0:raise ProofDebtError("drift caps nonnegative")

    def step(self, values: tuple[F,...], drift_cap:F, *, stamp:Stamp, survive:tuple[int,...]|None=None)->"MovingTarget":
        _compatible(self.stamp,stamp)
        b=rat(drift_cap)
        if b<0 or len(values)!=len(self.current_values):
            raise ProofDebtError("drift cap/target shape mismatch")
        for new,old in zip(values,self.current_values):
            if abs(rat(new)-rat(old))>b:
                raise ProofDebtError("SOURCE_TARGET_DRIFT_EXCEEDS_DECLARED_BOUND")
        new_live=self.live if survive is None else survive
        if not set(new_live).issubset(set(self.live)):
            raise ProofDebtError("NEW_SOURCE_GHOST_IN_HISTORY")
        return MovingTarget(self.stamp,self.source_labels,tuple(rat(x) for x in values),new_live,
                            self.stage+1,self.checks+(b,))

    def guaranteed_limit_range(self, future_tail_bound:F, *, universal_drift_law:bool=False):
        """Conditional on proof |T_inf(s)-T_stage(s)| <= future_tail_bound.

        Finite past drift checks alone do not certify any future bound.
        """
        if universal_drift_law is not True:
            raise ProofDebtError("FUTURE_TARGET_LAW_NOT_PROVED")
        b=rat(future_tail_bound)
        if b<0:raise ProofDebtError("negative drift tail")
        vals=[rat(self.current_values[i]) for i in self.live]
        return min(vals)-b,max(vals)+b


def future_geometric_drift(cap:F,ratio:F,stage:int)->F:
    c=rat(cap);r=rat(ratio);natural(stage)
    if c<0 or not 0<=r<1:raise ProofDebtError("invalid universal drift envelope")
    return c*r**stage/(1-r)


@dataclass(frozen=True)
class SignedEvidence:
    """A declared theorem enclosure for SAME scalar target and source.

    accepted evidence type is a mathematical PREMISE.  No physical source is
    authenticated just by presenting a correct-looking stamp.
    """
    stamp:Stamp
    target:str
    stage:int
    center:F
    error:F
    derivation:str

    def __post_init__(self):
        _named(self.target,"target")
        _named(self.derivation,"derivation identifier")
        natural(self.stage)
        if rat(self.error)<0:raise ProofDebtError("error must be nonnegative")
        rat(self.center)

    @property
    def interval(self)->tuple[F,F]:
        return rat(self.center)-rat(self.error),rat(self.center)+rat(self.error)


@dataclass(frozen=True)
class EvidenceLedger:
    stamp:Stamp
    target:str
    entries:tuple[SignedEvidence,...]=()

    def __post_init__(self):
        _named(self.target,"target")
        last=-1
        for e in self.entries:
            _compatible(self.stamp,e.stamp)
            if e.target!=self.target or e.stage<=last:
                raise ProofDebtError("target mismatch or stale stage")
            last=e.stage
        if self.entries:
            lo=max(e.interval[0] for e in self.entries)
            hi=min(e.interval[1] for e in self.entries)
            if lo>hi:
                raise ProofDebtError("INCONSISTENT_SOURCE_EVIDENCE")

    def append(self,e:SignedEvidence)->"EvidenceLedger":
        return EvidenceLedger(self.stamp,self.target,self.entries+(e,))

    @property
    def interval(self)->tuple[F,F]:
        if not self.entries:raise ProofDebtError("NO_CERTIFICATE")
        return max(e.interval[0] for e in self.entries),min(e.interval[1] for e in self.entries)

    @property
    def sign(self)->str:
        lo,hi=self.interval
        if lo>0:return "STRICTLY_POSITIVE"
        if hi<0:return "STRICTLY_NEGATIVE"
        if lo==hi==0:return "EXACT_ZERO"
        if lo>=0:return "NONNEGATIVE"
        if hi<=0:return "NONPOSITIVE"
        return "UNRESOLVED"


def toy_halting_real(stage:int,halting_step:int|None)->tuple[F,F]:
    """Bounded-simulation control, NOT a Turing halting decider.

    If an external machine halts first at t, the target = -2^(-t-2), else 0.
    Stage N simulates only N steps.  Universal |target-a_N| <=2^(-N-2).
    """
    natural(stage)
    if halting_step is not None:natural(halting_step)
    center=-F(1,2**(halting_step+2)) if halting_step is not None and halting_step<=stage else F(0)
    return center,F(1,2**(stage+2))


def gamma_tail_bracket(j:int, extra_terms:int=0)->tuple[F,F]:
    """Enclose exact authentic OUTSTANDING positive Gamma multiplier tail.

    eps_j = sum_(k>=j)16/(4k+1)^3 = (1/4) HurwitzZeta(3,j+1/4).
    Enclose by integral test after extra_terms exactly evaluated rungs.
    The sharp multiplier sup is at frequency 0 on full-line H^1 energy;
    this is NOT a positivity proof for the other signed Weil contributions.
    """
    natural(j,1);natural(extra_terms)
    sm=sum((F(16,(4*k+1)**3) for k in range(j,j+extra_terms)),F(0))
    k=j+extra_terms
    integ=F(2,(4*k+1)**2)
    return sm+integ,sm+integ+F(16,(4*k+1)**3)


def gamma_simple_upper(j:int)->F:
    return gamma_tail_bracket(j)[1]


def signed_weil_test_gate(qj_lower:F,qj_upper:F,h1_derivative_norm_sq:F,j:int)->str:
    """Verdict for ONE authentic v; inputs must already be rigorous bounds.

    True form Q=Q_J+R_J with 0<=R_J<=epsilon_J||v'||^2.
    """
    low,upper,der=rat(qj_lower),rat(qj_upper),rat(h1_derivative_norm_sq)
    if der<0 or low>upper:raise ProofDebtError("malformed signed quadratic enclosure")
    if low>=0:return "CERTIFIED_ONE_TEST_NONNEGATIVE"
    if upper+gamma_simple_upper(j)*der<0:return "CERTIFIED_ONE_TEST_NEGATIVE"
    return "UNRESOLVED_SIGN"


def exact_psd(matrix:tuple[tuple[F,...],...])->tuple[bool,tuple[F,...]|None]:
    """Exact rational symmetric congruence test, including singular PSD.

    Returns a negative Rayleigh witness in ORIGINAL coordinates on failure.
    No floating eigenvalues or tolerance predicates.
    """
    n=len(matrix)
    if not n or any(len(row)!=n for row in matrix):
        raise ProofDebtError("nonempty square matrix required")
    A=[[rat(x) for x in row] for row in matrix]
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):
        raise ProofDebtError("symmetric rational matrix required")
    U=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(k,n):
            if A[i][i]<0:
                return False,tuple(U[t][i] for t in range(n))
        piv=next((p for p in range(k,n) if A[p][p]>0),None)
        if piv is None:
            for i in range(k,n):
                for j in range(i+1,n):
                    if A[i][j]:
                        # in transformed coordinates, e_i + t e_j has negative q
                        t=-A[i][j]/(abs(A[j][j])+1)
                        witness=tuple(U[u][i]+t*U[u][j] for u in range(n))
                        return False,witness
            return True,None
        if piv!=k:
            for t in range(n): A[t][k],A[t][piv]=A[t][piv],A[t][k]
            A[k],A[piv]=A[piv],A[k]
            for t in range(n): U[t][k],U[t][piv]=U[t][piv],U[t][k]
        pivot=A[k][k]
        row=[A[k][j]/pivot for j in range(k+1,n)]
        for i in range(k+1,n):
            for j in range(i,n):
                A[i][j]-=A[i][k]*row[j-(k+1)]
                A[j][i]=A[i][j]
        for j in range(k+1,n):
            a=row[j-(k+1)]
            for t in range(n):U[t][j]-=a*U[t][k]
            A[k][j]=A[j][k]=F(0)
    return True,None


def schur_two_zeno_gate(M:tuple[tuple[F,...],...],
                        complementary_lower:F,cross_norm_upper:F,
                        truncation_error:F)->dict:
    """Conditional general Hilbert form certificate.

    Assumptions: Q_J on F + K has F block M, complement >=kappa_J,
    and cross-norm <=L.  TRUE Q obeys ||Q-Q_J|| <=eps in common form norm.
    Then Q>=0 when M-[eps+(L+eps)^2/(kappa_J-eps)]I>=0.
    These blocks are INPUT mathematical certificates, never inferred
    from a numerical sample; application to Weil remains UNVERIFIED.
    """
    k,L,e=rat(complementary_lower),rat(cross_norm_upper),rat(truncation_error)
    if k<=e or L<0 or e<0:
        raise ProofDebtError("complement coercivity must exceed uniform truncation debt")
    correction=e+(L+e)**2/(k-e)
    n=len(M)
    trial=tuple(tuple(rat(M[i][j])-(correction if i==j else 0) for j in range(n)) for i in range(n))
    ok,w=exact_psd(trial)
    return {"certifies_all_vectors_conditional_on_inputs":ok,
            "adjusted":trial,"correction":correction,"negative_witness":w,
            "claimed_authentic_weil_coefficients_verified":False}


__all__=["ProofDebtError","ProofEvent","ProofDebtLedger","AmortizedContract",
         "SourceFibre","MovingTarget","future_geometric_drift","SignedEvidence",
         "EvidenceLedger","toy_halting_real","gamma_tail_bracket","gamma_simple_upper",
         "signed_weil_test_gate","exact_psd","schur_two_zeno_gate"]


@dataclass(frozen=True)
class ProbeTable:
    """One *mathematically supplied*, read-only deterministic original-source chart."""
    stamp:Stamp
    name:str
    reports:tuple[str,...]

    def __post_init__(self):
        _named(self.name,"probe")
        if not self.reports or any(not isinstance(x,str) or not x for x in self.reports):
            raise ProofDebtError("complete nonempty report row required")


def _group_widths(sources:SourceFibre,probes:tuple[ProbeTable,...],indices:tuple[int,...]):
    groups={}
    for i in sources.indices():
        key=tuple(probes[j].reports[i] for j in indices)
        groups.setdefault(key,[]).append(i)
    max_width=F(0)
    witness=None
    for members in groups.values():
        lo=min(members,key=lambda i:rat(sources.values[i]))
        hi=max(members,key=lambda i:rat(sources.values[i]))
        width=rat(sources.values[hi])-rat(sources.values[lo])
        if width>max_width:
            max_width=width
            witness=(sources.sources[lo],sources.sources[hi])
    return max_width,witness


def epsilon_probe_cover(source:SourceFibre,probes:tuple[ProbeTable,...],
                        tolerance:F,*,max_charts:int=12)->dict:
    """Finite exact counterpart of compact approximate-target extraction.

    Select a minimum nonadaptive chart family whose every report fiber has
    target diameter STRICTLY less than tolerance.  If unavailable, output
    a target-disagreeing pair indistinguishable by ALL admitted charts.
    These tables do not certify physical simultaneous executability.
    """
    eps=rat(tolerance)
    if eps<=0:raise ProofDebtError("epsilon target must be strictly positive")
    natural(max_charts,0)
    if len(probes)>max_charts:
        raise ProofDebtError("RESOURCE_BUDGET_EXHAUSTED_NOT_IMPOSSIBILITY")
    if len(set(p.name for p in probes))!=len(probes):
        raise ProofDebtError("duplicate chart labels")
    for p in probes:
        _compatible(source.stamp,p.stamp)
        if len(p.reports)!=len(source.sources):
            raise ProofDebtError("source chart is not defined on all original states")
    from itertools import combinations
    for size in range(len(probes)+1):
        for idx in combinations(range(len(probes)),size):
            width,witness=_group_widths(source,probes,idx)
            if width<eps:
                return {"status":"CERTIFIED_FINITE_EPSILON_COVER",
                        "names":tuple(probes[i].name for i in idx),
                        "maximum_target_width":width,
                        "physical_joint_executability_verified":False,
                        "source_law_authenticated_externally":False}
    width,wit=_group_widths(source,probes,tuple(range(len(probes))))
    return {"status":"ARITY_OR_SOURCE_INFORMATION_OBSTRUCTION",
            "names":tuple(p.name for p in probes),
            "maximum_target_width":width,
            "indistinguishable_target_pair":wit,
            "physical_joint_executability_verified":False,
            "source_law_authenticated_externally":False}


def dynamic_protocol_blindness(source:SourceFibre,probes:tuple[ProbeTable,...],
                               *,target_separation:F=F(0))->dict:
    """Exact blindness floor for ANY adaptive read-only deterministic policy.

    Every pair with identical full available report signatures follows the
    same read-only adaptive transcript, even with stopping/randomization
    sourced independently of the hidden source. This is NOT a conclusion
    for destructive, changing-carrier or newly generated instruments.
    """
    bound=rat(target_separation)
    if bound<0:raise ProofDebtError("nonnegative contrast requested")
    if len(set(p.name for p in probes))!=len(probes):
        raise ProofDebtError("duplicate chart labels")
    for p in probes:
        _compatible(source.stamp,p.stamp)
        if len(p.reports)!=len(source.sources):
            raise ProofDebtError("incomplete read-only source chart")
    width,wit=_group_widths(source,probes,tuple(range(len(probes))))
    if width>0 and width>=bound:
        return {"status":"UNAVOIDABLE_READONLY_EPISTEMIC_DEBT",
                "lower_bound":width,"original_pair":wit,
                "unrestricted_other_probes_ruled_out":False}
    return {"status":"NO_INDEFEASIBLE_PAIR_AT_THIS_CONTRAST",
            "lower_bound":width,"unrestricted_other_probes_ruled_out":False}


__all__ += ["ProbeTable","epsilon_probe_cover","dynamic_protocol_blindness"]


def generic_rank_one_operator_stage(stage:int,halting_step:int|None):
    """Toy effective finite-rank operator approximation; not a zeta source.

    A_M=x_M |e_1><e_1| on ell2, A_(M,n)=a_n |e_1><e_1|,
    ||A_M-A_(M,n)||<=2^(-n-2) by bounded simulation.
    Any universal finite positivity DECIDER for such operator streams
    would decide complement of halting, which is impossible.
    """
    center,err=toy_halting_real(stage,halting_step)
    return {"matrix":((center,),),
            "norm_error_upper":err,
            "source_kind":"generic-computable-operator-NEGATIVE-CONTROL",
            "completed_weil_identification":False}


__all__ += ["generic_rank_one_operator_stage"]
