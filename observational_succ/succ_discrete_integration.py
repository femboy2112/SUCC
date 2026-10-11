"""Discrete integration of receiver-relative SUCC step differences.

Mathematical setting:
* A and B share a versioned rational basis and a certified initial position.
* A transmits successive finite differences of its actually traversed state.
* B integrates by prefix sums to reconstruct EACH intermediate state.
* If a separately justified source law says Delta^(d+1) x_n == 0 for every n,
  B can use the d-th order Newton jet at x_0 to calculate any x_n directly.
* When the coordinate frame changes, a covariant difference includes a
  connecting transport U_n. Ordered affine step operators can be composed
  by an associative prefix scan, including noncommuting operations.

No physical measurement, global proof/finite-time speedup, RH or gravitational
holography is inferred from these exact finite mathematical calculations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import comb
import json

from .basis_boundary_transport import BasisState, SharedBasis, SparseDelta


class DiscreteSuccError(ValueError):
    """Mismatch of shared initial condition, derivative law or transport."""


def q(x) -> Fraction:
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise DiscreteSuccError("Exact rational coefficient or integer required")


def _raw(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _hash(obj) -> str:
    return sha256(_raw(obj)).hexdigest()


def _fraction(s):
    if type(s) is not str or not 0 < len(s) <= 80:
        raise DiscreteSuccError("Canonical rational code required")
    try:
        x = Fraction(s)
    except (ValueError, ZeroDivisionError) as exc:
        raise DiscreteSuccError("Invalid rational code") from exc
    if str(x) != s:
        raise DiscreteSuccError("Noncanonical rational code")
    return x


def _parse(packet: bytes, expected_kind: str, fields: set[str]):
    if type(packet) is not bytes or not 0 < len(packet) <= 1000000:
        raise DiscreteSuccError("Bounded finite binary message required")
    try:
        obj = json.loads(packet.decode("utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise DiscreteSuccError("Malformed finite-difference packet") from exc
    if type(obj) is not dict or set(obj) != fields or obj.get("kind") != expected_kind:
        raise DiscreteSuccError("Wrong typed finite-difference protocol")
    return obj


def _vector(vec, dim=None) -> tuple[Fraction, ...]:
    if type(vec) is not tuple or len(vec) > 128:
        raise DiscreteSuccError("Expected immutable bounded vector")
    result = tuple(q(x) for x in vec)
    if dim is not None and len(result) != dim:
        raise DiscreteSuccError("Incompatible shared-basis vector dimension")
    return result


def _add(a, b):
    if len(a) != len(b):
        raise DiscreteSuccError("Cannot combine vectors from different dimensions")
    return tuple(x+y for x,y in zip(a,b))


def _sub(a, b):
    if len(a) != len(b):
        raise DiscreteSuccError("Cannot subtract vectors from different dimensions")
    return tuple(x-y for x,y in zip(a,b))


def _scale(c, x):
    c=q(c)
    return tuple(c*v for v in x)


def _zero(dim):
    return tuple(Fraction(0) for _ in range(dim))


def _nonzero_sparse(vector: tuple[Fraction,...]) -> SparseDelta:
    indices = tuple(i+1 for i,v in enumerate(vector) if v)
    return SparseDelta(indices, tuple(vector[i-1] for i in indices))


def _sparse_vector(delta: SparseDelta, basis: SharedBasis):
    delta.validate(basis)
    out = list(_zero(basis.dimension))
    for index,value in zip(delta.indices,delta.values):
        out[index-1] += value
    return tuple(out)


def finite_difference_states(
    first: BasisState,
    steps: tuple[SparseDelta, ...],
    basis: SharedBasis,
) -> tuple[BasisState,...]:
    """Sequential exact discrete integration: x_n=x_0+sum_{i<n}Delta x_i."""
    first.validate(basis)
    if type(steps) is not tuple or len(steps) > 128:
        raise DiscreteSuccError("Finite immutable path required")
    states = [first]
    for step in steps:
        if not isinstance(step,SparseDelta):
            raise DiscreteSuccError("Every finite SUCC change must be a sparse delta")
        states.append(states[-1].update(step,basis))
    return tuple(states)


@dataclass(frozen=True)
class ScanResult:
    states: tuple[BasisState, ...]
    parallelizable_dependency_depth: int
    number_of_additions_if_parallelized: int
    actual_parallel_execution_performed: bool = False


def parallel_prefix_differences(
    first: BasisState,
    steps: tuple[SparseDelta,...],
    basis: SharedBasis,
) -> ScanResult:
    """Hillis–Steele associative inclusive prefix scan.

    Algorithm is EXECUTED SEQUENTIALLY in Python, but its immutable stages
    have dependency depth ceil(log2 number_of_steps) and can be computed
    in parallel if adequate processors exist. The result is not a literal
    one-clock-step hardware operation or a physical time miracle.
    """
    first.validate(basis)
    if type(steps) is not tuple or len(steps) > 128:
        raise DiscreteSuccError("Bounded finite difference sequence required")
    offsets = [_sparse_vector(p,basis) for p in steps]
    stride = 1
    depth = additions = 0
    while stride < len(offsets):
        previous = tuple(offsets)
        for i in range(stride,len(offsets)):
            offsets[i] = _add(previous[i],previous[i-stride])
            additions += 1
        depth += 1
        stride *= 2
    states=(first,)+tuple(
        BasisState(_add(first.coefficients,v)) for v in offsets)
    if states!=finite_difference_states(first,steps,basis):
        raise ArithmeticError("Parallelizable scan and sequential SUCC disagree")
    return ScanResult(states,depth,additions)


def encode_step_differences(
    sender: BasisState, receiver: BasisState,
    basis: SharedBasis, steps:tuple[SparseDelta,...],
) -> bytes:
    """Transmit a path relative to B's initial condition, never a state dump."""
    receiver.validate(basis)
    sender.validate(basis)
    history=finite_difference_states(receiver,steps,basis)
    if history[-1]!=sender:
        raise DiscreteSuccError("Sender endpoint contradicts transmitted derivatives")
    return _raw({
        "kind":"source-relative-succ-differences-v1",
        "basis":basis.fingerprint,
        "anchor":receiver.anchor(basis),
        "end":sender.anchor(basis),
        "steps":[{
            "directions":list(step.canonical().indices),
            "values":[str(x) for x in step.canonical().values],
        } for step in steps],
    })


