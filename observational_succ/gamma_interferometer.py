"""Causal finite-source to archimedean Suzuki-Psi correlation bridge.

Exact real-rational Dirichlet-log source, integrated-prefix only.  The
zeta-normalized response for mutated sources is a CONTROL, not the Weil form
of an arbitrary L-function. No zero data or assumed positive Gram enters.

mpmath is loaded lazily; core observational_succ remains standard-library only.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Mapping


class InterferometerError(ValueError):
    """The source, exactness, or causal horizon contract failed."""


def _as_real_rational(value):
    if type(value) is int or isinstance(value, Fraction):
        return Fraction(value)
    if hasattr(value, "re") and hasattr(value, "im"):
        if value.im:
            raise InterferometerError("Complex source requires its own completed L-factor")
        return Fraction(value.re)
    raise InterferometerError("Source coefficients must be exact rational or real Q(i), never floats")


def _prime_power(n):
    if n < 2:
        return None
    for p in range(2, isqrt(n) + 1):
        if n % p:
            continue
        v, k = n, 0
        while v % p == 0:
            v //= p
            k += 1
        return (p, k) if v == 1 else None
    return n, 1


def _formal_convolution_log(a, nmax):
    """Exact b=log_*(a) over Q; every factor in each h^*r is >=2."""
    h = [Fraction(0), Fraction(0)] + [a[n] for n in range(2, nmax + 1)]
    b = [Fraction(0) for _ in range(nmax + 1)]
    power = h[:]
    r = 1
    while (1 << r) <= nmax:
        coefficient = Fraction(1 if r % 2 else -1, r)
        for n in range(2, nmax + 1):
            b[n] += coefficient * power[n]
        nxt = [Fraction(0) for _ in range(nmax + 1)]
        for d in range(2, nmax + 1):
            if not power[d]:
                continue
            for k in range(2, nmax // d + 1):
                if h[k]:
                    nxt[d * k] += power[d] * h[k]
        power = nxt
        r += 1
    return tuple(b)


def _mp():
    try:
        import mpmath
    except ImportError as exc:
        raise InterferometerError("Install mpmath to evaluate Gamma transport") from exc
    return mpmath


def _mprat(mp, r):
    return mp.mpf(r.numerator) / r.denominator


def archimedean_response(t, *, dps=55):
    """Exact Suzuki zeta normalization: poles + Gamma, not Gamma alone."""
    mp = _mp()
    with mp.workdps(dps):
        t = mp.mpf(t)
        if t < 0:
            raise InterferometerError("Requires nonnegative logarithmic time")
        if t == 0:
            return mp.mpf(0)
        q = mp.mpf(1) / 4
        pole = 4 * (mp.exp(t / 2) + mp.exp(-t / 2) - 2)
        gamma_linear = (t / 2) * (mp.digamma(q) - mp.log(mp.pi))
        gamma_remainder = (mp.pi**2 + 8 * mp.catalan
                           - mp.exp(-t / 2) * mp.lerchphi(mp.exp(-2*t), 2, q)) / 4
        return pole + gamma_linear + gamma_remainder


@dataclass(frozen=True)
class GammaInterferometer:
    """Immutable snapshot: its input must be an integrated, complete prefix."""
    horizon: int
    coefficients: tuple[Fraction, ...]
    connected: tuple[Fraction, ...]
    trace_head: str | None = None

    @classmethod
    def from_prefix(cls, source: Mapping[int, object], horizon: int, *, trace_head=None):
        if type(horizon) is not int or not 2 <= horizon <= 256:
            raise InterferometerError("Horizon must be an exact integer in 2..256")
        a = [Fraction(0)]
        for n in range(1, horizon + 1):
            try:
                a.append(_as_real_rational(source[n]))
            except KeyError as exc:
                raise InterferometerError(f"Event {n} not integrated; missing source cannot be predicted") from exc
        if a[1] != 1:
            raise InterferometerError("Dirichlet-log source requires a(1)=1")
        return cls(horizon, tuple(a), _formal_convolution_log(a, horizon), trace_head)

    @classmethod
    def from_engine(cls, engine, horizon=None):
        if not getattr(engine, "arithmetic", False):
            raise InterferometerError("Only natural arithmetic observational_succ is supported")
        integrated = engine.coefficients  # NOT pending observations or predictions
        if horizon is None:
            horizon = max(integrated, default=0)
        return cls.from_prefix(integrated, horizon, trace_head=engine.head)

    @property
    def matches_zeta_prefix(self):
        return all(x == 1 for x in self.coefficients[1:])

    def diagnostic(self):
        mixed, towers = [], []
        for n in range(2, self.horizon + 1):
            pk = _prime_power(n)
            if pk is None and self.connected[n]:
                mixed.append(n)
            elif pk is not None and self.connected[n] != Fraction(1, pk[1]):
                towers.append(n)
        return {
            "horizon": self.horizon, "zeta_prefix": self.matches_zeta_prefix,
            "non_prime_power_connected_anomalies": mixed,
            "prime_power_weight_anomalies": towers,
            "scope": "finite Euler-source audit, not RH or full Weil positivity",
        }

    def _response(self, t, *, dps=55, event_label=None):
        mp = _mp()
        with mp.workdps(dps):
            t = mp.mpf(t)
            if t < 0:
                raise InterferometerError("Use nonnegative time or even extension")
            if event_label is not None:
                if not 1 <= event_label <= self.horizon:
                    raise InterferometerError("Event outside integrated horizon")
                t = mp.log(event_label)
            elif t > mp.log(self.horizon):
                raise InterferometerError("Time exceeds integrated horizon")
            arch = archimedean_response(t, dps=dps)
            prime, active = mp.mpf(0), 0
            for n in range(2, self.horizon + 1):
                if event_label is not None:
                    present = n <= event_label
                else:
                    gap = t - mp.log(n)
                    if abs(gap) < mp.power(10, -max(8, dps // 2)):
                        raise InterferometerError("Ambiguous boundary: use at_event(n)")
                    present = gap >= 0
                if present and self.connected[n]:
                    a = mp.log(n)
                    prime += _mprat(mp, self.connected[n]) * mp.log(n) / mp.sqrt(n) * (t - a)
                    active += 1
            return {
                "t": t, "arch": arch, "finite": prime, "psi": arch-prime,
                "active_channels": active, "horizon": self.horizon,
                "trace_head": self.trace_head, "zeta_prefix": self.matches_zeta_prefix,
            }

    def at_event(self, n: int, *, dps=55):
        if type(n) is not int:
            raise InterferometerError("Event labels must be exact integers")
        return self._response(0, dps=dps, event_label=n)

    def at_time(self, t, *, dps=55):
        return self._response(t, dps=dps)

    def slope_jump(self, n: int, *, dps=55):
        """Outgoing minus incoming derivative at log(n)."""
        if type(n) is not int or not 2 <= n <= self.horizon:
            raise InterferometerError("Slope jump requires integrated event")
        mp = _mp()
        with mp.workdps(dps):
            return -_mprat(mp, self.connected[n]) * mp.log(n) / mp.sqrt(n)

    def screw(self, t, u, *, dps=55):
        """Two-time screw kernel; this method asserts NO positive sign."""
        mp = _mp()
        with mp.workdps(dps):
            t, u = mp.mpf(t), mp.mpf(u)
            def psi(x):
                return self.at_time(abs(x), dps=dps)["psi"]
            return psi(t) + psi(u) - psi(t-u)


def individual_impulse_determinant(a, w, *, dps=55):
    """Exact formula: det K(3a/4,5a/4) = -w*w*a*a/16 < 0.

    K(t,u)=-w[h_a(t)+h_a(u)-h_a(t-u)],
    h_a(t)=(abs(t)-a)_+. Thus neither sign of a nonzero isolated
    impulse gives a PSD screw kernel. The global Gamma coupling may differ.
    """
    mp = _mp()
    with mp.workdps(dps):
        a, w = mp.mpf(a), mp.mpf(w)
        if not a > 0 or not w:
            raise InterferometerError("Require a>0 and nonzero real event weight")
        t1, t2 = 3*a/4, 5*a/4
        h = lambda x: max(mp.mpf(0), abs(x)-a)
        k = lambda x,y: -w*(h(x)+h(y)-h(x-y))
        return k(t1,t1)*k(t2,t2)-k(t1,t2)**2
