"""Front A finite receipts: Clausen gate controls and exact carry probes.

Deterministic. Exact Fraction source states; outward interval arithmetic
(mpmath.iv, precision set only inside local_prec()) for every transcendental Clausen value; numpy
float64 only for the instrument calibration of the pair-sum energies.
Finite numbers here certify NOTHING about pi's base-16 normality.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
import math

import numpy as np
from contextlib import contextmanager
from mpmath import iv

HERE = Path(__file__).resolve().parent
PREREG_A = (64, 173, 347, 691, 1024)
CARRY_A = (173, 347, 691, 1024)
H = 50                      # Clausen truncation; tail <= 2^-H/(H+1)
PREC = 80                   # interval working precision (bits), local only
TAIL = F(1, 2**H*(H+1))     # rigorous bound on sum_{h>H} 2^-h/h
LAST = 2*max(PREREG_A)+64


def forcing(n, mutant=False):
    """Authentic four-pole BBP increment (mutant: first numerator 4 -> 3)."""
    assert n >= 1
    c = 3 if mutant else 4
    v = F(c, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)
    collapsed = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    if mutant:
        collapsed -= F(1, 8*n-7)
    assert v == collapsed
    return v


def orbit(last=LAST, seed=F(0), mutant=False):
    """Exact x_n={U_n(seed)} for 0<=n<=last."""
    x = seed % 1
    out = [x]
    for n in range(1, last+1):
        y = 16*x+forcing(n, mutant)
        x = y-(y.numerator//y.denominator)
        out.append(x)
    return out


@lru_cache(None)
def green(n, terms=24):
    """Rational enclosure [lo,hi] of T_n=sum_{j>=1}16^-j r(n+j).

    Tail: sum_{j>terms}16^-j r(n+j)=16^-terms T_{n+terms}, and
    0<T_m<=1/((8m+1)(8m+2)) (#521 CT-03).
    """
    lo = sum((forcing(n+j)/16**j for j in range(1, terms+1)), F())
    m = n+terms
    return lo, lo+F(1, 16**terms*(8*m+1)*(8*m+2))


@contextmanager
def local_prec(bits=None):
    """Temporarily set the interval context precision; always restored."""
    old = iv.prec
    iv.prec = PREC if bits is None else bits
    try:
        yield
    finally:
        iv.prec = old


def ivf(q):
    return iv.mpf(q.numerator)/iv.mpf(q.denominator)


def clausen_from_phases(phase_lists):
    """Enclosure of Q_{1/2} from per-h lists of phase intervals (mod 1).

    phase_lists[h-1] is a list of iv phases for frequency h.
    Returns (lo, hi) Fractions-as-strings of Q_{1/2}, tail included.
    """
    total = iv.mpf(0)
    absc = []
    for h, phases in enumerate(phase_lists, start=1):
        A = len(phases)
        cr = iv.mpf(0)
        ci = iv.mpf(0)
        for t in phases:
            ang = 2*iv.pi*t
            cr += iv.cos(ang)
            ci += iv.sin(ang)
        cr /= A
        ci /= A
        mod2 = cr**2+ci**2
        absc.append(mod2)
        total += mod2/(iv.mpf(2)**h*h)
    tot = total+ivf(TAIL)*iv.mpf([0, 1])
    lo = math.nextafter(float(tot.a), -math.inf)   # outward double endpoints
    hi = math.nextafter(float(tot.b), math.inf)
    return lo, hi, absc


def exact_phases(xs, A):
    out = []
    for h in range(1, H+1):
        row = []
        for n in range(A, 2*A):
            q = xs[n]
            row.append(iv.mpf((h*q.numerator) % q.denominator)/iv.mpf(q.denominator))
        out.append(row)
    return out


def shifted_phases(base, A):
    """Phases of x_n={b_n - T_n}: b_n exact rational, T_n rational enclosure."""
    out = []
    for h in range(1, H+1):
        row = []
        for n in range(A, 2*A):
            b = base(n)
            lo, hi = green(n)
            a = F((h*b.numerator) % b.denominator, b.denominator)
            row.append(ivf(a)-iv.mpf([ivf(h*lo).a, ivf(h*hi).b]))
        out.append(row)
    return out


def s(x):
    return iv.nstr(x, 25) if not isinstance(x, str) else x


def mstr(v):
    return format(float(v), '.17g')


def clausen_record(phases, label, A):
    with local_prec():
        lo, hi, absc = clausen_from_phases(phases)
        rec = dict(label=label, A=A, H=H, Q_lo=mstr(lo), Q_hi=mstr(hi),
                   A_times_Q_hi=mstr(A*hi), abs_c1_sq_hi=mstr(math.nextafter(float(absc[0].b), math.inf)))
    return rec, float(lo), float(hi)


# ---------------------------------------------------------------- energies
def pair_energies(xs, A, r=0.5, hmax=60):
    """Float64 calibration: E_{A,r}(0) and P_{A,2A,r} (stable sinc form)."""
    x = np.array([float(xs[n]) for n in range(A, 2*A)])
    idx = np.arange(A, 2*A)
    I, J = np.triu_indices(A, 1)
    alpha = x[J]-x[I]
    Qij = 16.0**(idx[J]-2*A).astype(float)-16.0**(idx[I]-2*A).astype(float)
    E = np.sum(np.log(1+r*r-2*r*np.cos(2*np.pi*alpha)))/A**2
    P = 0.0
    for h in range(1, hmax+1):
        P += -2*r**h/h*np.sum(np.cos(2*np.pi*h*(alpha+Qij/2))*np.sinc(h*Qij))
    P /= A**2
    return float(E), float(P)


# ---------------------------------------------------------------- carries
def block(n, k):
    v = F(0)
    for j in range(1, k+1):
        v = 16*v+forcing(n+j)
    return v


def admissible(A, d):
    """Rigorous sufficient admissibility: 16^d T_n <= 1 for all n in [A,2A)."""
    return all(16**d*green(n)[1] <= 1 for n in range(A, 2*A))


def carry_epoch(xs, A, m, k, seed_coherent=False):
    """Exact J_{A,m,k} via HS-01; checks CB-1 identity at every n."""
    d = m+k
    J = F(0)
    mism = 0
    bits = []
    for n in range(A, 2*A):
        Sk = block(n, k)
        Sd = block(n, d)
        Sm = block(n+k, m)
        assert Sd == 16**m*Sk+Sm and Sd < 1
        delta = (16**m*Sk) % 1
        assert delta == Sd-Sm
        if seed_coherent:
            b = 0                     # x_{n+d}=1-T_{n+d} > S_d(n)  (CB1g)
            assert 16**d*green(n)[1] <= 1
        else:
            x = xs[n]
            theta = (16**d*x) % 1
            b = int(theta+delta >= 1)
            b_cb1 = int(Sm <= xs[n+d] < Sd)
            mism += (b != b_cb1)
        bits.append(b)
        J += b-delta
    J /= A
    return J, mism, ''.join(map(str, bits))


def carry_survey(xs, A, coherent=False):
    rows = []
    for k in (1, 2):
        m = 1
        while admissible(A, m+k):
            J, mism, bits = carry_epoch(xs, A, m, k, coherent)
            c = 16**(m+k)/(64*A*A)
            rows.append(dict(m=m, k=k, c=c, J=mstr(J), sqrtA_absJ=mstr(math.sqrt(A)*abs(float(J))),
                             cb1_mismatches=mism,
                             bits_sha256=sha256(bits.encode()).hexdigest()[:16]))
            m += 1
    return rows


# ---------------------------------------------------------------- controls
def pi16_enclosure(terms=20):
    lo = sum((forcing(n)/16**n for n in range(1, terms+1)), F())
    m = terms
    return lo, lo+F(1, 16**terms*(8*m+1)*(8*m+2))


def nearest_periodic(p):
    lo, hi = pi16_enclosure()
    den = 16**p-1
    kl, kh = int(den*lo+F(1, 2)), int(den*hi+F(1, 2))
    assert kl == kh
    return F(kl, den)


def periodic_closed_form(alpha, p):
    pts = [(16**j*alpha) % 1 for j in range(p)]
    assert (16**p*alpha) % 1 == pts[0]
    with local_prec():
        tot = iv.mpf(0)
        for a in pts:
            for b in pts:
                t = ivf((a-b) % 1)
                tot += -iv.log(iv.mpf(5)/4-iv.cos(2*iv.pi*t))/2
        tot /= p*p
        return math.nextafter(float(tot.a), -math.inf), math.nextafter(float(tot.b), math.inf), pts


def bernoulli_onesided(eps=F(1, 64)):
    """Exact: p0=1/16, digit1 +eps, digit15 -eps (stochastically smaller).

    Checks F(a)>=a at every two-digit terminating a, hence nonnegative shell
    discrepancy (15/16)(F(a)-a) (Lemma CB-OS), and |nu^(1)|>0.
    """
    p = [F(1, 16)]*16
    p[1] += eps
    p[15] -= eps
    S = [sum(p[:d], F()) for d in range(17)]
    worst = None
    for t1 in range(16):
        for t2 in range(16):
            a = F(t1, 16)+F(t2, 256)
            Fa = S[t1]+p[t1]*S[t2]
            g = Fa-a
            assert g >= 0
            worst = g if worst is None or g < worst else worst
    # |nu^(1)| = prod_i |phi_p(16^-i)|, phi_p(t)=sum_a p_a e(a t)
    prod = 1.0
    for i in range(1, 40):
        z = sum(float(p[a])*complex(math.cos(2*math.pi*a/16**i), math.sin(2*math.pi*a/16**i))
                for a in range(16))
        prod *= abs(z)
    return dict(eps=str(eps), min_F_minus_a_on_grid=str(worst),
                abs_nu_hat_1=mstr(prod), Q_half_lower=mstr(prod**2/2))


def main():
    with local_prec():
        return _main()


def _main():
    receipt = dict(front='A', H=H, interval_prec_bits=PREC, tail_bound=mstr(TAIL),
                   prereg_A=list(PREREG_A), carry_A=list(CARRY_A))
    xs = orbit()
    xs5 = orbit(seed=F(1, 5))
    xm = orbit(mutant=True)
    # rational seed 1/5: exact identities
    ok5 = all(xs5[n] == (xs[n]+F(1, 5)) % 1 for n in range(len(xs)))
    okh = all(((h*xs5[n]) % 1) == ((h*xs[n]+F(h, 5)) % 1)
              for n in range(1, len(xs), 7) for h in (1, 2, 3, 7, 16, 50))
    receipt['seed_1_5'] = dict(orbit_identity_all_n=ok5, phase_identity_sampled=okh, n_max=len(xs)-1)

    true_rows, mut_rows, coh_rows, five_rows, cal_rows = [], [], [], [], []
    for A in PREREG_A:
        rec, lo, hi = clausen_record(exact_phases(xs, A), 'true', A)
        true_rows.append(rec)
        E, P = pair_energies(xs, A)
        mid = (lo+hi)/2
        cal_rows.append(dict(A=A, E=mstr(E), P=mstr(P), E_plus_Q_minus_log2_over_A=mstr(E+mid-math.log(2)/A),
                             abs_P_minus_E=mstr(abs(P-E)), RC3_bound=mstr(4*math.pi/(30*A)),
                             P_plus_Q_minus_log2_over_A=mstr(P+mid-math.log(2)/A)))
        rec5, lo5, hi5 = clausen_record(exact_phases(xs5, A), 'seed_1/5', A)
        rec5['overlaps_true'] = (lo5 <= hi and lo <= hi5)
        five_rows.append(rec5)
        mut_rows.append(clausen_record(exact_phases(xm, A), 'mutant_4to3', A)[0])
        # coherent: x_n = 1 - T_n
        rc, clo, chi = clausen_record(shifted_phases(lambda n: F(0), A), 'coherent', A)
        Delta = float(max(green(n)[1] for n in range(A, 2*A))-min(green(n)[0] for n in range(A, 2*A)))
        rc['spread_Delta'] = mstr(Delta)
        rc['log2_minus_8pi2Delta2'] = mstr(math.log(2)-8*math.pi**2*Delta**2)
        rc['bound_holds'] = (clo <= math.log(2)+float(TAIL)) and (chi >= math.log(2)-8*math.pi**2*Delta**2-1e-15)
        coh_rows.append(rc)
    receipt['true_seed_clausen'] = true_rows
    receipt['seed_1_5_clausen'] = five_rows
    receipt['mutant_clausen'] = mut_rows
    receipt['coherent_clausen'] = coh_rows
    receipt['calibration'] = cal_rows

    per = []
    for label, alpha, p in [('alpha=1/15', F(1, 15), 1)]+[
            (f'nearest_p{p}', nearest_periodic(p), p) for p in (2, 3, 4)]:
        cf_lo, cf_hi, pts = periodic_closed_form(alpha, p)
        rows = []
        for A in PREREG_A:
            rec, lo, hi = clausen_record(shifted_phases(lambda n, a=alpha: (16**n*a) % 1, A), label, A)
            bound = 4*(p-1)*math.log(2)/A+4*math.pi*float(green(A)[1])
            rec['closed_form_dev_bound'] = mstr(bound)
            rec['bound_holds'] = (hi >= cf_lo-bound) and (lo <= cf_hi+bound)
            rows.append(rec)
        per.append(dict(label=label, alpha=str(alpha), p=p, Q_nu_lo=mstr(cf_lo), Q_nu_hi=mstr(cf_hi), rows=rows))
    receipt['periodic_completions'] = per

    carries = {}
    coh_carries = {}
    for A in CARRY_A:
        carries[str(A)] = carry_survey(xs, A)
        coh_carries[str(A)] = carry_survey(None, A, coherent=True)
    receipt['true_seed_carries'] = carries
    receipt['coherent_carries'] = coh_carries
    receipt['bernoulli_onesided'] = bernoulli_onesided()

    # preregistered verdicts
    v = {}
    v['seed_1_5_exact'] = ok5 and okh and all(r['overlaps_true'] for r in five_rows)
    v['coherent_band'] = all(r['bound_holds'] for r in coh_rows)
    v['periodic_band'] = all(r['bound_holds'] for P_ in per for r in P_['rows'])
    v['true_AQ_below_6'] = all(float(r['A_times_Q_hi']) <= 6 for r in true_rows)
    v['mutant_AQ_below_6'] = all(float(r['A_times_Q_hi']) <= 6 for r in mut_rows)
    v['calibration_RC4'] = all(abs(float(r['E_plus_Q_minus_log2_over_A'])) <= 1e-9 for r in cal_rows)
    v['calibration_RC3'] = all(float(r['abs_P_minus_E']) <= float(r['RC3_bound']) for r in cal_rows)
    v['cb1_zero_mismatch'] = all(r['cb1_mismatches'] == 0 for rows in carries.values() for r in rows)
    v['true_sqrtA_J_below_4'] = all(float(r['sqrtA_absJ']) <= 4 for rows in carries.values() for r in rows)
    receipt['verdicts'] = v
    text = json.dumps(receipt, indent=1, sort_keys=True)
    receipt_hash = sha256(text.encode()).hexdigest()
    (HERE/'FINITE_RECEIPT.json').write_text(text+'\n')
    print(json.dumps(v, indent=1))
    print('receipt sha256', receipt_hash)
    return receipt


if __name__ == '__main__':
    main()