def decode_step_differences(
    receiver: BasisState, packet:bytes,basis: SharedBasis,
) -> ScanResult:
    obj=_parse(packet,"source-relative-succ-differences-v1",
               {"kind","basis","anchor","end","steps"})
    if (obj["basis"]!=basis.fingerprint
            or obj["anchor"]!=receiver.anchor(basis)
            or type(obj["steps"]) is not list
            or len(obj["steps"])>128):
        raise DiscreteSuccError("Receiver's known initial condition/basis changed")
    steps=[]
    for item in obj["steps"]:
        if (type(item) is not dict
                or set(item)!={"directions","values"}
                or type(item["directions"]) is not list
                or type(item["values"]) is not list
                or len(item["directions"])!=len(item["values"])
                or any(type(i) is not int for i in item["directions"])):
            raise DiscreteSuccError("Malformed relative finite-difference step")
        step=SparseDelta(tuple(item["directions"]),
                         tuple(_fraction(x) for x in item["values"]))
        step.validate(basis)
        if step.canonical()!=step:
            raise DiscreteSuccError("SUCC derivative packet must be canonical")
        steps.append(step)
    result=parallel_prefix_differences(receiver,tuple(steps),basis)
    if result.states[-1].anchor(basis)!=obj["end"]:
        raise DiscreteSuccError("Packet does not integrate to declared endpoint")
    return result


def difference_jet_from_samples(
    samples:tuple[BasisState,...],basis:SharedBasis,
) -> tuple[tuple[Fraction,...],...]:
    """Return [x0, Delta x0, Delta² x0, ..., Delta^d x0] exactly."""
    if type(samples) is not tuple or not 1<=len(samples)<=65:
        raise DiscreteSuccError("Need finite nonempty distinct-time sample sequence")
    layer=tuple(s.validate(basis).coefficients for s in samples)
    jet=[]
    while layer:
        jet.append(layer[0])
        layer=tuple(_sub(layer[i+1],layer[i])
                    for i in range(len(layer)-1))
    return tuple(jet)


