"""Source-typed complete Weil distribution for zeta and primitive chi_4.

The all-test identification is a classical contour theorem, derived in
research/2026-10-15/TATE_TO_WEIL_DISTRIBUTION.md.  These routines execute
finite source interfaces and exact analytic error budgets, not that theorem.
No zero locations are read.  Callable evaluation is numerical, never an
interval certificate.  Supremum bounds are explicit mathematical premises.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .completed_weil_transport import von_mangoldt_labels
from .diagonal_adele_zeta import rational
from .source_character_interaction import character_four
from .tate_weil_window import CompactWeilSourceWindow


@dataclass(frozen=True)
class TateWeilSource:
    """Two canonical mathematical sources; a source_id is not attestation."""

    character: str = "zeta"
    source_id: str = "canonical-rational-arithmetic"
    epoch: int = 0

    def __post_init__(self):
        if self.character not in ("zeta", "chi4"):
            raise ValueError("Only the reconstructed zeta and primitive chi4 sources")
        if not isinstance(self.source_id, str) or not self.source_id:
            raise ValueError("Declared source ID required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise ValueError("Nonnegative integer source epoch required")

    @classmethod
    def from_tate(cls, source):
        """Preserve declared provenance from one canonical upstream test.

        This adapter accepts only the two proved source types, not arbitrary
        Fourier-selfdual tests: those can introduce extra Mellin divisors.
        """
        from .tate_idelic_zeta import StandardTateSource
        from .tate_chi4 import Chi4TateSource
        if type(source) is StandardTateSource:
            return cls("zeta", source.source_id, source.epoch)
        if type(source) is Chi4TateSource:
            return cls("chi4", source.source_id, source.epoch)
        raise ValueError("Canonical StandardTateSource or Chi4TateSource required")

    @property
    def conductor(self):
        return 1 if self.character == "zeta" else 4

    @property
    def parity(self):
        return 0 if self.character == "zeta" else 1

    @property
    def pole_multiplicity(self):
        return int(self.character == "zeta")

    @property
    def alpha(self):
        return Q(1, 2) + self.parity

    def chi(self, n):
        if type(n) is not int:
            raise ValueError("Integer arithmetic source required")
        return 1 if self.character == "zeta" else character_four(n)

    def atoms(self, radius):
        """(n,p,chi(n)) labels for all possible impulses in [-R,R].

        Conservative exact cutoff: n < 3^ceil(R).  This finite implementation
        accepts 0<R<=10; the paper theorem has no support bound. Tests may vanish
        on some of these labels.  n=p^k carries log(p), NOT log(n).
        """
        r = rational(radius)
        if r <= 0:
            raise ValueError("Positive rational support radius required")
        labels = CompactWeilSourceWindow(r / 2).certificate()[
            "included_genuine_prime_power_labels"
        ]
        return tuple((n, p, self.chi(n)) for n, p in labels if self.chi(n))

    def verify_tape(self, radius, tape):
        """Reject omissions, duplicates, fake 6 and signed non-Euler tapes."""
        actual = tuple(tape)
        if any(type(row) is not tuple or len(row) != 3 or
               any(type(x) is not int for x in row) for row in actual):
            raise ValueError("Exact integer (n,p,chi(n)) records required")
        if actual != self.atoms(radius):
            raise ValueError("Tape differs from the declared canonical arithmetic source")
        return True

    def require_normalization(self, *, conductor, parity, half_density,
                              pole_multiplicity, root_number):
        """Upstream source contract, not an inference from Weil observations.

        Logarithmic derivatives forget overall scalar normalization. The
        differentiated functional equation omits the displayed root constant;
        this finite contract relies on independent Fourier certification.
        Full global logarithmic data plus self-duality can recover the root
        number from the parity of the central zero/pole order.
        """
        if (type(conductor) is not int or type(parity) is not int or
                type(pole_multiplicity) is not int or
                conductor != self.conductor or parity != self.parity or
                rational(half_density) != Q(1, 2) or
                pole_multiplicity != self.pole_multiplicity or
                rational(root_number) != 1):
            raise ValueError("Wrong conductor/parity/half-density/poles/root contract")
        return True

    def gamma_tail(self, J, *, M0, M1):
        """Exact bound |A-A_J| <= (M0+2M1)(1/(2a)+1/a²).

        Premises: g in C_c^1, ||g||inf<=M0, ||g'||inf<=M1;
        a=2J+parity+1/2.  Does not bound finite quadrature error.
        """
        a = self._rung(J)
        m0, m1 = _bounds(M0, M1)
        return (m0 + 2*m1) * (1/(2*a) + 1/a**2)

    def accelerated_gamma_tail(self, J, *, M0, M2):
        """O(J^-2) after subtracting g(0)/(2a) from A_J; C_c^2 premise."""
        a = self._rung(J)
        m0, m2 = _bounds(M0, M2)
        return m0/a**2 + (m2 + m0/4) * (1/(2*a**2) + 2/a**3)

    def _rung(self, J):
        if type(J) is not int or J < 1:
            raise ValueError("Positive finite Gamma ladder depth required")
        return 2*J + self.alpha

    def continuity_budget(self, radius, *, delta0, delta1):
        """Rational majorant for |W(g)-W(h)| on one fixed support [-R,R].

        delta0>=||g-h||inf, delta1>=||g'-h'||inf are premises.  Uses
        log(p)/sqrt(n)<p, e<3, |c_zeta|<4, |c_chi4|<2.  Deliberately
        coarse, but valid for arbitrary compact C^1 tests, not one tent.
        """
        r = rational(radius)
        d0, d1 = _bounds(delta0, delta1)
        atoms = self.atoms(r)
        ceil_half = _ceil(r/2)
        pole = self.pole_multiplicity * 4*r*3**ceil_half
        prime = 2*sum(p for _, p, _ in atoms)
        contact = 4 if self.character == "zeta" else 2
        integral = 1/self.alpha**2 + 1/(2*self.alpha)
        return (pole + prime + contact + integral)*d0 + 2*integral*d1


def _ceil(x):
    return -((-x.numerator)//x.denominator)


def _bounds(*args):
    values = tuple(rational(x) for x in args)
    if any(x < 0 for x in values):
        raise ValueError("Nonnegative rational norm/error bounds required")
    return values


def pointwise_negative_bump_certificate(width=Q(1, 100)):
    """Authentic zeta W is not positive on all pointwise nonnegative tests.

    Let g be any smooth bump, 0<=g<=1, g(log 2)=1, supported in
    (log 2-width,log 2+width). For 0<width<=1/100 only n=2 contributes,
    g(0)=0, A(g)<=0, pole<8*width and prime< -1/3. Thus W(g)<bound<0.
    This is NOT an autocorrelation: g(0)=0 while g is nonzero.
    Proof of interval isolation and elementary bounds is in the note.
    """
    w = rational(width)
    if not 0 < w <= Q(1, 100):
        raise ValueError("Proved bump isolation domain 0<width<=1/100")
    return {"prime": 2, "width": w, "pole_upper": 8*w,
            "prime_upper": -Q(1, 3), "gamma_upper": Q(0),
            "strict_Weil_upper": 8*w-Q(1, 3),
            "pointwise_nonnegative_test": True,
            "autocorrelation_test": False, "RH_proved": False}


def evaluate_compact_numeric(source, g, radius, *, knots=(), J=None, dps=40):
    """Numerical complete source evaluation, on a DECLARED compact C^2 test.

    The support, smoothness and any norm envelopes are caller premises;
    no finite sampling verifies them. All prime labels come from the same
    canonical source as the analytic formula. No zero oracle is consulted.
    J=None integrates the full Gamma kernel; J>=1 uses its finite ladder.
    Quadrature is diagnostic and has NO certified error interval.
    """
    import mpmath as mp
    if not isinstance(source, TateWeilSource):
        raise ValueError("Typed Tate/Weil source required")
    radius = rational(radius)
    atoms = source.atoms(radius)
    breaks = sorted({Q(0), radius, *(rational(x) for x in knots)})
    if breaks[0] != 0 or breaks[-1] != radius:
        raise ValueError("Quadrature knots must be in [0,R]")
    if J is not None:
        source._rung(J)
    if type(dps) is not int or not 25 <= dps <= 150:
        raise ValueError("Working precision 25..150 required")
    with mp.workdps(dps):
        m = lambda q: mp.mpf(q.numerator)/q.denominator
        R = m(radius)
        xs = [m(x) for x in breaks]
        h0 = g(mp.mpf(0))
        alpha = m(source.alpha)
        c = mp.log(source.conductor/mp.pi) + mp.digamma(mp.mpf(source.parity+1)/2)

        def sym(x):
            return g(x)+g(-x)

        def integrand(x):
            if x == 0:
                return h0/2 if J is None else mp.mpf(0)
            density = sym(x)-2*h0-2*h0*mp.expm1(-x/2)
            kernel = mp.exp(-alpha*x)/(-mp.expm1(-2*x))
            if J is not None:
                kernel *= -mp.expm1(-2*J*x)
            return kernel*density

        arch = c*h0-mp.quad(integrand, xs+[mp.inf])
        poles = source.pole_multiplicity*mp.quad(
            lambda x: sym(x)*(mp.exp(x/2)+mp.exp(-x/2)), xs)
        prime = -mp.fsum(mp.log(p)*chi/mp.sqrt(n)*sym(mp.log(n))
                         for n, p, chi in atoms if mp.log(n) <= R)
        return {"pole": poles, "prime": prime, "gamma": arch,
                "value": poles+prime+arch, "quadrature_certified": False,
                "zero_positions_used": False, "RH_proved": False}
