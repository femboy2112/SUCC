"""Deterministic finite certificate for the checkpoint splicing theorem."""
from fractions import Fraction as F
from math import gcd, isqrt, lcm, prod
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def four(n):
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def circle(z):
    z %= 1
    return min(z, 1-z)


def certify(a, witness=None):
    length, width = 1, 2
    while 16**length < a:
        length += 1
    mesh = 8
    span = a-1+max(width, length)
    horizon = a+span+8
    native, direct = 1, F(0)
    lifted = 0
    phases = {}
    for n in range(1, horizon+1):
        direct = 16*direct + four(n)
        f = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        old = native
        native = lcm(native, f.denominator)
        lifted = 16*lifted*(native//old) + f.numerator*(native//f.denominator)
        assert direct == F(lifted, native)
        if n == a:
            start_clock = native
        if a <= n < 2*a:
            phases[n] = direct % 1
    # BBP completion at epoch start via U_horizon and the exact tail bound.
    scale = 16**(horizon-a)
    lower, upper = direct/scale, (direct + F(1,64*horizon*horizon))/scale
    modulus = 16**span
    word = int(lower*modulus)
    assert word == int(upper*modulus)
    digits = format(word % modulus, '0'+str(span)+'x')
    selected = ['0']*span
    b = [i for i in range(a,2*a) if prime(8*i-7)]
    for i in b:
        j = i-a
        selected[j:j+length] = digits[j:j+length]
    target = F(2*int(''.join(selected),16)+1, 2*modulus)
    c = prod(p for p in range(2*a+1,8*a-7) if p%4 == 1 and prime(p))
    assert start_clock%c == 0
    # A nonzero residue near the center, chosen using only the lower enclosure.
    delta = target - (lower%1)
    j = round(c*delta)
    if j%c == 0:
        j += (1 if c*delta >= j else -1)
    seed = F(j*pow(16**a,-1,c) % c, c)
    assert seed and start_clock % seed.denominator == 0
    if (upper-lower)+F(1,c) >= F(1,2*modulus):
        return dict(A=a, status="grid width guarantee unavailable", native_grid_bits=c.bit_length(),
                    span=span, births=len(b))
    shift = 16**a*seed
    assert int(((lower+shift)%1)*modulus) == int(((upper+shift)%1)*modulus) == int(''.join(selected),16)
    for n in b:
        assert circle(16**n*seed) < F(1,16**length)
        assert gcd(8*n-7,seed.denominator) == 1
    touched = {i for i in range(a,2*a) if any(i <= t+length-1 and t <= i+width-1 for t in b)}
    good = [i for i in range(a,2*a) if i not in touched]
    tail_bound = F(1,64*a*a)
    for i in good:
        assert (phases[i]+16**i*seed+tail_bound)%1 <= F(1,16**width)+tail_bound
    for p in range(2,8*a):
        if prime(p) and (p<=2*a or p%4 == 3):
            assert gcd(seed.denominator,p) == 1
    if witness is not None:
        witness.update(clock=c, seed=seed)
    lower_energy_ratio = F(len(good)**2,a*a)*(1-mesh*(F(1,16**width)+tail_bound))
    return dict(A=a, births=len(b), L=length, m=width, mesh=mesh, interior=len(good),
                native_grid_bits=c.bit_length(), seed_denominator_bits=seed.denominator.bit_length(),
                energy_over_q_lower=str(lower_energy_ratio), span=span, tail_cutoff=horizon)


if __name__ == '__main__':
    assert four(1) != F(5,1) - F(2,4) - F(1,5) - F(1,6)
    print(json.dumps([certify(a) for a in (127,251,509,1024)], indent=2))
