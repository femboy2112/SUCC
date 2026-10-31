"""Independent numerical check of exact finite receipts, not their authority.

Reads emitted intervals; does not import any BBP or interval implementation.
The numerical reference is mpmath's pi at 1400 decimal digits, then 100-digit
character evaluation. No numerical value is used to construct the certificate.
"""
import json
from pathlib import Path
import mpmath as mp


def main():
    receipt = json.loads((Path(__file__).parent / "receipts/finite-circle.log").read_text())
    mp.mp.dps = 1400
    phase = mp.frac(mp.pi)
    phases = []
    for _ in range(1024):
        phases.append(phase)
        phase = mp.frac(16*phase)
    counts = []
    for table in receipt["occupancy"]:
        actual = [0]*table["bins"]
        for x in phases:
            actual[int(mp.floor(table["bins"]*x))] += 1
        assert table["ambiguous"] == []
        assert actual == table["lower"] == table["upper"]
        counts.append({"bins": table["bins"], "checked": sum(actual)})
    mp.mp.dps = 100
    cache = {h: [mp.exp(2j*mp.pi*h*x) for x in phases] for h in range(1,17)}
    largest = {"upper_millionths": -1}
    for row in receipt["fourier"]:
        z = sum(cache[row["h"]][row["start"]-1:row["end"]])
        scale = row["scale"]
        for part, bounds in ((z.real,row["real_interval_units"]),(z.imag,row["imag_interval_units"])):
            assert mp.mpf(bounds[0])/scale <= part <= mp.mpf(bounds[1])/scale
        if row["normalized_modulus_millionths"][1] > largest["upper_millionths"]:
            largest = {"start": row["start"], "end": row["end"], "h": row["h"],
                       "upper_millionths": row["normalized_modulus_millionths"][1]}
    print(json.dumps({"status": "PASS_NUMERICAL_CROSSCHECK_ONLY", "pi_decimal_precision": 1400,
                      "character_decimal_precision":100,"complex_rectangles_checked":len(receipt["fourier"]),
                      "bin_tables":counts,"largest_certified_mean":largest,
                      "authority": "Exact certificate comes from separate integer intervals and BBP tail, not mpmath"},indent=2))


if __name__ == "__main__":
    main()
