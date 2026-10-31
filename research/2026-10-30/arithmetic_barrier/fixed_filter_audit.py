"""Exact fixed-filter holdouts for CG-03, never an asymptotic certificate."""
from fractions import Fraction as F
from math import prod
import json
from independent_arithmetic_audit import prefix, prime, r, vp


def main():
    # Frozen before this run: native, difference, second difference, third lag,
    # two annihilating filters, and an unrelated integer filter.
    filters = ((1,), (-1, 1), (1, -2, 1), (-1, 0, 0, 1),
               (-16, 1), (256, -32, 1), (7, -3, 0, 2))
    times = (103, 173, 281, 419)
    values = prefix(max(times) + max(map(len, filters)))
    rows = []
    prime_checks = 0
    for cs in filters:
        d = len(cs)-1
        lam = sum(c*16**j for j,c in enumerate(cs))
        bs = [sum(cs[j]*16**(j-t) for j in range(t,d+1))
              for t in range(1,d+1)]
        for n in times:
            direct = sum((c*values[n+j] for j,c in enumerate(cs)), F())
            forced = sum((b*r(n+t) for t,b in enumerate(bs,1)), F())
            assert direct == lam*values[n] + forced
            product = prod(8*(n+t)-offset
                           for t in range(1,d+1) for offset in (7,4,3,2))
            assert product % forced.denominator == 0
            checked = 0
            if lam:
                for p in range(max(7,n//3),8*n+1):
                    if prime(p) and values[n].denominator % p == 0 and lam % p and product % p:
                        assert vp(values[n],p) == -1
                        assert vp(direct,p) == -1
                        checked += 1
            else:
                assert product % direct.denominator == 0
            rows.append({'coefficients':cs,'n':n,'P_at_16':lam,
                         'denominator_bits':direct.denominator.bit_length(),
                         'retained_prime_checks':checked})
            prime_checks += checked
    print(json.dumps({'status':'PASS_FINITE_EXACT','filter_cases':len(rows),
                      'retained_prime_checks':prime_checks,'rows':rows,
                      'asymptotic_rate_certified_by_this_run':False},indent=2))


if __name__ == '__main__':
    main()
