"""Reproducible finite-window counterexample; no infinite randomness oracle."""
import argparse
import json
from observational_succ.maximal_novelty_source import (
    maximal_window_periodic_witness, program_count_bound,
    rooted_cycle_factor_possible, full_binary_shift_has_cyclic_factor,
)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--verify", action="store_true")
    args = p.parse_args()
    observations = [maximal_window_periodic_witness(k) for k in range(1, 7)]
    if args.verify:
        assert [x["global_source_period"] for x in observations] == [2, 4, 8, 16, 32, 64]
        assert observations[3]["period_bits"] == "0000100110101111"
        assert all(x["all_order_k_blocks_exactly_once_per_cycle"] for x in observations)
        assert all(not x["globally_aperiodic"] for x in observations)
        assert program_count_bound(10, 3)[
            "maximum_strings_describable_below_length_minus_deficiency"] == 127
        assert rooted_cycle_factor_possible(16, 8)
        assert not rooted_cycle_factor_possible(16, 3)
        assert not full_binary_shift_has_cyclic_factor(2)
    print(json.dumps({
        "claim": "MAXIMAL_FINITE_BLOCK_NOVELTY_NOT_MAXIMAL_SOURCE_COMPLEXITY",
        "checks": observations,
        "Martin_Lof_random_source_constructed": False,
        "RH_proved": False,
        "verification": "PASS" if args.verify else "UNVERIFIED",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
