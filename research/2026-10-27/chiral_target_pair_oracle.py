"""Alternate-method numeric check: direct four-pole history and all-pair kernel.

Uses optional mpmath at 80 digits. This is corroboration of the rigorous
Fraction interval receipt, NOT a separate rigorous interval proof.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80
receipt = json.loads(Path(__file__).with_name('CHIRAL_REASSEMBLY_RECEIPT.json').read_text())
x = Q(0)
xs = []
for n in range(1, 257):
    r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
    x = (16*x+r) % 1
    xs.append(x)
for row in receipt['rows']:
    n = row['N']
    # Reduce exact differences before any arbitrary-precision conversion.
    total = mp.mpf(2*n)
    for a in range(n):
        for b in range(a):
            t = (xs[a]-xs[b]) % 1
            u = mp.mpf(t.numerator)/t.denominator
            total += 2*(3/(5-4*mp.cos(2*mp.pi*u))-1)
    value = total/(n*n)
    lo, hi = map(mp.mpf, row['authentic_full_energy'])
    if not lo <= value <= hi:
        raise AssertionError((n, lo, value, hi))
    print(n, mp.nstr(value, 45), 'inside exact Fraction enclosure')
print('INDEPENDENT DIRECT-FOUR-POLE / ALL-PAIR KERNEL HOLDOUT PASS; '
      'mpmath 80 digits, not proof authority')
