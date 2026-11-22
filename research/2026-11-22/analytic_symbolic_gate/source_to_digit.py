"""Exact finite source-to-digit and Diophantine shadow instruments.

All base-16 computations use exact Fraction arithmetic; the analytical theorems
(Pólya--Carlson and irrationality measure) are invoked in the paper dossier, not
pretended to follow from any finite computation. No external dependencies.
"""
from fractions import Fraction
from math import isqrt

B = 16


def forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError('n must be a positive integer')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def pi16_interval(depth: int) -> tuple[Fraction, Fraction]:
    """Original 4-pole BBP zero-seed interval for pi/16 (classical BBP import)."""
    if type(depth) is not int or depth < 0:
        raise ValueError('depth must be a nonnegative integer')
    p = sum((forcing(n) / B**n for n in range(1, depth+1)), Fraction(0))
    tail = forcing(depth+1) / (15 * B**depth)
    return p, p+tail


def hex_prefix(count: int, depth: int | None = None) -> str:
    """Certify a *finite* base-16 prefix using outward exact rational bounds."""
    if type(count) is not int or count < 1:
        raise ValueError('count must be a positive integer')
    if depth is None:
        depth = count+2
    a,b = pi16_interval(depth)
    lo,hi=(B**count*a).__floor__(), (B**count*b).__floor__()
    if lo != hi:
        raise ValueError('interval unresolved at this depth')
    return f'{lo:0{count}X}'


def periodic_shadow(prefix: str, block: str) -> Fraction:
    """prefix (n digits) followed by an infinite periodic p-digit block."""
    if not block or not all(c in '0123456789abcdefABCDEF' for c in prefix+block):
        raise ValueError('hexadecimal prefix and nonempty block required')
    n,p=len(prefix),len(block)
    A = int(prefix,16) if prefix else 0
    W = int(block,16)
    return Fraction(A*(B**p-1)+W, B**n*(B**p-1))


def common_prefix_length(x: str, y: str) -> int:
    k=0
    for a,b in zip(x,y):
        if a != b:
            break
        k+=1
    return k


def repeating_match(word: str, n: int, period: int) -> int:
    """Length of periodic repetition after prefix n, entirely within word."""
    if type(n) is not int or type(period) is not int or n < 0 or period <= 0 or n+period > len(word):
        raise ValueError('invalid prefix or period')
    k=0
    while n+k < len(word) and word[n+k] == word[n+(k%period)]:
        k+=1
    return k


def finite_irrationality_repetition_cap(n: int, p: int, nu_num: int, nu_den: int = 1000) -> Fraction:
    """L <= (nu-1)n + nu*p + 1 when pi has approximation exponent <nu.

    This is a symbolic implication, not a finite proof of pi's measure.
    """
    if min(n,p,nu_num,nu_den) < 0 or p == 0 or nu_den == 0 or nu_num <= 2*nu_den:
        raise ValueError('requires n>=0, p>=1 and rational nu>2')
    nu=Fraction(nu_num,nu_den)
    return (nu-1)*n+nu*p+1


def kempner_digit_at(position: int) -> int:
    """Digit at one-indexed position of sum_{j>=0}16^{-2**j}."""
    if type(position) is not int or position < 1:
        raise ValueError('position must be >= 1')
    return int(position & (position-1) == 0)


def kempner_digits(N: int) -> str:
    if type(N) is not int or N < 0:
        raise ValueError('N must be nonnegative')
    return ''.join('1' if kempner_digit_at(i) else '0' for i in range(1,N+1))


def kempner_phase_interval(n: int) -> tuple[Fraction,Fraction]:
    """Positive rigorous enclosure for {16**n beta}, beta=sum 16**(-2**k).

    Upper is a coarse geometric bound starting from the next exponent.
    """
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative clock required')
    power=1
    while power<=n:
        power*=2
    first=Fraction(1,16**(power-n))
    return first, first*Fraction(16,15)


def kempner_energy_shell_upper(B_: int) -> Fraction:
    """For B=2**k (k>=1): A_B(beta) <= 2*pi**2*THIS_RATIONAL.

    Also bounds average phase**2; no trigonometric floating evaluation.
    """
    if type(B_) is not int or B_<2 or B_&(B_-1):
        raise ValueError('B must be a power of 2 >= 2')
    # For n in [B,2B), next one is at 2B, and
    # theta_n <= (16/15)*16**(n-2B).
    q = Fraction(1,256)
    geometric = q*(1-q**B_)/(1-q)
    return Fraction(1,B_)*Fraction(256,225)*geometric


def exact_kempner_shell_phase_squares(B_: int, extra_powers: int = 5) -> Fraction:
    """Truncated exact beta phase squares. Lower bound for full phase-square sum.

    Strictly increasing in extra_powers; diagnostic only, not a certified
    complete upper approximation.
    """
    if type(B_) is not int or B_ < 2 or B_ & (B_-1):
        raise ValueError('B must be a power of 2 >=2')
    powers=[2*B_]
    for _ in range(extra_powers):
        powers.append(powers[-1]*2)
    total=Fraction(0)
    for n in range(B_,2*B_):
        phase=sum((Fraction(1,16**(p-n)) for p in powers),Fraction(0))
        total+=phase*phase
    return total/B_
