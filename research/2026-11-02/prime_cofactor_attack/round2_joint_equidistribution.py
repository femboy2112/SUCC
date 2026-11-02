#!/usr/bin/env python3
"""
Round 2 — JOINT equidistribution of (clock index, cofactor phase).

Question (handoff): is the cofactor phase e(h V_{p,n}) equidistributed on the unit
circle, INDEPENDENT of the clock index 16^{n-a_p} mod p, as n runs over the window
[a_p, (p+1)/2)?  I.e. is the joint pair (c_n, theta_n) equidistributed on (Z/p) x T?

Objects (p == 5 mod 8 prime, 5 < p <= X):
  a_p = (p+3)/8,  b_p = (p+1)/2 (exclusive),  window length L_p = (3p+1)/8
  U_n = 16 U_{n-1} + r(n),  U_0 = 0,  r(n) = 4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)
  V_{p,n} = U_n + 16^{n-a_p}/p   (c_p = -1; p-free denominator in the window)
  clock index   c_n = 16^{n-a_p} mod p          (in Z/p)
  cofactor phase theta_n = h * V_{p,n} mod 1    (on the unit circle)

Precision: theta_n is an exact rational phase.  Two INDEPENDENT methods cross-check:
  (M1) exact Fraction: k = (h*num) mod den, theta = k/den, e(theta)=exp(2pi i theta)
  (M2) digit-orbit:   U_n = 16^{n-1} pi - T_n (T_n tiny), so theta = h(16^{n-1} pi - T_n)
       computed from the base-16 digit orbit y_n = {16 y_{n-1}}, y_1 = {pi}, at
       mp.dps >= 0.6 * X.  T_n < (8n+1)^{-2} ~ tiny tail (J=30 terms suffices).

Tests:
  (T1) Marginal clock support:  |<16>| = ord_p(16) <= (p-1)/4 < p.  This is EXACT:
       the clock NEVER leaves the subgroup, so it is NOT equidistributed on Z/p.
  (T2) Marginal cofactor: mean of e(h V_{p,n}) over the window (should -> 0 if uniform).
  (T3) Joint cross-mean: E[ e(clock/p) * conj(e(cofactor)) ] vs the product of marginals
       E[e(clock/p)] * conj(E[e(cofactor)]).  Independence predicts equality.
  (T4) Conditional octant chi-square: bin cofactor phase into 8 octants conditioned on
       clock residue class (coarse: class = c_n mod 8), test uniformity (independence).

No normality claim.  Diagnostic only.
"""
import sys, math, json
sys.set_int_max_str_digits(300000)
from fractions import Fraction
from mpmath import mp, mpf, mpc, pi, cos, sin, exp, fmod

def r(n):
    return Fraction(4, 8*n-7) - Fraction(2, 8*n-4) - Fraction(1, 8*n-3) - Fraction(1, 8*n-2)

def compute_U(N):
    U = [Fraction(0)]*(N+1)
    s = Fraction(0)
    for i in range(1, N+1):
        s = 16*s + r(i)
        U[i] = s
    return U

def e_residue(h, num, den, dps):
    """M1: exact phase residue.  Returns complex e(theta)."""
    k = (h * num) % den
    th = mpf(2)*pi()*mpf(k)/mpf(den)
    return mpc(cos(th), sin(th))

def digit_orbit(X, h, dps):
    """M2: y_n = {16^{n-1} pi}; theta_n = h*(y_n - T_n); returns e(theta_n) array."""
    Nmax = (X+1)//2 - 1
    y = [mpf(0)]*(Nmax+1)
    y[1] = fmod(mp.pi, 1)
    for n in range(2, Nmax+1):
        y[n] = fmod(16*y[n-1], 1)
    T = [mpf(0)]*(Nmax+1)
    for n in range(1, Nmax+1):
        s = mpf(0); pw = mpf(16)
        for j in range(1, 31):
            s += mpf(r(n+j).numerator)/mpf(r(n+j).denominator) / pw
            pw *= 16
        T[n] = s
    eph = [None]*(Nmax+1)
    for n in range(1, Nmax+1):
        th = mpf(2)*pi()*mpf(h)*(y[n] - T[n])
        eph[n] = mpc(cos(th), sin(th))
    return eph

def sieve(n):
    is_p = [True]*(n+1); is_p[0]=is_p[1]=False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            for j in range(i*i, n+1, i): is_p[j]=False
    return [i for i in range(2, n+1) if is_p[i]]

def order(g, p):
    x = g % p; k = 1
    while x != 1:
        x = (x*g) % p; k += 1
    return k

