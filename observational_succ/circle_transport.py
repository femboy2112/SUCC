"""Exact finite-clock / real-circle torsion Pontryagin transport.

The genuine compact real Lie group R/Z contains the finite character groups
(Z/mZ)^ as rational torsion points k/m modulo 1. For m|n, finite clock
reduction goes n -> m, while the dual inclusion goes m -> n.

All phase equalities use rational classes modulo 1, not floating exp(2pi i t).
This is a finite part of harmonic-analysis duality, NOT the complete
Archimedean place, Gamma completion, or Weil-positive polarization.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd

from .core import BudgetExceeded, DomainError
from .yoneda import Arrow, FiniteFunctor


def mod1(q):
    x=Q(q)
    return x - (x.numerator // x.denominator)


@dataclass(frozen=True)
class FiniteClock:
    modulus: int

    def __post_init__(self):
        if type(self.modulus) is not int or not 2 <= self.modulus <= 10000:
            raise BudgetExceeded("Finite circle clock modulus must be in 2..10000")

    def mod(self, k):
        if type(k) is not int:
            raise DomainError("Clock index must be integral")
        return k % self.modulus

    def succ(self, k):
        return self.mod(k+1)

    def torsion(self, j):
        """Embed the character j as j/m in the real circle R/Z."""
        return mod1(Q(self.mod(j),self.modulus))

    def phase(self,k,j):
        """Exact phase class in R/Z for chi_j(k)=exp(2*pi*i*phase)."""
        return mod1(Q(self.mod(k)*self.mod(j),self.modulus))

    def order(self,j):
        return self.modulus // gcd(self.modulus,self.mod(j))


class CyclicOneObjectCategory:
    """One-object category B(Z/mZ), morphism composition = modular addition."""
    def __init__(self,modulus):
        self.clock=FiniteClock(modulus)
        self.objects=("*",)

    def identity(self,obj):
        if obj != "*":
            raise DomainError("Unknown cyclic groupoid object")
        return Arrow("*","*",(0,))

    def hom(self,a,b):
        if a!="*" or b!="*":
            raise DomainError("Unknown cyclic groupoid object")
        return tuple(Arrow("*","*",(k,)) for k in range(self.clock.modulus))

    def compose(self,left,right):
        if left not in self.hom("*","*") or right not in self.hom("*","*"):
            raise DomainError("Unknown cyclic group morphism")
        return Arrow("*","*",((left.word[0]+right.word[0])%self.clock.modulus,))


@dataclass(frozen=True)
class FiniteDualRefinement:
    m: int
    n: int

    def __post_init__(self):
        FiniteClock(self.m)
        FiniteClock(self.n)
        if self.n % self.m:
            raise DomainError("Finite quotient refinement requires m | n")

    def project(self,k):
        """Finite state projective direction: Z/n -> Z/m."""
        return FiniteClock(self.m).mod(k)

    def include_character(self,j):
        """Dual inductive direction: (Z/m)^ -> (Z/n)^."""
        return FiniteClock(self.n).mod((self.n//self.m)*FiniteClock(self.m).mod(j))

    def verify_phase(self,k,j):
        """chi_j(pi(k)) == chi_iota(j)(k), without computing exponentials."""
        source=FiniteClock(self.m).phase(self.project(k),j)
        target=FiniteClock(self.n).phase(k,self.include_character(j))
        return source == target

    def verify_exhaustive(self,max_cells=100000):
        if self.m*self.n>max_cells:
            raise BudgetExceeded("Finite duality verification grid exceeds interaction budget")
        for k in range(self.n):
            for j in range(self.m):
                if not self.verify_phase(k,j):
                    raise DomainError("Dual refinement is inconsistent")
        # Finite projection is surjective, dual inclusion is injective.
        if {self.project(k) for k in range(self.n)} != set(range(self.m)):
            raise DomainError("Primal projection is not surjective")
        if len({self.include_character(j) for j in range(self.m)}) != self.m:
            raise DomainError("Character inclusion is not injective")
        return {"m":self.m,"n":self.n,"phase_checks":self.m*self.n,
                "primal_direction":"projection n->m",
                "dual_direction":"inclusion m->n",
                "exact_circle":"R/Z rational torsion only",
                "status":"verified_finite"}

    def functors(self):
        """The two opposite-direction maps are honest cyclic-group functors."""
        if self.n > 64:
            raise BudgetExceeded("Exhaustive cyclic functor verification is bounded to n<=64")
        source= CyclicOneObjectCategory(self.n)
        target= CyclicOneObjectCategory(self.m)
        primal=FiniteFunctor(source,target,lambda _: "*",
            lambda arrow: Arrow("*","*",(self.project(arrow.word[0]),)))
        dualsrc=CyclicOneObjectCategory(self.m)
        dualtgt=CyclicOneObjectCategory(self.n)
        dual=FiniteFunctor(dualsrc,dualtgt,lambda _: "*",
            lambda arrow: Arrow("*","*",(self.include_character(arrow.word[0]),)))
        primal.verify()
        dual.verify()
        return primal,dual


def verify_refinement_tower(m,n,r,max_cells=100000):
    """Check the commuting finite inverse/dual direct towers, m|n|r."""
    a,b,c=FiniteDualRefinement(m,n),FiniteDualRefinement(n,r),FiniteDualRefinement(m,r)
    if r*m>max_cells:
        raise BudgetExceeded("Tower test would exceed finite resource budget")
    for k in range(r):
        if a.project(b.project(k)) != c.project(k):
            raise DomainError("Primal reduction tower is not coherent")
    for j in range(m):
        if b.include_character(a.include_character(j)) != c.include_character(j):
            raise DomainError("Dual inclusion tower is not coherent")
    return {"status":"verified_dual_tower","chain":[m,n,r],
            "primal_projective":True,"character_inductive":True}


def conductor_birth_2_to_6():
    """Calibrate the source's 2 -> 6 LCM clock refinement."""
    bridge=FiniteDualRefinement(2,6)
    bridge.verify_exhaustive()
    old={bridge.include_character(j) for j in range(2)}
    newest={j for j in range(6) if j not in old}
    by_conductor={}
    clock=FiniteClock(6)
    for j in sorted(newest):
        by_conductor.setdefault(clock.order(j),[]).append(j)
    assert by_conductor=={6:[1,5],3:[2,4]}
    return {"old_dual_indices":sorted(old),
            "new_dual_indices":sorted(newest),
            "new_exact_conductor_modes":by_conductor,
            "new_dimension":len(newest),
            "claim":"genuine finite-to-circle character bridge, not a Weil-sign theorem"}
