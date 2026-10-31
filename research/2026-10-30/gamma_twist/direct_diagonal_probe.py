"""Fresh exact first-birth witnesses for the direct diagonal obstruction.

No import of the parent transport implementation. These finite witnesses
calibrate an unbounded paper argument; no finite sample proves that argument.
"""
from fractions import Fraction as F
import json


def vp(x, p):
    if not x:
        return None
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


rows = []
for p, depth in ((3, 4), (5, 3), (7, 2), (11, 2), (13, 2),
                 (17, 2), (19, 2), (41, 1), (83, 1), (113, 1)):
    power = p**depth
    birth = ((power+7)//8 if power % 8 == 1 else
             (power+3)//8 if power % 8 == 5 else (power+1)//4)
    u = F()
    for n in range(1, birth+1):
        r = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        u = 16*u+r
    assert vp(u, p) == -depth
    primary = power*u
    residue = primary.numerator*pow(primary.denominator, -1, p) % p
    expected = 4 if power % 8 == 1 else -1 if power % 8 == 5 else -pow(2, -1, p)
    assert residue == expected % p
    rows.append({"p": p, "depth": depth, "birth": birth,
                 "valuation": vp(u, p), "normalized_residue": residue,
                 "outside_Q_zeta_8_times_squarefree": depth >= 2})
print(json.dumps({"status": "PASS", "rows": rows,
    "conclusion_scope": "finite calibration of inherited births and new domain obstruction",
    "pi_normality_proved": False}, indent=2))
