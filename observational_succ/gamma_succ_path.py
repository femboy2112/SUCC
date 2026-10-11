"""Provenance-retaining SUCC/Gamma and finite-prime reflection transports.

A scalar evaluation at u=1 forgets that the two Euler paths being
quotiented have different analytic dependence on u.  The first/second
jets are computed BEFORE endpoint evaluation.  All finite constructions
come from integer successor paths and finite Euler moments; the limiting
analytic identity is classical, not a proof of RH.

No zeta zeros, prebuilt positive Weil form, or regularized divergent sums.
Standard library core; mpmath is loaded only for analytic evaluations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt, prod


class PathDomainError(ValueError):
    """An event, cutoff, synthetic source, or analytic chart is invalid."""


def _integer(n, *, lower=1, upper=1024, name="integer"):
    if type(n) is not int or not lower <= n <= upper:
        raise PathDomainError(f"{name} must be an integer in {lower}..{upper}")
    return n


def _rational(q):
    if type(q) is int or isinstance(q, Fraction):
        return Fraction(q)
    raise PathDomainError("Moments must be exact rational numbers, not floats")


def primes_upto(n):
    _integer(n, lower=2, upper=1024, name="prime bound")
    sieve = bytearray(b"\x01") * (n+1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n-p*p)//p)+1)
    return tuple(p for p in range(2,n+1) if sieve[p])


def prime_valuation(n):
    _integer(n, upper=1024, name="integer event")
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:
                k+=1
                n//=p
            out.append((p,k))
        p+=1
    if n>1:
        out.append((n,1))
    return tuple(out)


@dataclass(frozen=True)
class FactorialSuccPath:
    """Record *all* finite successor multiplier events, not just n!."""

    cutoff: int

    def __post_init__(self):
        _integer(self.cutoff, lower=2, upper=256, name="successor cutoff")

    def multipliers(self):
        return tuple(range(1,self.cutoff+1))

    def event_trace(self):
        total=1
        rows=[]
        for k in self.multipliers():
            total*=k
            rows.append({"succ_event":k,"factor":k,"prime_valuation":prime_valuation(k),
                         "factorial_prefix":total})
        return tuple(rows)

    def prime_tower_exponents(self):
        ans=[]
        for p in primes_upto(self.cutoff):
            m=p
            exponent=0
            while m<=self.cutoff:
                exponent+=self.cutoff//m
                m*=p
            ans.append((p,exponent))
        return tuple(ans)

    def prime_product(self):
        return prod(p**k for p,k in self.prime_tower_exponents())

    def endpoint(self):
        return factorial(self.cutoff)

    def verify_bridge(self):
        if self.prime_product()!=self.endpoint():
            raise ArithmeticError("SUCC factorial and prime valuations disagree")
        return True

    def gamma_cutoff_integer(self,z):
        """Euler's finite gamma approximation G_N(z), exact for integer z>0."""
        _integer(z,upper=256,name="gamma integer argument")
        n=self.cutoff
        return Fraction(self.endpoint()*n**z,prod(z+k for k in range(n+1)))

    def gamma_succ_ratio(self,z):
        """G_N(z+1)/G_N(z) = z*N/(N+z+1), not z at finite N."""
        _integer(z,upper=256,name="gamma integer argument")
        n=self.cutoff
        return Fraction(n*z,n+z+1)

    def gamma_boundary_defect(self,z):
        _integer(z,upper=256,name="gamma integer argument")
        return Fraction(z*(z+1),self.cutoff+z+1)

    def gamma_euler(self,z,*,dps=60):
        mp=_mp()
        with mp.workdps(dps):
            z=mp.mpc(z)
            if mp.re(z)<=0:
                raise PathDomainError("Euler gamma limit only used in Re(z)>0")
            n=self.cutoff
            return mp.mpf(self.endpoint())*mp.power(n,z)/mp.rf(z,n+1)


def _mp():
    try:
        import mpmath as mp
    except ImportError as exc:
        raise PathDomainError("mpmath is needed for analytic readout") from exc
    return mp


@dataclass(frozen=True)
class MomentChannel:
    """Formal Euler slot (base, alpha); genuine zeta needs prime base, alpha=1."""
    base: int
    alpha: Fraction = Fraction(1)

    def __post_init__(self):
        _integer(self.base,lower=2,upper=1024,name="Euler base")
        a=_rational(self.alpha)
        if not 0<=a<self.base:
            raise PathDomainError("Re(u)>1/2 analytic chart requires 0<=alpha<base")
        object.__setattr__(self,"alpha",a)


