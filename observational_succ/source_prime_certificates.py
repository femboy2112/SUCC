"""Exact rational enclosures for causal finite prime/FUCC contributions.

For true zeta, Suzuki's prime-side wavefront is

 Psi_prime(t) = -sum_(n<=exp(|t|))
       [Lambda(n)/sqrt(n)] (|t|-log(n)).

For a normalized causal arithmetic source a, with formal Dirichlet
convolution logarithm b=log_*a, the source diagnostic is

 Psi_prime_a(t) = -sum_(n>=2)
       [b(n) log(n)/sqrt(n)] (|t|-log(n))_+ .

All logarithms and square roots are bounded using RATIONAL ARITHMETIC:
  log(x)=2sum_j y^(2j+1)/(2j+1), y=(x-1)/(x+1);
  positive tail <=2*y^(2m+1)/[(2m+1)(1-y^2)];
  reduce x=n/2^floor(log2(n)) so 0<=y<=1/3;
  sqrt(n) bounds from exact integer isqrt(n*10^(2P)).
No zero ordinates, mpmath, unverified numerical intervals,
or analytic continuation enter the CERTIFICATE.

This certifies only the PRIME side. Suzuki requires the FULL
Gamma+poles minus primes kernel; a rigorous archimedean interval oracle
and the source-to-Weil identity/sign are still missing.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

from .gamma_interferometer import GammaInterferometer
from .observer_reflection import RationalInterval, ReflectionBoundaryError


class SourceCertificateError(ValueError):
    pass


def _q(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise SourceCertificateError("All certified source inputs must be exact rationals")


def _positive_integer(n):
    if type(n) is not int or not 1 <= n <= 10000:
        raise SourceCertificateError("Exact logarithm integer input must be 1..10000")


def _terms(m):
    if type(m) is not int or not 2 <= m <= 200:
        raise SourceCertificateError("Log-tail terms must be an integer in 2..200")


def rational_log_ratio(num,den,*,terms=24):
    """Rigorous enclosure of log(num/den) for 1<=num/den<=2.

    The positive Taylor remainder is bounded by the geometric sum.
    Endpoint x=1 has EXACT log zero.
    """
    _terms(terms)
    if (type(num) is not int or type(den) is not int or den<=0
            or not den <= num <= 2*den):
        raise SourceCertificateError("Require integer ratio 1<=num/den<=2")
    y=Fraction(num-den,num+den)
    S=sum((Fraction(2,2*j+1)*y**(2*j+1)
           for j in range(terms)),Fraction(0))
    R=(Fraction(2,2*terms+1)*y**(2*terms+1)/
       (1-y*y))
    return RationalInterval(S,S+R)


def rational_log_integer(n,*,terms=24):
    """Exact rational log n enclosure using binary argument reduction."""
    _positive_integer(n)
    _terms(terms)
    if n==1:
        return RationalInterval.exact(0)
    k=n.bit_length()-1
    ln2=rational_log_ratio(2,1,terms=terms)
    mantissa=rational_log_ratio(n,1<<k,terms=terms)
    return ln2.scale(k)+mantissa


def rational_inverse_sqrt(n,*,places=20):
    """Rational bounds on 1/sqrt(n) from integer perfect-square bounds."""
    _positive_integer(n)
    if type(places) is not int or not 2<=places<=35:
        raise SourceCertificateError("Decimal places must be exact 2..35")
    scale=10**places
    lower_int=isqrt(n*scale*scale)
    lower=Fraction(lower_int,scale)
    if lower<=0:
        raise ArithmeticError("Nonpositive sqrt floor")
    if lower_int*lower_int==n*scale*scale:
        return RationalInterval.exact(1/lower)
    upper=Fraction(lower_int+1,scale)
    return RationalInterval(1/upper,1/lower)


def _ramp_from_log(t,ln):
    """Guaranteed interval for (|t|-log n)_+; no boundary branch guess."""
    x=abs(_q(t))
    return RationalInterval(max(Fraction(0),x-ln.upper),
                            max(Fraction(0),x-ln.lower))


def _ceil_fraction(q):
    return -(-q.numerator//q.denominator)


def finite_prime_horizon(times):
    """Conservative INTEGER active-event horizon from e<3."""
    ts=tuple(_q(z) for z in times)
    if not ts or len(ts)>16:
        raise SourceCertificateError("1..16 finite query times required")
    M=max([abs(t) for t in ts]+[abs(t-u) for t in ts for u in ts])
    if M>4:
        raise SourceCertificateError("Certified prime window restricted to |relative log time|<=4")
    return max(2,3**_ceil_fraction(M))


@dataclass(frozen=True)
class CertifiedPrimeSource:
    """A fully INTEGRATED Dirichlet-log prefix and pure rational bounds."""
    snapshot: GammaInterferometer
    log_terms: int = 24
    sqrt_places: int = 20

    def __post_init__(self):
        if not isinstance(self.snapshot,GammaInterferometer):
            raise SourceCertificateError("Need an actualized GammaInterferometer source snapshot")
        _terms(self.log_terms)
        if type(self.sqrt_places) is not int or not 2<=self.sqrt_places<=35:
            raise SourceCertificateError("Invalid square-root certificate accuracy")
        if not 2<=self.snapshot.horizon<=256:
            raise SourceCertificateError("Supported finite source horizon is 2..256")

    @classmethod
    def from_engine(cls,engine,horizon=None,*,log_terms=24,sqrt_places=20):
        """Bind a certified prime-only observer to a FULLY INTEGRATED journal.

        The GammaInterferometer adapter refuses pending source events
        and preserves the observed journal head; future predictions
        never become source coefficients just because their labels exist.
        """
        try:
            snap=GammaInterferometer.from_engine(engine,horizon)
        except (ValueError,TypeError) as exc:
            raise SourceCertificateError("Source not causally actualized") from exc
        return cls(snap,log_terms,sqrt_places)

    @classmethod
    def genuine(cls,horizon,*,log_terms=24,sqrt_places=20):
        if type(horizon) is not int or not 2<=horizon<=256:
            raise SourceCertificateError("Genuine source horizon must be 2..256")
        snap=GammaInterferometer.from_prefix(
            {n:1 for n in range(1,horizon+1)},horizon)
        return cls(snap,log_terms,sqrt_places)

    def _check_times(self,times):
        need=finite_prime_horizon(times)
        if need>self.snapshot.horizon:
            raise SourceCertificateError(
                f"Source prefix {self.snapshot.horizon} insufficient for proven horizon {need}")
        return need

    def prime_psi(self,t):
        """Rational interval for prime wavefront part only (NOT full Psi)."""
        self._check_times((t,))
        t=_q(t)
        value=RationalInterval.exact(0)
        for n in range(2,self.snapshot.horizon+1):
            b=self.snapshot.connected[n]
            if b==0:
                continue
            ln=rational_log_integer(n,terms=self.log_terms)
            h=_ramp_from_log(t,ln)
            if h.upper==0:
                continue
            inverse=rational_inverse_sqrt(n,places=self.sqrt_places)
            # for signed connected coefficient, interval products are
            # essential (fake sources need not be positive).
            weight=ln*inverse
            term=weight*h
            value=value+term.scale(-b)
        return value

    def prime_screw(self,t,u):
        """Rational interval enclosing ONLY the prime contribution to K."""
        self._check_times((t,u))
        t,u=_q(t),_q(u)
        return self.prime_psi(t)+self.prime_psi(u)-self.prime_psi(t-u)

    def oracle(self,t,u):
        return self.prime_screw(t,u)

    def provenance(self):
        return {
            "type":"rigorous rational finite prime/FUCC wavefront ONLY",
            "horizon":self.snapshot.horizon,
            "source_matches_zeta":self.snapshot.matches_zeta_prefix,
            "trace_head":self.snapshot.trace_head,
            "log_terms":self.log_terms,
            "sqrt_places":self.sqrt_places,
            "Gamma_pole_completion_certified":False,
            "full_Weil_positive_form_proved":False,
        }


def prime_delta_at_fake_six(*,t=Fraction(9,5),log_terms=30,
                            sqrt_places=26,horizon=20):
    """Strict interval source anomaly on the first fake-six ramp.

    A(6)=2, A(n)=1 otherwise. For log6<t<log12, no newly
    induced connected event beyond 6 contributes, so

      delta Psi_prime(t)
        = -log(6)/sqrt(6) * (t-log(6)).

    This is a theorem about the SOURCE PRIME SIDE only.
    """
    tq=_q(t)
    if type(horizon) is not int or not 12<=horizon<=81:
        raise SourceCertificateError("Need 12<=horizon<=81 for this controlled example")
    log6=rational_log_integer(6,terms=log_terms)
    log12=rational_log_integer(12,terms=log_terms)
    if tq<=log6.upper or tq>=log12.lower:
        raise SourceCertificateError(
            "Require a CERTIFIED interior rational time log6<t<log12")
    true=CertifiedPrimeSource.genuine(
        horizon,log_terms=log_terms,sqrt_places=sqrt_places)
    s={n:1 for n in range(1,horizon+1)}
    s[6]=2
    fake=CertifiedPrimeSource(
        GammaInterferometer.from_prefix(s,horizon),
        log_terms,sqrt_places)
    a=fake.prime_psi(tq)-true.prime_psi(tq)
    if not a.upper<0:
        raise ArithmeticError("Correct fake-six prime-source anomaly not certified negative")
    return a
