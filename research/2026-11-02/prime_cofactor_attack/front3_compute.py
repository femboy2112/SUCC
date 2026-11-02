#!/usr/bin/env python3
"""Front 3 — exact second-moment + hostile-control computation, correct precision.

Objects (p == 5 mod 8, prime, 5 < p <= X):
  a_p = (p+3)/8        (prime birth index)
  b_p = (p+1)/2 - 1    (window end)
  |W_p| = b_p - a_p + 1 = (3p+1)/8   (window length)
  R_p(h) = sum_{n=a_p}^{b_p} e(h U_n)   [exact identity: = sum e(-h 16^{n-a_p}/p) e(h V_{p,n})]
  U_n = 16 U_{n-1} + r(n), U_0=0, r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)

Precision: e(h U_n) has phase with denominator den(U_n) ~ exp(6n). We compute
  e(h U_n) = exp(2 pi i (h*num mod den)/den)   exactly as a residue (h*num mod den),
  then evaluate cos/sin via mpmath at dps >= 6*max_n/ln(10) + 40.
This is EXACT in the phase (integer residue), mpmath only supplies transcendental cos/sin.
Cross-check: a second independent method evaluates e(h U_n) = exp(2 pi i h * U_n) with
U_n as a high-precision mpf float (digit-orbit), at even higher dps.
"""
import sys, math, time, json
sys.set_int_max_str_digits(300000)
from fractions import Fraction
from mpmath import mp, mpf, mpc, pi, cos, sin, exp

def r(n):
    return Fraction(4, 8*n-7) - Fraction(2, 8*n-4) - Fraction(1, 8*n-3) - Fraction(1, 8*n-2)

def compute_U(N):
    U = [Fraction(0)]*(N+1)
    s = Fraction(0)
    for i in range(1, N+1):
        s = 16*s + r(i)
        U[i] = s
    return U

def e_exact_residue(h, Un, dps):
    """e(h*Un) = exp(2pi i * (h*num mod den)/den), exact phase residue."""
    mp.dps = dps
    num, den = Un.numerator, Un.denominator
    k = (h * num) % den
    theta = mpf(2)*pi()*mpf(k)/mpf(den)
    return mpc(cos(theta), sin(theta))

def e_float(h, Un, dps):
    """Independent method: U_n as high-precision float, e(2pi i h U_n)."""
    mp.dps = dps
    num, den = Un.numerator, Un.denominator
    uf = mpf(num)/mpf(den)
    theta = mpf(2)*pi()*mpf(h)*uf
    return exp(1j*theta) if False else mpc(cos(theta), sin(theta))

def sieve(n):
    is_p = [True]*(n+1); is_p[0]=is_p[1]=False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            for j in range(i*i, n+1, i): is_p[j]=False
    return [i for i in range(2, n+1) if is_p[i]]

def hostile_U(N, seed_kind, p=257):
    """Return U-like list for hostile controls (all EXACT Fractions).
    seed_kind:
      'coherent0'   : beta=0 => U_n = -T_n (the coherent counter-seed; T_n=positive tail)
                       Actually beta=0 means U_n(0) with sign flip: U_n = -T_n where T_n>0.
      'allzero'     : forcing r(n)=0 identically -> U_n = 0 (trivially coherent M/T=1)
      'haar'        : random seed — use pseudo-random rational phase U_n ~ independent uniform
      'clock257'    : p=257 period-4 clock (SPP-05 style): U_n = c_p * 16^n / p mod 1
    """
    if seed_kind == 'allzero':
        return [Fraction(0)]*(N+1)
    if seed_kind == 'coherent0':
        # beta=0 counter-seed s*=-pi/16: U_n = -T_n, T_n = sum_{j>=1} 16^{-j} r(n+j) > 0,
        # with 0 < T_n < (8n+1)^{-2}.  Exact truncated tail (J terms; tail < r/(15*16^J) negligible).
        out = [Fraction(0)]*(N+1)
        J = 80
        for n in range(1, N+1):
            s = Fraction(0)
            for j in range(1, J+1):
                s += r(n+j) * Fraction(1, 16**j)
            out[n] = -s
        return out
    if seed_kind == 'clock257':
        # p=257 clock: U_n = c*16^n/257 mod 1, c=4 (p≡1 mod8 birth residue) -> period ord_257(16)
        out = [Fraction(0)]*(N+1)
        c = 4
        for n in range(1, N+1):
            out[n] = Fraction((c * pow(16, n, 257)) % 257, 257)
        return out
    if seed_kind == 'haar':
        # genuinely random (deterministic PRNG) independent uniform phases
        import random
        random.seed(12345)
        out = [Fraction(0)]*(N+1)
        for n in range(1, N+1):
            # uniform rational phase with large denominator ~ random
            q = 2**40
            out[n] = Fraction(random.randrange(q), q)
        return out
    raise ValueError(seed_kind)

def second_moment(U, X, h, dps, kind):
    """Compute M = sum_p |R_p|^2 and T = sum_p |W_p|^2 for primes p==5 mod8, 5<p<=X."""
    primes = [p for p in sieve(X) if p % 8 == 5 and p > 5]
    M = mpf(0); T = mpf(0)
    # Precompute e(h U_n) for all needed n up to b_p max = (X+1)/2 - 1
    Nmax = (X + 1)//2 - 1
    eph = [None]*(Nmax+1)
    for n in range(1, Nmax+1):
        eph[n] = e_exact_residue(h, U[n], dps)
    for p in primes:
        ap = (p+3)//8
        bp = (p+1)//2 - 1
        W = bp - ap + 1
        T += mpf(W)**2
        # R_p = sum eph[ap..bp]
        R = mpc(0)
        for n in range(ap, bp+1):
            R += eph[n]
        M += abs(R)**2
    return M, T, len(primes)

def main():
    h = 1
    Xs = [256, 512, 1024]
    results = {}
    for X in Xs:
        Nmax = (X+1)//2 - 1
        dps = int(6*Nmax/math.log(10)) + 60
        mp.dps = dps
        print(f"=== X={X}, Nmax={Nmax}, dps={dps} ===", flush=True)
        U = compute_U(Nmax)
        # cross-check e() by two methods at one point
        chk_n = Nmax
        e1 = e_exact_residue(1, U[chk_n], dps+20)
        e2 = e_float(1, U[chk_n], dps+40)
        print(f"  cross-check e(U_{chk_n}): |e1-e2| = {abs(e1-e2)}", flush=True)
        results[X] = {}
        for kind in ['authentic', 'coherent0', 'allzero', 'clock257', 'haar']:
            if kind == 'authentic':
                Uu = U
            else:
                Uu = hostile_U(Nmax, kind)
            M, T, np_ = second_moment(Uu, X, h, dps, kind)
            ratio = M/T
            print(f"  {kind:12s}: M={float(M):.6e} T={float(T):.6e} M/T={float(ratio):.6f} (n_p={np_})", flush=True)
            results[X][kind] = {'M': float(M), 'T': float(T), 'MT': float(ratio), 'n_p': np_}
    with open('research/2026-11-02/prime_cofactor_attack/front3_results.json','w') as f:
        json.dump(results, f, indent=2)
    print("WROTE front3_results.json")

if __name__ == '__main__':
    main()
