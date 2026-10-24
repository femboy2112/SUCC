#!/usr/bin/env python3
"""Calibration record for the CYC-01 instrument.  Every check prints PASS/FAIL and the numbers."""
import sys, random, itertools, time
from fractions import Fraction
import numpy as np, mpmath as mp
sys.path.insert(0, '/tmp/claude-1000/-home-leah-SUCC/49d503dc-b72f-43d0-b0e2-39f6cb53160e/scratchpad')
from cyc01_instrument import *
import cyc01_xcheck as XB

NFAIL = 0
def check(name, ok, detail=''):
    global NFAIL
    if not ok: NFAIL += 1
    print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + detail if detail else ''))

Ns = [16, 64, 256, 1024, 4096]
HS = [1, 2, 3, 5, 7, -1, -3]
RS = [2, 3, 4, 5, 8]
print('versions: python', sys.version.split()[0], 'mpmath', mp.__version__, 'sympy', __import__('sympy').__version__,
      'numpy', np.__version__, '; long double nmant =', np.finfo(LD).nmant, '; mp.dps (rational path) =', mp.mp.dps)

# ------------------------------------------------------------------ C0: d_n recursion vs brute-force enumeration of all prime-step chains
print('\n== C0: d_n memoised recursion vs brute-force (all orderings of the prime multiset) ==')
def brute_d(n, c):
    fac = factorint(n); mult = []
    for p, e in fac.items(): mult += [p] * e
    best = None
    for perm in set(itertools.permutations(mult)):
        cur, cost = n, 0.0
        for p in perm:
            nxt = cur // p; cost += abs(c[cur] - c[nxt]); cur = nxt
        best = cost if best is None else min(best, cost)
    return best
rnd = random.Random(1)
worst = 0.0; ntest = 0
for n in [6, 12, 30, 36, 60, 72, 210, 360, 1000, 2310, 5040, 96, 7 * 255, 3 * 5 * 17 * 257]:
    divl = divisors(n)
    for trial in range(5):
        c = {m: rnd.uniform(-1, 1) for m in divl}
        C = {m: [LD(c[m])] for m in divl}
        D = compute_D(C, divl)
        w = abs(float(D[n][0]) - brute_d(n, c)); worst = max(worst, w); ntest += 1
check('C0 d_n == brute force on %d random tables (14 n values, <=5 prime-multiset size 8)' % ntest, worst < 1e-14, 'max|diff|=%.3e' % worst)
# hand-checkable case: c1=1,c2=0.5,c3=0.25,c6=0 -> d2=.5, d3=.75, d6=min(.5+.5? ...)
C = {1: [LD(1)], 2: [LD('0.5')], 3: [LD('0.25')], 6: [LD(0)]}
D = compute_D(C, [1, 2, 3, 6])
# d6 = min( d3+|c6-c3| = .75+.25 = 1.0 , d2+|c6-c2| = .5+.5 = 1.0 ) = 1.0 ; d2=0.5 ; d3=0.75
check('C0 hand case d2=0.5,d3=0.75,d6=1.0', [float(D[2][0]), float(D[3][0]), float(D[6][0])] == [0.5, 0.75, 1.0], str([float(D[k][0]) for k in (2, 3, 6)]))
C = {1: [LD(1)], 2: [LD('0.5')], 3: [LD('0.9')], 6: [LD('0.8')]}
D = compute_D(C, [1, 2, 3, 6])   # d2=.5, d3=.1, d6=min(.1+.1=.2, .5+.3=.8)=.2
check('C0 hand case 2: d6=0.2 (min picks p=2 branch)', abs(float(D[6][0]) - 0.2) < 1e-18, str(float(D[6][0])))

# ------------------------------------------------------------------ C1: x = 0
print('\n== C1: x = 0 (A=1 for all h,N; c_n=1; eta=2; d=0) ==')
nb = 4 * max(Ns) + 256
zbits = np.zeros(nb, dtype=np.uint8)
allok = True; worstA = 0; worstR = 0; mingap = None
for b, s in ((2, 1), (16, 4)):
    for srcname, src in (('BitSource', BitSource(zbits, s, Ns, 'x=0')), ('RatSource', RatSource(0, 1, b, Ns, 'x=0'))):
        for r in evaluate(src, b, HS, RS):
            N, R = r['N'], r['R']
            closed = mp.mpf(R - 1) / N + mp.sqrt(1 + mp.mpf(2 * (R - 1) * (R - 2)) / (3 * R * N))     # hand-derived closed form
            worstA = max(worstA, abs(mp.mpf(str(r['absA'])) - 1))
            worstR = max(worstR, abs(mp.mpf(str(r['RHS'])) - closed))
            g = mp.mpf(str(r['GAP']))
            if r['GAP'] < 0: allok = False
            if mingap is None or g < mingap[0]: mingap = (g, srcname, b, r['h'], R, N)
