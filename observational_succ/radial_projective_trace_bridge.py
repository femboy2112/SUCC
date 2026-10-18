"""p+1 Bruhat--Tits radial to p^k half-density and true idelic norm.

The first sphere has p+1 vertices and every further NONBACKTRACKING
sphere multiplies by p. The unique boundary normalization
sqrt((p+1)/p) / sqrt(sphere_size(p,k)) is exactly p^(-k/2).

This is a PROVED coefficient identity; it does NOT produce Connes' global
trace or fix Weil's distributional sign/contact/Gamma. Exact rationals
track squares of amplitudes, no assumed floating square roots.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt


class RadialTraceError(ValueError):
    """Malformed prime geometry, valuation depth or real/Tate source."""


def _prime(p):
    if type(p) is not int or not 2<=p<=1_000_000 or any(
        p%d==0 for d in range(2,isqrt(p)+1)
    ):
        raise RadialTraceError("genuine prime local place required")
    return p


def _depth(k,minimum=0,maximum=64):
    if type(k) is not int or not minimum<=k<=maximum:
        raise RadialTraceError("finite exact valuation depth required")
    return k


def sphere_size(p,k):
    """Exact # vertices at distance k in (p+1)-regular BT tree."""
    _prime(p);_depth(k)
    return 1 if k==0 else (p+1)*p**(k-1)


def radial_squared_amplitude(p,k):
    """For k>=1 the oriented first-sphere renormalization is p^-k.

    Radius zero requires a separate unit/identity-contact normalization.
    """
    _prime(p);_depth(k,minimum=1)
    n=sphere_size(p,k)
    raw_inverse_sphere=Q(1,n)
    projective_boundary_norm=Q(p+1,p)
    geometric=projective_boundary_norm*raw_inverse_sphere
    if geometric != Q(1,p**k):
        raise AssertionError("prime jet half-density geometry mismatch")
    return {
        "p":p,"k":k,"sphere_cardinality":n,
        "sphere_growth_ratio_after_first":p,
        "first_sphere_over_forward_branch_ratio":projective_boundary_norm,
        "inverse_sphere_amplitude_squared":raw_inverse_sphere,
        "normalized_amplitude_squared":geometric,
        "arith_half_density_squared":Q(1,p**k),
        "primitive_clock_symbol":f"log({p})",
        "candidate_Weil_magnitude_symbol":f"log({p})/sqrt({p}^{k})",
        "full_Connes_trace_obtained":False,"RH_proved":False,
    }


def radial_adjacency_coeff_square(p,i,j):
    """Symmetric normalized radial Jacobi adjacency coefficient squared."""
    _prime(p);_depth(i);_depth(j)
    if abs(i-j)!=1:
        return 0
    return p+1 if min(i,j)==0 else p


def radial_boundary_defect(p):
    """A_radial - sqrt(p)(V+V*) supported on first radial edge.

    A_radial has weight sqrt(p+1) from level 0 to 1, and sqrt(p)
    on every later edge. The difference is a real rank-two
    offdiagonal operator with eigenvalues +/- (sqrt(p+1)-sqrt(p)).
    Distinct eigenvalue signs mean positivity is NOT inherited.
    """
    _prime(p)
    return {
        "prime":p,"first_radial_coefficient_square":p+1,
        "all_later_coefficient_squares":p,
        "squared_weight_mismatch":1,
        "difference_is_rank_two":True,
        "boundary_defect_has_positive_and_negative_directions":True,
        "canonical_Connes_identity_contact_identified":False,
    }


def tree_adjacency_sign_transport(p,k):
    """Bipartite orientation J|sphere_k>=(-1)^k|sphere_k>.

    J A J=-A and J (A*A) J=A*A. Signed edges are gauge for
    fully-transported observables, NOT a proof that A is positive.
    """
    _prime(p);_depth(k)
    if k==64:
        raise RadialTraceError("one extra adjacent level needed")
    sign_i=(-1)**k
    sign_j=(-1)**(k+1)
    return {
        "edge":(k,k+1),"original_weight_square":radial_adjacency_coeff_square(p,k,k+1),
        "parity_left":sign_i,"parity_right":sign_j,
        "conjugated_edge_sign":sign_i*sign_j,
        "squared_positive_quadratic_invariant":True,
        "adjacency_itself_positive_definite":False,
    }


