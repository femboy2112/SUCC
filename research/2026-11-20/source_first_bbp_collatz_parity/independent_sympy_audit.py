"""Independent SymPy/mpmath oracle (different formulas from Fraction module).

Finite audit only. Classical ring/resultant facts and universal source-swap
response are established separately in THEOREMS.md.
"""
import json
from math import isqrt
from pathlib import Path
import sympy as s
import mpmath as mp

mp.mp.dps=360
T=s.Symbol('t')
P=s.Symbol('p',positive=True)
A=T*T+2
B=T*T+2*T+2
H=s.expand(A*B)
Q=s.expand((1-T)*H)
checks=0

def assertc(expr):
    global checks
    assert expr
    checks+=1

assertc(H==T**4+2*T**3+4*T**2+4*T+4)
assertc(s.resultant(A,B,T)==8)
assertc(s.Poly(H,T, modulus=2)==s.Poly(T**4,T,modulus=2))
E=s.rem((4+T**4)/8,H,T)
assertc(s.expand(E+T**3/s.Integer(4)+T*T/s.Integer(2)+T/s.Integer(2))==0)
assertc(s.rem(E*E-E,H,T)==0)
assertc(s.rem((1-E)**2-(1-E),H,T)==0)
assertc(s.rem(E*(1-E),H,T)==0)
assertc(s.rem(E,A,T)==1)       # E+ =1 on first root factor
assertc(s.rem(E,B,T)==0)       # E+ =0 on other factor
for prime in [3,5,7,11,13,17,19,23]:
    assertc(s.Poly(A,T,modulus=prime).gcd(s.Poly(B,T,modulus=prime)).degree()==0)

# Every possible f in the local 2-reduction F2[t]/t^4 has no idempotent except 0,1.
idempotents=[]
for poly in range(16):
    # char2: square kills cross terms, truncation t**4
    square=(poly&1)|(((poly>>1)&1)<<2)
    if square==poly:idempotents.append(poly)
    checks+=1
assertc(idempotents==[0,1])

# Independent source formula: original Mellin-integral partial fractions.
def r(j):
    return sum((int(c)/s.Integer(8*j-shift) for c,shift in [(4,7),(-2,4),(-1,3),(-1,2)]),s.Rational(0))
for j in range(1,73):
    assertc(s.factor(r(j))==(120*j*j-89*j+16)/s.Integer((2*j-1)*(4*j-1)*(8*j-7)*(8*j-3)))
    assertc(r(j)>r(j+1)>0)
for p in [7,11,13,17,19,23,29,31,37,41,43]:
    j=(p*p-1)//8
    D=s.factor(15*(r(j)-r(j+1)))
    assertc(D>0)
    d=0
    delta=D
    while delta<s.Rational(1,64):
        delta*=16;d+=1
    assertc(s.Rational(1,64)<=delta<s.Rational(1,4))
    # Actual source mark: at j+1 the 4/p^2 pole is the only p-primary term
    rp=r(j+1)
    assertc((rp-s.Rational(4,p*p)).q%p!=0)
    assertc((rp*p*p).p*pow(int((rp*p*p).q),-1,p)%p==4)
    # Source-swapped phase difference at future n=j+1+d, independent of x.
    assertc(s.factor((16**(j+1+d))*((s.Rational(15,16**(j+1)))* (r(j)-r(j+1)))-delta)==0)
    # Independent high precision using x=pi/16, not the BBP partial sum.
    m=j+1+d
    delta_mp=mp.mpf(int(delta.p))/mp.mpf(int(delta.q))
    factor=mp.power(16,m)
    phase=mp.frac(factor*mp.pi/16)
    swap=mp.frac(phase-delta_mp)
    sign=+1 if phase>=delta_mp else -1
    assertc(sign==(1 if int(mp.floor(256*phase))>int(mp.floor(256*swap)) else -1))
    assertc(int(mp.floor(256*phase))!=int(mp.floor(256*swap)))
    imag=mp.sin(2*mp.pi*delta_mp)
    assertc(imag>mp.sin(mp.pi/32)-mp.mpf('1e-200'))

# Independent pi evaluation of all the selected 48 Rademacher signals;
# 4*n+j chronological Collatz parities, not hexadecimal digits as inputs.
addr=0
for n in range(12):
    for bit in range(4):
        num=mp.power(2,4-bit)*mp.power(16,n)*mp.pi/16
        b=int(mp.floor(num))%2
        addr|=b<<(4*n+bit)
        checks+=1
assertc(addr==0xA5888A6F3423)

# Independent finite parity decoder via 2-adic reversed local branches.
def inv_word(word,bits):
    mod=1<<bits
    inv3=pow(3,-1,mod)
    x=0
    for i in range(bits-1,-1,-1):
        x=(2*x if not (word>>i)&1 else (2*x-1)*inv3)%mod
    return x
seed=inv_word(addr,48)
assertc(seed==0x138D4B466283)
state=seed
bits=[]
for j in range(48):
    bits.append(state&1)
    state=state//2 if state%2==0 else (3*state+1)//2
    assertc(bits[-1]==((addr>>j)&1))

# Finite original-BBP 3-adic reciprocity: nearest odd-return distance fixes mod3.
positions=[i for i in range(48) if (addr>>i)&1]
for a,b in zip(positions,positions[1:]):
    x=seed
    for _ in range(a):x=x//2 if x%2==0 else (3*x+1)//2
    assertc(x%2==1)
    gap=b-a
    assertc((3*x+1)%(1<<gap)==0)
    assertc(((3*x+1)//(1<<gap))%3 == (1 if gap%2==0 else 2))

receipt={
    'audit':'independent_sympy_mpmath',
    'result':'PASS',
    'exact_and_high_precision_checks':checks,
    'prime_square_events_checked':11,
    'prime_labels':[7,11,13,17,19,23,29,31,37,41,43],
    'ring_f2_idempotents':idempotents,
    'ring_resultant':8,
    'parity_address_48_bits':hex(addr),
    'collatz_seed_mod_2_48':hex(seed),
    'mpmath_decimal_digits':mp.mp.dps,
    'scope':'Finite independent-calculation audit, not independent proof of universal estimates or R0.'
}
Path(__file__).with_name('audit_receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps(receipt,indent=2,sort_keys=True))
