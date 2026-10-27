"""Prove the exact 3-adic structure theorem for the BBP source (analytically).

THEOREM candidate: The 3-adic valuation v_3(den U_n) and the 3-adic fractional part
frac_3(U_n) of the authentic zero-selected BBP states U_n satisfy an EXACT linear
recurrence modulo 3^k, giving a deterministic, log-growth 3-adic memory.

Let me derive the recurrence.  U_{n+1} = 16 U_n + r(n+1), U_0 = 0.

Modulo 3^k, with k = v_3(den U_n) + 1:
   16 = 1 + 15, and 15 = 3*5.  So 16 = 1 mod 3, 16 = 7 mod 9, 16 = 16 mod 27, etc.

The 3-adic dynamics: U_{n+1} = 16 U_n + r(n+1) mod 3^k.

Since 16 is a 3-adic unit (v_3(16)=0) and in fact 16 = 1 + 3*5, the map U -> 16U is
"close to identity" 3-adically (16 = 1 mod 3).  This means the 3-adic part of U_n
evolves SLOWLY (nearly the identity), accumulating the 3-adic content of r(n+1).

The exact statement I can prove:

PROPOSITION (exact 3-adic recurrence). For every k>=1, the residue of U_n mod 3^k is
determined by the finite window of source terms, and v_3(den U_n) = max over the source
pole valuations, growing like O(log n).  Concretely, v_3(den U_n) <= v_3(n) + O(1).

Proof sketch: den U_n divides (after reduction) the product of source denominators
(2j-1)(4j-1)(8j-7)(8j-3) for j=1..n.  Each factor 8j-7 = 8(j-1)+1, etc.  The 3-adic
valuation of 8j-7 is v_3(8j-7), and these are the only source of 3-factors.  Hence
v_3(den U_n) = max_{j<=n} [v_3(8j-7)+v_3(4j-1)+v_3(8j-3)] up to the specific cancellation,
and this maximum is O(log n) (it's v_3 of an arithmetic-type product).

Let me VERIFY the O(log n) growth and the exact log base by computing v_3(den U_n) for
large n, and confirm it's bounded by ~ 2 log_3 n.
"""
from fractions import Fraction
import sympy as sp

def r(n):
    n=Fraction(n)
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def Us(N):
    U=[Fraction(0)]
    for n in range(1,N+1): U.append(16*U[-1]+r(n))
    return U

N=200
U=Us(N)

print("=== v_3(den U_n) growth: is it O(log_3 n)? ===")
print(f"{'n':>6} {'v3':>4} {'log3(n)':>8} {'v3/log3':>8}")
for n in [5,10,20,40,80,120,160,200]:
    A=U[n].numerator; B=U[n].denominator
    v=0; b=B
    while b%3==0: b//=3; v+=1
    l3 = sp.log(n,3)
    print(f"{n:>6} {v:>4} {sp.N(l3,5):>8} {sp.N(v/l3,5):>8}")

# The exact relation: v_3(den U_n) should track the source pole valuations.
# Let me verify the precise formula: the 3-valuation of den U_n equals the max of
# v_3 contributions from the source, and confirm it's a deterministic log-growth.
print("\n=== exact source-pole formula for v_3(den U_n) ===")
for n in [7,8,13,14,22,40,80]:
    A=U[n].numerator; B=U[n].denominator
    v=0; b=B
    while b%3==0: b//=3; v+=1
    # max pole valuation at this n
    poles = [8*n-7, 4*n-1, 8*n-3]
    vp = max(sp.multiplicity(3,p) for p in poles)
    print(f"  n={n}: v3(den)={v}, max source pole v3={vp}")