check('C1 |A|=1 (max dev %s), RHS == closed form (max dev %s), GAP>=0 in all 2 bases x 2 paths x 7 h x 5 R x 5 N = 700 cells'
      % (mp.nstr(worstA, 5), mp.nstr(worstR, 5)), allok and worstA < 1e-17 and worstR < 1e-17)
print('       smallest GAP among x=0 cells:', mp.nstr(mingap[0], 12), mingap[1:], ' (closed form (R-1)/N + (R-1)(R-2)*... -> 1/N at R=2: 1/4096 = %s)' % mp.nstr(mp.mpf(1) / 4096, 12))

# ------------------------------------------------------------------ C2: x = 1/2
print('\n== C2: x = 1/2 (orbit 1/2,0,0,...): A = ((-1)^h + N-1)/N exactly ==')
ok = True; worst = 0
for b, s in ((2, 1), (16, 4)):
    hb = np.zeros(nb, dtype=np.uint8); hb[0] = 1                  # 0.1000... binary = 1/2
    for srcname, src in (('BitSource', BitSource(hb, s, Ns, 'x=1/2')), ('RatSource', RatSource(1, 2, b, Ns, 'x=1/2'))):
        for h in HS:
            Ah = src.A(h)
            for i, N in enumerate(Ns):
                exact = Fraction((-1) ** abs(h) + N - 1, N)
                got = abs(mp.mpf(str(Ah[i][0])) + 0)       # real part
                dev = abs(mp.mpf(str(Ah[i][0])) - mp.mpf(exact.numerator) / exact.denominator) + abs(mp.mpf(str(Ah[i][1])))
                worst = max(worst, dev)
        # c_n closed form for several n
        for n in (1, 2, 3, 6, 15, 255, 4095):
            cn = src.c(n)
            for i, N in enumerate(Ns):
                ex = Fraction((-1) ** n + N - 1, N)
                worst = max(worst, abs(mp.mpf(str(cn[i])) - mp.mpf(ex.numerator) / ex.denominator))
check('C2 A and c_n match exact Fractions (4 paths); max dev %s' % mp.nstr(worst, 5), worst < 1e-17)
# bound check
src = RatSource(1, 2, 2, Ns, 'x=1/2'); rows = evaluate(src, 2, HS, RS)
print('       min GAP at x=1/2,b=2 :', mp.nstr(min(r['GAP'] for r in rows), 15), '(all >= 0:', all(r['GAP'] >= 0 for r in rows), ')')
src = RatSource(1, 2, 16, Ns, 'x=1/2'); rows = evaluate(src, 16, HS, RS)
print('       min GAP at x=1/2,b=16:', mp.nstr(min(r['GAP'] for r in rows), 15), '(all >= 0:', all(r['GAP'] >= 0 for r in rows), ')')

# ------------------------------------------------------------------ C3: rational periodic orbits
print('\n== C3: rational x with periodic orbit: instrument vs exact/direct ==')
def direct_exact_A(p, q, b, h, N):
    """independent: iterate Fractions, mpmath exp at dps 60."""
    with mp.workdps(60):
        x = Fraction(p, q); acc = mp.mpc(0)
        for j in range(N):
            acc += mp.expjpi(2 * mp.mpf(h * x.numerator) / x.denominator)
            x = (x * b) - int(x * b)
        return acc / N
def naive_hi_dps_A(p, q, b, h, N):
    """independent: x as mpf at dps large enough that b^j x keeps >=40 fractional digits (the 'brute' reduce)."""
    dps = int(N * np.log10(b)) + 60
    with mp.workdps(dps):
        x = mp.mpf(p) / q; acc = mp.mpc(0)
        for j in range(N):
            v = mp.mpf(h) * mp.mpf(b) ** j * x
            acc += mp.expjpi(2 * mp.frac(v))
        return mp.mpc(acc / N)
