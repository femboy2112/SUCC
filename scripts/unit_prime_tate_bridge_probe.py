"""Fast source-typed arithmetic receipt; no global theorem by finite enumeration."""
from fractions import Fraction as Q
import json
from observational_succ.tate_idelic_zeta import StandardTateSource
from observational_succ.unit_prime_tate_bridge import (
    completed_tate_clock, source_prime_stage, finite_prime_current,
    archimedean_even_source, local_prime_occupation,
    scalar_gaussian_rescaling, finite_coherent_vs_diagonal_gibbs,
    prime_variance_tail_bound, diagonal_norm_unit,
)

def main():
    source=StandardTateSource("unit-prime-Tate-probe",0)
    results=[]
    for P in (3,5,11):
        finite=source_prime_stage(source,P,2,shell_depth=6)
        completed=completed_tate_clock(source,P,2)
        assert finite["stage_zeta"]<=completed["zeta_interval"][1]
        assert completed["completed_Lambda_interval"].lo>0
        assert completed["polar_zero_modes"]==(-1,1)
        results.append({
            "P":P,
            "zeta_stage":str(finite["stage_zeta"]),
            "zeta_tail":str(completed["zeta_interval"][1]-finite["stage_zeta"]),
            "prime_current_tail":str(finite_prime_current(
                source,P,2)["source_von_Mangoldt_tail_upper"]),
            "variance_tail":str(prime_variance_tail_bound(P,2)),
        })
    assert local_prime_occupation(2,2)["mean_valuation"]==Q(1,3)
    assert archimedean_even_source(source,2)["gamma_pi_monomial"]==(1,-1)
    assert scalar_gaussian_rescaling(2,4)["new_to_canonical_Mellin_ratio"]==Q(1,4)
    assert finite_coherent_vs_diagonal_gibbs(2)["pure_exchange_expectation"]==Q(4,5)
    assert diagonal_norm_unit(Q(-7,12))==1
    print(json.dumps({
        "schema":"UPT_SOURCE_BRIDGE_V1","stages":results,
        "finite_exact_tests_only":True,
        "analytic_theorem_in_research_dossier":True,
        "Weil_sign_proved":False,"RH_proved":False
    },indent=2))

if __name__=="__main__":
    main()
