"""Finite cyclic observer: source-derived primitive indices and Haar clocks.

The infinite theorem uses the *full* profinite completion of a cyclic group,
not a finite cyclic experiment. Source indices are finite quotient cardinalities;
ordinary positive-integer arithmetic is a metatheoretic validation target.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from .prime_jet_genesis import JetSource, SourceError, counting_measure


@dataclass(frozen=True)
class CyclicObserver:
    modulus: int

    def __post_init__(self):
        if type(self.modulus) is not int or not 2 <= self.modulus <= 300:
            raise SourceError("finite cyclic observer requires 2<=modulus<=300")

    def subgroups(self):
        """Enumeration of actual additive subgroups of C_m, not a prime test."""
        m=self.modulus
        return tuple(sorted({frozenset((k*a)%m for k in range(m))
                             for a in range(m)},key=lambda s:(-len(s),tuple(sorted(s)))))

    def maximal_indices(self):
        """Indices of maximal proper subgroups, by strict subgroup inclusion."""
        m=self.modulus
        groups=self.subgroups()
        full=frozenset(range(m))
        candidates=[g for g in groups if g!=full]
        maximal=[g for g in candidates if not any(g < other for other in candidates)]
        indices=tuple(sorted(m//len(g) for g in maximal))
        if len(set(indices))!=len(indices):
            raise SourceError("non-distinct primitive quotient indices")
        return indices

    def subgroup_of_index(self,index):
        if type(index) is not int or index<=1 or self.modulus%index:
            raise SourceError("unavailable subgroup index")
        matching=[g for g in self.subgroups() if self.modulus//len(g)==index]
        if len(matching)!=1:
            raise SourceError("cyclic subgroup index is not unique")
        return matching[0]

    def haar_mass(self,index):
        """Normalized counting Haar: each coset of subgroup has equal mass."""
        return F(len(self.subgroup_of_index(index)),self.modulus)

    def primitive_jet_source(self,horizon):
        """Only source-observed maximal quotient species become FUCC jets."""
        indices=self.maximal_indices()
        return JetSource(tuple((f'quotient_index_{p}',F(p)) for p in indices),F(horizon))

    def certify_clock(self,index,observed_q):
        """An independent primitive must have e^lambda=1/haar_mass=index."""
        if index not in self.maximal_indices():
            raise SourceError("not a primitive maximal-open-subgroup species")
        if type(observed_q) not in (int,F) or F(observed_q)!=1/self.haar_mass(index):
            raise SourceError("incompatible finite-place Haar/index log clock")
        return True

    def reconstructed_atoms(self,horizon):
        return counting_measure(self.primitive_jet_source(horizon))
