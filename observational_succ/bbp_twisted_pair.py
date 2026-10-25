"""Exact BBP Galois twisted-pair and contragredient observer algebra.

The p-primary source is an AUTHENTIC BBP first-birth window. Distinct
Galois labels are alternative arithmetic observers, not simultaneously
authenticated physical realisations of pi. The pair moments and spectra
are exact integer/Fraction arithmetic. External BGK estimates and
analytic geometry are proved or attributed separately in the dossier.
PI NORMALITY IS NOT PROVED.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from math import comb, gcd, isqrt


def _integer(n, lower):
    if type(n) is not int or n < lower:
        raise ValueError(f"expected integer >= {lower}")
    return n


def is_odd_prime(p):
    _integer(p, 3)
    return all(p % d for d in range(2, isqrt(p) + 1))


def authentic_window_prime(p):
    if not is_odd_prime(p) or p % 8 != 1:
        raise ValueError("genuine prime congruent to 1 mod 8 required")
    return p


def multiplicative_order_16(p):
    authentic_window_prime(p)
    value = 1
    for j in range(1, p):
        value = 16 * value % p
        if value == 1:
            return j
    raise ArithmeticError("prime clock multiplicative order missing")


def authentic_forcing(n):
    _integer(n, 1)
    return (Q(4, 8*n-7) - Q(2, 8*n-4)
            - Q(1, 8*n-3) - Q(1, 8*n-2))


def authentic_window(p):
    """Exact selected BBP states (y,u_p,w_p) on the p-free birth window.

    The unique source starts y0=0. The complement has denominator coprime
    to p; no claim that its value is small, random, or mixing.
    """
    authentic_window_prime(p)
    m = (p-1)//8
    L = multiplicative_order_16(p)
    if m % L:
        raise ArithmeticError("local multiplicative order does not divide m")
    y = Q()
    states = []
    for n in range(1, 4*m+1):
        y = (16*y + authentic_forcing(n)) % 1
        if n >= m+1:
            t = n-m-1
            u = Q(4*pow(16, t, p) % p, p)
            w = (y-u) % 1
            if w.denominator % p == 0:
                raise ArithmeticError("complement still has a p-primary part")
            states.append((y, u, w))
    if len(states) != 3*m:
        raise AssertionError("invalid first-birth window length")
    return L, tuple(states)


def channel_phase(p, h, a, t, w=0):
    """Rational Q/Z phase of e(4*h*a*16^t/p+h*w)."""
    authentic_window_prime(p)
    if type(h) is not int or h == 0:
        raise ValueError("nonzero integer Fourier harmonic required")
    _integer(a, 1)
    _integer(t, 0)
    if a >= p:
        raise ValueError("Galois label must belong to F_p^*")
    return (Q(4*h*a*pow(16, t, p), p) + h*Q(w)) % 1


def differential_phase(p, h, a, b, t):
    """Common-mode-free oriented Galois pair in Q/Z."""
    authentic_window_prime(p)
    _integer(a, 1)
    _integer(b, 1)
    _integer(t, 0)
    if a >= p or b >= p or a == b or type(h) is not int or not h:
        raise ValueError("distinct labelled pair and nonzero harmonic required")
    return Q(4*h*(a-b)*pow(16, t, p), p) % 1


def contragredient_label(p, starting_label, time):
    """Observer FUCC: a_t=a0*16^(-t) mod p."""
    authentic_window_prime(p)
    _integer(starting_label, 1)
    _integer(time, 0)
    if starting_label >= p:
        raise ValueError("starting observer label outside F_p^*")
    return starting_label * pow(pow(16, time, p), -1, p) % p


def delayed_matched_labels(p, future_label, delay):
    """At t use a=16^d*b, at t+d use b: local p-phase cancels."""
    authentic_window_prime(p)
    _integer(future_label, 1)
    _integer(delay, 1)
    if future_label >= p:
        raise ValueError("future Galois label outside F_p^*")
    return future_label * pow(16, delay, p) % p, future_label


def opposite_pair_product_phase(p, h, a, t, w):
    """Unordered opposite-wire product phase: e(2h*w)."""
    authentic_window_prime(p)
    _integer(a, 1)
    _integer(t, 0)
    if a >= p or type(h) is not int or not h:
        raise ValueError("invalid opposite-wire labels")
    return (channel_phase(p, h, a, t, w)
            + channel_phase(p, h, p-a, t, w)) % 1


def chord_pair_moment(p, k):
    """Exact mean of |1-z(a)*conj(z(b))|^(2k), a!=b.

    For 1<=k<p: p/(p-1)*C(2k,k). At k=p: p/(p-1)*(C(2p,p)-2).
    Source-independent because the complete complementary source cancels.
    """
    if not is_odd_prime(p):
        raise ValueError("genuine odd prime required")
    _integer(k, 0)
    if k == 0:
        return Q(1)
    total = sum(((-1 if m % 2 else 1)*comb(2*k, k+m)
                 for m in range(-k, k+1) if m % p == 0))
    return Q(p*total, p-1)


def independent_chord_pair_oracle(p, k):
    """Independent group-ring test using Phi_p(zeta)=0, no floats."""
    if not is_odd_prime(p):
        raise ValueError("genuine odd prime required")
    _integer(k, 0)
    if k == 0:
        return Q(1)
    coefficients = [0]*p
    for label in range(1, p):
        for mode in range(-k, k+1):
            coefficients[label*mode % p] += (
                (-1 if mode % 2 else 1)*comb(2*k, k+mode))
    if len(set(coefficients[1:])) != 1:
        raise ArithmeticError("nonzero group-ring residues are not balanced")
    return Q(coefficients[0]-coefficients[1], p-1)


def galois_frame_spectrum(p, harmonic=1):
    """Normalized channel Gram spectrum, independent of all w_t.

    Let L=ord_p(16), Delta be any complete multiple of L and
    z_t(a)=e(4h*a*16^t/p+h*w_t), |e(h*w_t)|=1.
    The (p-1)x(p-1) Gram has eigenvalues p/L (L-1 times),
    (p-L)/L (once), zero (p-1-L times).
    """
    authentic_window_prime(p)
    if type(harmonic) is not int or harmonic % p == 0:
        raise ValueError("harmonic must be nonzero modulo p")
    L = multiplicative_order_16(p)
    rows = ((Q(p, L), L-1), (Q(p-L, L), 1), (Q(), p-1-L))
    assert sum(m for _, m in rows) == p-1
    assert sum(v*m for v, m in rows) == p-1
    return L, rows


def exact_frame_row_trace(p, harmonic, s, t):
    """Sum_(a in Fp*) e(4h*a*(16^s-16^t)/p): p-1 or -1."""
    authentic_window_prime(p)
    if type(harmonic) is not int or harmonic % p == 0:
        raise ValueError("nontrivial prime-local harmonic required")
    _integer(s, 0)
    _integer(t, 0)
    return p-1 if pow(16, s, p) == pow(16, t, p) else -1


def p_free_fake_phase_source(p, h, selected_label, target_phases, denominator):
    """Finite rational p-free fake matching ANY requested selected phases.

    Other conjugate-wire differentials remain EXACTLY the same.
    The new drive is derived from w and is NOT the BBP four-pole forcing.
    """
    authentic_window_prime(p)
    _integer(denominator, 2)
    _integer(selected_label, 1)
    if (gcd(denominator, p) != 1 or selected_label >= p
            or type(h) is not int or h == 0):
        raise ValueError("invalid source conductor, label or harmonic")
    targets = tuple(Q(x) % 1 for x in target_phases)
    if not targets:
        raise ValueError("nonempty finite target required")
    weights, errors = [], []
    for t, target in enumerate(targets):
        local = Q(4*h*selected_label*pow(16, t, p), p) % 1
        residual = (target-local) % 1
        # Solve h*w=residual (mod 1) BEFORE rounding a p-free q-grid.
        # Rounding residual alone only works for h=1; it is not a
        # generic character-selection oracle.
        ideal = (residual/Q(h)) % 1
        v = denominator*ideal + Q(1, 2)
        n = (v.numerator // v.denominator) % denominator
        w = Q(n, denominator)
        delta = (local+h*w-target) % 1
        err = min(delta, 1-delta)
        if err > Q(abs(h), 2*denominator):
            raise ArithmeticError("finite p-free source selection precision failed")
        weights.append(w)
        errors.append(err)
    drive = tuple((weights[t+1]-16*weights[t]) % 1
                  for t in range(len(weights)-1))
    assert all(x.denominator % p for x in tuple(weights)+drive)
    return tuple(weights), drive, max(errors)


def orientation_connection(swaps):
    """Z2 transport sigma_t=s_t*s_(t+1) for time-dependent wire swaps."""
    switches = tuple(swaps)
    if not switches or any(type(s) is not int or s not in (-1, 1)
                           for s in switches):
        raise ValueError("orientations must be +/-1")
    return tuple(switches[t]*switches[t+1]
                 for t in range(len(switches)-1))


def untwist_oriented_phases(phases, connection):
    """Recover a Q/Z differential history up to one initial global swap."""
    phases = tuple(Q(x) % 1 for x in phases)
    connection = tuple(connection)
    if (not phases or len(connection) != len(phases)-1
            or any(type(s) is not int or s not in (-1, 1)
                   for s in connection)):
        raise ValueError("source history and Z2 connection mismatch")
    orient = 1
    result = []
    for t, value in enumerate(phases):
        result.append(orient*value % 1)
        if t < len(connection):
            orient *= connection[t]
    return tuple(result)


def two_pair_cosine_gain(x):
    """Elementary uniform gain: max(|cos(theta)|,|cos(2theta)|)>=1/2."""
    x = Q(x)
    if abs(x) > 1:
        raise ValueError("cosine argument outside [-1,1]")
    return max(abs(x), abs(2*x*x-1))

def locked_wire_curvature(p, harmonic, initial_label, time, w_now, w_next):
    """psi_(t+1)-16*psi_t on a coherent a_t=16^-t*a0 observer wire."""
    authentic_window_prime(p)
    _integer(time, 0)
    a = contragredient_label(p, initial_label, time)
    an = contragredient_label(p, initial_label, time+1)
    return (channel_phase(p, harmonic, an, time+1, w_next)
            -16*channel_phase(p, harmonic, a, time, w_now)) % 1


def recover_initial_wire_from_source(p, harmonic, curvature, forcing_readout):
    """Authenticate the missing starting wire from one absolute source readout.

    kappa=harmonic*r(t)-60*harmonic*a0/p (mod 1);
    p*{kappa-h*r} is an INTEGER. For p=1 mod8 and p not dividing
    harmonic, 60*harmonic is invertible modulo p.
    """
    authentic_window_prime(p)
    if type(harmonic) is not int or harmonic % p == 0:
        raise ValueError("p-local frequency is needed for exact source calibration")
    delta = (Q(curvature)-harmonic*Q(forcing_readout)) % 1
    lifted = p*delta
    if lifted.denominator != 1:
        raise ValueError("claimed source curvature is not in the Galois p-fiber")
    return (-lifted.numerator*pow(60*harmonic, -1, p)) % p

def flat_zero_forcing_counterfeit(p, selected_label, horizon):
    """One p-free initial q-grid state with EXACT ZERO complement forcing.

    Matches an anti-clock source for every finite time 0<=t<horizon
    with circular phase error <=16^(horizon-1)/(2q).
    q=p*16^horizon+1 (coprime to p) is exponentially large.
    This is NOT the authentic BBP initial state or forcing.
    """
    authentic_window_prime(p)
    _integer(selected_label, 1)
    _integer(horizon, 1)
    if selected_label>=p:
        raise ValueError("invalid source label")
    q=p*16**horizon+1
    desired=(-Q(4*selected_label,p))%1
    t=q*desired+Q(1,2)
    rounded=t.numerator//t.denominator
    w0=Q(rounded%q,q)
    initial_distance=(Q(4*selected_label,p)+w0)%1
    initial_distance=min(initial_distance,1-initial_distance)
    assert initial_distance<=Q(1,2*q)
    phases=[]
    for j in range(horizon):
        w=(16**j*w0)%1
        if w.denominator%p==0:
            raise ArithmeticError("flat counterfeit imported p torsion")
        phase=(Q(4*selected_label*pow(16,j,p),p)+w)%1
        error=min(phase,1-phase)
        if error>Q(16**j,2*q):
            raise ArithmeticError("flat-source finite alignment failed")
        phases.append((w,error))
    return q,tuple(phases),Q(16**(horizon-1),2*q)