def finite_newton_reconstruct_samples(
    samples:tuple[BasisState,...],basis:SharedBasis,
) -> tuple[BasisState,...]:
    """Newton binomial inversion of ANY finite sequence, no recurrence law.

    Let samples be x0,...,xN. The N+1 lower-triangular Pascal transform
    is invertible, so for each 0<=n<=N,
       x_n=sum_{r=0}^n binom(n,r) Delta^r x_0
    with zero source/polynomial assumptions beyond the true finite samples.

    Returning x_(N+1) from the same truncated jet WOULD BE AN UNJUSTIFIED
    extrapolation unless an independent recurrence/source theorem holds.
    """
    if type(samples) is not tuple or not 1<=len(samples)<=33:
        raise DiscreteSuccError("Finite exact Newton inversion has bounded sample count")
    jet=difference_jet_from_samples(samples,basis)
    result=tuple(newton_evaluate(samples[0],jet[1:],n,basis)
                 for n in range(len(samples)))
    if result!=samples:
        raise ArithmeticError("Finite Newton binomial inversion contradicted")
    return result


def newton_evaluate(
    base:BasisState,
    difference_jets:tuple[tuple[Fraction,...],...],
    n:int,basis:SharedBasis,
) -> BasisState:
    """Newton forward formula, conditional on a polynomial source law.

    Without an externally established degree bound this is only the
    INTERPOLATING polynomial for the initial finite samples, not a
    certificate of the unknown actual source after those samples.
    """
    base.validate(basis)
    if (type(n) is not int or not 0<=n<=1000000
            or type(difference_jets) is not tuple
            or len(difference_jets)>32):
        raise DiscreteSuccError("Bounded exact evaluation of a finite jet required")
    v=base.coefficients
    for r, coeff in enumerate(difference_jets,1):
        c=_vector(coeff,basis.dimension)
        if r<=n:
            v=_add(v,_scale(comb(n,r),c))
    return BasisState(v)


@dataclass(frozen=True)
class PolynomialJetSourceFamily:
    """Previously accepted law: x_n is Newton polynomial degree<=d.

    Source candidates are finite arrays of allowed INITIAL forward jets.
    The program checks a candidate belongs to this declared family and
    that the family consists of Newton laws by construction. It does not
    independently infer from finitely many observations that nature follows
    the law for every n. This membership remains a substantive premise.
    """
    basis_hash: str
    degree_bound: int
    candidate_jets: tuple[tuple[tuple[Fraction,...],...],...]
    proof_label: str = "newton-polynomial-source-family-v1"

    def verify(self,basis:SharedBasis):
        if (self.basis_hash!=basis.fingerprint
                or type(self.degree_bound) is not int
                or not 0<=self.degree_bound<=16
                or type(self.candidate_jets) is not tuple
                or not self.candidate_jets
                or type(self.proof_label) is not str or not self.proof_label):
            raise DiscreteSuccError("Missing declared polynomial source law")
        canonical=[]
        for candidate in self.candidate_jets:
            if type(candidate) is not tuple or len(candidate)!=self.degree_bound:
                raise DiscreteSuccError("Candidate violates declared polynomial degree")
            canonical.append(tuple(_vector(v,basis.dimension) for v in candidate))
        if len(set(canonical))!=len(canonical):
            raise DiscreteSuccError("Duplicate source-class initial jet")
        return True

    def fingerprint(self,basis:SharedBasis):
        self.verify(basis)
        return _hash({"basis":basis.fingerprint,
                      "degree":self.degree_bound,
                      "label":self.proof_label,
                      "source_candidates":[
                          [[str(v) for v in vec] for vec in jets]
                          for jets in self.candidate_jets],
                      })

    def contains(self,jets,basis:SharedBasis):
        self.verify(basis)
        canonical=tuple(_vector(v,basis.dimension) for v in jets)
        return canonical in self.candidate_jets


