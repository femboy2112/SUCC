"""Is the 1/N decay of D^(3) generic (all alpha) or pi-specific?

If generic: it's a UNIVERSAL fact (the x3 defect of ANY x16-orbit is O(1/N) at the level
of first-N empirical averages), hence still non-discriminating but REAL and RIGOROUS.
If pi-specific: could be a genuine signal.

Recall the earlier finding: D^(3) <= 2 trivially (O(1)). Now precision-safe shows 1/N.
This means the earlier "O(1)" was too crude; the TRUE statement is D^(3) = O(1/N)
UNIVERSALLY.  Why?  Because
  e(3h x) - e(h x) = e(h x)(e(2h x) - 1),
and the x16 orbit of ANY alpha has the property that the DIFFERENCE telescopes when
summed because 16 and 3... no, 3 is odd, 16 = 2^4, they don't relate.

Let me just MEASURE it for many alphas at fixed N and see if |D^(3)| ~ 1/N universally.
"""
import math
import mpmath as mp
mp.mp.dps = 80
pi = mp.pi
e = lambda x: mp.e**(2j*mp.pi*x)

def hex_orbit(alpha,N):
    x=mp.frac(alpha); out=[]
    for _ in range(N): out.append(x); x=mp.frac(16*x)
    return out
def Dorbit(alpha,N,h):
    xs=hex_orbit(alpha,N)
    return sum(e(3*h*x)-e(h*x) for x in xs)/N

alphas = {'pi':pi, 'sqrt2':mp.sqrt(2), 'sqrt3':mp.sqrt(3), 'e':mp.e,
          'phi':(1+mp.sqrt(5))/2, 'ln2':mp.log(2), '1/7':mp.mpf(1)/7,
          '0.101101110...':mp.mpf('0.10110111011110')}

print("=== is |D^(3)_{N,1}| ~ 1/N for ALL alpha?  (N*|D| should be constant) ===")
for name,a in alphas.items():
    vals = []
    for N in [1000, 4000, 16000]:
        vals.append(abs(Dorbit(a,N,1)))
    # N*|D| constancy
    c = [N*vals[i] for i,N in enumerate([1000,4000,16000])]
    print(f"  {name:10s}: N*|D^(3)| = {mp.nstr(c[0],6)}, {mp.nstr(c[1],6)}, {mp.nstr(c[2],6)}")

# If N*|D| is constant for ALL, it's universal O(1/N) -- a genuine RIGOROUS fact
# about x16 orbits: the x3-defect of the empirical measure decays like 1/N universally.
# This is because the map x->16x is EXPANDING and the defect is a "second-order"
# boundary term.  Let me try to PROVE the universal 1/N.

print("\n=== attempt: is D^(3) = (1/N) * [bounded boundary] universally? ===")
print("Consider S_N = sum_{n=0}^{N-1} [e(3h 16^n a) - e(h 16^n a)].")
print("This is the difference of two Weyl sums of the SAME x16 orbit at DIFFERENT points")
print("(3a and a) with related frequencies (3h and h).")
print("")
print("The clean fact: e(3h x) - e(h x) = e(h x)(e(2h x)-1).  Summing over x16-orbit")
print("does NOT telescope because 3 is not a power of 16.")
print("")
print("So the observed 1/N must be checked more carefully -- is it EXACTLY 1/N or is it")
print("1/N with slowly-growing coefficient?  Let me push to larger N with full precision.")
for name in ['pi','sqrt2']:
    a = alphas[name]
    print(f"  {name}:")
    for N in [10000, 40000, 160000, 640000]:
        d = abs(Dorbit(a,N,1))
        print(f"    N={N}: |D^(3)|={mp.nstr(d,8)}  N*|D|={mp.nstr(N*d,8)}")
