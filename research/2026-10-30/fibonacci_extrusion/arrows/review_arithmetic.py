"""Complementary arithmetic review, no imports from arithmetic front."""
import hashlib,json
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).parent
DOSSIER=ROOT.parent/'arithmetic/FIBONACCI_ARITHMETIC.md'


def run():
    M=s.Matrix([[1,1],[1,0]])
    smith=smith_normal_form(M-16*s.eye(2),domain=s.ZZ)
    assert sorted(abs(int(smith[i,i])) for i in range(2))==[1,239]
    row_cases=[]
    for m in (17,31,71,239,478,717,239**2):
        solutions=[(16*y%m,y) for y in range(m) if (239*y)%m==0]
        assert len(solutions)==gcd(m,239)
        assert all(((x+y-16*x)%m,(x-16*y)%m)==(0,0) for x,y in solutions)
        if m==239**2:
            assert all(x%239==0 and y%239==0 for x,y in solutions)
        row_cases.append({'modulus':m,'count':len(solutions)})
    roots=[x for x in range(239) if (x*x-x-1)%239==0]
    assert roots==[16,224]
    lift=16;mod=239;lifts=[]
    for precision in range(2,7):
        good=[lift+mod*d for d in range(239)
              if ((lift+mod*d)**2-(lift+mod*d)-1)%(mod*239)==0]
        assert len(good)==1
        lift=good[0];mod*=239
        lifts.append({'precision':precision,'root':lift,'modulus':mod})
    assert lifts[0]['root']==44231
    U=F(0);birth=None;integral_count=0
    for n in range(1,211):
        r=sum((F(c,8*n-d) for c,d in ((4,7),(-2,4),(-1,3),(-1,2))),F())
        U=16*U+r
        if n<60:
            assert U.denominator%239!=0
            integral_count+=1
        elif n==60:
            scaled=239*U
            assert scaled.denominator%239!=0
            birth=(scaled.numerator*pow(scaled.denominator,-1,239))%239
            assert birth==119
    firsts={str(d):next(n for n in range(1,240) if (8*n-d)%239==0)
            for d in (7,4,3,2)}
    assert firsts=={'7':210,'4':120,'3':90,'2':60}
    r1=sum((F(c,8-d) for c,d in ((4,7),(-2,4),(-1,3),(-1,2))),F())
    r2=sum((F(c,16-d) for c,d in ((4,7),(-2,4),(-1,3),(-1,2))),F())
    D=15*r1+r2
    assert D==F(38599,819)
    assert D.numerator*pow(D.denominator,-1,239)%239==198
    n=s.symbols('n',nonnegative=True,integer=True)
    # Compare original recurrence's algebra without any source function.
    u,r,t=s.symbols('u r t')
    assert s.expand(16*(16*u+r)+t-(16*u+r)-u)==239*u+15*r+t
    fibres=[0,1]
    while fibres[-1]<5000:
        fibres.append(sum(fibres[-2:]))
    surgery=[]
    for N in (1024,4096):
        # Fixed deterministic finite string; normality itself is a paper argument.
        digits=[];k=1
        while len(digits)<N:
            digits.extend(int(c,16) for c in format(k,'x'))
            k+=1
        digits=digits[:N]
        edits=set()
        for k in range(2,len(fibres)):
            if fibres[k]>=N:break
            edits.update(range(fibres[k],min(N,fibres[k]+k*k)))
        altered=list(digits)
        for i in edits:altered[i]=0
        for width in (1,2,3):
            changed=sum(digits[i:i+width]!=altered[i:i+width]
                        for i in range(N-width+1))
            assert changed<=width*len(edits)
            surgery.append({'N':N,'width':width,'edited_positions':len(edits),
                            'changed_word_windows':changed,'upper_bound':width*len(edits)})
    result={'dossier_sha256':hashlib.sha256(DOSSIER.read_bytes()).hexdigest(),
            'smith_diagonal':[int(smith[i,i]) for i in range(2)],
            'modular_rows':row_cases,'hensel_brute_lifts':lifts,
            'first_pole_times':firsts,'integral_states_before_birth':integral_count,
            'birth_residue':birth,'forcing_initial_defect':str(D),
            'forcing_initial_residue':198,'finite_surgery_controls':surgery,
            'scope':'FA01-02 and FA04 reviewed; separate implementation, same-model authority'}
    with (ROOT/'receipts/arithmetic-review.json').open('x') as f:
        json.dump(result,f,indent=2)
    print(json.dumps(result))


if __name__=='__main__':
    run()
