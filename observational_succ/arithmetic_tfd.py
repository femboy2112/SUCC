"""Exact finite controls for arithmetic thermofield and prime-mirror theorems.

No infinite-dimensional conclusion is inferred from these finite checks.
Even beta=2*s gives rational unnormalised amplitudes n**(-s); normalised
density entries and squared residuals remain rational. Gaussian rationals
allow phase-mutation controls without floating point or optional packages.
See research/2026-10-22/PRIME_MIRROR_RIGIDITY.md for the completion theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .unit_prime_succ import prime


class ArithmeticTFDError(ValueError):
    pass


def _integer(n, lo=1, hi=10000):
    if type(n) is not int or not lo <= n <= hi:
        raise ArithmeticTFDError(f"integer in [{lo},{hi}] required")
    return n


def _rational(x):
    if type(x) not in (int, Q):
        raise ArithmeticTFDError("exact int/Fraction required; no floats or bools")
    return Q(x)


def _prime(p):
    _integer(p, 2)
    if not prime(p):
        raise ArithmeticTFDError("genuine prime coordinate required")
    return p


@dataclass(frozen=True)
class Gaussian:
    """An element of Q(i), with exact arithmetic and conjugation."""
    real: Q = Q(0)
    imag: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "real", _rational(self.real))
        object.__setattr__(self, "imag", _rational(self.imag))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Gaussian) else Gaussian(_rational(x))

    def __add__(self, other):
        b = self.coerce(other)
        return Gaussian(self.real + b.real, self.imag + b.imag)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __mul__(self, other):
        b = self.coerce(other)
        return Gaussian(self.real*b.real-self.imag*b.imag,
                        self.real*b.imag+self.imag*b.real)

    __rmul__ = __mul__

    def conjugate(self):
        return Gaussian(self.real, -self.imag)

    def norm_squared(self):
        return self.real*self.real + self.imag*self.imag

    def __truediv__(self, other):
        b = self.coerce(other)
        if not b.norm_squared():
            raise ArithmeticTFDError("division by zero amplitude")
        numerator = self * b.conjugate()
        return Gaussian(numerator.real/b.norm_squared(), numerator.imag/b.norm_squared())


def _amplitudes(amplitudes):
    if not isinstance(amplitudes, dict) or len(amplitudes) > 10000:
        raise ArithmeticTFDError("bounded sparse amplitude dictionary required")
    return {_integer(n): Gaussian.coerce(a) for n, a in amplitudes.items()}


def thermal_amplitudes(cutoff, amplitude_exponent=1):
    """Unnormalised a_n=n^-s, 1<=n<=N, inverse temperature beta=2s."""
    _integer(cutoff)
    _integer(amplitude_exponent, 1, 12)
    return {n: Gaussian(Q(1, n**amplitude_exponent)) for n in range(1, cutoff+1)}


def norm_squared(amplitudes):
    return sum((a.norm_squared() for a in _amplitudes(amplitudes).values()), Q(0))


def reduced_probabilities(amplitudes):
    """Both partial traces of sum a_n|n,n> are diag(|a_n|²/Z)."""
    a = _amplitudes(amplitudes)
    z = norm_squared(a)
    if not z:
        raise ArithmeticTFDError("zero vector has no normalised density")
    return {n: v.norm_squared()/z for n, v in a.items()}


def mirror_residual(amplitudes, p, coefficient, *, output_cutoff=None):
    """Sparse residual of (V_p x I)psi-c(I x V_p*)psi, zero extending input.

    Default output retains leakage to pN. output_cutoff=N also compresses
    BOTH output factors, and can misleadingly give zero at finite cutoff.
    """
    a = _amplitudes(amplitudes)
    _prime(p)
    c = Gaussian.coerce(coefficient)
    if output_cutoff is not None:
        _integer(output_cutoff)
    ns = set(a) | {n//p for n in a if n % p == 0}
    out = {}
    for n in sorted(ns):
        if output_cutoff is not None and p*n > output_cutoff:
            continue
        v = a.get(n, Gaussian()) - c*a.get(p*n, Gaussian())
        if v.norm_squared():
            out[(p*n, n)] = v
    return out


def residual_squared(amplitudes, p, coefficient, *, output_cutoff=None):
    z = norm_squared(amplitudes)
    if not z:
        raise ArithmeticTFDError("zero vector has no normalised residual")
    r = mirror_residual(amplitudes, p, coefficient, output_cutoff=output_cutoff)
    return sum((a.norm_squared() for a in r.values()), Q(0))/z


def thermal_cutoff_residual(cutoff, p, amplitude_exponent=1):
    """Closed formula, independent of sparse operator application."""
    a = thermal_amplitudes(cutoff, amplitude_exponent)
    _prime(p)
    z = norm_squared(a)
    tail = sum((Q(1, n**(2*amplitude_exponent))
                for n in range(cutoff//p+1, cutoff+1)), Q(0))
    return tail/z


def thermal_tail_bound(cutoff, p, amplitude_exponent=1):
    """R_N² <= M^(1-beta)/((beta-1) Z_N), M=floor(N/p)>=1."""
    a = thermal_amplitudes(cutoff, amplitude_exponent)
    _prime(p)
    m = cutoff//p
    if not m:
        return Q(1)
    beta = 2*amplitude_exponent
    return Q(1, (beta-1)*m**(beta-1))/norm_squared(a)


def interior_mirror_defects(amplitudes, p, coefficient):
    """Tests only declared coefficient pairs n,pn, NOT an infinite law."""
    a = _amplitudes(amplitudes)
    _prime(p)
    c = Gaussian.coerce(coefficient)
    return {n: a[n]-c*a[p*n] for n in sorted(a)
            if p*n in a and (a[n]-c*a[p*n]).norm_squared()}


def reconstruct_smooth_prefix(coefficients, cutoff):
    """a_1=1, a_n=prod c_p^-v_p(n) for supported smooth n<=cutoff.

    Missing-prime coordinates are omitted, not certified zero globally.
    """
    _integer(cutoff)
    if not isinstance(coefficients, dict):
        raise ArithmeticTFDError("prime-indexed coefficient dictionary required")
    cs = {_prime(p): Gaussian.coerce(c) for p, c in coefficients.items()}
    if any(not c.norm_squared() for c in cs.values()):
        raise ArithmeticTFDError("nonzero mirror coefficients required")
    out = {}
    for n in range(1, cutoff+1):
        r, a = n, Gaussian(1)
        for p, c in sorted(cs.items()):
            while r % p == 0:
                r //= p
                a = a/c
        if r == 1:
            out[n] = a
    return out


def pure_overlap_squared(a, b):
    """Fidelity of two normalised diagonal-pair pure states; exact Q(i)."""
    a, b = _amplitudes(a), _amplitudes(b)
    za, zb = norm_squared(a), norm_squared(b)
    if not za or not zb:
        raise ArithmeticTFDError("nonzero states required")
    overlap = sum((v.conjugate()*b.get(n, Gaussian()) for n,v in a.items()), Gaussian())
    return overlap.norm_squared()/(za*zb)


def finite_prime_kernel_projection_squared(amplitudes, coefficients):
    """Exact ||P_F a||², where P_F projects to the INFINITE F-mirror kernel.

    Finite input, closed-form geometric tails. Real rational coefficients>1
    make both the normalisation product and spectral gap rational. The
    amplitude source may still be complex Q(i).
    """
    a = _amplitudes(amplitudes)
    if not isinstance(coefficients, dict):
        raise ArithmeticTFDError("prime-indexed coefficient dictionary required")
    cs = {_prime(p): _rational(c) for p,c in coefficients.items()}
    if any(c <= 1 for c in cs.values()):
        raise ArithmeticTFDError("projection oracle requires real c_p>1")
    normalizer = Q(1)
    for c in cs.values():
        normalizer *= 1-Q(1)/(c*c)
    rough_overlaps = {}
    for n,v in a.items():
        r, weight = n, Q(1)
        for p,c in cs.items():
            while r % p == 0:
                r //= p
                weight /= c
        rough_overlaps[r] = rough_overlaps.get(r,Gaussian()) + weight*v
    return normalizer*sum((v.norm_squared() for v in rough_overlaps.values()),Q())


def finite_mirror_gap_certificate(amplitudes, coefficients):
    """Finite-F spectral-gap theorem with the genuine infinite kernel."""
    a = _amplitudes(amplitudes)
    if not coefficients:
        raise ArithmeticTFDError("nonempty finite prime family required")
    projection = finite_prime_kernel_projection_squared(a,coefficients)
    cs = {p:_rational(c) for p,c in coefficients.items()}
    z = norm_squared(a)
    if not z:
        raise ArithmeticTFDError("nonzero finite source required")
    energy = sum((z*residual_squared(a,p,c) for p,c in cs.items()),Q())
    gap = min((c-1)**2 for c in cs.values())
    distance = z-projection
    return {"norm_squared":z,"projection_squared":projection,
            "distance_squared":distance,"energy":energy,"gap":gap,
            "slack":energy-gap*distance}


def thermal_mirror_fidelity_certificate(amplitudes, prime_cutoff, amplitude_exponent=1):
    """Certified lower fidelity to INFINITE beta=2s TFD from weighted mirrors.

    Source has explicitly declared finite support<=prime_cutoff. The omitted
    genuine-prime residuals have an analytic rational majorant; this is not
    an extrapolation from finite experimental probes of an unknown source.
    """
    a = _amplitudes(amplitudes)
    _integer(prime_cutoff,2)
    _integer(amplitude_exponent,1,12)
    if any(n>prime_cutoff for n in a):
        raise ArithmeticTFDError("cutoff must cover entire declared source support")
    z = norm_squared(a)
    if not z:
        raise ArithmeticTFDError("nonzero finite source required")
    s = amplitude_exponent
    observed = sum((residual_squared(a,p,p**s)/((p**s-1)**2)
                    for p in range(2,prime_cutoff+1) if prime(p)),Q())
    tail = Q(1)/((1-Q(1,2**s))**2*(2*s-1)*prime_cutoff**(2*s-1))
    error_upper = observed+tail
    return {"weighted_energy_observed":observed,"weighted_energy_tail_upper":tail,
            "infidelity_upper":error_upper,
            "fidelity_lower":max(Q(0),1-error_upper),
            "source_scope":"declared finite support; analytic prime-tail lift"}


def probe():
    a = thermal_amplitudes(24)
    mutation = dict(a)
    mutation[6] = 2*mutation[6]
    phase = reconstruct_smooth_prefix({2: Gaussian(0, 2), 3: Gaussian(3)}, 24)
    certified2 = thermal_mirror_fidelity_certificate(thermal_amplitudes(100),100)
    certified4 = thermal_mirror_fidelity_certificate(thermal_amplitudes(16,2),16,2)
    return {
        "scope": "exact finite rational/Gaussian-rational arithmetic",
        "cutoff": 24,
        "beta": 2,
        "prime2_residual_squared": str(residual_squared(a, 2, 2)),
        "compressed_prime2_residual_squared": str(residual_squared(a, 2, 2, output_cutoff=24)),
        "oscillation_N2_N3": [str(thermal_cutoff_residual(n, 2)) for n in (2, 3)],
        "mutation6_prime2_defect_indices": list(interior_mirror_defects(mutation, 2, 2)),
        "mutation6_prime3_defect_indices": list(interior_mirror_defects(mutation, 3, 3)),
        "complex_phase_prime2_interior_defects": len(interior_mirror_defects(phase, 2, Gaussian(0,2))),
        "beta2_N100_certified_fidelity_above_9_10": certified2["fidelity_lower"] > Q(9,10),
        "beta4_N16_certified_fidelity_above_99_100": certified4["fidelity_lower"] > Q(99,100),
        "infinite_theorem_by_tests": False,
        "geometry_reconstructed": False,
        "RH_proved": False,
    }
