"""Independent exact audit of inherited ternary height and recent-window transfer.

Only Python integers and Fraction. No import from SUCC implementation.
The four-interval law is an alternative certificate for inherited T1, not
a newly discovered height theorem. Finite checks do not prove normality.
"""

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def source(n, mutation=False):
    return (F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)
            + (1 if mutation else -1)*F(1, 8*n-2))


def valuation(a, p):
    if not a:
        raise ValueError("zero has no finite valuation")
    exponent = 0
    while a % p == 0:
        exponent += 1
        a //= p
    return exponent


def d3(x):
    return 3 ** valuation(x.denominator, 3)


def height(n):
    if n == 1:
        return 3
    q = 9
    while n >= (9*q+7)//8:
        q *= 9
    if n < (5*q+3)//8:
        return q
    if n < (3*q+1)//4:
        return q//3
    return 3*q


def run():
    # Fresh full rational range beyond inherited direct Fraction limit 333.
    exact_last = 6144
    starts = [1, 2, 7, 11, 333, 4096, 5001]
    lengths = [1, 2, 17, 64]
    wanted = set(starts) | {t+length for t in starts for length in lengths}
    states = {0: F(0)}
    u = F(0)
    for n in range(1, exact_last+1):
        u = 16*u + source(n)
        assert d3(u) == height(n), (n, "full Fraction height")
        assert 9*d3(u) > 4*n and d3(u) <= 8*n
        if n in wanted:
            states[n] = u

    window_count = 0
    for t in starts:
        for length in lengths:
            n = t+length
            recent = F(0)
            for j in range(t+1, n+1):
                recent = 16*recent+source(j)
            error = states[n]-recent
            assert error == 16**length*states[t]
            assert d3(error) == d3(states[t]) >= 3
            assert valuation(error.numerator,2) >= 4*length
            assert error.denominator % 2
            window_count += 1
    # Full-history null control.
    recent = F(0)
    for n in range(1, 65):
        recent = 16*recent+source(n)
    full = F(0)
    for j in range(1,65):
        full += 16**(64-j)*source(j)
    assert recent == full

    # Fresh modular range: use modulus 81, not the inherited modulus 27 table.
    modular_last = 1_000_003
    modulus = 81
    q = 1
    residue = 0
    for n in range(1, modular_last+1):
        while 3*q <= 8*n:
            q *= 3
            residue = 3*residue % modulus
        residue = 16*residue % modulus
        for e,c in ((7,4),(4,-2),(3,-1),(2,-1)):
            den = 8*n-e
            pp = 3**valuation(den,3)
            assert q % pp == 0
            residue = (residue+c*(q//pp)*pow(den//pp,-1,modulus)) % modulus
        assert residue, (n,"nonzero normalized state mod81")
        observed = q // (3**valuation(residue,3))
        assert observed == height(n), (n,observed,height(n))

    # Certificate of the exceptional cancellation plateau, with all eight
    # contributing denominators at depths k or k-1.
    rows=[]
    running=0
    for m,e,c in [(2,2,-1),(3,7,4),(4,4,-2),(7,3,-1),
                  (10,2,-1),(11,7,4),(12,4,-2),(15,3,-1)]:
        weight=F(3*c,m)
        j_mod3=(e*2)%3
        increment=(pow(16,-j_mod3,9)*weight.numerator
                   *pow(weight.denominator,-1,9))%9
        running=(running+increment)%9
        rows.append(dict(m=m,e=e,c=c,j_mod3=j_mod3,
                         increment_mod9=increment,cumulative_mod9=running))
    assert running == 6

    # A last-tap sign mutation survives the coarse height through this window.
    # It must be rejected by the declared leading-unit observation instead.
    mutant=F(0)
    first_mutation_failure=None
    first_unit_failure=None
    for n in range(1,65):
        mutant=16*mutant+source(n,mutation=True)
        if d3(mutant) != height(n):
            first_mutation_failure=n
        if n == 1:
            normalized=3*mutant
            leading=normalized.numerator*pow(normalized.denominator,-1,3)%3
            if leading != 1:
                first_unit_failure=n
    assert first_mutation_failure is None
    assert first_unit_failure == 1
    # Rejected development formula (q+3)/8 for odd k is not even an integer.
    assert (27+3)%8 != 0 and (27+1)//4 == 7

    return {
        "status":"PASS",
        "scope":"finite exact audit; inherited all-n theorem has separate paper proof",
        "source":"literal four signed BBP fractions, U0=0",
        "fraction_first":1,"fraction_last":exact_last,
        "fresh_fraction_holdout":[4096,6144],
        "modular_first":1,"modular_last":modular_last,"modulus":modulus,
        "fresh_modular_holdout":[180002,modular_last],
        "recent_window_pairs":window_count,
        "window_starts":starts,"window_lengths":lengths,
        "null_full_history_window":True,
        "last_tap_sign_mutation_height_failure_through64":first_mutation_failure,
        "last_tap_sign_mutation_leading_unit_failure":first_unit_failure,
        "development_receipt":"Height-only rejection test initially failed; mutation preserves tested heights. Leading-unit witness correctly rejects it at n=1.",
        "rejected_odd_birth_formula":"(3**k+3)/8; corrected (3**k+1)/4 for odd k",
        "tail_mod9_certificate":rows,
        "normality_proved":False,"collatz_proved":False,"rh_proved":False,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
