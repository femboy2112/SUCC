"""Deterministic exact rational experiment receipt; no π digits or oracle."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from observational_succ.bbp_euler_mascheroni import (
    forcing, block_source, bbp_gamma_log_argument, source_endpoint_jets,
    mellin_first_jet_coefficient, valuation, log_linear_prime_coefficients,
    q_lambert_partial, q_lambert_tail_bound, divisor_count,
    multiplicative_order_16, prime_factorization,
)

REPO = Path(__file__).resolve().parents[3]
SOURCE = "original r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U0=0"


def exact_receipt() -> dict:
    cases=[]
    for g in (1,2,3,4,5,6,7,8,9,10,16):
        argument=bbp_gamma_log_argument(g)
        cases.append({"g":g,"blocked_first":str(block_source(g)),
                      "block_log_argument":str(argument),
                      "source_jets":[str(x) for x in source_endpoint_jets(g)],
                      "mellin_first_coefficient":str(mellin_first_jet_coefficient(g)),
                      "v3":valuation(argument,3),"v31":valuation(argument,31)})
    c8=bbp_gamma_log_argument(8)
    return {
        "schema":"succ-bbp-euler-mascheroni-v1",
        "scope":"exact rational source and q-Lambert finite; pi-normality OPEN",
        "source":SOURCE,
        "derivation_parent":"c0e5681762d0c13b38fb14a76937db17a9658e95 (#568)",
        "cases":cases,
        "special_source_terms":{"r7":str(forcing(7)),"r8":str(forcing(8)),
                                "r7_3adic":valuation(forcing(7),3),
                                "r8_31adic":valuation(forcing(8),31)},
        "g8_factorization":{"numerator":str(c8.numerator),
                            "denominator":str(c8.denominator),
                            "denominator_prime_powers":{str(p):e for p,e in prime_factorization(c8.denominator).items()}},
        "q_gamma_end_point":{"q":"1/16", "lambert_terms":16,
                             "lambert_partial":str(q_lambert_partial(16)),
                             "lambert_remaining_less_than":str(q_lambert_tail_bound(16)),
                             "ord_16_mod_31":multiplicative_order_16(31),
                             "ord_16_mod_27":multiplicative_order_16(27),
                             "divisor_tau_27":divisor_count(27),
                             "divisor_tau_31":divisor_count(31)},
        "proof_boundary":{"pi_to_source":"classical BBP identity imported",
                          "gamma_limit":"gamma - (1/2)log(4*pi)",
                          "all_epoch_signed_bound":"OPEN"},
        "module_sha256":hashlib.sha256((REPO/"observational_succ/bbp_euler_mascheroni.py").read_bytes()).hexdigest(),
        "test_sha256":hashlib.sha256((REPO/"tests/test_bbp_euler_mascheroni.py").read_bytes()).hexdigest(),
    }


def serialized_receipt() -> str:
    return json.dumps(exact_receipt(),ensure_ascii=False,indent=2,sort_keys=True)+"\n"

if __name__=="__main__":
    print(serialized_receipt(),end="")
