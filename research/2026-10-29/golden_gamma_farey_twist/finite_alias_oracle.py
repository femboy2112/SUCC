"""Independent numerical finite-resolution Eisenstein alias demonstration, not proof."""
from mpmath import mp
mp.dps=65

def sigma3minus(n):return sum(mp.mpf(d)**-3 for d in range(1,n+1) if n%d==0)
def a(n,y=mp.mpf(1)):
 return mp.pi/(2*mp.zeta(4)*y)*(1+2*mp.pi*n*y)*mp.exp(-2*mp.pi*n*y)*sigma3minus(n)
def upper(q,y=mp.mpf(1)):
 C=mp.pi*mp.zeta(3)/(2*mp.zeta(4)*y)
 B=2*mp.pi*y;v=mp.exp(-4*mp.pi*y)
 return 4*C*C*v**q*((1+B*q)**2/(1-v)+B*B*v*(1+v)/(1-v)**3)
for q in [1,2,4,8,16]:
 e=2*sum(a(m*q)**2 for m in range(1,21))
 upper_bound=upper(q)
 assert e>0 and e<upper_bound
 print('NONUNIFORM_MASS_Q',q,'energy',mp.nstr(e,35),'analytic_upper',mp.nstr(upper_bound,35),'ratio',mp.nstr(e/upper_bound,12))
print('FINITE_ALIAS_ORACLE_PASS (all values numerical; inequality is paper proved)')
