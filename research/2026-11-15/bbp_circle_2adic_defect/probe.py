"""BBP circle/2-adic defect probe. Exact source arithmetic, finite witnesses.

Self-contained standard-library implementation. This module does NOT establish
pi normality, a source-specific Weyl saving, or a physical p-adic carrier.
"""
from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


def forcing(n: int) -> Fraction:
    """The original four-pole forcing, continued to integral 2-adic indices."""
    return Fraction(120*n*n - 89*n + 16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def forcing_four_poles(n: int) -> Fraction:
    if n < 1:
        raise ValueError('the original real BBP source starts at n=1')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def mod_fraction(value: Fraction, modulus: int) -> int:
    """Embed an odd-denominator rational in Z/2^e."""
    if modulus < 2 or modulus & (modulus-1):
        raise ValueError('modulus must be a power of 2 >= 2')
    if value.denominator % 2 == 0:
        raise ValueError('the rational is not a 2-adic integer')
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def stable_clock(n: int, k: int) -> int:
    """The 2-adic limit F(n) modulo 16^k; only k source taps survive."""
    if k < 1:
        raise ValueError('depth must be positive')
    q = 16**k
    return sum(16**j*mod_fraction(forcing(n-j), q)
               for j in range(k)) % q


def negative_clock(m: int) -> Fraction:
    """Exact rational 2-adic source predecessor F(-m), using F(0)=0.

    This is the 2-adic analytic continuation of the original *formula*,
    NOT a claim that original physical real BBP forcing has negative time.
    """
    if type(m) is not int or m < 1:
        raise ValueError('positive backwards source depth required')
    return -sum((16**j*forcing(-j) for j in range(m)),Fraction())/16**m


def v2_fraction(value: Fraction) -> int:
    """Exact two-adic valuation of a nonzero rational number."""
    if not value:
        raise ValueError('valuation of zero is infinite')
    def v2_int(n):
        n=abs(n)
        return (n & -n).bit_length()-1
    return v2_int(value.numerator)-v2_int(value.denominator)


def lifted_states(count: int, seed: Fraction = Fraction()) -> list[Fraction]:
    """Exact original recurrence (without reducing its integer carries)."""
    if count < 0:
        raise ValueError('count must be nonnegative')
    state = Fraction(seed)
    out = [state]
    for n in range(1, count+1):
        state = 16*state + forcing(n)
        out.append(state)
    return out


def green_bounds(n: int, depth: int) -> tuple[Fraction, Fraction]:
    """Strict rational enclosure of original T_n, n>=0, depth>=0."""
    if n < 0 or depth < 0:
        raise ValueError('n and depth must be nonnegative')
    low = sum((forcing(n+j)/16**j for j in range(1, depth+1)), Fraction())
    upper = low + forcing(n+depth+1)/(15*16**depth)
    return low, upper


def certified_prefix(state: Fraction, n: int, k: int,
                     max_depth: int = 50) -> dict:
    """Certify {U_n+T_n} radix-16 prefix from rational tail intervals."""
    if n < 1 or k < 1:
        raise ValueError('positive source index and digit depth required')
    q = 16**k
    u = state % 1
    a = (q*u.numerator)//u.denominator
    for depth in range(1, max_depth+1):
        low, upper = green_bounds(n, depth)
        floor_low = (q*(u+low)).numerator // (q*(u+low)).denominator
        floor_high = (q*(u+upper)).numerator // (q*(u+upper)).denominator
        if floor_low == floor_high:
            return {'uncompleted': a, 'completed': floor_low % q,
                    'increments': floor_low-a, 'q': q, 'depth': depth,
                    'tail_low': low, 'tail_high': upper}
    raise ArithmeticError('prefix remains uncertified at declared depth cap')


def global_prefix(n: int, k: int, depth: int = 40) -> int:
    """Independent decomposition: root x=sum r(j)/16^j, then 16^n*x."""
    q = 16**k
    low, high = green_bounds(0, depth)
    a, b = q*16**n*low, q*16**n*high
    fa = a.numerator//a.denominator
    fb = b.numerator//b.denominator
    if fa != fb:
        raise ArithmeticError('global root interval needs more depth')
    return fa % q


def reverse_digits(value: int, k: int) -> int:
    q = 16**k
    if k < 1 or not 0 <= value < q:
        raise ValueError('prefix must be in the declared radix register')
    out = 0
    for _ in range(k):
        out = 16*out + value % 16
        value //= 16
    return out


def seam_delta(value: int, k: int) -> tuple[int, int]:
    """Reverse-image of real prefix +1; exact 2-adic gap and seam depth."""
    q = 16**k
    if not 0 <= value < q:
        raise ValueError('prefix is outside register')
    new_value = (value+1) % q
    delta = (reverse_digits(new_value, k)-reverse_digits(value,k)) % q
    if value == q-1:
        return delta, 0  # global -1 -> 0 seam
    remaining, trailing = value, 0
    while remaining % 16 == 15:
        remaining //= 16
        trailing += 1
    first_changed = k-trailing  # one-based REAL digit index
    expected = (17*16**(first_changed-1)) % q
    if delta != expected:
        raise AssertionError('digit reversal carry geometry failed')
    return delta, first_changed


def phase_turns(turns: float) -> complex:
    return cmath.exp(2j*math.pi*turns)


def bridge(h: int, t: int, k: int) -> complex:
    """Circle/2-adic Fourier unitary entry using its digit-product law."""
    q = 16**k
    result = complex(1)
    for j in range(1, k+1):
        alpha = h/16**j - t*16**(j-1)/q
        result *= sum(phase_turns(d*alpha) for d in range(16))/16
    return result


def bridge_direct(h: int, t: int, k: int) -> complex:
    """Independent full finite DFT, practical only for small depth."""
    q = 16**k
    return sum(phase_turns((h*reverse_digits(a,k)-t*a)/q)
               for a in range(q))/q


def character_means(prefixes: list[int], k: int) -> list[complex]:
    """2-adic character means of actual *digit-reversal code*, NOT U_n mod q."""
    q = 16**k
    b = [reverse_digits(a,k) for a in prefixes]
    return [sum(phase_turns(t*v/q) for v in b)/len(b)
            for t in range(q)]


def critical_depth(B: int) -> int:
    """Largest 16^k<=32B^2: genuine source q*T_n<1/2 for n>=B."""
    if B < 1:
        raise ValueError('positive shell required')
    k = 0
    while 16**(k+1) <= 32*B*B:
        k += 1
    return max(k,1)


def shell_receipt(B: int, states: list[Fraction]) -> dict:
    k = critical_depth(B)
    q = 16**k
    if len(states) < 2*B:
        raise ValueError('supply states through 2B-1')
    original, corrected = [], []
    seam_count, wrap_count, signed_parity = 0, 0, 0
    max_depth = 0
    for n in range(B,2*B):
        packet = certified_prefix(states[n],n,k)
        if q*packet['tail_high'] >= 1:
            raise AssertionError('critical depth did not keep one-step seam')
        a = packet['uncompleted']; a2 = packet['completed']
        d = packet['increments']
        assert d in (0,1) and a2==(a+d)%q
        assert d == int((q*(states[n]%1+packet['tail_low'])).numerator //
                        (q*(states[n]%1+packet['tail_low'])).denominator > a)
        original.append(a); corrected.append(a2)
        seam_count += d
        wrap_count += d*int(a==q-1)
        signed_parity += d*(1 if a%2==0 else -1)
        max_depth=max(max_depth,packet['depth'])
    h=q//2
    source_mean = sum(phase_turns(h*a/q) for a in original)/B
    completed_mean = sum(phase_turns(h*a/q) for a in corrected)/B
    expected_change = Fraction(-2*signed_parity,B)
    if abs((completed_mean-source_mean)-float(expected_change))>1e-8:
        raise AssertionError('signed critical-frequency seam identity failed')
    return {'B':B,'depth_k':k,'q':q,'seam_hits':seam_count,
            'global_minus_one_hits':wrap_count,
            'signed_parity':signed_parity,
            'critical_h':h,'critical_phase_jump':str(expected_change),
            'max_future_terms_for_certification':max_depth,
            'normality':'OPEN'}


def make_report(shells=(8,16,32,64,96)) -> dict:
    states = lifted_states(2*max(shells)-1)
    examples=[]
    for k in (1,2,3):
        q=16**k
        unique=len({stable_clock(t,k) for t in range(q)})
        examples.append({'k':k,'modulus':q,'distinct_residues':unique,
                         'is_permutation':unique==q})
    first=states[1]
    local_first=(16*(first%1)).numerator//(16*(first%1)).denominator
    return {
        'source':'original four-pole BBP, U_0=0; classical BBP identity for pi imported',
        'source_first_state':str(first),
        'first_arithmetic_padic_residue_mod16':mod_fraction(first,16),
        'first_real_hex_digit_of_rational_state':local_first,
        'stable_padic_clocks':examples,
        'source_negative_predecessor_F_minus_1':str(negative_clock(1)),
        'negative_clock_exact_valuations':[
            {'m':m,'F_minus_m':str(negative_clock(m)),
             'partial_sum_2adic_valuation':v2_fraction(
                 sum((16**j*forcing(-j) for j in range(m)),Fraction()))}
            for m in range(1,9)],
        'predeclared_finite_shells':[shell_receipt(B,states) for B in shells],
        'status':'FINITE OBSERVATIONS only; R0 and pi normality OPEN'}


if __name__ == '__main__':
    print(json.dumps(make_report(),indent=2,sort_keys=True))
