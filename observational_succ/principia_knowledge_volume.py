"""Exact finite source-relative knowledge volume (classical observability).

This analyzes a declared bank of possible action words, not a physically
executable adaptive policy on one disturbed carrier. No claims about RH.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Sequence


class InvalidLinearSource(ValueError):
    pass


def qmat(rows: Sequence[Sequence[int | Fraction]]) -> tuple[tuple[Fraction,...],...]:
    return tuple(tuple(Fraction(x) for x in row) for row in rows)


def rank(rows: Sequence[Sequence[int | Fraction]], dimension: int) -> int:
    if dimension < 1 or any(len(row) != dimension for row in rows):
        raise InvalidLinearSource('invalid row dimensions')
    a = [list(map(Fraction, row)) for row in rows]
    pivot = 0
    for col in range(dimension):
        pos = next((j for j in range(pivot, len(a)) if a[j][col]), None)
        if pos is None:
            continue
        a[pivot], a[pos] = a[pos], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [v/scale for v in a[pivot]]
        for j in range(len(a)):
            if j != pivot and a[j][col]:
                fac=a[j][col]
                a[j] = [v - fac*w for v,w in zip(a[j], a[pivot])]
        pivot += 1
    return pivot


def matmul(a: tuple[tuple[Fraction,...],...], b: tuple[tuple[Fraction,...],...]) -> tuple[tuple[Fraction,...],...]:
    if not a or not b or len(a[0]) != len(b):
        raise InvalidLinearSource('noncomposable linear maps')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),Fraction(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def identity(n:int) -> tuple[tuple[Fraction,...],...]:
    return tuple(tuple(Fraction(i==j) for j in range(n)) for i in range(n))


@dataclass(frozen=True)
class LinearSource:
    name: str
    dimension: int
    reports: tuple[tuple[Fraction,...],...]
    actions: tuple[tuple[str,tuple[tuple[Fraction,...],...]],...]


def make_source(reports:Sequence[Sequence[int | Fraction]], actions:dict[str,Sequence[Sequence[int | Fraction]]],
                *, source_name:str='finite-exact-linear-carrier') -> LinearSource:
    if not reports or not reports[0]:
        raise InvalidLinearSource('nonempty observable required')
    n=len(reports[0]); p=qmat(reports)
    if any(len(row)!=n for row in p):
        raise InvalidLinearSource('ragged reports')
    typed=tuple((name,qmat(a)) for name,a in sorted(actions.items()))
    if any(not name or len(a)!=n or any(len(r)!=n for r in a) for name,a in typed):
        raise InvalidLinearSource('non-square source actions')
    return LinearSource(source_name,n,p,typed)


@dataclass(frozen=True)
class KnowledgeVolume:
    source: str
    dimensions: tuple[int,...]
    independent_paths: tuple[tuple[str,...],...]
    report_rows: tuple[tuple[Fraction,...],...]


def analyze(source:LinearSource, max_depth:int) -> KnowledgeVolume:
    if source.name!='finite-exact-linear-carrier' or max_depth<0 or source.dimension<1:
        raise InvalidLinearSource('unlicensed source or search depth')
    # Verify the entire source passport; a forged LinearSource is not trusted.
    n=source.dimension
    if not source.reports or any(len(row)!=n for row in source.reports):
        raise InvalidLinearSource('bad source reports')
    if any(not label or len(a)!=n or any(len(row)!=n for row in a) for label,a in source.actions):
        raise InvalidLinearSource('bad action matrix')
    if len({label for label,_ in source.actions})!=len(source.actions):
        raise InvalidLinearSource('duplicate action label')
    bank=[]; distinguished=[];dims=[]
    alphabet=dict(source.actions)
    for length in range(max_depth+1):
        for word in product(alphabet.keys(),repeat=length):
            transition=identity(n)
            for label in word:
                transition=matmul(alphabet[label],transition)  # chronological path composition
            for row in matmul(source.reports,transition):
                if rank(bank+[row],n)>rank(bank,n):
                    distinguished.append(tuple(word))
                bank.append(row)
        dims.append(rank(bank,n))
    return KnowledgeVolume(source.name,tuple(dims),tuple(distinguished),tuple(bank))


def target_determined(volume:KnowledgeVolume, target:Sequence[int | Fraction]) -> bool:
    if volume.source!='finite-exact-linear-carrier' or not volume.report_rows:
        raise InvalidLinearSource('unrecognized knowledge evidence')
    n=len(volume.report_rows[0]); t=tuple(Fraction(v) for v in target)
    if len(t)!=n:
        raise InvalidLinearSource('target has wrong dimension')
    return rank(volume.report_rows+(t,),n)==rank(volume.report_rows,n)
