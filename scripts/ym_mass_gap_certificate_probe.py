"""Deterministic exact-rational / exact Q(i) YM mass-certificate TOY probe.

From the SUCC project root:
  PYTHONPATH=. python scripts/ym_mass_gap_certificate_probe.py

This uses no Wilson 4D measure, continuum limit, or imported Lean theorem.
"""
from fractions import Fraction as Q
import json

from observational_succ.ym_mass_gap_certificate import (
    GaussianQ, coherent_spectral_gram, gram_gap_at_one_time,
    hermitian_gap_at_one_time, spectral_gram, two_state_ratio,
    two_block_gap, weighted_block_gap, entrywise_error_gap,
)


def receipt():
    rows = []
    for n in (2, 8, 32, 128):
        row = {"mesh": f"1/{n}", "ticks_at_physical_time_1": n}
        for name in ("gapped", "gapless"):
            ratio = two_state_ratio(n, name)
            spectrum = (Q(1), ratio)
            bank = ((Q(0), Q(1)),)
            c0, ct = spectral_gram(spectrum, bank, 0), spectral_gram(spectrum, bank, n)
            row[name + "_transfer_ratio"] = str(ratio)
            row[name + "_macro_ratio"] = str(ct[0][0])
            row[name + "_q_two_thirds_pass"] = gram_gap_at_one_time(c0, ct, Q(2, 3))
        rows.append(row)

    n = 32
    spectrum = (Q(1), 1-Q(1, n*n), 1-Q(1, n))
    coarse = ((Q(0), Q(0), Q(1)),)
    complete = (coarse[0], (Q(0), Q(1), Q(0)))

    z = GaussianQ(Q(0), Q(1))
    bank = ((Q(0), Q(1), Q(1)), (Q(0), Q(1), z))
    eig = (Q(1), Q(1, 4), Q(2, 5))
    g0, gt = coherent_spectral_gram(eig, bank, 0), coherent_spectral_gram(eig, bank, 1)

    return {
        "scope": "finite exact toy semigroups only; actual Yang--Mills gap OPEN",
        "physical_time": "1",
        "cutoffs": rows,
        "incomplete_bank_q_half_pass": gram_gap_at_one_time(
            spectral_gram(spectrum, coarse, 0), spectral_gram(spectrum, coarse, n), Q(1,2)),
        "complete_bank_q_half_pass": gram_gap_at_one_time(
            spectral_gram(spectrum, complete, 0), spectral_gram(spectrum, complete, n), Q(1,2)),
        "two_block_strict": two_block_gap(Q(2,5), Q(3,5), Q(1,10)),
        "two_block_q_seven_tenths": weighted_block_gap(
            Q(2,5), Q(3,5), Q(1,10), Q(1), Q(1), Q(7,10)),
        "coherent_detail_massless_mutant_pass": two_block_gap(Q(3,5), Q(3,5), Q(2,5)),
        "coherent_qi_cross_t1": str(gt[0][1].re) + "+" + str(gt[0][1].im) + "i",
        "coherent_qi_q_half_pass": hermitian_gap_at_one_time(g0, gt, Q(1,2)),
        "coherent_qi_q_third_pass": hermitian_gap_at_one_time(g0, gt, Q(1,3)),
        "margin_safe": entrywise_error_gap(
            ((Q(1),),), ((Q(1,2),),), Q(3,4), Q(0), Q(1,10)),
        "margin_unsafe": entrywise_error_gap(
            ((Q(1),),), ((Q(1,2),),), Q(3,4), Q(0), Q(3,10)),
    }


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, sort_keys=True))
