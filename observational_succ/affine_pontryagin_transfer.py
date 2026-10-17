"""Exact source-indexed SUCC/FUCC affine and Q/Z preimage transfer.

Pure rational finite-support algebra. The root-average endomorphism is the
classical arithmetic Bost--Connes rho_n, NOT an inverse source event and NOT
an analytic continuation or an RH positivity operator. No nontrivial zeros.

Source: Bost--Connes, Selecta Math. 1 (1995), 411--457; SUCC Pontryagin
atlas and finite affine presentation. All equalities here are finite algebra.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F


class TransferContractError(ValueError):
    """A source, arithmetic, or finite-computation contract was violated."""


def _rat(x):
    if type(x) not in (int, F):
        raise TransferContractError("exact integer/Fraction required (float and bool rejected)")
    return F(x)


def _posint(x, *, limit=256):
    if type(x) is not int or not 1 <= x <= limit:
        raise TransferContractError(f"positive exact integer <= {limit} required")
    return x


def _frame(source_id, epoch):
    if not isinstance(source_id, str) or not source_id.strip():
        raise TransferContractError("nonempty original source ID required")
    if type(epoch) is not int or epoch < 0:
        raise TransferContractError("nonnegative integer source epoch required")
    return source_id, epoch


def _prime(p):
    _posint(p)
    if p < 2 or any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
        raise TransferContractError("FUCC generator must be an actual prime")
    return p


@dataclass(frozen=True)
class RationalCharacterAlgebra:
    """Formal element of Q[Q/Z]: pairs (reduced frequency mod 1, coefficient).

    Terms are NOT complex-number sums. Multiplication is convolution on Q/Z.
    Source identity and epoch are checked on every binary operation.
    """
    terms: tuple[tuple[F, F], ...]
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self):
        _frame(self.source_id, self.epoch)
        normalized = {}
        for row in self.terms:
            if not isinstance(row, (tuple, list)) or len(row) != 2:
                raise TransferContractError("each term must be (rational phase, rational coefficient)")
            r, c = (_rat(row[0]) % 1), _rat(row[1])
            normalized[r] = normalized.get(r, F(0)) + c
        object.__setattr__(self, "terms", tuple(sorted((r, c) for r, c in normalized.items() if c)))

    @classmethod
    def basis(cls, frequency=F(0), source_id="Z-integer-modular-source", epoch=0):
        return cls(((frequency, F(1)),), source_id, epoch)

    @classmethod
    def zero(cls, source_id="Z-integer-modular-source", epoch=0):
        return cls((), source_id, epoch)

    def _check(self, other):
        if not isinstance(other, RationalCharacterAlgebra) or (self.source_id, self.epoch) != (other.source_id, other.epoch):
            raise TransferContractError("cannot glue different original source IDs or epochs")

    def add(self, other):
        self._check(other)
        return type(self)(self.terms + other.terms, self.source_id, self.epoch)

    def scale(self, scalar):
        a = _rat(scalar)
        return type(self)(tuple((r, a*c) for r, c in self.terms), self.source_id, self.epoch)

    def multiply(self, other):
        self._check(other)
        return type(self)(tuple(((r+s) % 1, c*d) for r,c in self.terms for s,d in other.terms), self.source_id, self.epoch)

    def sigma(self, n):
        """Classical dual multiplication sigma_n(e(r))=e(nr). Unital."""
        n = _posint(n)
        return type(self)(tuple(((n*r)%1,c) for r,c in self.terms), self.source_id, self.epoch)

    def rho(self, n):
        """Classical nonunital root average rho_n(e(r))=(1/n) sum_{ns=r}e(s)."""
        n = _posint(n)
        return type(self)(tuple((((r+k)/n) % 1, c/n) for r,c in self.terms for k in range(n)), self.source_id, self.epoch)

    def haar(self):
        """Normalized ADDITIVE Haar integral on Zhat, Fourier coefficient at r=0."""
        return next((c for r,c in self.terms if not r), F(0))

    def support(self):
        return tuple(r for r, _ in self.terms)


def exact_transfer_relations(r=F(1, 6), s=F(1, 10), n=2, m=3, *, source_id="Z-integer-modular-source", epoch=0):
    """Independent finite exact checks; not a proof of an infinite-dimensional completion."""
    e = RationalCharacterAlgebra.basis(r, source_id, epoch)
    f = RationalCharacterAlgebra.basis(s, source_id, epoch)
    unit = RationalCharacterAlgebra.basis(0, source_id, epoch)
    rn = unit.rho(n)
    return {
        "rho_multiplicative": e.multiply(f).rho(n) == e.rho(n).multiply(f.rho(n)),
        "rho_semigroup": e.rho(n).rho(m) == e.rho(m*n),
        "sigma_semigroup": e.sigma(n).sigma(m) == e.sigma(m*n),
        "sigma_left_inverse": e.rho(n).sigma(n) == e,
        "rho_sigma_projection": e.sigma(n).rho(n) == e.multiply(rn),
        "projector_idempotent": rn.multiply(rn) == rn,
        "projector_nonunital": rn != unit if n > 1 else rn == unit,
        "haar_adjoint_n": e.rho(n).multiply(f).haar() == e.multiply(f.sigma(n)).haar() / n,
        "source": (source_id, epoch),
        "full_bost_connes_Cstar_completed": False,
        "RH_proved": False,
    }


@dataclass(frozen=True)
class AffineSourceWord:
    """Chronologically ordered SUCC steps and genuine prime-FUCC steps.

    Step ('S',1) means x->x+1; ('V',p) means x->p*x.
    Two words may have equal endpoint maps while different causal transcripts.
    """
    steps: tuple[tuple[str, int], ...]
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self):
        _frame(self.source_id, self.epoch)
        normalized = []
        if not isinstance(self.steps, (tuple,list)):
            raise TransferContractError("finite chronological word required")
        for step in self.steps:
            if not isinstance(step, (tuple, list)) or len(step) != 2:
                raise TransferContractError("step must be ('S',1) or ('V',prime)")
            kind, k = step
            if kind == "S" and type(k) is int and k == 1:
                pass
            elif kind == "V":
                _prime(k)
            else:
                raise TransferContractError("unknown, composite or malformed source operation")
            normalized.append((kind, k))
        object.__setattr__(self, "steps", tuple(normalized))

    def normal_form(self):
        """Map n->a*n+b, with time order exactly as entered."""
        a,b=1,0
        for kind,k in self.steps:
            if kind == "S":
                b += 1
            else:
                a *= k
                b *= k
        return a,b

    def act(self, x):
        if type(x) is not int or x < 0:
            raise TransferContractError("N-carrier nonnegative exact integer required")
        a,b=self.normal_form()
        return a*x+b

    def dual_character(self, r):
        """e_r(a*x+b)=exp(2*pi*i*phase)*e_frequency(x). Exact phase in Q/Z."""
        r = _rat(r) % 1
        a,b=self.normal_form()
        return ((a*r)%1, (b*r)%1)

    def then(self, other):
        if not isinstance(other, AffineSourceWord) or (self.source_id,self.epoch)!=(other.source_id,other.epoch):
            raise TransferContractError("cannot compose histories from unrelated sources")
        return type(self)(self.steps+other.steps, self.source_id, self.epoch)


def history_loss_witness(p=2):
    """Equal affine endpoints but inequivalent time-labelled original event words."""
    _prime(p)
    left = AffineSourceWord((("S",1),("V",p)))
    right = AffineSourceWord((("V",p),) + (("S",1),)*p)
    assert left.normal_form() == right.normal_form() == (p,p)
    assert left.steps != right.steps
    return {
        "left_steps": left.steps, "right_steps": right.steps,
        "normal_form": left.normal_form(),
        "equal_affine_endpoints": True,
        "different_chronological_source_history": True,
        "endpoint_decoder_of_event_count_exists": False,
        "theorem_type": "coimage-factorization-obstruction",
        "physical_source_authentication": False,
    }


def verify_dual_word_composition(w1, w2, r):
    """Contravariant pullback with exact cyclotomic phase, no floating exp."""
    w = w1.then(w2)
    r = _rat(r)%1
    freq2,phase2=w2.dual_character(r)
    freq1,phase1=w1.dual_character(freq2)
    # w(x) = w2(w1(x)); phase from w2 plus pulled back w1.
    return w.dual_character(r)==(freq1, (phase1+phase2)%1)
