"""Basis-indexed relative SUCC deltas and an exact boundary Fourier code.

Scope: finite-support Q-coefficient updates in a countably indexed shared
basis, with executable six-mode test windows. Under a shared, versioned
dictionary and last-known position, a packet (directions, values) specifies
a state DIFFERENCE, not the entire sender's current state.

Tests distinguish:
 * commutative sparse vector deltas versus NONCOMMUTING ordered path actions;
 * honest proof-induced value compression versus guessed source restrictions;
 * exact reconstruction of degree<6 mode polynomials from all sixth-root
   boundary samples versus higher-mode aliasing.

A sixth-root Fourier code is a classical mathematical boundary encoding; it
does not constitute gravitational holography, black-hole entropy, or an RH
zero-to-bulk theorem. Source/proof/physical-event authentication is EXTERNAL.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import comb
import json


class BasisTransportError(ValueError):
    """Ill-typed basis, stale anchor, or non-justified encoded assertion."""


def _q(x) -> Fraction:
    if type(x) is int or isinstance(x,Fraction):
        return Fraction(x)
    raise BasisTransportError("Use exact Fraction or integer coefficients")


def _as_decimal_string(x):
    return str(_q(x))


def _parse_fraction(s):
    if type(s) is not str or not 0 < len(s) <= 100:
        raise BasisTransportError("Malformed rational source coefficient")
    try:
        return Fraction(s)
    except (ValueError,ZeroDivisionError,OverflowError) as e:
        raise BasisTransportError("Invalid rational source coefficient") from e


def _wire(obj) -> bytes:
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()


def _hash(obj) -> str:
    return sha256(_wire(obj)).hexdigest()


@dataclass(frozen=True)
class SharedBasis:
    """Finite declared observable window e1..eN of countable e1,e2,... basis."""
    dimension: int
    version: str = "shared-countable-basis-window-v1"

    def __post_init__(self):
        if type(self.dimension) is not int or not 1 <= self.dimension <= 128:
            raise BasisTransportError("Finite bounded test window required")
        if type(self.version) is not str or not self.version:
            raise BasisTransportError("Versioned shared mathematical language required")

    @property
    def fingerprint(self):
        return _hash({"version":self.version,"indices":list(range(1,self.dimension+1))})


@dataclass(frozen=True)
class BasisState:
    coefficients: tuple[Fraction,...]

    def __post_init__(self):
        if type(self.coefficients) is not tuple or len(self.coefficients) > 128:
            raise BasisTransportError("Immutable bounded coefficients required")
        object.__setattr__(self,"coefficients",tuple(_q(x) for x in self.coefficients))

    @classmethod
    def from_sparse(cls, basis: SharedBasis, entries: dict[int,object]):
        if type(entries) is not dict or any(
            type(i) is not int or not 1 <= i <= basis.dimension for i in entries
        ):
            raise BasisTransportError("Unknown shared-basis coordinate")
        return cls(tuple(_q(entries.get(i,0)) for i in range(1,basis.dimension+1)))

    def validate(self,basis: SharedBasis):
        if len(self.coefficients) != basis.dimension:
            raise BasisTransportError("State and shared basis window disagree")
        return self

    def anchor(self,basis: SharedBasis):
        self.validate(basis)
        return _hash({"basis":basis.fingerprint,"coefficients":[str(x) for x in self.coefficients]})

    def update(self,delta: "SparseDelta",basis: SharedBasis):
        self.validate(basis)
        delta.validate(basis)
        v=list(self.coefficients)
        for i,d in zip(delta.indices,delta.values):
            v[i-1]+=d
        return BasisState(tuple(v))


@dataclass(frozen=True)
class SparseDelta:
    """Sparse *commutative* additive update; indices are basis directions."""
    indices: tuple[int,...]
    values: tuple[Fraction,...]

    def __post_init__(self):
        if (type(self.indices) is not tuple or type(self.values) is not tuple
                or len(self.indices) != len(self.values)
                or len(self.indices) > 128 or len(set(self.indices))!=len(self.indices)
                or any(type(i) is not int or i < 1 for i in self.indices)):
            raise BasisTransportError("Pair unique positive basis directions with values")
        object.__setattr__(self,"values",tuple(_q(x) for x in self.values))

    def validate(self,basis: SharedBasis):
        if any(i > basis.dimension for i in self.indices):
            raise BasisTransportError("Delta names a direction outside shared basis")
        return self

    def canonical(self):
        d={i:v for i,v in zip(self.indices,self.values) if v!=0}
        return SparseDelta(tuple(sorted(d)),tuple(d[i] for i in sorted(d)))

    def add(self,other:"SparseDelta",basis: SharedBasis):
        self.validate(basis)
        other.validate(basis)
        accum={}
        for i,v in (*zip(self.indices,self.values),*zip(other.indices,other.values)):
            accum[i]=accum.get(i,Fraction())+v
        return SparseDelta(tuple(sorted(accum)),tuple(accum[i] for i in sorted(accum))).canonical()


@dataclass(frozen=True)
class CertifiedEqualFamily:
    """Exhaustively checked finite premise for a reusable 'all coefficients equal' proof.

    A mathematical lemma is valid only relative to its candidate source
    class, here a finite family supplied and verified by both observers.
    This is not a proof that the real universe satisfies that source prior.
    """
    directions: tuple[int,...]
    admissible_deltas: tuple[SparseDelta,...]
    label: str = "equal-support-coefficients-v1"

    def verify(self,basis: SharedBasis):
        if (type(self.directions) is not tuple or not self.directions
                or len(set(self.directions))!=len(self.directions)
                or any(type(i) is not int or not 1 <= i <= basis.dimension
                       for i in self.directions)
                or type(self.admissible_deltas) is not tuple
                or not self.admissible_deltas
                or type(self.label) is not str or not self.label):
            raise BasisTransportError("A nonempty, typed source family is required")
        target=set(self.directions)
        for delta in self.admissible_deltas:
            delta.validate(basis)
            if set(delta.indices)!=target or len(set(delta.values))!=1:
                raise BasisTransportError("Proposed proof fails over declared source class")
        return True

    def fingerprint(self,basis: SharedBasis):
        self.verify(basis)
        canonical=[(d.canonical().indices,[str(q) for q in d.canonical().values])
                   for d in self.admissible_deltas]
        return _hash({"basis":basis.fingerprint,"label":self.label,
                      "directions":self.directions,"source_candidates":canonical})


def _parse_packet(payload,kind,fields):
    if type(payload) is not bytes or not 0 < len(payload) <= 1000000:
        raise BasisTransportError("Finite bounded packet required")
    try:
        obj=json.loads(payload.decode("utf-8"))
    except (UnicodeError,ValueError) as exc:
        raise BasisTransportError("Malformed delta packet") from exc
    if type(obj) is not dict or set(obj)!=fields or obj.get("kind")!=kind:
        raise BasisTransportError("Unexpected versioned delta packet")
    return obj


def encode_sparse_delta(sender: BasisState,receiver: BasisState,
                        basis: SharedBasis,delta: SparseDelta,
                        certified_family: CertifiedEqualFamily|None=None) -> bytes:
    """A's knowledge as a PATCH relative to B's exact last state."""
    sender.validate(basis)
    receiver.validate(basis)
    delta.validate(basis)
    if receiver.update(delta,basis) != sender:
        raise BasisTransportError("Submitted delta does not reconstruct sender's state")
    if certified_family is None:
        mode="unrestricted"
        values=[str(q) for q in delta.values]
        proof_id=None
    else:
        certified_family.verify(basis)
        if (tuple(delta.indices)!=certified_family.directions
                or delta not in certified_family.admissible_deltas):
            raise BasisTransportError("Sender delta violates verified premise/source family")
        mode="equal-coefficients"
        values=[str(delta.values[0])]
        proof_id=certified_family.fingerprint(basis)
    return _wire({
        "kind":"basis-relative-delta-v1",
        "basis":basis.fingerprint,
        "anchor":receiver.anchor(basis),
        "end":sender.anchor(basis),
        "directions":list(delta.indices),
        "values":values,
        "mode":mode,
        "proof":proof_id,
    })


def decode_sparse_delta(receiver: BasisState,payload: bytes,
                        basis: SharedBasis,
                        certified_family: CertifiedEqualFamily|None=None) -> BasisState:
    receiver.validate(basis)
    obj=_parse_packet(payload,"basis-relative-delta-v1",
                     {"kind","basis","anchor","end","directions","values","mode","proof"})
    if (obj["basis"]!=basis.fingerprint
            or obj["anchor"]!=receiver.anchor(basis)
            or type(obj["directions"]) is not list
            or type(obj["values"]) is not list
            or len(obj["directions"])>basis.dimension
            or any(type(i) is not int for i in obj["directions"])):
        raise BasisTransportError("Stale position, wrong basis, or invalid directions")
    indices=tuple(obj["directions"])
    if obj["mode"]=="unrestricted":
        if obj["proof"] is not None or len(obj["values"])!=len(indices):
            raise BasisTransportError("Unrestricted deltas need all source values")
        values=tuple(_parse_fraction(x) for x in obj["values"])
    elif obj["mode"]=="equal-coefficients":
        if certified_family is None or len(obj["values"])!=1:
            raise BasisTransportError("Missing trusted source-specific proof family")
        certified_family.verify(basis)
        if (obj["proof"]!=certified_family.fingerprint(basis)
                or indices!=certified_family.directions):
            raise BasisTransportError("No matching proved value compression rule")
        v=_parse_fraction(obj["values"][0])
        values=(v,)*len(indices)
    else:
        raise BasisTransportError("Unknown proof-aware encoding mode")
    delta=SparseDelta(indices,values).validate(basis)
    if obj["mode"]=="equal-coefficients" and delta not in certified_family.admissible_deltas:
        raise BasisTransportError("Reconstruction outside certified source class")
    result=receiver.update(delta,basis)
    if result.anchor(basis)!=obj["end"]:
        raise BasisTransportError("Decoder result did not match declared endpoint")
    return result


@dataclass(frozen=True)
class FrameActionBasis:
    """Noncommuting path directions in a shared local coordinate frame.

    Index 1: translate by value.
    Index 4: dilate by (1+value).
    Index 5: translate by value.
    Not a basis of a linear vector space: these are state operations and
    the path order is part of the meaning.
    """
    version: str = "frame-actions-v1"
    indices: tuple[int,...] = (1,4,5)

    @property
    def fingerprint(self):
        return _hash({"kind":"affine-ordered-operators","indices":self.indices,
                      "version":self.version,
                      "operator_types":("translate","dilate","translate")})

    def step(self,state,idx:int,value):
        state,value=_q(state),_q(value)
        if idx == 1 or idx == 5:
            return state+value
        if idx == 4:
            return state*(1+value)
        raise BasisTransportError("Unknown basis action")

    def apply(self,state,path:tuple[tuple[int,Fraction],...]):
        if type(path) is not tuple:
            raise BasisTransportError("Ordered path must be an immutable sequence")
        current=_q(state)
        for idx,v in path:
            if type(idx) is not int or idx not in self.indices:
                raise BasisTransportError("Path direction absent in shared operator language")
            current=self.step(current,idx,v)
        return current


def encode_action_path(initial,steps:tuple[tuple[int,Fraction],...],
                       operators:FrameActionBasis) -> bytes:
    if type(steps) is not tuple or len(steps)>64:
        raise BasisTransportError("Finite ordered path needed")
    current=_q(initial)
    final=operators.apply(current,steps)
    return _wire({
        "kind":"ordered-frame-delta-v1",
        "basis":operators.fingerprint,
        "anchor":str(current),
        "steps":[[i,str(_q(v))] for i,v in steps],
        "end":str(final),
    })


def decode_action_path(initial,packet:bytes,operators:FrameActionBasis):
    obj=_parse_packet(packet,"ordered-frame-delta-v1",
                      {"kind","basis","anchor","steps","end"})
    if (obj["basis"]!=operators.fingerprint
            or obj["anchor"]!=str(_q(initial))
            or type(obj["steps"]) is not list
            or len(obj["steps"])>64):
        raise BasisTransportError("Stale/nonlocal action-path anchor")
    path=[]
    for pair in obj["steps"]:
        if type(pair) is not list or len(pair)!=2 or type(pair[0]) is not int:
            raise BasisTransportError("Malformed operation direction/value pair")
        path.append((pair[0],_parse_fraction(pair[1])))
    result=operators.apply(initial,tuple(path))
    if str(result)!=obj["end"]:
        raise BasisTransportError("Reconstructed path endpoint mismatched commitment")
    return result


@dataclass(frozen=True)
class Root6:
    """Exact Q(sqrt(-3)), as a+b*zeta_6, where zeta_6^2=zeta_6-1."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self,"a",_q(self.a))
        object.__setattr__(self,"b",_q(self.b))

    def __add__(self,other):
        if not isinstance(other,Root6):
            return NotImplemented
        return Root6(self.a+other.a,self.b+other.b)

    def __neg__(self):
        return Root6(-self.a,-self.b)

    def __sub__(self,other):
        return self+(-other)

    def __mul__(self,other):
        if not isinstance(other,Root6):
            return NotImplemented
        # zeta_6^2=zeta_6-1
        return Root6(self.a*other.a-self.b*other.b,
                     self.a*other.b+self.b*other.a+self.b*other.b)

    def scale(self,q):
        q=_q(q)
        return Root6(self.a*q,self.b*q)

    def conjugate(self):
        # conjugate(zeta_6)=1-zeta_6
        return Root6(self.a+self.b,-self.b)

    def power(self,n:int):
        if type(n) is not int:
            raise BasisTransportError("Integer Fourier exponent required")
        n=n%6
        result=Root6(1)
        unit=Root6(0,1)
        for _ in range(n):
            result=result*unit
        return result


