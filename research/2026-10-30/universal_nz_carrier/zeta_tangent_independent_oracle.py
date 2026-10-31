"""Independent formula-only reference for odd/even zeta tangent reflection."""
from math import comb
import mpmath as mp, json
mp.mp.dps=105
rows=[]
for m in [1,2,3,4,5,6,7,8]:
    # Direct binomial polynomials at a fixed finite grade
    n=m+2
    fine=mp.fsum([(-1)**j*comb(n,j)*mp.mpf(j+1)**m*mp.log(j+1) for j in range(n+1)])
    if m%2:
        analytic=mp.diff(mp.zeta,-m)/mp.zeta(-m)
        ref=mp.log(2*mp.pi)+mp.euler-mp.harmonic(m)+mp.fsum(mp.log(p)/(mp.mpf(p)**(m+1)-1) for p in list(__import__('sympy').primerange(2,10000)))
        # The positive prime cutoff misses a positive tail; check from the exact logarithmic derivative at 1+m.
        prime_exact=mp.log(2*mp.pi)+mp.euler-mp.harmonic(m)-mp.diff(mp.zeta,m+1)/mp.zeta(m+1)
        assert abs(prime_exact-analytic)<mp.mpf('1e-90')
        assert 0<analytic-ref<mp.mpf('0.002')
    else:
        analytic=mp.diff(mp.zeta,-m)
        ref=(-1)**(m//2)*mp.factorial(m)*mp.zeta(m+1)/(2*(2*mp.pi)**m)
        assert abs(ref-analytic)<mp.mpf('1e-90')
    assert (-1)**(m+1)*fine>0
    rows.append({'m':m,'sign':int(mp.sign(fine)),'tangent':mp.nstr(analytic,28)})
print(json.dumps({'status':'PASS','rows':rows,'precision_dps':mp.mp.dps},indent=2))
