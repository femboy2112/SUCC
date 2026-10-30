"""Independent high-precision observations, NOT interval-proof certificates."""
import mpmath as mp
from math import pi
mp.mp.dps=90

lam=(mp.sqrt(5)-1)/2
gamma=mp.euler
C=mp.log(mp.gamma(mp.mpf(1)/2)*mp.gamma(mp.mpf(3)/4)/(
    mp.gamma(mp.mpf(19)/24)*mp.gamma(mp.mpf(21)/40)))
K=C-gamma/15
assert mp.mpf('0.0522')<K<mp.mpf('0.0523')
print('DPS',mp.mp.dps)
print('GAMMA_LOG_COMPLETION',mp.nstr(C,65))
print('EULER_HARMONIC_FINITE_PART',mp.nstr(K,65))
print('GOLDEN_OMEGA',mp.nstr(lam-gamma,65))
print('15*K-OMEGA',mp.nstr(15*K-(lam-gamma),65))
checks=0

def eta(n):return mp.log1p(1/mp.mpf(24*n-6))+mp.log1p(1/mp.mpf(40*n-20))

def source(a):
    a=mp.mpf(a)
    return 4/a-2/(a+3)-1/(a+4)-1/(a+5)

def inversion(a):
    a=mp.mpf(a)
    return mp.log(source(16/a)/source(a))-3*mp.log(a/4)

for a in (mp.mpf('0.125'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4'),mp.mpf('9'),mp.mpf('37')):
    identity=mp.log(16*(a+3)*(a+5)/((3*a+16)*(5*a+16)))
    assert abs(inversion(a)-identity)<mp.mpf('1e-82')
    checks+=1
for n in (1,2,3,7,16,48,128):
    assert abs((mp.log(mp.mpf(16)/15)-inversion(8*n-7))-eta(n))<mp.mpf('1e-82')
    checks+=1

for N in (16,32,128,512,2048):
    s=mp.fsum(eta(n) for n in range(1,N+1))
    # Numerical holdout against completely separate Gamma functions.
    P=(mp.rf(mp.mpf(1)/2,N)*mp.rf(mp.mpf(3)/4,N)/
       (mp.rf(mp.mpf(19)/24,N)*mp.rf(mp.mpf(21)/40,N)))
    assert abs(mp.log(P)+s)<mp.mpf('1e-77')
    val=s-mp.harmonic(N)/15
    assert 0<K-val<mp.mpf(7)/(180*N)
    checks+=1
    print('N',N,'finite_part',mp.nstr(val,27),'certified_error_upper',mp.nstr(mp.mpf(7)/(180*N),8))

# Stable Abel/Cesaro phase-twist no-go: coherent phase has nonzero limiting modulus.
for c in (1,15):
    tau=mp.mpf(c)/15
    predicted=1/mp.sqrt(1+tau*tau)
    for N in (4096,20000):
        accumulating=mp.mpf('0')
        accumulator=mp.mpc(0)
        for n in range(1,N+1):
            accumulating+=eta(n)
            accumulator+=mp.exp(mp.j*c*accumulating)
        observed=abs(accumulator)/N
        # Very slow but standard logarithmic convergence; these are only observations.
        if N==20000:assert abs(observed-predicted)<mp.mpf('.002')
        checks+=1
        print('phase_twist_c',c,'N',N,'observed_modulus',mp.nstr(observed,17),'asymptotic_modulus',mp.nstr(predicted,17))

print('INDEPENDENT_NUMERICAL_HOLDOUT_PASS checks='+str(checks))
