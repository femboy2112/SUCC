"""Build math toward x3-invariance of pi's orbit, exploiting the SUCC asset:
the SUMMABLE Green tail, which the generic x2x3 problem does NOT have.

The idea to test: is there a source-specific identity that makes D^(3)(pi) expressible
as something that cancels better than the raw orbit?

Key structural fact: U_{n+1} = 16^n pi - T_{n+1},  sum_n T_n < infinity  (Green tail summable).

The x3 defect of pi's orbit:
  D^(3)_{N,h}(pi) = (1/N) sum_n [ e(3h 16^n pi) - e(h 16^n pi) ].

Rewrite via the SOURCE:  e(h 16^n pi) = e(h U_{n+1}) * e(h T_{n+1}).
So:
  D^(3) = (1/N) sum_n [ e(3h U_{n+1}) e(3h T_{n+1}) - e(h U_{n+1}) e(h T_{n+1}) ].

Now the source recurrence U_{n+1} = 16 U_n + r(n+1) with RATIONAL r.  Crucially:
  e(3h U_{n+1}) = e(3h * 16 U_n) * e(3h r(n+1))
               = e(3h U_n)^{16} * e(3h r(n+1)).

This is a COCYCLE / multiplicative structure: the x3 defect can be re-expressed through
the recurrence, potentially giving a telescoping identity that the raw orbit lacks.

Let me look for the cleanest exact identity.  Define the phase increment:
  phi_n = h U_n (real),  so e(h U_{n+1}) = e(16 phi_n) e(h r(n+1)).

The x3 defect: e(3h U_{n+1}) - e(h U_{n+1}).

Actually, let me test a SPECIFIC sharp conjecture: does the SUMMABILITY of T_n give
  D^(3)_{N,h}(pi) - D^(3)_{N,h}(source) = o(1)
with the source version having an EXACT telescoping via the recurrence?

We already proved |D^(3)_source - D^(3)_orbit| = O(1/N) via summable tail. So they're
equivalent. The question is whether the SOURCE version telescopes.

Let me compute the source x3 defect and look for a closed telescoping structure:
  D^(3)_source = (1/N) sum_n [ e(3h U_{n+1}) - e(h U_{n+1}) ].
Using U_{n+1} = 16^n pi - T_{n+1}:
  = (1/N) sum_n [ e(3h 16^n pi) e(-3h T_{n+1}) - e(h 16^n pi) e(-h T_{n+1}) ].

The T_{n+1} factors are ~1 for large n (T -> 0). This does NOT telescope obviously.

CONCLUSION to test: there is NO free telescoping; the source transports.  But let me
verify ONE more genuinely-new angle: the SIGNED four-pole structure of r(n) itself.

r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2).

The FOUR poles with coefficients (4,-2,-1,-1) sum to 4-2-1-1 = 0.  This is a
"vanishing residue" / total-mass-zero structure.  Does it imply ANY cancellation in the
x3 defect?  Let me check the exact sum of the pole coefficients and whether the x3 defect
inherits a signed structure.

Actually the KEY question for the research program: what is the SMALLEST true theorem that
would be NEW and would ADVANCE x2x3?  Candidates:
  (a) An explicit quantitative bound on D^(3)_{N,h}(pi) in terms of the Green tail --
      i.e. a NONTRIVIAL bound better than the trivial O(1), valid for a SPECIFIC
      arithmetic class including pi.
  (b) A theorem that D^(3) for the SOURCE is bounded by something summable-in-n,
      which would be genuinely new if it exploits the signed poles.

Let me investigate (a): compute |D^(3)_{N,h}(pi)| vs 1/N and vs 1/sqrt(N) to see the
actual rate, and see if the signed source gives a better-than-trivial bound.
"""
import math
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 60
pi = mp.pi
e = lambda x: mp.e**(2j*mp.pi*x)

def r(n):
    n=Fraction(n)
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

# total mass of poles: 4-2-1-1 = 0
print("pole coefficients: 4 - 2 - 1 - 1 =", 4-2-1-1, "(total mass 0 -- vanishing residue)")

def Us(N):
    U=[Fraction(0)]
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U
def uf(U,n): return mp.mpf(U[n].numerator)/U[n].denominator

# rate of |D^(3)(pi)| vs N, using precision-safe digit shift
def hex_orbit(alpha,N):
    x=mp.frac(alpha); out=[]
    for _ in range(N): out.append(x); x=mp.frac(16*x)
    return out

def Dorbit(alpha,N,h):
    xs=hex_orbit(alpha,N)
    return sum(e(3*h*x)-e(h*x) for x in xs)/N

print("\n=== rate of |D^(3)_{N,1}(pi)| vs N (is it 1/N? 1/sqrt(N)?) ===")
prev=None
for N in [100, 300, 1000, 3000, 10000, 30000, 100000]:
    d = abs(Dorbit(pi,N,1))
    s = f"  N={N}: |D^(3)|={mp.nstr(d,6)}"
    if prev is not None:
        # estimate exponent p in |D| ~ N^{-p}
        p = -mp.log(d/prev)/mp.log(N/prev_N)
        s += f"   (exponent p~{mp.nstr(p,3)})"
    print(s)
    prev=d; prev_N=N

# Compare to the SOURCE x3 defect rate (does source decay faster?)
print("\n=== source x3 defect vs orbit x3 defect (does source give better rate?) ===")
Umax=Us(10000)
for N in [100,1000,10000]:
    ds = sum(e(3*uf(Umax,n+1))-e(uf(Umax,n+1)) for n in range(N))/N
    do = Dorbit(pi,N,1)
    print(f"  N={N}: |D_source|={mp.nstr(abs(ds),6)}  |D_orbit|={mp.nstr(abs(do),6)}")
