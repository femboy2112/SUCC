"""Exact target filters for finite original-zero BBP shells.

Integer interval arithmetic, no supplied pi digits, floating trigonometry,
or extrapolation. Source identity is the repository's classical BBP import.
See PI_FILTERS.md for the rounding and signed-gap proofs.
"""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


SOURCE = "r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2);U0=0"
PARENT = "db9fb4b84672050efa79b13377f1e73364598a14"
SHELLS = (32, 64, 137, 271, 547, 1091)
RESOLUTIONS = (16, 32, 64)


def natural(value: int, name: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def forcing(n: int) -> F:
    """Combined polynomial form; independently checked against four poles."""
    natural(n, "n", 1)
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def source_tail_bound(n: int) -> F:
    natural(n, "n")
    return F(47, 225*(n+1)**2)


def raw_intervals(last: int, guard_bits: int = 48):
    """Yield (n, low, width, scale) for a closed circular enclosure of {U_n}.

    The interval is [low/scale,(low+width)/scale] modulo one. It may straddle
    zero. Width is propagated, never silently reset after modular reduction.
    scale=2**(4*last+guard_bits); width/scale < 2**(-guard_bits)/15.
    """
    natural(last, "last")
    natural(guard_bits, "guard_bits", 1)
    scale = 1 << (4*last + guard_bits)
    low = width = 0
    yield 0, low, width, scale
    for n in range(1, last+1):
        num = 120*n*n-89*n+16
        den = (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        floor_r, rem = divmod(scale*num, den)
        low = (16*low + floor_r) % scale
        width = 16*width + int(rem != 0)
        yield n, low, width, scale


def contains_circle(value: F, low: int, width: int, scale: int) -> bool:
    if type(value) not in (int, F):
        raise ValueError("exact rational phase required")
    return (F(value)*scale-low) % scale <= width


def certified_cell(low: int, width: int, scale: int, q: int):
    """Return the one certified half-open cell, or None at unresolved seams."""
    natural(q, "q", 2)
    for value, label in ((low, "low"), (width, "width"), (scale, "scale")):
        natural(value, label, int(label == "scale"))
    if low >= scale:
        raise ValueError("low must be the reduced representative")
    first, last = q*low//scale, q*(low+width)//scale
    return first if first == last and 0 <= first < q else None


def cell_minorant(a: int, q: int) -> F:
    """inf of 8*dist(x,Z)^2 over the closed q-cell."""
    natural(q, "q", 2)
    natural(a, "cell")
    if a >= q:
        raise ValueError("cell out of range")
    return 8*F(min(a, q-a-1), q)**2


def gap_from_counts(counts, ambiguous: int, shell: int) -> dict:
    """Lower certificate for 1-Re W_B(1) of the completed original-zero orbit.

    Counts must come from authenticated interval data to support a source
    claim. This function alone merely checks the count shape and arithmetic.
    """
    natural(shell, "shell", 1)
    natural(ambiguous, "ambiguous")
    if not isinstance(counts, (tuple, list)) or len(counts) < 2:
        raise ValueError("at least two cells required")
    for x in counts:
        natural(x, "count")
    if sum(counts)+ambiguous != shell:
        raise ValueError("counts plus unresolved mass must equal the shell")
    q = len(counts)
    raw = sum((count*cell_minorant(a, q) for a, count in enumerate(counts)), F())/shell
    payment = 8*source_tail_bound(shell)
    lower = max(F(), raw-payment)
    return {"shell": shell, "q": q, "counts": list(counts),
            "ambiguous": ambiguous, "raw_minorant": str(raw),
            "tail_payment": str(payment), "signed_gap_lower": str(lower)}


def run_shells(shells=SHELLS, resolutions=RESOLUTIONS, guard_bits: int = 48) -> dict:
    if not isinstance(shells, (tuple, list)) or not shells:
        raise ValueError("nonempty shell list required")
    if not isinstance(resolutions, (tuple, list)) or not resolutions:
        raise ValueError("nonempty resolution list required")
    for b in shells:
        natural(b, "shell", 1)
    for q in resolutions:
        natural(q, "q", 2)
    natural(guard_bits, "guard_bits", 1)
    if len(set(shells)) != len(shells) or len(set(resolutions)) != len(resolutions):
        raise ValueError("duplicate shell/resolution")
    bins = {(b,q): [0]*q for b in shells for q in resolutions}
    unknown = {(b,q): 0 for b in shells for q in resolutions}
    last = 2*max(shells)-1
    for n, low, width, scale in raw_intervals(last, guard_bits):
        for b in shells:
            if b <= n < 2*b:
                for q in resolutions:
                    a = certified_cell(low, width, scale, q)
                    if a is None:
                        unknown[b,q] += 1
                    else:
                        bins[b,q][a] += 1
    entries = [gap_from_counts(bins[b,q], unknown[b,q], b)
               for b in shells for q in resolutions]
    return {"source": SOURCE, "seed": "0", "parent": PARENT,
            "authority": "VERIFIED_FINITE_ONLY", "guard_bits": guard_bits,
            "last_index": last, "scale_bits": 4*last+guard_bits,
            "interval_width_strict_bound": str(F(1, 15*(1 << guard_bits))),
            "shells": list(shells), "resolutions": list(resolutions),
            "entries": entries, "uniform_R0_proved": False,
            "pi_normality_proved": False}


def verify_receipt(receipt: dict) -> bool:
    """Recompute the source, intervals and every bound; reject metadata mutants."""
    try:
        expected = run_shells(receipt["shells"], receipt["resolutions"], receipt["guard_bits"])
        return json.dumps(receipt, sort_keys=True, allow_nan=False) == json.dumps(
            expected, sort_keys=True, allow_nan=False)
    except (KeyError, TypeError, ValueError, OverflowError):
        return False


def main():
    result = run_shells()
    path = Path(__file__).with_name("PI_RESULTS.json")
    text = json.dumps(result, indent=2, sort_keys=True)+"\n"
    path.write_text(text)
    print(json.dumps({"artifact": path.name, "sha256": sha256(text.encode()).hexdigest(),
                      "shells": len(SHELLS), "filters_per_shell": len(RESOLUTIONS),
                      "ambiguous_total": sum(x["ambiguous"] for x in result["entries"]),
                      "uniform_R0_proved": False}, sort_keys=True))


if __name__ == "__main__":
    main()