def main():
    h = 1
    Xs = [256, 512, 1024]
    results = {}
    for X in Xs:
        Nmax = (X+1)//2 - 1
        dps = int(6*Nmax/math.log(10)) + 60
        mp.dps = dps
        U = compute_U(Nmax)
        ephM2 = digit_orbit(X, h, int(0.6*X) + 40)
        primes = [p for p in sieve(X) if p % 8 == 5 and p > 5]
        print(f"=== X={X}, Nmax={Nmax}, n_primes={len(primes)}, dps={dps} ===", flush=True)

        tot_w = 0
        S_clock = mpc(0); S_cofac = mpc(0); S_joint = mpc(0)
        # cross-method agreement at the largest n
        nchk = Nmax
        eM1 = e_residue(h, U[nchk].numerator, U[nchk].denominator, dps+20)
        eM2 = ephM2[nchk]
        agree = abs(eM1 - eM2)
        # marginal clock support: track distinct residues visited (union over primes)
        # conditional octant chi-square
        cond_bins = {}   # clock_class -> [counts in 8 octants]
        cov_acc = mpf(0); cov_n = 0

        for p in primes:
            ap = (p+3)//8; bp = (p+1)//2
            W = bp - ap
            tot_w += W
            zc = mpc(0); zf = mpc(0); zj = mpc(0)
            for n in range(ap, bp):
                ci = pow(16, n-ap, p)
                cph = e_residue(1, ci, p, dps)
                Vn = U[n] + Fraction(16**(n-ap), p)
                fph = e_residue(h, Vn.numerator, Vn.denominator, dps)
                zc += cph; zf += fph; zj += cph * fph.conjugate()
            S_clock += zc; S_cofac += zf; S_joint += zj
            # conditional octant (cofactor phase -> 8 octants) by clock class mod 8
            for n in range(ap, bp):
                ci = pow(16, n-ap, p)
                Vn = U[n] + Fraction(16**(n-ap), p)
                th = e_residue(h, Vn.numerator, Vn.denominator, dps)
                ang = mp.phase(th)  # in (-pi, pi]
                oct = int(math.floor((float(ang) + float(pi)) / (float(pi)/4))) % 8
                cls = ci % 8
                key = (p, cls)
                if key not in cond_bins:
                    cond_bins[key] = [0]*8
                cond_bins[key][oct] += 1
                cov_acc += th.real * (mpf(ci)/mpf(p) - mpf(1)/2)
                cov_n += 1

        mean_clock = S_clock / mpf(tot_w)
        mean_cofac = S_cofac / mpf(tot_w)
        mean_joint = S_joint / mpf(tot_w)
        pred_joint = mean_clock * mean_cofac.conjugate()
        delta = abs(mean_joint - pred_joint)

        # T4: chi-square over all (p,class) cells with >= 8 samples
        chi2 = mpf(0); dof = 0
        for key, cnts in cond_bins.items():
            tot = sum(cnts)
            if tot < 8: continue
            expc = tot/8.0
            for c in cnts:
                chi2 += (c - expc)**2 / expc
            dof += 7
        results[X] = {
            'n_primes': len(primes), 'tot_w': tot_w,
            'agree_m1_m2': float(agree),
            'mean_clock': [float(mean_clock.real), float(mean_clock.imag)],
            'mean_cofac': [float(mean_cofac.real), float(mean_cofac.imag)],
            'mean_joint': [float(mean_joint.real), float(mean_joint.imag)],
            'pred_joint': [float(pred_joint.real), float(pred_joint.imag)],
            'delta_joint': float(delta),
            'cov_stat': float(cov_acc/mpf(cov_n)),
            'chi2': float(chi2), 'dof': dof,
        }
        rr = results[X]
        print(f"  cross-method |e1-e2| at n={nchk}: {rr['agree_m1_m2']:.3e}", flush=True)
        print(f"  |mean_clock|={float(abs(mean_clock)):.5f}  |mean_cofac|={float(abs(mean_cofac)):.5f}", flush=True)
        print(f"  |mean_joint|={float(abs(mean_joint)):.5f}  |pred_joint|={float(abs(pred_joint)):.5f}", flush=True)
        print(f"  delta_joint={rr['delta_joint']:.6f}  cov_stat={rr['cov_stat']:.6f}", flush=True)
        print(f"  chi2={rr['chi2']:.1f} dof={rr['dof']}", flush=True)

    with open('research/2026-11-02/prime_cofactor_attack/round2_joint_results.json','w') as f:
        json.dump(results, f, indent=2)
    print("WROTE round2_joint_results.json")

if __name__ == '__main__':
    main()
