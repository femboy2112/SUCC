"""Compare exact certificate boxes to the separately generated numeric oracle.

The numerical oracle is a diagnostic only; analytic rational enclosures carry
certificate authority. Also replay the finite source-frame equalities exactly.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.duck_bbp import forcing, lifted_orbit, tail_interval


def main():
    folder = Path(__file__).with_name("receipts")
    certified = json.loads((folder / "certified_gram.json").read_text())["results"]
    numeric = json.loads((folder / "oracle.json").read_text())["cases"]
    oracle = {(r["start"], r["degree"]): r for r in numeric}
    entries = 0
    for cert in certified:
        ref = oracle[(cert["start"], cert["degree"])]
        assert Q(cert["eigenvalue_lower"]) <= Q(ref["eigenvalues_numerical"][0])
        for row, other in zip(cert["gram"], ref["gram"]):
            for box, number in zip(row, other):
                assert Q(box["real_low"]) <= Q(number["real"]) <= Q(box["real_high"])
                assert Q(box["imag_low"]) <= Q(number["imag"]) <= Q(box["imag_high"])
                entries += 1
    frames = 0
    rejected_mutations = 0
    for n in (0, 1, 7, 31, 89):
        for d in range(1, 8):
            t = tail_interval(n, d)[0]
            next_same = tail_interval(n+1, d)[0]
            next_common = tail_interval(n+1, d-1)[0]
            seam = 16*t-next_same-forcing(n+1)
            assert seam == -forcing(n+d+1)/16**d
            assert 16*t-next_common-forcing(n+1) == 0
            assert lifted_orbit(n)+t == 16**n*tail_interval(0, n+d)[0]
            frames += 3
            # Replacing the fixed-depth seam by zero is an explicit false mutant.
            assert seam != 0
            rejected_mutations += 1
    # The 15-cycle x=1/225 has a rank-one phase Hankel despite (CH).
    # Check the rational exponents exactly; the stated rank and cosine margin
    # follow from the written character identities, without rounded trig.
    cycle_checks = 0
    for n in range(15):
        assert pow(16, n, 225) == (1 + 15*n) % 225
        for j in range(6):
            phase = Q(pow(16, n+j, 225), 225)
            base = Q(pow(16, n, 225), 225)
            assert (phase - base - Q(j, 15)).denominator == 1
            cycle_checks += 1
        assert (15*Q(pow(16, n, 225), 225) - Q(1, 15)).denominator == 1
        cycle_checks += 1
    result = {
        "certificate_cases": len(certified),
        "numerical_complex_entries_inside_certified_boxes": entries,
        "exact_source_frame_equalities": frames,
        "fixed_depth_zero_seam_mutations_rejected": rejected_mutations,
        "rank_one_CH_cycle_exact_character_identities": cycle_checks,
        "scope": "finite different-method checks within one model family; no asymptotic inference",
    }
    (folder / "crosscheck.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