def boundary_evaluations(coefficients:tuple[Fraction,...]):
    """Evaluate any rational polynomial at all six sixth roots of unity.

    Up to degree 5, this boundary encoding has an EXACT inverse.
    With unbounded degrees, z^6-1 is an explicit nonzero kernel element.
    """
    if type(coefficients) is not tuple or len(coefficients)>128:
        raise BasisTransportError("Finite polynomial coefficients required")
    a=tuple(_q(x) for x in coefficients)
    zeta=Root6(0,1)
    samples=[]
    for j in range(6):
        point=zeta.power(j)
        result=Root6()
        zpow=Root6(1)
        for x in a:
            result=result+zpow.scale(x)
            zpow=zpow*point
        samples.append(result)
    return tuple(samples)


def boundary_decode_bandlimited(samples:tuple[Root6,...]) -> tuple[Fraction,...]:
    """Exact inverse DFT for degree <= 5 mode functions.

    a_n = (1/6)sum_{j=0}^5 F(zeta^j)*zeta^(-jn).
    This is NOT a decoder of arbitrary unconstrained infinite functions.
    """
    if (type(samples) is not tuple or len(samples)!=6
            or any(not isinstance(x,Root6) for x in samples)):
        raise BasisTransportError("Need all six exact boundary values")
    zeta=Root6(0,1)
    output=[]
    for n in range(6):
        result=Root6()
        for j,value in enumerate(samples):
            result=result+value*zeta.power(-j*n)
        coeff=result.scale(Fraction(1,6))
        if coeff.b!=0:
            raise BasisTransportError("Boundary data inconsistent with rational bandlimited source")
        output.append(coeff.a)
    return tuple(output)


