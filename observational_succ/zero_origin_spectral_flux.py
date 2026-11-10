"""Zero-origin spectral flux diagnostics for the original four-pole BBP orbit.

Research only.  Finite, source-authenticated data and conservation identities
are NOT a proof of pi-normality or a physical energy law.  Python >=3.10,
standard library only.  Uses the existing, frozen duck_bbp forcing/tail API.

Digiting convention: digit n (1-based) is floor(16*{16^(n-1)*pi})
for n >= 1. The identity U_n+T_n=16^(n-1)*pi is an imported classical
BBP bridge. We certify each digit using rational U_n and rational T_n bounds.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import cos, pi, sin, sqrt
from typing import Iterable, Sequence

from .duck_bbp import forcing, source_tail_budget, tail_interval

ALPHABET = 16
SHIFTS = (3, 4, 5)
WEIGHTS = (2, 1, 1)


def channel_forcings(n: int) -> tuple[Fraction, Fraction, Fraction]:
    """Three exact positive differences whose sum is the genuine forcing."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    a = 8 * n - 7
    return tuple(Fraction(w * d, a * (a + d))
                 for d, w in zip(SHIFTS, WEIGHTS))


def integer_floor(x: Fraction) -> int:
    return x.numerator // x.denominator


@dataclass(frozen=True)
class CertifiedTrace:
    digits: tuple[int, ...]
    carries: tuple[int, ...]
    orbit_phases: tuple[float, ...]  # diagnostics only; exact states checked first
    channel_phases: tuple[tuple[float, ...], ...]
    max_tail_depth: int
    tail_refinements: int
    verified_phase_steps: int
    seed: int = 0

    @property
    def count(self) -> int:
        return len(self.digits)


def certified_zero_orbit(count: int, max_tail_depth: int = 48,
                         channels_until: int = 1024) -> CertifiedTrace:
    """Build zero-origin orbit sequentially and certify HEX digits exactly.

    Every claimed digit is identified by TWO rational endpoints enclosing the
    completed real source. Ambiguity aborts; it is never rounded away.  A
    *different* source/seed is not silently substituted at a failing step.
    """
    if type(count) is not int or count < 1:
        raise ValueError("count >= 1 required")
    if type(max_tail_depth) is not int or max_tail_depth < 0:
        raise ValueError("max_tail_depth >= 0 required")
    if type(channels_until) is not int or channels_until < 0:
        raise ValueError("channels_until >= 0 required")
    state = Fraction(0)  # original U0, on the circle
    channel_states = [Fraction(0), Fraction(0), Fraction(0)]
    digits: list[int] = []
    carries: list[int] = []
    orbit: list[float] = []
    channels: list[list[float]] = [[], [], []]
    refinements = 0
    largest_depth = 0
    for n in range(1, count + 1):
        parts = channel_forcings(n)
        source = forcing(n)
        if sum(parts, Fraction(0)) != source:
            raise AssertionError("source channel decomposition broken")
        raw = 16 * state + source
        carry = integer_floor(raw)
        state = raw - carry
        if not (0 <= state < 1):
            raise AssertionError("invalid real circle representative")
        if n <= channels_until:
            for i, part in enumerate(parts):
                channel_states[i] = (16 * channel_states[i] + part) % 1
            if (sum(channel_states, Fraction(0)) % 1) != state:
                raise AssertionError("channel-phase reconstruction failed")
        # For the zero seed ONLY: U_n + T_n = 16^(n-1) pi.
        lower = state
        upper = state + source_tail_budget(n)
        depth = 0
        while integer_floor(16 * lower) != integer_floor(16 * upper):
            depth += 1
            if depth > max_tail_depth:
                raise ArithmeticError(
                    f"digit n={n} unresolved at tail depth {max_tail_depth}"
                )
            partial_lo, partial_hi = tail_interval(n, depth)
            lower, upper = state + partial_lo, state + partial_hi
        if depth:
            refinements += 1
            largest_depth = max(largest_depth, depth)
        digits.append(integer_floor(16 * lower) % 16)
        carries.append(carry)
        orbit.append(float(state))
        if n <= channels_until:
            for i, part_state in enumerate(channel_states):
                channels[i].append(float(part_state))
    return CertifiedTrace(tuple(digits), tuple(carries), tuple(orbit),
                          tuple(tuple(c) for c in channels),
                          largest_depth, refinements, min(count,channels_until))


