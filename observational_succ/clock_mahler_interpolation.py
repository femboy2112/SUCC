"""Clock algebra, Mahler finite differences and Kummer p-adic congruences.

CLASSICAL external mathematical results:
  (1) Euler's theorem: a^phi(p^r)=1 mod p^r for p not dividing a.
  (2) Mahler's theorem: continuous Z_p -> Q_p functions are exactly the
      convergent Newton series sum Delta^j f(0) * binom(x,j), coefficients
      converging p-adically to zero.
  (3) Kummer congruence: for suitable positive even weights k,l not
      divisible by p-1, if k==l mod (p-1)p^(r-1), then
      (1-p^(k-1))*B_k/k == (1-p^(l-1))*B_l/l mod p^r.

EXACT elementary laboratory:
  The SUCC/FUCC prime gap (p-1)p^(r-1) is also the odd-p unit clock
  period phi(p^r). The local clock function f_p(n)=(1-p)^n has
  Delta^j f_p(0)=(-p)^j and Mahler interpolation at -1 yields
  1/(1-p)=sum_{j>=0}p^j in Q_p. These identities are proved exactly
  by binomial algebra and geometric-series tails.

The code computes exact modular instances of Kummer's IMPORTED theorem,
including the negative control that the UNCORRECTED zeta values need not
obey the same precision clock. Tests do not prove Kummer congruences for
all indices, construct a Kubota--Leopoldt measure, prove analyticity,
or establish any connection to RH nontrivial-zero placement.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from math import comb

from .residue_one_arch import prime, valuation, residue


class ClockInterpolationError(ValueError):
    """Wrong prime, weight branch, modulus or nonintegral p-adic source."""


def _bounded_int(n, smallest, largest):
    if type(n) is not int or not smallest <= n <= largest:
        raise ClockInterpolationError("Bounded exact integer required")
    return n


def unit_clock_period(p:int, resolution:int) -> int:
    """For odd p, phi(p^resolution)=(p-1)p^(resolution-1)."""
    if not prime(p) or p == 2:
        raise ClockInterpolationError("Odd prime unit clock required")
    _bounded_int(resolution,1,5)
    return (p-1)*p**(resolution-1)


def prime_jet_return_gap(p:int,jet_level:int) -> int:
    """SUCC gap p^(j+1)-p^j exactly equals unit clock period p^(j+1)."""
    _bounded_int(jet_level,0,4)
    return unit_clock_period(p,jet_level+1)


def unit_clock_power(p:int,resolution:int,unit:int,weight:int) -> int:
    """Reading on (Z/p^r Z)^x, where weight can be any integer."""
    period=unit_clock_period(p,resolution)
    _bounded_int(unit,-1000000,1000000)
    _bounded_int(weight,-1000000,1000000)
    if unit%p==0:
        raise ClockInterpolationError("Nonunit base cannot be read on unit clock")
    modulus=p**resolution
    # Negative powers exist because unit is invertible modulo p^r.
    return pow(unit,weight%period,modulus)


def unit_clock_indistinguishability(p:int,resolution:int,a:int,b:int):
    """Every unit gives same output for exponent separation by period."""
    period=unit_clock_period(p,resolution)
    _bounded_int(a,-100000,100000)
    _bounded_int(b,-100000,100000)
    if (a-b)%period!=0:
        raise ClockInterpolationError("Exponents not on same p-adic clock tick")
    modulus=p**resolution
    for unit in range(1,modulus):
        if unit%p and unit_clock_power(p,resolution,unit,a) != unit_clock_power(
            p,resolution,unit,b
        ):
            raise ArithmeticError("Euler clock periodicity contradicted")
    return True


def local_power_mahler_coefficient(p:int,j:int) -> int:
    """Delta^j[(1-p)^n] at n=0 is exactly (-p)^j."""
    if not prime(p):
        raise ClockInterpolationError("A genuine prime-indexed source required")
    _bounded_int(j,0,128)
    return (-p)**j


def local_euler_from_mahler_truncation(p:int,terms:int):
    """Evaluate the p-adic Mahler series f_p(-1) to K terms.

    f_p(x)=(1-p)^x has coefficients a_j=(-p)^j.
    binom(-1,j)=(-1)^j, hence f_p(-1)=sum_{j>=0}p^j.
    Difference of rational target and K terms is p^K/(1-p)
    with valuation K and thus p-adic norm p^-K.
    """
    if not prime(p):
        raise ClockInterpolationError("Only authentic prime Euler factors")
    _bounded_int(terms,1,40)
    coefficients=tuple(local_power_mahler_coefficient(p,j)
                       for j in range(terms))
    partial=sum((Fraction(p)**j for j in range(terms)),Fraction())
    target=Fraction(1,1-p)
    defect=target-partial
    if defect!=Fraction(p**terms,1-p) or valuation(defect,p)!=terms:
        raise ArithmeticError("Mahler continuation/jet tail contradicted")
    if residue(target,p)!=1%p:
        raise ArithmeticError("Euler unit lost its prime-local residue 1")
    return {
        "p":p,
        "terms":terms,
        "initial_SUCC_jets":tuple(str(a) for a in coefficients),
        "coefficient_valuation_levels":tuple(range(terms)),
        "newton_evaluation_at_minus_one":str(partial),
        "continued_local_euler_factor":str(target),
        "exact_error":str(defect),
        "error_valuation":terms,
        "local_finite_precision_clock":str(p**terms),
        "residue_one_mod_prime":True,
        "p_adic_mahler_theorem_constructed":False,
    }


@lru_cache(maxsize=2048)
def bernoulli(n:int) -> Fraction:
    """Bernoulli B_n, standard convention B_1=-1/2, exact arithmetic.

    The Bernoulli special-value theorem zeta(1-n)=-B_n/n is IMPORTED.
    """
    _bounded_int(n,0,160)
    values=[Fraction(1)]
    for j in range(1,n+1):
        numerator=sum(
            (Fraction(comb(j+1,k))*values[k] for k in range(j)),Fraction())
        values.append(-numerator/Fraction(j+1))
    return values[n]


def corrected_zeta_value(p:int,even_weight:int) -> Fraction:
    """(1-p^(k-1))*zeta(1-k), on a NONEXCEPTIONAL even-weight branch.

    The value is algebraic/rational; interpreting this entire infinite
    family as values of one analytic p-adic function uses Kummer theory,
    not merely the finite test.
    """
    if (not prime(p) or p<5 or type(even_weight) is not int
            or not 2<=even_weight<=160 or even_weight%2
            or even_weight%(p-1)==0):
        raise ClockInterpolationError("Nonexceptional even weight and p>=5 required")
    return -Fraction(1-p**(even_weight-1))*bernoulli(even_weight)/even_weight


def raw_zeta_special_value(even_weight:int) -> Fraction:
    if type(even_weight) is not int or not 2<=even_weight<=160 or even_weight%2:
        raise ClockInterpolationError("Even positive weight required")
    return -bernoulli(even_weight)/even_weight


def rational_residue(value:Fraction,p:int,r:int) -> int:
    """p-adically integral rational value modulo p^r."""
    if not isinstance(value,Fraction) or not prime(p):
        raise ClockInterpolationError("Exact rational and prime needed")
    _bounded_int(r,1,5)
    if valuation(value,p)<0:
        raise ClockInterpolationError("Nonintegral value has no Z_p residue")
    return residue(value,p,r)


def kummer_clock_witness(p:int,resolution:int,weight:int):
    """Exact SPECIAL CASE of classical Kummer congruence.

    Compare k and k+phi(p^resolution). Both occupy the same tick
    at precision p^resolution. Test corrected Bernoulli special values.
    This is a test of an externally known theorem, not its universal proof.
    """
    modulus_period=unit_clock_period(p,resolution)
    _bounded_int(weight,2,128)
    neighbor=weight+modulus_period
    if neighbor>160:
        raise ClockInterpolationError("Weight exceeds exact Bernoulli cap")
    left=corrected_zeta_value(p,weight)
    right=corrected_zeta_value(p,neighbor)
    lr=rational_residue(left,p,resolution)
    rr=rational_residue(right,p,resolution)
    if lr!=rr:
        raise ArithmeticError("Kummer corrected zeta clock mismatch")
    rawleft=raw_zeta_special_value(weight)
    rawright=raw_zeta_special_value(neighbor)
    uncorrected=(rational_residue(rawleft,p,resolution),
                 rational_residue(rawright,p,resolution))
    return {
        "prime":p,
        "resolution":resolution,
        "unit_clock_period":modulus_period,
        "SUCC_FUCC_prime_jet_gap":prime_jet_return_gap(p,resolution-1),
        "weights":(weight,neighbor),
        "modulus":p**resolution,
        "corrected_zeta_residues":(lr,rr),
        "raw_zeta_residues":uncorrected,
        "corrected_values_are_clock_compatible":True,
        "uncorrected_values_are_clock_compatible":uncorrected[0]==uncorrected[1],
        "global_Kummer_congruence_proved_from_finite_examples":False,
        "p_adic_L_function_or_measure_constructed":False,
    }


def clock_mahler_demo():
    local=local_euler_from_mahler_truncation(5,4)
    if (local["continued_local_euler_factor"]!="-1/4"
            or local["error_valuation"]!=4):
        raise ArithmeticError("p=5 local Mahler source behavior changed")
    w5=kummer_clock_witness(5,2,2)
    w7=kummer_clock_witness(7,2,2)
    if (w5["weights"]!=(2,22)
            or w5["corrected_zeta_residues"]!=(17,17)
            or w5["raw_zeta_residues"]!=(2,17)
            or w7["corrected_zeta_residues"]!=(25,25)):
        raise ArithmeticError("Exact Kummer clock example changed")
    return {
        "status":"SUCC_CLOCK_MAHLER_KUMMER_COMPATIBILITY",
        "p_five_clock_mod_25_period":unit_clock_period(5,2),
        "p_five_SUCC_jet_gap_at_level_one":prime_jet_return_gap(5,1),
        "unit_clock_period_equals_prime_jet_gap":True,
        "mahler_source_function":"f_p(n)=(1-p)^n",
        "mahler_coefficient_formula":"Delta^r f_p(0)=(-p)^r",
        "mahler_interpolated_minus_one":"1/(1-p)",
        "mahler_p_five_local":local,
        "kummer_p_five_weights":w5,
        "kummer_p_seven_weights":w7,
        "wrong_unremoved_Euler_factor_breaks_clock_congruence":True,
        "clock_algebra_generates_a_p_adic_zeta_measure_without_extra_proofs":False,
        "classical_Mahler_and_Kummer_theorems_imported":True,
        "nontrivial_zeta_zeros_used":False,
        "RH_claimed":False,
    }
