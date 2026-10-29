"""Independent numerical checks, not proof of infinite normality.

No imports from relative_observer.py. Polynomial original source A/D, mpmath
high-precision pi, separate Green-tail sum, and analytic Eisenstein coefficient
are independent implementations of the objects in README.md.
"""
import mpmath as mp
from fractions import Fraction
from math import gcd

mp.mp.dps=210
B=16

def r_poly(n):
    n=mp.mpf(n)
    return (120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def green(n,depth=165):
    return mp.fsum([r_poly(n+j)/mp.power(16,j) for j in range(1,depth+1)])

def e(x):
    return mp.exp(2j*mp.pi*x)

def a(h,y):
    h=abs(int(h));y=mp.mpf(y)
    return 45/(mp.pi**3*y)*(1+2*mp.pi*h*y)*mp.exp(-2*mp.pi*h*y)*mp.fsum(mp.mpf(1)/d**3 for d in range(1,h+1) if h%d==0)

def E_val(phases,y, modes=28):
    N=len(phases)
    vals=[mp.fsum([e(h*v) for v in phases])/N for h in range(1,modes+1)]
    return 2*mp.fsum([a(h,y)**2*abs(vals[h-1])**2 for h in range(1,modes+1)])

def near(x,y,eps):
    assert abs(x-y)<eps,(mp.nstr(x,55),mp.nstr(y,55),mp.nstr(abs(x-y),25))

# Independent polynomial reproduction of signed four-pole forcing.
for n in range(1,35):
    r=4/mp.mpf(8*n-7)-2/mp.mpf(8*n-4)-1/mp.mpf(8*n-3)-1/mp.mpf(8*n-2)
    near(r_poly(n),r,mp.mpf('1e-100'))
print('ORACLE_POLYNOMIAL_FOURPOLE_PASS count=34')

alpha=mp.pi/16
prefix=mp.fsum(r_poly(j)/mp.power(16,j) for j in range(1,65))
near(prefix,alpha,mp.mpf('1e-78'))
print('ORACLE_BBP_PI_PASSPORT_PASS alpha=',mp.nstr(alpha,45))

# Strongly source-specific exact Green-tail identity, high precision only.
for n in (1,2,3,5,12,22,42):
    U=mp.power(16,n)*alpha-green(n)
    recurrence=mp.fsum(mp.power(16,n-j)*r_poly(j) for j in range(1,n+1))
    near(U,recurrence,mp.mpf('1e-72'))
    for k in (1,2,4,8):
        observed=(mp.power(16,n+k)-mp.power(16,n))*alpha +green(n)-green(n+k)
        direct=mp.fsum(mp.power(16,n+k-j)*r_poly(j) for j in range(1,n+k+1))-recurrence
        near(observed,direct,mp.mpf('1e-70'))
print('ORACLE_EXACT_GREEN_LAG_PASS n=1,2,3,5,12,22,42; k=1,2,4,8')

# Uniform in lag O(1/N) source-error. Arbitrary future lag 1 to 50.
for N in (10,24,42):
    for k in (1,2,5,13,35,50):
        delta_sum=mp.fsum(green(n)-green(n+k) for n in range(1,N+1))
        envelope=mp.fsum(mp.mpf(1)/((8*n+1)*(8*n+2)) for n in range(1,min(k,N)+1))
        assert delta_sum>0
        assert delta_sum<envelope
        assert envelope<mp.mpf(17)/648
print('ORACLE_UNIFORM_LAG_TELESCOPE_PASS N=10,24,42 k=1,2,5,13,35,50')

# Both phases are computed without using the affine recurrence to help verify.
for N in (8,16,32):
    for k in (1,2,5,13):
        C=mp.fsum(green(n)-green(n+k) for n in range(1,N+1))
        for h in (1,3):
            d=[(mp.power(16,k)-1)*mp.power(16,n)*alpha+green(n)-green(n+k) for n in range(1,N+1)]
            pure=[(mp.power(16,k)-1)*mp.power(16,n)*alpha for n in range(1,N+1)]
            observed=mp.fsum(e(h*x) for x in d)/N
            base=mp.fsum(e(h*x) for x in pure)/N
            err=abs(observed-base)
            assert err<=2*mp.pi*h*C/N+mp.mpf('1e-65')
print('ORACLE_SIGNED_RELATIVE_BOUND_PASS all N=8,16,32 k=1,2,5,13 h=1,3')

# Direct gauge-independent modular energy for relative increments.
N=32;y=mp.mpf('0.6')
relative=[15*mp.power(16,n)*alpha+green(n)-green(n+1) for n in range(1,N+1)]
source_only=[15*mp.power(16,n)*alpha for n in range(1,N+1)]
Er=E_val(relative,y)
Eb=E_val(source_only,y)
A=mp.fsum(green(n)-green(n+1) for n in range(1,N+1))
weighted=mp.fsum(h*a(h,y)**2 for h in range(1,29))
assert abs(Er-Eb)<=8*mp.pi*A*weighted/N+mp.mpf('1e-55')
print('ORACLE_MODULAR_RELATIVE_ENERGY_PASS', 'N=',N,'y=',mp.nstr(y,4),'Erel=',mp.nstr(Er,18),'Ebase=',mp.nstr(Eb,18))

# A source-specific global Green-memory constant: independent Gamma/digamma
# computation and a direct ORIGINAL rational-integral computation.
closed = (-mp.pi/20 + mp.sqrt(2)*mp.pi/48 + mp.log(2)/24
          + mp.sqrt(2)*mp.log(1+mp.sqrt(2))/24)
Sdigamma=-(4*mp.digamma(mp.mpf(9)/8)-2*mp.digamma(mp.mpf(3)/2)
           -mp.digamma(mp.mpf(13)/8)-mp.digamma(mp.mpf(7)/4))/8
Mpsi=(Sdigamma-(mp.pi-mp.mpf(47)/15))/15
rational_integral = mp.quad(
 lambda x: x**8/((1+x+x**2+x**3+x**4+x**5+x**6+x**7)
                   *(2-x*x)*(x*x-2*x+2)),
 [0,mp.mpf('0.25'),mp.mpf('0.6'),mp.mpf('0.9'),1])
near(closed,Mpsi,mp.mpf('1e-145'))
near(closed,rational_integral,mp.mpf('1e-145'))
assert 0<closed<mp.mpf(17)/648
print('ORACLE_GAMMA_45_MEMORY_CLOSED_PASS',mp.nstr(closed,50))
print('ORACLE_GAMMA_45_DERIVED_CONSTANT_2PI=',mp.nstr(2*mp.pi*closed,35))

# One parameter authentic source-memory family M(z), with inherited Oily
# two-channel fixed point z=phi^-2.  This is a positive auxiliary constant.
lam=(mp.sqrt(5)-1)/2
z_gold=lam**2
Rp=lambda x: (1-x)/((2-x*x)*(x*x-2*x+2))
Mgold_int=mp.quad(lambda x: z_gold*x**8/(1-z_gold*x**8)*Rp(x),
                  [0,mp.mpf('0.3'),mp.mpf('0.8'),1])
Mgold_sum=mp.fsum(z_gold**n*green(n) for n in range(1,241))
near(Mgold_int,Mgold_sum,mp.mpf('1e-105'))
print('ORACLE_OILY_GOLDEN_MEMORY_FAMILY_PASS',mp.nstr(Mgold_int,51))

# Same forcing, coherent advanced seed s=-pi/16 has alpha=0, so relative
# displacements tend to zero, and Eisenstein energy tends to positive Dirac.
for N in (16,64,180):
    ds=[green(n)-green(n+1) for n in range(1,N+1)]
    En=E_val(ds,1,16)
    Epoint=2*mp.fsum(a(h,1)**2 for h in range(1,17))
    assert 0<En<Epoint
    print('COHERENT_COUNTERSEED_FINITE N=',N,'energy=',mp.nstr(En,20),'point_limit=',mp.nstr(Epoint,20))

# Explicit non-source counterexample: single-increment histogram almost Haar
# while position is not. Use q-grid exact cyclotomic relations via averages.
for q in (17,31,61):
    coords=[mp.mpf(j)/(15*q) for j in range(q)]
    observed=[15*x for x in coords]
    near(mp.fsum(e(v) for v in observed)/q,0,mp.mpf('1e-95'))
    old=mp.fsum(e(v) for v in coords)/q
    assert abs(old)>mp.mpf('0.98')
print('ORACLE_NONINVARIANT_ALIAS_PASS q=17,31,61')
print('INDEPENDENT_ORACLE_ALL_PASS (no assertion on pi normality)')
