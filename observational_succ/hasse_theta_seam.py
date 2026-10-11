"""Finite SUCC differences vs theta/Gamma completion: a source-sensitive seam.

Two CLASSICAL continuation routes from integer data:
  (1) Euler transform of the alternating Dirichlet series (Hasse/Sondow).
      At s=-m, finitely many exact differences reproduce zeta(-m).
  (2) Poisson/theta heat kernel, a globally entire, reflection-symmetric
      representation of completed xi.

The two paths agree for the TRUE zeta source. Their agreement is NOT a
Weil-positive theorem and is not automatic for an arbitrary arithmetic
source. A single counterfeit coefficient at 6 exposes the gap.

The Hasse series with 1/(n+1) is source FRAGILE: inserting a single
impulse does not generally preserve convergence. Never advertise a
generic finite-mutant Hasse transform as analytic continuation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping


class SeamError(ValueError):
    """Finite window, source, analytic chart or causal contract violated."""


def _index(n, *, minimum=0, maximum=256, name="index"):
    if type(n) is not int or not minimum <= n <= maximum:
        raise SeamError(f"{name} must be an exact integer in {minimum}..{maximum}")
    return n


def _rational(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise SeamError("Only exact rational/integer source coefficients permitted")


def _mp():
    try:
        import mpmath
    except ImportError as exc:
        raise SeamError("mpmath is required for non-rational analytic readouts") from exc
    return mpmath


def _mprat(mp, q):
    f=Fraction(q)
    return mp.mpf(f.numerator)/f.denominator


@dataclass(frozen=True)
class SUCCDifferenceSource:
    """Only integrated, complete coefficients a(1)..a(horizon) are read.

    No future-tail model is inferred from finite agreement with zeta.
    Negative-integer finite-difference values of a MUTANT are diagnostics,
    not the analytic continuation of an arbitrary Dirichlet series.
    """
    horizon: int
    coefficients: tuple[Fraction, ...]
    trace_head: str | None = None

    @classmethod
    def from_prefix(cls, source: Mapping[int,object], horizon: int, *, trace_head=None):
        _index(horizon, minimum=2, name="actualized coefficient horizon")
        if not isinstance(source, Mapping):
            raise SeamError("Source must be a mapping of integrated events")
        values=[Fraction(0)]
        for k in range(1,horizon+1):
            if k not in source:
                raise SeamError(f"Event {k} has not been integrated")
            values.append(_rational(source[k]))
        if values[1]!=1:
            raise SeamError("Normalized Dirichlet source requires a(1)=1")
        return cls(horizon,tuple(values),trace_head)

    @classmethod
    def zeta(cls,horizon):
        return cls.from_prefix({n:1 for n in range(1,horizon+1)},horizon)

    @classmethod
    def from_engine(cls,engine,horizon=None):
        from .gamma_interferometer import GammaInterferometer,InterferometerError
        try:
            snap=GammaInterferometer.from_engine(engine,horizon)
        except (InterferometerError,ValueError) as exc:
            raise SeamError("Source must be fully integrated, never predicted") from exc
        return cls(snap.horizon,snap.coefficients,snap.trace_head)

    @property
    def genuine_zeta_prefix(self):
        return all(c==1 for c in self.coefficients[1:])

    def _difference_row_exact(self,power,terms):
        """Full signed forward-difference row at nonnegative integer power."""
        _index(power,maximum=100,name="polynomial degree")
        _index(terms,maximum=self.horizon-1,name="last SUCC difference index")
        return [self.coefficients[k]*k**power for k in range(1,terms+2)]

    def _successive_differences(self,row):
        """Uses sign convention Δ_- f(k)=f(k)-f(k+1)."""
        while row:
            yield row[0]
            row=[row[j]-row[j+1] for j in range(len(row)-1)]

    def euler_eta_negative(self,m,*,terms=None):
        """Finite Euler transform, evaluated EXACTLY at s=-m.

        E_N(-m)=Σ_(n=0)^N 2^(-n-1) (Δ_-^n [a(k)k^m])|_(k=1).
        With genuine zeta and N>=m this equals eta(-m) EXACTLY.
        For fake source it is a finite diagnostic, NOT necessarily
        the infinite Euler-transformed continuation at finite N.
        """
        _index(m,maximum=64,name="negative integer order")
        if terms is None:
            terms=min(m,self.horizon-1)
        _index(terms,maximum=self.horizon-1,name="Euler window")
        row=self._difference_row_exact(m,terms)
        return sum((Fraction(q,2**(n+1))
                    for n,q in enumerate(self._successive_differences(row))),
                   Fraction())

    def hasse_pole_negative(self,m,*,terms=None):
        """Second, local-prime-2-free Hasse construction, exactly rational.

        H_N(-m) = 1/(-m-1) Σ_(n<=N)
                     (Δ_-^n [a(k)k^(m+1)])_1/(n+1).
        For genuine zeta and N>=m+1, this equals zeta(-m).
        A finite source impulse can make H_N diverge as N increases.
        """
        _index(m,maximum=64,name="negative integer order")
        if terms is None:
            terms=min(m+1,self.horizon-1)
        _index(terms,maximum=self.horizon-1,name="Hasse window")
        row=self._difference_row_exact(m+1,terms)
        return sum((Fraction(q,n+1)
                    for n,q in enumerate(self._successive_differences(row))),
                   Fraction()) /(-m-1)

    def zeta_negative_certified(self,m):
        """Classical Hasse theorem + EXACT terminating finite SUCC differences.

        Requires complete *true zeta prefix* through max(m+1,m+2) and
        equality of two independent rational formulas. The labels
        'certified' here refer to exact algebra conditional on Hasse's
        already-established analytic identity, not a newly proved theorem.
        """
        _index(m,maximum=64,name="negative integer order")
        if not self.genuine_zeta_prefix:
            raise SeamError("Exact zeta continuation requires the real zeta source")
        if self.horizon < m+2:
            raise SeamError("Need all coefficients through m+2 for Hasse")
        eta=self.euler_eta_negative(m,terms=m)
        z_from_eta=eta/Fraction(1-2**(1+m))
        z_hasse=self.hasse_pole_negative(m,terms=m+1)
        if z_from_eta!=z_hasse:
            raise ArithmeticError("Independent finite SUCC continuation formulas differ")
        return {
            "m":m,
            "eta":eta,
            "zeta":z_from_eta,
            "hasse":z_hasse,
            "euler_nonzero_differences_at_most":m+1,
            "hasse_nonzero_differences_at_most":m+2,
            "source_zeta_verified_through":self.horizon,
            "status":"exact terminating rational values via classical Hasse identities",
        }

    def negative_difference_rows(self,m,*,terms=None):
        """Provenance: retain every SUCC-difference contribution unquotiented."""
        _index(m,maximum=64,name="negative integer order")
        if terms is None:
            terms=min(self.horizon-1,m+6)
        _index(terms,maximum=self.horizon-1,name="SUCC window")
        left=list(self._successive_differences(self._difference_row_exact(m,terms)))
        right=list(self._successive_differences(self._difference_row_exact(m+1,terms)))
        return {
            "eta":tuple(Fraction(q,2**(j+1)) for j,q in enumerate(left)),
            "hasse_numerator":tuple(Fraction(q,j+1) for j,q in enumerate(right)),
            "source_genuine_prefix":self.genuine_zeta_prefix,
        }

    def parity_source_defects(self, *, primitive_only=False):
        """Exact local-prime-2 source seam d(m)=a(2m)-a(2)a(m).

        On coprime (odd) m this is multiplicativity at the new prime
        2; for ALL m it asserts stronger complete multiplicativity
        along the 2-ray, which general Hecke L-functions may not obey.
        """
        defect={}
        for m in range(1,self.horizon//2+1):
            if primitive_only and m%2==0:
                continue
            d=self.coefficients[2*m]-self.coefficients[2]*self.coefficients[m]
            if d:
                defect[m]=d
        return defect

    def source_prefix_compatible(self,longer):
        if not isinstance(longer,SUCCDifferenceSource) or longer.horizon<self.horizon:
            raise SeamError("Comparison requires a later complete source")
        if self.coefficients!=longer.coefficients[:self.horizon+1]:
            raise SeamError("Earlier source coefficients have been revised")
        return True

    def eta_euler_analytic(self,s,*,terms=72,dps=90):
        """Euler-accelerated eta for arbitrary complex s; numeric readout.

        This transform of the altered finite data does NOT generally
        yield (1-2^(1-s))*the altered Dirichlet series. The parity
        compatibility law must separately be checked. No formal
        truncation-error certificate is inferred from mpmath digits.
        """
        _index(terms,maximum=self.horizon-1,name="analytic Euler window")
        mp=_mp()
        with mp.workdps(dps):
            s=mp.mpc(s)
            row=[_mprat(mp,self.coefficients[k])*mp.power(k,-s)
                 for k in range(1,terms+2)]
            total=mp.mpc(0)
            for n in range(terms+1):
                total+=row[0]/mp.power(2,n+1)
                row=[row[j]-row[j+1] for j in range(len(row)-1)]
            return +total

    def zeta_from_eta_analytic(self,s,*,terms=72,dps=90):
        if not self.genuine_zeta_prefix:
            raise SeamError("No zeta claim from mutated Euler-transformed source")
        mp=_mp()
        with mp.workdps(dps):
            s=mp.mpc(s)
            denom=1-mp.power(2,1-s)
            if abs(denom)<mp.mpf("1e-12"):
                raise SeamError("2-Euler normalization is zero/ill-conditioned; use Hasse pole chart")
            eta=self.eta_euler_analytic(s,terms=terms,dps=dps)
            return +(eta/denom)




def eta_prime_trivial(m, *, terms=120, dps=100):
    """Eta derivative from NEVER-TERMINATING finite SUCC windows at s=-2m.

    For the GENUINE zeta source,
    eta(s)=(1-2^(1-s))*zeta(s).
    At s=-2m, eta(-2m)=zeta(-2m)=0, but
    eta'(-2m) = (1-2^(1+2m))*zeta'(-2m) != 0.
    The differentiated Euler-transform terms are
      -2^(-n-1) Δ_-^n[k^(2m) log(k)]|_(k=1).
    These do NOT terminate at n=2m, unlike the value terms.
    This is a high-precision numerical finite prefix; no rigorous
    derivative remainder bound is claimed by the caller.
    """
    _index(m,minimum=1,maximum=8,name="trivial-zero index")
    _index(terms,minimum=2*m+3,maximum=256,name="derivative SUCC horizon")
    mp=_mp()
    with mp.workdps(dps):
        row=[-mp.power(k,2*m)*mp.log(k) for k in range(1,terms+2)]
        result=mp.mpf(0)
        for n in range(terms+1):
            result+=row[0]/mp.power(2,n+1)
            row=[row[k]-row[k+1] for k in range(len(row)-1)]
        return +result


def gamma_pole_prime_bridge(m, *, terms=120, dps=100):
    """Two independent analytic readouts of the cancelled Gamma-zeta jet.

    Source side: differentiated Euler/eta finite differences at -2m.
    Euler-safe reflection side:
      ζ'(-2m)=(-1)^m (2m)! ζ(2m+1)/(2(2π)^(2m)).
    This is CLASSICAL and not a proof of RH; -2m is a known trivial
    zero index, NOT a fitted nontrivial zero or spectral input.
    """
    _index(m,minimum=1,maximum=8,name="trivial-zero index")
    mp=_mp()
    with mp.workdps(dps):
        eta_prime=eta_prime_trivial(m,terms=terms,dps=dps)
        zprime=eta_prime/(1-2**(1+2*m))
        euler_safe=((-1)**m*mp.factorial(2*m)/
                    (2*mp.power(2*mp.pi,2*m))*mp.zeta(2*m+1))
        completed_pole=2*((-1)**m)/mp.factorial(m)*zprime
        return {
            "eta_derivative":+eta_prime,
            "zeta_derivative_from_finite_differences":+zprime,
            "zeta_derivative_from_safe_euler":+euler_safe,
            "derivative_discrepancy":+abs(zprime-euler_safe),
            "gamma_pole_times_zero_finite_value":+completed_pole,
            "derivative_SUCC_terms":terms+1,
            "status":"numerical calibration of classical Gamma-pole/trivial-zero identity",
            "nontrivial_zeros_used":False,
        }




def eta_jet_trivial(m,order,*,terms=120,dps=110):
    """High-precision SUCC-difference jets at the known trivial point -2m.

    eta^(r)(-2m)=Σ_(n>=0)2^(-n-1)
      Δ_-^n [ (-log k)^r*k^(2m) ]_(k=1).
    Order 0 terminates. Orders 1 and 2 do NOT terminate. The finite
    n cutoff is a numerical approximation; these figures are NOT
    certified interval bounds.
    """
    _index(m,minimum=1,maximum=8,name="Gamma-trivial index")
    _index(order,minimum=1,maximum=2,name="spectral derivative order")
    _index(terms,minimum=2*m+3,maximum=256,name="SUCC jet horizon")
    mp=_mp()
    with mp.workdps(dps):
        row=[mp.power(k,2*m)*mp.power(-mp.log(k),order)
             for k in range(1,terms+2)]
        total=mp.mpf(0)
        for n in range(terms+1):
            total+=row[0]/mp.power(2,n+1)
            row=[row[k]-row[k+1] for k in range(len(row)-1)]
        return +total


def gamma_subtracted_prime_current(m,*,terms=120,dps=110):
    """Gamma-corrected NEGATIVE-half-plane jets equal POSITIVE Euler current.

    For s0=-2m, with C(s)=1-2^(1-s) and eta=C*zeta,
       ζ''(s0)/(2ζ'(s0))
         = eta''(s0)/(2 eta'(s0)) - C'(s0)/C(s0).
    By the functional equation,
       ζ''(-2m)/(2ζ'(-2m)) + ψ(2m+1) - log(2π)
         = -ζ'(2m+1)/ζ(2m+1)
         = sum_(p,k) (log p)/p^(k(2m+1)) > 0.

    Uses only the canonical trivial-zero INDICES, not any nontrivial
    zeros, nor the Weil sign. Both eta jets have INFINITE finite-difference
    expansions (the scalar eta(-2m)=0 terminates).
    """
    _index(m,minimum=1,maximum=8,name="Gamma-trivial index")
    mp=_mp()
    with mp.workdps(dps):
        first=eta_jet_trivial(m,1,terms=terms,dps=dps)
        second=eta_jet_trivial(m,2,terms=terms,dps=dps)
        c0=1-mp.power(2,1+2*m)
        dc=mp.power(2,1+2*m)*mp.log(2)
        current=(second/(2*first)-dc/c0
                 +mp.digamma(2*m+1)-mp.log(2*mp.pi))
        right=-mp.diff(mp.zeta,2*m+1)/mp.zeta(2*m+1)
        return {
            "source_eta_first_jet":+first,
            "source_eta_second_jet":+second,
            "gamma_corrected_negative_side":+current,
            "positive_safe_prime_current":+right,
            "error":+abs(current-right),
            "source_SUCC_order":terms+1,
            "nontrivial_zero_input":False,
            "status":"classical reflection/Dirichlet-Euler identity with finite-SUCC numerical jets",
        }


def prime_current_tail_enclosure(m,prime_cutoff,*,dps=90):
    """Analytic finite-prime lower bound plus tail upper envelope.

    Let σ=2m+1 >=3. Then
      J=sum_p log(p)/(p^σ-1).
    Bound the omitted PRIME sum by all integers n>P, using
      1/(n^σ-1) <= n^-σ/(1-2^-σ),
      sum_(n>P) log(n)n^-σ <= integral_P^∞ log(x)x^-σ dx.
    Thus J_P <= J <= J_P + P^(1-σ)
      [log(P)/(σ-1)+1/(σ-1)^2]/(1-2^-σ).
    Unlike a bare numerical observation, the bound is analytically
    justified; its printed mp evaluation is not directed-rounding.
    """
    _index(m,minimum=1,maximum=8,name="Euler prime current order")
    _index(prime_cutoff,minimum=2,maximum=1024,name="finite prime cutoff")
    from .gamma_succ_path import primes_upto
    mp=_mp()
    with mp.workdps(dps):
        sigma=2*m+1
        partial=mp.fsum(mp.log(p)/(mp.power(p,sigma)-1)
                        for p in primes_upto(prime_cutoff))
        p=mp.mpf(prime_cutoff)
        missing=(mp.power(p,1-sigma)
                 *(mp.log(p)/(sigma-1)+mp.mpf(1)/(sigma-1)**2)
                 /(1-mp.power(2,-sigma)))
        return {
            "prime_cutoff":prime_cutoff,
            "sigma":sigma,
            "lower":+partial,
            "tail_upper_bound":+missing,
            "upper":+(partial+missing),
            "positive":bool(partial>0),
            "scope":"analytically bounded omitted prime channels in Euler-safe region",
        }

def prime_two_parity_error_from_exact_finite_model(s, *,
                                                  n=6,delta=1,dps=75):
    """Alias for finite_mutation_parity_error, requiring explicit countermodel.

    There is NO analytic source-identity claim for an arbitrary finite
    observer's UNDECLARED infinite future.
    """
    return finite_mutation_parity_error(s,n=n,delta=delta,dps=dps)

def theta_xi_partial(s,*,max_integer=4,dps=75,mutations: Mapping[int,object] | None=None):
    """Poisson/self-dual completed-xi HEAT representation, finite integer terms.

    xi_M(s)=1/2 + s(s-1)/2 Σ_(n<=M) [ (πn²)^(-s/2)Γ(s/2,πn²)
                                    +(πn²)^(-(1-s)/2)Γ((1-s)/2,πn²) ].
    A mutation to the Gaussian weights leaves the reflection symmetry
    MANIFEST by construction; it need not represent the completion of
    the mutated arithmetic Dirichlet series!
    """
    _index(max_integer,minimum=1,maximum=40,name="heat integer cutoff")
    if mutations is None:
        mutations={}
    if not isinstance(mutations,Mapping):
        raise SeamError("Heat weights need an explicit sparse mutation map")
    checked={}
    for n,v in mutations.items():
        _index(n,minimum=1,maximum=max_integer,name="mutated heat integer")
        checked[n]=_rational(v)
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        total=mp.mpc(0)
        for n in range(1,max_integer+1):
            alpha=mp.pi*n*n
            a=_mprat(mp,checked.get(n,Fraction(1)))
            total+=a*(mp.power(alpha,-s/2)*mp.gammainc(s/2,alpha,mp.inf)
                      +mp.power(alpha,-(1-s)/2)
                         *mp.gammainc((1-s)/2,alpha,mp.inf))
        return +(mp.mpf("0.5")+s*(s-1)*total/2)


def theta_xi_tail_bound(s,*,max_integer=4,dps=75):
    """THEORETICAL absolute truncation bound in 0<=Re(s)<=1.

    Bound = |s(s-1)|/π * exp[-π(M+1)^2] /
       [(M+1)^2 (1-exp[-π(2M+3)])].
    Because x^(Re(s)/2-1), x^((1-Re(s))/2-1) <=1 for x>=1.
    Derived from the theta/Poisson exact formula, not numerically fitted.
    Floating mpmath evaluation is not a directed-rounding proof.
    """
    _index(max_integer,minimum=1,maximum=40,name="heat cutoff")
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        if not 0<=mp.re(s)<=1:
            raise SeamError("Tail envelope presently proved only in closed critical strip")
        m=max_integer
        return +(abs(s*(s-1))/mp.pi
                  *mp.exp(-mp.pi*(m+1)**2)
                  /((m+1)**2*(1-mp.exp(-mp.pi*(2*m+3)))))


def raw_completed_finite_mutation(s, *, n=6, delta=1, dps=75):
    """EXPLICIT COUNTERMODEL ζ(s)+delta*n^-s, not a discovered future event.

    The source is defined FOR ALL n in this adversarial thought-experiment:
    a(m)=1+delta if m=n and a(m)=1 otherwise.
    Gamma-complete this actual meromorphic Dirichlet series, not a
    forced reflection-symmetric fictitious theta construction.
    """
    _index(n,minimum=2,maximum=256,name="mutated source index")
    d=_rational(delta)
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        if s in (0,1,-2,-4,-6,-8):
            raise SeamError("Use a regular chart for this raw gamma/pole product")
        zeta_part=mp.zeta(s)+_mprat(mp,d)*mp.power(n,-s)
        return +(s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*zeta_part/2)


def finite_mutation_parity_error(s,*,n=6,delta=1,dps=75):
    """Exact 2-Euler transport defect for a single declared source mutation.

    a(m)=1+delta*[m=n] globally, with n even and n>=6.
    E_a-(1-2^(1-s)) D_a = -(2-2^(1-s))*delta*n^-s
    since n is even, and the alternating sign at n is minus.
    This is algebra on absolutely convergent Dirichlet series, then
    meromorphically continued as a finite elementary correction.
    """
    _index(n,minimum=6,maximum=256,name="even mutation")
    if n%2:
        raise SeamError("This parity formula was derived for even event n")
    d=_rational(delta)
    mp=_mp()
    with mp.workdps(dps):
        s=mp.mpc(s)
        return +((_mprat(mp,d)*mp.power(n,-s))
                  *(-2+mp.power(2,1-s)))



def symmetric_offline_quartet_counterexample():
    """Exact real-even polynomial positive on critical line yet with off-line zeros.

    With x=s-1/2, choose off-line quartet x=±(1/4±i/2), so
      P(x)=x^4+(3/8)x^2+25/256.
    On critical line x=it:
      P(it)=(t^2-3/16)^2+1/16 >=1/16>0.
    Real symmetry, s->1-s, outer zero-freeness and positivity ON line
    are ALL insufficient to force every zero onto that line.
    This deliberately synthetic polynomial is NOT zeta.
    """
    Q=Fraction
    return {
        "coefficients_even_quartic": (Q(1),Q(3,8),Q(25,256)),
        "line_square_center":Q(3,16),
        "critical_line_positive_lower_bound":Q(1,16),
        "constructed_offline_zero_real_parts":(Q(1,4),Q(3,4)),
        "constructed_offline_zero_imag_magnitude":Q(1,2),
        "actual_zeta_zeros_used":False,
        "scope":"exact symmetry and on-line positivity countermodel; not an L-function",
    }


def riemann_siegel_leading(t,*,source: SUCCDifferenceSource | None=None,
                          dps=75):
    """Asymptotic Hardy Z main sum, directly reading integer SUCC BULK.

    DLMF 25.10.3:
      Z(t)=2Σ_(n<=floor(sqrt(t/(2π))))
              cos(theta(t)-t*log n)/sqrt(n) + R(t).
    theta(t)=Im logGamma(1/4+it/2)-t/2 log(pi).
    NO remainder is bounded here; do not certify zeros or RH with
    the leading main sum. If source!=None, the changed coefficients
    are a controlled PROBE ONLY, not an approximate functional equation
    for the arbitrary mutant source.

    The load-bearing cutoff is the factor-square horizon
      n<=sqrt(t/(2π)); a source mutation at n=6 is invisible below
      t<2π*36 and becomes visible after crossing that threshold.
    """
    mp=_mp()
    with mp.workdps(dps):
        t=mp.mpf(t)
        if not mp.isfinite(t) or t<10:
            raise SeamError("Riemann-Siegel asymptotic probe requires finite t>=10")
        m=int(mp.floor(mp.sqrt(t/(2*mp.pi))))
        if m<1 or m>256:
            raise SeamError("Riemann-Siegel source window exceeds 256 stage budget")
        if source is not None:
            if not isinstance(source,SUCCDifferenceSource) or source.horizon<m:
                raise SeamError(f"Need integrated source coefficients through window {m}")
        theta=(mp.im(mp.loggamma(mp.mpf(1)/4+mp.j*t/2))
               -t*mp.log(mp.pi)/2)
        total=mp.fsum(
            (_mprat(mp,source.coefficients[n]) if source is not None
             else mp.mpf(1))
            *mp.cos(theta-t*mp.log(n))/mp.sqrt(n)
            for n in range(1,m+1)
        )
        return {
            "window":m,
            "phase":+theta,
            "main_sum":+(2*total),
            "source_faithful_zeta_prefix":(
                source is None or source.genuine_zeta_prefix),
            "scope":"Riemann-Siegel main sum only; its nonzero remainder is not bounded",
            "nontrivial_zero_input":False,
        }


def hardy_z_calibration(t,*,dps=75):
    """Independent analytic HOLDOUT for main sum; does not read zero lists."""
    mp=_mp()
    with mp.workdps(dps):
        t=mp.mpf(t)
        if t<10:
            raise SeamError("Riemann-Siegel calibration requires t>=10")
        theta=(mp.im(mp.loggamma(mp.mpf(1)/4+mp.j*t/2))
               -t*mp.log(mp.pi)/2)
        return +mp.re(mp.exp(mp.j*theta)*mp.zeta(mp.mpf(1)/2+mp.j*t))



def _source_prime_power(n):
    """Return p for n=p^k (k>=1), else None. No zero inputs."""
    _index(n,minimum=2,maximum=2048,name="moment source event")
    from .arithmetic import factorization
    decomposition=factorization(n)
    return decomposition[0][0] if len(decomposition)==1 else None


def prime_source_moment_energy(vector,*,source_horizon=128,
                               fake_composite_six=Fraction(0),dps=80):
    """Positive finite Hankel/Householder moment Gram from positive prime jets.

    For true Λ(n), define µ=Σ_(n>=2)Λ(n)/n³ δ_(1/n²).
    The gamma-subtracted trivial-zero currents satisfy
      J_m=Σ_(n>=2) Λ(n)/n^(2m+1)
         =∫ x^(m-1) dµ(x), m>=1.
    For rational polynomial P(x)=Σ_i c_i x^i,
      ∫ P(x)^2 dµ(x) >=0.
    We evaluate a finite cutoff plus an *artificial* composite n=6
    weight c*log6. This fake also retains positivity! Therefore
    the moment PSD is not an Euler authenticity/Weil criterion.

    The FULL moment sequence is uniquely determining for finite positive
    measures on [0,1/4] (Hausdorff moment problem), but *PSD alone*
    selects many other measures. Code only evaluates finite partials;
    it does not infer a full measure from samples.
    """
    _index(source_horizon,minimum=6,maximum=1024,name="prime moment source horizon")
    if not isinstance(vector,(tuple,list)) or not 1<=len(vector)<=32:
        raise SeamError("Nonempty polynomial vector of length <=32 required")
    coeff=tuple(_rational(x) for x in vector)
    extra=_rational(fake_composite_six)
    if extra<0:
        raise SeamError("Only nonnegative composite injection in this PSD control")
    mp=_mp()
    with mp.workdps(dps):
        energy=mp.mpf(0)
        fake_piece=mp.mpf(0)
        for n in range(2,source_horizon+1):
            p=_source_prime_power(n)
            weight=mp.log(p) if p is not None else mp.mpf(0)
            if n==6 and extra:
                fake_piece+=_mprat(mp,extra)*mp.log(6)
                weight+=_mprat(mp,extra)*mp.log(6)
            if weight==0:
                continue
            poly=mp.fsum(_mprat(mp,c)*mp.power(n,-2*j)
                         for j,c in enumerate(coeff))
            energy+=weight*poly*poly/mp.power(n,3)
        return {
            "energy":+energy,
            "nonnegative":bool(energy>=0),
            "fake_composite_six_weight":+fake_piece,
            "genuine_source":bool(extra==0),
            "limitation":"generic positive fake channels pass; not Weil sign",
        }


def prime_current_finite_differences(m,order,*,source_horizon=128,dps=85):
    """Classical complete monotonicity of the SPECIAL prime-current moments.

    J_m=Σ Λ(n)/n^(2m+1). Then for ΔJ_m=J_(m+1)-J_m,
      (-1)^r Δ^r J_m
       =Σ Λ(n)/n^(2m+1) (1-n^-2)^r >=0.

    This is exact algebra and a positive-measure moment representation,
    not RH/Weil positivity. Numeric approximation is finite-source only.
    """
    _index(m,minimum=1,maximum=32,name="moment index")
    _index(order,minimum=0,maximum=20,name="finite difference order")
    _index(source_horizon,minimum=6,maximum=1024,name="arithmetic source horizon")
    mp=_mp()
    with mp.workdps(dps):
        moments=[]
        for j in range(order+1):
            moments.append(mp.fsum(
                mp.log(p)*mp.power(n,-(2*(m+j)+1))
                for n in range(2,source_horizon+1)
                for p in [_source_prime_power(n)] if p is not None
            ))
        difference=mp.fsum(
            ((-1)**j)*__import__("math").comb(order,j)*moments[j]
            for j in range(order+1)
        )
        positive_integral=mp.fsum(
            mp.log(p)*mp.power(n,-(2*m+1))
            *mp.power(1-mp.power(n,-2),order)
            for n in range(2,source_horizon+1)
            for p in [_source_prime_power(n)] if p is not None
        )
        return {
            "alternating_SUCC_difference":+difference,
            "positive_moment_formula":+positive_integral,
            "agreement_error":+abs(difference-positive_integral),
            "source_horizon":source_horizon,
            "status":"positive finite-moment hierarchy, RH-inert",
        }
