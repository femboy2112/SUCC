"""Exact Gaussian-rational circle checks, not a floating-point proof oracle."""
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))
from observational_succ.farey_gauss_defect import golden_interval
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument
from observational_succ.operational_yoneda_descent import BeliefGame, ObservationPathCategory

@dataclass(frozen=True)
class CQ:
    re: Q=Q(0)
    im: Q=Q(0)
    def __post_init__(self):
        object.__setattr__(self,'re',Q(self.re));object.__setattr__(self,'im',Q(self.im))
    def __add__(self,z):
        z=as_cq(z);return CQ(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self):return CQ(-self.re,-self.im)
    def __sub__(self,z):return self+-as_cq(z)
    def __rsub__(self,z):return as_cq(z)+-self
    def __mul__(self,z):
        z=as_cq(z);return CQ(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def conj(self):return CQ(self.re,-self.im)
    def norm2(self):return self.re*self.re+self.im*self.im
    def __truediv__(self,z):
        z=as_cq(z)
        if not z.norm2():raise ZeroDivisionError('zero complex denominator')
        return self*z.conj()*CQ(1/z.norm2())
    def __pow__(self,n):
        if type(n) is not int or n<0:raise ValueError('nonnegative exact exponent required')
        out=CQ(1);base=self
        while n:
            if n&1:out=out*base
            base=base*base;n//=2
        return out
    def pair(self):return [str(self.re),str(self.im)]

def as_cq(x):return x if isinstance(x,CQ) else CQ(x)

def rational_rotation(t):
    t=Q(t);return CQ((1-t*t)/(1+t*t),2*t/(1+t*t))

def fibonacci(k):
    if type(k) is not int or k<0:raise ValueError('nonnegative index required')
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a

def alpha_multiply(x,y):
    """Pairs a+b alpha, with alpha²=1-alpha."""
    a,b=x;c,d=y
    return a*c+b*d,a*d+b*c-b*d

def alpha_power(k):
    result=(1,0)
    for _ in range(k):result=alpha_multiply(result,(0,1))
    return result

def calibrate(points):
    if len(points)!=3:raise ValueError('three oriented readings required')
    p0,p1,p2=map(as_cq,points)
    d=p1-p0;w=p2-2*p1+p0
    if not d.norm2() or not w.norm2():raise ValueError('nonzero return chord and curvature required')
    g=d*d/w;c=p0-g;rho=(p2-p1)/d
    return {'center':c,'gain':g,'return':rho,'curvature_squared':w.norm2()/d.norm2()**2}

def points(c,g,rho):return tuple(c+g*rho**j for j in range(3))

def belief_adapter():
    """Finite exact candidates; all initial two observations coincide."""
    rotations=tuple(rational_rotation(Q(t)) for t in (Q(1,2),Q(2,3),Q(-1,2),Q(-2,3)))
    triples=[]
    for rho in rotations:
        g=CQ(1)/(rho-1);triples.append(points(-g,g,rho))
    assert all(row[0]==CQ(0) and row[1]==CQ(1) for row in triples)
    width=len(rotations);count=3*width+1;terminal=count-1
    alphabet=tuple(dict.fromkeys(p for row in triples for p in row))
    outputs=tuple(alphabet.index(triples[j][stage]) for stage in range(3) for j in range(width))+(0,)
    transitions=tuple((stage+1)*width+j if stage<2 else terminal
                      for stage in range(3) for j in range(width))+(terminal,)
    field=FiniteCarrier(count,(Instrument('read',outputs,transitions,(True,)*(count-1)+(False,)),),
                        'circle:fixed-gain-oriented-rational-candidates',
                        'three-clock-readings:common-terminal-collapse')
    labels=tuple(str(j) for _ in range(3) for j in range(width))+('terminal',)
    game=BeliefGame.build(field,tuple(range(width)),labels,target_id='original-return-rotation')
    category=ObservationPathCategory(game,3)
    return game,category

def run():
    checks={'fibonacci_return':0,'brackets':0,'circle_recovery':0,'similarity':0,
            'reflection':0,'curvature_transport':0,'noise':0,'belief':0}
    for k in range(2,202):
        sign=(-1)**(k-1)
        assert tuple(sign*v for v in alpha_power(k))==(-fibonacci(k-1),fibonacci(k))
        assert fibonacci(k-1)*fibonacci(k+1)-fibonacci(k)**2==(-1)**k
        checks['fibonacci_return']+=2
        lo,hi=golden_interval(k-1)
        assert hi-lo==Q(1,fibonacci(k)*fibonacci(k+1))
        # x²+x-1 is increasing for positive x; this certifies the bracket.
        assert lo*lo+lo-1<=0<=hi*hi+hi-1
        checks['brackets']+=2
    rotations=[rational_rotation(t) for t in (Q(1,7),Q(1,2),Q(2,3),Q(-1,3),Q(3,2))]
    centers=(CQ(),CQ(2,-3),CQ(Q(-2,7),Q(5,11)))
    gains=(CQ(1),CQ(2,-1),CQ(Q(3,5),Q(-4,5)))
    for rho in rotations:
        assert rho.norm2()==1
        for c in centers:
            for g in gains:
                row=points(c,g,rho);got=calibrate(row)
                assert (got['center'],got['gain'],got['return'])==(c,g,rho)
                assert got['curvature_squared']==1/g.norm2()
                checks['circle_recovery']+=2
                for scale,shift in ((CQ(2,1),CQ(-3,2)),(CQ(Q(1,3),Q(-2,5)),CQ(7))):
                    mapped=calibrate(tuple(scale*p+shift for p in row))
                    assert (mapped['center'],mapped['gain'],mapped['return'])==(scale*c+shift,scale*g,rho)
                    checks['similarity']+=1
                reflected=calibrate(tuple(p.conj() for p in row))
                assert reflected['return']==rho.conj()
                assert all((row[j]-row[i]).norm2()==(row[j].conj()-row[i].conj()).norm2()
                           for i in range(3) for j in range(3))
                checks['reflection']+=2
        # Exact return transport for another base rotation, at Fibonacci clocks.
        for k in range(2,10):
            rk=rho**fibonacci(k);rnext=rho**fibonacci(k+1);rprev=rho**fibonacci(k-1)
            assert rnext==rk*rprev
            g=CQ(2,-1);row=points(CQ(3),g,rk);w=row[2]-2*row[1]+row[0]
            assert rk.conj()*w/(rk-1).norm2()==-g
            checks['curvature_transport']+=2
        # Exact errors at a conservative budget; four independently signed errors.
        R=Q(3,2);g=CQ(R);c=CQ(Q(1,7),Q(-2,9));base=points(c,g,rho)
        t2=(rho-1).norm2();eps=R*t2/128;u=Q(1,128)
        for mask in range(16):
            noises=[CQ(eps if mask>>j&1 else -eps) for j in range(4)]
            noisy=tuple(p+v for p,v in zip(base,noises[:3]));est=calibrate(noisy)
            assert (est['gain']-g).norm2()<=(14*eps/t2)**2
            assert (est['center']-c).norm2()<=(18*eps/t2)**2
            z=rational_rotation(Q(3,7));Y=c+g*z+noises[3]
            zhat=(Y-est['center'])/est['gain']
            assert (zhat-z).norm2()<=(48*u)**2
            checks['noise']+=3
    game,category=belief_adapter()
    assert game.rank()==3
    assert game.goal(game.root) is None
    current=game.root
    for step in range(3):
        branches=game.options(current)['read']
        if step<2:assert len(branches)==1
        else:assert len(branches)==4
        current=branches[0][1]
    assert game.goal(current)=='0'
    assert {state for _,state in current}=={game.field.count-1}
    checks['belief']=6
    return {'status':'EXACT-FINITE','checks':checks,'total_checks':sum(checks.values()),
            'belief_rank':game.rank(),'history_objects':len(category.objects),
            'scope':'Exact arithmetic validates finite instances; paper proves universal stated lemmas.',
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