def radial_mode_samples(coefficients:tuple[Fraction,...],radius) -> tuple[Root6,...]:
    """Exact analytic-polynomial samples at r*zeta6^j, 0<r<=1.

    Mode n is attenuated by r^n. The inverse exists on declared degree<6
    polynomials when r>0 but can amplify finite measurement errors by r^-n.
    """
    radius=_q(radius)
    if not 0 < radius <= 1:
        raise BasisTransportError("Normalized positive rational radius at most one required")
    if type(coefficients) is not tuple or len(coefficients)>6:
        raise BasisTransportError("Radial probe expects declared six-mode code subspace")
    return boundary_evaluations(tuple(_q(c)*radius**n
                                      for n,c in enumerate(coefficients)))


def decode_radial_modes(samples:tuple[Root6,...],radius) -> tuple[Fraction,...]:
    radius=_q(radius)
    if not 0 < radius <= 1:
        raise BasisTransportError("Positive radius required for algebraic inverse")
    attenuated=boundary_decode_bandlimited(samples)
    return tuple(c/radius**n for n,c in enumerate(attenuated))


def round_root6_samples(samples:tuple[Root6,...],step) -> tuple[Root6,...]:
    """Toy finite-precision apparatus; round rational components separately.

    This measures neither real-world entropy nor black-hole boundary data.
    It is an explicit non-injective observation map at the declared precision.
    """
    step=_q(step)
    if step<=0 or any(not isinstance(z,Root6) for z in samples):
        raise BasisTransportError("Positive finite precision and exact source samples required")
    return tuple(Root6(Q(round(z.a/step))*step,Q(round(z.b/step))*step)
                 for z in samples)


