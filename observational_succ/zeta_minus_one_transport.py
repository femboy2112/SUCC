"""Exact finite-prime versus global analytic transport at zeta(-1).

This mathematical laboratory distinguishes four operations:
1. The convergent prime Euler product for Re(s)>1, especially s=2.
2. The finite local rational factor L_p(-1)=1/(1-p), whose infinite
   cutoff product tends to ZERO (and is NOT zeta(-1)).
3. The functional equation mapping zeta(-1) to -zeta(2)/(2*pi^2),
   a *global*, source-specific relation including the Archimedean place.
4. Abel continuation of the alternating eta series, recovering -1/12.

Only finite exact rational computations are executed. The global functional
equation and zeta(2)=pi^2/6 are classical imported theorems, not derived by
the source code. The rigorous Euler cutoff bound follows by comparing the
prime tail with a telescoping product over all integers > cutoff.

Removing the p=2 factor or injecting a fake composite Euler factor
demonstrates why the same global reflection formula cannot be applied
blindly to a modified source. No theorem about RH zero locations is claimed.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, pi, prod


class EulerTransportError(ValueError):
    """An invalid source, prime, domain, or analytic transport assumption."""


def _integer(value, smallest:int = 0, maximum:int = 100000):
    if type(value) is not int or value < smallest or value > maximum:
        raise EulerTransportError("Exact integer in declared finite domain required")
    return value


def _prime(p:int) -> bool:
    if type(p) is not int or p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    d=3
    while d*d<=p:
        if p%d==0:
            return False
        d+=2
    return True


def primes_upto(cutoff:int) -> tuple[int,...]:
    """Deterministic exact prime enumeration, no external source required."""
    _integer(cutoff,2,10000)
    sieve=bytearray(b"\x01")*(cutoff+1)
    sieve[:2]=b"\x00\x00"
    for p in range(2,int(cutoff**0.5)+1):
        if sieve[p]:
            sieve[p*p:cutoff+1:p]=b"\x00"*(((cutoff-p*p)//p)+1)
    return tuple(i for i in range(2,cutoff+1) if sieve[i])


def prime_jet_gap(p:int,k:int=0) -> int:
    """Finite SUCC steps between p^k and p^(k+1): (p-1)*p^k."""
    if not _prime(p):
        raise EulerTransportError("FUCC prime jet requires an actual prime")
    _integer(k,0,64)
    return (p-1)*p**k


def shift_dilation_address_defect(multiplier:int, address:int, shifts:int=1) -> int:
    """Exact affine SUCC/FUCC coordinate discrepancy.

       S^a V_q(n) - V_q S^a(n)
         = (q*n+a) - q*(n+a) = a*(1-q).

    q need not be prime! Thus this algebraic identity cannot, by itself,
    pick out the prime factors in Euler's product. Also, this is a
    *difference of destination indices*, not a scalar operator commutator
    on the Hilbert space with basis |n>.
    """
    _integer(multiplier,2,10000)
    _integer(address,1,1000000)
    _integer(shifts,0,128)
    left=multiplier*address+shifts
    right=multiplier*(address+shifts)
    actual=left-right
    if actual != shifts*(1-multiplier):
        raise ArithmeticError("Exact affine shift-dilation law contradicted")
    return actual


def shift_dilation_operator_identity(p:int,address:int,shifts:int=1) -> bool:
    """Equality of kets V_p S^a|n> = S^(p*a) V_p|n>.

    Demonstrates the established ax+b semigroup relation, NOT a
    construction of Cuntz's completed / quotient C*-algebra.
    """
    _integer(p,2,10000)
    _integer(address,1,1000000)
    _integer(shifts,0,128)
    return p*(address+shifts)==p*address+p*shifts



def local_prime_factor_minus_one(p:int) -> Fraction:
    """Analytic/RATIONAL continuation of ONE geometric Euler factor only."""
    if not _prime(p):
        raise EulerTransportError("Euler factors are indexed by prime places")
    return Fraction(1,1-p)


def local_factor_at_two(p:int) -> Fraction:
    """Convergent positive-side Euler factor (1-p^(-2))^(-1)."""
    if not _prime(p):
        raise EulerTransportError("Euler factor needs a real prime")
    return Fraction(p*p,p*p-1)


def naive_cutoff_at_minus_one(cutoff:int) -> Fraction:
    """Product of separately continued prime factors; tends to zero."""
    return prod((local_prime_factor_minus_one(p)
                 for p in primes_upto(cutoff)),start=Fraction(1))


def convergent_cutoff_at_two(cutoff:int) -> Fraction:
    """Finite rational Euler product, converging upward to zeta(2)."""
    return prod((local_factor_at_two(p)
                 for p in primes_upto(cutoff)),start=Fraction(1))


@dataclass(frozen=True)
class EulerGlobalCutoff:
    """Rigorous bounds for zeta(2) using prime product through X.

    zeta(2)= P_X * tail; 1 <= tail <= (X+1)/X, since the
    omitted primes are a subset of omitted integers n>X and
    product_{n=X+1}^infty (1-n^-2)^-1 = (X+1)/X.

    By classical functional equation,
      (-2*pi^2)*zeta(-1) == zeta(2)
    so the same rational interval bounds this normalized
    Archimedean-transported negative-side value.

    The upper bound on the *unscaled* transport error is
    1/(12*X), using zeta(2)=pi^2/6 and P_X<=zeta(2).
    """
    cutoff:int
    primes:tuple[int,...]
    naive_local_product:Fraction
    convergent_positive_product:Fraction
    zeta_two_lower:Fraction
    zeta_two_upper:Fraction
    absolute_minus_one_error_leq_coefficient:Fraction

    @property
    def prime_count(self):
        return len(self.primes)

    def rigorous_tail_ratio_upper(self):
        return Fraction(self.cutoff+1,self.cutoff)

    def transported_minus_one_estimate(self):
        """Numerical DISPLAY ONLY; proof needs separate classical pi/FE."""
        return -float(self.convergent_positive_product)/(2*pi*pi)

    def exact_report(self):
        return {
            "cutoff":self.cutoff,
            "prime_count":self.prime_count,
            "last_prime":self.primes[-1],
            "continued_local_product":str(self.naive_local_product),
            "positive_euler_product":str(self.convergent_positive_product),
            "zeta_2_lower":str(self.zeta_two_lower),
            "zeta_2_upper":str(self.zeta_two_upper),
            "tail_ratio_upper":str(self.rigorous_tail_ratio_upper()),
            "transport_error_absolute_leq":str(self.absolute_minus_one_error_leq_coefficient),
            "transported_minus_one_estimate_display_only":self.transported_minus_one_estimate(),
        }


def certified_euler_cutoff(cutoff:int) -> EulerGlobalCutoff:
    primes=primes_upto(cutoff)
    local=naive_cutoff_at_minus_one(cutoff)
    positive=convergent_cutoff_at_two(cutoff)
    expected=Fraction((-1)**len(primes),prod((p-1 for p in primes)))
    if local!=expected or positive<=1:
        raise ArithmeticError("Prime cutoff source was inconsistent")
    upper=positive*Fraction(cutoff+1,cutoff)
    return EulerGlobalCutoff(
        cutoff,primes,local,positive,positive,upper,
        Fraction(1,12*cutoff),
    )


def positive_side_mutation_controls():
    """Removing p=2 or adding a fake p=6 destroys original source identity.

    F(s)=(1-2^-s)*zeta(s) excludes prime two in Re(s)>1.
      F(-1)=(1-2)*(-1/12) = +1/12.
      F(2)=(1-1/4)*zeta(2) = 3/4*zeta(2).
    Wrongly applying zeta's SAME gamma/reflection factor to F would
    produce -F(2)/(2*pi²)= -1/16, not +1/12.

    Source-mutated functions may have their own functional equations
    or auxiliary correction factors; one must derive them independently.
    """
    zeta_minus_one=Fraction(-1,12)
    actual_without_two=(1-2)*zeta_minus_one
    false_without_two=Fraction(3,4)*zeta_minus_one
    original_at_2=convergent_cutoff_at_two(11)
    fake_six=original_at_2*Fraction(6*6,6*6-1)
    if actual_without_two == false_without_two or fake_six==original_at_2:
        raise ArithmeticError("Source-control mutation did not change consequence")
    return {
        "base_zeta_minus_one":str(zeta_minus_one),
        "two_deletion_analytic_value":str(actual_without_two),
        "two_deletion_bad_reused_zeta_reflection":str(false_without_two),
        "prime_two_deletion_invalidates_unmodified_functional_equation":True,
        "fake_composite_six_factor_changes_convergent_prime_product":True,
        "fake_six_is_not_a_prime_euler_factor":not _prime(6),
    }


def eta_abel_value(r) -> Fraction:
    """Sum_{n>=1} (-1)^(n-1) n r^n = r/(1+r)^2, 0<=r<1.

    The r -> 1^- limit is eta(-1)=1/4 by Abel continuation.
    """
    if type(r) not in (int,Fraction):
        raise EulerTransportError("Only exact rational regulator is admitted")
    r=Fraction(r)
    if not 0<=r<1:
        raise EulerTransportError("Abel regulator lies in [0,1)")
    return r/(1+r)**2


def eta_abel_deficit(r) -> Fraction:
    """EXACT quadratic gap to eta(-1)=1/4."""
    value=eta_abel_value(r)
    r=Fraction(r)
    right=(1-r)**2/(4*(1+r)**2)
    left=Fraction(1,4)-value
    if left!=right:
        raise ArithmeticError("Abel convergence identity failed")
    return left


def negative_odd_zeta_from_bernoulli(m:int) -> Fraction:
    """Classical zeta(1-2m)=-B_{2m}/(2m), exact rational regression.

    The Bernoulli values are generated from their standard recurrence;
    the identity to zeta analytic continuation is an imported theorem.
    """
    _integer(m,1,16)
    n=2*m
    B=[Fraction(1)]
    for j in range(1,n+1):
        numerator=sum(
            (Fraction(comb(j+1,k))*B[k] for k in range(j)),Fraction())
        B.append(-numerator/Fraction(j+1))
    return -B[2*m]/(2*m)


def bost_connes_spectral_trace_cutoff(beta:int,count:int) -> Fraction:
    """EXACT finite trace of the diagonal Dirichlet Hamiltonian.

    In the classical Bost–Connes representation H|n>=log(n)|n>, so
    Tr_N(exp(-beta H))=sum_{n=1}^N n^(-beta).
    For beta>1 the full infinite operator is trace class and the trace
    is zeta(beta). For beta=-1, the ordinary trace diverges like N^2/2.
    Its continuation -1/12 is NOT this operator's ordinary trace.

    This code only sums finite rational terms, and DOES NOT construct
    the Bost–Connes C*-dynamical system or any KMS state.
    """
    _integer(count,1,4096)
    if type(beta) is not int or not -8<=beta<=8:
        raise EulerTransportError("Use a bounded integer inverse-temperature exponent")
    return sum((Fraction(n,1)**(-beta) for n in range(1,count+1)),
               Fraction(0))


def zeta_minus_one_transport_demo():
    small=(certified_euler_cutoff(x) for x in (2,3,5,7,11,29,47))
    cutoffs=[x.exact_report() for x in small]
    if [x["continued_local_product"] for x in cutoffs[:5]]!=[
        "-1","1/2","-1/8","1/48","-1/480"
    ]:
        raise ArithmeticError("Local factor source jet sequence changed")
    if negative_odd_zeta_from_bernoulli(1)!=Fraction(-1,12):
        raise ArithmeticError("Bernoulli zeta(-1) independent certificate failed")
    if negative_odd_zeta_from_bernoulli(2)!=Fraction(1,120):
        raise ArithmeticError("Higher negative-odd functional equation failed")
    mutation=positive_side_mutation_controls()
    for N in (1,2,4,8,16):
        if bost_connes_spectral_trace_cutoff(-1,N)!=Fraction(N*(N+1),2):
            raise ArithmeticError("Finite diagonal negative beta trace contradicted")
    if bost_connes_spectral_trace_cutoff(2,4)!=sum(
            (Fraction(1,n*n) for n in range(1,5)),Fraction()):
        raise ArithmeticError("Positive beta trace cutoff contradicted")
    for p in (2,3,5,7,11,13):
        if (shift_dilation_address_defect(p,3)!=1-p
                or not shift_dilation_operator_identity(p,3)):
            raise ArithmeticError("SUCC/FUCC ax+b semigroup relation failed")
    if shift_dilation_address_defect(6,3)!=-5:
        raise ArithmeticError("Composite nonprime semigroup negative control failed")
    return {
        "status":"ZETA_MINUS_ONE_GLOBAL_EULER_ARCHIMEDEAN_TRANSPORT",
        "local_prime_minus_one_factor":"-1/(p-1)",
        "prime_jet_first_return_gap":"p-1",
        "shift_dilation_one_step_address_defect":"1-p",
        "ax_b_operator_semigroup_relation":"V_p S = S^p V_p",
        "same_shift_dilation_defect_rule_for_composite_six":True,
        "nonprime_affine_defect_does_not_authorize_euler_prime_factor":True,
        "operator_commutator_claimed_scalar":False,
        "cuntz_ax_b_finite_arch_completion_proved_here":False,
        "local_factor_is_rational_continuation_of_geometric_series":True,
        "local_factor_partial_products_tend_to_zero":True,
        "global_zeta_minus_one_value":"-1/12",
        "global_transport_identity":"zeta(-1)=-zeta(2)/(2*pi^2)",
        "completed_zeta_symmetric_values":"Lambda(-1)=Lambda(2)=pi/6",
        "bost_connes_classical_diagonal_hamiltonian":"H|n> = log(n)|n>",
        "bost_connes_partition_function_for_beta_gt_one_is_zeta":True,
        "bost_connes_positive_beta_two_finite_trace_n_four":str(bost_connes_spectral_trace_cutoff(2,4)),
        "bost_connes_beta_minus_one_finite_trace_n_four":str(bost_connes_spectral_trace_cutoff(-1,4)),
        "bost_connes_analytic_zeta_minus_one_is_not_ordinary_trace":True,
        "bost_connes_operator_algebra_or_KMS_state_constructed_here":False,
        "positive_side_prime_product_converges":True,
        "finite_positive_prime_cutoffs_with_rigorous_tail_bound":cutoffs,
        "abel_eta_negative_one":"1/4",
        "eta_to_zeta_factor_at_minus_one":"-3",
        "abel_eta_derivation_matches_zeta_negative_one":True,
        "negative_odd_s_minus_three":str(negative_odd_zeta_from_bernoulli(2)),
        "prime_source_mutation_controls":mutation,
        "local_continuation_and_global_product_commute":False,
        "analytic_continuation_and_functional_equation_are_imported_theorems":True,
        "source_specific_euler_gamma_completed_weil_RH_bridge_proved":False,
        "nontrivial_zeta_zeros_used_as_inputs":False,
        "RH_claimed":False,
    }
