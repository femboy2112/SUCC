"""Exact finite quantum instruments and non-erasing causal observation records.

This is a mathematically valid two-dimensional REAL quantum-measurement
submodel, using only fractions. It provides a physical-carrier example
INDEPENDENT OF NUMBER THEORY, Gödel, Turing and RH.

A state is a real symmetric PSD trace-one density matrix. An instrument
is a finite list of rational Kraus operators {K_o}, satisfying
Σ_o K_o^T K_o = I exactly. For outcome o,

   p_o = tr(K_o rho K_o^T),
   rho_o = K_o rho K_o^T / p_o.

The experiment's finite causal event history is immutable. The normalized
*reduced state* may evolve and discard coherence while the classical
outcome record remains available. A positive quantum carrier does NOT
certify any arithmetic Weil form.

This real-qubit construction is NOT a physically complete model of a
person, measurement hardware, or general complex quantum mechanics.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256


class QuantumRecordError(ValueError):
    """Unnormalized states, invalid instruments, erased or impossible events."""


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
ZERO = Fraction(0)
ONE = Fraction(1)
IDENTITY: Matrix = ((ONE,ZERO),(ZERO,ONE))
INITIAL_ZERO: Matrix = ((ONE,ZERO),(ZERO,ZERO))
INITIAL_PLUS: Matrix = ((Fraction(1,2),Fraction(1,2)),
                        (Fraction(1,2),Fraction(1,2)))


def _q(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise QuantumRecordError("Use exact integer/Fraction quantum coordinates, never floats")


def _matrix(a) -> Matrix:
    if not isinstance(a,(tuple,list)) or len(a)!=2:
        raise QuantumRecordError("Real-qubit matrices have exactly two rows")
    rows=[]
    for row in a:
        if not isinstance(row,(tuple,list)) or len(row)!=2:
            raise QuantumRecordError("Real-qubit matrices have exactly two columns")
        rows.append((_q(row[0]),_q(row[1])))
    return tuple(rows)  # type: ignore[return-value]


def _transpose(a:Matrix) -> Matrix:
    return ((a[0][0],a[1][0]),(a[0][1],a[1][1]))


def _multiply(a:Matrix,b:Matrix) -> Matrix:
    return tuple(tuple(
        a[i][0]*b[0][j]+a[i][1]*b[1][j]
        for j in range(2)) for i in range(2))  # type: ignore[return-value]


def _add(a:Matrix,b:Matrix) -> Matrix:
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2))
                 for i in range(2))  # type: ignore[return-value]


def _scale(a:Matrix,q) -> Matrix:
    x=_q(q)
    return tuple(tuple(x*v for v in row) for row in a)  # type: ignore[return-value]


def _trace(a:Matrix) -> Fraction:
    return a[0][0]+a[1][1]


def _validate_density(rho) -> Matrix:
    r=_matrix(rho)
    if r[0][1]!=r[1][0]:
        raise QuantumRecordError("Density matrix must be symmetric")
    if _trace(r)!=1:
        raise QuantumRecordError("Density matrix must have trace one")
    if r[0][0]<0 or r[1][1]<0 or r[0][0]*r[1][1]-r[0][1]**2<0:
        raise QuantumRecordError("Density matrix must be positive semidefinite")
    return r


def _fingerprint(prior:str,instrument:str,outcome:str,p:Fraction,joint:Fraction,rho:Matrix)->str:
    """A deterministic append-only integrity chain, NOT authenticated provenance."""
    coords=",".join(f"{x.numerator}/{x.denominator}" for row in rho for x in row)
    msg=f"{prior}|{instrument}|{outcome}|{p}|{joint}|{coords}"
    return sha256(msg.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Instrument:
    """Each outcome has exactly one rational Kraus operator."""
    name: str
    outcomes: tuple[tuple[str,Matrix], ...]

    def __post_init__(self):
        if not self.name or not self.name.isidentifier():
            raise QuantumRecordError("Instrument name must be a stable identifier")
        if type(self.outcomes) is not tuple or not self.outcomes:
            raise QuantumRecordError("Require a nonempty immutable outcome family")
        labels=set()
        operators=[]
        for label,raw in self.outcomes:
            if type(label) is not str or not label or label in labels:
                raise QuantumRecordError("Outcome names must be unique nonempty strings")
            labels.add(label)
            operators.append((label,_matrix(raw)))
        completeness=((ZERO,ZERO),(ZERO,ZERO))
        for _,k in operators:
            completeness=_add(completeness,_multiply(_transpose(k),k))
        if completeness!=IDENTITY:
            raise QuantumRecordError("Outcome Kraus operators must satisfy Σ K^T K = I")
        object.__setattr__(self,"outcomes",tuple(operators))

    def event(self,rho:Matrix,outcome:str):
        rho=_validate_density(rho)
        family=dict(self.outcomes)
        if outcome not in family:
            raise QuantumRecordError("Unrecognized outcome in observed instrument")
        k=family[outcome]
        unnormalized=_multiply(_multiply(k,rho),_transpose(k))
        p=_trace(unnormalized)
        if p<=0:
            raise QuantumRecordError("Impossible zero-probability observation cannot occur")
        posterior=_validate_density(_scale(unnormalized,Fraction(1)/p))
        return p,posterior

    def probabilities(self,rho:Matrix):
        rho=_validate_density(rho)
        results={}
        for label,k in self.outcomes:
            results[label]=_trace(_multiply(_multiply(k,rho),_transpose(k)))
        if sum(results.values(),ZERO)!=1 or min(results.values())<0:
            raise ArithmeticError("Complete positive instrument has invalid outcome weights")
        return results


@dataclass(frozen=True)
class Observation:
    index:int
    instrument:str
    outcome:str
    conditional_probability:Fraction
    joint_probability:Fraction
    posterior:Matrix
    previous_head:str
    head:str


@dataclass(frozen=True)
class QuantumObserver:
    """Finite immutable physical record + current reduced quantum state."""
    initial:Matrix=INITIAL_ZERO
    state:Matrix=INITIAL_ZERO
    records:tuple[Observation,...]=()
    joint_probability:Fraction=ONE
    head:str="0"*64

    def __post_init__(self):
        _validate_density(self.initial)
        _validate_density(self.state)
        if not isinstance(self.records,tuple) or any(not isinstance(x,Observation) for x in self.records):
            raise QuantumRecordError("Observation history must be an immutable tuple")
        if not 0<self.joint_probability<=1:
            raise QuantumRecordError("Observed joint probability must be in (0,1]")
        if len(self.head)!=64:
            raise QuantumRecordError("Record head must be a hexadecimal integrity digest")

    @classmethod
    def initial_state(cls,rho=INITIAL_ZERO):
        r=_validate_density(rho)
        return cls(initial=r,state=r)

    def advance(self,instrument:Instrument,outcome:str):
        if not isinstance(instrument,Instrument):
            raise QuantumRecordError("Only validated instruments can update observed state")
        prob,posterior=instrument.event(self.state,outcome)
        joint=self.joint_probability*prob
        digest=_fingerprint(self.head,instrument.name,outcome,prob,joint,posterior)
        item=Observation(len(self.records)+1,instrument.name,outcome,prob,joint,
                         posterior,self.head,digest)
        return QuantumObserver(self.initial,posterior,
                               self.records+(item,),joint,digest)

    def verify(self,instruments:dict[str,Instrument])->bool:
        """Replay every actual event and check the entire immutable chain."""
        if not isinstance(instruments,dict):
            raise QuantumRecordError("Need instrument registry for replay")
        state=QuantumObserver.initial_state(self.initial)
        for old in self.records:
            if old.instrument not in instruments:
                raise QuantumRecordError("Missing original instrument for replay")
            new=state.advance(instruments[old.instrument],old.outcome)
            if new.records[-1]!=old:
                raise QuantumRecordError("Stored outcome history was altered")
            state=new
        if (state.state!=self.state or state.head!=self.head
                or state.joint_probability!=self.joint_probability):
            raise QuantumRecordError("Observer state differs from replayed history")
        return True


def measure_z()->Instrument:
    return Instrument("Z",(
        ("zero",((ONE,ZERO),(ZERO,ZERO))),
        ("one",((ZERO,ZERO),(ZERO,ONE))),
    ))


def measure_x()->Instrument:
    half=Fraction(1,2)
    return Instrument("X",(
        ("plus",((half,half),(half,half))),
        ("minus",((half,-half),(-half,half))),
    ))


def causal_noncommutativity_probe()->dict:
    """No RH input: authentic order-sensitive physical observations."""
    initial=QuantumObserver.initial_state()
    z,x=measure_z(),measure_x()
    x_then_z=initial.advance(x,"plus").advance(z,"zero")
    z_then_x=initial.advance(z,"zero").advance(x,"plus")
    assert x_then_z.verify({"X":x,"Z":z})
    assert z_then_x.verify({"X":x,"Z":z})
    return {
        "status":"EXACT_FINITE_QUANTUM_CAUSAL_ORDER",
        "x_then_z_joint":str(x_then_z.joint_probability),
        "z_then_x_joint":str(z_then_x.joint_probability),
        "records_distinct":x_then_z.records!=z_then_x.records,
        "replayed_provenance":True,
        "quantum_model":"real two-state, rational Kraus instruments",
        "cognitive_realization_claimed":False,
        "Weil_positivity_claimed":False,
    }
