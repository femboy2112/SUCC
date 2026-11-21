"""Independent cross-implementation audit: no import from parity_dual module.
Uses direct forward parity iteration, a backward inverse-branch reconstruction,
SymPy exact symbolic factorization and independently derived BBP rational sums.
This is an implementation witness, not an independent mathematical proof.
"""
from fractions import Fraction
from pathlib import Path
import json
import math
import sympy as sp

checks=0

def ck(x, why):
    global checks
    checks+=1
    if not x: raise AssertionError(why)


def C(x): return x//2 if x%2==0 else (3*x+1)//2

def direct_parities(x,n):
    bits=[]
    for _ in range(n):
        bits.append(x%2)
        x=C(x)
    return sum(b<<i for i,b in enumerate(bits))

def reconstruct_reversed(y,n):
    M=1<<n
    z=0
    for i in range(n-1,-1,-1):
        z=(2*z if ((y>>i)&1)==0 else (2*z-1)*pow(3,-1,M))%M
    return z

# Exact finite homeomorphism at increasingly deep moduli.
for n in (1,2,3,4,6,8,10,12):
    seen=set()
    for x in range(1<<n):
        y=direct_parities(x,n)
        seen.add(y)
        ck(reconstruct_reversed(y,n)==x,('inverse',n,x))
    ck(len(seen)==(1<<n),('permutation',n))

# Mirror is source-coordinate versus parity-coordinate; test the transported map.
n=12; M=1<<n
for x in range(512):
    y=direct_parities(x,n)
    omega=reconstruct_reversed((M-1)^y,n)
    ck(direct_parities(omega,n)==(M-1)^y,('omega-parity',x))
    ck(reconstruct_reversed((M-1)^direct_parities(omega,n),n)==x,('omega-2',x))
    ck(C(omega)%(M//2)==reconstruct_reversed(((M-1)^direct_parities(C(x),n-1))%(M//2),n-1),('omega-C',x))

# Original four-pole mask exact factorization and root chart connections.
t=sp.symbols('t')
H=sp.expand((t*t+2)*(t*t+2*t+2))
Q=sp.expand((1-t)*H)
ck(Q==4-2*t**3-t**4-t**5,'four-pole Q')
ck(sp.rem(t**8-16,H,t)==0,'eighth root source filter')
ck(sp.expand(sp.factor(Q)-(1-t)*(t*t+2)*(t*t+2*t+2))==0,'source factors')
# 1/4 & 3/4 normalized positions correspond to odd residues 1,3 under 2-bit coding.
for x in range(-400,401):
    ck(direct_parities(x,2)==x%4,('mod4',x))

# The original source independently certifies the twelve hexadecimal digits.
def source(j):
    return Fraction(4,8*j-7)-Fraction(2,8*j-4)-Fraction(1,8*j-3)-Fraction(1,8*j-2)
P=sum((source(j)/16**j for j in range(1,13)),Fraction())
U=P+source(13)/(15*16**12)
lo=(16**12*P).__floor__();hi=(16**12*U).__floor__()
ck(lo==hi,'π prefix interval')
word=format(lo,'012X')
ck(word=='3243F6A8885A','π digits')
y=sum(int(c,16)<<(4*j) for j,c in enumerate(word))
a=reconstruct_reversed(y,48)
ck(y==0xA5888A6F3423,'π parity journal')
ck(a==0x138D4B466283,'π 2adic source residue')
ck(direct_parities(a,48)==y,'π48 parity replay')
# Mutant is a different BBP source; the coding theorem still holds, hence not a normality certificate.
mutant_source=lambda j:source(j)+Fraction(2,(8*j-7)*(8*j-6)*(8*j-5))
Pm=sum((mutant_source(j)/16**j for j in range(1,13)),Fraction())
Um=Pm+mutant_source(13)/(15*16**12)
ck((Pm*16**12).__floor__()==(Um*16**12).__floor__(),'mutant bounded at M=12')
ck((Pm*16**12).__floor__()!=lo,'mutant source different')

output={'status':'passed','checks':checks,'finite_moduli':[1,2,3,4,6,8,10,12],
        'bbp_prefix':word,'bbp_collatz_parity_address':f'0x{y:012X}',
        'bbp_collatz_source_residue':f'0x{a:012X}',
        'authority':'independently coded finite exact and symbolic checks; NOT pi normality or Collatz proof'}
outpath=Path(__file__).with_name('independent_audit_receipt.json')
outpath.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
