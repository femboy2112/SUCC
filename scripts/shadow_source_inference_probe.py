#!/usr/bin/env python3
"""Deterministic, exact, independently replayable Shadow-SUCC certificates.

The analytic identities in the dossier (Hermite Fourier and Gamma Mellin)
are classical theorems; this script verifies their exact rational ingredients.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from fractions import Fraction as Q

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.shadow_source_inference import (
    ShadowCarrier,minimal_shadow_probe_design,receding_shadow_escape,
    shadow_claim_error_budget,verify_shadow_base_change)
from observational_succ.shadow_archimedean_tests import (
    GaussianScaleShadow,construct_hermite_impostor,
    explicit_positive_hermite_multiplier)
from observational_succ.shadow_zero_divisor import (
    distinct_prime_scale_shadows,offcritical_vs_line_shadow,
    two_prime_shadow_conditioning_obstruction,
    construct_global_polynomial_from_shadows)


def clean(x):
    if type(x) is Q:return str(x)
    if type(x) is tuple or type(x) is list:return [clean(z) for z in x]
    if type(x) is dict:return {k:clean(v) for k,v in x.items()}
    return x


def report():
    carrier=ShadowCarrier('one-source',0,'linear-forms',3)
    a=carrier.report('E_A','Alice',(1,0,0),4)
    b=carrier.report('E_B','Bob',(0,1,0),-3)
    before=carrier.shadow_fucc((a,),(1,1,0))
    after=carrier.shadow_fucc((a,b),(1,1,0))
    assert before['status']=='UNRESOLVED' and after['status']=='PROVED'
    assert after['claim']==1
    f=GaussianScaleShadow('scale-2-positive',(Q(2),Q(1,2)),(Q(1,3),Q(2,3)))
    reference=GaussianScaleShadow('canonical',(Q(1),),(Q(1),))
    fake=construct_hermite_impostor((2,4,6),(Q(1,4),Q(1),Q(2)))
    other=offcritical_vs_line_shadow(Q(10,11)).certificate()
    source_infinite=receding_shadow_escape(100)
    constructed=construct_global_polynomial_from_shadows(
        (-1,1),(1,1),(-1,1,-1,1),(1,1,1,1))
    assert constructed['global_polynomial']==(1,0,1)
    out={
      'status':'CLASSICAL CONDITIONAL SHADOW THEOREMS WITH EXACT FINITE CERTIFICATES',
      'empirical_source_authenticated':False,
      'finite_shadow_fucc':{'unresolved_countermodel':before,
                             'proved_after_cross_tower':after,
                             'minimal_design':minimal_shadow_probe_design(
                                 ((1,0,0),(0,1,0),(1,1,0)),(1,1,0)),
                             'error_budget':shadow_claim_error_budget((Q(1),Q(1)),
                                                                   (Q(1,10),Q(1,20))),
                             'source_restriction_nonconverse':verify_shadow_base_change(
                                 ((1,0),),(0,1),((1,),(1,)))},
      'gaussian_mixture_selection':f.moment_shadow(),
      'canonical_mixture':reference.moment_shadow(),
      'finite_hermite_impostor':{
          'degree':len(fake.polynomial)-1,
          'Mellin_probes':fake.sampled_moments,
          'point_probes_y':fake.sampled_y,
          'normalization_and_fourier_claims':fake.checks(),
          'Mellin_C2_of_EXPLICIT_noncanonical_example':explicit_positive_hermite_multiplier(2),
          'Mellin_C4_of_EXPLICIT_noncanonical_example':explicit_positive_hermite_multiplier(4),
      },
      'construct_global_from_compatible_analytic_shadows':constructed,
      'common_zero_divisor':{
          'prime_scale_pair':distinct_prime_scale_shadows(2,3).certificate(),
          'off_line_vs_on_line':other,
          'global_decoder_instability':two_prime_shadow_conditioning_obstruction(2,3)},
      'finite_source_escape':source_infinite,
      'RH_or_Weil_positivity_proved':False,
      'canonical_real_gamma_from_finite_primes_alone':False,
      'warning':'Selected test vector != canonical local gamma DISTRIBUTION on whole test space',
    }
    assert out['common_zero_divisor']['global_decoder_instability'][
               'global_uniformly_bounded_bezout_decoder_exists'] is False
    return clean(out)

if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