worst1 = worst2 = 0
for (p, q, b) in [(1, 3, 16), (1, 9, 16), (1, 9, 2), (1, 7, 2), (1, 15, 16), (1, 17, 16), (1, 6, 2), (5, 12, 16)]:
    for h in (1, 2, 3, -1, -3, 5, 7):
        for N in (16, 64, 256):
            src = RatSource(p, q, b, [N], 'q'); a = src.A(h)[0]
            got = mp.mpc(a[0], a[1])
            e1 = abs(got - direct_exact_A(p, q, b, h, N)); worst1 = max(worst1, e1)
            if N <= 64:
                e2 = abs(got - naive_hi_dps_A(p, q, b, h, N)); worst2 = max(worst2, e2)
check('C3a RatSource A == direct Fraction-orbit mp.expjpi (8 sources x 7 h x 3 N=168 cells), max |dev|=%s' % mp.nstr(worst1, 5), worst1 < mp.mpf(10) ** -45)
check('C3b RatSource A == brute-force mpf at dps=N*log10(b)+60 (112 cells), max |dev|=%s' % mp.nstr(worst2, 5), worst2 < mp.mpf(10) ** -40)
# known exact values
for h in (1, 2, 4, 5):
    src = RatSource(1, 3, 16, [16, 64, 4096], 'x=1/3'); a = src.A(h)
    z = mp.expjpi(2 * mp.mpf(h) / 3)
    d = max(abs(mp.mpc(*a[i]) - z) for i in range(3))
    check('C3c x=1/3,b=16 (fixed point): A_{%d,N}=exp(2 pi i %d/3) exactly for all N, dev %s' % (h, h, mp.nstr(d, 4)), d < mp.mpf(10) ** -45)
src = RatSource(1, 9, 16, [3, 6, 48, 4095, 4096, 4097, 3 * 1000], 'x=1/9')
a = src.A(1)
vals = [abs(mp.mpc(*t)) for t in a]
# h=1: zeta9 (1 + zeta3 + zeta3^2) = 0 per period => A=0 at N=3m ; N=3m+1 -> 1/N ; N=3m+2 -> |zeta9^1+zeta9^7|/N
check('C3d x=1/9,b=16,h=1: |A|=0 at N=3,6,48,3000 and 4095 (hand: zeta9+zeta9^7+zeta9^4=0)', all(vals[i] < mp.mpf(10) ** -45 for i in (0, 1, 2, 3, 6)),
      'values: ' + ', '.join(mp.nstr(v, 3) for v in vals))
check('C3e x=1/9,b=16,h=1: |A_4096| = 1/4096 and |A_4097|=|zeta9^1+zeta9^7|/4097 (hand)',
      abs(vals[4] - mp.mpf(1) / 4096) < mp.mpf(10) ** -45 and abs(vals[5] - abs(mp.expjpi(mp.mpf(2) / 9) + mp.expjpi(mp.mpf(14) / 9)) / 4097) < mp.mpf(10) ** -45,
      '%s %s' % (mp.nstr(vals[4], 15), mp.nstr(vals[5], 15)))

# ------------------------------------------------------------------ C3f: BitSource (numpy path) vs RatSource on rational expansions
print('\n== C3f: BitSource (the sweep path) on the binary expansion of a rational vs exact RatSource ==')
nbits = 4 * 4096 + 256
worstA = worstRHS = worstGAP = 0; ncell = 0
for (p, q) in [(1, 3), (1, 9), (1, 7), (1, 5), (1, 17), (1, 6), (5, 12), (1, 255), (2, 13), (1, 101), (7, 257), (1, 65537)]:
    M = (p << nbits) // q                             # floor(p 2^nbits / q): truncation error 2^-nbits (rational with eventually-zero orbit beyond, irrelevant: window within range)
    bits = bits_from_int(M, nbits)
    for b, s in ((2, 1), (16, 4)):
        bs = BitSource(bits, s, Ns, 'bits'); rs = RatSource(p, q, b, Ns, 'rat')
        r1 = evaluate(bs, b, [1, 2, 3, 5, 7, -3], [2, 3, 4, 8]); r2 = evaluate(rs, b, [1, 2, 3, 5, 7, -3], [2, 3, 4, 8])
        for u, v in zip(r1, r2):
            assert (u['h'], u['R'], u['N']) == (v['h'], v['R'], v['N'])
            worstA = max(worstA, abs(mp.mpf(str(u['absA'])) - v['absA']))
            worstRHS = max(worstRHS, abs(mp.mpf(str(u['RHS'])) - v['RHS']))
            worstGAP = max(worstGAP, abs(mp.mpf(str(u['GAP'])) - v['GAP'])); ncell += 1
