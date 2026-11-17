#!/usr/bin/env python3
"""Independent replay: literal four taps, backward Horner, hexadecimal slicing.

This verifier imports no computation from endpoint_shell_certificate.py.
The mathematical tail/interval proof is separately supplied in the manuscript.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path


def source(j):
    return F(4, 8*j-7)-F(2, 8*j-4)-F(1, 8*j-3)-F(1, 8*j-2)


def replay(path):
    data = json.loads(Path(path).read_text())
    b0, b1 = data["min_shell"], data["max_shell"]
    digits, n = data["grid_digits"], data["source_depth"]
    assert n == 2*b1 + digits
    assert data["shell_count"] == b1-b0+1
    q = 16**digits
    assert q == data["grid_denominator"]
    # Reverse source summation, independently from the forward U recurrence.
    prefix = F(0)
    for j in range(n, 0, -1):
        prefix = (prefix + source(j))/16
    u = prefix * 16**n
    digest = hashlib.sha256(f"{u.numerator:x}/{u.denominator:x}".encode()).hexdigest()
    assert digest == data["endpoint_sha256_hex_fraction"]
    assert str(source(n+1)/15) == data["tail_upper"]
    assert 0 < source(n+1)/15 < 1
    c = u.numerator//u.denominator
    digit_text = f"{c:0{n}x}"
    assert len(digit_text) == n
    lo, hi = [], []
    for k in range(2*b1):
        a = int(digit_text[k:k+digits], 16)
        left, right = F(a, q), F(a+2, q)
        if right >= 1:
            lower = 0
        else:
            lower = min(left, 1-right)
        upper = min(F(1, 2), min(left, 1-left)+F(2, q))
        lo.append(int((q*lower)**2))
        hi.append(int((q*upper)**2))
    # A moving-sum recurrence, independently from stored prefix-sum differences.
    sl, sh = sum(lo[b0:2*b0]), sum(hi[b0:2*b0])
    minimum = None
    minimum_b = None
    all_pass = True
    for b in range(b0, b1+1):
        i = b-b0
        assert sl == data["lower_sums"][i]
        assert sh == data["upper_sums"][i]
        bound = F(8*sl, b*q*q)
        if minimum is None or bound < minimum:
            minimum, minimum_b = bound, b
        all_pass = all_pass and bound > F(2, 5)
        if b < b1:
            sl += lo[2*b] + lo[2*b+1] - lo[b]
            sh += hi[2*b] + hi[2*b+1] - hi[b]
    assert data["minimum_phase_lower"] == str(minimum)
    assert data["minimum_phase_lower_shell"] == minimum_b
    assert data["all_exceed_two_fifths"] == all_pass
    return {
        "status": "PASS",
        "source_depth": n,
        "all_integer_shells_verified": b1-b0+1,
        "min_shell": b0,
        "max_shell": b1,
        "endpoint_digest": digest,
        "minimum_phase_lower": str(minimum),
        "minimum_phase_lower_shell": minimum_b,
        "all_exceed_two_fifths": all_pass,
        "independence_scope": "different source expression, direction of summation, digit extraction and shell aggregation; shared Fraction library and mathematical BBP/tail premises",
        "boundary": "finite certificates only; no proof of R0"
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = replay(args.certificate)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