def histograms_cyclic(digits: Sequence[int], depth: int) -> Counter[tuple[int, ...]]:
    """All N cyclic words. This convention preserves exact marginalization."""
    n = len(digits)
    if n < 1 or type(depth) is not int or depth < 1:
        raise ValueError("nonempty digits and depth>=1 required")
    if depth > n:
        raise ValueError("depth must not exceed cyclic period")
    if any(type(d) is not int or not (0 <= d < 16) for d in digits):
        raise ValueError("hex digits must be integers 0..15")
    return Counter(tuple(digits[(i+j) % n] for j in range(depth))
                   for i in range(n))


def histograms_linear(digits: Sequence[int], depth: int) -> Counter[tuple[int, ...]]:
    """No wrap; these counts differ from cyclic counts at most depth-1 starts."""
    n = len(digits)
    if type(depth) is not int or not 1 <= depth <= n:
        raise ValueError("1 <= depth <= N")
    return Counter(tuple(digits[i:i+depth]) for i in range(n-depth+1))


def discrepancy_energy(counts: Counter, count: int, depth: int) -> Fraction:
    """E_k = 16^k sum(p_k -16^-k)^2; exact rational."""
    if count <= 0 or sum(counts.values()) != count:
        raise ValueError("count mismatch")
    if depth < 1:
        raise ValueError("depth >= 1")
    return Fraction(16**depth * sum(c*c for c in counts.values()) - count*count,
                    count*count)


def refinement_flux(coarse: Counter, fine: Counter, n: int, depth: int) -> Fraction:
    """Exact positive flux E_(k+1)-E_k from 15 new Fourier sectors per parent.

    Uses p_(k+1)(wa)-p_k(w)/16. This is the orthogonal Fourier complement
    with a nonzero character in the new digit coordinate.
    """
    if type(depth) is not int or depth < 1 or n <= 0:
        raise ValueError("depth >=1 and n>0")
    if sum(coarse.values()) != n or sum(fine.values()) != n:
        raise ValueError("count mismatch")
    if any(sum(fine.get(w+(a,), 0) for a in range(16)) != c
           for w, c in coarse.items()):
        raise ValueError("incompatible marginal counts")
    return Fraction(16**(depth - 1) * sum(
        (16*fine.get(w+(a,), 0) - c)**2
        for w, c in coarse.items() for a in range(16)
    ), n*n)


def energy_ladder(digits: Sequence[int], depth: int = 3) -> dict:
    if len(digits) < depth:
        raise ValueError("N must be >= requested depth")
    cs = [histograms_cyclic(digits, k) for k in range(1, depth+1)]
    es = [discrepancy_energy(c, len(digits), k) for k,c in enumerate(cs,1)]
    fs = [refinement_flux(cs[k], cs[k+1], len(digits), k+1)
          for k in range(depth-1)]
    if any(es[k+1]-es[k] != fs[k] for k in range(depth-1)):
        raise AssertionError("exact orthogonal flux identity failed")
    return {"energies": es, "new_mode_flux": fs,
            "support": [len(c) for c in cs],
            "linear_start_count": [len(digits)-k+1 for k in range(1,depth+1)]}


