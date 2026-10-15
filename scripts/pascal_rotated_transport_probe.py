#!/usr/bin/env python3
"""Recompute exact Pascal/coupling/rotation/Gamma synthetic source receipt."""
from __future__ import annotations

import json
from fractions import Fraction as Q
from math import factorial, isqrt

from observational_succ.structural_coupling import discover_couplings
from observational_succ.pascal_rotated_transport import (
    UnitFrame,apply_pascal,backward_kernel,bayes_backwards_from_p,
    FractionalGammaSUCC,gamma_succ_convolution_moment,
    discrete_wait_probability,discrete_wait_survival,
    dual_count_time_certificate,colored_poisson_prefactor,count_time_adjunction,
    binomial_absolute_tail_enclosure,commutator_witness,
    coproduct_monomial,cyclic_convolve,evaluate_extension_fiber,
    falsely_commutative_sum,formal_path_monomials,forward_binomial,
    generalized_binomial,generalized_pascal_prefix,group_word_sum,
    laguerre_two_atom_moment,matmul,mixture_binomial,parity_character,
    pascal_matrix,project_backwards,residue_walk_law,rotate_clockwise,
    shifted_atomic_moment,shifted_exponential_moment,shift_moment_recurrence,
    triple_split_coefficient,weighted_adjoint,
)


def enc(obj):
    if isinstance(obj,Q):return str(obj)
    if isinstance(obj,tuple):return [enc(v) for v in obj]
    if isinstance(obj,list):return [enc(v) for v in obj]
    if isinstance(obj,dict):return {k:enc(v) for k,v in obj.items()}
    return obj


