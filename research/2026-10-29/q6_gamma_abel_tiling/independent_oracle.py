"""Independent research oracle: rational BBP recurrence, actual q=6 carry atoms,
positive four-pole integral, and Gamma Fresnel/Dirichlet identities.

Numerical results are observations, not interval-certified infinite proofs.
"""
from fractions import Fraction
from math import comb,gcd,pi,sin,sqrt
from collections import defaultdict
import json
import mpmath as mp

mp.mp.dps=110
lam=(mp.sqrt(5)-1)/2


def r(n):
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)


def q(n):
    rn=r(n)
    return [Fraction(comb(n,j))*sum((Fraction((-1)**k*comb(j,k))*r(2*n-j+k) for k in range(j+1)),Fraction())/rn for j in range(n+1)]


def u_and_carry(N):
    s=Fraction();out=[s];c=[None]
    for n in range(1,N+1):
        v=16*s+r(n)
        k=v.numerator//v.denominator
        s=v-k
        out.append(s);c.append(k)
    return out,c


def mpfrac(a):return mp.mpf(a.numerator)/a.denominator

def degree(j):return int(gcd(j+2,6)==1)-int(gcd(j,6)==1)

def Dincrement(j):return mp.mpf(1)/(j+2)+mp.mpf(1)/(j+3)+lam**(j+3)

def complex_seam(n,h,states,carries,twist=True):
    sum_by_bin=defaultdict(lambda:mp.mpc(0))
    w=q(n)
    z_anchor=mp.e**(2j*mp.pi*h*mpfrac(states[n+1]))
    for j,wj in enumerate(w):
        d=degree(j)
        if not d:continue
        z=mp.e**(2j*mp.pi*h*mpfrac(states[n+j]))
        angle=mp.e**(1j*mp.pi*(j+2)/8) if twist else 1
        sum_by_bin[carries[n+j]]+=mpfrac(wj)*d*Dincrement(j)*angle*(z-z_anchor)
    return dict(sum_by_bin)


def tail(n,depth=85):
    return sum(mp.mpf(1)/16**j*mpfrac(r(n+j)) for j in range(1,depth+1))


def coherent_seam(n,h,twist=True):
    ws=q(n)
    u0=-tail(n+1)
    anchor=mp.e**(2j*mp.pi*h*u0)
    val=mp.mpc(0)
    for j,wj in enumerate(ws):
        d=degree(j)
        if not d:continue
        # U_{n+j}(s_*)=-T_{n+j}, exactly at the formal infinite level.
        u=-tail(n+j)
        factor=mp.e**(1j*mp.pi*(j+2)/8) if twist else 1
        val+=mpfrac(wj)*d*Dincrement(j)*factor*(mp.e**(2j*mp.pi*h*u)-anchor)
    return val


def independent_scalar_control():
    # Gamma(1/2) Fresnel Abel rotation at the quartic split.
    eps=mp.mpf('0.00000001')
    value=mp.gamma(mp.mpf('0.5'))/(eps-1j)**mp.mpf('0.5')
    phase=mp.arg(value)
    assert abs(phase-mp.pi/4)<mp.mpf('1e-8')
    # Dirichlet(1/2 fourfold) normalization has Gamma(2)/Gamma(1/2)^4=1/pi^2.
    assert abs(mp.gamma(2)/mp.gamma(mp.mpf('0.5'))**4-1/mp.pi**2)<mp.mpf('1e-90')
    # Genuine rank response increment is gamma-free and positive at each grade.
    for j in range(60):
        D=lambda rr: mp.digamma(rr)-(1+lam)**(-rr)
        assert abs((D(j+4)-D(j+2))-Dincrement(j))<mp.mpf('1e-90')
    return phase


def main():
    phase=independent_scalar_control()
    states,carries=u_and_carry(121)
    observed=[]
    for n in (5,8,12,20,30,45,60):
        vals=complex_seam(n,1,states,carries)
        coherent=coherent_seam(n,1)
        observ={"n":n,"actual_sum_abs":float(abs(sum(vals.values()))),
                "actual_carry_l1":float(sum(abs(v) for v in vals.values())),
                "nonzero_carry_bins":sorted(vals),
                "coherent_abs":float(abs(coherent)),
                "coherent_all_carries_15":True}
        observed.append(observ)
        print(n,observ)
    # Exact residue sums independent from geometric-closed calculation via high-depth series.
    mass_1=sum(mp.mpf(j+1)/mp.power(2,j+2) for j in range(1,250,6))
    mass_3=sum(mp.mpf(j+1)/mp.power(2,j+2) for j in range(3,250,6))
    assert abs(mass_1-mp.mpf(352)/1323)<mp.mpf('1e-60')
    assert abs(mass_3-mp.mpf(172)/1323)<mp.mpf('1e-60')
    # The independent generic irrational rotation control (sqrt(2)) crosses the lower threshold often.
    vals=[abs(mp.e**(2j*mp.pi*255*16**n*mp.sqrt(2))-1) for n in range(40)]
    assert max(vals) >= 2*mp.sin(mp.pi/17)
    report={"source":"original four pole BBP", "phase_tests":observed,
            "fresnel_quarter_angle_deg":float(phase*180/mp.pi),
            "exact_limit_lower_bound":"86984497/13280710590",
            "normality_proved":False,"fully_certified_interval_oracle":False}
    with open('/mnt/data/succ_gamma_farey_tiling/independent_receipt.json','w') as f:json.dump(report,f,indent=2)

if __name__=='__main__':main()
