from fractions import Fraction as Q
from observational_succ.selected_orbit import SelectedOrbit, original_forcing
import mpmath as mp
mp.mp.dps=80
F=lambda t:mp.mpf(t.numerator)/t.denominator
ex=lambda t:mp.expjpi(2*F(t))
seeds=(Q(0),Q(1,16),Q(1,3)); Bs=(7,13,37,73); qs=(1,2,7,16); hs=(1,-1,3,17)
exact_rows=0; num_cases=0; max_ratio=mp.mpf(0)
for seed in seeds:
    o=SelectedOrbit(seed)
    for n in range(146):
        y=o.state(n+1); r=original_forcing(n+1); c=(16*o.state(n)+r).__floor__()
        assert (Q(c)+y-r)/16==o.state(n)
        exact_rows+=1
    for B in Bs:
      for q in qs:
       for h in hs:
        truth=mp.mpc(0); approx=mp.mpc(0)
        for n in range(B,2*B):
            y=o.state(n+1);r=original_forcing(n+1); c=(16*o.state(n)+r).__floor__()
            w=(q*y).__floor__();lam=q*y-w
            assert Q(0)<=lam<1
            weight=ex(Q(h,16)*(c-r))
            approx+=weight*((1-F(lam))*ex(Q(h*w,16*q))+F(lam)*ex(Q(h*(w+1),16*q)))
            truth+=ex(h*o.state(n))
        err=abs(truth-approx)/B; bound=mp.pi**2*h*h/(512*q*q)
        assert err<=bound+mp.mpf('1e-70')
        max_ratio=max(max_ratio,err/bound);num_cases+=1
# seed alias exact
z=SelectedOrbit(0);a=SelectedOrbit(Q(1,16))
assert all(z.state(n)==a.state(n) for n in range(1,147))
# Missing forcing correction kills claimed q^-2 accuracy.
n=0; y=z.state(1); c=original_forcing(1).__floor__(); q=16; w=(q*y).__floor__();lam=q*y-w
bad=ex(Q(c,16))*((1-F(lam))*ex(Q(w,16*q))+F(lam)*ex(Q(w+1,16*q)))
assert abs(ex(z.state(0))-bad)>mp.pi**2/(512*q*q)
# Moment ambiguity asymptotic sharpness: symmetric interior pair and midpoint.
ratios=[]
for q in (16,64,256):
    eps=Q(1,10000*q); left=eps; right=Q(1,q)-eps; mid=Q(1,2*q)
    assert (left+right)/2==mid
    gap=abs((ex(left/16)+ex(right/16))/2-ex(mid/16))
    ratios.append(str(gap/(mp.pi**2/(512*q*q))))
print({'exact_rows':exact_rows,'interpolation_cases':num_cases,'max_observed_error_over_bound':str(max_ratio),'alias_rows':146,'missing_source_mutant':'rejected','sharpness_ratios':ratios,'numeric_status':'80-digit exploratory checks; analytic bound is authority'})
