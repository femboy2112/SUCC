"""Two independent Gamma_SUCC transports; run with --verify for bounded probes."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F

from observational_succ.gamma_dirac_continuum import (
    GammaClock, alias_sum, compact_comb_pairing, direct_comb,
)


def receipt():
    import mpmath as mp
    integer_events=[]
    for q in (2,3,8,32):
        x=compact_comb_pairing(q)
        assert x["absolute_error"] <= x["proved_error_ceiling"]
        integer_events.append({"denominator":q, "sum":str(x["sum"]),
                               "signed_error":str(x["signed_error"]),
                               "proved_ceiling":str(x["proved_error_ceiling"])})
    results=[]
    with mp.workdps(75):
        for kind, sample in (("Gamma",mp.mpc('1','2')),
                             ("Gamma_R",mp.mpc('.5','6'))):
            clock=GammaClock(F(1,2),kind)
            x=direct_comb(sample,clock,left=-1400,right=65,dps=75)
            a=alias_sum(sample,clock,aliases=4,dps=75)
            diff=abs(a-x["clock_sum"])
            assert x["observed_absolute_error"] <= x["combined_upper"]
            assert diff < mp.mpf('1e-26'), (kind, diff)
            results.append({"kind":kind,
                            "direct_error":mp.nstr(x["observed_absolute_error"],9),
                            "analytic_upper":mp.nstr(x["combined_upper"],9),
                            "direct_vs_poisson_error":mp.nstr(diff,9)})
    pole=GammaClock(F(1,2),"Gamma_R").pole(1,1)
    assert pole["real_part"] == -2 and pole["imaginary_pi_multiplier"] == 8
    assert pole["residue_rational"] == -2 and pole["residue_pi_exponent"] == 1
    return {
        "schema":"SUCC_DIRAC_GAMMA_v1",
        "claim":"classical Gamma_R via two-sided weighted SUCC; spectral alias obstruction",
        "source":"discrete rational log-clock and authentic pi normalization",
        "status":"PROVED_PAPER_PLUS_EXACT_AND_NUMERICAL_CONTROLS",
        "weak_distribution_controls":integer_events,
        "independent_analytic_calibrations":results,
        "first_spurious_Gamma_R_pole":{
            "real_part":pole["real_part"],
            "imaginary_part":"8*pi",
            "residue":"-2*pi",
            "zeta_nonzero_by":"functional equation; Euler product at 3-8*pi*i",
        },
        "full_spectral_uniformity":False,
        "constructed_euler_product":False,
        "source_to_completed_Weil_sign":False,
        "RH_proved":False,
    }


if __name__ == "__main__":
    if sys.argv[1:] not in ([],["--verify"]):
        raise SystemExit("usage: python scripts/gamma_dirac_continuum_probe.py [--verify]")
    data=receipt()
    if sys.argv[1:] == ["--verify"]:
        print("DIRAC_GAMMA source-domain, exact comb and independent analytic checks: OK")
    else:
        print(json.dumps(data,indent=2,sort_keys=True))