def encode_newton_jet(
    receiver:BasisState, basis:SharedBasis,
    samples:tuple[BasisState,...], law:PolynomialJetSourceFamily,
    horizon:int,
) -> bytes:
    receiver.validate(basis)
    law.verify(basis)
    if (type(horizon) is not int or not 0<=horizon<=128
            or len(samples)!=law.degree_bound+1):
        raise DiscreteSuccError("Need d+1 observed initial states for degree-d jet")
    jet=difference_jet_from_samples(samples,basis)
    if jet[0]!=receiver.coefficients or not law.contains(jet[1:],basis):
        raise DiscreteSuccError("Samples or derivative jet violate shared source-law context")
    predicted=newton_evaluate(receiver,jet[1:],horizon,basis)
    return _raw({
        "kind":"certified-newton-succ-jet-v1",
        "basis":basis.fingerprint,
        "anchor":receiver.anchor(basis),
        "law":law.fingerprint(basis),
        "degree":law.degree_bound,
        "horizon":horizon,
        "jets":[[str(v) for v in row] for row in jet[1:]],
        "end":predicted.anchor(basis),
    })


def decode_newton_jet(
    receiver:BasisState,packet:bytes,basis:SharedBasis,
    law:PolynomialJetSourceFamily,
) -> tuple[BasisState,...]:
    obj=_parse(packet,"certified-newton-succ-jet-v1",
               {"kind","basis","anchor","law","degree","horizon","jets","end"})
    law.verify(basis)
    if (obj["basis"]!=basis.fingerprint
            or obj["anchor"]!=receiver.anchor(basis)
            or obj["law"]!=law.fingerprint(basis)
            or type(obj["degree"]) is not int
            or obj["degree"]!=law.degree_bound
            or type(obj["horizon"]) is not int
            or not 0<=obj["horizon"]<=128
            or type(obj["jets"]) is not list
            or len(obj["jets"])!=law.degree_bound):
        raise DiscreteSuccError("Wrong initial state or missing proof of finite jet degree")
    jets=[]
    for vector in obj["jets"]:
        if type(vector) is not list or len(vector)!=basis.dimension:
            raise DiscreteSuccError("Malformed difference jet coefficient vector")
        jets.append(tuple(_fraction(v) for v in vector))
    if not law.contains(tuple(jets),basis):
        raise DiscreteSuccError("Unjustified Newton source-program coefficients")
    reconstructed=tuple(newton_evaluate(receiver,tuple(jets),n,basis)
                        for n in range(obj["horizon"]+1))
    if reconstructed[-1].anchor(basis)!=obj["end"]:
        raise DiscreteSuccError("Derivative jet and endpoint commitment disagree")
    return reconstructed


@dataclass(frozen=True)
class RationalFrame:
    """Invertible rational matrix, small enough for exact Gauss-Jordan."""
    rows:tuple[tuple[Fraction,...],...]

    def __post_init__(self):
        if (type(self.rows) is not tuple or not 1<=len(self.rows)<=8
                or any(type(row) is not tuple or len(row)!=len(self.rows)
                       for row in self.rows)):
            raise DiscreteSuccError("A local coordinate frame is a square matrix")
        object.__setattr__(self,"rows",
                           tuple(tuple(q(x) for x in row) for row in self.rows))

    @property
    def dim(self): return len(self.rows)

    @classmethod
    def identity(cls,dim):
        if type(dim) is not int or not 1<=dim<=8:
            raise DiscreteSuccError("Finite nonzero frame dimension required")
        return cls(tuple(tuple(Fraction(int(i==j)) for j in range(dim))
                         for i in range(dim)))

    def act(self, vector):
        v=_vector(vector,self.dim)
        return tuple(sum((a*b for a,b in zip(row,v)),Fraction(0))
                     for row in self.rows)

    def compose(self, prior:"RationalFrame") -> "RationalFrame":
        """self composed after prior; matrix multiplication self*prior."""
        if not isinstance(prior,RationalFrame) or prior.dim!=self.dim:
            raise DiscreteSuccError("Coordinate frames are not composable")
        return RationalFrame(tuple(
            tuple(sum((self.rows[i][k]*prior.rows[k][j]
                       for k in range(self.dim)),Fraction(0))
                  for j in range(self.dim))
            for i in range(self.dim)))

    def inverse(self) -> "RationalFrame":
        n=self.dim
        rows=[list(a)+list(b) for a,b in zip(
            self.rows,RationalFrame.identity(n).rows)]
        for col in range(n):
            pivot=next((i for i in range(col,n) if rows[i][col]!=0),None)
            if pivot is None:
                raise DiscreteSuccError("No inverse; transport loses coordinate information")
            rows[col],rows[pivot]=rows[pivot],rows[col]
            val=rows[col][col]
            rows[col]=[x/val for x in rows[col]]
            for k in range(n):
                if k!=col:
                    t=rows[k][col]
                    rows[k]=[a-t*b for a,b in zip(rows[k],rows[col])]
        return RationalFrame(tuple(tuple(row[n:]) for row in rows))


