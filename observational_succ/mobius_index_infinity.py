"""Möbius sieve projections, SUCC index-at-infinity, FUCC Haar shells.

CLASSICAL exact mathematics in an authenticated source-indexed SUCC model:
  S|n>=|n+1>, V_p|n>=|pn> on l2(N_{>=1}).
P_p=V_p V_p* projects to multiples of a GENUINE prime p. Hence
  E_P=prod_{p in P}(I-P_p)=sum_{d|primorial(P)}mu(d)V_d V_d*
is an orthogonal projection, positive despite its signed coefficients.

The strong cofinal limit E_P -> |1><1| has norm defect exactly 1 at
every FINITE stage, while normalized counting traces converge to the
finite-idelic unit Haar mass prod(1-1/p), then to zero across all primes.

The p^k shell projector P_{p,k}=P_{p^k}-P_{p^(k+1)} has asymptotic
arithmetic density (1-1/p)*p^-k. Dividing by unit Haar mass gives p^-k
and its Hilbert positive square-root p^-k/2, independently matching
the local Connes and Tate half-density. No zero locations, no
Archimedean Gamma/contact, no Weil positivity, no RH proof.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd, isqrt, prod


class IndexBoundaryError(ValueError):
    """Malformed source, fake prime-place, or unsupported exact finite horizon."""


def _natural_source(n, *, lower=1, upper=2_000_000):
    if type(n) is not int or not lower <= n <= upper:
        raise IndexBoundaryError("genuine integer source in declared finite horizon")
    return n


def _prime(p):
    _natural_source(p, lower=2, upper=200_000)
    if any(p % j == 0 for j in range(2, isqrt(p) + 1)):
        raise IndexBoundaryError("local Euler place must be a genuine prime")
    return p


def _primes(primes):
    if (type(primes) is not tuple or len(primes) > 9 or
        any(type(p) is not int for p in primes) or
        primes != tuple(sorted(set(primes)))):
        raise IndexBoundaryError("sorted distinct finite genuine prime places required")
    for p in primes:
        _prime(p)
    return primes


def _k(k):
    if type(k) is not int or not 0 <= k <= 40:
        raise IndexBoundaryError("genuine exact p-valuation depth 0..40 required")
    return k


def squarefree_mobius_tape(primes):
    """Signed expansion of true Euler/projector factors. Exact finite algebra."""
    _primes(primes)
    out={1:1}
    for p in primes:
        out.update({p*d:-sign for d,sign in tuple(out.items())})
    expected=1<<len(primes)
    if len(out)!=expected or any(s not in (-1,1) for s in out.values()):
        raise AssertionError("squarefree prime orientation collision")
    return tuple(sorted(out.items()))


def sieve_projection(n,primes):
    """Exact <n|E_P|n>, computed from both multiplication and Möbius."""
    n=_natural_source(n)
    _primes(primes)
    product_value=prod((int(n%p!=0) for p in primes),start=1)
    mobius_value=sum(sign for d,sign in squarefree_mobius_tape(primes) if n%d==0)
    if product_value!=mobius_value or product_value not in (0,1):
        raise AssertionError("Möbius negative counting not a positive projection")
    return {
        "n":n,"genuine_primes":primes,
        "projection_diagonal":product_value,"signed_incidence_diagonal":mobius_value,
        "full_positive_projection_by_commuting_factors":True,
        "original_succ_fucc_source":True,
        "same_as_original_signed_Weil_quadratic":False,
    }


def finite_sieve_count(primes,N):
    """Trace P_N E_P P_N, with exact rational error to profinite Haar.

    floor(N/d)=N/d+epsilon_d, |epsilon_d|<1 for d>1.
    Therefore |count/N - prod_p(1-1/p)|<=(2^|P|-1)/N.
    For N divisible by M=prod P, the error is ZERO.
    """
    _primes(primes)
    N=_natural_source(N)
    tape=squarefree_mobius_tape(primes)
    observed=sum(sign*(N//d) for d,sign in tape)
    mass=prod((F(p-1,p) for p in primes),start=F(1))
    bound=F(len(tape)-1,N)
    if not (0<=observed<=N and abs(F(observed,N)-mass)<=bound):
        raise AssertionError("finite trace source-density majorant broken")
    return {
        "genuine_primes":primes,"N":N,
        "integer_source_trace":observed,
        "normalized_trace":F(observed,N),
        "additive_profinite_unit_Haar":mass,
        "exact_total_variation_scalar_error":abs(F(observed,N)-mass),
        "source_uniform_error_upper":bound,
        "perfect_period_when_N_multiple_of_primorial":N%prod(primes,start=1)==0,
        "mobius_terms":tape,
        "all_prime_limit_was_computed_by_finite_test":False,
        "RH_proved":False,
    }


def prime_shell(n,p,k):
    """True spectral projection onto exactly v_p(n)=k."""
    n=_natural_source(n)
    p=_prime(p);_k(k)
    pk=p**k
    value=int(n%pk==0)-int(n%(pk*p)==0)
    if value not in (0,1):
        raise AssertionError("a valuation-shell spectral projector is not positive")
    return value


def shell_trace(p,k,N):
    """Exact finite trace of the p-valuation shell and canonical Haar limit."""
    p=_prime(p);_k(k);N=_natural_source(N)
    power=p**k
    count=N//power-N//(power*p)
    source_density=F(p-1,p**(k+1))
    actual=F(count,N)
    delta=abs(actual-source_density)
    if delta>F(1,N):
        raise AssertionError("p-valuation shell discrepancy exceeds 1/N")
    return {
        "p":p,"k":k,"N":N,
        "finite_exact_shell_count":count,
        "normalized_finite_trace":actual,
        "limit_additive_Haar_shell_density":source_density,
        "p_adic_unit_Haar_mass":F(p-1,p),
        "multiplicative_Haar_shell_mass":F(1),
        "finite_horizon_density_error":delta,
        "rigorous_error_upper":F(1,N),
        "source_half_density_amplitude_squared":F(1,power),
        "source_original_half_density_symbol":f"1/sqrt({p}^{k})",
        "genuine_local_place":True,
        "Weil_positivity_proved":False,
    }


def finite_succ_boundary(N):
    """Compressed original unilateral SUCC S_N on e1..eN.

    [S_N*,S_N] = |1><1| - |N><N| (for N=1 both cancel).
    Trace is zero at EVERY finite N. Strong N->infinity limit is
    [S*,S]=|1><1| with trace one, because boundary |N><N|
    converges strongly but NOT in trace norm to zero.
    """
    N=_natural_source(N)
    diagonal=tuple((n,int(n==1)-int(n==N))
                   for n in range(1,N+1)
                   if int(n==1)-int(n==N))
    if sum(x for n,x in diagonal)!=0:
        raise AssertionError("finite-dimensional commutator trace not zero")
    return {
        "N":N,"finite_diagonal_nonzero":diagonal,
        "finite_commutator_trace":0,
        "strong_limit_commutator_rank":1,
        "strong_limit_trace":1,
        "negative_escape_boundary_trace":-1 if N>1 else 0,
        "operator_norm_error_for_N_greater_than_1":1 if N>1 else None,
        "trace_norm_convergence":False,
        "Fredholm_index_of_unilateral_S":-1,
        "no_canonical_Connes_global_trace_inferred":True,
    }


def finite_fucc_boundary(p,N):
    """Compression V_{p,N}=P_N V_p P_N.

    [V_{p,N}*,V_{p,N}] diagonal =
      1_{n<=floor(N/p)}-1_{p|n}, trace zero.
    Local strong limit at fixed n: 1-1_{p|n}; its normalized bulk
    trace tends to 1-1/p. The lost upper boundary has exact
    counterterm -1_{N/p<n<=N}, not a negligible trace correction.
    """
    p=_prime(p);N=_natural_source(N)
    low=N//p
    diag=tuple((n,int(n<=low)-int(n%p==0))
               for n in range(1,N+1)
               if int(n<=low)-int(n%p==0))
    if sum(x for n,x in diag)!=0:
        raise AssertionError("finite FUCC commutator trace !=0")
    return {
        "p":p,"N":N,"source_lower_interval_size":low,
        "finite_commutator_diagonal":diag,
        "finite_commutator_trace":0,
        "strong_local_limit_diagonal_rule":"1 - 1_{p|n}",
        "limit_defect_bulk_trace_density":F(p-1,p),
        "finite_upper_boundary_counterterm_trace":-(N-low),
        "normalized_escape_trace":F(-(N-low),N),
        "trace_density_at_fixed_N_of_compressed_commutator":F(0),
        "limit_operator_trace_class":False,
        "original_source_prime_powers_suppressed":False,
    }


def strong_sieve_limit(primes,probes):
    """Finite source probes of E_P -> P_1, plus UNIVERSAL proof contract.

    For every integer n>1, some prime divides it, so all cofinal
    sufficiently large P kill e_n. P_1 survives. For every finite P,
    Euclid gives a prime q outside P; E_P e_q=e_q and P_1 e_q=0,
    hence ||E_P-P_1||=1. Strong, NOT norm convergence.
    """
    _primes(primes)
    if type(probes) is not tuple or not probes:
        raise IndexBoundaryError("nonempty declared original integer probes")
    values=tuple((n,sieve_projection(n,primes)["projection_diagonal"])
                 for n in probes)
    return {
        "genuine_primes":primes,
        "finite_probe_response":values,
        "universal_strong_limit_on_all_l2_sequences":"|1><1|",
        "proof_from_unique_prime_factorization":True,
        "finite_stage_operator_norm_difference_from_limit":F(1),
        "norm_convergence":False,
        "every_finite_truncation_converges_in_integer_basis":True,
        "normalized_trace_limit_over_primes":"0 by sum_p 1/p divergence",
        "vacuum_state_limit":"1",
        "all_place_Weil_trace_identified":False,
    }


def exact_prime_jets_from_index_density(p,k):
    """Three exact, differently implemented original source routes.

    Shell density/(1-1/p)=p^-k matches Connes C_p(p^k)^2 and
    true one-place Tate idele norm. [H,V_p]=log(p)V_p then supplies
    log(p), yielding the magnitude log(p)/sqrt(p^k).
    This does NOT fix the signed global Weil functional.
    """
    p=_prime(p);_k(k)
    if k==0:
        raise IndexBoundaryError("Weil prime-power jet requires k>=1")
    if p**k>200000:
        raise IndexBoundaryError("original Weil source ceiling 200000")
    from .connes_oriented_scaling import prime_jet_half_density
    from .tate_idelic_zeta import RationalChartIdele,multiplicative_shell_mass
    from .completed_weil_transport import von_mangoldt_labels
    numerator=F(p-1,p**(k+1))
    unit=F(p-1,p)
    squared=numerator/unit
    connes=prime_jet_half_density(p,k)["half_density_coefficient_squared"]
    idele=RationalChartIdele(F(1),F(1),((p,F(p**k)),),
                             "Q-standard-Tate",0)
    original=dict(von_mangoldt_labels(p**k))
    if (squared!=F(1,p**k) or squared!=connes or
        squared!=idele.norm or multiplicative_shell_mass(p,k)!=1 or
        original.get(p**k)!=p):
        raise AssertionError("TRUE_ORIGINAL_PRIME_PLACE_HALF_DENSITY_MISMATCH")
    return {
        "p":p,"k":k,"p_power":p**k,
        "source_shell_density":numerator,
        "genuine_padic_unit_Haar":unit,
        "normalized_amplitude_squared":squared,
        "connes_Cp_squared":connes,
        "Tate_one_place_norm":idele.norm,
        "actual_von_Mangoldt_label":original[p**k],
        "original_H_Vp_commutator_symbol":f"log({p})",
        "source_prime_jet_weight":f"log({p})/sqrt({p}^{k})",
        "signed_Gamma_contact_pole_terms_derived":False,
        "all_test_completed_Weil_PSD_proved":False,
        "RH_proved":False,
    }


def sign_mutant_control(p):
    """Replace minus with plus: I+P_p is NOT a projection."""
    p=_prime(p)
    return {
        "genuine_prime":p,"authentic_at_n_p":0,
        "plus_sign_mutant_at_n_p":2,
        "mutant_square_at_n_p":4,
        "mutant_idempotent":False,
        "nonnegative_coefficients_alone_source_correct":False,
    }



def sieve_succ_commutator(primes,n):
    """Exact [S,E_P]|n> = (E_P(n)-E_P(n+1))|n+1>.

    Strong P-exhaustion gives [S,P1]=|2><1|. If P is a finite
    genuine prime set CONTAINING 2, choose any omitted prime q>3:
    E_P(q-1)=0 (even), E_P(q)=1, so [S,E_P]|q-1>=-|q>.
    The limiting [S,P1] vanishes on |q-1>. Thus the commutator
    convergence is STRONG but NEVER operator norm, with distance
    at least one. This is a source-dynamics obstruction to erasing
    an apparently negligible zero-density sieve frontier.
    """
    _primes(primes)
    n=_natural_source(n)
    if n>=2_000_000:
        raise IndexBoundaryError("original unit SUCC endpoint exceeds finite horizon")
    before=sieve_projection(n,primes)["projection_diagonal"]
    after=sieve_projection(n+1,primes)["projection_diagonal"]
    coef=before-after
    limit_coef=int(n==1)
    return {
        "genuine_primes":primes,"original_SUCC_edge":(n,n+1),
        "finite_sieve_edge_coefficient":coef,
        "strong_limit_unit_boundary_edge_coefficient":limit_coef,
        "difference_from_limit":coef-limit_coef,
        "cofinal_operator_norm_difference_at_least_one_if_2_in_P":2 in primes,
        "finite_stage_source_outcome_equals_global":coef==limit_coef,
        "completed_Weil_trace_or_contact_identified":False,
    }



def finite_normalized_trace_escape(N,fixed_label=1):
    """An exact probability state can lose ALL mass on fixed basis vectors.

    rho_N=P_N/N has Tr(rho_N)=1, but <n|rho_N|n>=1/N for
    every fixed n<=N and tends to zero. No trace-class positive
    density rho with Tr(rho)=1 can have ALL its diagonal entries
    zero, because Tr(rho)=sum_n<n|rho|n> for any orthonormal basis.
    Consequently a weak-* limit of normalized finite matrix traces
    (when taken via subsequences/subnets on bounded observables)
    is SINGULAR/non-normal, not an ordinary Hilbert-space density.

    This is a classical warning about 'normalization at infinity':
    the source observer state/topology matters. It does NOT identify
    a Dixmier trace or the Connes canonical trace functional.
    """
    N=_natural_source(N)
    n=_natural_source(fixed_label)
    prob=F(1,N) if n<=N else F(0)
    return {
        "finite_rank_source_cutoff":N,
        "fixed_original_integer_basis_label":n,
        "finite_density_matrix_trace":F(1),
        "density_matrix_operator_norm":F(1,N),
        "fixed_basis_probability":prob,
        "limit_fixed_basis_probability_for_every_n":F(0),
        "candidate_normal_state_with_all_zero_diagonals_possible":False,
        "source_tracial_state_at_infinity_can_be_nonnormal":True,
        "same_state_as_unit_vacuum":False,
        "actual_Connes_trace_constructed":False,
    }



def completed_source_blindness_controls():
    """Prove arithmetic Möbius/positive-sieve data do NOT identify completed W.

    The literal multiplication operators V_p are identical for ordinary
    zeta and primitive Dirichlet chi_-3; the ORIGINAL finite log derivative
    coefficient at p=2 has opposite sign, and ramified p=3 is omitted in
    chi_-3, even though the same sieve E_(2,3) acts on l2(N).

    Independently the canonical real Weil identity/contact test changes by
    2048/3003 under a +delta_0 mutation while E_(2,3) is unchanged.
    Thus the source representation without character, conductor and
    Gamma/contact data is NON-IDENTIFYING, not source-complete.
    """
    from .tate_weil_source_bridge import (
        TateWeilProfile, finite_log_derivative_tape,
    )
    from .source_homotopy_defect import compact_contact_ambiguity
    zeta=finite_log_derivative_tape(12,TateWeilProfile.canonical("zeta"))
    chi=finite_log_derivative_tape(12,TateWeilProfile.canonical("chi_minus_3"))
    true_z={n:phase for n,p,phase in zeta}
    true_chi={n:phase for n,p,phase in chi}
    contact=compact_contact_ambiguity(F(1))
    if (true_z.get(2)!=1 or true_chi.get(2)!=-1 or
        true_z.get(3)!=1 or 3 in true_chi or
        contact["difference_in_signed_Weil_autocorrelation"]!=F(2048,3003)):
        raise AssertionError("SOURCE_CHARACTER_OR_CONTACT_MUTANT_NOT_DISCRIMINATED")
    return {
        "original_multiplicative_source":"same integer Vp in both profiles",
        "positive_Mobius_sieve_source":"same E_(2,3) in both profiles",
        "zeta_primitive_p2_dirichlet_coefficient":true_z[2],
        "chi_minus_3_primitive_p2_coefficient":true_chi[2],
        "zeta_p3_euler_coefficient":true_z[3],
        "chi_minus_3_p3_ramified_factor_absent":3 not in true_chi,
        "unit_W_contact_mutation_effect":contact["difference_in_signed_Weil_autocorrelation"],
        "unit_W_contact_mutation_visible_to_E_sieve":False,
        "full_signed_completed_W_identifiable_from_Vp_only":False,
        "character_conductor_and_Arch_contact_are_redundant":False,
        "RH_proved":False,
    }
