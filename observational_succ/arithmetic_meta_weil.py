"""Arithmetic Meta-SUCC: genuine prime dilation, Gamma boundary leakage, and a
source-specific infinite-dimensional high-moment Weil certificate.

Honesty boundary: this is NOT a proof of RH or global Weil positivity.
The complete signed Q_W is an EXTERNAL CLASSICAL Weil/Suzuki identity.
All asserted numerically certified margins in this module use exact Fraction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import ceil, factorial, isqrt


class ArithmeticMetaError(ValueError):
    """Violation of the declared source or exact certificate contract."""


@dataclass(frozen=True)
class SourceContract:
    source_id: str = "Riemann-zeta-Euler-primes-Q"
    epoch: int = 0
    coordinate: str = "log-half-density-L2R"
    gamma_conductor: int = 1
    gamma_parity: int = 0
    half_density: F = F(1, 2)

    def __post_init__(self) -> None:
        if (type(self.epoch) is not int or type(self.gamma_conductor) is not int
                or type(self.gamma_parity) is not int or type(self.half_density) is not F
                or self.source_id != "Riemann-zeta-Euler-primes-Q" or self.epoch != 0
                or self.coordinate != "log-half-density-L2R"
                or self.gamma_conductor != 1 or self.gamma_parity != 0
                or self.half_density != F(1, 2)):
            raise ArithmeticMetaError("source/epoch/coordinate/half-density/Gamma mutation")


def _is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    return all(n % p for p in range(2, isqrt(n) + 1))


def prime_power_jet(n: int) -> tuple[int, int] | None:
    """Exact primitive Euler p^k provenance; 6 is NOT a primitive jet."""
    if type(n) is not int or n < 2:
        return None
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            if not _is_prime(p):
                continue
            k, m = 0, n
            while m % p == 0:
                m //= p
                k += 1
            return (p, k) if m == 1 else None
    return (n, 1)


def authentic_prime_tape(N: int, contract: SourceContract | None = None):
    """Labels only; weights are symbolic log(p)/sqrt(p^k), not floats."""
    if type(N) is not int or N < 1:
        raise ArithmeticMetaError("positive integer source cutoff required")
    _ = contract if contract is not None else SourceContract()
    if not isinstance(_, SourceContract):
        raise ArithmeticMetaError("no untyped source admission")
    return tuple((n, *jet) for n in range(2, N + 1) if (jet := prime_power_jet(n)) is not None)


def prime_commuting_square(n: int, p: int, q: int) -> bool:
    """Multiplicativity square on the original integer source, not a model fit."""
    if type(n) is not int or n < 1 or not _is_prime(p) or not _is_prime(q):
        raise ArithmeticMetaError("positive integer and two genuine primes required")
    return p * (q * n) == q * (p * n)


def half_density_unitary_indicator_demo(alpha: F) -> F:
    """Exact squared transformed norm of f=1_[1,2] at α=1/2 or 1.

    In general U_alpha f(u)=exp(alpha*u) f(exp u) has squared norm
    int_1^2 x^(2alpha-1) dx.  This is a finite demonstration, not the proof
    of full L2 unitarity (provided in the paper dossier).
    """
    if alpha == F(1, 2):
        return F(1)
    if alpha == F(1):
        return F(3, 2)
    raise ArithmeticMetaError("only exact rational demonstration controls supported")


def gamma_carlemann_sample_2log2(distance: int) -> F:
    """Exact ν_0(2*log(2)*distance) = 2^|d|/(4^|d|+1)."""
    if type(distance) is not int:
        raise ArithmeticMetaError("integer dyadic clock distance required")
    d = abs(distance)
    return F(2 ** d, 4 ** d + 1)


def _mm(A: tuple[tuple[F, ...], ...], B: tuple[tuple[F, ...], ...]):
    n = len(A)
    if not n or any(len(row) != n for row in A + B) or len(B) != n:
        raise ArithmeticMetaError("square rational matrices required")
    return tuple(tuple(sum((A[i][k] * B[k][j] for k in range(n)), F(0))
                       for j in range(n)) for i in range(n))


def dyadic_window_commutator(n: int = 3):
    """Rational sampled real-Gamma kernel vs genuine jet-4 shift.

    Calibration only: point-sampling is NOT a continuum Galerkin matrix.
    Continuum commutator/no-go and norm bound are separately proved.
    """
    if type(n) is not int or n < 2:
        raise ArithmeticMetaError("at least two dyadic clock sites")
    K = tuple(tuple(gamma_carlemann_sample_2log2(i-j)
                    for j in range(n)) for i in range(n))
    S = tuple(tuple(F(int(j == i + 1)) for j in range(n)) for i in range(n))
    SK, KS = _mm(S, K), _mm(K, S)
    return K, S, tuple(tuple(SK[i][j] - KS[i][j] for j in range(n)) for i in range(n))


def finite_shift_energy_identity(values: tuple[F, ...], step: int):
    """Exact full-line zero-extension identity for a prime clock shift:

    ||T_step v - v||² - 2||v||² = -2 Re <T_step v, v>.

    The weight log(p)/sqrt(p^k) is SOURCE-derived separately, not fitted.
    """
    if not values or any(not isinstance(v, (int, F)) for v in values):
        raise ArithmeticMetaError("exact nonempty rational finite signal required")
    if type(step) is not int or step < 1:
        raise ArithmeticMetaError("positive shift step required")
    x = tuple(map(F, values))
    d = len(x)
    def v(i):
        return x[i] if 0 <= i < d else F(0)
    norm = sum((y*y for y in x), F(0))
    overlap = sum((v(i + step)*v(i) for i in range(d)), F(0))
    energy = sum(((v(i+step) - v(i))**2 for i in range(-step, d)), F(0))
    return {"norm": norm, "overlap": overlap, "energy": energy,
            "source_signed_prime_term": -2*overlap,
            "corrected_square": energy - 2*norm}


def gamma_rungs_multiplier_lower(T: int = 40, J: int = 75) -> F:
    """Certified rational lower bound to the authentic Gamma symbol M_G(T).

    M_G(T)=sum_{j>=0} 2 T²/(α_j(α_j²+T²)), α_j=2j+1/2.
    No digamma values, zeta zeros, or floating arithmetic used.
    """
    if type(T) is not int or T < 1 or type(J) is not int or J < 1:
        raise ArithmeticMetaError("finite positive Gamma-rung certificate parameters")
    T2 = T*T
    return sum((F(2*T2)/(F(4*j+1, 2)*(F(4*j+1, 2)**2 + T2))
                for j in range(J)), F(0))


def moment_fourier_leak_upper(a: F, T: int, N: int) -> F:
    """Exact rational majorant for low-frequency Fourier mass on moment-null v.

    (1/(2π))∫_{-T}^T |vhat|² ≤ E_N(a,T) ||v||².
    Uses π>3 and e^x<4^ceil(x) for positive x; deliberately loose.
    """
    if type(a) is not F or a <= 0 or type(T) is not int or T <= 0 or type(N) is not int or N < 0:
        raise ArithmeticMetaError("exact a rational, integer T>0 and moment N>=0 required")
    return F(2*a*T, 3)*4**ceil(2*a*T)*(a*T)**(2*(N+1))/factorial(N+1)**2


def first_prime_moment_100_certificate() -> dict:
    """A fully rational, source-conditional whole-test-space theorem:

    For every v∈C_c^∞(-1/2,1/2) with ∫x^k v=0 for k=0..100,
    Q_zeta(v) > (291/5000)||v||².

    The paper proof imports the classical complete *signed* Weil/Suzuki form,
    the real-source Gamma ladder, elementary inequalities on constants, and
    zero locations nowhere. This routine certifies two explicit integer
    comparisons, not the imported analytic theorem independently.
    """
    a, T, J, N = F(1, 2), 40, 75, 100
    low = gamma_rungs_multiplier_lower(T, J)
    leak = moment_fourier_leak_upper(a, T, N)
    if not low > F(359, 50):
        raise ArithmeticMetaError("finite rational 75-rung bound failed")
    if not leak < F(1, 100):
        raise ArithmeticMetaError("moment Fourier budget failed")
    # C_G<6, 2 w_2<1, 2||sinh(x/2)||²<1/20 at a=1/2.
    budget = F(141,20)
    exact_margin = F(359,50)*F(99,100)-budget
    if exact_margin != F(291,5000) or exact_margin <= 0:
        raise ArithmeticMetaError("exact margin did not certify")
    return {"radius": "1/2", "gamma_frequency": 40,
            "gamma_rungs": J, "moment_order": N,
            "gamma_finite_lower": "359/50", "gamma_comparison_holds": low > F(359,50),
            "leak_upper": "1/100", "leak_comparison_holds": leak < F(1,100),
            "signed_source_budget": "141/20", "certified_all_test_margin": str(exact_margin),
            "RH_proved": False, "whole_space_unrestricted": False}


def abstract_flat_holonomy_word(prime_steps: tuple[tuple[int,int], ...]) -> int:
    """Compute integral valuation log-clock exponent for one prime at a time.

    Commutators of authentic translations vanish; no frustration invented.
    The result 0 is the identity transport on the continuous log carrier.
    """
    total = 0
    for p, e in prime_steps:
        if not _is_prime(p) or type(e) is not int:
            raise ArithmeticMetaError("genuine prime generator and signed exponent required")
        total += e   # only for a single common prime; caller must check p
    if len({p for p,_ in prime_steps}) > 1:
        raise ArithmeticMetaError("one-coordinate exponent requires one prime; use valuation vectors otherwise")
    return total


def valuation_holonomy(prime_steps: tuple[tuple[int,int], ...]):
    """True multi-prime abelian clock: identity iff *every* valuation sum 0."""
    totals: dict[int,int] = {}
    for p,e in prime_steps:
        if not _is_prime(p) or type(e) is not int:
            raise ArithmeticMetaError("genuine p^e arithmetic label required")
        totals[p] = totals.get(p, 0)+e
    return tuple(sorted((p,e) for p,e in totals.items() if e))


def signed_non_euler_character4_prime_weight(n: int):
    """Control: χ4 primitive character introduces signed w_3, unlike zeta.

    χ4 weight is not an honest nonnegative zeta prime-square coefficient.
    Completion requires conductor 4 and odd Gamma parity, not zeta's.
    """
    jet=prime_power_jet(n)
    if jet is None:
        return 0
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def first_prime_boundary_commutator_certificate() -> dict:
    """Entirely rational proof-of-constants supporting continuum commutator:

    On W=(-1/2,1/2), b=log 2, S=P T_b P, K=P (ν_0*) P,
    ||[S,K]|| > 3/22.  Actual operator argument is in dossier;
    this routine proves all rational ingredient inequalities only.
    """
    # Using log2=2 arctanh(1/3): 2/3 < log2 < 25/36 < 7/10.
    assert F(25,36) < F(7,10)
    # δ=(1-b)/2 > 3/20, b δ > (2/3)*(3/20)=1/10.
    assert F(2,3)*F(3,20)==F(1,10)
    # t=(b+δ)/2=(1+b)/4 < 17/40.
    t2over2 = F(17,40)**2 / 2
    cosh_upper=1/(1-t2over2)  # cosh t <= 1/(1-t²/2)
    assert cosh_upper < F(11,10)
    # Hence ν0(b+δ)>1/(2*(11/10))=5/11.
    assert F(1)/(2*F(11,10)) == F(5,11)
    assert F(3,10)**2 < F(1,10)
    # √(b δ)*ν0(b+δ) > (3/10)*(5/11) = 3/22.
    assert F(3,10)*F(5,11) == F(3,22)
    return {"window_half_width":"1/2", "prime":"2", "gamma_layer":"nu_0 Carleman",
            "commutator_norm_strictly_greater_than":"3/22",
            "rational_bound_check": True, "transport_was_unitary_after_compression":False,
            "RH_proved":False}


def independent_tent_weil_oracle(radius: str = "0.5", dps: int = 45):
    """OPTIONAL high-precision diagnostic (NOT interval arithmetic).

    Two separately implemented time-side original Weil and Gamma-Carleman
    formulas for v(x)=(1-|x|/a)_+. Original prime tape, no zero locations.
    All exact theorem margins above remain Fraction, independent of this oracle.
    """
    import mpmath as mp
    mp.mp.dps=dps
    a=mp.mpf(radius)
    if not (a>0):
        raise ArithmeticMetaError("a must be positive")
    h0=2*a/3
    def h(t):
        t=abs(t)
        if t<=a:
            return h0-t*t/a+t**3/(2*a*a)
        if t<=2*a:
            return (2*a-t)**3/(6*a*a)
        return mp.mpf(0)
    def k(t):
        return mp.exp(-t/2)/(1-mp.exp(-2*t))
    def kb(t):
        s=mp.exp(-t/2)
        return mp.atanh(s)+mp.atan(s)
    source=[]
    for n in range(2,int(mp.ceil(mp.exp(2*a)))+1):
        if mp.log(n)>=2*a:continue
        j=prime_power_jet(n)
        if j is not None:source.append((n,mp.log(j[0])/mp.sqrt(n)))
    P=4*mp.quad(lambda t: h(t)*mp.cosh(t/2),[0,a,2*a])
    prime=-2*sum((w*h(mp.log(n)) for n,w in source),mp.mpf(0))
    def arch_integrand(t):
        if t==0: return h0/2
        return k(t)*(2*h(t)-2*mp.exp(-t/2)*h0)
    arch=-(mp.euler+mp.log(4*mp.pi))*h0 - mp.quad(arch_integrand,[0,a,2*a]) + 2*h0*mp.atanh(mp.exp(-2*a))
    original=P+prime+arch
    def pos_integrand(t):
        if t==0:return mp.mpf(0)
        return 2*k(t)*(h0-h(t))
    Eg=mp.quad(pos_integrand,[0,a,2*a])+2*h0*kb(2*a)
    C=8*(mp.cosh(a/2)-1)/a
    reconstructed=Eg-(mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi))*h0+2*C**2+prime
    return {"radius":str(a), "source_prime_powers":[n for n,_ in source],
            "original_W":mp.nstr(original,dps-5),
            "source_carlemann":mp.nstr(reconstructed,dps-5),
            "difference":mp.nstr(abs(original-reconstructed),10),
            "gamma_energy":mp.nstr(Eg,25),
            "signed_prime_term":mp.nstr(prime,25),
            "test_function":"triangular H1_0", "zero_positions_used":False,
            "rigorous_interval_certificate":False}


def _frac_det(M: tuple[tuple[F,...], ...]) -> F:
    """Exact determinant using independent Leibniz permutations, small n only."""
    from itertools import permutations
    n=len(M)
    if any(len(r)!=n for r in M):
        raise ArithmeticMetaError("square Gram matrix required")
    s=F(0)
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=F(-1 if inversions%2 else 1)
        for i in range(n):term*=M[i][p[i]]
        s+=term
    return s


def exact_finite_schur_sufficiency(
    kappa: F, low_form: tuple[tuple[F,...],...],
    cross_image_gram: tuple[tuple[F,...],...]
) -> dict:
    """A SOUND abstract finite-dimensional *sufficient* condition, not RH.

    If Q(u)>=kappa||u||² on the moment-null complement and low span has
    Q(f_i,f_j)=low_form, <Af_i,Af_j>=cross_image_gram, then PSD of
    M=low_form - kappa^-1 cross_image_gram implies Q>=0 on the entire domain.
    All matrices here MUST be externally certified as those actual source data.
    """
    from itertools import combinations
    if not isinstance(kappa,F) or kappa<=0:
        raise ArithmeticMetaError("strict rational complement gap required")
    n=len(low_form)
    if not (0<n<=8 and len(cross_image_gram)==n):
        raise ArithmeticMetaError("small, nonempty fixed-size Gram required")
    def convert(A):
        if any(len(r)!=n or any(not isinstance(v,(int,F)) for v in r) for r in A):
            raise ArithmeticMetaError("exact full real Gram matrix required")
        B=tuple(tuple(F(v) for v in row) for row in A)
        if any(B[i][j]!=B[j][i] for i in range(n) for j in range(n)):
            raise ArithmeticMetaError("symmetric data required")
        return B
    A=convert(low_form); B=convert(cross_image_gram)
    M=tuple(tuple(A[i][j]-B[i][j]/kappa for j in range(n)) for i in range(n))
    for m in range(1,n+1):
        for idx in combinations(range(n),m):
            if _frac_det(tuple(tuple(B[i][j] for j in idx) for i in idx)) < 0:
                raise ArithmeticMetaError("cross-image Gram must be PSD")
    minors=[]
    for m in range(1,n+1):
        for idx in combinations(range(n),m):
            determinant=_frac_det(tuple(tuple(M[i][j] for j in idx) for i in idx))
            minors.append((idx,determinant))
    return {"sufficient_for_full_form":all(x>=0 for _,x in minors),
            "source_operator_identified_here":False,
            "corrected_matrix":tuple(tuple(str(y) for y in row) for row in M),
            "principal_minors":tuple((ix,str(det)) for ix,det in minors)}


def moment_fourier_leak_sharp_upper(a: F, T: int, N: int) -> F:
    """Sharper rational majorant using |exp(iy)-Taylor_N(iy)|<=|y|^(N+1)/(N+1)!
    for real y: integral remainder has |exp(ity)|=1; NO e^(aT) loss.
    """
    if type(a) is not F or a<=0 or type(T) is not int or T<=0 or type(N) is not int or N<0:
        raise ArithmeticMetaError("exact a,T,N needed")
    return F(2*a*T,3)*(a*T)**(2*(N+1))/factorial(N+1)**2


def improved_first_prime_moment_29_certificate() -> dict:
    """Better authentic completed-Weil whole-subspace theorem:

    For ALL v∈C_c∞(-1/2,1/2) with ∫x^jv=0 for j=0..29,
    Q_zeta(v)>369/10000 ||v||².
    All numeric comparison gates are exact integer/Fraction arithmetic.
    See dossier proof for γ<3/5, logπ<23/20 and signed budgets.
    """
    a,T,J,N=F(1,2),21,75,29
    L=gamma_rungs_multiplier_lower(T,J)
    leak=moment_fourier_leak_sharp_upper(a,T,N)
    if not L>F(131,20):
        raise ArithmeticMetaError("sharp 75-Gamma-rung bound failed")
    if not leak<F(1,500):
        raise ArithmeticMetaError("sharp Taylor moment Fourier budget failed")
    # Prove gamma<3/5 using H_32 and 3 terms of log2=2 atanh(1/3).
    H32=sum((F(1,n) for n in range(1,33)),F(0))
    log2_lower=2*(F(1,3)+F(1,81)+F(1,1215))
    if not H32-5*log2_lower < F(3,5):
        raise ArithmeticMetaError("Euler gamma rational majorant failed")
    # Exponential lower sum establishes log(pi)<23/20 because π<22/7.
    exp_23_20_lower=sum((F(23,20)**k/factorial(k) for k in range(6)),F(0))
    if not exp_23_20_lower > F(22,7):
        raise ArithmeticMetaError("log pi rational upper bound failed")
    # C_G < (3/5 + 11/7 + 3*(25/36) + 23/20) < 109/20.
    contact_upper=F(3,5)+F(11,7)+F(25,12)+F(23,20)
    if not contact_upper < F(109,20):
        raise ArithmeticMetaError("Gamma contact budget failed")
    budget=F(13,2)  # +2w2<1 and negative pole 2(sinh(1/2)-1/2)<1/20.
    margin=F(131,20)*F(499,500)-budget
    if margin!=F(369,10000) or margin<=0:
        raise ArithmeticMetaError("moment-29 Weil margin failed")
    return {"radius":"1/2", "gamma_frequency":T, "gamma_rungs":J,
            "vanishing_moment_orders":"0..29", "number_of_moment_constraints":30,
            "gamma_rational_lower":"131/20", "leak_upper":"1/500",
            "Gamma_contact_upper":"109/20", "complete_signed_budget":"13/2",
            "certified_all_test_margin":"369/10000",
            "classical_Weil_identification_imported": True,
            "source_realized_prime_powers":[2], "RH_proved":False,
            "unrestricted_first_window_sign_proved":False}
