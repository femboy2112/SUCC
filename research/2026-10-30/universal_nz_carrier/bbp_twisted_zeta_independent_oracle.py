"""Separate SymPy/mpmath reference for BBP shifted-zeta source pole, no local imports."""
import json
import sympy as sp
import mpmath as mp
mp.mp.dps=90
n=sp.symbols('n',positive=True,integer=True)
R=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
assert sp.limit(n**2*R,n,sp.oo)==sp.Rational(15,64)
assert sp.simplify(n*R-(sp.Rational(7,16)/(n-sp.Rational(7,8))-sp.Rational(1,8)/(n-sp.Rational(1,2))-sp.Rational(3,64)/(n-sp.Rational(3,8))-sp.Rational(1,32)/(n-sp.Rational(1,4))))==0
original=-sum(mp.mpf(c*(8-d))/64*mp.digamma(mp.mpf(d)/8) for d,c in [(1,4),(4,-2),(5,-1),(6,-1)])
mutant=-mp.mpf(35)/64*mp.digamma(mp.mpf(1)/8)+mp.mpf(20)/64*mp.digamma(mp.mpf(1)/2)
assert abs(original-mutant)>mp.mpf('0.01')
N=2048
h=mp.fsum(j*(4/mp.mpf(8*j-7)-2/mp.mpf(8*j-4)-1/mp.mpf(8*j-3)-1/mp.mpf(8*j-2)) for j in range(1,N+1))
assert abs(h-mp.mpf(15)/64*mp.log(N)-original)<mp.mpf(2)/N
print(json.dumps({'status':'PASS','finite_part_original':mp.nstr(original,75),'finite_part_mutant':mp.nstr(mutant,75),'source_harmonic_limit_N':N,'source_residue':'15/64','mpmath':mp.__version__,'sympy':sp.__version__},indent=2))