def online_word_surplus(digits: Sequence[int], depth: int) -> dict:
    """Exact arrival-by-arrival signed discrepancy impulse for linear words.

    D(M)=sum_w (C_w-M/B)^2.  New word a makes D(M+1)-D(M)=
       2(C_a-M/B)+(1-1/B).
    This is kinematics, NOT a proved negative-drift or anti-clumping law.
    """
    if type(depth) is not int or depth < 1 or len(digits) < depth:
        raise ValueError("invalid depth")
    b = 16**depth
    counts = Counter()
    arrivals = 0
    reinforcing = 0
    opposing = 0
    zero = 0
    signed_surplus_sum = 0  # integer B*C_a - M
    max_surplus = -10**30
    max_deficit = 10**30
    lhs_total = Fraction(0)
    q = 0
    for i in range(len(digits)-depth+1):
        w = tuple(digits[i:i+depth])
        before = counts[w] * b - arrivals
        after_step = Fraction(2*before + b-1, b)
        old_q = q
        old_d = Fraction(old_q) - Fraction(arrivals*arrivals, b)
        counts[w] += 1
        arrivals += 1
        new_q = old_q + 2*(counts[w]-1)+1
        q = new_q
        new_d = Fraction(new_q) - Fraction(arrivals*arrivals, b)
        if new_d - old_d != after_step:
            raise AssertionError("linear signed arrival balance failed")
        lhs_total += after_step
        reinforcing += before > 0
        opposing += before < 0
        zero += before == 0
        max_surplus = max(max_surplus, before)
        max_deficit = min(max_deficit, before)
        signed_surplus_sum += before
    return {"depth": depth, "windows": arrivals,
            "reinforcing": reinforcing, "opposing": opposing, "neutral": zero,
            "signed_surplus_mean": Fraction(signed_surplus_sum, b*arrivals),
            "max_surplus_units": Fraction(max_surplus,b),
            "min_surplus_units": Fraction(max_deficit,b),
            "unscaled_discrepancy_final": lhs_total}


