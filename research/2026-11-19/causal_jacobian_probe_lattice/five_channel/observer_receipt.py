"""Reproduce the exact finite observer, retained-history and repair receipts."""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import observer as o


def run():
    clocks = (55, 89, 144, 233)
    journal = o.make_journal(233)
    assert o.validate_journal(journal, authentic=True)
    snapshot = o.observe(journal, clocks)
    coefficients, seed = o.recover(snapshot)
    assert coefficients == o.BBP_COEFFICIENTS and seed == 0
    source_hash = sha256("\n".join(map(str, journal.states)).encode()).hexdigest()
    charts = []
    for p in (2, 3, 5, 7, 11):
        c = o.prime_chart(clocks, p)
        charts.append({"prime": p, "row_exponents": c.exponents,
                       "rank_mod_p": c.rank, "source_inverse_loss": c.loss,
                       "five_channel_budget_for_three_digits":
                       o.five_channel_budget(c, 233, 3)})
    old_repair = o.observe(journal, (55, 89, 147, 233))
    assert o.recover(old_repair) == (coefficients, seed)
    plan = o.plan_universal_repair(clocks)
    repaired_journal = o.advance(journal, max(plan.basis_clocks)-journal.horizon)
    assert repaired_journal.states[:len(journal.states)] == journal.states
    repaired_snapshot = o.observe(repaired_journal, plan.basis_clocks)
    assert o.recover(repaired_snapshot) == (coefficients, seed)
    matrix = o.cleared_cauchy_matrix(plan.basis_clocks)
    determinant = o.determinant(matrix)
    assert determinant == 2**19
    report = {
        "status": "EXACT_FINITE_SOURCE_OBSERVER",
        "scope": "four-pole coefficient family plus unwrapped seed",
        "normality_proved": False,
        "R0_proved": False,
        "horizon": journal.horizon,
        "clocks": clocks,
        "innovations": list(map(str, snapshot.innovations)),
        "normalized_unwrapped_anchor": str(snapshot.anchor),
        "recovered_coefficients": list(map(str, coefficients)),
        "recovered_seed": str(seed),
        "full_rational_journal_sha256": source_hash,
        "fibonacci_determinant_gain": str(
            o.cauchy_determinant(clocks)/o.cauchy_determinant((55, 56, 57, 58))),
        "original_prime_charts": charts,
        "retrospective_repair": {"present_time": 233,
                                 "clocks": old_repair.clocks,
                                 "source_time_reversed": False},
        "universal_forward_repair": {
            "clocks": plan.basis_clocks,
            "history": plan.history,
            "new_horizon": repaired_journal.horizon,
            "old_history_preserved": True,
            "row_lcms": o.row_denominator_lcms(plan.basis_clocks),
            "integer_matrix": [[str(x) for x in row] for row in matrix],
            "determinant": str(determinant),
            "smith_form_by_theorem": [1, 4, 64, 2048],
            "binary_extra_source_digits": 11,
            "odd_prime_inverse_loss_by_theorem": 0,
            "fifth_channel_budget_is_separate": True,
        },
    }
    path = Path(__file__).resolve().parent/"receipts"/"observer.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(report, indent=2)+"\n")
    return report


if __name__ == "__main__":
    r = run()
    print(json.dumps({"status": r["status"],
                      "coefficients": r["recovered_coefficients"],
                      "seed": r["recovered_seed"],
                      "universal_clocks": r["universal_forward_repair"]["clocks"],
                      "integer_determinant": r["universal_forward_repair"]["determinant"]},
                     indent=2))
