#!/usr/bin/env python3
"""Independent exact carry/cylinder calibration, preserved from the adversary lane."""
from fractions import Fraction as Q
from math import prod
checks = 0

def check(ok):
    global checks
    checks += 1
    assert ok, checks

for m in range(1, 9):
    for L in range(1, 13):
        den = 2**(m+L)
        cuts = [Q(j,3*2**m) for j in range(1,3*2**m) if j%3]
        cells = {int(den*x) for x in cuts}
        alt = {int(''.join(str((i+b)%2) for i in range(L)),2) for b in (0,1)}
        expected = {a*2**L+s for a in range(2**m) for s in alt}
        check(cells == expected)
        check(len(cells) == 2**(m+1))
        check(Q(len(cells),den) == Q(2,2**L))
        for x in cuts:
            a = int(den*x)
            lo,hi = (Q(a,den)+x)/2, (Q(a+1,den)+x)/2
            check(int(den*lo) == int(den*hi))
            def label(t):
                qx = 3*t
                return int(2**m*(qx-int(qx)))
            check(label(lo) != label(hi))

for q in range(3, 32, 2):
    for m in range(1, 8):
        for L in range((q-1).bit_length(),(q-1).bit_length()+6):
            cells = {(j*2**L)//q for j in range(1,q*2**m) if j%q}
            check(len(cells) == (q-1)*2**m)
            check(Q(len(cells),2**(m+L)) == Q(q-1,2**L))

for p in [Q(1,4),Q(1,3),Q(2,5),Q(1,2),Q(2,3),Q(3,4)]:
    d = 1-p+p*p
    f13,f23 = (1-p)**2/d,(1-p)/d
    check(f13 == (1-p)*f23)
    check(f23 == 1-p+p*f13)
    f16,f56 = (1-p)*f13,1-p+p*f23
    law = f16+(1-p-f13)+(f56-f23)
    check(law == 1-p+p*(1-p)*(2*p-1)/d)
    for L in range(1,20):
        altmass = sum(prod(p if (i+b)%2 else 1-p for i in range(L)) for b in (0,1))
        expected = (2 if L%2 == 0 else 1)*(p*(1-p))**(L//2)
        check(altmass == expected)
check(Q(3,4)+Q(1,4)*Q(3,4)*(Q(1,2)-1)/(1-Q(1,4)+Q(1,16)) == Q(33,52))
cycle = {Q(pow(2,r,5),5) for r in range(4)}
check(cycle == {Q(i,5) for i in range(1,5)})
check({3*x-int(3*x) for x in cycle} == cycle)
check(16*Q(1,5)-int(16*Q(1,5)) == Q(1,5))
check(3*Q(1,5)-int(3*Q(1,5)) != Q(1,5))
print({'checks': checks, 'status': 'passed', 'arithmetic': 'integers and Fraction only'})
