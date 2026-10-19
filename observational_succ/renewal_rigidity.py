"""Exact rational Beurling mutant and translation-renewal source discriminator.

No zero locations computed.  This is an adversarial model, not an arithmetic
reconstruction of N from independently certified physical prime clocks.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import gcd

from .source_minimality import SourceLawError, modulus

MUTANT_A = F(9,2)      # replaces rational prime 3
MUTANT_B = F(35,11)    # replaces rational prime 5
BASE_COPRIME = 15
BASE_DENSITY = F(8,15)


def mutant_atoms(horizon):
    """Enumerate exactly {m*(9/2)^k*(35/11)^l: gcd(m,15)=1} <=H.

    Each source triple is a unique word because v_3=2k and v_5=l.
    Does NOT use primes as indexed source generators.
    """
    H = modulus(horizon, 20000)
    result = defaultdict(int)
    for m in range(1,H+1):
        if gcd(m,BASE_COPRIME)!=1: continue
        q = F(m)
        while q <= H:
            r = q
            while r <= H:
                result[r] += 1
                r *= MUTANT_B
            q *= MUTANT_A
    return dict(sorted(result.items()))


def calibration_atoms(horizon):
    """Independent target oracle for finite comparison, NOT an input source."""
    H = modulus(horizon,20000)
    return {F(n):1 for n in range(1,H+1)}


def renewal_residual(atoms, horizon):
    """η - (τ_1)_*η - δ_1, exact on all support points <=H.

    η is the pushed-forward multiplicative counting measure, τ_1(x)=x+1.
    Finite boundary terms above H are excluded explicitly.
    """
    H = modulus(horizon,20000)
    xs = {x for x in atoms if x <= H}
    xs.update(x+1 for x in atoms if x+1 <= H)
    xs.add(F(1))
    residual = {}
    for x in sorted(xs):
        if x < 1: continue
        c=F(atoms.get(x,0))-F(atoms.get(x-1,0))-(1 if x==1 else 0)
        if c: residual[str(x)] = str(c)
    return residual


def first_unit_cell(atoms):
    if atoms.get(F(1))!=1 or any(n!=1 for n in atoms.values()) or len(atoms)<2:
        raise SourceLawError("collision-free source with vacuum and successor required")
    return sorted(atoms)[1]-1


def affine_counterexample(atoms, q=F(2)):
    if any(v!=1 for v in atoms.values()) or q not in atoms:
        raise SourceLawError("affine-rank probe requires independent collision-free source")
    order = tuple(sorted(atoms))
    rank = {x:i+1 for i,x in enumerate(order)}
    for x,y in zip(order,order[1:]):
        if q*x in rank and q*y in rank:
            d=rank[q*y]-rank[q*x]-rank[q]
            if d:
                return {"x":str(x),"Sx":str(y),"q":str(q),
                        "rank_q":rank[q],"rank_qx":rank[q*x],
                        "rank_qSx":rank[q*y],"defect":d}
    return None


def density_residue_certificate():
    """Exact equality required by dominated-convergence asymptotic theorem.

    Dirichlet series on Re s>1:
    ζ_B(s)=ζ(s) (1-3^-s)(1-5^-s)/
                  ((1-(9/2)^-s)(1-(35/11)^-s)).
    """
    removed = (1-F(1,3))*(1-F(1,5))
    added = (1-1/MUTANT_A)*(1-1/MUTANT_B)
    assert removed == added == BASE_DENSITY
    return {"original_local_density":str(BASE_DENSITY),
            "new_local_euler_product":str(added),
            "zeta_factor_at_one":str(removed/added),
            "same_prime_count_as_ordinary_up_to_constant":True,
            "all_nontrivial_zero_coordinates_read":False,
            "proof_of_density_one_is_analytic_not_finite_enumeration":True}