@dataclass(frozen=True)
class PrimeMomentPath:
    """Finite, ordered numerator and denominator Euler routes.

    For given finite factors Z_B(s)=prod_b (1-alpha_b b^-s)^-1:
      numerator(u) = Z_B(2u)
      denominator(u) = Z_B(2)^u
    Their scalar ratio at u=1 is 1, but the *germ* need not be constant.

    Artificial base/alpha controls have the same scalar cancellation but are
    NOT genuine zeta Euler prefixes and their reflected readouts are NOT
    zeta functional equations.
    """
    horizon: int
    channels: tuple[MomentChannel,...]
    source_head: str | None = None

    def __post_init__(self):
        _integer(self.horizon,lower=2,upper=1024,name="prime cutoff")
        ch=tuple(self.channels)
        if not ch or len(ch)>175 or any(not isinstance(x,MomentChannel) for x in ch):
            raise PathDomainError("A nonempty finite sequence of moment channels is required")
        labels=tuple(x.base for x in ch)
        if labels!=tuple(sorted(set(labels))) or labels[-1]>self.horizon:
            raise PathDomainError("Unique sorted source slots must stay within cutoff")
        object.__setattr__(self,"channels",ch)

    @classmethod
    def genuine(cls,horizon,*,source_head=None):
        ps=primes_upto(horizon)
        return cls(horizon,tuple(MomentChannel(p) for p in ps),source_head)

    @classmethod
    def from_engine(cls,engine,horizon=None):
        """Requires COMPLETE integrated zeta coefficients through the horizon.

        The engine may contain unobserved predictions or a pending event;
        they do not enter the source prefix. Mutations are rejected rather
        than silently converted into a prime-perfect Euler product.
        """
        from .gamma_interferometer import GammaInterferometer
        try:
            observed=GammaInterferometer.from_engine(engine,horizon)
        except (ValueError,KeyError) as exc:
            raise PathDomainError("Complete integrated arithmetic source needed") from exc
        if not observed.matches_zeta_prefix:
            raise PathDomainError("Integrated source is not the actual zeta Euler prefix")
        return cls.genuine(observed.horizon,source_head=observed.trace_head)

    def is_genuine_prefix(self):
        return (tuple(x.base for x in self.channels)==primes_upto(self.horizon)
                and all(x.alpha==1 for x in self.channels))

    def paths(self):
        return {
            "numerator": [{"base":x.base,"alpha":str(x.alpha),
                           "route":"Euler Z_B(2u)","u_exponent":"2u"} for x in self.channels],
            "denominator": [{"base":x.base,"alpha":str(x.alpha),
                             "route":"pi^2=6 Z_B(2), denominator Z_B(2)^u",
                             "u_exponent":"u at fixed s=2"} for x in self.channels],
            "evaluated_ratio_at_u_1": "1",
            "scalar_evaluation_is_not_an_injective_path_map": True,
            "source_faithful_zeta_prefix":self.is_genuine_prefix(),
            "source_journal_head":self.source_head,
        }

    def zeta_two_rational(self):
        result=Fraction(1)
        for ch in self.channels:
            x=ch.alpha/Fraction(ch.base**2)
            result/=1-x
        return result

    def scalar_ratio_at_one(self):
        """Exactly 1, even for counterfeit Euler factors. Never a RH test."""
        return Fraction(1)

    def pi_squared_proxy(self):
        return 6*self.zeta_two_rational()

    def first_jet(self,*,dps=60):
        """(d/du) log[Z_B(2u)/Z_B(2)^u] at u=1."""
        mp=_mp()
        with mp.workdps(dps):
            return mp.fsum(
                mp.log(1-_mprat(mp,ch.alpha)/ch.base**2)
                - 2*mp.log(ch.base)*_mprat(mp,ch.alpha)/(ch.base**2-_mprat(mp,ch.alpha))
                for ch in self.channels
            )

    def second_jet(self,*,dps=60):
        """Second derivative of logarithm at u=1; generic, not RH-specific."""
        mp=_mp()
        with mp.workdps(dps):
            return mp.fsum(
                4*mp.log(ch.base)**2*_mprat(mp,ch.alpha)*ch.base**2
                / (ch.base**2-_mprat(mp,ch.alpha))**2
                for ch in self.channels
            )

    def ratio(self,u,*,dps=60):
        mp=_mp()
        with mp.workdps(dps):
            u=mp.mpc(u)
            if mp.re(u)<=mp.mpf("0.5"):
                raise PathDomainError("Finite transport is used on Re(u)>1/2")
            logR=mp.mpc(0)
            for ch in self.channels:
                a=_mprat(mp,ch.alpha)
                x=a/ch.base**2
                y=a*mp.power(ch.base,-2*u)
                logR+=u*mp.log(1-x)-mp.log(1-y)
            return mp.exp(logR)

    def reflected_transport(self,u,gamma_path:FactorialSuccPath,*,dps=60):
        """Finite two-path *diagnostic*, not an exact functional equation.

        T_{P,N}(u)=2^(1-2u) G_N(2u) cos(pi_P*u) /6^u
                       * [Z_P(2u)/Z_P(2)^u].
        Both prime pi_P and Gamma G_N are FINITE approximants.
        Limit for genuine primes as P,N->infinity and Re(u)>1/2 is
        zeta(1-2u), by the classical functional equation.
        """
        if not isinstance(gamma_path,FactorialSuccPath):
            raise PathDomainError("An explicit finite SUCC gamma path is required")
        mp=_mp()
        with mp.workdps(dps):
            u=mp.mpc(u)
            if mp.re(u)<=mp.mpf("0.5"):
                raise PathDomainError("Reflect only from Euler-safe Re(2u)>1")
            piP=mp.sqrt(6*_mprat(mp,self.zeta_two_rational()))
            G=gamma_path.gamma_euler(2*u,dps=dps)
            return (mp.power(2,1-2*u)*G*mp.cos(piP*u)
                    *mp.power(6,-u)*self.ratio(u,dps=dps))

    def at_u_one(self,gamma_path:FactorialSuccPath,*,dps=60):
        """At u=1, finite source ratio cancels but BOTH boundary histories persist."""
        mp=_mp()
        with mp.workdps(dps):
            piP=mp.sqrt(6*_mprat(mp,self.zeta_two_rational()))
            return mp.cos(piP)*_mprat(mp,gamma_path.gamma_cutoff_integer(2))/12

    def reflected_log_jet_one(self,gamma_path:FactorialSuccPath,*,dps=60):
        """First logarithmic jet of full finite transport at u=1.

        The Gamma finite-boundary digamma sum, finite pi_P rotation,
        and prime moments are individually retained.
        """
        mp=_mp()
        with mp.workdps(dps):
            n=gamma_path.cutoff
            piP=mp.sqrt(6*_mprat(mp,self.zeta_two_rational()))
            gamma_succ=2*(mp.log(n)-mp.fsum(1/mp.mpf(k) for k in range(2,n+3)))
            pole=-2*mp.log(2)-mp.log(6)
            sine=-piP*mp.tan(piP)
            prime=self.first_jet(dps=dps)
            return {"gamma_succ":gamma_succ,"powers":pole,"sine_rotation":sine,
                    "finite_prime_jet":prime,
                    "total":gamma_succ+pole+sine+prime,
                    "scalar_quotient_only":self.scalar_ratio_at_one(),
                    "is_genuine_source":self.is_genuine_prefix()}

    def genuine_first_jet_tail_bound(self,*,dps=60):
        """Certified O(log P/P) bound for missing PRIME jets (genuine only).

        |log(1-p^-2)| <= (4/3)p^-2, and
        2log(p)/(p^2-1) <= (8/3)log(p)/p^2.
        Sum over *integers* > P using the integral bounds yields
        |J_inf - J_P| <= (4/3)(2log P+3)/P, P>=2.
        """
        if not self.is_genuine_prefix():
            raise PathDomainError("The prime tail bound requires true complete Euler source")
        mp=_mp()
        with mp.workdps(dps):
            return mp.mpf(4)*(2*mp.log(self.horizon)+3)/(3*self.horizon)

    def genuine_pi_squared_tail_bound(self):
        """0 <= pi² - 6 Z_P(2) <= 6/P for genuine complete prefixes."""
        if not self.is_genuine_prefix():
            raise PathDomainError("Requires genuine consecutive prime prefix")
        return Fraction(6,self.horizon)


