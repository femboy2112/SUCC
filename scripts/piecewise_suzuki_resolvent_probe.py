"""Research receipt: exact analytic Suzuki integrals vs midpoint and K-Riesz gates."""
import json
from fractions import Fraction as F

from observational_succ.analytic_suzuki_schur_gate import CertifiedAnalyticSuzukiTrial
from observational_succ.source_direct_quotient_gate import CertifiedSourceDirectQuotientTrial
from observational_succ.source_riesz_high_comparison import coercivity_slack_no_go
from observational_succ.direct_quotient_schur import exact_psd
from observational_succ.contact_ladder_projection import exact_contact_low4_certificate
from observational_succ.source_schur_response_search import source_response_analytic_trial


def main():
    old=CertifiedSourceDirectQuotientTrial(J_deriv=2,grid=8,J_galerkin=64,rank=5)
    analytic=CertifiedAnalyticSuzukiTrial(J_deriv=2,J_galerkin=64,rank=5,digits=100,
                                         young_eta=F(1,8))
    oldq=tuple(tuple(F(x) for x in row) for row in old['quotient_loewner_upper'])
    newq=tuple(tuple(F(x) for x in row) for row in analytic['true_quotient_gram_upper'])
    difference=tuple(tuple(oldq[i][j]-newq[i][j] for j in range(4)) for i in range(4))
    diag_old=tuple(oldq[i][i] for i in range(4))
    diag_new=tuple(newq[i][i] for i in range(4))
    optimized=source_response_analytic_trial(rank=6,J_source=64,J_deriv=2)
    receipt={
        "source":"PINNED_SUZUKI_FIRST_PRIME",
        "base":"research/direct-quotient-pontryagin-transfer-2026-10-17",
        "certified_finite_J_analytic_no_grid":True,
        "old_midpoint_verdict":old["verdict"],
        "piecewise_analytic_verdict":analytic["verdict"],
        "old_quotient_upper_diagonal":tuple(str(x) for x in diag_old),
        "piecewise_quotient_upper_diagonal":tuple(str(x) for x in diag_new),
        "new_quotient_upper_is_below_old_in_Loewner":exact_psd(difference),
        "old_source_gate_verified":old.get("source_gate_passed",False),
        "new_source_gate_verified":analytic.get("source_passport_verified",False),
        "new_interval_quotient_radii":analytic["finite_quotient_gram_radius_parity"],
        "old_and_new_use_no_zeta_zero_coordinates":True,
        "new_analytic_schur_lower_positive":analytic["source_S4_lower_psd"],
        "operator_comparison_no_ghost":coercivity_slack_no_go(),
        "contact_low4_norms":tuple(str(exact_contact_low4_certificate()["gram"][i][i]) for i in range(4)),
        "finite_U_genuine_source_search":{
            "U":optimized["candidate"]["U"],
            "ridge":optimized["candidate"]["ridge"],
            "original_source_checked":optimized["genuine_S4_source_audited"],
            "authentic_first_window_verdict":optimized["genuine_first_window_verdict"],
            "RH_proved":False,
        },
        "RH_PROVED":False,
    }
    print(json.dumps(receipt,indent=2,default=str))


if __name__=="__main__":
    main()