@dataclass(frozen=True)
class AffineStep:
    """One local-frame SUCC step y_next=U*y_current+eta."""
    transport:RationalFrame
    delta:tuple[Fraction,...]

    def __post_init__(self):
        if not isinstance(self.transport,RationalFrame):
            raise DiscreteSuccError("An action has a typed linear transport")
        object.__setattr__(self,"delta",
                           _vector(self.delta,self.transport.dim))

    @classmethod
    def identity(cls,dim):
        return cls(RationalFrame.identity(dim),_zero(dim))

    def act(self,vector):
        return _add(self.transport.act(vector),self.delta)

    def compose(self,prior:"AffineStep") -> "AffineStep":
        """self∘prior=(Uself Uprior, Uself eta_prior+eta_self)."""
        if not isinstance(prior,AffineStep):
            raise DiscreteSuccError("Affine path must compose other affine paths")
        return AffineStep(
            self.transport.compose(prior.transport),
            _add(self.transport.act(prior.delta),self.delta),
        )


def covariant_step(
    current_frame:RationalFrame,
    next_frame:RationalFrame,
    canonical_difference:tuple[Fraction,...],
) -> AffineStep:
    """Frame-covariant derivative connection.

    If y_n=F_n x_n and x_(n+1)=x_n+delta_n, then
    y_(n+1)=(F_(n+1)F_n^-1)y_n+F_(n+1)delta_n.
    """
    if current_frame.dim!=next_frame.dim:
        raise DiscreteSuccError("Changing frame changed the dimension")
    d=_vector(canonical_difference,current_frame.dim)
    return AffineStep(
        next_frame.compose(current_frame.inverse()),
        next_frame.act(d),
    )


def covariant_initial_jet_from_local_samples(
    frames:tuple[RationalFrame,...],
    local_samples:tuple[tuple[Fraction,...],...],
) -> tuple[tuple[Fraction,...],...]:
    """Return forward-difference jet PARALLEL-TRANSPORTED TO FRAME ZERO.

    Given y_n=F_n x_n at finitely many sampled times, convert each back
    into global coordinates x_n and compute Delta^r x_0. Finally express
    each such jet vector in the same initial local frame F_0.
    This does not assert a global recurrence or perform extra source probes.
    """
    if (type(frames) is not tuple or type(local_samples) is not tuple
            or not 1<=len(frames)==len(local_samples)<=33
            or any(not isinstance(frame,RationalFrame) for frame in frames)):
        raise DiscreteSuccError("Paired finite frames and source samples required")
    dim=frames[0].dim
    if any(frame.dim!=dim for frame in frames):
        raise DiscreteSuccError("Source coordinate dimensions differ")
    physical_in_canonical_frame=tuple(
        BasisState(frame.inverse().act(_vector(y,dim)))
        for frame,y in zip(frames,local_samples)
    )
    b=SharedBasis(dim)
    canonical_jet=difference_jet_from_samples(physical_in_canonical_frame,b)
    return tuple(frames[0].act(v) for v in canonical_jet)