def _mprat(mp,q):
    q=Fraction(q)
    return mp.mpf(q.numerator)/q.denominator


def gamma_periodic_gauge(z,epsilon,*,dps=60):
    """A fake Gamma sharing EVERY positive-integer factorial & SUCC recurrence.

    Gamma_eps(z)=Gamma(z) exp(eps sin(2*pi*z)). A nonzero eps violates
    global log-convexity at sufficiently large positive real z; hence
    SUCC recurrence plus integer values alone cannot specify Gamma.
    """
    mp=_mp()
    with mp.workdps(dps):
        z=mp.mpf(z)
        if z<=0:
            raise PathDomainError("Positive real gamma chart only")
        eps=mp.mpf(epsilon)
        if z == mp.floor(z):
            # Sin(2*pi*n) is algebraically zero; do not turn its
            # finite-precision approximation into an enormous factorial error.
            return mp.gamma(z)
        return mp.gamma(z)*mp.exp(eps*mp.sin(2*mp.pi*z))


def gamma_periodic_log_curvature(z,epsilon,*,dps=60):
    """Second z-derivative of log Gamma_eps on positive real axis."""
    mp=_mp()
    with mp.workdps(dps):
        z,eps=mp.mpf(z),mp.mpf(epsilon)
        if z<=0:
            raise PathDomainError("Positive real gamma chart only")
        return mp.polygamma(1,z)-eps*(2*mp.pi)**2*mp.sin(2*mp.pi*z)
