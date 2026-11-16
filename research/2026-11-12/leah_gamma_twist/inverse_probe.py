from fractions import Fraction as Q
from observational_succ.duck_bbp import forcing
from observational_succ.selected_orbit import SelectedOrbit

checks=0
for seed in [Q(0), Q(1,16), Q(1,7), -sum((forcing(k)/16**k for k in range(1,601)),Q())]:
    o=SelectedOrbit(seed)
    eps=[o.state(n)-(o.state(n)+Q(1,2)).numerator//(o.state(n)+Q(1,2)).denominator for n in range(601)]
    a=[None]+[16*eps[n-1]+forcing(n)-eps[n] for n in range(1,601)]
    for n in range(2,601):
        assert a[n].denominator==1 and abs(a[n])<=8
        checks+=1
    for B in [1,2,3,5,11,23,37,73,149,293]:
        E=sum((eps[n]**2 for n in range(B,2*B)),Q())
        D=eps[2*B]**2-eps[B]**2
        K=sum((a[n+1]**2 for n in range(B,2*B)),Q())
        R=sum(((a[n+1]-forcing(n+1))**2 for n in range(B,2*B)),Q())
        diff=sum(((eps[n]-eps[n+1])**2 for n in range(B,2*B)),Q())
        plus=sum(((eps[n]+eps[n+1])**2 for n in range(B,2*B)),Q())
        assert R==225*E+16*diff-15*D
        assert R==289*E-16*plus+17*D
        assert 225*E-Q(15,4)<=R<=289*E+Q(17,4)
        budget=Q(15,4*B)+Q(225,4096*B**3)
        assert abs(R-K)<=budget
        checks+=4
        for L in [1,2,3,5,8]:
            if L>B: continue
            good=[n for n in range(B,2*B-L) if all(a[n+j]==0 for j in range(1,L+1))]
            assert B-len(good)<=L*(1+K)
            for n in good:
                block=sum((forcing(n+j)/16**j for j in range(1,L+1)),Q())
                assert eps[n]+block==eps[n+L]/16**L
                checks+=1
            checks+=1
print({'exact_checks':checks,'seeds':4,'shells_per_seed':10,'max_source_clock':600})
