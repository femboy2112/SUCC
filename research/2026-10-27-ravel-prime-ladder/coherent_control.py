"""RIGOROUS PROOF of the universal 1/N theorem for the x3 transversal defect.

THEOREM (universal x3-defect bound). For every real alpha and every nonzero integer h,
   D^{(3)}_{N,h}(alpha) := (1/N) sum_{n=0}^{N-1} [ e(3h 16^n alpha) - e(h 16^n alpha) ]
   satisfies  |D^{(3)}_{N,h}(alpha)| <= 2/N  ... wait, that's trivial (each term <= 2).

The NONTRIVIAL claim is |D^{(3)}| ~ C/N (not just <= 2). Let me find the EXACT reason.

Actually here is the clean PROOF of why S_N = sum [e(3h 16^n a) - e(h 16^n a)] is BOUNDED:

Use the factorization  e(3x) - e(x) = e(x)(e(2x)-1) = 2i e(2x) sin(2 pi x).

So the n-th term = 2i e(2h 16^n a) sin(2 pi h 16^n a).

Now, 16^n = 2^{4n}.  The sequence 16^n a mod 1 is the x16-orbit.

Hmm, this factorization doesn't immediately give boundedness.

The ACTUAL reason S_N is bounded is a DEEP fact: it's NOT universally bounded for all alpha
-- it's bounded because the difference of two Weyl sums of the SAME orbit at related
frequencies has cancellation. But "bounded for all alpha" is FALSE: for a NON-normal alpha
(e.g. alpha whose orbit is supported near 0), the Weyl sums W_N(h) ~ 1 (not 0), and then
D^(3) = W_N(3h) - W_N(h) ~ (1 - 1) = 0 also.  For a normal alpha, W_N -> 0, so D^(3) -> 0 too.

Wait, so D^(3) -> 0 in BOTH cases (normal AND coherent)!  That's the point: the defect
is ALWAYS ~0, because:
  - normal alpha: both W_N(3h) and W_N(h) -> 0, so difference -> 0.
  - coherent alpha (orbit -> single point c): W_N(k) -> e(kc) for all k, so
    W_N(3h)-W_N(h) -> e(3hc)-e(hc), which is NOT 0 in general (e.g. c=1/4, h=1: e(3/4)-e(1/4) = nonzero).

So D^(3) -> 0 is NOT universal; it's 0 for normal alpha but can be nonzero for coherent alpha.
The observed 1/N decay for pi, sqrt2, e, phi, ln2 (all the "nice" irrationals) reflects that
THESE particular alphas have D^(3) -> 0 (consistent with them being normal OR with a weaker
property).  1/7 is RATIONAL so its orbit is periodic and D^(3) is a finite-period average that
happens to give a specific constant.

So the universal 1/N law I "found" is actually: for alphas whose x16-orbit is equidistributed
(normal-ish), D^(3) ~ 1/N with the constant determined by the first few digits. This is the
RIGHT statement, and it's NOT universal -- it requires the orbit to be equidistributed.

THE CRUX REFINED: D^(3) -> 0 is EQUIVALENT to (a weak form of) equidistribution, NOT a free
fact.  And proving D^(3)(pi) -> 0 IS the x2x3 wall, because for pi we don't know the orbit
is equidistributed.

Let me verify this refined picture: compute D^(3) for a COHERENT (non-equidistributed) alpha
and confirm it does NOT go to 0.
"""
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
e = lambda x: mp.e**(2j*mp.pi*x)

def S_complex(alpha,N,h):
    x=mp.frac(alpha); s=mp.mpc(0)
    for _ in range(N):
        s += e(3*h*x)-e(h*x); x=mp.frac(16*x)
    return s

# coherent alpha: alpha = tiny, orbit stays near 0 (e.g. alpha = 1/16^k * small)
# alpha = 2^{-100}: x16 orbit -> {2^{-100}, 2^{-96}, ...} heads toward 0 then cycles near 0.
print("=== D^(3) for COHERENT (non-equidistributed) alpha -- should NOT go to 0 ===")
for alpha_name, alpha in [('2^-40 (coherent)', mp.power(2,-40)),
                          ('tiny rational 1/3 (periodic)', mp.mpf(1)/3),
                          ('1/5 (periodic)', mp.mpf(1)/5)]:
    print(f"  {alpha_name}:")
    for N in [1000, 10000, 100000]:
        d = S_complex(alpha,N,1)/N
        print(f"    N={N}: D^(3) = {mp.nstr(d,6)}  |D|={mp.nstr(abs(d),6)}")

print("\nIf coherent alpha gives NONZERO D^(3) that persists, then D^(3)->0 is genuinely")
print("equivalent to equidistribution (the x2x3 wall), NOT a free fact.")
