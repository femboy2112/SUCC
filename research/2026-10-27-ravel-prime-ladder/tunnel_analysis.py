"""The real tunnels: which conditions force normality WITHOUT reducing to W_N(h)->0?

The wall: prove (1/N) sum e(h 16^n pi) -> 0 for all h != 0  (Weyl).

Genuinely-different sufficient conditions (each must be verified to NOT be equivalent
to the wall, i.e. potentially easier, or at least a DIFFERENT attack surface):

TUNNEL 1 -- Positive entropy + x3 invariance (Rudolph-Johnson).
  If the orbit closure carries a x16-ergodic measure with positive x16-entropy AND
  x3-invariance, it's Lebesgue. The two hypotheses:
     (a) x3-invariance: D^(3)_{N,h}(pi) -> 0   [we showed this is NON-discriminating but
         still a real hypothesis; it's necessary]
     (b) positive entropy: h_top(closure) > 0, OR equivalently SOME block frequency
         deviation bound below the trivial.
  Is (b) provably easier than Weyl?  A SINGLE nonzero entropy suffices; Weyl needs ALL
  frequencies. So (b) is a ONE-BIT statement (is entropy 0 or >0?) vs Weyl's infinite
  family. This is the "tunnel": one bit of information instead of infinite.

TUNNEL 2 -- Finite-automaton / word-complexity lower bound.
  Normality in base 16 is equivalent to: every block w of length k has frequency 16^{-k}.
  A WEAKER sufficient condition: the base-16 expansion has positive topological entropy,
  i.e. the number of distinct length-k blocks grows like exp(c k), c>0. If c = ln 16,
  it's normal; if 0 < c < ln 16, NOT normal but STILL >0 entropy (not enough for R-J).
  So positive entropy alone (c>0) is NOT sufficient for normality -- need c = ln 16.

  This is the CRUX: Rudolph-Johnson needs x16/x3-invariance + positive entropy to get
  LEBESGUE (which forces FULL normality), so the entropy just needs to be POSITIVE, not
  maximal. That's the tunnel: positive entropy (one bit) + x3 invariance => full normality.

TUNNEL 3 -- Algebraic independence / transcendence.
  pi's normality is NOT known to follow from transcendence (many transcendental numbers
  are non-normal). But a DIFFERENT strong property could suffice. Is there a known
  "pi satisfies X => normal" theorem with X provable?  No such X is currently proved.

Let me TEST whether positive entropy is genuinely checkable/weaker for pi, i.e. measure
the empirical entropy (distinct-block growth) of pi's hex orbit, and see if even the
WEAKER "positive entropy" statement is plausible/attacked by known results.
"""
import math
import mpmath as mp
mp.mp.dps = 200
pi = mp.pi

def hex_digits(N):
    x = mp.frac(pi)
    ds = []
    for _ in range(N):
        d = mp.floor(16*x)
        ds.append(int(d))
        x = mp.frac(16*x)
    return ds

# empirical distinct-block count for length k over first N digits
def block_entropy(N, kmax):
    ds = hex_digits(N)
    for k in range(1, kmax+1):
        blocks = set()
        for i in range(N-k+1):
            blocks.add(tuple(ds[i:i+k]))
        count = len(blocks)
        # topological entropy rate estimate: (1/k) ln count
        rate = math.log(count)/k if count>0 else 0
        print(f"  N={N} k={k}: distinct {k}-blocks = {count},  rate=(ln count)/k = {rate:.5f}  (ln16={math.log(16):.5f})")

print("=== empirical block-entropy rate of pi's hex digits (positive-entropy check) ===")
block_entropy(20000, 6)

# If rate -> ln 16 for growing k (within finite precision), entropy is maximal = normal direction.
# The TUNNEL question is purely: is entropy POSITIVE (c > 0)?  Empirically obvious (distinct blocks
# grow), but that's just the known fact that pi's expansion isn't eventually periodic --
# which follows from pi irrational + not having repeating tail.  Positive entropy is NOT known
# to be provable in general for pi either (it's implied by, and close to, normality).
print()
print("KEY REALIZATION: positive entropy of the base-16 orbit is EXACTLY the statement that")
print("the orbit is not supported on finitely many blocks of any given length with a periodic")
print("tail -- i.e. that pi's expansion is not eventually periodic.  That IS provable (pi is")
print("irrational, even transcendental, so not eventually periodic).  But positive entropy from")
print("'not eventually periodic' is only c>0, NOT c=ln16, and Rudolph-Johnson with positive")
print("entropy + x2x3-invariance gives LEBESGUE which WOULD force c=ln16.")
print()
print("So the tunnel is: prove x3-invariance D^(3)->0 (the ONE remaining analytic input)")
print("AND positive entropy (which for pi follows from transcendence? NO -- need care).")
print("The x3-invariance is still the wall. Positive entropy is the easy part (irrationality).")