def covariant_newton_evaluate(
    initial_local:tuple[Fraction,...],
    covariant_differences:tuple[tuple[Fraction,...],...],
    initial_frame:RationalFrame,
    target_frame:RationalFrame,
    n:int,
) -> tuple[Fraction,...]:
    """Discrete Taylor/Newton formula with a known (flat) frame connection.

    Let j_r=F_0 Delta^r x_0 and y_0=F_0 x_0. Then
        y_n=(F_n F_0^-1) * [ y_0 + sum_{r>=1} C(n,r) j_r ].

    For n within sampled data, the full N-th order jet is always exact.
    Beyond data, a finite d-th order jet is only SOURCE-FAITHFUL with an
    independently proven global Delta^(d+1) x=0 recurrence/source law.
    """
    if (not isinstance(initial_frame,RationalFrame)
            or not isinstance(target_frame,RationalFrame)
            or initial_frame.dim!=target_frame.dim
            or type(n) is not int or not 0<=n<=1000000
            or type(covariant_differences) is not tuple
            or len(covariant_differences)>32):
        raise DiscreteSuccError("Invalid local frames or bounded Newton jet")
    local=_vector(initial_local,initial_frame.dim)
    for r,candidate in enumerate(covariant_differences,1):
        v=_vector(candidate,initial_frame.dim)
        if r<=n:
            local=_add(local,_scale(comb(n,r),v))
    return target_frame.compose(initial_frame.inverse()).act(local)


def finite_covariant_newton_reconstruct_samples(
    frames:tuple[RationalFrame,...],
    local_samples:tuple[tuple[Fraction,...],...],
) -> tuple[tuple[Fraction,...],...]:
    """Unconditional EXACT finite inversion under arbitrary changing frames.

    Global frames are assumed known/invertible; no actual extra sources
    were probed and no prediction after the sampled horizon is certified.
    """
    jet=covariant_initial_jet_from_local_samples(frames,local_samples)
    returntuple=tuple(
        covariant_newton_evaluate(jet[0],jet[1:],frames[0],frame,n)
        for n,frame in enumerate(frames)
    )
    if returntuple!=tuple(_vector(s,frames[0].dim) for s in local_samples):
        raise ArithmeticError("Finite covariant Pascal inversion contradicted")
    return returntuple


def certified_covariant_newton_path(
    basis:SharedBasis,
    frames:tuple[RationalFrame,...],
    local_first_samples:tuple[tuple[Fraction,...],...],
    law:PolynomialJetSourceFamily,
) -> tuple[tuple[Fraction,...],...]:
    """Directly evaluate every future local frame under a shared global law.

    Source-class membership is a declared, externally justified premise.
    The caller provides known invertible F_n for ALL requested n. Without
    those transported coordinate maps, an initial jet in F_0 does not
    identify future local coordinates in other arbitrary changing frames.
    """
    law.verify(basis)
    d=law.degree_bound
    if (type(frames) is not tuple or not 1<=len(frames)<=129
            or len(frames)<d+1
            or type(local_first_samples) is not tuple
            or len(local_first_samples)!=d+1
            or basis.dimension>8
            or any(not isinstance(frame,RationalFrame)
                   or frame.dim!=basis.dimension for frame in frames)):
        raise DiscreteSuccError("Known full frame sequence and d+1 source samples needed")
    initial_jet=covariant_initial_jet_from_local_samples(
        frames[:d+1],local_first_samples)
    canonical_jets=tuple(frames[0].inverse().act(v)
                         for v in initial_jet[1:])
    if not law.contains(canonical_jets,basis):
        raise DiscreteSuccError("Global source recurrence is unverified for this local jet")
    return tuple(
        covariant_newton_evaluate(initial_jet[0],initial_jet[1:],
                                  frames[0],frame,n)
        for n,frame in enumerate(frames)
    )


@dataclass(frozen=True)
class AffineScanReceipt:
    values:tuple[tuple[Fraction,...],...]
    dependency_layers:int
    composition_count:int
    actual_parallel_execution_performed:bool = False


def parallel_prefix_affine(
    initial:tuple[Fraction,...],actions:tuple[AffineStep,...],
) -> AffineScanReceipt:
    """Associative ordered affine scan: independent layers are parallelizable.

    Does NOT change the physical measurement causality required to create
    the actions. Python loops run sequentially; the reported O(log N)
    is circuit dependency depth if an actual parallel runtime is supplied.
    """
    if type(actions) is not tuple or len(actions)>128:
        raise DiscreteSuccError("A finite ordered action path is required")
    initial=_vector(initial)
    if any(a.transport.dim!=len(initial) for a in actions):
        raise DiscreteSuccError("Incompatible local frame vector dimensions")
    composed=list(actions)
    offset=1
    stages=work=0
    while offset<len(composed):
        prior=tuple(composed)
        for i in range(offset,len(composed)):
            composed[i]=prior[i].compose(prior[i-offset])
            work+=1
        stages+=1
        offset*=2
    vector_trace=(initial,)+tuple(op.act(initial) for op in composed)
    current=initial
    expected=[current]
    for op in actions:
        current=op.act(current)
        expected.append(current)
    if tuple(expected)!=vector_trace:
        raise ArithmeticError("Associative affine prefix failed discrete SUCC")
    return AffineScanReceipt(vector_trace,stages,work)


