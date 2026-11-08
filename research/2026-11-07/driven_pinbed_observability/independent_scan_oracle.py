"""Independent finite checks for coherent B2 scans and BBP source transfer.

Only Python standard library. No SUCC imports and no floating-point decisions.
Rational quadratics, an elementary prime-cyclotomic quotient, and rigorous
Machin/Taylor intervals supply different checks from the Fourier proof.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json


def b2(x):
    x = Q(x) % 1
    return x*x-x+Q(1, 6)


def r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def original_source(nmax):
    out = [Q(0)]
    for n in range(1, nmax+1):
        out.append(16*out[-1]+r(n))
    return out


def finite_tails(nmax):
    out = [Q(0)]*(nmax+1)
    for n in range(nmax-1, -1, -1):
        out[n] = (r(n+1)+out[n+1])/16
    return out


def sample_surface(points, m):
    return tuple(sum((b2(Q(j, m)-x) for x in points), Q(0))/len(points)
                 for j in range(m))


@dataclass(frozen=True)
class PC:
    """Q[z]/(1+z+...+z^(p-1)) for a prime p, independently implemented."""
    p: int
    a: tuple[Q, ...]

    def __post_init__(self):
        assert self.p >= 2 and all(self.p % d for d in range(2, self.p))
        assert len(self.a) == self.p-1

    @classmethod
    def from_cyclic(cls, p, coeff):
        a = [Q(0)]*p
        for j, v in enumerate(coeff):
            a[j % p] += v
        last = a[-1]
        return cls(p, tuple(v-last for v in a[:-1]))

    @classmethod
    def root(cls, p, e):
        a = [Q(0)]*p
        a[e % p] = 1
        return cls.from_cyclic(p, a)

    @classmethod
    def scalar(cls, p, c):
        return cls(p, (Q(c),)+(Q(0),)*(p-2))

    def __add__(self, other):
        assert self.p == other.p
        return PC(self.p, tuple(x+y for x, y in zip(self.a, other.a)))

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self+(-other)

    def scale(self, c):
        return PC(self.p, tuple(Q(c)*x for x in self.a))

    def __mul__(self, other):
        assert self.p == other.p
        out = [Q(0)]*(2*self.p-3)
        for i, x in enumerate(self.a):
            for j, y in enumerate(other.a):
                out[i+j] += x*y
        return PC.from_cyclic(self.p, out)


def exact_scan(samples, h):
    m = len(samples)
    total = PC.scalar(m, 0)
    for j, y in enumerate(samples):
        total = total+PC.root(m, -h*j).scale(y/m)
    return total


@dataclass(frozen=True)
class I:
    lo: Q
    hi: Q

    def __post_init__(self):
        assert self.lo <= self.hi

    @classmethod
    def point(cls, x):
        return cls(Q(x), Q(x))

    def __add__(self, other):
        if not isinstance(other, I):
            other = I.point(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+(-other if isinstance(other, I) else -Q(other))

    def __mul__(self, other):
        if not isinstance(other, I):
            other = I.point(other)
        v = (self.lo*other.lo, self.lo*other.hi,
             self.hi*other.lo, self.hi*other.hi)
        return I(min(v), max(v))

    __rmul__ = __mul__

    def inflate(self, radius):
        assert radius >= 0
        return I(self.lo-radius, self.hi+radius)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))


def atan_interval(q, count=18):
    s = sum(((-1)**j*q**(2*j+1)/Q(2*j+1)
             for j in range(count)), Q(0))
    endpoint = s+(-1)**count*q**(2*count+1)/Q(2*count+1)
    return I(min(s, endpoint), max(s, endpoint))


PI = 16*atan_interval(Q(1, 5))-4*atan_interval(Q(1, 239))
assert Q(3) < PI.lo < PI.hi < Q(22, 7)


def phase_interval(turns, degree=12):
    """Enclose exp(2*pi*i*turns), including exact input quantization error."""
    turns = Q(turns) % 1
    if turns > Q(1, 2):
        turns -= 1
    scale = 2**30
    approx_i = (turns*scale+Q(1, 2)).numerator//(turns*scale+Q(1, 2)).denominator
    approx = Q(approx_i, scale)
    center_pi = (PI.lo+PI.hi)/2
    x = 2*center_pi*approx
    drift = abs(approx)*(PI.hi-PI.lo)+2*PI.hi*abs(turns-approx)
    x2 = x*x
    cterm, csum = Q(1), Q(1)
    sterm, ssum = x, x
    for j in range(1, degree+1):
        cterm *= -x2/Q((2*j-1)*(2*j))
        sterm *= -x2/Q((2*j)*(2*j+1))
        csum += cterm
        ssum += sterm
    cr = abs(x)**(2*degree+2)/factorial(2*degree+2)+drift
    sr = abs(x)**(2*degree+3)/factorial(2*degree+3)+drift
    return I(csum-cr, csum+cr), I(ssum-sr, ssum+sr)


def ci_add(a, b):
    return a[0]+b[0], a[1]+b[1]


def ci_scale(a, c):
    return a[0]*c, a[1]*c


def ci_sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def ci_norm2_upper(a):
    return a[0].abs_upper()**2+a[1].abs_upper()**2


def interval_scan(samples, h, *, sign=-1, normalize=True, h2=True):
    m = len(samples)
    out = (I.point(0), I.point(0))
    for j, y in enumerate(samples):
        out = ci_add(out, ci_scale(phase_interval(Q(sign*h*j, m)), y))
    gain = 2*(PI*PI)*(h*h if h2 else 1)*(Q(1, m) if normalize else 1)
    return ci_scale(out, gain)


def mode_interval(points, h):
    out = (I.point(0), I.point(0))
    for x in points:
        out = ci_add(out, phase_interval(-h*x))
    return ci_scale(out, Q(1, len(points)))


def outward(interval, digits=12):
    scale = 10**digits
    low = interval.lo.numerator*scale//interval.lo.denominator
    high = -((-interval.hi.numerator*scale)//interval.hi.denominator)
    def fmt(n):
        a = abs(n)
        return ('-' if n < 0 else '')+str(a//scale)+'.'+str(a % scale).zfill(digits)
    return [fmt(low), fmt(high)]


def overlap(alpha, s):
    s = Q(s) % 1
    return max(alpha-s, 0)+max(alpha-(1-s), 0)


def window_energy_group_ring(v, length, tone):
    """Discrete response norm, represented in Q[Z/mZ] without trig evaluation."""
    m = len(v)
    a = Q(length, m)
    out = [Q(0)]*m
    for y in range(m):
        for j in range(length):
            for ell in range(length):
                out[(tone*(ell-j)) % m] += v[(y+j) % m]*v[(y+ell) % m]/(m*a*a)
    return tuple(out)


def overlap_energy_group_ring(v, length, tone):
    m = len(v)
    a = Q(length, m)
    out = [Q(0)]*m
    for x, p in enumerate(v):
        for y, q in enumerate(v):
            out[(tone*(y-x)) % m] += p*q*overlap(a, Q(y-x, m))/(a*a)
    return tuple(out)


def run():
    checks = {}
    def check(name, condition):
        assert condition, name
        checks[name] = checks.get(name, 0)+1

    for m in (2, 3, 5, 7, 11, 17, 29):
        base = sample_surface([Q(0)], m)
        check('dc_locked_atom_exact', sum(base)/m == Q(1, 6*m*m))
        for h in range(1, m//2+1):
            y = exact_scan(base, h)
            zeta = PC.root(m, -h)
            one = PC.scalar(m, 1)
            zero = PC.scalar(m, 0)
            check('sharp_delta_cyclotomic_identity',
                  (one-zeta)*(one-zeta)*y.scale(m*m)+zeta.scale(2) == zero)
            for a in ((range(m) if m <= 11 else (0, 1, m-1))):
                shifted = exact_scan(sample_surface([Q(a, m)], m), h)
                check('grid_atom_phase_transport', shifted == PC.root(m, -h*a)*y)

    for m in (3, 5, 7, 11):
        v1 = (Q(1),)+(Q(0),)*(m-1)
        v2 = (Q(1, 2), Q(1, 3))+(Q(0),)*(m-3)+(Q(1, 6),)
        v3 = (Q(1, m),)*m
        for length in range(1, m):
            for tone in (0, 1, 2):
                for v in (v1, v2, v3):
                    check('cyclic_continuum_energy_identity',
                          window_energy_group_ring(v, length, tone) ==
                          overlap_energy_group_ring(v, length, tone))

    phase_samples = sample_surface([Q(1, 4)], 17)
    phase_true = (I.point(0), I.point(-1))
    good = interval_scan(phase_samples, 1)
    phase_bound = Q(6, 17*17)
    check('quadrature_control_passes', ci_norm2_upper(ci_sub(good, phase_true)) < phase_bound**2)
    wrong = interval_scan(phase_samples, 1, sign=1)
    check('wrong_phase_mutant_rejected', wrong[1].lo-Q(-1) > phase_bound)
    wrong = interval_scan(sample_surface([Q(0)], 17), 1, normalize=False)
    check('missing_normalization_mutant_rejected', wrong[0].lo-1 > phase_bound)
    wrong = interval_scan(sample_surface([Q(0)], 17), 2, h2=False)
    check('missing_h_squared_mutant_rejected', 1-wrong[0].hi > Q(6*4, 17*17))

    kmax = 154
    source = original_source(kmax)
    tails = finite_tails(kmax)
    wrong_source = [-x for x in tails]
    check('same_forcing_wrong_seed_rejected', wrong_source[0] != 0)
    for n in range(1, kmax+1):
        check('same_forcing_wrong_seed_transition', wrong_source[n] == 16*wrong_source[n-1]+r(n))

    rows = []
    for a, m in ((19, 11), (37, 17), (73, 29)):
        points = [source[n] % 1 for n in range(a, 2*a)]
        completed_approximants = [source[n]+tails[n] for n in range(a, 2*a)]
        wrong_points = [wrong_source[n] % 1 for n in range(a, 2*a)]
        samples = sample_surface(points, m)
        bad_samples = sample_surface(wrong_points, m)
        # Tail beyond the single common cutoff K: T_n-tail_n=16^(n-K)T_K.
        residual_average = sum((Q(16)**(n-kmax)/Q(15*(kmax+1)**2)
                                for n in range(a, 2*a)), Q(0))/a
        for h in (1, 2, 3):
            estimate = interval_scan(samples, h)
            direct = mode_interval(points, h)
            completed = mode_interval(completed_approximants, h)
            completed = tuple(v.inflate(2*PI.hi*h*residual_average) for v in completed)
            alias_bound = Q(6*h*h, m*m)
            source_bound = Q(22*h, 105*a*a)
            radius = alias_bound+source_bound
            direct_difference = ci_sub(estimate, direct)
            completed_difference = ci_sub(estimate, completed)
            check('fresh_bbp_alias_enclosure', ci_norm2_upper(direct_difference) < alias_bound**2)
            check('fresh_bbp_completed_transport', ci_norm2_upper(completed_difference) < radius**2)
            wrong_estimate = interval_scan(bad_samples, h)
            check('fixed_wrong_seed_stays_locked', wrong_estimate[0].lo > 1-radius)
            rows.append({
                'A': a, 'scan_M': m, 'harmonic': h,
                'original_estimate_real': outward(estimate[0]),
                'original_estimate_imag': outward(estimate[1]),
                'completed_mode_real': outward(completed[0]),
                'completed_mode_imag': outward(completed[1]),
                'wrong_seed_estimate_real': outward(wrong_estimate[0]),
                'alias_radius_rational': str(alias_bound),
                'combined_radius_rational': str(radius),
                'comparison_passed': True,
            })

    return {
        'status': 'PASS',
        'arithmetic': 'exact Fractions; prime cyclotomic quotient; rigorous rational Machin/Taylor intervals',
        'scope': 'finite checks only; all-parameter claims rest on the written proofs',
        'checks_by_family': checks,
        'total_checks': sum(checks.values()),
        'mutations_rejected': 3,
        'fresh_epochs': rows,
        'fixed_wrong_seed_cutoff_K': kmax,
        'source_hash': sha256('\n'.join(str(x) for x in source).encode()).hexdigest(),
        'oracle_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'pi_interval': outward(PI, 22),
        'source_selected_mode_decay': 'OPEN',
        'pi_base16_normality': 'OPEN',
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
