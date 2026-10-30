"""Independent analytic/numerical controls. SymPy/mpmath only for diagnostics.

Analytic formulas and stdlib exact probes remain separate authorities.
No selected BBP normality claimed.
"""
from __future__ import annotations
import importlib.util, json
from pathlib import Path
import sympy as sp
import mpmath as mp
spec=importlib.util.spec_from_file_location('ct',Path(__file__).with_name('cototient_dual_probe.py'))
ct=importlib.util.module_from_spec(spec);spec.loader.exec_module(ct)

lam=(sp.sqrt(5)-1)/2
G=sp.symbols('z')
A=4*G/(4-G**2)**2
C=(4+G**2)/(4-G**2)**2
assert sp.simplify(A+C-1/(2-G)**2)==0
assert sp.simplify((4+G**2)*A-4*G*C)==0
Dodd=1+sp.log(2)+sp.log(3)/8-sp.EulerGamma-sp.Rational(9,8)*(1/(1+2*lam)**2-1/(3+2*lam)**2)
Deven=1+sp.log(2)-sp.log(3)/10-sp.EulerGamma-sp.Rational(9,10)*(1/(1+2*lam)**2+1/(3+2*lam)**2)
Delta=sp.simplify(Dodd-Deven)
assert sp.simplify(Delta - (sp.Rational(909,50)-sp.Rational(81,10)*sp.sqrt(5)+sp.Rational(9,40)*sp.log(3)))==0
assert not Delta.has(sp.EulerGamma)
Dtotal=sp.simplify(sp.Rational(4,9)*Dodd+sp.Rational(5,9)*Deven)
assert sp.simplify(Dtotal - (sp.Rational(4,5)+sp.log(2)-sp.EulerGamma))==0
Cov=sp.simplify(sp.Rational(20,81)*Delta)
assert not Cov.has(sp.EulerGamma)
assert sp.simplify(sp.Rational(1,4)/sp.Rational(5,9)-sp.Rational(9,20))==0

mp.mp.dps=60
m=lambda v:mp.mpf(v.numerator)/v.denominator if hasattr(v,'numerator') else mp.mpf(v)
values={"odd_gamma_contrast":str(mp.mpf(str(sp.N(Dodd,60)))) ,"even_gamma_contrast":str(mp.mpf(str(sp.N(Deven,60)))) ,"normalized_difference":str(mp.mpf(str(sp.N(Delta,60)))) ,"selection_covariance":str(mp.mpf(str(sp.N(Cov,60)))) ,"ordinary_weighted_mean":str(mp.mpf(str(sp.N(Dtotal,60))))}

# Two independent routes: finite source's rational signed exponential reduction,
# vs direct quadrature of the positive source times a Pascal parity likelihood.
def from_poles(n,prim):
    coeffs=ct.sector_rate_coeffs(n,prim)
    den=mp.fsum(m(c)/r for r,c in coeffs.items())
    a=8*n-7
    e_log=mp.log(2*a)-mp.euler-mp.fsum((m(c)/r)*mp.log(r) for r,c in coeffs.items())/den
    e_lap=mp.fsum(m(c)/(r+2*a*mp.mpf(str(sp.N(lam,70)))) for r,c in coeffs.items())/den
    return e_log-e_lap

def from_integral(n,prim):
    a=8*n-7
    def q(x):
        return 4-2*mp.exp(-3*x)-mp.exp(-4*x)-mp.exp(-5*x)
    def parity(x):
        p=(2*mp.exp(-8*x)-1)**n
        return (1-p)/2 if prim else (1+p)/2
    def f(x):return mp.log(2*a*x)-mp.exp(-2*a*mp.mpf(str(sp.N(lam,70)))*x)
    def integrand(x):return mp.exp(-a*x)*q(x)*parity(x)
    den=mp.quad(integrand,[0,mp.mpf('0.1'),mp.mpf('0.5'),1,mp.inf])
    num=mp.quad(lambda x:integrand(x)*f(x),[0,mp.mpf('0.1'),mp.mpf('0.5'),1,mp.inf])
    return num/den

holdouts=[]
for n in (2,4,7):
    test={"n":n}
    for prim in (True,False):
        result_a=from_poles(n,prim);result_b=from_integral(n,prim)
        assert abs(result_a-result_b)<mp.mpf('1e-45'),(n,prim,result_a,result_b)
        test['primitive' if prim else 'cototient']=str(result_a)
        test['difference_to_direct_quad_'+str(prim)]=mp.nstr(abs(result_a-result_b),8)
    test['normalized_diff']=str(mp.mpf(test['primitive'])-mp.mpf(test['cototient']))
    holdouts.append(test)
values['source_finite_holdouts']=holdouts

# Complete factorial q=6, no missing cell. Same event as the *marked* grade-rank translation J -> J+2.
def D_j(j):
    return mp.digamma(j+2)-mp.power((mp.sqrt(5)-1)/2,j+2)
q=6
cells={}
for a in (0,1):
 for b in (0,1):
    indexes=[j for j in range(170) if int(__import__('math').gcd(j,q)==1)==a and int(__import__('math').gcd(j+2,q)==1)==b]
    num=mp.fsum(mp.mpf(j+1)/mp.power(2,j+2)*D_j(j) for j in indexes)
    den=ct.grade_rank_primitive_cells(q)[(a,b)]
    val=num/m(den)
    cells[f'{a}{b}']={"probability":str(den),"contrast":str(val)}
interaction=mp.mpf(cells['11']['contrast'])-mp.mpf(cells['10']['contrast'])-mp.mpf(cells['01']['contrast'])+mp.mpf(cells['00']['contrast'])
values['grade_rank_q6']={"cells":cells,"factorial_interaction":str(interaction),"unnormalized_tail_bound_at_170":str(mp.mpf(170*170+5*170+8)/mp.power(2,171))}

z2=mp.zeta(2);zp=mp.diff(mp.zeta,2);gamma=mp.euler
fp_t=gamma/z2-zp/z2**2
fp_c=gamma*(1-1/z2)+zp/z2**2
values['dirichlet_fp']={"totient":str(fp_t),"cototient":str(fp_c),"difference":str(fp_t-fp_c),"zeta2":str(z2),"zeta2_derivative":str(zp)}
print(json.dumps(values,indent=2))
Path(__file__).with_name('independent_receipt.json').write_text(json.dumps(values,indent=2)+'\n')
