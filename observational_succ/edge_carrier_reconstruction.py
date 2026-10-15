"""Source-indexed carrier reconstruction from categorical edge presentations.

Theorems are classical: free one-loop category; group completion N -> Z;
ring localization Z -> Q; gaussian ring Z[i]; inverse limit of all Z/nZ
is the profinite ring Z-hat. Exact finite implementations here represent
specific FINITELY DESCRIBED elements and canonical maps, not the entirety
of the inverse limit or physically performed infinite observations.

IMPORTANT: a directed RAY 0->1->2->... inverted as a path groupoid does
NOT give Z as its based automorphism group (the graph is a tree).
The 1-VERTEX 1-LOOP category with endomorphism monoid N *does*.
No RH, full adelic completion, or physical source attestation is proved.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, lcm


class EdgeCarrierError(ValueError):
    """Invalid source law, arrow, localization, probe or unfounded equivalence."""


def nat(n: int) -> int:
    if type(n) is not int or n < 0:
        raise EdgeCarrierError("An exact nonnegative successor count is required")
    return n


def integer(n: int) -> int:
    if type(n) is not int:
        raise EdgeCarrierError("An exact integer edge count is required")
    return n


def prime(p: int) -> bool:
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def atlas(primes: tuple[int, ...]) -> tuple[int, ...]:
    if type(primes) is not tuple or tuple(sorted(set(primes))) != primes or any(not prime(p) for p in primes):
        raise EdgeCarrierError("Prime atlas must be sorted genuine distinct primes")
    return primes


def source_token(label: str) -> str:
    if type(label) is not str or not label.strip():
        raise EdgeCarrierError("Source identity must be a nonempty declared string")
    return label


@dataclass(frozen=True)
class NatLoop:
    """s^n in the free category on one object * and one loop s."""
    count: int

    def __post_init__(self) -> None:
        nat(self.count)

    def then(self, next_loop: "NatLoop") -> "NatLoop":
        if not isinstance(next_loop, NatLoop):
            raise EdgeCarrierError("Cannot compose an unknown source generator")
        return NatLoop(self.count + next_loop.count)

    def group_complete(self) -> "IntegerLoop":
        return IntegerLoop(self.count, 0)


@dataclass(frozen=True)
class IntegerLoop:
    """Formal signed path s^forward * (s^-1)^backward, *before quotient*.

    Equality in the group completion is NOT dataclass tuple equality.
    The canonical group-completion equality is forward+other.backward =
    backward+other.forward.
    """
    forward: int
    backward: int = 0

    def __post_init__(self) -> None:
        nat(self.forward)
        nat(self.backward)

    @property
    def winding(self) -> int:
        return self.forward - self.backward

    @classmethod
    def from_winding(cls, n: int) -> "IntegerLoop":
        n = integer(n)
        return cls(max(n, 0), max(-n, 0))

    def equivalent(self, other: "IntegerLoop") -> bool:
        if not isinstance(other, IntegerLoop):
            raise EdgeCarrierError("Equivalence requires two signed paths")
        return self.forward + other.backward == self.backward + other.forward

    def canonical(self) -> "IntegerLoop":
        return IntegerLoop.from_winding(self.winding)

    def then(self, other: "IntegerLoop") -> "IntegerLoop":
        if not isinstance(other, IntegerLoop):
            raise EdgeCarrierError("Compose only declared arrows")
        return IntegerLoop(self.forward + other.forward, self.backward + other.backward)

    def inverse(self) -> "IntegerLoop":
        return IntegerLoop(self.backward, self.forward)

    def transport(self, base_coordinate: int = 0) -> int:
        """Choose one basepoint of a Z-torsor: action is free/transitive."""
        return integer(base_coordinate) + self.winding

    def cyclic_target(self, modulus: int, generator_image: int) -> int:
        """Unique group extension of the N-loop's cyclic target homomorphism.

        A monoid map N -> Z/m is determined by the generator's image g.
        Its unique extension along N->Z sends winding k to k*g modulo m.
        """
        if type(modulus) is not int or modulus < 2:
            raise EdgeCarrierError("Finite cyclic target modulus >=2")
        return self.winding * integer(generator_image) % modulus


@dataclass(frozen=True)
class RayPath:
    """Free path groupoid completion of a RAY, not the one-loop category."""
    start: int
    signed_steps: tuple[int, ...]

    def __post_init__(self) -> None:
        nat(self.start)
        if type(self.signed_steps) is not tuple or any(type(x) is not int or x not in (-1, 1) for x in self.signed_steps):
            raise EdgeCarrierError("A ray uses individually typed ±1 edges")
        pos = self.start
        for step in self.signed_steps:
            pos += step
            if pos < 0:
                raise EdgeCarrierError("A ray cannot traverse a nonexistent negative vertex")

    @property
    def end(self) -> int:
        return self.start + sum(self.signed_steps)

    def thin_groupoid_arrow(self) -> tuple[int, int]:
        """In a tree every reduced path is determined by its endpoints."""
        return self.start, self.end

    @property
    def nontrivial_based_loop_after_reduction(self) -> bool:
        # Any walk in a tree with equal endpoints reduces to the empty word.
        return False

    def then(self, other: "RayPath") -> "RayPath":
        if not isinstance(other, RayPath) or self.end != other.start:
            raise EdgeCarrierError("Only compose adjacent actual ray histories")
        return RayPath(self.start, self.signed_steps + other.signed_steps)


@dataclass(frozen=True)
class RationalSpan:
    """Ring localization of Z at all nonzero integer scalars.

    Canonical pair (n,d), d>0 and gcd(|n|,d)=1. Its genuine target is Q.
    Numerator may be constructed from a group-completed successor loop.
    """
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        n, d = integer(self.numerator), integer(self.denominator)
        if d == 0:
            raise EdgeCarrierError("Localization cannot invert the zero arrow")
        if d < 0:
            n, d = -n, -d
        k = gcd(abs(n), d)
        object.__setattr__(self, "numerator", n // k)
        object.__setattr__(self, "denominator", d // k)

    @classmethod
    def from_edges(cls, numerator: IntegerLoop, denominator: NatLoop) -> "RationalSpan":
        if not isinstance(numerator, IntegerLoop) or not isinstance(denominator, NatLoop):
            raise EdgeCarrierError("Need integer group-arrow and positive natural denominator")
        return cls(numerator.winding, denominator.count)

    def as_fraction(self) -> Fraction:
        """External mathematical comparison oracle, not the representation."""
        return Fraction(self.numerator, self.denominator)

    def add(self, other: "RationalSpan") -> "RationalSpan":
        if not isinstance(other, RationalSpan):
            raise EdgeCarrierError("Cannot add an untyped rational arrow")
        return RationalSpan(self.numerator * other.denominator +
                            other.numerator * self.denominator,
                            self.denominator * other.denominator)

    def multiply(self, other: "RationalSpan") -> "RationalSpan":
        if not isinstance(other, RationalSpan):
            raise EdgeCarrierError("Cannot multiply an untyped rational arrow")
        return RationalSpan(self.numerator * other.numerator,
                            self.denominator * other.denominator)

    def negative(self) -> "RationalSpan":
        return RationalSpan(-self.numerator, self.denominator)

    def inverse(self) -> "RationalSpan":
        if self.numerator == 0:
            raise EdgeCarrierError("Zero has no inverse in the fraction field")
        return RationalSpan(self.denominator, self.numerator)

    def subtract(self, other: "RationalSpan") -> "RationalSpan":
        return self.add(other.negative())

    def divide(self, other: "RationalSpan") -> "RationalSpan":
        return self.multiply(other.inverse())


@dataclass(frozen=True)
class SLocalization:
    """Stage Z[S^-1]; only denominators from declared genuine primes S."""
    primes: tuple[int, ...]
    source_id: str = "Q-integer-lattice"
    epoch: int = 0

    def __post_init__(self) -> None:
        atlas(self.primes)
        source_token(self.source_id)
        if type(self.epoch) is not int or self.epoch < 0:
            raise EdgeCarrierError("Source epoch must be nonnegative")

    def contains(self, x: RationalSpan) -> bool:
        if not isinstance(x, RationalSpan):
            raise EdgeCarrierError("Only test canonical rational arrows")
        rest = x.denominator
        for p in self.primes:
            while rest % p == 0:
                rest //= p
        return rest == 1

    def admit(self, x: RationalSpan) -> RationalSpan:
        if not self.contains(x):
            raise EdgeCarrierError("Unobserved/inverted prime needed for denominator")
        return x

    def extend(self, new_prime: int) -> "SLocalization":
        if not prime(new_prime) or new_prime in self.primes:
            raise EdgeCarrierError("Prime extension must be genuine and new")
        return SLocalization(tuple(sorted(self.primes + (new_prime,))),
                             self.source_id, self.epoch)

    def inclusion_preserves(self, x: RationalSpan, other: "SLocalization") -> bool:
        if (not isinstance(other, SLocalization) or
            (self.source_id, self.epoch) != (other.source_id, other.epoch) or
            not set(self.primes).issubset(other.primes)):
            raise EdgeCarrierError("Only lawful same-source increasing atlases")
        if self.contains(x) and not other.contains(x):
            raise AssertionError("Localization transition lost a source element")
        return True


@dataclass(frozen=True)
class GaussianInteger:
    """Z[X]/(X^2+1) = Z[i], encoded in the constructed Z x Z."""
    real: IntegerLoop
    imag: IntegerLoop

    def __post_init__(self) -> None:
        if not isinstance(self.real, IntegerLoop) or not isinstance(self.imag, IntegerLoop):
            raise EdgeCarrierError("Gaussian coordinates require completed integers")
        # Unlike the historical raw IntegerLoop event presentation, Z[i] is
        # a QUOTIENT RING: equal group-completion arrows must have one
        # canonical object-level representation.
        object.__setattr__(self, "real", self.real.canonical())
        object.__setattr__(self, "imag", self.imag.canonical())

    @classmethod
    def from_pair(cls, a: int, b: int) -> "GaussianInteger":
        return cls(IntegerLoop.from_winding(a), IntegerLoop.from_winding(b))

    @property
    def pair(self) -> tuple[int, int]:
        return self.real.winding, self.imag.winding

    def add(self, other: "GaussianInteger") -> "GaussianInteger":
        if not isinstance(other, GaussianInteger):
            raise EdgeCarrierError("Gaussian ring requires correctly typed input")
        a, b = self.pair
        c, d = other.pair
        return GaussianInteger.from_pair(a+c, b+d)

    def multiply(self, other: "GaussianInteger") -> "GaussianInteger":
        if not isinstance(other, GaussianInteger):
            raise EdgeCarrierError("Gaussian ring requires correctly typed input")
        a, b = self.pair
        c, d = other.pair
        return GaussianInteger.from_pair(a*c-b*d, a*d+b*c)

    def conjugate(self) -> "GaussianInteger":
        a, b = self.pair
        return GaussianInteger.from_pair(a, -b)

    def norm(self) -> int:
        a, b = self.pair
        return a*a + b*b


@dataclass(frozen=True)
class GaussianRational:
    """Localization Q[i] with exact Q-coordinate ring, NOT the full C."""
    real: RationalSpan
    imag: RationalSpan

    def __post_init__(self) -> None:
        if not isinstance(self.real, RationalSpan) or not isinstance(self.imag, RationalSpan):
            raise EdgeCarrierError("Only rational coordinates define Q(i)")

    @classmethod
    def from_gaussian(cls, z: GaussianInteger) -> "GaussianRational":
        a, b = z.pair
        return cls(RationalSpan(a), RationalSpan(b))

    def multiply(self, other: "GaussianRational") -> "GaussianRational":
        if not isinstance(other, GaussianRational):
            raise EdgeCarrierError("Require a Q(i) multiplier")
        a,b,c,d = self.real,self.imag,other.real,other.imag
        return GaussianRational(a.multiply(c).subtract(b.multiply(d)),
                                a.multiply(d).add(b.multiply(c)))

    def inverse(self) -> "GaussianRational":
        a,b = self.real,self.imag
        denominator = a.multiply(a).add(b.multiply(b))
        if denominator.numerator == 0:
            raise EdgeCarrierError("0 has no field inverse")
        return GaussianRational(a.divide(denominator), b.negative().divide(denominator))

    def as_pair(self) -> tuple[Fraction, Fraction]:
        return self.real.as_fraction(), self.imag.as_fraction()


@dataclass(frozen=True)
class ProfiniteProgram:
    """Finite syntax for selected points of lim_(n|m) Z/nZ = Z-hat.

    The complete inverse limit has uncountably many points; its *finite
    source programs* form only a subclass. Every query residue(n) halts.
    Ring operations act pointwise at each finite clock.
    """
    kind: str
    seed: int = 0
    left: "ProfiniteProgram | None" = None
    right: "ProfiniteProgram | None" = None
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self) -> None:
        if self.kind not in ("integer", "prime_projector", "sum", "product"):
            raise EdgeCarrierError("Unknown finite global program constructor")
        source_token(self.source_id)
        if type(self.epoch) is not int or self.epoch < 0:
            raise EdgeCarrierError("Invalid original source epoch")
        if self.kind in ("integer","prime_projector"):
            if self.left is not None or self.right is not None:
                raise EdgeCarrierError("Atomic carrier program cannot hold child expressions")
            if type(self.seed) is not int or (self.kind == "prime_projector" and not prime(self.seed)):
                raise EdgeCarrierError("Atomic integer or authentic prime label required")
        else:
            if (type(self.seed) is not int or self.seed != 0 or
                not isinstance(self.left, ProfiniteProgram) or
                not isinstance(self.right, ProfiniteProgram) or
                (self.left.source_id,self.left.epoch) != (self.source_id,self.epoch) or
                (self.right.source_id,self.right.epoch) != (self.source_id,self.epoch)):
                raise EdgeCarrierError("Composition needs same source, epoch and two valid children")

    @staticmethod
    def integer(n: int, *, source_id: str = "Z-integer-modular-source",
                epoch: int = 0) -> "ProfiniteProgram":
        return ProfiniteProgram("integer", integer(n), source_id=source_id, epoch=epoch)

    @staticmethod
    def projector(p: int, *, source_id: str = "Z-integer-modular-source",
                  epoch: int = 0) -> "ProfiniteProgram":
        if not prime(p):
            raise EdgeCarrierError("A projector requires a real rational prime")
        return ProfiniteProgram("prime_projector", p, source_id=source_id, epoch=epoch)

    def _combine(self, other: "ProfiniteProgram", kind: str) -> "ProfiniteProgram":
        if not isinstance(other, ProfiniteProgram) or (
            self.source_id,self.epoch) != (other.source_id,other.epoch):
            raise EdgeCarrierError("Cannot glue unrelated source programs")
        return ProfiniteProgram(kind, 0, self, other, self.source_id, self.epoch)

    def add(self, other: "ProfiniteProgram") -> "ProfiniteProgram":
        return self._combine(other,"sum")

    def multiply(self, other: "ProfiniteProgram") -> "ProfiniteProgram":
        return self._combine(other,"product")

    def residue(self, n: int) -> int:
        if type(n) is not int or n < 1 or n > 2_000_000:
            raise EdgeCarrierError("One positive bounded finite clock modulus required")
        if self.kind == "integer":
            return self.seed % n
        if self.kind == "prime_projector":
            p = self.seed
            if n == 1 or n % p:
                return 0
            part = n
            while part % p == 0:
                part //= p
            power = n // part
            # x = 1 mod p^v_p(n), x=0 mod (n/p^v_p(n)).
            # CRT gives x=part * inverse(part mod power) modulo n.
            return (part * pow(part, -1, power)) % n
        if self.kind == "sum":
            return (self.left.residue(n) + self.right.residue(n)) % n
        return (self.left.residue(n) * self.right.residue(n)) % n

    def bonding(self, big: int, small: int) -> dict:
        if (type(big) is not int or type(small) is not int or
            big < 1 or small < 1 or big % small):
            raise EdgeCarrierError("Reduction arrow Z/big -> Z/small requires small | big")
        a = self.residue(big)
        b = self.residue(small)
        if a % small != b:
            raise AssertionError("Source program failed genuine inverse-system bonding")
        return {
            "source": self.source_id, "epoch": self.epoch,
            "larger_modulus": big, "smaller_modulus": small,
            "larger_residue": a, "smaller_residue": b,
            "ring_bonding_compatible": True,
            "global_object_is_finitely_described": True,
            "all_points_of_Zhat_finitely_described": False,
            "physically_executed_infinite_limit": False,
        }


def finite_clock_collision(horizon: int) -> dict:
    """0 and L=lcm(1,...,H) indistinguishable on ALL moduli n<=H."""
    if type(horizon) is not int or not 1 <= horizon <= 60:
        raise EdgeCarrierError("Positive bounded observation horizon required")
    L=1
    for n in range(1,horizon+1):
        L=lcm(L,n)
    if not all(L%n==0 for n in range(1,horizon+1)):
        raise AssertionError("Finite modular alias not genuinely observed")
    return {
        "horizon": horizon, "distinct_source_integers": (0,L),
        "all_declared_finite_modular_probes_match": True,
        "first_refuting_modulus": L+1,
        "global_Zhat_points_equal": False,
        "all_finite_probes_can_be_executed_at_once": False,
    }


def prime_projector_is_not_integer(p: int) -> dict:
    """Mathematical proof of a proper Z -> Z-hat embedding.

    e_p at all q!=p prime-power clocks is zero; at p clock equals one.
    If e_p were the diagonal image of integer a, divisibility by arbitrary
    powers q^k forces a=0, contradicting a mod p=1.
    """
    e=ProfiniteProgram.projector(p)
    witness_q=3 if p==2 else 2
    vals={n:e.residue(n) for n in (p, witness_q,witness_q**2,p*witness_q)}
    if vals[p]!=1%p or any(e.residue(witness_q**k) for k in range(1,6)):
        raise AssertionError("False noninteger projector signature")
    if any(e.residue(n)**2 % n != e.residue(n) for n in vals):
        raise AssertionError("Local idempotent failed")
    return {
        "prime": p, "witness_prime": witness_q,
        "finite_residue_examples": vals,
        "idempotent_at_every_clock": "CLASSICAL_CRT_PROOF",
        "nontrivial": True,
        "in_diagonal_Z": False,
        "reason": "all q^k divisibility implies source integer 0, but residue mod p=1",
        "full_inverse_limit_exists": "CLASSICAL_DEFINITION/COMPACTNESS",
        "full_Zhat_reconstructed_by_finitely_many_samples": False,
        "RH_proved": False,
    }


def carrier_interface_contract() -> tuple[dict,...]:
    """Typed mathematical equivalences versus proper embeddings/limits."""
    return (
        {
            "small": "free one-vertex successor loop category B(N)",
            "large": "one-vertex groupoid B(Z)",
            "kind": "GROUP_COMPLETION_ISOMORPHISM_ON_HOM",
            "invariant": "identity, composition, inverses; based torsor",
            "new_operation": "formally invert the generating loop",
            "source_loss": False,
            "not_equal_vertex_carriers": True,
        },
        {
            "small": "completed integer ring Z plus inversion contracts",
            "large": "fraction field Q",
            "kind": "LOCALIZATION_RING_ISOMORPHISM",
            "invariant": "0,1,+,*,inverses of nonzero integers",
            "new_operation": "adjoin inverses to every nonzero integer",
            "source_loss": False,
        },
        {
            "small": "two copies of integer group + relation i^2=-1",
            "large": "Gaussian integer ring Z[i]",
            "kind": "PRESENTATION_RING_ISOMORPHISM",
            "invariant": "complex multiplication, conjugation, norm",
            "new_operation": "add imaginary generator with polynomial relation",
            "source_loss": False,
        },
        {
            "small": "finite rings Z/nZ with divisibility reduction arrows",
            "large": "profinite ring Z-hat",
            "kind": "INVERSE_LIMIT_ISOMORPHISM_BY_DEFINITION",
            "invariant": "all compatible residues +,+* and topology",
            "new_operation": "inverse-limit completion, not an executed omega-step",
            "source_loss": False,
            "Z_to_Zhat": "proper dense embedding, NOT ring isomorphism",
            "all_global_points_have_finite_code": False,
        },
        {
            "small": "all Cauchy sequences in Q(i) modulo null sequences",
            "large": "C",
            "kind": "METRIC_COMPLETION_FIELD_ISOMORPHISM_CLASSICAL",
            "invariant": "field operations, complex norm and complete topology",
            "source_embedding": "Q(i) is a proper dense subfield",
            "all_global_points_have_finite_code": False,
        },
        {
            "small": "Zhat with nonzero integer multipliers formally inverted",
            "large": "A_f(Q), restricted product of (Q_p,Z_p)",
            "kind": "LOCALIZATION_ADELIC_RING_ISOMORPHISM_CLASSICAL",
            "invariant": "ring operations, Haar-compatible restricted product topology",
            "source_embedding": "Zhat is a proper compact open subring",
            "all_global_points_have_finite_code": False,
        },
        {
            "small": "R with the full finite adele ring A_f(Q)",
            "large": "A_Q",
            "kind": "REAL_FINITE_PLACE_PRODUCT_CARRIER_ISOMORPHISM_CLASSICAL",
            "invariant": "true Archimedean topology, restricted finite places",
            "rational_real_chart_is_full_real_carrier": False,
        },
        {
            "small": "Q(i) Gaussian rational field before completion",
            "large": "C",
            "kind": "NOT_YET_EQUIVALENT_UNCOMPLETED",
            "missing": "Cauchy completion / topology and noncomputable points",
            "source_loss": "unverified if completion/source maps underspecified",
        },
    )



def finite_prime_partition(n: int) -> dict:
    """True CRT primitive idempotents partition unity at every finite stage.

    At n=product p^v_p(n), e_p=1 mod p^v_p(n) and 0 at all other
    prime powers; therefore sum_(p|n)e_p=1 and e_p e_q=0 for p!=q.
    Passing to all n yields Zhat ~= product_p Zp as rings, CLASSICAL CRT.
    """
    if type(n) is not int or not 1 <= n <= 2_000_000:
        raise EdgeCarrierError("A finite positive modulus <=2,000,000 required")
    residue=n
    primes=[]
    d=2
    while d*d<=residue:
        if residue%d==0:
            primes.append(d)
            while residue%d==0:
                residue//=d
        d+=1
    if residue>1:primes.append(residue)
    e={p:ProfiniteProgram.projector(p).residue(n) for p in primes}
    pairwise={ f'{p}:{q}': (e[p]*e[q])%n
               for i,p in enumerate(primes) for q in primes[i+1:] }
    if (sum(e.values())%n != (1%n)
        or any(x for x in pairwise.values())
        or any(v*v%n!=v for v in e.values())):
        raise AssertionError("CRT idempotent partition failed genuine source modulus")
    return {
        "modulus": n, "prime_places": tuple(primes),
        "idempotent_residues": e, "pairwise_products": pairwise,
        "sum_modulus": sum(e.values())%n,
        "identity_modulus": 1%n,
        "ring_partition_certified_at_finite_stage": True,
        "all_places_topological_completion": "CLASSICAL_CRT_THEOREM",
        "all_primes_computed_in_this_finite_stage": False,
        "RH_proved": False,
    }



def finite_cyclic_yoneda(modulus: int) -> dict:
    """Exact finite Yoneda calibration on the one-object group B(Z/m).

    Its representable presheaf is the regular Z/m-set. Naturality
    f(x+a)=f(x)+a forces f(x)=x+k, k=f(0), and there are exactly
    m such natural self-transformations, one for every edge k.

    Brute enumeration of all m^m endofunctions is an INDEPENDENT
    finite control, not a proof of general Yoneda from samples.
    """
    from itertools import product
    if type(modulus) is not int or not 1 <= modulus <= 6:
        raise EdgeCarrierError("Exact finite Yoneda calibration modulus 1..6")
    n=modulus
    natural=[]
    for tup in product(range(n),repeat=n):
        if all(tup[(x+a)%n] == (tup[x]+a)%n
               for x in range(n) for a in range(n)):
            natural.append(tup)
    target=tuple(tuple((x+k)%n for x in range(n)) for k in range(n))
    if tuple(sorted(natural)) != tuple(sorted(target)):
        raise AssertionError("Representable Yoneda edge carrier failed full enumeration")
    return {
        "modulus":n,"candidate_endofunctions":n**n,
        "naturality_constrained_endofunctions":len(natural),
        "recovered_cyclic_edges":n,
        "all_and_only_right_translations":True,
        "natural_transformation_to_arrow_bijection":True,
        "yoneda_full_faithfulness_generalized_by_samples":False,
        "RH_proved":False,
    }