check('C3f BitSource == RatSource on %d cells: max|dA|=%s max|dRHS|=%s max|dGAP|=%s' % (ncell, mp.nstr(worstA, 4), mp.nstr(worstRHS, 4), mp.nstr(worstGAP, 4)),
      max(worstA, worstRHS, worstGAP) < 2e-17)

# ------------------------------------------------------------------ C4: floats lie
print('\n== C4: naive float64 phase  h*b^j*x  (the trap) vs exact, x=1/9, b=2, N=64, h=1 ==')
b, N, h = 2, 64, 1
naive = sum(np.exp(2j * np.pi * (h * (float(b) ** j) * (1 / 9)))  for j in range(N)) / N
exact = direct_exact_A(1, 9, 2, 1, N)
print('       naive float64 A = %r ; exact A = %s ; |dev| = %.3e  (exact |A|=%s)' % (naive, mp.nstr(exact, 17), abs(complex(exact) - naive), mp.nstr(abs(exact), 8)))

# ------------------------------------------------------------------ C5: pi hex digits + instrument vs independent B on pi
print('\n== C5: pi in base 16 ==')
nbp = 4 * 4096 + 512
pb, Mpi = pi_bits(nbp)
hexs = format(Mpi, '0%dx' % (nbp // 4))
known = '243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89452821e638d01377be5466cf34e90c6cc0ac29b7c97c50dd3f84d5b5b54709179216d5d98979fb1b'
check('C5a first %d hex digits of frac(pi) equal the (Blowfish P-array/S-box) published digits' % len(known), hexs[:len(known)] == known, hexs[:40])
with mp.workdps(60):
    pass
# Instrument A on pi vs Instrument B (independent) -- cells N<=1024
srcA = BitSource(pb, 4, [16, 64, 256, 1024], 'pi'); rowsA = evaluate(srcA, 16, [1, 3, -3, 7], [2, 3, 5])
t0 = time.time()
worst = {k: 0 for k in ('absA', 'RHS', 'GAP', 'S')}
for h in (1, 3, -3, 7):
    Bres = XB.cell_B(Mpi, nbp, 4, 16, h, [2, 3, 5], [16, 64, 256, 1024], 50)
    for r in rowsA:
        if r['h'] != h or r['R'] not in (2, 3, 5): continue
        v = Bres[(r['R'], r['N'])]
        for k in worst: worst[k] = max(worst[k], abs(mp.mpf(str(r[k])) - v[k]))
check('C5b Instrument A vs B (mpmath dps50, exact big-int remainders) on x=pi base 16: 48 cells; max dev ' + ', '.join('%s=%s' % (k, mp.nstr(v, 3)) for k, v in worst.items()),
      max(worst.values()) < 3e-17, '(B time %.0fs)' % (time.time() - t0))

# ------------------------------------------------------------------ C6: random x : A vs B at two precisions
print('\n== C6: random x (seed %d, k=0..3), Instrument A vs B(dps 40) vs B(dps 80) ==' % SEED)
worstAB = {k: 0 for k in ('absA', 'RHS', 'GAP')}; worstBB = 0; n6 = 0
for k in range(4):
    bits = random_bits(k, nbp); M = int(bytes(bits + 48), 2)
    for b, s in ((2, 1), (16, 4)):
        Nsub = [16, 64, 256] if b == 16 else [16, 64, 256, 1024]
        if s * (max(Nsub) - 1) + 128 > nbp: continue
        src = BitSource(bits, s, Nsub, 'rnd'); h = [1, 5, -3, 2][k]
        rowsA = evaluate(src, b, [h], [2, 4])
        B40 = XB.cell_B(M, nbp, s, b, h, [2, 4], Nsub, 40); B80 = XB.cell_B(M, nbp, s, b, h, [2, 4], Nsub, 80)
        for r in rowsA:
            v = B40[(r['R'], r['N'])]; w = B80[(r['R'], r['N'])]; n6 += 1
            for kk in worstAB: worstAB[kk] = max(worstAB[kk], abs(mp.mpf(str(r[kk])) - w[kk]))
            worstBB = max(worstBB, abs(v['GAP'] - w['GAP']), abs(v['RHS'] - w['RHS']))
check('C6 A vs B(dps80) on %d random cells: ' % n6 + ', '.join('%s=%s' % (k, mp.nstr(v, 3)) for k, v in worstAB.items()) + '; B(40) vs B(80) max dev = %s' % mp.nstr(worstBB, 3),
      max(worstAB.values()) < 3e-17 and worstBB < mp.mpf(10) ** -30)

print('\nTOTAL FAILURES:', NFAIL)
sys.exit(1 if NFAIL else 0)
