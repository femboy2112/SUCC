"""Independent hostile numerical audit; no production/research oracle imports.

Double-precision probes corroborate inequalities and may falsify them.
They are not interval or universal proof certificates.
"""
from pathlib import Path
from hashlib import sha256
import argparse,cmath,itertools,json,math,random
import numpy as np

HERE=Path(__file__).resolve().parent


def geometry():
    ratios={k:0. for k in ('g','c','radius','curvature','z','unit_phase','rho','turn')}
    count=0
    directions=[cmath.exp(2j*math.pi*j/16) for j in range(16)]
    rng=random.Random(81173)
    alpha=(math.sqrt(5)-1)/2
    rotations=[('diameter',-1+0j)]+[(f'golden_{k}',cmath.exp(2j*math.pi*((-1)**(k-1)*alpha**k))) for k in (2,3,5,8,12)]
    for label,rho in rotations:
        c=complex(0.4,-0.7);g=complex(0.6,0.8);R=abs(g);t=abs(rho-1);u=1/64;eps=u*R*t*t
        clean=[c+g*rho**j for j in range(3)];z=cmath.exp(2j*math.pi*.371);Y=c+g*z
        noises=itertools.product(directions,repeat=4) if label=='diameter' else ([rng.choice(directions) for _ in range(4)] for _ in range(4096))
        for noise in noises:
            pts=[x+eps*eta for x,eta in zip(clean,noise)];yy=Y+eps*noise[3]
            d=pts[1]-pts[0];w=pts[2]-2*pts[1]+pts[0]
            gg=d*d/w;cc=pts[0]-gg;zz=(yy-cc)/gg;zhat=zz/abs(zz)
            rr=(pts[2]-pts[1])/d
            records={'g':abs(gg-g)/(14*eps/t**2),'c':abs(cc-c)/(18*eps/t**2),
                     'radius':abs(abs(gg)-R)/(14*u*R),'curvature':abs(1/abs(gg)-1/R)/(18*u/R),
                     'z':abs(zz-z)/(48*u),'unit_phase':abs(zhat-z)/(96*u),
                     'rho':abs(rr-rho)/(4*eps/(R*t-2*eps))}
            if label!='diameter':
                turn=cmath.phase(rr/abs(rr))/math.tau;actual=cmath.phase(rho)/math.tau
                records['turn']=abs(turn-actual)/(2*eps/(R*t-2*eps))
            for name,value in records.items():
                assert value <= 1+1e-9,(label,name,value)
                ratios[name]=max(ratios[name],value)
            count+=1
    return {'cases':count,'max_ratio_to_declared_bound':ratios,'u':'1/64',
            'noise_menu':'16 boundary directions; exhaustive 16^4 diameter case, deterministic 4096 samples per golden return'}


def frames():
    fib=[0,1]
    for _ in range(15):fib.append(sum(fib[-2:]))
    alpha=(math.sqrt(5)-1)/2
    rows=[]
    for k in (5,6,7,8,9,10,11,12,13):
        q,p=fib[k],fib[k-1]
        eps=(q-1)*alpha**k/q
        nodes=np.mod(np.arange(q)*alpha,1.)
        grid=np.mod(np.arange(q)*p,q)/q
        ordered=np.sort(nodes)
        discrepancy=float(np.max(np.arange(1,q+1)/q-ordered)-np.min(np.arange(q)/q-ordered))
        assert discrepancy <=1/q+eps+1e-12
        for H in sorted({1,max(1,q//8),max(1,(q-1)//2)}):
            if 2*H>=q:continue
            modes=np.arange(-H,H+1)
            A=np.exp(2j*np.pi*nodes[:,None]*modes[None,:])/math.sqrt(q)
            B=np.exp(2j*np.pi*grid[:,None]*modes[None,:])/math.sqrt(q)
            error=float(np.linalg.norm(A-B,ord=2))
            tau=2*math.pi*H*math.sqrt(eps/q)
            singular=np.linalg.svd(A,compute_uv=False)
            assert error <=tau+1e-11,(k,H,error,tau)
            assert min(singular)>=1-tau-1e-11 and max(singular)<=1+tau+1e-11
            rows.append({'k':k,'q':q,'H':H,'discrepancy':discrepancy,'discrepancy_bound':1/q+eps,
                         'operator_error':error,'operator_bound':tau,
                         'minimum_singular':float(min(singular)),'maximum_singular':float(max(singular))})
    # Deliberately alias a bandwidth: q rows cannot identify q+1 Fourier unknowns.
    q=13;H=7;modes=np.arange(-H,H+1);nodes=np.mod(np.arange(q)*alpha,1.)
    A=np.exp(2j*np.pi*nodes[:,None]*modes[None,:])/math.sqrt(q)
    assert A.shape[1]>np.linalg.matrix_rank(A)
    return {'rows':rows,'rank_alias_control':{'q':q,'unknowns':len(modes),'rank':int(np.linalg.matrix_rank(A))}}


def run():
    proof_paths=['prime_resonance/THEOREMS.md','fixed_depth/THEOREMS.md','fibonacci_geometry/THEOREMS.md','fibonacci_covariance/THEOREMS.md','source_probe.py']
    return {'status':'PASS','authority':'Independent numerical checks and separate paper audit; not interval proof',
            'geometry':geometry(),'frames':frames(),
            'dependencies':{s:sha256((HERE.parent/s).read_bytes()).hexdigest() for s in proof_paths if (HERE.parent/s).exists()},
            'oracle_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
