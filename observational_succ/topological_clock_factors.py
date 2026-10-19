"""Exact finite diagnostics for continuous cyclic-factor source obstructions.

Global compact-Hausdorff factor theorems are paper proofs, not extrapolations of
sampled orbit points. A nonrepeating orbit need not admit any CONTINUOUS
C_m factor, and a source with Zhat as factor need not be isomorphic to Zhat.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from .orbit_clock_genesis import ClockSourceError, _nat


@dataclass(frozen=True)
class RationalContraction:
    """On [0,1], T(x)=(1+x)/2, root 0; x_n=1-2**(-n)."""
    def state(self, n:int) -> Fraction:
        _nat(n,"orbit index",minimum=0,maximum=100000)
        return Fraction(1)-Fraction(1,2**n)

    def successor(self, value:Fraction) -> Fraction:
        if type(value) not in (int,Fraction) or not 0<=value<=1:
            raise ClockSourceError("a rational point in the unit interval is required")
        return (Fraction(1)+Fraction(value))/2

    def close_different_clock_residues(self, modulus:int, tolerance:Fraction) -> dict:
        """Finite exact witness of distinct mod-m residues arbitrarily close near 1.

        The general impossibility theorem follows analytically from convergence
        to the fixed point 1 and continuity; a finite pair is ONLY a control.
        """
        _nat(modulus,"clock modulus",minimum=2,maximum=10000)
        if type(tolerance) not in (int,Fraction) or not 0<Fraction(tolerance)<=1:
            raise ClockSourceError("strictly positive exact rational tolerance required")
        tolerance=Fraction(tolerance)
        n=0
        while Fraction(1,2**(n+1))>=tolerance:
            n+=1
            if n>100000:
                raise ClockSourceError("precision source budget exhausted")
        x,y=self.state(n),self.state(n+1)
        return {"n":n,"next":n+1,"x":str(x),"y":str(y),
                "gap":str(y-x),"tolerance":str(tolerance),
                "clock_residues":(n%modulus,(n+1)%modulus),
                "distinct_residues":n%modulus !=(n+1)%modulus,
                "gap_strictly_below_tolerance": y-x<tolerance,
                "global_continuity_conclusion_is_paper_theorem":True}


def odometer_cylinder_projection(source_period:int,target_period:int)->tuple[int,...]:
    """A valid finite clopen cylinder map only when the smaller clock divides."""
    _nat(source_period,"source cylinder period",maximum=10000)
    _nat(target_period,"target cylinder period",maximum=10000)
    if source_period%target_period:
        raise ClockSourceError("no coherent profinite quotient on this finite cylinder")
    return tuple(k%target_period for k in range(source_period))


def hidden_contraction_same_profinite_point(factorial_depth:int,clock_moduli:tuple[int,...])->dict:
    """Finite witness for K=orbit-closure in Zhat x [0,1].

    At times j!, every fixed finite modular coordinate eventually returns to 0
    while u_(j!) -> 1 != 0. The global non-injective fiber needs limit theorem.
    """
    _nat(factorial_depth,"factorial depth",minimum=2,maximum=20)
    if type(clock_moduli) is not tuple or any(type(m) is not int or m<1 for m in clock_moduli):
        raise ClockSourceError("finite actual clock moduli required")
    n=factorial(factorial_depth)
    # Keep 2^(-n) symbolic: materializing 2^(20!) would be impossible.
    return {"n":n,"observed_moduli":clock_moduli,
            "all_sampled_profinite_residues_zero":all(n%m==0 for m in clock_moduli),
            "distance_of_hidden_coordinate_from_limit":f"2^(-{n})",
            "root_hidden_coordinate":"0", "limit_hidden_coordinate":"1",
            "same_global_profinite_point_in_limit_paper_theorem":True,
            "no_finite_check_proves_infinite_noninjective_fiber":True}
