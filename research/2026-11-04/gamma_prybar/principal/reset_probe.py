"""Exact sparse-reset control. Run as a script to reproduce RESET_RECEIPT.json."""
from fractions import Fraction as F
from math import gcd, isqrt, lcm, prod
import json


def prime(p):
    return p >= 2 and all(p % a for a in range(2, isqrt(p) + 1))


def forcing(n):
    return sum((F(w, 8*n-c) for w, c in ((4, 7), (-2, 4), (-1, 3), (-1, 2))), F())


def run(first=112, end=533):
    r = [F()] + [forcing(n) for n in range(1, 2*end+1)]
    u = [F()]
    for x in r[1:]:
        u.append(16*u[-1] + x)
    boundary = F(u[2*first] // 1, 16**(2*first))
    q = q_control = 1
    control = [F()]
    delta = F()
    reset = first
    blocks = []
    birth_checks = 0
    for n in range(1, end+1):
        if n == reset:
            donors = [p for p in range(4*n+1, 8*n-10) if p % 8 == 5 and prime(p)]
            h = prod(donors)
            assert q % h == 0
            # u[2n]/16^n is u[n] plus the finite Green tail.
            target = h * (16**n * boundary - u[2*n]/16**n)
            w = target // 1
            while gcd((u[n] + F(w, h)).denominator, h) != h:
                w += 1
            delta = F(w, h)
            assert abs(w-target) <= n*n
            blocks.append(dict(start=n, donor_count=len(donors), grid_bits=h.bit_length(),
                               rounding_search=w-(target//1)))
            reset = 7*(5*n//28)
        else:
            delta *= 16
        y = u[n] + delta
        changed_r = y - 16*control[-1]
        assert q % (changed_r-r[n]).denominator == 0
        q = lcm(q, r[n].denominator)
        q_control = lcm(q_control, changed_r.denominator)
        assert q == q_control and u[n].denominator == y.denominator
        if prime(8*n-7):
            assert changed_r == r[n] and delta.denominator % (8*n-7)
            birth_checks += 1
        if blocks:
            s = blocks[-1]["start"]
            for j in {s, (n+s)//2}:
                if j < n:
                    for coeff in (-1, 1, -3):
                        assert (y+coeff*control[j]).denominator == (u[n]+coeff*u[j]).denominator
        if n >= 2*first:
            assert abs(y - 16**n*boundary) < F(1, 4096)
        control.append(y)
    return dict(first=first, last=end, mesh=32, blocks=blocks, birth_checks=birth_checks,
                state_denominator_and_lcm_checks=end,
                circle_radius_after_double_first="1/4096", all_assertions_passed=True)


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
