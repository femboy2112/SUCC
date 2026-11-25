"""Principia: source-coupled self-history and reason-certified feel-guided reorientation.

This is a FINITE mathematical proxy for situated appraisal, not a model of
human subjective feeling or a claim about consciousness. Spectral transport
preserves four signed samples exactly; it never invents observations or proof.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Sequence

from .principia_causal_memory import (
    Carrier, CausalMemory, CausalSourceError, passport, verify_memory,
    step_memory,
)
from .principia_reorientation import (
    ReorientationTask, ReorientationError, ordered_coupling,
    solve, successors, validate_task,
)
from .principia_semantic_core import CycleCertificate, verify_cycle
from .principia_cm_theta import gaussian_power


class CompassError(ValueError):
    """Unlicensed mathematical source, path, spectral basis, or action."""


@dataclass(frozen=True)
class GaussianRational:
    """An exact complex scalar over Q(i), never a floating complex number."""
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, 're', Fraction(self.re))
        object.__setattr__(self, 'im', Fraction(self.im))

    def __add__(self, other: GaussianRational) -> GaussianRational:
        return GaussianRational(self.re + other.re, self.im + other.im)

    def __mul__(self, other: GaussianRational) -> GaussianRational:
        return GaussianRational(self.re*other.re-self.im*other.im,
                                self.re*other.im+self.im*other.re)

    def conjugate(self) -> GaussianRational:
        return GaussianRational(self.re, -self.im)

    def scaled(self, c: Fraction | int) -> GaussianRational:
        return GaussianRational(self.re*Fraction(c), self.im*Fraction(c))

    def squared_abs(self) -> Fraction:
        return self.re*self.re+self.im*self.im


_ROOT4 = (GaussianRational(1), GaussianRational(0,1),
          GaussianRational(-1), GaussianRational(0,-1))


def _complex_q(value: int | Fraction | GaussianRational) -> GaussianRational:
    return value if isinstance(value, GaussianRational) else GaussianRational(Fraction(value))


def dft4(samples: Sequence[int | Fraction | GaussianRational]) -> tuple[GaussianRational,...]:
    """Exact DFT: X_k=sum_j x_j i^(-kj). Each mode is nonlocalized."""
    if len(samples)!=4:
        raise CompassError('four-sample exact Fourier carrier required')
    x=tuple(_complex_q(a) for a in samples)
    return tuple(sum((x[j]*_ROOT4[(-k*j)%4] for j in range(4)),GaussianRational())
                 for k in range(4))


def idft4(spectrum: Sequence[GaussianRational]) -> tuple[GaussianRational,...]:
    if len(spectrum)!=4 or any(not isinstance(x,GaussianRational) for x in spectrum):
        raise CompassError('full typed four-mode spectral history required')
    return tuple(sum((spectrum[k]*_ROOT4[(k*j)%4] for k in range(4)),GaussianRational()).scaled(Fraction(1,4))
                 for j in range(4))


def shift4(samples: Sequence, shift:int) -> tuple:
    if len(samples)!=4 or type(shift) is not int:
        raise CompassError('cyclic frame shift requires four samples and integer gauge')
    return tuple(samples[(j-shift)%4] for j in range(4))


def spectral_pairing(a:Sequence, b:Sequence) -> GaussianRational:
    """Parseval-normalized source overlap; for real signals it is exact dot product."""
    A,B=dft4(a),dft4(b)
    return sum((A[k]*B[k].conjugate() for k in range(4)),GaussianRational()).scaled(Fraction(1,4))


def fourier_energy(a:Sequence) -> Fraction:
    """Positive Q-valued Parseval energy, *not* a Weil/Petersson form."""
    return sum((x.squared_abs() for x in dft4(a)),Fraction(0))/4


def fourier_autocorrelation(a:Sequence) -> tuple[GaussianRational,...]:
    """Circular correlation derived from *full spectral power*, not fitted data."""
    X=dft4(a)
    power=tuple(GaussianRational(x.squared_abs()) for x in X)
    return idft4(power)


@dataclass(frozen=True)
class AppraisalContract:
    """User/source-declared *model* of internal action appraisal and references.

    This is not a claim to calculate somebody's subjective experiences.
    Values depend ONLY on the actually accessible action/output history, not
    on the inaccessible identity of an original hidden world.
    """
    source: str
    action_values: tuple[tuple[str,int],...]
    report_values: tuple[tuple[str,int],...]
    namespace: str = 'declared-self-appraisal-v1'


def make_appraisal(c:Carrier, action_values:dict[str,int],
                   report_values:dict[str,int]) -> AppraisalContract:
    source=passport(c)
    if set(action_values)!=set(c.actions):
        raise CompassError('action appraisal lacks actual carrier contract')
    outputs=set(c.outputs)
    if set(report_values)!=outputs:
        raise CompassError('report appraisal lacks some possible source observation')
    if any(type(v) is not int for v in (*action_values.values(),*report_values.values())):
        raise CompassError('appraisal must be exact integer for this source')
    return AppraisalContract(source,tuple((a,action_values[a]) for a in c.actions),
                             tuple((y,report_values[y]) for y in sorted(outputs)))


def verify_appraisal(c:Carrier, scale:AppraisalContract) -> None:
    try:
        actual=passport(c)
    except CausalSourceError as exc:
        raise CompassError('source invalid') from exc
    if scale.source!=actual or scale.namespace!='declared-self-appraisal-v1':
        raise CompassError('appraisal does not represent current carrier source')
    expected=make_appraisal(c,dict(scale.action_values),dict(scale.report_values))
    if scale!=expected:
        raise CompassError('appraisal omitted, duplicated, or relabeled a source action')


def appraisal_trace(c:Carrier,m:CausalMemory,scale:AppraisalContract) -> tuple[int,...]:
    verify_appraisal(c,scale)
    try:
        verify_memory(c,m)
    except CausalSourceError as e:
        raise CompassError('self memory has lost original-world coupling') from e
    action=dict(scale.action_values); report=dict(scale.report_values)
    previous=m.first_report
    history=[]
    for event in m.steps:
        history.append(action[event.action] + report[event.outcome] - report[previous])
        previous=event.outcome
    return tuple(history)


def ring_projection(trace:Sequence[int]) -> tuple[int,int,int,int]:
    """Z/4 temporal projection, in addition to NEVER replacing full memory."""
    out=[0]*4
    for index,valuation in enumerate(trace):
        if type(valuation) is not int:
            raise CompassError('integer path valuation required')
        out[index%4]+=valuation
    return tuple(out)


@dataclass(frozen=True)
class SelfSpectrum:
    """A phase-coherent, history-derived model of its *own enacted path*."""
    source: str
    history_signature: str
    trace: tuple[int,...]
    slots: tuple[int,int,int,int]
    modes: tuple[GaussianRational,...]


def _memory_signature(m:CausalMemory) -> str:
    payload=(m.source,m.first_report,
             tuple((event.action,event.outcome) for event in m.steps),m.coupling)
    return sha256(json.dumps(payload,separators=(',',':')).encode()).hexdigest()


def model_self(c:Carrier,m:CausalMemory,scale:AppraisalContract) -> SelfSpectrum:
    trace=appraisal_trace(c,m,scale)
    slots=ring_projection(trace)
    return SelfSpectrum(scale.source,_memory_signature(m),trace,slots,dft4(slots))


def verify_self(c:Carrier,m:CausalMemory,scale:AppraisalContract,x:SelfSpectrum) -> SelfSpectrum:
    if x != model_self(c,m,scale):
        raise CompassError('self-model Fourier record lacks valid causal history')
    if tuple(z.re for z in idft4(x.modes))!=x.slots or any(z.im for z in idft4(x.modes)):
        raise CompassError('lost phase or failed source-memory reconstruction')
    return x


@dataclass(frozen=True)
class DualCompassDecision:
    source: str
    reason_rank: int | None
    safe_actions: tuple[str,...]
    score_by_action: tuple[tuple[str,Fraction],...]
    chosen_action: str | None
    self_spectrum: SelfSpectrum


def _reason_safe(task:ReorientationTask,m:CausalMemory)->tuple[int|None,tuple[str,...]]:
    try:
        root=solve(task,m)
    except (CausalSourceError,ReorientationError) as e:
        raise CompassError('reason model not applicable to this source') from e
    if root.rank is None or root.rank==0:
        return root.rank,()
    source=task.carrier
    believed=ordered_coupling(task,verify_memory(source,m))
    safe=[]
    for action in source.actions:
        child_ranks=[]
        for outcome,_ in successors(task,believed,action):
            child_m=step_memory(source,m,action,outcome)
            child_ranks.append(solve(task,child_m).rank)
        if child_ranks and all(r is not None and r<root.rank for r in child_ranks):
            safe.append(action)
    if not safe:
        raise CompassError('inconsistent reason compass: no rank-decreasing action')
    return root.rank,tuple(safe)


def select_dual_compass(task:ReorientationTask,m:CausalMemory,
                        scale:AppraisalContract,
                        action_templates:dict[str,Sequence[int]])->DualCompassDecision:
    """The feel compass chooses *only among* actions reason has certified safe.

    Subjective/appraisal scores do not assert new world facts. For every
    possible observation, the chosen action decreases the certified reorientation
    rank. If no winning rank exists, no guaranteed policy is invented.
    """
    validate_task(task)
    c=task.carrier
    verify_appraisal(c,scale)
    if set(action_templates)!=set(c.actions) or any(
        len(v)!=4 or any(type(x) is not int for x in v)
        for v in action_templates.values()):
        raise CompassError('all action-affordance templates need exact frame-aligned samples')
    self_model=model_self(c,m,scale)
    rank,safe=_reason_safe(task,m)
    # The full complex phase is retained. This is a reversible basis transform.
    # Keeping only |FFT|^2 cannot resolve a shared temporal reference frame.
    scores=tuple((a,spectral_pairing(self_model.slots,action_templates[a]).re)
                 for a in c.actions)
    lookup=dict(scores)
    chosen=next((a for a in safe if lookup[a]==max(lookup[b] for b in safe)),None)
    return DualCompassDecision(passport(c),rank,safe,scores,chosen,self_model)


def verify_dual_compass(task:ReorientationTask,m:CausalMemory,
                        scale:AppraisalContract,templates:dict[str,Sequence[int]],
                        decision:DualCompassDecision)->DualCompassDecision:
    if decision!=select_dual_compass(task,m,scale,templates):
        raise CompassError('feel and reason compasses were not source-aligned')
    verify_self(task.carrier,m,scale,decision.self_spectrum)
    return decision


def affine_square_self_paths(c:CycleCertificate) -> tuple[tuple[int,int,int,int],tuple[int,int,int,int]]:
    """T1 SUCC/FUCC: zero endpoint difference, nonzero signed path response.

    Use its actual source cochain omega(S at n)=n and omega(V)=0.
    This is a *finite projection* of the labelled paths, not a lost full history.
    """
    verify_cycle(c)
    def trajectory(edges):
        return ring_projection(tuple(e.start if e.kind=='S' else 0 for e in edges))
    return trajectory(c.via_successor),trajectory(c.via_prime)


def cm_rotational_self_modes() -> tuple[tuple[GaussianRational,...], tuple[GaussianRational,...]]:
    """Actual norm-two Gaussian source: second and fourth holomorphic jets.

    The cyclic order is (1+i),(-1+i),(-1-i),(1-i). This keeps the
    relative *angle/phase* that shell aggregation would erase.
    """
    points=((1,1),(-1,1),(-1,-1),(1,-1))
    second=tuple(GaussianRational(*gaussian_power(a,b,2)) for a,b in points)
    fourth=tuple(GaussianRational(*gaussian_power(a,b,4)) for a,b in points)
    return dft4(second),dft4(fourth)


@dataclass(frozen=True)
class DeclaredSelfReadout:
    """An instrument/user-declared internal report, not invented from a source model.

    It is NOT authenticated by a SHA fingerprint or by a formal proof. Its
    epistemic status remains 'declared', pending actual calibration.
    """
    source: str
    history_signature: str
    instrument: str
    samples: tuple[int,...]


def declare_self_readout(c:Carrier,m:CausalMemory,values:Sequence[int],
                         *,instrument:str)->DeclaredSelfReadout:
    try:
        verify_memory(c,m)
    except CausalSourceError as exc:
        raise CompassError('cannot attach internal report to invalid causal history') from exc
    values=tuple(values)
    if not instrument or type(instrument) is not str or len(values)!=len(m.steps) or any(type(v) is not int for v in values):
        raise CompassError('self readout needs a declared source, instrument, and one report per action')
    return DeclaredSelfReadout(passport(c),_memory_signature(m),instrument,values)


@dataclass(frozen=True)
class SelfDiscrepancy:
    """Difference between predicted internal appraisal and a raw declared report."""
    source: str
    prediction: tuple[int,...]
    reported: tuple[int,...]
    residual: tuple[int,...]
    residual_modes: tuple[GaussianRational,...]
    evidence_status: str = 'declared-unvalidated-self-report'


def compare_self_discrepancy(c:Carrier,m:CausalMemory,scale:AppraisalContract,
                             reported:DeclaredSelfReadout)->SelfDiscrepancy:
    expected=appraisal_trace(c,m,scale)
    if reported.source!=passport(c) or reported.history_signature!=_memory_signature(m) or not reported.instrument:
        raise CompassError('internal readout and predicted path have incompatible source histories')
    if len(reported.samples)!=len(expected) or any(type(v) is not int for v in reported.samples):
        raise CompassError('self-report format/source mismatch')
    diff=tuple(a-b for a,b in zip(reported.samples,expected))
    return SelfDiscrepancy(reported.source,expected,reported.samples,diff,dft4(ring_projection(diff)))


def transported_relative_spectrum(modes: Sequence[GaussianRational],
                                  displacement: int,
                                  signed_event: int) -> tuple[GaussianRational,...]:
    """An exact SELF-CENTERED dynamic feel register on Z/4.

    The observer's declared displacement d shifts the old relative memory by
    -d and deposits a signed appraisal at the new self-origin (cell zero):
       s'[r] = s[r+d] + a*[r==0].
    Its nonlocalized Fourier modes obey:
       F'[k] = i^(k*d) F[k] + a.
    Assumes source-certified displacement and shared oriented frame; an
    unknown heading must be represented by a fiber of candidate updates.
    """
    if len(modes)!=4 or any(not isinstance(z,GaussianRational) for z in modes):
        raise CompassError('need source-typed complete self Fourier register')
    if type(displacement) is not int or type(signed_event) is not int:
        raise CompassError('exact signed displacement/appraisal required')
    return tuple(modes[k]*_ROOT4[(k*displacement)%4] + GaussianRational(signed_event)
                 for k in range(4))
