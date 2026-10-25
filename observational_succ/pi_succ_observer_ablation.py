"""Exact finite factorial ablation of synchronized natural-carrier BBP observers.

Every feature is read from the same anchored rational trajectory.  The event
is a rigorously certified four-bit digit of pi/16 using the *fixed* BBP tail.
Train/test losses use exact Fractions, not a normality or asymptotic theorem.
No fitted example is used as its own validation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict

from .bbp_natural_carrier import exact_forcing, source_tail_enclosure
from .pascal_lucas_quotient import lucas_row_support

FAMILIES=("dyadic","pascal","lucas","odd-primary")


def _nat(n: int, lower: int=0) -> int:
    if type(n) is not int or n<lower:
        raise ValueError(f"integer >= {lower} required")
    return n


def dyadic_residue(x: Q, bits: int) -> int:
    _nat(bits,1)
    if type(x) is not Q or x.denominator%2==0:
        raise ValueError("exact 2-adic integral rational required")
    mod=1<<bits
    return x.numerator*pow(x.denominator,-1,mod)%mod


def certified_digit_at_n(n: int, phase: Q, max_terms: int=12) -> tuple[int,int]:
    """Exact source-first certificate. Return (digit,tail terms), or fail closed.

    A return with tail terms 0 uses 0<T_n<1/[(8n+1)(8n+2)]
    from the inherited genuine BBP positive kernel.  No numerical pi oracle.
    """
    _nat(n,1);_nat(max_terms,1)
    if type(phase) is not Q:raise ValueError("rational source phase required")
    y=phase%1
    upper=Q(1,(8*n+1)*(8*n+2))
    start=16*y
    a=start.numerator//start.denominator
    finish=start+16*upper
    b=finish.numerator//finish.denominator
    if a==b:return a%16,0
    for m in range(1,max_terms+1):
        lo,hi=source_tail_enclosure(n,m)
        a=(16*(y+lo));b=(16*(y+hi))
        if a.numerator//a.denominator==b.numerator//b.denominator:
            return a.numerator//a.denominator%16,m
    raise ArithmeticError("insufficient exact BBP tail terms to certify digit")


@dataclass(frozen=True)
class SourceObservation:
    n: int
    digit: int
    features: tuple[int,int,int,int]
    tail_terms: int

    @property
    def zero_gate(self) -> int:
        return int(self.digit==0)


def source_observations(first: int, last: int) -> tuple[SourceObservation,...]:
    """One chronological exact fraction machine, INCLUDING previous state."""
    _nat(first,1);_nat(last,first)
    y=Q(0)
    out=[]
    for n in range(1,last+1):
        before=y
        y=(16*y+exact_forcing(n))%1
        if n<first:continue
        digit,terms=certified_digit_at_n(n,y)
        # P: genuine 1-step backward Pascal row, actual source time n.
        # Q: 3/5 negative-valuation DEPTH, not the useless Boolean support.
        # The support flags are identically 1 by n=16: they carry no signal.
        p=(dyadic_residue(y-before,3))
        den=y.denominator
        d3=d5=0
        while den%3==0:
            den//=3;d3+=1
        while den%5==0:
            den//=5;d5+=1
        q=(d3%3)+3*(d5%3)
        d=dyadic_residue(y,2)
        lucas=lucas_row_support(2,n)%7
        out.append(SourceObservation(n,digit,(d,p,lucas,q),terms))
    return tuple(out)


def keys_for_subset(row: SourceObservation, subset: tuple[int,...]) -> tuple[int,...]:
    return tuple(row.features[i] for i in subset)


def train_exact_model(rows: tuple[SourceObservation,...], subset: tuple[int,...]) -> dict[tuple[int,...],tuple[int,int]]:
    if not rows:raise ValueError("nonempty training window required")
    counts=defaultdict(lambda:[0,0])
    for row in rows:
        c=counts[keys_for_subset(row,subset)]
        c[0]+=1;c[1]+=row.zero_gate
    return {k:tuple(v) for k,v in counts.items()}


def brier_error(test_rows: tuple[SourceObservation,...], model: dict[tuple[int,...],tuple[int,int]], subset: tuple[int,...]) -> Q:
    """Exact independent held-out squared error, fixed Beta(1,15) prior.

    Unknown heldout feature cells predict 1/16; includes no target leakage.
    """
    if not test_rows:raise ValueError("nonempty holdout required")
    err=Q(0)
    for row in test_rows:
        N,T=model.get(keys_for_subset(row,subset),(0,0))
        pred=Q(T+1,N+16)
        err+=(row.zero_gate-pred)**2
    return err/len(test_rows)


def complete_factorial(train: tuple[SourceObservation,...], test: tuple[SourceObservation,...]) -> dict[tuple[int,...],Q]:
    """Every one of the 2^4 factorial cells; no mixed term without all cells."""
    if not train or not test:raise ValueError("nonempty source windows required")
    table={}
    for n in range(5):
        for subset in combinations(range(4),n):
            table[subset]=brier_error(test,train_exact_model(train,subset),subset)
    assert len(table)==16
    return table


def full_four_way_interaction(table: dict[tuple[int,...],Q]) -> Q:
    if set(table)!={t for n in range(5) for t in combinations(range(4),n)}:
        raise ValueError("complete 16-cell factorial table required")
    return sum(((-1)**(4-len(s))*table[s] for s in table),Q())


def feature_mutation(rows: tuple[SourceObservation,...], index: int, step: int=1) -> tuple[SourceObservation,...]:
    """Deliberately wrong time alignment of one observer, retaining gate truth."""
    _nat(index);_nat(step,1)
    if index>=4 or not rows:raise ValueError("one of four source families required")
    return tuple(SourceObservation(row.n,row.digit,
        tuple((rows[(i+step)%len(rows)].features[index] if j==index else row.features[j])
             for j in range(4)),row.tail_terms)
        for i,row in enumerate(rows))
