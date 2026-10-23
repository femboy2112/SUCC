"""Exact finite arithmetic -> Dirichlet -> Bruhat--Tits-star code experiment.

Classical inputs: Hardy--Dirichlet coefficient embedding and the [[3,1,2]]_3
qutrit erasure code. The three geometric legs are actual 2-adic lattice
neighbors mod 2, not a claimed gravitational Einstein--Rosen bridge.

Source chart: span{|1>, |2>, |4>}; geometric quantum alphabet F_3.
Only compressed V_2 is represented; additive S does NOT preserve this chart.
No zero coordinates, fake prime jets, signed Weil claim, or RH claim.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import isqrt

Q = 3
SOURCE = (1, 2, 4)
PAIRS = ((0, 1), (0, 2), (1, 2))


def _frac(x):
    if type(x) not in (int, F):
        raise TypeError("integer or Fraction expected; floats and bools forbidden")
    return F(x)


def _digit(x):
    if type(x) is not int or x not in range(Q):
        raise ValueError("one F3 digit expected")
    return x


def dirichlet_samples(coeffs):
    """F(s)=a_0+a_1 2^-s+a_2 4^-s, at s=1,2,3 (exact rational)."""
    if len(coeffs) != Q:
        raise ValueError("three coefficients expected")
    a = tuple(map(_frac, coeffs))
    return tuple(sum((a[i] * F(1, (2**i)**s) for i in range(Q)), F())
                 for s in range(1, Q+1))


def dirichlet_reconstruct(samples):
    """Inverse rational Vandermonde, independent of floating evaluation."""
    if len(samples) != Q:
        raise ValueError("three rational samples expected")
    f0, f1, f2 = map(_frac, samples)
    return (f0/3 - 2*f1 + F(8,3)*f2,
            -4*f0 + 20*f1 - 16*f2,
            F(32,3)*f0 - 32*f1 + F(64,3)*f2)


def prime_shift(coeffs):
    """P_{1,2,4} V_2 P_{1,2,4}; nilpotent, NOT cyclic."""
    if len(coeffs) != Q:
        raise ValueError("three source coefficients expected")
    a, b, _ = map(_frac, coeffs)
    return (F(), a, b)


def additive_shift_compressed(coeffs):
    """P_{1,2,4} S P_{1,2,4}; paths leave this non-hereditary chart."""
    if len(coeffs) != Q:
        raise ValueError("three source coefficients expected")
    a, _, _ = map(_frac, coeffs)
    return (F(), a, F())


def local_bruhat_tits_neighbors():
    """Index-two sublattices L between 2Z_2^2 and Z_2^2, via F2 kernels."""
    vectors = tuple(product(range(2), repeat=2))
    forms = ((1, 0), (0, 1), (1, 1))
    kernels = tuple(frozenset((x, y) for x, y in vectors
                              if (a*x + b*y) % 2 == 0)
                    for a, b in forms)
    assert len(set(kernels)) == 3 and all(len(k) == 2 for k in kernels)
    return kernels


def codeword(i):
    """Each tuple has amplitude 1/sqrt(3) in the 3-qutrit codeword |i_L>."""
    i = _digit(i)
    return tuple((j, (j+i) % Q, (j+2*i) % Q) for j in range(Q))


def pair_decode(pair, visible):
    """Recover logical slope i and erased digit k from any two boundary legs."""
    if pair not in PAIRS or len(visible) != 2:
        raise ValueError("ordered pair of distinct geometric legs required")
    x, y = pair
    u, v = map(_digit, visible)
    i = ((v-u) * pow(y-x, -1, Q)) % Q
    j = (u-i*x) % Q
    lost = ({0,1,2}-set(pair)).pop()
    k = (j+i*lost) % Q
    return (i, k)


def pair_encode(i, k, pair):
    """Exact inverse decoder: (logical digit, EPR ancillary digit) -> pair."""
    _digit(i)
    _digit(k)
    if pair not in PAIRS:
        raise ValueError("ordered pair of distinct legs required")
    lost = ({0,1,2}-set(pair)).pop()
    j = (k-i*lost) % Q
    return tuple((j+i*x) % Q for x in pair)


def two_leg_prime_shift(pair, visible, *, reverse=False):
    """Two-leg boundary representative of compressed V2 or V2-adjoint.

    Returns None for the nilpotent terminal state. The erased leg is fixed,
    and the EPR ancilla digit k is preserved under either operation.
    """
    i, k = pair_decode(pair, visible)
    if reverse:
        if i == 0:
            return None
        return pair_encode(i-1, k, pair)
    if i == Q-1:
        return None
    return pair_encode(i+1, k, pair)


def act_on_boundary(word, pair, *, reverse=False):
    if len(word) != Q or any(type(d) is not int or d not in range(Q) for d in word):
        raise ValueError("one three-qutrit computational basis word required")
    newpair = two_leg_prime_shift(pair, tuple(word[x] for x in pair), reverse=reverse)
    if newpair is None:
        return None
    out = list(word)
    for site, digit in zip(pair, newpair):
        out[site] = digit
    return tuple(out)


def arithmetic_tfd_beta2_weights():
    """Unnormalized coefficients for beta=2: (4,2,1)/sqrt(21)."""
    return (4, 2, 1)


def encoded_tfd_support(weights=(4, 2, 1)):
    """Integer numerator amplitudes of (W\\otimes W)|TFD_2>.

    Every (left,right) six-digit word has amplitude value/(3*sqrt(21)).
    No approximate complex amplitudes or numerical normalization involved.
    """
    out = {}
    for i, weight in enumerate(weights):
        for left in codeword(i):
            for right in codeword(i):
                key = (left, right)
                assert key not in out
                out[key] = weight
    assert len(out) == 27
    return out


def encoded_mirror_images(left_pair, right_pair, *, weights=(4, 2, 1)):
    """Compare (T_A\\otimes I) and (I\\otimes 2 T_B^dagger) on TFD_2.

    All coefficients are exact integers with common factor 1/(3*sqrt(21)).
    The physical two-leg representatives act on codewords, not arbitrary
    claimed infinite-source Hilbert vectors.
    """
    left_action, right_action = {}, {}
    for (left, right), weight in encoded_tfd_support(weights).items():
        new_left = act_on_boundary(left, left_pair)
        if new_left is not None:
            key = (new_left, right)
            left_action[key] = left_action.get(key, 0) + weight
        new_right = act_on_boundary(right, right_pair, reverse=True)
        if new_right is not None:
            key = (left, new_right)
            right_action[key] = right_action.get(key, 0) + 2*weight
    return left_action, right_action


def truncation_mirror_residual_beta2(N, p=2):
    """Exactly squared residual of finite source TFD_N prime-mirror identity.

    ||(V_p\\otimes 1 - p(1\\otimes V_p*) ) Omega_N||^2
      = (sum_{floor(N/p)<n<=N} n^-2)/(sum_{n<=N} n^-2)
    for beta=2. The RHS norm is on the infinite ambient Hilbert space.
    """
    if type(N) is not int or not 1 <= N <= 10000:
        raise ValueError("integer source cutoff 1..10000 required")
    if type(p) is not int or p < 2 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError("genuine prime expected")
    z = sum((F(1, n*n) for n in range(1, N+1)), F())
    tail = sum((F(1, n*n) for n in range(N//p+1, N+1)), F())
    return tail/z


def source_chart_braid_defect():
    """PVP PSP != (PSP)^2 PVP on the nonhereditary {1,2,4} chart."""
    e0 = (F(1),F(),F())
    lhs = prime_shift(additive_shift_compressed(e0))
    rhs = additive_shift_compressed(additive_shift_compressed(prime_shift(e0)))
    return lhs, rhs
