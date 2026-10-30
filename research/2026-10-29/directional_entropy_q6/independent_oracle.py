"""Independent high-precision checks for SUCC four-pole directional information.

Separate direct Laplace-integral implementation; numerical observations only.
No numerical output proves the all-parameter theorem or pi normality.
"""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps=58
T=mp.mpf
POLES=((0,4),(3,-2),(4,-1),(5,-1))
CELLS={"00":(0,2,4),"01":(3,),"10":(1,),"11":(5,)}


def r(a):
    return mp.fsum(T(c)/(a+d) for d,c in POLES)

def q(x):
    return 4-2*mp.exp(-3*x)-mp.exp(-4*x)-mp.exp(-5*x)

def mu_mean(a):
    return mp.fsum(T(c)/(a+d)**2 for d,c in POLES)/r(a)

def cell_func(t,residues):
    u=t-t*t/2;v=t*t/2
    if abs(u-v)<mp.mpf('1e-65'):
        return mp.fsum(mp.fsum((T(r+6*k+1)/2**(r+6*k+2) for k in range(65))) for r in residues)
    def cell(r):
        return (1-u)*(1-v)/(u-v)*(u**(r+1)/(1-u**6)-v**(r+1)/(1-v**6))
    return mp.fsum(cell(r) for r in residues)

def cell_masses(a):
    norm=r(a)
    def one(rs):
        f=lambda y: mp.exp(-y)*q(y/a)*cell_func(mp.exp(-y/a),rs)/(a*norm)
        return mp.quad(f,[0,3,12,32,75,mp.inf])
    result={key:one(rs) for key,rs in CELLS.items()}
    assert abs(mp.fsum(result.values())-1)<mp.mpf('1e-47')
    return result


def entropy(p,q):
    return mp.fsum(p[k]*mp.log(p[k]/q[k]) for k in CELLS)

# Independent direct cumulants by differentiation of log four-pole R.
def kappa(a):
    f=lambda x:mp.log(r(x))
    return mp.diff(f,a,2),-mp.diff(f,a,3)

out={"source":"authentic signed four-pole rational forcing, positive Laplace carrier","checks":{}}
for a in [T(1),T(9),T(17),T(81),T(321)]:
    s=T(8)
    lr=mp.log(r(a)/r(a+s)); m=mu_mean(a); ms=mu_mean(a+s)
    forward=lr-s*ms; reverse=s*m-lr
    v,k3=kappa(a)
    assert 0<forward<reverse
    assert abs(forward+reverse-s*(m-ms))<mp.mpf('1e-50')
    assert v>0 and k3>0
    out["checks"][str(int(a))]={"forward_KL":mp.nstr(forward,20),"reverse_KL":mp.nstr(reverse,20),"jeffreys":mp.nstr(forward+reverse,20),"arrow":mp.nstr(reverse-forward,20)}

alpha=(T(121)-mp.sqrt(241))/30
beta=(T(121)+mp.sqrt(241))/30
parts=[(1,(1+T(j))/8) for j in (0,3,4,5)]+[(-1,(1+x)/8) for x in (alpha,beta)]
minfo=T(6853)/5640
alim=-8*minfo-2*mp.fsum(sign*mp.digamma(t) for sign,t in parts)-2*mp.log(T(3008)/225)
assert 5 < alim < 6
out["total_symmetric_information"]=mp.nstr(8*minfo,35)
out["total_directional_asymmetry"]=mp.nstr(alim,35)
out["total_forward_information"]=mp.nstr((8*minfo-alim)/2,35)
out["total_reverse_information"]=mp.nstr((8*minfo+alim)/2,35)

# Direct integral source measure, with original Oily geometric grade conditional.
p_end={"00":T(5)/9,"01":T(172)/1323,"10":T(352)/1323,"11":T(64)/1323}
c_end={"00":T(4)/27,"01":-T(4468)/27783,"10":T(4640)/27783,"11":-T(4288)/27783}
K=T(871588)/1042965
for a in [T(80),T(160),T(320),T(640),T(1280)]:
    p=cell_masses(a)
    pnext=cell_masses(a+8)
    kl=entropy(pnext,p)
    out["checks"]["q6_"+str(int(a))]={"asymptotic_scaled_marginal_KL":mp.nstr(a**4*kl,20),"target":mp.nstr(128*K,20),"scaled_mass_errors":{key:mp.nstr(a*(p[key]-p_end[key]),17) for key in CELLS},"first_jet_target":{key:mp.nstr(2*c_end[key],17) for key in CELLS}}
    assert kl>0 and kl<mp.mpf('0.00001')

output=Path(__file__).with_name('independent_oracle_receipt.json')
output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('Independent quadrature and directional KL checks PASS')
print('Total symmetric KL:',out['total_symmetric_information'])
print('Total directional asymmetry:',out['total_directional_asymmetry'])
for key in ('q6_80','q6_160','q6_320','q6_640','q6_1280'):
    print(key, 'scaled q6 KL',out['checks'][key]['asymptotic_scaled_marginal_KL'],'target',out['checks'][key]['target'])
