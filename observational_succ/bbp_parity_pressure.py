"""Original-zero BBP parity = odd-primary CRT sign x global winding x real tail.

No statement in this module proves original-zero pi parity balance or normality.
The module imports the immutable duck_bbp rational source and error budget.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, log, prod

from observational_succ import duck_bbp

ZERO = Fraction(0)
BASE = 16


def prime_powers(value: int) -> dict[int, int]:
    """Exact small-integer factorization, returns p -> highest power p**e."""
    if type(value) is not int or value < 1:
        raise ValueError("positive integer required")
    out: dict[int, int] = {}
    m = value
    p = 2
    while p * p <= m:
        v = 1
        while m % p == 0:
            m //= p
            v *= p
        if v > 1:
            out[p] = v
        p = 3 if p == 2 else p + 2
    if m > 1:
        out[m] = m
    return out


def prime_coordinate(value: Fraction, p: int) -> int:
    """Numerator of the p-primary fractional character, when v_p(den)=1.

    Returns zero for p-integral rational values. A p**2 denominator is
    intentionally rejected: this theorem uses a genuine first p-shell.
    """
    value = Fraction(value)
    d = value.denominator
    if d % p:
        return 0
    if d % (p*p) == 0:
        raise ValueError("p^2 denominator not in simple-pole regime")
    return (value.numerator * pow(d // p, -1, p)) % p


@dataclass(frozen=True)
class SourceParity:
    n: int
    numerator: int
    denominator: int
    remainder: int
    coordinates: tuple[tuple[int, int, int], ...]  # (p, p**v, local numerator)
    winding: int
    tail_correction: int
    completed_parity: int
    prime_product_sign: int
    winding_sign: int
    local_clock_sign: int
    def local(self, p: int) -> int:
        for q, m, k in self.coordinates:
            if q == p:
                if m != p:
                    raise ValueError("chosen prime is not in simple-pole regime")
                return k
        return 0


def original_zero_parity_states(stop: int, tail_depth: int = 12):
    """Yield certified source-time parity states at n=1..stop.

    Q_n=lcm_{j<=n}(den(r(j))) is allowed to be unreduced. All relevant
    denominators are odd. Tail thresholds are certified by outward Fractions.
    """
    if type(stop) is not int or stop < 1 or type(tail_depth) is not int or tail_depth < 0:
        raise ValueError("stop>=1, depth>=0")
    a, q = 0, 1
    powers: dict[int, int] = {}
    for n in range(1, stop + 1):
        r = duck_bbp.forcing(n)
        qnew = q // gcd(q, r.denominator) * r.denominator
        a = BASE * a * (qnew // q) + r.numerator * (qnew // r.denominator)
        q = qnew
        for p, power in prime_powers(r.denominator).items():
            powers[p] = max(power, powers.get(p, 1))
        assert q % 2 == 1 and a % 2 == n % 2
        assert q == prod(powers.values())
        rem = a % q
        theta = ZERO
        coord = []
        local_sign = (-1) ** n
        for p, m in sorted(powers.items()):
            k = (a * pow(q // m, -1, m)) % m
            coord.append((p, m, k))
            theta += Fraction(k, m)
            local_sign *= -1 if k % 2 else 1
        winding = theta.numerator // theta.denominator
        assert Fraction(rem, q) == theta - winding
        x = Fraction(rem, q)
        lo, hi = duck_bbp.tail_interval(n, tail_depth)
        if x + lo >= 1:
            epsilon = 1
        elif x + hi < 1:
            epsilon = 0
        else:
            lo, hi = duck_bbp.tail_interval(n, max(32, tail_depth+16))
            if x + lo >= 1:
                epsilon = 1
            elif x + hi < 1:
                epsilon = 0
            else:
                raise ValueError(f"cannot certify completed integer boundary at n={n}")
        winding_sign = (-1) ** (winding + epsilon)
        real_parity = (a // q + epsilon) % 2
        assert (-1) ** real_parity == local_sign * winding_sign
        yield SourceParity(n, a, q, rem, tuple(coord), winding, epsilon,
                           real_parity, (-1) ** (sum(k for _,_,k in coord)),
                           winding_sign, local_sign)


def parity_covariance(states: list[SourceParity], p: int) -> dict[str, Fraction]:
    """Exact signed one-prime/complement split on a specified chronological epoch."""
    if not states:
        raise ValueError("nonempty consecutive epoch required")
    if any(states[i+1].n != states[i].n+1 for i in range(len(states)-1)):
        raise ValueError("require consecutive original-clock states")
    if any(not any(q == p and m == p for q,m,_ in state.coordinates) for state in states):
        raise ValueError("selected simple-pole prime must occur in every epoch state")
    p_signs = [(-1) ** state.local(p) for state in states]
    real = [(-1) ** state.completed_parity for state in states]
    comp = [p_signs[i] * real[i] for i in range(len(states))]
    N = len(states)
    mp = Fraction(sum(p_signs),N)
    mr = Fraction(sum(real),N)
    mc = Fraction(sum(comp),N)
    cov = mr - mp*mc
    assert mr == mp*mc + cov
    return {"prime_mean":mp,"complement_mean":mc,"real_mean":mr,
            "signed_covariance":cov,"tail_correction_count":sum(s.tail_correction for s in states),
            "number_of_samples":N}


def parity_projected_haar(digits: list[int], starts: int) -> dict[str, Fraction]:
    """Exact Walsh/Rademacher h=8 component of 16-child Haar successor frame.

    IMPORTANT: this digit h=8 character is NOT the continuous Weyl e(8*x).
    """
    if starts < 1 or starts > len(digits):
        raise ValueError("insufficient actual digits")
    if any(type(d) is not int or not 0 <= d < 16 for d in digits):
        raise ValueError("hex digits only")
    counter = Counter(digits[:starts])
    p = [Fraction(counter.get(i,0),starts) for i in range(16)]
    parity = sum(((-1)**i*p[i] for i in range(16)),ZERO)
    J = 16*sum(((p[i]-p[(i-1)%16])**2 for i in range(16)),ZERO)
    isolated = 4*parity*parity
    assert J >= isolated
    return {"digit_h8_parity_mean":parity,"projected_successor_energy":isolated,
            "full_successor_energy":J,"other_modes_energy":J-isolated}


def collision_pressure(counts: dict[tuple[int,...], int], alphabet_cells: int) -> dict[str, Fraction]:
    """Exact empirical inverse participation / counting pressure decomposition.

    Full support may have 16**k bins even if most bins are empty. They are
    handled analytically, never materialized as a giant dense array.
    """
    B = alphabet_cells
    if type(B) is not int or B < 1 or any(type(c) is not int or c <= 0 for c in counts.values()) or len(counts)>B:
        raise ValueError("positive counts in <= B occupied bins")
    N = sum(counts.values())
    if N < 1:
        raise ValueError("need at least one sample")
    q, r = divmod(N, B)
    squared = sum(c*c for c in counts.values())
    E = Fraction(B*squared,N*N)-1
    finite_floor = Fraction(r*(B-r),N*N)
    integer_excess = sum((c-q)*(c-q-1) for c in counts.values()) + (B-len(counts))*q*(q+1)
    excess = Fraction(B*integer_excess,N*N)
    shot = Fraction(B,N)-1
    repeats = Fraction(B*sum(c*(c-1) for c in counts.values()),N*N)
    assert E == finite_floor + excess == shot + repeats
    assert excess >=0 and E>=0
    return {"N":Fraction(N),"B":Fraction(B),"E":E,"finite_floor":finite_floor,
            "excess":excess,"shot_noise_floor":shot,"repeat_collision_pressure":repeats,
            "effective_volume":Fraction(N*N,squared),"occupied_bins":Fraction(len(counts))}


def even_residue_local_tv(Q: int, m: int) -> Fraction:
    """Exact local TV to uniform when canonical global residue b is forced EVEN.

    Uniform over even b in [0,Q), Q odd, m odd divides Q. This is a
    counterexample: every fixed local m can be near Haar while b parity=+1.
    """
    if not (type(Q) is int and type(m) is int and Q > 1 and m > 1 and Q % 2 and m % 2 and Q % m == 0):
        raise ValueError("Q,m odd; 1<m divides Q")
    return Fraction(m*m-1,2*m*(Q+1))


def parity_fourier_l1_upper(p: int) -> float:
    """Elementary uniform upper bound of odd-modulus parity Fourier l1 norm.

    For k in [0,p), eta(k)=(-1)^k; hat eta(h)=2/[p(1+e(-h/p))].
    In particular ||hat eta||_1 <= 2+log p. Floating here is a bound
    display, not a certified numerical interval calculation.
    """
    if not (type(p) is int and p>=3 and p%2):
        raise ValueError("odd modulus >=3")
    return 2+log(p)


def odd_denom_shadow(A: int, selected_prime: int = 1) -> tuple[Fraction, Fraction]:
    """Construct a rational odd-denom counterseed, without pi digit oracle.

    D=selected_prime*16**(2A+48)+1 is odd and p-unit for p=selected_prime.
    For n in [A,2A+8), completed phases are rigorously in [0,1/16).
    Returned certificate is one outward upper bound at n=2A+7.
    """
    if type(A) is not int or A < 2 or type(selected_prime) is not int or selected_prime<1 or selected_prime%2==0:
        raise ValueError("A>=2, odd positive selected_prime")
    N=2*A+16
    lo,hi=duck_bbp.tail_interval(0,N)
    D=selected_prime*BASE**(2*A+48)+1
    z=D*lo
    seed=-Fraction(z.numerator//z.denominator,D)
    assert seed.denominator%2==1
    if selected_prime>1:
        assert seed.denominator%selected_prime != 0
    bound=BASE**(2*A+7)*(seed+hi)
    assert 0<bound < Fraction(1,16)
    return seed, bound
