"""Original real-Gamma infinite boundary: exact rational and source-only probe."""
import argparse
import json
from fractions import Fraction as F
from observational_succ.infinite_gamma_carleman import (
    alpha, finite_geometric, dyadic_nonnorm_witness,
    analytic_gamma_kernel_window, h01_tail_bound,
    original_source_infinite_gamma_contract,
)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",action="store_true")
    p.add_argument("--verify",action="store_true")
    a=p.parse_args()
    nonnorm=[dyadic_nonnorm_witness(j) for j in (1,8,64,189,1024)]
    h01=[h01_tail_bound(j) for j in (8,64,189,1024)]
    g=[finite_geometric(F(1,2),n) for n in (1,2,8,32)]
    source=original_source_infinite_gamma_contract() if a.source else None
    window=analytic_gamma_kernel_window(F(1,256),64)
    if a.verify:
        assert all(F(z["tail_cross_block_lower"])>=F(3,32) for z in nonnorm)
        assert all(not z["source_S4_positive_proved"] for z in h01)
        assert all(x["exact_equal"] for x in g)
        assert F(window["tail_lower"])>0
        assert [alpha(j+1)-alpha(j) for j in range(20)]==[F(2)]*20
        if a.source:
            assert source["source_git_blob"]=="0cc8510b71d178fc79e8d410a86d8b6014cf9178"
            assert source["true_prime_power"]==((2,2),)
            assert source["RH_proved"] is False
    print(json.dumps({
        "program":"INFINITE_GAMMA_CARLEMAN_BOUNDARY_2026_10_18",
        "finite_geometric_exact_controls":g,
        "rational_series_holdout":window,
        "uniform_operator_nonnorm_witnesses":nonnorm,
        "H01_form_tail_budgets":h01,
        "source":source,
        "original_S4_positive_proved":False,
        "RH_proved":False,
        "verification":"PASS" if a.verify else "UNVERIFIED",
    },sort_keys=True))


if __name__=="__main__":
    main()
