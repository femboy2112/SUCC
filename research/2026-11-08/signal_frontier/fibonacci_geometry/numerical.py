"""Independent Cartesian golden-circle readout. Numerical corroboration only."""
from hashlib import sha256
from pathlib import Path
import argparse
import json
import mpmath as mp
from oracle import fibonacci


def center_cartesian(p0,p1,p2):
    u,v=p1-p0,p2-p0
    A=(abs(p1)**2-abs(p0)**2)/2
    B=(abs(p2)**2-abs(p0)**2)/2
    det=u.real*v.imag-u.imag*v.real
    return mp.mpc((A*v.imag-B*u.imag)/det,(u.real*B-v.real*A)/det)


def run():
    ambient=mp.mp.dps
    rows=[]
    with mp.workdps(100):
        alpha=(mp.sqrt(5)-1)/2
        c,g=mp.mpc(mp.mpf(2)/7,-mp.mpf(3)/11),mp.mpc(mp.mpf(7)/5,mp.mpf(2)/3)
        R=abs(g);epsilon=mp.mpf('1e-12');tol=mp.mpf('1e-65')
        def point(j):return c+g*mp.exp(2j*mp.pi*j*alpha)
        def data(k):
            q=fibonacci(k);delta=(-1)**(k-1)*alpha**k
            ps=[point(j*q) for j in range(3)]
            rho=mp.exp(2j*mp.pi*delta)
            w=ps[2]-2*ps[1]+ps[0]
            D=mp.conj(rho)*w/delta**2
            return q,delta,ps,rho,w,D
        def string(x):return mp.nstr(x,45)
        for k in (2,3,5,8,13,21,34):
            q,delta,ps,rho,w,D=data(k)
            recovered=center_cartesian(*ps)
            gain=ps[0]-recovered
            d=ps[1]-ps[0]
            assert abs(recovered-c)<tol and abs(gain-g)<tol
            assert abs(abs(w)/abs(d)**2-1/R)<tol
            assert abs(q*alpha-fibonacci(k-1)-delta)<tol
            curvature_error=abs(D+4*mp.pi**2*g)
            curvature_bound=4*mp.pi**4*R*alpha**(2*k)/3
            assert curvature_error<=curvature_bound+tol
            Dnext=data(k+1)[-1]
            J=(Dnext-alpha**2*D)/(1-alpha**2)
            rich_error=abs(J+4*mp.pi**2*g)
            rich_bound=(8*mp.pi**6/45)*R*alpha**(4*k)*alpha**2*(1+alpha**2)/(1-alpha**2)
            assert rich_error<=rich_bound+tol
            noisy=[ps[0]+epsilon,ps[1]-epsilon,ps[2]+epsilon]
            nd=noisy[1]-noisy[0];nw=noisy[2]-2*noisy[1]+noisy[0]
            noisy_gain=nd**2/nw
            t=abs(rho-1);u=epsilon/(R*t*t)
            gain_error=abs(noisy_gain-g)
            if u<=mp.mpf(1)/64:assert gain_error<=14*epsilon/t**2+tol
            known_gain=(noisy[1]-noisy[0])/(rho-1)
            assert abs(known_gain-g)<=2*epsilon/t+tol
            rows.append({'k':k,'integer_return':q,'signed_return_turns':string(delta),
                         'center_recovery_error':string(abs(recovered-c)),
                         'curvature_bias':string(curvature_error),'curvature_bound':string(curvature_bound),
                         'two_resolution_bias':string(rich_error),'two_resolution_bound':string(rich_bound),
                         'epsilon':string(epsilon),'noise_ratio_u':string(u),
                         'blind_budget_applicable':bool(u<=mp.mpf(1)/64),
                         'blind_gain_error':string(gain_error),
                         'known_phase_gain_error':string(abs(known_gain-g))})
    assert mp.mp.dps==ambient
    return {'status':'NUMERICAL-CORROBORATION-NOT-INTERVAL','precision_digits':100,
            'independent_algorithm':'Cartesian perpendicular-bisector center versus chord-ratio theorem',
            'rows':rows,'global_precision_preserved':True,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(len(result['rows']),'golden-circle numerical cases pass')
if __name__=='__main__':main()
