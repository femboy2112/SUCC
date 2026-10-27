"""Characterize the 3-adic memory structure of the authentic BBP source EXACTLY.

Observation: frac_3(U_n) takes structured values (1/3, 1/9, 4/9, 7/9, 5/9, 6/9, 4/27, 10/27...).

Hypothesis: the 3-adic valuation v_3(den U_n) grows slowly (deterministically), and the
3-adic fractional part frac_3(U_n) is determined by U_n mod 3^{v_3(den)}.

Let me extract the EXACT pattern: v_3(den U_n) and frac_3(U_n) for many n, and find the law.

Key: U_{n+1} = 16 U_n + r(n+1).  mod 3^k, this is a linear recurrence.  Since 16 = 1 mod 3,
and 16 = 7 mod 9, etc., the 3-adic dynamics of U_n has a specific structure.

Actually the CRUCIAL fact: the source r(n) has denominators (2n-1)(4n-1)(8n-7)(8n-3).
The 3-adic valuation of these denominators is v_3(2n-1)+v_3(4n-1)+v_3(8n-7)+v_3(8n-3).
This determines v_3(den U_n).

Let me compute v_3(den U_n) and frac_3(U_n) exactly and find the pattern.
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

def frac_3(A, B):
    v = 0; b = B
    while b % 3 == 0:
        b //= 3; v += 1
    if v == 0: return Fraction(0)
    b_inv = pow(b, -1, 3**v)
    num = (A * b_inv) % (3**v)
    return Fraction(num, 3**v)

U = Us(40)
print("=== v_3(den U_n) and frac_3(U_n), exact ===")
print(f"{'n':>3} {'v3(den)':>7} {'frac_3(U_n)':>12}")
for n in range(1, 25):
    A = U[n].numerator; B = U[n].denominator
    v = 0; b = B
    while b % 3 == 0: b//=3; v+=1
    f3 = frac_3(A, B)
    print(f"{n:>3} {v:>7} {str(f3):>12}")

# Find the law for v_3(den U_n): den includes factors 8n-7, 8n-3, 4n-1, 2n-1.
# v_3 of the LCM of these.  Let's compute v_3(den U_n) directly vs the source poles.
print("\n=== v_3(den U_n) vs v_3 of source poles ===")
for n in [1,2,4,5,7,8,10,13,14,16,22]:
    A=U[n].numerator; B=U[n].denominator
    v=0; b=B
    while b%3==0: b//=3; v+=1
    # source pole 3-valuations
    poles = [8*n-7, 8*n-4, 8*n-3, 8*n-2]
    vpoles = [sp.multiplicity(3,p) for p in poles]
    print(f"  n={n}: v3(den U_n)={v}, pole valuations={vpoles}")