def fft_radix_two(values: Sequence[complex]) -> list[complex]:
    """Unnormalized forward FFT with exp(-2 pi i m*n/N). Diagnostics only."""
    n = len(values)
    if n <= 0 or n & (n-1):
        raise ValueError("FFT length must be positive power of 2")
    out = [complex(v) for v in values]
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            out[i], out[j] = out[j], out[i]
    length=2
    while length<=n:
        wlen=complex(cos(-2*pi/length), sin(-2*pi/length))
        for off in range(0,n,length):
            w=1+0j
            for k in range(off,off+length//2):
                u=out[k];v=out[k+length//2]*w
                out[k]=u+v
                out[k+length//2]=u-v
                w*=wlen
        length*=2
    return out


def spectral_line_summary(digits: Sequence[int], h: int = 1) -> dict:
    """Total normalized FFT power is 1 for all samples (Parseval).

    DC = histogram character energy; nonzero lines measure temporal pattern.
    Spectral concentration is descriptive, not normality evidence.
    """
    if type(h) is not int or not 1 <= h <= 15:
        raise ValueError("1<=h<=15")
    n = len(digits)
    chars=[complex(cos(2*pi*h*d/16),sin(2*pi*h*d/16)) for d in digits]
    spec=fft_radix_two(chars)
    powers=[abs(x/n)**2 for x in spec]
    best=max(range(1,n),key=lambda i:powers[i]) if n>1 else 0
    total=sum(powers)
    if abs(total-1.0)>1e-9:
        raise AssertionError(f"Parseval discrepancy {total}")
    return {"h":h, "length":n,
            "dc_power":powers[0],"largest_nonzero_power":powers[best],
            "largest_nonzero_index":best,
            "largest_nonzero_period":(n/min(best,n-best) if best else None),
            "power_total":total,
            "inverse_participation":1/sum(x*x for x in powers),
            "power_at_period_16":powers[n//16] if n>=16 and n%16==0 else None,
            "power_at_period_2":powers[n//2] if n>=2 else None}


def temporal_flux(digits: Sequence[int], h: int, period: int, mode: int = 1,
                  thresholds: tuple[float,...] = (1.0,2.0,3.0)) -> dict:
    """Drive one frequency and retain signed Reinforce/Cancel work.

    S_(t+1)=S_t + u_t, |u_t|=1.
    Exact identity: |S_(t+1)|^2-|S_t|^2=1+2*Re(conj(S_t)*u_t).
    No negative drift is assumed, and coherent controls must fail it.
    """
    if not 1<=h<=15 or period<=1 or not 0<mode<period:
        raise ValueError("frequency parameters invalid")
    phase_table=[complex(cos(2*pi*h*d/16),sin(2*pi*h*d/16)) for d in range(16)]
    rotating=[complex(cos(-2*pi*mode*r/period),sin(-2*pi*mode*r/period))
              for r in range(period)]
    state=complex(0)
    bins={str(t):[0,0.,0.] for t in thresholds}
    all_work=0.
    peak_amplitude=0.
    for t,d in enumerate(digits):
        u=phase_table[d]*rotating[t%period]
        amplitude=abs(state)
        if t:
            normal=amplitude/sqrt(t)
            work=(state.conjugate()*u).real
            all_work+=work
            peak_amplitude=max(peak_amplitude,normal)
            for threshold in thresholds:
                if normal>=threshold:
                    z=bins[str(threshold)]
                    z[0]+=1;z[1]+=work;z[2]+=int(work<0)
        state+=u
    return {"period":period,"mode":mode,"h":h,
            "terminal_power":abs(state/len(digits))**2,
            "max_sqrt_time_amplitude":peak_amplitude,
            "mean_signed_work":all_work/max(1,len(digits)-1),
            "conditional_work":{key:{"observations":v[0],
                                     "mean_work":v[1]/v[0] if v[0] else None,
                                     "fraction_negative":v[2]/v[0] if v[0] else None}
                                for key,v in bins.items()}}


def spectrum_by_clock_residue(digits: Sequence[int], modulus: int) -> dict:
    """Temporal stratification: each residue class is an independent readout.

    No independent digit law or common drift is assumed.  The grouping alone
    can detect periodic sources whose global histogram is perfectly flat.
    """
    if type(modulus) is not int or modulus < 1 or not digits:
        raise ValueError("positive modulus and nonempty stream required")
    classes=[[0]*16 for _ in range(modulus)]
    for n,d in enumerate(digits):
        classes[n%modulus][d]+=1
    deviations=[max(abs(c/sum(row)-1/16) for c in row) if sum(row) else 0.
                for row in classes]
    return {"modulus":modulus,"class_sizes":[sum(x) for x in classes],
            "max_within_class_digit_bias":max(deviations),
            "mean_within_class_digit_bias":sum(deviations)/modulus}


def energy_checkpoint(digits: Sequence[int], depths: int = 3) -> dict:
    ladder=energy_ladder(digits,depths)
    n=len(digits)
    return {"n":n,
            "digit_counts":[digits.count(i) for i in range(16)],
            "digit_energy":float(ladder["energies"][0]),
            "word_energies":[float(x) for x in ladder["energies"]],
            "depth_flux":[float(x) for x in ladder["new_mode_flux"]],
            "word_support":ladder["support"],
            "spectral":spectral_line_summary(digits,1) if n>1 and not n&(n-1) else None,
            "residue_strata":[spectrum_by_clock_residue(digits,q)
                              for q in (2,4,8,16) if n>=q]}


def de_bruijn_hex(order: int) -> tuple[int,...]:
    """Classical de Bruijn cycle, alphabet 16, each order-k word occurs once."""
    if type(order) is not int or not 1 <= order <= 4:
        raise ValueError("order must be in [1,4]")
    a=[0]*(16*order)
    result=[]
    def db(t:int,p:int):
        if t>order:
            if order%p==0:
                result.extend(a[1:p+1])
            return
        a[t]=a[t-p]
        db(t+1,p)
        for j in range(a[t-p]+1,16):
            a[t]=j
            db(t+1,t)
    db(1,1)
    if len(result)!=16**order:
        raise AssertionError("deBruijn length invalid")
    return tuple(result)


def spectral_feedback_toy(length: int, seed: int = 20261108,
                          beta: float = 0.65, window: int = 64) -> tuple[int,...]:
    """Explicitly artificial spectral-feedback generator, NOT a model of pi.

    Four temporal spectral modes with periods 16,8,4,2 receive negative
    feedback when their present complex amplitudes are reinforced. The DC
    mode is *not* penalized: a digit may repeat arbitrarily often, and
    every next digit always has positive probability.

    This construction tests distinguishability from a shuffle; any spectral
    suppression is BY DESIGN, not evidence that genuine BBP has feedback.
    """
    import random
    from math import exp
    if type(length) is not int or length < 1 or type(window) is not int or window < 16:
        raise ValueError("invalid stream length/window")
    if not (0 <= beta <= 10):
        raise ValueError("beta must lie in [0,10]")
    rng = random.Random(seed)
    digit_phases = [complex(cos(2*pi*d/16),sin(2*pi*d/16)) for d in range(16)]
    modes=(1,2,4,8)
    rotations={m:tuple(complex(cos(-2*pi*m*t/16),sin(-2*pi*m*t/16))
                       for t in range(16)) for m in modes}
    sums={m:0j for m in modes}
    past=[]
    for t in range(length):
        rotated={m:rotations[m][t%16] for m in modes}
        raw=[]
        for d in range(16):
            signed=sum((sums[m].conjugate()*digit_phases[d]*rotated[m]).real
                       for m in modes)/4
            raw.append(-beta*2*signed/sqrt(window))
        maxraw=max(raw)
        weights=[exp(s-maxraw) for s in raw]
        u=rng.random()*sum(weights)
        chosen=15
        for d,w in enumerate(weights):
            u-=w
            if u<0:
                chosen=d;break
        past.append(chosen)
        for m in modes:
            sums[m]+=digit_phases[chosen]*rotated[m]
            if t>=window:
                old_digit=past[t-window]
                sums[m]-=digit_phases[old_digit]*rotations[m][(t-window)%16]
    return tuple(past)


def channel_phase_summary(trace: CertifiedTrace, start: int = 0) -> dict:
    """Check source-conditioned *joint phase* vs factorized channels.

    A scalar seed shift acts on the total by e(h*16^n*s); the three
    positive-source channel phases alone do not identify that seed.
    """
    end=len(trace.channel_phases[0])
    if not 0 <= start < end:
        raise ValueError("start outside channel-verified trace")
    n=end-start
    means=[0j]*3;joint=0j
    for j in range(start,end):
        vec=[complex(cos(2*pi*trace.channel_phases[k][j]),
                     sin(2*pi*trace.channel_phases[k][j])) for k in range(3)]
        for k in range(3):
            means[k]+=vec[k]/n
        joint+=vec[0]*vec[1]*vec[2]/n
    factorized=means[0]*means[1]*means[2]
    return {"joint_modulus":abs(joint),
            "factorized_modulus":abs(factorized),
            "factorization_residual_modulus":abs(joint-factorized),
            "channel_mean_moduli":[abs(x) for x in means]}


def signed_vdc_energy(phases: Sequence[float], h: int, horizon: int) -> dict:
    """Actual BBP phase f_n=e(hU_n); finite time-lag energy with ALL signs.

    The direct zero-padded moving sum and signed-correlation expansion agree.
    A user of this function must not infer normality from a finite sample.
    """
    n=len(phases)
    if not 1<=h<=15 or not 1<=horizon<=n:
        raise ValueError("invalid character/horizon")
    z=[complex(cos(2*pi*h*x),sin(2*pi*h*x)) for x in phases]
    lag=[]
    for ell in range(1,horizon):
        value=sum((z[j+ell]*z[j].conjugate() for j in range(n-ell)),0j)/n
        lag.append(value)
    signed=1/horizon + 2/horizon*sum(
        (1-(ell+1)/horizon)*val.real for ell,val in enumerate(lag))
    # Incremental pad sums F_t=sum_{j=0}^{H-1} z_(t+j) on t=-(H-1)..n-1.
    total=0j; squares=0.
    for t in range(-(horizon-1),n):
        if 0<=t+horizon-1<n:
            total+=z[t+horizon-1]
        if t-1>=0:
            total-=z[t-1]
        squares+=abs(total)**2
    direct=squares/(n*horizon*horizon)
    if abs(direct-signed)>1e-8:
        raise AssertionError("signed lag energy identity broken")
    w=sum(z)/n
    return {"h":h,"H":horizon,"N":n,
            "weyl_modulus":abs(w),"weyl_power":abs(w)**2,
            "signed_energy":signed,"direct_energy":direct,
            "vdc_upper_bound":(n+horizon-1)/n*direct,
            "first_lag_real":lag[0].real if lag else None}
