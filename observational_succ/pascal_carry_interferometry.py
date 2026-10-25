"""Exact Pascal/Lucas/Kummer and Walsh/cyclotomic carry tomography.

Scope: mathematical identities and BBP source estimates, NOT pi normality.
Source indices n >= 1; carry samples sourced via the preceding exact module.
No random, float, or guessed independence assumptions enter certificates.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial, isqrt
from .pi_dyadic_prime_transfer import (
    _bbp_forcing, _bbp_states, dyadic_carry_branch_certificate,
)


def _integer(x: int, minimum: int=0) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError(f"strict integer >= {minimum} required")
    return x


def pascal_row(n: int) -> tuple[int, ...]:
    _integer(n)
    return tuple(comb(n, k) for k in range(n + 1))


def _prime(p: int) -> int:
    _integer(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("genuine prime required")
    return p


def base_p_digits(n: int, p: int) -> tuple[int, ...]:
    _integer(n)
    _prime(p)
    digits = []
    while n:
        digits.append(n % p)
        n //= p
    return tuple(digits or [0])


def lucas_mod_p(n: int, k: int, p: int) -> int:
    """Lucas in base-p digits: exact residue of (n choose k) mod p."""
    _integer(n)
    _integer(k)
    _prime(p)
    if k > n:
        return 0
    a, b = base_p_digits(n, p), base_p_digits(k, p)
    result = 1
    for i, ki in enumerate(b):
        ni = a[i] if i < len(a) else 0
        if ki > ni:
            return 0
        result = result * comb(ni, ki) % p
    return result


def kummer_carries(n: int, k: int, p: int) -> int:
    """Count carries for k+(n-k) in base p; equals v_p(C(n,k))."""
    _integer(n)
    _integer(k)
    _prime(p)
    if k > n:
        raise ValueError("k must be <= n")
    a, b, carry, total = k, n-k, 0, 0
    while a or b or carry:
        z = a % p + b % p + carry
        carry = z // p
        total += carry
        a //= p
        b //= p
    return total


def valuation(n: int, p: int) -> int:
    _integer(n, 1)
    _prime(p)
    count = 0
    while n % p == 0:
        count += 1
        n //= p
    return count


def binomial_valuation(n: int, k: int, p: int) -> int:
    _integer(n)
    _integer(k)
    if k > n:
        raise ValueError("k must be <= n")
    return valuation(comb(n,k),p)


def _bit_sign(k: int, mask: int) -> int:
    return -1 if (k & mask).bit_count() & 1 else 1


def walsh_moments(histogram: list[int] | tuple[int,...]) -> tuple[int,...]:
    """M_mask=sum_k hist[k]*(-1)^popcount(k&mask), all 16 masks."""
    if len(histogram) != 16 or any(type(x) is not int or x < 0 for x in histogram):
        raise ValueError("sixteen nonnegative integer bucket counts required")
    return tuple(sum(num*_bit_sign(k,mask) for k,num in enumerate(histogram))
                 for mask in range(16))


def invert_walsh(moments: tuple[int,...]) -> tuple[Q,...]:
    if len(moments) != 16 or any(type(x) is not int for x in moments):
        raise ValueError("sixteen integer Walsh moments required")
    return tuple(Q(sum(moments[mask]*_bit_sign(k,mask)
                       for mask in range(16)),16) for k in range(16))


def branch_gate_counts(hist: tuple[int,...] | list[int]) -> tuple[int,...]:
    if len(hist) != 16:
        raise ValueError("need 16 residues")
    return tuple(sum(hist[k] for k in range(16) if k % (1 << j) == 0)
                 for j in range(5))


def signed_shells_from_gates(gates: tuple[int,...]) -> tuple[int,...]:
    if len(gates) != 5:
        raise ValueError("need five nested binary counts")
    return tuple((1 << (j-1))*(2*gates[j]-gates[j-1]) for j in range(1,5))


def signed_shells_from_walsh(moments: tuple[int,...]) -> tuple[int,...]:
    if len(moments) != 16:
        raise ValueError("need sixteen moments")
    return tuple(sum(moments[mask] for mask in range(1,16)
                     if mask.bit_length() == j) for j in range(1,5))


def walsh_pascal_certificate(histogram: list[int] | tuple[int,...]) -> dict:
    moments = walsh_moments(histogram)
    gates = branch_gate_counts(histogram)
    shells1 = signed_shells_from_gates(gates)
    shells2 = signed_shells_from_walsh(moments)
    assert shells1 == shells2
    assert tuple(invert_walsh(moments)) == tuple(histogram)
    assert 16*histogram[0] == moments[0] + sum(moments[1:])
    assert 16*gates[4] == gates[0] + sum(shells1)
    rows = tuple(sum(moments[mask] for mask in range(16)
                     if mask.bit_count()==r) for r in range(5))
    return {"gates":gates,"shells":shells1,"walsh_moments":moments,
            "pascal_order_contributions":rows,
            "pascal_order_multiplicity":pascal_row(4),
            "zero_branch_excess":16*gates[4]-gates[0],
            "exact_inverse_verified":True}


def even_parity_countermodel() -> dict:
    """16 total observations, on 8 even-parity residues, multiplicity 2 each.

    All Walsh contrasts of orders 1,2,3 vanish, but the unique order-4
    contrast equals total mass. Uniform 16-residue law is distinguished only
    by the 4th interaction. No claim this is the authentic BBP source.
    """
    hist = [2 if k.bit_count()%2 == 0 else 0 for k in range(16)]
    cert = walsh_pascal_certificate(hist)
    assert cert['pascal_order_contributions'] == (16,0,0,0,16)
    assert cert['zero_branch_excess'] == 16
    return {"hist":hist,**cert}


def finite_difference(values: tuple[Q,...], index: int, order: int) -> Q:
    _integer(index)
    _integer(order)
    if index+order >= len(values):
        raise ValueError("insufficient sequence values")
    return sum(((-1)**(order-j)*comb(order,j)*values[index+j]
                for j in range(order+1)),Q())


def forcing_difference(n: int, order: int) -> Q:
    _integer(n,1)
    _integer(order)
    return finite_difference(tuple(_bbp_forcing(n+j) for j in range(order+1)),0,order)


def beta_integer(a: int, b: int) -> Q:
    _integer(a,1)
    _integer(b,1)
    return Q(factorial(a-1)*factorial(b-1),factorial(a+b-1))


def forcing_difference_upper(n: int, order: int) -> Q:
    """Rigorous 15*8^order*B(8n-7,order+2) upper bound.

    r(n)=integral_0^1 t^(8n-8)(1-t)P(t) dt, 0<P(t)<=15;
    (1-t^8)^order <= 8^order(1-t)^order.
    """
    _integer(n,1)
    _integer(order)
    return 15*(8**order)*beta_integer(8*n-7,order+2)


def forcing_pascal_certificate(n: int, order: int) -> dict:
    delta = forcing_difference(n,order)
    bound = forcing_difference_upper(n,order)
    assert 0 < (-1)**order*delta < bound
    return {"n":n,"order":order,"signed_difference":str(delta),
            "absolute_numerator":delta.numerator,"upper":str(bound),
            "sign":1 if delta>0 else -1}


def _circle(value: Q) -> Q:
    return value % 1


def pascal_source_jet(n: int, order: int) -> dict:
    """Delta^k(y_n) = 15^k y_n + sum_0^(k-1)15^(k-1-j)Delta^j r(n+1)
    modulo one. Exact on the selected y0=0; the identity is generic over
    all initial selectors and alone cannot imply cancellation.
    """
    _integer(n)
    _integer(order,1)
    states = _bbp_states(n+order)
    left = _circle(finite_difference(states,n,order))
    correction = sum((15**(order-1-j)*forcing_difference(n+1,j)
                     for j in range(order)),Q())
    right = _circle(15**order*states[n] + correction)
    assert left == right
    simple_bound = Q(15**order-1,14)*_bbp_forcing(n+1)
    assert abs(correction) <= simple_bound
    return {"n":n,"order":order,"circle_lhs":str(left),
            "circle_rhs":str(right),"source_correction":str(correction),
            "absolute_correction_bound":str(simple_bound),
            "source_correction_numerator":correction.numerator,
            "identity_verified":True}


def prime_clock_pascal_gain(p: int, t: int, order: int) -> dict:
    _prime(p)
    _integer(t)
    _integer(order)
    analytic = (4*pow(16,t,p)*pow(15,order,p))%p
    check = sum(((-1)**(order-j)*comb(order,j)*4*pow(16,t+j,p)
                 for j in range(order+1)))%p
    assert analytic == check
    return {"prime":p,"time":t,"order":order,"residue":analytic,
            "annihilated_all_t":order>=1 and p in (3,5),
            "p_clock_invertible_gain":p not in (3,5)}


def signed_jet_remainder_upper(sample_size: int, tau: Q,
                               epsilon: Q, order: int=2,
                               active_pairs: int | None=None) -> Q:
    """Provable global bound on transporting 15 additive carry characters.

    Uses |exp(i t)-sum_{m<=R}(it)^m/m!|<=|t|^(R+1)/(R+1)!,
    |h|<=8 => |2*pi*h/16|<=pi<22/7; |eta-delta+|<=tau+eps.
    This bounds absolute truncation error without estimating signed jet.
    """
    _integer(sample_size)
    _integer(order)
    tau,epsilon=Q(tau),Q(epsilon)
    if not (0<=epsilon<tau<=Q(1,4)):
        raise ValueError("need 0<=eps<tau<=1/4")
    count=sample_size**2 if active_pairs is None else _integer(active_pairs)
    if count > sample_size**2:
        raise ValueError("active pairs must be a subset")
    return 15*count*((Q(22,7)*(tau+epsilon))**(order+1))/factorial(order+1)


def source_pascal_tomography(p: int, tau: Q) -> dict:
    base = dyadic_carry_branch_certificate(p,tau)
    cert = walsh_pascal_certificate(base['branch_histogram'])
    assert tuple(base['dyadic_nested_counts'])==cert['gates']
    assert tuple(base['ramanujan_shells'])==cert['shells']
    bound=signed_jet_remainder_upper(base['window_length'],Q(tau),
                                     Q(base['forcing_drift']),2,
                                     cert['gates'][0])
    return {"prime":p,"tau":str(Q(tau)),"window_length":base['window_length'],
            "active_pairs":cert['gates'][0],"branch_counts":cert['gates'],
            "primitive_shells":cert['shells'],
            "walsh_order_contributions":cert['pascal_order_contributions'],
            "fourth_order_interaction":cert['walsh_moments'][15],
            "zero_branch_excess":cert['zero_branch_excess'],
            "second_order_jet_error_upper":str(bound),
            "second_order_jet_error_upper_over_window":str(bound/base['window_length']),
            "zero_branch_count":cert['gates'][4],
            "local_fourier_transport":"exact for integer centered carry; "+
                                      "jet bound unconditional but jet size unbounded"}