def independent_three_route_prime_jet(p,k,source_id="Q-standard-Tate",epoch=0):
    """Compare genuine BT normalized shell, Connes local fixed point and
    existing Tate idelic p-only norm on the SAME p,k source labels.

    The three objects share this squared coefficient; an equality of
    completed *distributions* does not follow. No external zero reads.
    """
    _prime(p);_depth(k,minimum=1,maximum=24)
    if type(source_id) is not str or not source_id.strip():
        raise RadialTraceError("source identifier required")
    if type(epoch) is not int or epoch<0:
        raise RadialTraceError("source epoch required")
    from .tate_idelic_zeta import RationalChartIdele
    from .connes_oriented_scaling import local_fixed_point, RationalScale
    geo=radial_squared_amplitude(p,k)
    local=RationalChartIdele(Q(1),Q(1),((p,Q(p)**k),),source_id,epoch)
    connes=local_fixed_point(RationalScale(Q(p)**k,source_id,epoch),p,1)
    if not (geo["normalized_amplitude_squared"]==
            local.norm==connes.half_density_coefficient_squared==Q(1,p**k)):
        raise AssertionError("TRIPLE_PRIME_PLACE_HALF_DENSITY_MISMATCH")
    return {
        "source":source_id,"epoch":epoch,"p":p,"k":k,
        "BT_radial_squared":geo["normalized_amplitude_squared"],
        "Tate_single_place_idele_norm":local.norm,
        "Connes_off_identity_half_density_squared":connes.half_density_coefficient_squared,
        "exact_local_three_route_agreement":True,
        "all_place_trace_identified":False,"Weil_sign_proved":False,
    }


def rooted_ball_vertices(p,depth):
    """Small exact finite BT-tree ball used ONLY for independent combinatorics."""
    _prime(p);_depth(depth,maximum=5)
    if p>5:
        raise RadialTraceError("finite brute-tree oracle requires p<=5")
    root=(0,)
    layers=[(root,)]
    for level in range(1,depth+1):
        branching=p+1 if level==1 else p
        layers.append(tuple(parent+(j,) for parent in layers[-1]
                            for j in range(branching)))
    return tuple(layers)


def independent_ball_sphere_oracle(p,depth):
    """Brute original graph count instead of invoking closed form sphere size."""
    layers=rooted_ball_vertices(p,depth)
    empirical=tuple(len(layer) for layer in layers)
    theoretical=tuple(sphere_size(p,k) for k in range(depth+1))
    return {
        "p":p,"depth":depth,"brute_spheres":empirical,
        "theorem_spheres":theoretical,
        "source_tree_counts_match":empirical==theoretical,
        "infinite_tree_constructed_by_finite_run":False,
    }


def classical_tate_positive_euler_crosscheck(p,beta,depth=4):
    """Actual Tate unramified local Mellin and p^k tower on Re(s)>1.

    Signed uniform negative twist yields 1/(1+p^-beta), while standard
    zeta is 1/(1-p^-beta). No source equivalence by probabilities alone.
    """
    _prime(p)
    if type(beta) is not int or not 2<=beta<=12:
        raise RadialTraceError("integer convergent Tate exponent >=2")
    _depth(depth,maximum=20)
    from .tate_idelic_zeta import finite_euler_stage
    from .oriented_mobius_adelic import signed_local_euler_factor
    true=finite_euler_stage((p,),beta,depth)
    signed=signed_local_euler_factor(p,beta,-1)
    positive=signed_local_euler_factor(p,beta,+1)
    if true["complete_finite_place_product"]!=positive["phase_twisted_local"]:
        raise AssertionError("Tate local Euler contract mismatch")
    if signed["phase_twisted_local"]==positive["phase_twisted_local"]:
        raise AssertionError("wrongly equated opposite Euler source")
    return {
        "p":p,"beta":beta,"Tate_actual_local_factor":true["complete_finite_place_product"],
        "positive_tower_factor":positive["phase_twisted_local"],
        "negative_twist_factor":signed["phase_twisted_local"],
        "actual_source_equal_to_positive":True,
        "actual_source_equal_to_negative":False,
        "gamma_pole_contact_and_global_trace_proved":False,
    }



def original_weil_prime_tape_gate(N):
    """Cross-check EVERY genuine p^k <= N against pinned actual Weil source.

    Independent integer prime enumeration constructs the same (n,p) pairs.
    This is an exact proof-scoped magnitude identification; signs/contact,
    Gamma and all-test trace remain deliberately separate.
    """
    if type(N) is not int or not 2<=N<=500:
        raise RadialTraceError("exact finite full-prime horizon 2..500")
    from .completed_weil_transport import von_mangoldt_labels
    original=von_mangoldt_labels(N)
    candidate=[]
    for p in range(2,N+1):
        if p>2 and any(p%d==0 for d in range(2,isqrt(p)+1)):
            continue
        k=1
        while p**k<=N:
            rec=radial_squared_amplitude(p,k)
            n=p**k
            if rec["normalized_amplitude_squared"]!=Q(1,n):
                raise AssertionError("wrong complete original source weight")
            candidate.append((n,p,k))
            k+=1
    expected=tuple(sorted((n,p) for n,p,k in candidate))
    if expected!=original or (6,6) in expected:
        raise AssertionError("MUTATED_ORIGINAL_WEIL_PRIME_SOURCE")
    return {
        "horizon":N,"original_prime_power_tape":original,
        "radial_prime_jet_tape":tuple(sorted(candidate)),
        "exact_all_prime_power_labels_and_half_density_squares":True,
        "fake_prime6_not_in_source":(6,6) not in expected,
        "original_signed_Weil_distribution_identified":False,
        "arch_gamma_contact_added":False,"RH_proved":False,
    }
