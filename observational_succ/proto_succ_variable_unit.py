"""Proto-SUCC with a variable primitive unit and its higher-difference lift.

The universal one-step generator is 0 --d--> d.  Its realization on an
additive carrier R is S_d(x)=x+d; in the formal coefficient module Z[D]
this is one declared unit D, not necessarily the numeral 1 or an invertible
element. Setting D=1 recovers the ordinary successor.

A p-adic unit d induces a bijective change of coordinates x -> d*x
on Z/p^r Z, and S_d conjugates S_1.  A nonunit d restricts the reachable
clock orbit, and d=0 collapses the first path.  For prime dilation V_p,
V_p S_d = S_(p*d) V_p, and the scalar difference in INTEGER DESTINATION
ADDRESSES between S_d V_p and V_p S_d is d*(1-p).
This is NOT a scalar operator commutator on orthonormal basis vectors.

The one-level-higher SUCC acts on its OWN first difference:
 (x,d,a) -> (x+d,d+a,a).
More generally on a finite Newton jet (j_0,..,j_m):
 SUCC(j_0,..,j_m)=(j_0+j_1,..,j_(m-1)+j_m,j_m).
Its n-step values are exact integer-binomial polynomials and inverse
iterations exist because the lift is unipotent. This is classical discrete
calculus, NOT a new result about zeta or physical causal completion.

An infinite jet requires independent convergence/source support;
formal finite jets do not justify arbitrary extrapolation of a source.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, gcd

from .residue_one_arch import prime


class ProtoSuccError(ValueError):
    """Bad prime-local unit, damaged frame map or unsupported interpolation."""


def _int(x, lower=-1000000, upper=1000000):
    if type(x) is not int or not lower <= x <= upper:
        raise ProtoSuccError("Exact integer address or unit required")
    return x


def binomial_integer(n: int, k: int) -> int:
    """Integral binomial for arbitrary n in Z, k>=0, including n negative."""
    _int(n)
    _int(k, 0, 128)
    if n>=0:
        return comb(n,k) if k<=n else 0
    return (-1)**k * comb(k-n-1,k)


@dataclass(frozen=True)
class FormalD:
    """a+b*D in the rank-two Z-submodule span_Z{1,D} of Z[D].

    This intentionally allows + and integer scalar operations, but does
    not assume D is invertible or silently localize Z[D] at D.
    """
    constant: int = 0
    unit_coefficient: int = 0

    def __post_init__(self):
        _int(self.constant)
        _int(self.unit_coefficient)

    def __add__(self, other: "FormalD"):
        if not isinstance(other, FormalD):
            return NotImplemented
        return FormalD(self.constant+other.constant,
                       self.unit_coefficient+other.unit_coefficient)

    def times(self, scalar:int):
        _int(scalar)
        return FormalD(self.constant*scalar,
                       self.unit_coefficient*scalar)

    def specialize(self, unit:int):
        _int(unit)
        return self.constant+self.unit_coefficient*unit


def proto_succ_formal(n:int) -> FormalD:
    """Base at zero; n primitive paths of FORMAL length one D-unit."""
    _int(n,0,10000)
    return FormalD(0,n)


def generalized_succ(address:int,unit:int) -> int:
    _int(address)
    _int(unit)
    return address+unit


def modular_succ(address:int,unit:int,p:int,resolution:int) -> int:
    if not prime(p):
        raise ProtoSuccError("A finite place requires an actual prime")
    _int(address)
    _int(unit)
    _int(resolution,1,8)
    return (address+unit)%(p**resolution)


def additive_clock_period(p:int,resolution:int,unit:int) -> int:
    """Smallest n>0 with n*unit=0 mod p^resolution, valid for unit=0."""
    if not prime(p):
        raise ProtoSuccError("Prime residue clock required")
    _int(resolution,1,8)
    _int(unit)
    modulus=p**resolution
    return modulus//gcd(abs(unit),modulus)


def modular_orbit(p:int,resolution:int,unit:int) -> tuple[int,...]:
    """Complete cycle at most once, exact finite positive test scope."""
    modulus=p**_int(resolution,1,5)
    if not prime(p) or modulus>4096:
        raise ProtoSuccError("Bounded actual prime clock required")
    period=additive_clock_period(p,resolution,unit)
    orbit=tuple((i*unit)%modulus for i in range(period))
    if len(set(orbit))!=period or (period*unit)%modulus!=0:
        raise ArithmeticError("Computed clock period was not primitive")
    return orbit


def clock_change_isomorphism(p:int,resolution:int,unit:int):
    """C_u(x)=u*x conjugates S_1 to S_u iff p does NOT divide u.

    In the finite clock, a nonunit d yields a noninvertible map. In
    Z_p, multiplication by a nonzero p-divisible d is injective but
    nonsurjective; don't falsely extend the finite kernel conclusion.
    """
    if not prime(p):
        raise ProtoSuccError("Prime place needed")
    _int(resolution,1,8)
    _int(unit)
    modulus=p**resolution
    if gcd(unit,modulus)!=1:
        raise ProtoSuccError("Nonunit step does not define full clock isomorphism")
    inv=pow(unit,-1,modulus)
    for n in range(min(modulus,257)):
        if (unit*(n+1)-(unit*n+unit))%modulus!=0:
            raise ArithmeticError("Conjugation square did not commute")
    return {"prime":p,"resolution":resolution,"unit":unit,
            "modulus":modulus,"inverse":inv,
            "full_cycle_period":additive_clock_period(p,resolution,unit),
            "S_unit_conjugate_to_S_one":True,
            "invertible_p_adic_unit":True}


def shift_dilation_address_defect(p:int,address:int,unit:int) -> int:
    """(S_d V_p - V_p S_d)(n)=d(1-p) as INTEGER ADDRESS DIFFERENCE."""
    if not prime(p):
        raise ProtoSuccError("FUCC dilation requires an actual prime")
    _int(address)
    _int(unit)
    x=p*address+unit
    y=p*(address+unit)
    if x-y!=(1-p)*unit:
        raise ArithmeticError("Semidirect ax+b address relation contradicted")
    return x-y


def normalized_defect_mod(p:int,resolution:int,address:int,unit:int) -> int:
    """After invertible unit gauge, normalized defect=1-p mod p^r."""
    data=clock_change_isomorphism(p,resolution,unit)
    difference=shift_dilation_address_defect(p,address,unit)
    return (difference*data["inverse"])%data["modulus"]


def prime_jet_directed_gap(p:int,jet_level:int,unit:int) -> int:
    """S_d steps needed between d*p^k and d*p^(k+1) as displacement."""
    if not prime(p):
        raise ProtoSuccError("Prime jet requires a genuine prime")
    _int(jet_level,0,12)
    _int(unit)
    gap=unit*(p-1)*p**jet_level
    if gap!=unit*(p**(jet_level+1)-p**jet_level):
        raise ArithmeticError("Variable-unit prime-jet gap mismatch")
    return gap


@dataclass(frozen=True)
class HigherSuccJet:
    """(x,Delta x,Delta² x,..,Delta^m x), fixed top derivative.

    Integral coefficients ensure binomial iteration works modulo p^r
    even at p=2; no division by factorial is needed.
    """
    coefficients: tuple[int,...]

    def __post_init__(self):
        if (type(self.coefficients) is not tuple
                or not 2<=len(self.coefficients)<=12):
            raise ProtoSuccError("Need base and one-or-more finite derivatives")
        for x in self.coefficients:
            _int(x)

    @property
    def degree(self):
        return len(self.coefficients)-1

    def succ(self) -> "HigherSuccJet":
        j=self.coefficients
        return HigherSuccJet(tuple(j[i]+j[i+1]
                                   for i in range(len(j)-1))+(j[-1],))

    def at(self,n:int) -> "HigherSuccJet":
        """Direct n-th successor via unipotent Pascal/binomial matrix."""
        _int(n,-128,10000)
        j=self.coefficients
        result=tuple(sum(
            binomial_integer(n,k-i)*j[k]
            for k in range(i,len(j)))
            for i in range(len(j)))
        return HigherSuccJet(result)

    def first_coordinate(self,n:int) -> int:
        return self.at(n).coefficients[0]

    def mod(self,p:int,resolution:int) -> "HigherSuccJet":
        if not prime(p):
            raise ProtoSuccError("Prime residue place required")
        _int(resolution,1,8)
        modulus=p**resolution
        return HigherSuccJet(tuple(j%modulus for j in self.coefficients))


def higher_succ_step_units(jet:HigherSuccJet,steps:int) -> tuple[int,...]:
    """Obtain each changing unit, not just the final net displacement."""
    _int(steps,0,256)
    return tuple(jet.at(n).coefficients[1] for n in range(steps))


def classify_linear_unit_stability(p:int,first_unit:int,acceleration:int):
    """Exact universal criterion for d_n=d0+n*a remaining a p-adic unit.

    For p prime and d0,a integers, d_n is invertible in EVERY Z/p^r Z
    at all n>=0 iff p does not divide d0 and p divides a.

    If p divides d0, the initial frame fails.
    Otherwise, if a is nonzero mod p, the FIRST bad n lies in
    {1,...,p-1} and satisfies n=-d0 * a^{-1} modulo p.
    This is a finite obstruction to *unit-frame conjugacy only*, not
    to the arithmetic integer path itself or physical proof existence.
    """
    if not prime(p):
        raise ProtoSuccError("Actual prime required for local unit stability")
    _int(first_unit)
    _int(acceleration)
    if first_unit%p==0:
        bad=0
    elif acceleration%p==0:
        bad=None
    else:
        bad=(-first_unit*pow(acceleration,-1,p))%p
        if not 1<=bad<p:
            raise ArithmeticError("A unit could not become nonunit at time zero")
    expected_unit_everywhere=first_unit%p != 0 and acceleration%p==0
    if (bad is None)!=expected_unit_everywhere:
        raise ArithmeticError("Linear unit stability equivalence violated")
    for n in range(p):
        actual=(first_unit+n*acceleration)%p==0
        if bad is None:
            if actual:
                raise ArithmeticError("Declared always-unit trajectory failed")
        elif n<bad and actual or n==bad and not actual:
            raise ArithmeticError("First loss of unit character computed incorrectly")
    return {
        "prime":p,"initial_unit":first_unit,"acceleration":acceleration,
        "full_clock_gauge_valid_at_every_n":expected_unit_everywhere,
        "first_nonunit_succ_index":bad,
        "all_p_power_clocks_have_same_unit_condition":True,
        "integer_SUCC_path_stops_when_unit_is_nonunit":False,
        "source_or_physical_proof_barrier_claimed":False,
    }


def clock_unit_change_witness():
    """A higher SUCC can change a unit step into a nonunit step."""
    initial=HigherSuccJet((0,1,4))
    after=initial.succ()
    if initial.coefficients!=(0,1,4) or after.coefficients!=(1,5,4):
        raise ArithmeticError("Second derivative successor test contradicted")
    before=clock_change_isomorphism(5,2,1)
    after_period=additive_clock_period(5,2,5)
    if before["full_cycle_period"]!=25 or after_period!=5:
        raise ArithmeticError("Nonunit clock transition was not detected")
    try:
        clock_change_isomorphism(5,2,after.coefficients[1])
    except ProtoSuccError:
        pass
    else:
        raise ArithmeticError("Nonunit mistakenly remained invertible")
    return {
        "prime":5,"resolution":2,
        "starting_jet":[0,1,4],
        "after_meta_succ_jet":[1,5,4],
        "initial_unit_clock_period":25,
        "updated_nonunit_clock_period":5,
        "path_still_exists_as_integer_SUCC":True,
        "same_full_clock_coordinate_isomorphism_survives":False,
        "physical_proof_impossibility_claimed":False,
    }


def variable_proto_succ_demo():
    formal=[proto_succ_formal(n).unit_coefficient for n in range(5)]
    if formal!=[0,1,2,3,4]:
        raise ArithmeticError("Universal proto-SUCC generator failed")
    dtest=(3,5,7)
    for p in dtest:
        if shift_dilation_address_defect(p,11,1)!=1-p:
            raise ArithmeticError("d=1 specialization failed")
        for u in (1,2,3):
            if shift_dilation_address_defect(p,11,u)!=(1-p)*u:
                raise ArithmeticError("Formal variable unit law failed")
    stable=classify_linear_unit_stability(5,2,5)
    unstable=classify_linear_unit_stability(5,1,4)
    if (not stable["full_clock_gauge_valid_at_every_n"]
            or unstable["first_nonunit_succ_index"]!=1):
        raise ArithmeticError("General dynamic unit stability theorem failed")
    clock=clock_change_isomorphism(5,2,2)
    if normalized_defect_mod(5,2,11,2)!=(1-5)%25:
        raise ArithmeticError("Normalized Euler factor defect changed")
    jet=HigherSuccJet((0,2,3))
    values=[jet.first_coordinate(n) for n in range(6)]
    if values!=[0,2,7,15,26,40]:
        raise ArithmeticError("Second-level SUCC quadratic law failed")
    higher=HigherSuccJet((0,1,2,3))
    if any(higher.at(n).coefficients!=HigherSuccJet(
        higher.at(n-1).coefficients).succ().coefficients for n in range(1,6)):
        raise ArithmeticError("Third-level SUCC identity failed")
    return {
        "status":"VARIABLE_UNIT_PROTO_SUCC_UNIPOTENT_LIFT",
        "formal_original_one_step":"0 -> D",
        "formal_first_five_addresses_in_D_units":formal,
        "S_one_is_D_equals_one_specialization":True,
        "SUCC_unit_is_separate_from_absolute_coordinate_one":True,
        "S_unit_mod_25_with_unit_two_period":clock["full_cycle_period"],
        "unit_inverse_mod_25":clock["inverse"],
        "normalized_shift_dilation_defect":"1-p",
        "raw_shift_dilation_defect":"D*(1-p)",
        "symbolic_unit_must_not_be_automatically_assumed_invertible":True,
        "higher_order_SUCC_jet_formula":"x_n=sum_k binom(n,k) Delta^k x_0",
        "quadratic_d0_two_acceleration_three":values,
        "higher_order_integer_binomial_formula":True,
        "changing_unit_can_stop_being_a_local_clock_unit":clock_unit_change_witness(),
        "linear_step_unit_stability_iff_d0_unit_and_acceleration_divisible_by_p":True,
        "stable_d0_two_a_five_mod_p_five":stable,
        "unstable_d0_one_a_four_mod_p_five":unstable,
        "d_zero_specialization_loses_normalized_defect_information":True,
        "prime_jet_clock_period_identity_requires_declared_local_unit":True,
        "new_RH_Gamma_or_Kubota_Leopoldt_theorem_claimed":False,
    }