def zero_only_line_counterexample():
    """Two symmetric entire polynomial functions with identical critical-line
    zeros, but only one contains additional off-line zeros.

    Let w=s-1/2, F=1+w^2, G=(1+w^2)(1-16w^2). Both satisfy s<->1-s
    reflection and reality symmetry. The extra second factor has roots
    w=+/-1/4 (s=1/4 and 3/4) but is 1+16*t^2 >0 on w=i*t.
    Hence the set of CRITICAL-LINE zeros alone is not a complete
    reconstruction code for the broader function class.

    Neither polynomial has the Euler product, Gamma completion, prescribed
    growth or other specific constraints of the true xi function. This
    countermodel is NOT an RH counterexample.
    """
    # Values (real,imag) of a polynomial in w with Q[i] arithmetic.
    def sq(x,y):
        x,y=_q(x),_q(y)
        return x*x-y*y, 2*x*y

    def fg(wr,wi):
        ur,ui=sq(wr,wi)
        fr,fi=Q(1)+ur,ui
        hr,hi=Q(1)-16*ur,-16*ui
        return ((fr,fi),(fr*hr-fi*hi,fr*hi+fi*hr))

    for t in (Q(-3),Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),Q(3)):
        F,G=fg(0,t)
        if (F==(Q(0),Q(0)))!=(G==(Q(0),Q(0))):
            raise ArithmeticError("Critical-line zero agreement control failed")
    for wr in (Q(-1,4),Q(1,4)):
        F,G=fg(wr,0)
        if F==(Q(0),Q(0)) or G!=(Q(0),Q(0)):
            raise ArithmeticError("New off-line zero was not established")
    return {
        "status":"SYMMETRIC_ENTIRE_POLYNOMIAL_LINE_ZERO_NONUNIQUENESS",
        "line_zeros_in_both":["1/2-i","1/2+i"],
        "extra_offline_zeros_in_one":["1/4","3/4"],
        "both_respect_s_to_one_minus_s":True,
        "both_respect_reality_conjugation":True,
        "line_zero_locations_alone_determine_global_entire_function":False,
        "full_exact_line_function_values_have_identity_theorem_uniqueness":True,
        "either_function_is_true_riemann_xi":False,
        "RH_disproved_or_proved":False,
    }