def receipt():
    f=UnitFrame(Q(1,2),Q(2,3),'stipulated-alpha','rational-unit-basis',0)
    p=Q(1,3)
    mixed=((Q(1,4),Q(1,4)),(Q(3,4),Q(3,4)))
    groups=discover_couplings(4,2).candidates
    N=5
    P=pascal_matrix(N,Q(2,3))
    W=(Q(1),Q(2),Q(3),Q(4),Q(5),Q(6))
    adj=weighted_adjoint(P,W)
    coassoc=all(triple_split_coefficient(n,a,b,n-a-b,'left')==
                triple_split_coefficient(n,a,b,n-a-b,'right')
                for n in range(10) for a in range(n+1) for b in range(n-a+1))
    inv=matmul(P,pascal_matrix(N,Q(-2,3)))==pascal_matrix(N,0)
    betas=tuple(forward_binomial(6,v) for v in (Q(1,3),Q(2,3)))
    p_back=bayes_backwards_from_p(6,3,Q(1,3))
    p_back_alt=bayes_backwards_from_p(6,3,Q(2,3))
    mixture=mixture_binomial(5,mixed)
    spectral=residue_walk_law(5,2,1,2,p)
    gentries=[]
    for g in groups:
        comm=commutator_witness(g)
        gentries.append({
            'rho':g.multiplier,'cocycle':list(g.cocycle),
            'commuting_generators':comm is None,
            'ordered_AB_BA_witness':comm,
            'pascal_word_fiber_2_1':evaluate_extension_fiber(g,2,1),
            'true_n2_word_operator':group_word_sum(g,2),
            'invalid_commutative_n2_operator':falsely_commutative_sum(g,2),
            'binomial_collapse_valid_at_n2':group_word_sum(g,2)==falsely_commutative_sum(g,2),
        })
    s=Q(1,2);z=Q(1,2);cutoff=18
    val=generalized_pascal_prefix(s,cutoff,z)
    err=binomial_absolute_tail_enclosure(s,cutoff,z)
    scale=10**12
    q=isqrt(3*scale**2//2)
    low=Q(q,scale);high=Q(q+1,scale)
    return enc({
      'program':'PASCAL_ROTATED_SUCC_SOURCE_RELATIVE_RECEIPT',
      'base':'femboy2112/SUCC research/structural-coupling-discovery-2026-10-13@cf36f907ac042f82c349b4c601083473836e34ca',
      'algebra':{
         'unit_steps':(f.a,f.b),'pascal_row_6':tuple((x.k,x.multiplicity,x.address) for x in f.row(6)),
         'formal_paths_row_6':formal_path_monomials(6),
         'coproduct_row_6':coproduct_monomial(6),
         'coassociativity_through_degree_9':coassoc,
         'B_d_B_negative_d_identity_N5':inv,
         'shifted_moments_example':apply_pascal((1,1,2,6,24),Q(2,3)),
      },
      'rotation':{
         'finite_depth_6_cell_2_1_rotated':rotate_clockwise(2,1,6),
         'same_cell_depth_7_rotated':rotate_clockwise(2,1,7),
         'weighted_adjoint_row0':adj[0],
         'adjoint_differs_from_inverse':adj!=pascal_matrix(N,Q(-2,3)),
         'metric_dependence':adj!=weighted_adjoint(P,(Q(1),)*6),
      },
      'boundary':{
         'p_one_third_row6':betas[0], 'p_two_thirds_row6':betas[1],
         'backwards_at_6_3_from_two_sources':(p_back,p_back_alt),
         'same_reverse_different_forward':p_back==p_back_alt and betas[0]!=betas[1],
         'mixed_row5':mixture,
         'mixture_projects_to_row4':project_backwards(mixture)==mixture_binomial(4,mixed),
         'global_point_forced_by_shape':not(p_back==p_back_alt and betas[0]!=betas[1]),
      },
      'couplings':{
         'distinct_c4_by_c2_candidates':len(groups),
         'ordered_word_fiber_diagnostics':gentries,
         'nonabelian_pascal_scalar_collapse_fails':all(
              group_word_sum(g,2)!=falsely_commutative_sum(g,2)
              for g in groups if commutator_witness(g) is not None),
         'group_path_order_preserved':all(
             tuple(sorted((v,sum(cnt for k in range(n+1) for t,cnt in evaluate_extension_fiber(g,n,k) if t==v))
                            for v in {u for k in range(n+1) for u,_ in evaluate_extension_fiber(g,n,k)}))
             ==group_word_sum(g,n) for g in groups for n in range(5)),
      },
      'operational_rotation':{
        'universal_count_time_adjunction_pathwise':all(
            count_time_adjunction((Q(0),Q(1,2),Q(1,2),Q(1),Q(3,2)),t,n)
            for t in (Q(0),Q(1,3),Q(1,2),Q(1),Q(3,2),Q(2)) for n in range(1,6)),
        'finite_pascal_wait_T3_eq5_p_half':discrete_wait_probability(5,3,Q(1,2)),
        'finite_wait_event_CDF_identity':all(
            discrete_wait_probability(m,3,Q(1,3))==
            discrete_wait_survival(m-1,3,Q(1,3))-discrete_wait_survival(m,3,Q(1,3))
            for m in range(1,33)),
        'colored_poisson_prefactor_N5':tuple(colored_poisson_prefactor(5,k,Q(1),Q(1,3)) for k in range(6)),
        'poisson_count_color_joint_normalization_prefactor':sum(
            (colored_poisson_prefactor(5,k,Q(1),Q(1,3)) for k in range(6)),Q(0)),
        'certified_Bernoulli_to_Poisson_wait_survival':tuple(
            (m,dual_count_time_certificate(m,3,Q(1))) for m in (4,8,16,32,64)),
        'false_fixed_p_scaling_negative_control':(
            discrete_wait_survival(60,3,Q(1,2)),
            discrete_wait_survival(60,3,Q(1,60))),
        'Gamma_entails_Poisson_source_not_Pascal_shape':
             discrete_wait_survival(60,3,Q(1,2))==discrete_wait_survival(60,3,Q(1,60)),
      },
      'fractional_gamma_succ':{
         'source_rate':Q(2),
         'shape_a':Q(1,2),
         'shape_b':Q(3,2),
         'convolution_shape':FractionalGammaSUCC(Q(1,2),Q(2)).compose(
             FractionalGammaSUCC(Q(3,2),Q(2))).shape,
         'moments_a_0_6':tuple(FractionalGammaSUCC(Q(1,2),Q(2)).moment(i) for i in range(7)),
         'moments_b_0_6':tuple(FractionalGammaSUCC(Q(3,2),Q(2)).moment(i) for i in range(7)),
         'moments_convolution_0_6':tuple(
             gamma_succ_convolution_moment(FractionalGammaSUCC(Q(1,2),Q(2)),
                                           FractionalGammaSUCC(Q(3,2),Q(2)),i)
             for i in range(7)),
         'moments_equal_direct_gamma_0_12':all(
             gamma_succ_convolution_moment(FractionalGammaSUCC(Q(1,2),Q(2)),
                                           FractionalGammaSUCC(Q(3,2),Q(2)),i)==
             FractionalGammaSUCC(Q(2),Q(2)).moment(i) for i in range(13)),
         'laplace_symbolic_rate2_u_2_3':FractionalGammaSUCC(Q(1,2),Q(2)).laplace_signature(Q(2,3)),
         'gamma_source_rate_selected_not_derived':True,
         'fractional_shape_is_physical_half_event':False,
      },
      'spectral':{
         'C2_row5':spectral,
         'parity_character_row5':parity_character(5,1,2,p),
         'parity_character_matches_cyclic_group_algebra':spectral[0]-spectral[1]==parity_character(5,1,2,p),
         'cyclic_convolution_n2_plus_n3':cyclic_convolve(residue_walk_law(2,2,1,2,p),residue_walk_law(3,2,1,2,p))==spectral,
      },
      'gamma':{
         'exp1_integer_moments_0_6':tuple(factorial(i) for i in range(7)),
         'positive_two_atom_moments_0_6':tuple(laguerre_two_atom_moment(i) for i in range(7)),
         'delta1_integer_moments_0_6':tuple(shifted_atomic_moment(i) for i in range(7)),
         'first_exp_vs_2atom_disagreement':next((i for i in range(7) if factorial(i)!=laguerre_two_atom_moment(i)),None),
         'exp_shift_unit_half_0_5':tuple(shifted_exponential_moment(n,Q(1,2)) for n in range(6)),
         'gamma_moment_ibp_identity_0_10':all(shifted_exponential_moment(n,Q(1,2))==shift_moment_recurrence(n,Q(1,2)) for n in range(11)),
         'generalized_half_row_0_7':tuple(generalized_binomial(Q(1,2),k) for k in range(8)),
         'generalized_half_row_has_negative_coefficient':generalized_binomial(Q(1,2),2)<0,
         'half_binomial_sum_z_half_cutoff18':val,
         'half_binomial_absolute_tail_bound':err,
         'independent_sqrt_3_over_2_exact_bracket':(low,high),
         'tail_interval_overlaps_exact_sqrt_bracket':val-err<=high and val+err>=low,
         'gamma_forced_by_pascal_geometry_alone':
              shifted_atomic_moment(2)==shifted_exponential_moment(2),
      },
      'scope':{
        'all_probabilities_exact_fraction':True,
        'finite_source_tables_declared_not_measured':True,
        'classical_Hopf_deFinetti_and_Gamma_context':True,
        'positive_exponential_moment_all_n_uniqueness_paper_proof_only':True,
        'arbitrary_analytic_completion_from_finite_integer_moments_claimed':False,
        'physical_source_authenticated':False,
        'real_90_degree_infinite_limit_constructed':False,
        'Weil_form_RH_claimed':False,
        'academic_priority_asserted':False,
      },
    })


def main():
    print(json.dumps(receipt(),sort_keys=True,indent=2))

if __name__=='__main__':main()
