"""Resource-bounded divisibility observers and symbolic prime-power witnesses.

The sharp separation theorem is elementary: the least integer divisor probe
separating two positive integers is a prime power at the first unequal
valuation. The target may be kept as a symbolic factorization of huge size.
No physical feasibility or global RH decidability is inferred.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import lcm

from .arithmetic import factorization, structure_birth
from .core import BudgetExceeded, DomainError


def _prime(p):
    return type(p) is int and 2 <= p <= 1_000_000 and factorization(p) == ((p, 1),)


@dataclass(frozen=True)
class ValuationWord:
    """A positive integer specified by its *verified* finite prime valuations.

    Exponents can be much larger than the number of digits in the observer's
    budget. Values need not be constructed as integers.
    """
    factors: tuple[tuple[int, int], ...]

    def __post_init__(self):
        factors = tuple(self.factors)
        if len(factors) > 2048:
            raise BudgetExceeded("Too many formal prime generators")
        if tuple(sorted(factors)) != factors or len(set(p for p, _ in factors)) != len(factors):
            raise DomainError("Prime valuation coordinates must be strictly ordered")
        for p, k in factors:
            if not _prime(p) or type(k) is not int or not 1 <= k <= 2048:
                raise DomainError("Expected prime p<=1e6 and positive exponent k<=2048")
        object.__setattr__(self, "factors", factors)

    @classmethod
    def from_integer(cls, n):
        if type(n) is not int or not 1 <= n <= 1_000_000:
            raise DomainError("Materialized integer adapter supports 1..1000000")
        return cls(factorization(n))

    def exponent(self, p):
        return dict(self.factors).get(p, 0)

    def multiply_prime(self, p, k=1):
        if not _prime(p) or type(k) is not int or k < 1:
            raise DomainError("Expected a genuine positive prime-power increment")
        a = dict(self.factors)
        a[p] = a.get(p, 0) + k
        return ValuationWord(tuple(sorted(a.items())))

    def divisible_by(self, n):
        """A concrete legal question: does j|target for 1<=j<=1e6?"""
        return all(self.exponent(p) >= k for p, k in factorization(n))

    def label(self):
        return "1" if not self.factors else " * ".join(f"{p}^{k}" for p, k in self.factors)

    def min_separating_prime_power(self, other):
        """Return (p,k,p**k). This can exceed any feasible physical budget."""
        if not isinstance(other, ValuationWord):
            raise DomainError("Both models require the same typed valuation interface")
        a,b = dict(self.factors),dict(other.factors)
        possibilities = []
        for p in set(a) | set(b):
            if a.get(p, 0) != b.get(p, 0):
                k = min(a.get(p, 0), b.get(p, 0)) + 1
                # At most 2049: finite for proof purposes, however astronomical.
                possibilities.append((p**k, p, k))
        if not possibilities:
            return None
        value,p,k = min(possibilities)
        return (p,k,value)


def lcm_word(n):
    """The LCM wavefront in prime-power normal form, without constructing L_n."""
    if type(n) is not int or not 1 <= n <= 10000:
        raise BudgetExceeded("LCM-horizon construction is bounded to 1..10000")
    if n == 1:
        return ValuationWord(())
    prime = bytearray(b"\x01")*(n+1)
    prime[0:2] = b"\x00\x00"
    p = 2
    while p*p <= n:
        if prime[p]:
            prime[p*p::p] = b"\x00"*len(prime[p*p::p])
        p += 1
    fs = []
    for p in range(2, n+1):
        if not prime[p]:
            continue
        k, power = 0, p
        while power <= n:
            k += 1
            power *= p
        fs.append((p,k))
    return ValuationWord(tuple(fs))


@dataclass(frozen=True)
class ProbeBudget:
    """A *declared* interaction horizon, not a claim of physical realizability."""
    max_probe_label: int
    max_materialized_queries: int = 10000

    def __post_init__(self):
        if type(self.max_probe_label) is not int or self.max_probe_label < 1 or self.max_probe_label.bit_length() > 2048:
            raise BudgetExceeded("Probe horizon must be a finite positive <=2048-bit integer")
        if type(self.max_materialized_queries) is not int or not 1 <= self.max_materialized_queries <= 100000:
            raise BudgetExceeded("Invalid materialization budget")


@dataclass(frozen=True)
class ProbeCertificate:
    horizon: int
    verdict: str
    witness: tuple[int, int] | None
    first_discriminating_value: int | None
    same_global_valuation: bool
    proof: str

    def data(self):
        return {"horizon": str(self.horizon), "verdict": self.verdict,
                "witness_prime_power": None if self.witness is None else
                    {"prime": self.witness[0], "exponent": self.witness[1]},
                "first_discriminating_value": None if self.first_discriminating_value is None else
                    str(self.first_discriminating_value),
                "same_global_valuation": self.same_global_valuation,
                "proof": self.proof,
                "epistemic_warning": "No detection within this finite probe budget is not proof of global equality, RH, or physical unobservability"}


def compare_observers(a: ValuationWord, b: ValuationWord, budget: ProbeBudget):
    """Exact certificate for Hom(j,a) vs Hom(j,b), all 1<=j<=budget.

    Deductive compression: tests a theorem about a finite family of probes,
    *not* an executed physical enumeration of every j in that horizon.
    """
    if not isinstance(a, ValuationWord) or not isinstance(b, ValuationWord):
        raise DomainError("Compare typed valuation words")
    missing = a.min_separating_prime_power(b)
    if missing is None:
        return ProbeCertificate(budget.max_probe_label, "same_valuation_word", None, None,
                                True, "Equal prime valuations, hence equal positive integers")
    p,k,first = missing
    if first <= budget.max_probe_label:
        return ProbeCertificate(budget.max_probe_label, "distinguished", (p,k), first,
                                False, f"The probe j={p}^{k} divides exactly one candidate")
    return ProbeCertificate(budget.max_probe_label, "indistinguishable_within_budget", None,
                            first, False, f"Every probe j<=B has valuations below both candidates' first unequal prime-power threshold ({p}^{k})")


def execute_probe(a, b, j, budget: ProbeBudget):
    """An *actual* legal divisibility query; returns finite evidence only."""
    if type(j) is not int or not 1 <= j <= budget.max_probe_label or j > 1_000_000:
        raise BudgetExceeded("Concrete query is outside the observer's finite executable budget")
    if not isinstance(a, ValuationWord) or not isinstance(b, ValuationWord):
        raise DomainError("Malformed global targets")
    v1,v2 = a.divisible_by(j),b.divisible_by(j)
    return {"query": j, "a": v1, "b": v2, "distinguishes": v1 != v2}


def sample_signature(word, budget: ProbeBudget):
    """Literal finite Yoneda signature, refusing accidental unbounded scans."""
    if budget.max_probe_label > budget.max_materialized_queries:
        raise BudgetExceeded("A full signature requires more queries than the declared execution allowance")
    if budget.max_probe_label > 1_000_000:
        raise BudgetExceeded("Concrete integer probes above 1e6 are unavailable")
    return tuple(int(word.divisible_by(j)) for j in range(1, budget.max_probe_label+1))


def budget_demo():
    """A 10^4 horizon, with target representations not materialized as integers."""
    B=10000
    current = lcm_word(B)
    other = current.multiply_prime(2)
    cert = compare_observers(current,other,ProbeBudget(B))
    p,k,t = current.min_separating_prime_power(other)
    assert cert.verdict == "indistinguishable_within_budget" and t>B
    return {"B":B, "formal_target_factors":len(current.factors),
            "witness_prime_power":f"{p}^{k}",
            "first_discrimination":t,"finite_verdict":cert.verdict,
            "source_only":"No zeta zeros or global sign input"}
