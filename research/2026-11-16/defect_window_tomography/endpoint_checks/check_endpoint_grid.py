"""Independent exact interval/extrema audit; run from the SUCC repo root."""
from fractions import Fraction as F
import importlib.util

spec=importlib.util.spec_from_file_location('grid','scripts/endpoint_shell_certificate.py')
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
checks=0

for q in (2,4,16,32,256):
    for a in range(q):
        low,high=g.grid_distance_bounds(a,q)
        # Exhaust all extrema of the triangular torus-distance function.
        points=[F(a,q),F(a+2,q)]
        points.extend(F(k,2) for k in range(5)
                      if F(a,q)<=F(k,2)<=F(a+2,q))
        ds=[min(x%1,1-x%1) for x in points]
        assert F(low,q)==min(ds),(q,a,low,ds)
        assert F(high,q)>=max(ds),(q,a,high,ds)
        checks+=2

for M in (1,2,7,31,83):
    for d in (1,2,3,6):
        N=2*M+d
        u=g.terminal_state(N)
        C=u.numerator//u.denominator
        Q=16**d
        # A strictly deeper rational prefix and source tail enclose true x.
        later=g.terminal_state(N+8)/16**(N+8)
        upper=later+g.forcing(N+9)/(15*16**(N+8))
        assert 0<C<16**N
        for n in range(2*M):
            scale=16**(N-n)
            integer=C//scale
            a=(C//16**(2*M-n))%Q
            left,right=F(a,Q),F(a+2,Q)
            assert left<16**n*later-integer<16**n*upper-integer<right,(M,d,n)
            checks+=1

print('exact interval/extrema assertions',checks,'PASS')
