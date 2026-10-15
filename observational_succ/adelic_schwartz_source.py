"""Source-indexed Gaussian x compact-open finite-place Tate tensor.

Symbolic evaluation on the DIAGONAL Q lattice of the *actual* adelic
Schwartz-Bruhat function
   Phi_(q,d,t)(x) = exp(-pi*t*((x_inf-d)/q)^2)
                     * prod_p 1_(d+q Z_p)(x_p),
for q in Q^*, d in Q, t in Q_{>0}.
All but finitely many p factors equal the standard 1_Zp. Fourier formulas
are classical analytic imports; exact Fraction code verifies local support,
global product-modulus, phase reciprocity and lattice sum relabeling only.
It never constructs the full adele ring, a Haar integral or Weil positivity.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .diagonal_adele_zeta import (
    additive_reciprocity, multiplicative_reciprocity, rational, valuations,
)
from .tate_schwartz_functor import PadicBall, TateFunctorError


@dataclass(frozen=True)
class DiagonalGaussianTensor:
    """Finite symbolic description of one full standard adelic test function."""
    scale: F
    shift: F
    time: F = F(1)
    source_id: str = "Q-standard-tate-Gaussian"
    epoch: int = 0

    def __post_init__(self):
        q, d, t = rational(self.scale), rational(self.shift), rational(self.time)
        if not q or t <= 0:
            raise TateFunctorError("Global Tate Gaussian requires q != 0 and t > 0")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise TateFunctorError("Global source identifier required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise TateFunctorError("Global source epoch must be nonnegative")
        object.__setattr__(self, "scale", q)
        object.__setattr__(self, "shift", d)
        object.__setattr__(self, "time", t)

    def exceptional_places(self) -> tuple[int, ...]:
        """Only primes affecting the standard finite-source tensor."""
        out = set(valuations(self.scale))
        if self.shift:
            out.update(p for p, v in valuations(self.shift).items() if v < 0)
        return tuple(sorted(out))

    def local_ball(self, p: int) -> PadicBall:
        """Genuine p-field factor 1_(d+q Zp); no composite fake places."""
        v = valuations(self.scale).get(p, 0)
        return PadicBall(p, self.shift, v, self.source_id, self.epoch)

    def at_rational(self, x: int | F) -> dict:
        """Exact support and Gaussian exponent at diagonally embedded Q."""
        x = rational(x)
        z = (x-self.shift)/self.scale
        support = z.denominator == 1
        return {
            "sample": x, "nonzero": support,
            "integer_label_if_nonzero": int(z) if support else None,
            "Gaussian_exponent_pi": self.time*z*z if support else None,
            "certified_all_finite_places_by_rational_integrality": True,
            "value_symbolic": "exp(-pi*Gaussian_exponent_pi)" if support else "0",
            "full_adelic_topology_computed": False,
        }

    def fourier_at_rational(self, xi: int | F) -> dict:
        """All-place Fourier on a diagonal rational frequency, symbolically.

        Local Fourier is taken with psi_inf(x)=exp(2pi i x),
        psi_p(x)=exp(-2pi i {x}_p), exactly the Tate character convention.
        For a fixed rational xi, the only active finite primes divide the
        denominators/valuations of q, d, or xi.
        """
        xi = rational(xi)
        q, d = self.scale, self.shift
        qxi = q*xi
        finite_support = (qxi.denominator == 1)
        active = set(self.exceptional_places())
        if xi:
            active.update(valuations(xi))
        active = tuple(sorted(active))
        locals_ = {p: self.local_ball(p).fourier(xi) for p in active}

        # On this rational chart these exact tests must equal the global
        # condition q*xi in Z. An unobserved p is never silently discarded.
        if all(t.amplitude for t in locals_.values()) != finite_support:
            raise AssertionError("Finite-place support did not match global Z intersection")

        norm = multiplicative_reciprocity(q)
        if norm["global_product"] != 1:
            raise AssertionError("The rational lattice must have product modulus one")

        ax = additive_reciprocity(d*xi)
        # additive_reciprocity uses real - and finite +; our local Fourier
        # chooses the globally opposite (+ real, - finite), which also cancels.
        real_phase = (d*xi) % 1
        finite_phase = sum((c.phase for c in locals_.values()), F(0)) % 1 if finite_support else F(0)
        phase_total = (real_phase + finite_phase) % 1 if finite_support else F(0)
        if finite_support and (phase_total != 0 or not ax["diagonal_character_trivial"]):
            raise AssertionError("Global Tate phase reciprocity failed")

        finite_modulus = F(1)
        for t in locals_.values():
            if t.amplitude:
                finite_modulus *= t.amplitude
        if finite_support and abs(q)*finite_modulus != 1:
            raise AssertionError("Archimedean/finite Haar scaling did not cancel")

        return {
            "frequency": xi, "finite_active_places": active,
            "local_Fourier_values": locals_,
            "finite_support": finite_support,
            "source_integral_label": int(qxi) if finite_support else None,
            "real_phase": real_phase if finite_support else F(0),
            "finite_phase": finite_phase,
            "global_phase": phase_total,
            "global_Haar_affine_scaling": F(1),
            "gaussian_exponent_pi": qxi*qxi/self.time if finite_support else None,
            "Gaussian_amplitude_symbolic": "1/sqrt(time)" if finite_support else "0",
            "all_places_formula": "t^-1/2 * exp(-pi*(q*xi)^2/t)"
                                  if finite_support else "0",
            "phase_cancellation_proved_exact_on_diagonal": finite_support,
            "full_Poisson_formula_proved_by_finite_samples": False,
            "Weil_positive": False,
            "RH_proved": False,
        }

    def affine(self, multiplier: int | F, increment: int | F) -> "DiagonalGaussianTensor":
        """Apply x -> m*x+d to the physical input carrier, preserving t."""
        m, d = rational(multiplier), rational(increment)
        if not m:
            raise TateFunctorError("Affine field multiplication must be invertible")
        return DiagonalGaussianTensor(self.scale*m, self.shift*m+d,
                                      self.time, self.source_id, self.epoch)

    def poisson_index_receipt(self, index: int) -> dict:
        """The two rational lattice sums are indexed by the SAME integer Z.

        The equality of the Gaussian sums theta(t)=t^-1/2 theta(1/t)
        still uses genuine Poisson summation (CLASSICAL IMPORT).
        """
        if type(index) is not int:
            raise TateFunctorError("Original source lattice index must be an integer")
        original_x = self.shift + self.scale*index
        dual_xi = F(index)/self.scale
        primal = self.at_rational(original_x)
        dual = self.fourier_at_rational(dual_xi)
        if (not primal["nonzero"] or not dual["finite_support"] or
                primal["integer_label_if_nonzero"] != index or
                dual["source_integral_label"] != index):
            raise AssertionError("Source-indexed lattice bijection failed")
        return {
            "index": index, "primal_lattice_point": original_x,
            "dual_lattice_point": dual_xi,
            "primal_Gaussian_exponent_pi": primal["Gaussian_exponent_pi"],
            "dual_Gaussian_exponent_pi": dual["gaussian_exponent_pi"],
            "dual_global_phase": dual["global_phase"],
            "matched_original_integer_source": True,
            "theta_functional_equation_proved_by_this_finite_index": False,
            "RH_proved": False,
        }
