"""Exact selected-BBP mirror/collision instruments; floats are diagnostics only.

Paper implications and their OPEN source premises are separated in PROOFS.md.
No randomness, pi digits, changed seed, or averaged prime phase is an input.
"""
from fractions import Fraction
from math import cos, fsum, lcm, pi, sin, sqrt


def source(n: int) -> Fraction:
    if n < 1:
        raise ValueError('n must be positive')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def odd_source(n: int) -> Fraction:
    """Same four signed poles, after exactly combining the two even poles."""
    if n < 1:
        raise ValueError('n must be positive')
    return (Fraction(4, 8*n-7) - Fraction(1, 8*n-3)
            - Fraction(3*n-1, (2*n-1)*(4*n-1)))


def fraction_phases(last: int) -> list[Fraction]:
    if last < 0:
        raise ValueError('last must be nonnegative')
    u = Fraction(0)
    out = []
    for n in range(1, last+1):
        u = (16*u + source(n)) % 1
        out.append(u)
    return out


def odd_modular_lift(last: int) -> tuple[int, list[int]]:
    """Integer-only original phases at times 1..last, common ODD modulus."""
    if last < 0:
        raise ValueError('last must be nonnegative')
    den = 1
    for n in range(1, last+1):
        den = lcm(den, 2*n-1, 4*n-1, 8*n-7, 8*n-3)
    out, a = [], 0
    for n in range(1, last+1):
        d = (2*n-1)*(4*n-1)
        assert den % d == 0  # these two odd factors are coprime
        injection = 4*(den//(8*n-7)) - den//(8*n-3) - (3*n-1)*(den//d)
        a = (16*a + injection) % den
        out.append(a)
    return den, out


def _validate(residues: list[int], den: int) -> None:
    if den < 1 or not residues or any(a < 0 or a >= den for a in residues):
        raise ValueError('nonempty residues in [0,den), den positive')


def energy(residues: list[int], den: int, mesh: int) -> tuple[list[int], Fraction]:
    _validate(residues, den)
    if mesh < 2:
        raise ValueError('mesh must be at least 2')
    counts = [0]*mesh
    for a in residues:
        counts[mesh*a//den] += 1
    return counts, Fraction(mesh*sum(c*c for c in counts), len(residues)**2)


def slow_mesh(A: int) -> int:
    """For A=2^j: m=2^floor(log2 j), clipped below at 2; m is ~log A."""
    if A < 2 or A & (A-1):
        raise ValueError('A must be a dyadic integer >=2')
    j = A.bit_length()-1
    return max(2, 1 << (j.bit_length()-1))


def mirror_wasserstein(residues: list[int], den: int,
                       beta: Fraction = Fraction(1, 16)) -> Fraction:
    """EXACT interval W1 between empirical U and J_beta(U), J_beta(x)=beta-x.

    Sorted equal-mass matching on [0,1], not a claim about an optimal
    circular matching. Its circle-character transport bound is valid.
    """
    _validate(residues, den)
    beta = Fraction(beta) % 1
    q = lcm(den, beta.denominator)
    xs = sorted(a*(q//den) for a in residues)
    b = beta.numerator*(q//beta.denominator)
    ys = sorted((b-x) % q for x in xs)
    return Fraction(sum(abs(x-y) for x, y in zip(xs, ys)), q*len(xs))


def cdf_wasserstein(xs: list[Fraction], ys: list[Fraction]) -> Fraction:
    """Independent exact integral of absolute empirical-CDF difference."""
    if not xs or len(xs) != len(ys):
        raise ValueError('equal nonzero sample sizes required')
    from collections import Counter
    a, b = Counter(map(Fraction, xs)), Counter(map(Fraction, ys))
    knots = sorted(set(a) | set(b))
    count = 0
    total = Fraction(0)
    for left, right in zip(knots, knots[1:]):
        count += a[left]-b[left]
        total += abs(count)*(right-left)
    return total/len(xs)


def antiphase_matching_cost(residues: list[int], den: int, h: int = 1) -> Fraction:
    """Exact cost of one FEASIBLE rank-half-turn permutation, not an optimum.

    Mean ||h(U_tau-U)-1/2||. Gives |mean e(hU)| <= pi*cost.
    The permutation is an involution when the number of samples is even.
    """
    _validate(residues, den)
    if h == 0:
        raise ValueError('h must be nonzero')
    xs = sorted((h*a) % den for a in residues)
    N, total = len(xs), 0
    for i, x in enumerate(xs):
        y = xs[(i+N//2) % N]
        v = (2*(y-x)-den) % (2*den)
        total += min(v, 2*den-v)
    return Fraction(total, 2*den*N)


def antiphase_weyl_ceiling(cost: Fraction) -> Fraction:
    if not 0 <= cost <= Fraction(1, 2):
        raise ValueError('cost must lie in [0,1/2]')
    return min(Fraction(1), Fraction(22, 7)*cost)


def primitive_frequency(h: int) -> tuple[int, int]:
    if h == 0:
        raise ValueError('h must be nonzero')
    g, v = abs(h), 0
    while g % 16 == 0:
        g //= 16
        v += 1
    return g, v


def mirror_weyl_ceiling(W: Fraction, N: int, h: int) -> Fraction:
    """Exact rational ceiling from W1 + original-source Ward error.

    Valid ONLY for the original BBP source (or a proved identical Ward bound),
    not an arbitrary finite cloud. This is deliberately conservative.
    """
    if N < 1 or not 0 <= W <= 1:
        raise ValueError('N positive and W in [0,1] required')
    g, v = primitive_frequency(h)
    ward = (2 + Fraction(165*g, 56))/N
    reduction = (2*v + Fraction(11*g*(16**v-1), 56))/N
    return min(Fraction(1), 8*(Fraction(374*g, 7)*W + ward)+reduction)


def ladder_count(mesh: int, h: int) -> int:
    if mesh < 2 or h == 0:
        raise ValueError('mesh>=2 and h!=0 required')
    f, k = abs(h), 0
    while 4*f <= mesh:
        k += 1
        f *= 16
    return k


def weyl_float(points: list[Fraction], h: int) -> complex:
    """Uncertified floating diagnostic, phases reduced before conversion."""
    if not points:
        raise ValueError('nonempty points required')
    xs = [float((h*Fraction(x)) % 1) for x in points]
    return complex(fsum(cos(2*pi*x) for x in xs),
                   fsum(sin(2*pi*x) for x in xs))/len(xs)


def fejer_float(points: list[Fraction], mesh: int) -> float:
    if not points or mesh < 2 or mesh % 2:
        raise ValueError('nonempty points and even mesh>=2 required')
    return 1 + 2*fsum((1-2*h/mesh)*abs(weyl_float(points, h))**2
                     for h in range(1, mesh//2))


def tail_norm_bound_float(A: int, mesh: int) -> float:
    """Paper upper pi*m^(3/2)/(sqrt(12288)*A^2), float diagnostic only."""
    if A < 1 or not 2 <= mesh <= A:
        raise ValueError('2<=mesh<=A required')
    return pi*mesh**1.5/(sqrt(12288)*A*A)


def rational_interval(x: Fraction, bits: int = 40) -> dict[str, int]:
    if bits < 1:
        raise ValueError('bits must be positive')
    scale = 1 << bits
    lo = (x.numerator*scale)//x.denominator
    hi = -((-x.numerator*scale)//x.denominator)
    return {'lower_numerator': lo, 'upper_numerator': hi, 'denominator': scale}
