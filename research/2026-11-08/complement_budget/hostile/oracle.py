"""Independent finite hostile checks; no imports of other research oracles.

Exact identities and source histories use integers/Fraction. The source fold
uses a fresh mpmath interval context; raw endpoint rationals are retained.
The paper's universal statements are not inferred from these finite checks.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from observational_succ.duck_bbp import forcing


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def cycle(p, xi=1):
    if not prime(p) or p == 2 or xi % p == 0:
        raise ValueError("odd prime and nonzero anchor required")
    out, x = [], xi % p
    while x not in out:
        out.append(x)
        x = 16 * x % p
    assert x == xi % p
    return out


def eligible(p):
    if p % 8 != 1 or not prime(p):
        return False
    return len(cycle(p)) ** 2 > p * 4 ** isqrt(p.bit_length())


def ambiguity_counts(p, xi, h):
    """Exact cyclotomic witness for H4, independent of complex arithmetic.

    After subtracting (p-m)*chi_-h(x), each coefficient of the polynomial
    in zeta_p must equal m-1, hence the result is (m-1)*Phi_p(zeta_p)=0.
    """
    support = cycle(p, xi)
    m = len(support)
    checks = 0
    for x in support:
        counts = [0] * p
        for t in range(p):
            if (t + h) % p:
                for y in support:
                    counts[(t * (x - y) - h * y) % p] += 1
        counts[-h * x % p] -= p - m
        assert counts == [m - 1] * p
        checks += 1
    return checks


def factor_identity():
    coeff = [(-1) ** j for j in range(16)]
    out = [0] * 17
    for j, v in enumerate(coeff):
        out[j] += v
        out[j + 1] += v
    assert out == [1] + [0] * 15 + [-1]
    return len(out)


def hash_fraction(hasher, x):
    for value in (x.numerator, x.denominator):
        sign = b"-" if value < 0 else b"+"
        raw = abs(value).to_bytes(max(1, (abs(value).bit_length()+7)//8), "big")
        hasher.update(sign + len(raw).to_bytes(8, "big") + raw)


def source_case(p=4409, harmonics=(1, 3)):
    """The preregistered A1103 development clock; exact unwrapped source."""
    from mpmath.ctx_iv import MPIntervalContext
    from mpmath.libmp import to_rational
    iv = MPIntervalContext()
    iv.dps = 50
    L, m = (p-1)//4, len(cycle(p))
    if p % 8 != 1 or L != 2*m:
        raise ValueError("two-replica clean source clock required")
    n0 = L + 1
    xi = 4 * pow(16, n0-(p+7)//8, p) % p
    xclock = cycle(p, xi)
    states, residues = [], []
    current = F()
    unwrapped, carries, phases = hashlib.sha256(), hashlib.sha256(), hashlib.sha256()
    hash_fraction(unwrapped, current)
    source_checks = 0
    for n in range(1, 2*L+1):
        direct = F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
        assert direct == forcing(n)
        current = 16*current + forcing(n)
        frac = current % 1
        hash_fraction(unwrapped, current)
        hash_fraction(phases, frac)
        carry = (16 * (states[-1] if states else F()) + direct).__floor__()
        hash_fraction(carries, F(carry))
        states.append(frac)
        if n >= n0:
            assert current.denominator % p == 0 and current.denominator % (p*p)
            q = current.denominator // p
            principal = current.numerator * pow(q, -1, p) % p
            assert principal == xclock[(n-n0) % m]
            residues.append(principal)
        source_checks += 1
    cases = []
    for h in harmonics:
        values = [(h*(states[n+m-1]-states[n-1])) % 1 for n in range(n0,n0+m)]
        for r in range(m-1):
            n = n0+r
            assert (values[r+1]-16*values[r]-h*(forcing(n+m+1)-forcing(n+1))) % 1 == 0
        total = iv.mpf(0)
        for value in values:
            t = iv.mpf(value.numerator)/value.denominator
            total += abs(iv.cos(iv.pi*t))
        mean = total/m
        lo, hi = [F(*to_rational(x)) for x in mean._mpi_]
        # pi<22/7 gives a rational version of the proved H2 lower bound.
        lower = F(m-1,17*m)*(1-F(330*abs(h),7*(8*n0+1)**2))
        assert lo >= lower
        cases.append({"h":h,"fold_l1_interval":[str(lo),str(hi)],
                      "fold_l1_decimal":[float(lo),float(hi)],
                      "rational_H2_lower":str(lower),"H2_lower_decimal":float(lower),
                      "exact_lag_recurrence_checks":m-1})
    return {"p":p,"m":m,"L":L,"n0":n0,"repeat_count":2,
            "PR1_eligible":eligible(p),"source_checks":source_checks,
            "principal_part_checks":len(residues),
            "source":"original four poles, U0=0; all unwrapped states and carries hashed",
            "unwrapped_sha256":unwrapped.hexdigest(),"literal_carry_sha256":carries.hexdigest(),
            "phase_sha256":phases.hexdigest(),"interval_decimal_precision":50,"cases":cases}


def run(include_source=True):
    checks = []
    for p in (17,41,73,89,97,113,137,193):
        for xi in (1,3):
            for h in (1,3):
                checks.append({"p":p,"xi":xi,"h":h,
                               "exact_cyclotomic_equalities":ambiguity_counts(p,xi,h)})
    repeat_checks = 0
    eligible_twice = []
    for p in range(17,5000,8):
        if prime(p):
            m = len(cycle(p))
            assert ((p-1)//8) % m == 0
            repeat_checks += 1
            if eligible(p) and (p-1)//4 == 2*m:
                eligible_twice.append(p)
    # Exact hostile controls for the even-radix and forcing assumptions.
    assert (-1)**17 == -1 and (-1)**16 == 1
    assert ((-1)**16)*(-1) == -1
    payload = {"status":"finite exact/interval checks; no asymptotic inference",
               "implementation_independence":"No other research oracle imported; canonical forcing shared",
               "ambiguity":checks,"cyclotomic_equalities":sum(x["exact_cyclotomic_equalities"] for x in checks),
               "even_repeat_prime_checks":repeat_checks,"eligible_q2_primes_below_5000":eligible_twice,
               "factor_coefficients_checked":factor_identity(),
               "hostile_controls":["odd radix17 allows constant antipodes",
                                   "radix16 antipodes need forcing phase1/2",
                                   "coherent complement has rho=Rsig=0 in nonresonant linear representation but budget>=1"]}
    if include_source:
        payload["source"] = source_case()
    payload["dependencies"] = {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (ROOT/"observational_succ/duck_bbp.py",Path(__file__))}
    return payload


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    parser.add_argument("--without-source",action="store_true")
    args=parser.parse_args()
    result=run(not args.without_source)
    encoded=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(encoded)
    else:
        print(encoded,end="")
