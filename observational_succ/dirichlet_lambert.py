"""Source-faithful Lambert W in the *Dirichlet-convolution* algebra.

Unlike applying scalar W to log(n!), this retains the labelled
multiplicative decomposition of each source coefficient.

For a(1)=1 let h=a-delta_1. In the coefficientwise completed
Dirichlet-convolution ring define
    W_*(h) = sum_(k>=1) (-k)^(k-1)/k! h^(*k).
The sum is FINITE at each integer n: factors in a k-fold convolution
are >=2, so k<=floor(log_2 n). It uniquely solves
    W_*(h) * exp_*(W_*(h)) = h.
Here '*' is Dirichlet convolution, NOT pointwise multiplication.

The transform is sensitive to mixed-composite mutations, but in general
W_*(h)(6) != 0 even for a perfectly genuine Euler product. It is not
a multiplicativity certificate, positivity theorem, or RH reduction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Mapping


class ArithmeticWError(ValueError):
    pass


def _exact_real(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    if hasattr(x, "re") and hasattr(x, "im") and not x.im:
        return Fraction(x.re)
    raise ArithmeticWError("Only exact rational real coefficients are currently supported")


def _horizon(n):
    if type(n) is not int or not 2 <= n <= 256:
        raise ArithmeticWError("Finite source horizon must be an integer in 2..256")
    return n


def convolve(a, b):
    """Truncated Dirichlet convolution on equal-length coefficient tuples."""
    if not isinstance(a, tuple) or not isinstance(b, tuple) or len(a) != len(b):
        raise ArithmeticWError("Expected equal-length coefficient tuples")
    nmax=len(a)-1
    if nmax<2 or a[0]!=0 or b[0]!=0:
        raise ArithmeticWError("Coefficient index 0 is reserved and must vanish")
    out=[Fraction(0)]*(nmax+1)
    for n in range(1,nmax+1):
        if not a[n]:
            continue
        for k in range(1,nmax//n+1):
            if b[k]:
                out[n*k]+=_exact_real(a[n])*_exact_real(b[k])
    return tuple(out)


def identity(nmax):
    _horizon(nmax)
    return tuple([Fraction(0),Fraction(1)]+[Fraction(0)]*(nmax-1))


def _star_series(h, coeff):
    """Apply scalar formal series coefficients through local Dirichlet powers."""
    nmax=len(h)-1
    if not h or h[1]!=0 or h[0]!=0 or nmax<2:
        raise ArithmeticWError("Formal series input must be in augmentation ideal h(1)=0")
    power=h
    result=[Fraction(0)]*(nmax+1)
    k=1
    while (1<<k)<=nmax:
        scale=coeff(k)
        for n in range(2,nmax+1):
            if power[n]:
                result[n]+=scale*power[n]
        power=convolve(power,h)
        k+=1
    return tuple(result)


def star_lambert_w(h):
    """Formal principal Lambert W, uniquely determined at zero by W(0)=0."""
    return _star_series(h,lambda k: Fraction((-k)**(k-1),factorial(k)))


def star_log_unit(a):
    """Dirichlet logarithm of a(1)=1; the connected Euler coefficients."""
    nmax=len(a)-1
    if a[1]!=1:
        raise ArithmeticWError("Connected source requires a(1)=1")
    h=tuple(Fraction(0) if n<=1 else _exact_real(a[n]) for n in range(nmax+1))
    return _star_series(h,lambda k: Fraction((-1)**(k+1),k))


def star_exp(w):
    """Formal convolution exponential of an augmentation-ideal element."""
    nmax=len(w)-1
    if w[1]!=0:
        raise ArithmeticWError("Convolution exp requires w(1)=0")
    ident=identity(nmax)
    power=ident
    out=list(ident)
    k=1
    while (1<<k)<=nmax:
        power=convolve(power,w)
        inv=Fraction(1,factorial(k))
        for n in range(2,nmax+1):
            if power[n]:
                out[n]+=inv*power[n]
        k+=1
    return tuple(out)


def _factor_paths(n, max_paths=5000):
    """Independent ordered-factor witness enumerator, not the production star."""
    if type(n) is not int or not 2<=n<=64:
        raise ArithmeticWError("Finite witness n must be in 2..64")
    paths=[]
    def visit(rem,prefix):
        if len(paths)>=max_paths:
            raise ArithmeticWError("Witness path budget exceeded")
        if rem==1:
            paths.append(prefix)
            return
        for d in range(2,rem+1):
            if rem%d==0:
                visit(rem//d,prefix+(d,))
    visit(n,())
    return tuple(paths)


@dataclass(frozen=True)
class DirichletLambertSnapshot:
    horizon: int
    source: tuple[Fraction,...]
    h: tuple[Fraction,...]
    w: tuple[Fraction,...]
    connected: tuple[Fraction,...]
    source_head: str | None = None

    @classmethod
    def from_prefix(cls, source: Mapping[int,object], horizon: int, *, source_head=None):
        horizon=_horizon(horizon)
        if not isinstance(source, Mapping):
            raise ArithmeticWError("Source must be a mapping of integrated coefficients")
        a=[Fraction(0)]
        for n in range(1,horizon+1):
            if n not in source:
                raise ArithmeticWError(f"Missing integrated source coefficient a({n})")
            a.append(_exact_real(source[n]))
        if a[1]!=1:
            raise ArithmeticWError("Normalized arithmetic source needs a(1)=1")
        h=tuple(Fraction(0) if n<=1 else a[n] for n in range(horizon+1))
        return cls(horizon,tuple(a),h,star_lambert_w(h),
                   star_log_unit(tuple(a)),source_head)

    @classmethod
    def from_engine(cls, engine, horizon=None):
        """Same causal scope as prior gamma interferometer: integrated only."""
        from .gamma_interferometer import GammaInterferometer, InterferometerError
        try:
            complete=GammaInterferometer.from_engine(engine,horizon)
        except (InterferometerError,KeyError,ValueError) as exc:
            raise ArithmeticWError("Complete integrated source prefix required") from exc
        return cls.from_prefix(
            {n:complete.coefficients[n] for n in range(1,complete.horizon+1)},
            complete.horizon,source_head=complete.trace_head)

    def verify_inverse_identity(self):
        """All coefficients of w * exp_*(w) = h, without zero data."""
        return convolve(self.w,star_exp(self.w)) == self.h

    def preserve_prefix(self, longer):
        """Filtration compatibility: future source events cannot alter prior w."""
        if not isinstance(longer,DirichletLambertSnapshot) or longer.horizon<self.horizon:
            raise ArithmeticWError("Compare a larger source horizon")
        if longer.source[:self.horizon+1]!=self.source:
            raise ArithmeticWError("Earlier source observations were changed")
        return longer.w[:self.horizon+1]==self.w

    def composite_six(self):
        """Exact connected Euler discriminator extracted from the W_* coordinates.

        w(6)=a(6)-2a(2)a(3);
        w(6)+a(2)a(3)=a(6)-a(2)a(3)=log_*(a)(6).
        The W transform ALONE does not yield the correct Euler support.
        """
        if self.horizon<6:
            raise ArithmeticWError("Six must have been integrated")
        relation=self.w[6]+self.source[2]*self.source[3]
        if relation!=self.connected[6]:
            raise ArithmeticError("Arithmetic W/Euler-log relation failed")
        return {
            "w6":str(self.w[6]),"a2a3":str(self.source[2]*self.source[3]),
            "connected_b6":str(relation),
            "mixed_composite_euler_consistent":relation==0,
            "source_head":self.source_head,
        }

    def witnesses(self,n):
        if type(n) is not int or not 2<=n<=min(64,self.horizon):
            raise ArithmeticWError("Bounded witness must be within integrated horizon <=64")
        result=[]
        for path in _factor_paths(n):
            k=len(path)
            weight=Fraction((-k)**(k-1),factorial(k))
            amplitude=weight
            for m in path:
                amplitude*=self.h[m]
            result.append({"factors":list(path),"length":k,
                           "tree_weight":str(weight),"signed_amplitude":str(amplitude)})
        # Independent history expansion checks the optimized Dirichlet convolution.
        if sum((Fraction(x["signed_amplitude"]) for x in result),Fraction(0))!=self.w[n]:
            raise ArithmeticError("Independent ordered-path enumeration disagrees")
        return result

    def analytic_mellin_probe(self, s, *, dps=65):
        """Safe analytic intertwiner: D(W_*h)(s) = W_0(Dh(s)).

        Uses a finite supported h. Equality holds for the entire (infinite)
        formal W_*h once ||h||_sigma < 1/e; truncating its output at
        n<=horizon is only an approximation. Missing-path tail bounds
        use absolute series, not zero information. This mpmath diagnostic
        is NOT interval-arithmetic certification.
        """
        try:
            import mpmath as mp
        except ImportError as exc:
            raise ArithmeticWError("mpmath needed for analytic Mellin check") from exc
        with mp.workdps(dps):
            s=mp.mpc(s)
            sig=mp.re(s)
            if sig<1:
                raise ArithmeticWError("Probe only the declared convergent positive half-plane")
            def number(q):
                return mp.mpf(q.numerator)/q.denominator
            abs_mass=mp.fsum(number(abs(self.h[n]))*mp.power(n,-sig)
                             for n in range(2,self.horizon+1))
            if abs_mass>=1/mp.e:
                raise ArithmeticWError("Safe Lambert germ requires ||h||_sigma < 1/e")
            Dh=mp.fsum(number(self.h[n])*mp.power(n,-s)
                       for n in range(2,self.horizon+1))
            W_total=mp.lambertw(Dh,0)
            finite=mp.fsum(number(self.w[n])*mp.power(n,-s)
                            for n in range(2,self.horizon+1))
            # Positive absolute coefficient mass of the full W_*(h)
            # is -W_0(-||h||_sigma) by the rooted-tree coefficient series.
            full_absolute=-mp.lambertw(-abs_mass,0)
            abs_h=tuple(abs(q) for q in self.h)
            power=abs_h
            known_absolute=mp.mpf(0)
            k=1
            while (1<<k)<=self.horizon:
                c=mp.mpf(k**(k-1))/factorial(k)
                known_absolute+=c*mp.fsum(
                    number(power[n])*mp.power(n,-sig)
                    for n in range(2,self.horizon+1))
                power=convolve(power,abs_h)
                k+=1
            error_bound=max(mp.mpf(0),full_absolute-known_absolute)
            return {
                "input":+Dh,
                "analytic_lambert":+W_total,
                "finite_star_sum":+finite,
                "absolute_error":+abs(W_total-finite),
                "truncation_bound":+error_bound,
                "abs_input_mass":+abs_mass,
                "scope":"safe Mellin intertwiner; numerical bound evaluation, NOT RH",
            }