def succ_derivative_demo():
    basis=SharedBasis(6)
    initial=BasisState.from_sparse(basis,{1:2,2:7,4:3})
    first=SparseDelta((1,4,5),(Fraction(1),)*3)
    path=(first,SparseDelta((1,5),(Fraction(2),Fraction(-1))),
          SparseDelta((1,4),(Fraction(-1),Fraction(2))),
          SparseDelta((4,5),(Fraction(3),Fraction(1))))
    true_trace=finite_difference_states(initial,path,basis)
    packet=encode_step_differences(true_trace[-1],initial,basis,path)
    recovered=decode_step_differences(initial,packet,basis)
    if recovered.states!=true_trace:
        raise ArithmeticError("All intermediate SUCC states were not reconstructed")
    if finite_newton_reconstruct_samples(true_trace,basis)!=true_trace:
        raise ArithmeticError("Arbitrary FINITE Newton data was incorrectly inverted")
    # A low-degree source family generates a VERY long path via a short jet.
    d1=(Fraction(1),Fraction(0),Fraction(0),Fraction(1),Fraction(1),Fraction(0))
    d2=(Fraction(1),Fraction(0),Fraction(0),Fraction(-1),Fraction(0),Fraction(0))
    law=PolynomialJetSourceFamily(
        basis.fingerprint,2,((d1,d2),(tuple(-x for x in d1),_zero(6))))
    samples=tuple(newton_evaluate(initial,(d1,d2),n,basis) for n in range(3))
    small_packet=encode_newton_jet(initial,basis,samples,law,24)
    polynomial_trace=decode_newton_jet(initial,small_packet,basis,law)
    if len(polynomial_trace)!=25 or any(
        polynomial_trace[n]!=newton_evaluate(initial,(d1,d2),n,basis)
        for n in range(25)
    ):
        raise ArithmeticError("Polynomial source law failed direct reconstructed evaluation")
    # A/B change of basis with nontrivial transport between two steps.
    F0=RationalFrame.identity(2)
    F1=RationalFrame(((0,1),(1,0)))
    F2=RationalFrame(((1,1),(0,1)))
    x0=(Fraction(2),Fraction(3))
    deltas=((Fraction(1),Fraction(0)),(Fraction(0),Fraction(2)))
    steps=(covariant_step(F0,F1,deltas[0]),
           covariant_step(F1,F2,deltas[1]))
    scan=parallel_prefix_affine(F0.act(x0),steps)
    x1=_add(x0,deltas[0])
    x2=_add(x1,deltas[1])
    if scan.values!=(F0.act(x0),F1.act(x1),F2.act(x2)):
        raise ArithmeticError("Discrete covariant SUCC frame transport not commuting")
    return {
        "status":"EXACT_DISCRETE_SUCC_DERIVATIVE_INTEGRATION",
        "basis_indices":[1,2,3,4,5,6],
        "initial_condition_is_receiver_anchored":True,
        "ordinary_difference_steps":len(path),
        "all_intermediate_succ_states_reconstructed":True,
        "unconditional_newton_inversion_of_all_observed_finite_steps":True,
        "additive_prefix_parallel_dependency_layers":recovered.parallelizable_dependency_depth,
        "additive_prefix_executed_on_actual_parallel_hardware":False,
        "polynomial_degree_law":law.degree_bound,
        "polynomial_reconstructed_states":len(polynomial_trace),
        "polynomial_jet_directions_count":len((d1,d2)),
        "law_premise_proved_from_finite_samples_alone":False,
        "covariant_frame_transport_square_commutes":True,
        "affine_parallel_dependency_layers":scan.dependency_layers,
        "affine_prefix_actually_parallel_executed":False,
        "real_world_source_measurement_authenticated":False,
        "RH_claimed":False,
    }
