"""Proof-carrying partial factorization trees and finite Scott/Kleene probes.

Standard-library-only; does NOT prove Goldbach. Scott-continuity claims are
paper arguments in SCOTT_PATH_RELATIVITY.md. Every arithmetic check is exact.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isqrt
from typing import Literal

Kind = Literal["unknown", "prime", "split"]


@dataclass(frozen=True)
class Trace:
    n: int
    kind: Kind = "unknown"
    left: "Trace | None" = None
    right: "Trace | None" = None

    def __post_init__(self):
        if self.n < 2:
            raise ValueError("this tree domain is for n>=2; 1 is the separate unit")
        if self.kind == "unknown":
            if self.left is not None or self.right is not None:
                raise ValueError("unknown node cannot have children")
        elif self.kind == "prime":
            if self.left is not None or self.right is not None or not trial_prime(self.n):
                raise ValueError("invalid prime certificate")
        elif self.kind == "split":
            if self.left is None or self.right is None or self.left.n * self.right.n != self.n:
                raise ValueError("invalid nontrivial factor split")
        else:
            raise ValueError("unknown trace kind")


def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def prime(n: int) -> Trace:
    return Trace(n, "prime")


def split(a: Trace, b: Trace) -> Trace:
    return Trace(a.n * b.n, "split", a, b)


def refines(old: Trace, new: Trace) -> bool:
    """Prefix-information order: new contains old evidence without alteration."""
    if old.n != new.n:
        return False
    if old.kind == "unknown":
        return True
    if old.kind != new.kind:
        return False
    if old.kind == "prime":
        return True
    return refines(old.left, new.left) and refines(old.right, new.right)


def factor_choice(n: int, policy: str = "minimum") -> tuple[int, int]:
    factors = [(d, n//d) for d in range(2, isqrt(n)+1) if n % d == 0]
    if not factors:
        raise ValueError("prime n has no proper factor pair")
    if policy == "minimum":
        return factors[0]
    if policy == "balanced":
        return factors[-1]
    if policy == "reverse":
        a, b = factors[0]
        return b, a
    raise ValueError("unknown choice policy")


def normalize(n: int, policy: str = "minimum") -> Trace:
    if trial_prime(n):
        return prime(n)
    a, b = factor_choice(n, policy)
    return split(normalize(a, policy), normalize(b, policy))


def refine_once(tree: Trace, policy: str = "minimum") -> Trace:
    """One atomic extension: prime leaf certification or nontrivial split."""
    if tree.kind == "prime":
        return tree
    if tree.kind == "unknown":
        if trial_prime(tree.n):
            return prime(tree.n)
        a, b = factor_choice(tree.n, policy)
        return split(Trace(a), Trace(b))
    new_left = refine_once(tree.left, policy)
    if new_left != tree.left:
        return split(new_left, tree.right)
    new_right = refine_once(tree.right, policy)
    return split(tree.left, new_right)


def trace_chain(n: int, policy: str = "minimum") -> tuple[Trace, ...]:
    current = Trace(n)
    history = [current]
    while True:
        nxt = refine_once(current, policy)
        if nxt == current:
            return tuple(history)
        assert refines(current, nxt)
        current = nxt
        history.append(current)


def bounds(tree: Trace) -> tuple[int, int]:
    """Sound Ω(n) interval: count each unresolved cofactor as [1, floor log2 n]."""
    if tree.kind == "prime":
        return (1, 1)
    if tree.kind == "unknown":
        return (1, tree.n.bit_length()-1)
    l1, u1 = bounds(tree.left)
    l2, u2 = bounds(tree.right)
    return l1+l2, u1+u2


def defect_bounds(tree: Trace) -> tuple[int, int]:
    l, u = bounds(tree)
    return l-1, u-1


def prime_transport(p: int, tree: Trace) -> Trace:
    """Certified multiplicative prime transport, including carried evidence."""
    return split(prime(p), tree)


def true_omega(n: int) -> int:
    result = 0
    k = 2
    while k*k <= n:
        while n % k == 0:
            n //= k
            result += 1
        k += 1
    return result + (1 if n > 1 else 0)


def split_count(tree: Trace) -> int:
    if tree.kind != "split":
        return 0
    return 1+split_count(tree.left)+split_count(tree.right)


def terminal(tree: Trace) -> bool:
    return tree.kind == "prime" or (tree.kind == "split" and terminal(tree.left) and terminal(tree.right))


def pair_bounds(left: Trace, right: Trace) -> tuple[int, int]:
    a,b = defect_bounds(left)
    c,d = defect_bounds(right)
    return a+c,b+d


def goldbach_interval(n: int, evidence: dict[int, Trace]) -> tuple[int, int]:
    """Under/over approximation to unordered Goldbach witness count at midpoint n.

    If an endpoint has no trace, it receives the bottom (unknown) trace.
    """
    lower, upper = 0, 0
    for d in range(n-1):
        left, right = n-d, n+d
        lo, hi = pair_bounds(evidence.get(left, Trace(left)), evidence.get(right, Trace(right)))
        lower += int(hi == 0)
        upper += int(lo == 0)
    return lower,upper


def kleene_step(facts: frozenset[tuple]) -> frozenset[tuple]:
    """Finitary Horn-step on global evidence. Arbitrary malformed inputs are
    not claimed sound; its least-fixed-point chain from empty is sound.
    """
    new = set(facts)
    new.add(("seen", 2))
    for fact in facts:
        op,n,*args = fact
        if op == "seen":
            new.add(("seen", n+1))
            new.add(("tested", n, 1))
        elif op == "tested":
            k = args[0]
            if k >= isqrt(n):
                new.add(("prime",n))
            elif n % (k+1) == 0:
                new.add(("composite",n,k+1))
            else:
                new.add(("tested",n,k+1))
    return frozenset(new)


def kleene_prefix(steps: int) -> frozenset[tuple]:
    x = frozenset()
    for _ in range(steps):
        x = kleene_step(x)
    return x


def report() -> dict:
    cases=[]
    for n in (9,10,12,60,97,101,997):
        paths = {p: trace_chain(n,p) for p in ("minimum","balanced")}
        cases.append({"n":n,"omega":true_omega(n),"paths":{
            p:{"rank_intervals":[list(bounds(t)) for t in c],"split_count":split_count(c[-1]),
               "stages":len(c)-1} for p,c in paths.items()}})
    eve={m:normalize(m) for m in range(2,21)}
    return {"status":"finite tested, Goldbach OPEN", "paths":cases,
            "midpoint10":{"bottom":goldbach_interval(10,{}),"complete":goldbach_interval(10,eve)},
            "chen_level_at_20":{"d1":list(pair_bounds(normalize(9),normalize(11))),
                                  "d3":list(pair_bounds(normalize(7),normalize(13)))}}


if __name__ == '__main__':
    import json
    print(json.dumps(report(),indent=2))