def finite_boundary_demo():
    basis=SharedBasis(6)
    origin=BasisState.from_sparse(basis,{1:2,2:7,4:3})
    delta=SparseDelta((1,4,5),(1,1,1))
    endpoint=origin.update(delta,basis)
    packet=encode_sparse_delta(endpoint,origin,basis,delta)
    if decode_sparse_delta(origin,packet,basis)!=endpoint:
        raise ArithmeticError("Basis-indexed sparse packet did not round-trip")
    family=CertifiedEqualFamily(
        (1,4,5),tuple(SparseDelta((1,4,5),(v,v,v))
                       for v in (Fraction(0),Fraction(1),Fraction(2))),
    )
    proof_packet=encode_sparse_delta(endpoint,origin,basis,delta,family)
    if decode_sparse_delta(origin,proof_packet,basis,family)!=endpoint:
        raise ArithmeticError("Proof-induced coefficient sharing failed")
    parsed=json.loads(proof_packet.decode())
    if parsed["values"]!=["1"]:
        raise ArithmeticError("Proof did not reduce three value codes to one")
    code=(Fraction(0),Fraction(1),Fraction(0),Fraction(0),Fraction(1),Fraction(1))
    boundary=boundary_evaluations(code)
    if boundary_decode_bandlimited(boundary)!=code:
        raise ArithmeticError("Exact sixth-root Fourier recovery violated")
    alias=boundary_evaluations((Fraction(-1),)+(Fraction(0),)*5+(Fraction(1),))
    if alias!=boundary_evaluations(()) or all(c==0 for c in code):
        raise ArithmeticError("Nontrivial high-mode boundary alias not detected")
    hidden_mode=(Q(0),)*5+(Q(1),)
    r=Q(1,2)
    exact_radial=radial_mode_samples(hidden_mode,r)
    if decode_radial_modes(exact_radial,r)!=hidden_mode:
        raise ArithmeticError("Exact radial reconstructability was violated")
    truncated=round_root6_samples(exact_radial,Q(1,8))
    if truncated!=round_root6_samples(radial_mode_samples((Q(0),)*6,r),Q(1,8)):
        raise ArithmeticError("Expected finite-precision high-mode blindness not observed")
    line_zero_control=zero_only_line_counterexample()
    action=FrameActionBasis()
    ordered=((1,Fraction(1)),(4,Fraction(1)),(5,Fraction(1)))
    permuted=((4,Fraction(1)),(1,Fraction(1)),(5,Fraction(1)))
    if action.apply(0,ordered)!=3 or action.apply(0,permuted)!=2:
        raise ArithmeticError("Noncommuting ordered-path witness invalid")
    return {
        "status":"EXACT_SHARED_BASIS_RELATIVE_BOUNDARY_TRANSPORT",
        "basis_indices":[1,2,3,4,5,6],
        "source_packet_directions":[1,4,5],
        "source_packet_values":[1,1,1],
        "state_transmitted_as_snapshot":False,
        "receiver_sparse_update_correct":True,
        "proof_context_value_codes_before":3,
        "proof_context_value_codes_after":len(parsed["values"]),
        "total_message_bit_optimality_claimed":False,
        "noncommutative_ordered_path_endpoints":[3,2],
        "boundary_exact_bandlimited_reconstruction":True,
        "boundary_unrestricted_high_mode_alias_exists":True,
        "radial_exact_high_mode_reconstruction":True,
        "radial_high_mode_attenuation":"1/32",
        "finite_precision_root_six_samples_hide_mode_five":True,
        "critical_line_zero_only_incomplete_for_symmetric_polynomial_family":True,
        "true_xi_line_zero_locations_claimed_complete":False,
        "line_zero_control":line_zero_control,
        "boundary_probe_count":6,
        "three_of_six_support_min_fixed_bits":(comb(6,3)-1).bit_length(),
        "gravity_holographic_correspondence_proved":False,
        "RH_claimed":False,
    }
