"""Exact unwrapped common-denominator BBP histories and independent residues."""
from fractions import Fraction as Q
from hashlib import sha256
from math import lcm
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
PRIOR = ROOT/'research/2026-11-07/learning_yoneda/arithmetic'
sys.path.insert(0, str(PRIOR))
from finite_adelic import odd_prime, exact_integer, prime_set

POLES = ((4, 7), (-2, 4), (-1, 3), (-1, 2))


def common_history(last, retain_from=0):
    exact_integer(last, 'last', 1)
    exact_integer(retain_from, 'retain_from')
    if retain_from > last:
        raise ValueError('retained chronology cannot be empty')
    denominator = 1
    for n in range(1, last+1):
        for _, pole in POLES:
            denominator = lcm(denominator, 8*n-pole)
    unwrapped = 0
    previous_floor = 0
    history_digest = sha256(b'BBP:4,-2,-1,-1;7,4,3,2;U0=0;unwrapped\0')
    carry_digest = sha256(b'floor(U_n)-16floor(U_(n-1))\0')
    residues = [] if retain_from else [0]
    for n in range(1, last+1):
        forcing = sum(c*(denominator//(8*n-pole)) for c, pole in POLES)
        unwrapped = 16*unwrapped+forcing
        floor, residue = divmod(unwrapped, denominator)
        carry = floor-16*previous_floor
        previous_floor = floor
        raw = unwrapped.to_bytes(max(1, (unwrapped.bit_length()+7)//8), 'big')
        history_digest.update(len(raw).to_bytes(8, 'big')+raw)
        carry_digest.update(str(carry).encode()+b'\n')
        if n >= retain_from:
            residues.append(residue)
    return {'last': last, 'retain_from': retain_from, 'denominator': denominator,
            'final_unwrapped_numerator': unwrapped, 'residues': residues,
            'unwrapped_sha256': history_digest.hexdigest(), 'carry_sha256': carry_digest.hexdigest()}


def direct_modular_residue(n, denominator):
    """Independent BBP power-sum algorithm, not a recurrence."""
    exact_integer(n, 'time')
    exact_integer(denominator, 'denominator', 1)
    value = 0
    for j in range(1, n+1):
        for coefficient, pole in POLES:
            d = 8*j-pole
            if denominator % d:
                raise ValueError('denominator does not cover source poles')
            value += coefficient*pow(16, n-j, d)*(denominator//d)
    return value % denominator


def principal_pair(numerator, denominator, p):
    if type(numerator) is not int:
        raise ValueError('integer numerator required')
    odd_prime(p)
    exact_integer(denominator, 'denominator', 1)
    pe = 1
    while denominator % p == 0:
        denominator //= p
        pe *= p
    if pe == 1:
        return 0, 1
    return numerator*pow(denominator, -1, pe) % pe, pe


def matched_seed(data, A, K, eta, primes):
    """PE14/AR center, implemented without rebuilding Fraction histories."""
    exact_integer(A, 'A', 1)
    exact_integer(K, 'K')
    if type(eta) is not Q or not 0 < eta < Q(1, 4):
        raise ValueError('exact eta in (0,1/4) required')
    primes = prime_set(primes)
    B = data['last']
    if A > B:
        raise ValueError('A exceeds final source time')
    den = data['denominator']
    S = data['final_unwrapped_numerator']
    scale = 16**(B-A)*den
    M = -((-S)//scale)
    center = Q(M*scale-S, den*16**B)
    D = 2
    for p in primes:
        D *= p
    target = Q(2**K*16**B)/eta
    qmin = -((-target.numerator)//target.denominator)
    q = 1+D*(-((-(qmin-1))//D))
    mq = center*q/2**K
    m = max(1, -((-mq.numerator)//mq.denominator))
    seed = Q(2**K*m, q)
    assert 0 < seed and 0 <= seed-center <= eta/16**B
    assert all(seed.denominator % p for p in primes)
    return seed, center, M
