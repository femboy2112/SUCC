"""Independent high-precision checks of zeta/Gamma/Oily analytic bridges.

Uses mpmath, not the submitted exact-Fraction implementation. Finite
calculations check predeclared identities; known analytic continuation and
weak-convergence results are established by mathematical proofs, not these runs.
"""
from __future__ import annotations
import json
import mpmath as mp
from pathlib import Path
mp.mp.dps=55


def val(z):
    return {"re":mp.nstr(mp.re(z),25),"im":mp.nstr(mp.im(z),25)} if abs(mp.im(z))>mp.mpf('1e-45') else mp.nstr(mp.re(z),25)


def derivative(s):
    return mp.diff(mp.zeta,s)


def tilted_laplace(eps, t):
    """X_e=eps*log N with N from zeta(1+eps) prior."""
    return mp.zeta(1+eps*(1+t))/mp.zeta(1+eps)


def size_biased_laplace(eps,t):
    """Size bias by log N; n=1 becomes zero mass, unlike a positive-event sensor."""
    return derivative(1+eps*(1+t))/derivative(1+eps)


def theta_completed(s):
    """Independent theta/Poisson formula for completed zeta (not Euler product)."""
    def positive_theta(t):
        return sum((mp.exp(-mp.pi*n*n*t) for n in range(1,9)),mp.mpf(0))
    integral=mp.quad(lambda t:positive_theta(t)*(t**(s/2-1)+t**((1-s)/2-1)),[1,2,4,10,mp.inf])
    return 1/(s*(s-1))+integral


def oily_kernel(x):
    return (1-x)/((2-x*x)*(x*x-2*x+2))


def oily_laplace(a,t):
    """The actual original positive Oily kernel, Y=a*(1-x)."""
    breaks=sorted(set([mp.mpf(0),mp.mpf(1),mp.mpf(4),mp.mpf(12),mp.mpf(30),mp.mpf(60),mp.mpf(a)]))
    def weight(y):
        x=1-y/a
        return (x**a)*oily_kernel(x)/a
    z=mp.quad(weight,breaks)
    return mp.quad(lambda y:mp.exp(-t*y)*weight(y),breaks)/z


def run():
    details={"precision_dps":mp.mp.dps,"scope":"independent numeric controls, not full proofs or RH claims"}
    for s in (mp.mpf('2'), mp.mpf('2.5'),mp.mpf('2')+3j, mp.mpf('0.5')+7j):
        lhs=theta_completed(s)
        rhs=mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
        diff=abs(lhs-rhs)
        assert diff<mp.mpf('1e-44'),(s,diff)
        details.setdefault("theta_Mellin_gluing",[]).append({"s":val(s),"theta":val(lhs),"zeta_gamma":val(rhs),"error":mp.nstr(diff,12)})

    details["beta_near_critical"]=[]
    for estr in ('0.25','0.1','0.05','0.02','0.01','0.005'):
        e=mp.mpf(estr)
        lap=tilted_laplace(e,mp.mpf(1))
        size=size_biased_laplace(e,mp.mpf(1))
        mean=-derivative(1+e)/mp.zeta(1+e)
        finite_part=mean-1/e
        details["beta_near_critical"].append({"epsilon":estr,"exp_laplace_t1":val(lap),"target": "0.5", "sizebiased_gamma2_laplace_t1":val(size),"target_gamma2":"0.25","log_mean_finite_part":val(finite_part),"target_finite_part":val(-mp.euler)})
        assert abs(lap-mp.mpf('.5'))<mp.mpf('.071')
        assert abs(size-mp.mpf('.25'))<mp.mpf('.005')
    assert abs(mp.mpf(details['beta_near_critical'][-1]['log_mean_finite_part'])+mp.euler)<mp.mpf('0.001')

    details["oily_exact_kernel_laplace"]=[]
    for a in (16,64,256,1024):
        lap=oily_laplace(mp.mpf(a),mp.mpf(1))
        details['oily_exact_kernel_laplace'].append({"a":a,"Laplace_Gamma2_t1":val(lap),"limit":"0.25"})
    assert abs(mp.mpf(details['oily_exact_kernel_laplace'][-1]['Laplace_Gamma2_t1'])-mp.mpf('.25'))<mp.mpf('0.003')

    details['gamma_KL']={"KL_Exp_to_Gamma2":val(mp.euler),"KL_Gamma2_to_Exp":val(1-mp.euler),"symmetric":val(1)}
    details['zeta2']=val(mp.zeta(2)); details['zeta2_pi']=val(mp.pi**2/6)
    assert abs(mp.zeta(2)-mp.pi**2/6)<mp.mpf('1e-50')
    dest=Path(__file__).resolve().parents[1]/'research/2026-10-28/ZETA_WAVEFRONT_ORACLE_RECEIPT.json'
    dest.write_text(json.dumps(details,indent=2,sort_keys=True)+'\n')
    print('PASS: independent mpmath zeta/size-biased Gamma law, Euler finite part, theta-Mellin gluing and original Oily kernel')
    print('receipt',dest)
    print('final eps',details['beta_near_critical'][-1])
    print('Oily a=1024:',details['oily_exact_kernel_laplace'][-1])

if __name__=='__main__':run()
