#!/usr/bin/env python3
"""Exact finite source-relative prime sundial calibration (not physical time)."""
import json
from fractions import Fraction
from itertools import product

from observational_succ.portable_prime_sundial import (
    PortablePrimeSundial as Dial, SundialContractError,
    representation_alias_pair,
)


def receipt() -> dict:
    a,b=representation_alias_pair()
    phase=a.phase_wheel(((2,3),(3,1),(5,1)))
    shadows=a.three_shadows()
    scaled=a.homogeneous_scale(2)
    rebuilt=Dial.reconstruct_three_shadows(
        shadows.origin,shadows.numerator_step,shadows.denominator_step,
        "new mathematical representative","canonical projective")
    assert a.projectively_equal(rebuilt)
    assert a.projectively_equal(scaled)
    assert (rebuilt.a,rebuilt.b,rebuilt.u,rebuilt.v)==(1,2,1,1)
    assert (scaled.a,scaled.b,scaled.u,scaled.v)==(2,4,2,2)
    rad=Dial.rad_anchored(12,18,"declared-integer-source")
    births=rad.rad_births(2,2)
    nonunit=Dial(1,2,2,2,"declared-integer-source","nonunit-even")
    stationary=Dial(6,10,3,5,"declared-integer-source","coprime-dir")
    sharp=Dial(1,20,3,5,"declared-integer-source","invertible")
    frames,clock_checks,aligned,refused=0,0,0,0
    # Oracle independently enumerates all n mod p^r, rather than
    # trusting the valuation-root congruence solver.
    for aa,bb,uu,vv in product(range(1,5),repeat=4):
        d=Dial(aa,bb,uu,vv,"finite-enumerated-source","source-unit")
        frames+=1
        for n in range(4):
            assert d.wedge(n,n)==d.determinant()
            assert d.determinant()%d.diagonal_gcd(n)==0
        for p,r in ((2,1),(2,2),(3,1),(5,1)):
            reading=d.prime_clock(p,r)
            M=p**r
            oracle=sum(1 for n in range(M)
                       if (aa+n*uu)%M==0 and (bb+n*vv)%M==0)
            assert reading.diagonal_count==oracle
            clock_checks+=1
            aligned+=int(oracle>0)
    for bad in (lambda:a.prime_clock(4),
                lambda:nonunit.phase_wheel(((2,1),))):
        try:
            bad()
        except SundialContractError:
            refused+=1
    M,n=sharp.invertible_determinant_part()
    assert (M,n)==(11,7)
    assert phase.phase_offset==119 and phase.wheel==120
    assert a.ratio(1,1)==Fraction(2,3) and b.ratio(1,1)==Fraction(3,5)
    assert rad.diagonal_gcd(2)==6
    assert stationary.stationary_gcd_rule(20)==(22,1)
    assert refused==2
    return {
      "status":"EXACT_FINITE_PORTABLE_SUNDIAL_SOURCE_CONTRACT",
      "parent":"SUCC Academic Main V source arithmetic (RAD/RIS, phase-clock, observer/descent)",
      "independent_frames_checked":frames,
      "prime_power_clock_readings_checked":clock_checks,
      "diagonal_prime_power_windows_nonempty":aligned,
      "invalid_source_or_clock_contracts_rejected":refused,
      "equal_initial_ratio_alias":{
          "fraction":str(a.ratio(0,0)),
          "first_next":str(a.ratio(1,1)),"second_next":str(b.ratio(1,1)),
          "D_first":a.determinant(),"D_second":b.determinant(),
      },
      "prime_phase_wheel":{
          "prime_depths":phase.prime_depths,"wheel":phase.wheel,
          "relative_phase":phase.phase_offset,
          "first_synchronized_k":phase.simultaneous_k,
          "first_synchronized_l":phase.simultaneous_l,
          "actual_arm_values":a.arms(phase.simultaneous_k,phase.simultaneous_l),
      },
      "rad_anchor":{
          "initial_arms":rad.arms(0,0),"units":(rad.u,rad.v),
          "determinant":rad.determinant(),
          "two_diagonal_steps":rad.arms(2,2),"gcd":rad.diagonal_gcd(2),
          "new_denominator_primes":births[1].new_prime_support,
          "rad_denominator":births[1].actual_radical,
          "ris_denominator":births[1].actual_residual,
      },
      "three_shadow_reconstruction":{
          "readings":[str(shadows.origin),str(shadows.numerator_step),
                      str(shadows.denominator_step)],
          "normalized":[str(shadows.normalized_a),str(shadows.normalized_u),
                        str(shadows.normalized_v)],
          "canonical_frame":[rebuilt.a,rebuilt.b,rebuilt.u,rebuilt.v],
          "homothetic_other_frame":[scaled.a,scaled.b,scaled.u,scaled.v],
          "ratio_paths_equivalent":a.projectively_equal(rebuilt),
          "original_integer_scale_authenticated":shadows.source_authenticated,
          "counterfactual_probe_access_authorized":shadows.counterfactual_probes_authorized,
      },
      "nonunit_prime_divides_D_but_cannot_cancel":{
          "D":nonunit.determinant(),"p":2,
          "numerator_clock_is_empty":nonunit.prime_clock(2).numerator_class is None,
          "diagonal_alignment_exists":nonunit.prime_clock(2).diagonal_class is not None,
      },
      "stationary":{
          "D":stationary.determinant(),
          "ratio_at_time_20":str(stationary.ratio(20,20)),
          "gcd_at_time_20":stationary.diagonal_gcd(20),
      },
      "sharp_prime_to_unit_part":{
          "D":sharp.determinant(),"M":M,"witness_n":n,
          "gcd_at_witness":sharp.diagonal_gcd(n),
      },
      "source_authenticated":False,"physical_time_model":False,
      "primality_inferred_from_phase":False,
      "new_academic_priority_established":False,
      "ABC_proved":False,"RH_proved":False,"signed_Weil_positive":False,
    }


if __name__=="__main__":
    print(json.dumps(receipt(),sort_keys=True,indent=2))
