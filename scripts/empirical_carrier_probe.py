"""Reproduce source-qualified, exact finite checks for the carrier proposal.

Run from repo root: python scripts/empirical_carrier_probe.py
No physical collision simulation or experimental measurement is performed.
"""

import sys
import json
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.scalar_circle_spectral import (
    CircleScalar, massless_zeta_tail_bound, poisson_theta_direct, poisson_theta_dual,
)
from observational_succ.empirical_carrier import (
    HiggsChannel, RateFactorization, angular_even_moment, audit_higgs_scale,
    compatible_angular_carriers, calibrated_angular_dimension,
    finite_euler_coefficients, gaussian_radial_mellin, gram_example,
    gram_positive_definite, local_shell_factor, quantum_rate_signature,
    quantum_triangle_phase, rate_reparameterize,normalized_archimedean_mellin,
)


def to_string(x):
    if isinstance(x,Q):
        return str(x)
    if isinstance(x,dict):
        return {str(k):to_string(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [to_string(v) for v in x]
    return x


def probe():
    ch=(HiggsChannel('fermion_F','fermion',Q(3),Q(1,4),'declared-toy',0),
        HiggsChannel('vector_V','vector',Q(6),Q(6),'declared-toy',0))
    mutated=(ch[0],HiggsChannel('vector_V','vector',Q(6),Q(8),'declared-toy',0))
    h=audit_higgs_scale(ch)
    bad=audit_higgs_scale(mutated)
    assert h.compatible and not bad.compatible

    raw3=angular_even_moment(3,1)
    observed=angular_even_moment(5,1)
    shadows=compatible_angular_carriers(observed)
    assert shadows==((5,0),(3,1)) and calibrated_angular_dimension(observed,1)==3
    # A(u)=1-u² for d=3; all shape moments of the *accepted* density agree with d=5.
    all_moments=[str(Q(3,(2*j+1)*(2*j+3))) for j in range(10)]
    assert all_moments==[str(angular_even_moment(5,j)) for j in range(10)]

    w=RateFactorization((Q(1),Q(2)),(Q(3),Q(4)),(Q(1,2),Q(1,4)))
    w2=rate_reparameterize(w,(Q(3,2),Q(7,3)))
    assert w.observations==w2.observations

    plus,minus=gram_example(1),gram_example(-1)
    assert gram_positive_definite(plus) and gram_positive_definite(minus)
    assert quantum_rate_signature(plus)==quantum_rate_signature(minus)
    assert quantum_triangle_phase(plus)!=quantum_triangle_phase(minus)

    prime=finite_euler_coefficients((2,3),36)
    composite=finite_euler_coefficients((2,3,6),36,enforce_primes=False)
    assert prime[6]==1 and composite[6]==2 and composite[36]==3

    # 2026 ATLAS published CENTRAL VALUES only: 3.65 fb vs 3.68 fb,
    # source at https://cds.cern.ch/record/2957352; not refit from collision events.
    atlas_ratio=Q(365,368)
    zero=CircleScalar('declared-circle',0,Q(0),Q(1))
    massive=CircleScalar('declared-circle',0,Q(1),Q(1))
    assert zero.truncated_spectral_zeta(1,12,nonzero_modes_only=True)==zero.massless_dirichlet_truncation(1,12)
    assert zero.multiplicative_two_three_defect()==0
    assert massive.multiplicative_two_three_defect()==-6
    heat_direct=poisson_theta_direct(1.,1.,12)
    heat_dual=poisson_theta_dual(1.,1.,12)
    assert abs(heat_direct-heat_dual)<1e-12
    return to_string({
        'title':'EMPIRICAL_CARRIER_HIGGS_SPECTRAL_RECEIPT',
        'empirical_input':{
            'source':'ATLAS Collaboration, CERN document 2957352, March 2026',
            'url':'https://cds.cern.ch/record/2957352',
            'observable':'H -> ZZ* -> 4 leptons fiducial cross-section, 13.6 TeV',
            'reported_fiducial_fb':'3.65 (+0.35/-0.33)',
            'reported_SM_fiducial_fb':'3.68 +/- 0.17',
            'central_ratio_only':atlas_ratio,
            'full_systematics_and_correlations_reanalyzed':False,
            'direct_coupling_or_universal_carrier_identified':False,
        },
        'higgs_cross_sector':{
            'toy_data_not_empirical':True,
            'source_id':h.source_id,
            'common_v':h.scales[0],
            'different_sectors':h.cross_sector,
            'pass_same_v':h.compatible,
            'mutated_v_values':bad.scales,
            'mutated_pass':bad.compatible,
            'mutated_witness':bad.first_conflict,
        },
        'angular_detector_alias':{
            'true_d':3,'accepted_histogram_looks_like_d':5,
            'unaccepted_second_moment':raw3,'accepted_second_moment':observed,
            'rivals_d_k':shadows,'independently_calibrated_k':1,
            'reconstructed_d_after_calibration':calibrated_angular_dimension(observed,1),
            'first_ten_accepted_even_moments':all_moments,
            'actual_detector_calibration_performed':False,
        },
        'rate_factorization_gauge':{
            'original_rates':w.observations,'reparameterized_rates':w2.observations,
            'different_phase_space':w.phase_space!=w2.phase_space,
            'different_amplitudes':w.amplitude_sq!=w2.amplitude_sq,
        },
        'quantum_state_gram':{
            'both_psd':gram_positive_definite(plus) and gram_positive_definite(minus),
            'pairwise_rates_both':quantum_rate_signature(plus),
            'triangle_plus':quantum_triangle_phase(plus),
            'triangle_minus':quantum_triangle_phase(minus),
            'actual_interferometric_readout_performed':False,
        },
        'archimedean_and_local':{
            'real_gaussian_mellin_d1_s1':gaussian_radial_mellin(1,1),
            'real_gaussian_mellin_d2_s2':gaussian_radial_mellin(2,2),
            'real_3d_integral_s2':gaussian_radial_mellin(3,2),
            'arch_factor_from_3d_s2':normalized_archimedean_mellin(3,2),
            'p2_local_factor_s2':local_shell_factor(2,2),
            'p3_local_factor_s2':local_shell_factor(3,2),
            'p6_fake_formal_factor_s2':local_shell_factor(6,2,prime_required=False),
            'legitimate_coefficient_n6':prime[6],
            'fake_euler_coefficient_n6':composite[6],
            'fake_euler_coefficient_n36':composite[36],
        },
        'scalar_circle_spectral':{
            'source_id':'declared-circle',
            'circle_exists_as_actual_physical_Higgs_compactification':False,
            'massless_mode_eigenvalues_n1_n2_n3':[
                zero.eigenvalue(n) for n in (1,2,3)],
            'massive_mode_eigenvalues_n1_n2_n3':[
                massive.eigenvalue(n) for n in (1,2,3)],
            'massless_mode_zeta_s1_cutoff12':zero.massless_dirichlet_truncation(1,12),
            'massless_spectral_sum_s1_cutoff12':zero.truncated_spectral_zeta(1,12,nonzero_modes_only=True),
            'massless_integral_tail_bound':massless_zeta_tail_bound(1,12),
            'massless_normalized_multiplicativity_defect':zero.multiplicative_two_three_defect(),
            'massive_normalized_multiplicativity_defect':massive.multiplicative_two_three_defect(),
            'positive_mass_invalidates_native_euler_product':True,
            'heat_theta_at_t1_direct_float':heat_direct,
            'heat_theta_at_t1_dual_float':heat_dual,
            'nontrivial_zeros_used':False,
        },
        'claim_firewalls':{
            'physically_universal_carrier_constructed':False,
            'higgs_explains_all_mass':False,
            'prime_source_derived_from_physical_phase_space':False,
            'completed_Weil_form_identified':False,
            'RH_proved':False,
            'nontrivial_zeta_zero_inputs':False,
            'all_quantitative_toy_certificates_exact_rational_except_labeled_gamma_diagnostic':True,
        },
    })


def main():
    value=probe()
    path=Path(__file__).resolve().parents[1]/'research/2026-10-13/EMPIRICAL_CARRIER_RECEIPT.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
    print(json.dumps(value,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
