"""Exact golden-address/source oracle plus explicitly numerical chord checks."""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from math import comb
import argparse, hashlib, importlib.util, itertools, json
import mpmath as mp

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OLD=ROOT/'research/2026-10-29/operational_triangle_frontier/operational_triangle.py'
spec=importlib.util.spec_from_file_location('gt_original_triangle',OLD)
source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)

@dataclass(frozen=True)
class Golden:
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def coerce(x):return x if isinstance(x,Golden) else Golden(x)
    def __add__(self,x):
        x=self.coerce(x);return Golden(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Golden(-self.a,-self.b)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x)
        return Golden(self.a*x.a+self.b*x.b,self.a*x.b+self.b*x.a-self.b*x.b)
    __rmul__=__mul__
    def inverse(self):
        norm=self.a*self.a-self.a*self.b-self.b*self.b
        if not norm:raise ZeroDivisionError
        return Golden((self.a-self.b)/norm,-self.b/norm)
    def __truediv__(self,x):return self*self.coerce(x).inverse()
    def __rtruediv__(self,x):return self.coerce(x)*self.inverse()
    def __pow__(self,n):
        if type(n)is not int or n<0:raise ValueError('nonnegative integer exponent')
        x=self;out=Golden(1)
        while n:
            if n&1:out=out*x
            x=x*x;n//=2
        return out
    def sign(self):
        a,b=2*self.a-self.b,self.b
        if not b:return (a>0)-(a<0)
        if b>0:
            if a>=0:return 1
            v=5*b*b-a*a;return (v>0)-(v<0)
        if a<=0:return -1
        v=a*a-5*b*b;return (v>0)-(v<0)
    def __abs__(self):return self if self.sign()>=0 else -self
    def encode(self):return [str(self.a),str(self.b)]
    def numerical(self):
        """Display helper with cancellation guard; exact checks use sign(), never this."""
        height=max(abs(q).bit_length() for q in (self.a.numerator,self.a.denominator,
                                                self.b.numerator,self.b.denominator))
        with mp.workdps(max(mp.mp.dps,8*height//3+30)):
            return (mp.mpf(self.a.numerator)/self.a.denominator+
                    (mp.mpf(self.b.numerator)/self.b.denominator)*(mp.sqrt(5)-1)/2)

ALPHA=Golden(0,1)
ZERO=Golden()

def intervals(depth,k0=0):
    if type(depth)is not int or depth<0 or type(k0)is not int or k0<0:raise ValueError('nonnegative depths')
    row=[('',ZERO,ALPHA**k0)]
    for _ in range(depth):
        nextrow=[]
        for word,left,length in row:
            nextrow.extend(((word+'0',left,ALPHA*length),
                            (word+'1',left+ALPHA*length,ALPHA**2*length)))
        row=nextrow
    return row


def grade_source(a,m):
    """Independent finite differences, not canonical binomial expansion."""
    if F(a)<=0 or type(m)is not int or m<0:raise ValueError('a>0 and m>=0 required')
    diffs=[source.R(F(a)+8*k)/source.R(a) for k in range(m+1)]
    row=[]
    for j in range(m+1):
        row.append(comb(m,j)*diffs[m-j])
        diffs=[x-y for x,y in zip(diffs,diffs[1:])]
    return row


def grade_geometry(m):return [comb(m,j)*ALPHA**(m+j) for j in range(m+1)]

def tv(a,m):
    qs=grade_source(a,m);gs=grade_geometry(m)
    assert sum(qs)==1 and all(q>0 for q in qs)
    assert sum(gs,ZERO)==Golden(1)
    return sum((abs(Golden(q)-g) for q,g in zip(qs,gs)),ZERO)/2


def cayley(p,q=1):
    # (p/q-i)/(p/q+i), exact Gaussian rational coordinates; q=0 is infinity.
    if q==0:return F(1),F(0)
    den=p*p+q*q
    return F(p*p-q*q,den),F(-2*p*q,den)


def exact_run():
    counts={'arc_checks':0,'clock_checks':0,'posterior_checks':0,'grade_routes':0,'farey_checks':0,'tv_bounds':0}
    for k0 in (0,3):
        for m in range(10):
            row=intervals(m,k0)
            right=ZERO
            for word,left,length in row:
                assert left==right
                prefix_ones=0;closed_left=ZERO
                for i,bit in enumerate(word,1):
                    if bit=='1':
                        closed_left+=ALPHA**(k0+i+prefix_ones)
                        prefix_ones+=1
                assert left==closed_left
                assert length.sign()>0
                assert length==ALPHA**(k0+m+word.count('1'))
                right=left+length;counts['arc_checks']+=4
                assert left.a.denominator==left.b.denominator==1
                assert right.a.denominator==right.b.denominator==1
                counts['clock_checks']+=2
            assert right==ALPHA**k0
            assert sum((length for _,_,length in row),ZERO)==ALPHA**k0
            labels=[int(x.b) for _,left,length in row for x in (left,left+length)]
            offset=max(0,-min(labels))
            assert all(offset+j>=0 for j in labels)
            counts['clock_checks']+=len(labels)
    assert intervals(2)[1][1]==ALPHA**2
    assert intervals(2)[2][1]==ALPHA
    for a in (1,9,25):
        for m in range(10):
            qs=grade_source(a,m)
            for j,q in enumerate(qs):
                assert q==source.endpoint_mass(a,m,j);counts['grade_routes']+=1
            if m<9:
                later=grade_source(a,m+1)
                for word,_,_ in intervals(m):
                    j=word.count('1')
                    w=qs[j]/comb(m,j)
                    assert w==later[j]/comb(m+1,j)+later[j+1]/comb(m+1,j+1)
                    counts['posterior_checks']+=1
    fixed_rows=[]
    for m in (64,128,193,257):
        distance=tv(1,m);eta=F(1,8)
        bound=Golden(1)-4*eta/(ALPHA*source.R(1))-F(1,2*m*eta*eta)
        assert (distance-bound).sign()>=0
        assert bound.sign()>0
        counts['tv_bounds']+=1
        fixed_rows.append({'m':m,'a':1,'eta':str(eta),'held_out':m in(193,257),
                           'tv':distance.encode(),'bound':bound.encode()})
    native_rows=[]
    for m in (64,128,193,257):
        a=8*m-7;distance=tv(a,m)
        bound=Golden(1)-4/(m*ALPHA)-2*(1-source.R(a+8)/source.R(a))/(ALPHA**2)
        assert (distance-bound).sign()>=0 and bound.sign()>0
        threshold=next(t for t in range(1,m+1) if (Golden(t)-m*ALPHA**2/2).sign()>0)
        exponential=Golden(1)-2**(threshold-1)*(1-ALPHA**2/2)**m-F(2,3)**threshold*source.R(a-4*m)/source.R(a)
        assert (distance-exponential).sign()>=0 and exponential.sign()>0
        counts['tv_bounds']+=2
        native_rows.append({'m':m,'a':a,'held_out':m in(193,257),'tv':distance.encode(),'bound':bound.encode(),
                            'threshold':threshold,'exponential_bound':exponential.encode()})
    first=source.R(9)/source.R(1);reset=source.R(17)/source.R(9)
    assert first!=reset
    f0,f1=0,1
    for k in range(1,35):
        f0,f1=f1,f0+f1
        if k>=2:
            p,q=f0,f1  # F_k,F_(k+1)
            prev=q-p
            assert abs(prev*q-p*p)==1
            med=(prev+p,p+q)
            assert med==(q,p+q)
            points=[cayley(prev,p),cayley(p,q),cayley(*med)]
            assert len(set(points))==3
            assert all(x*x+y*y==1 for x,y in points)
            counts['farey_checks']+=4
    assert cayley(0)!=cayley(1)
    for n in range(1,33):
        direct=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
        assert source.r(n)==direct
        assert source.R(8*n-7)==direct
    return {'status':'PASS','authority':'exact Fraction and Q(alpha) finite certificates',
            'counts':counts,'fixed_prior_tv':fixed_rows,'native_finite_tv':native_rows,
            'moving_prior_counterexample':{'initial_zero_mu1':str(first),'initial_zero_mu9':str(reset)},
            'source_hash':hashlib.sha256(OLD.read_bytes()).hexdigest(),
            'oracle_hash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def numerical_run():
    rows=[]
    with mp.workdps(100):
        alpha=(mp.sqrt(5)-1)/2
        for k in (2,3,6,13,27,41):
            for R in (mp.mpf(1),mp.mpf(3)/7):
                a,b,c=alpha**(k+1),alpha**(k+2),alpha**k
                vertices=[R*mp.exp(2j*mp.pi*x) for x in (0,a,c)]
                sides=[abs(vertices[1]-vertices[0]),abs(vertices[2]-vertices[1]),abs(vertices[2]-vertices[0])]
                defect=sides[0]+sides[1]-sides[2]
                formula=8*R*mp.sin(mp.pi*a/2)*mp.sin(mp.pi*b/2)*mp.sin(mp.pi*c/2)
                u,v=vertices[1]-vertices[0],vertices[2]-vertices[0]
                area=abs(u.real*v.imag-u.imag*v.real)/2
                area_formula=2*R*R*mp.sin(mp.pi*a)*mp.sin(mp.pi*b)*mp.sin(mp.pi*c)
                assert abs(defect/formula-1)<mp.mpf('1e-75')
                assert abs(area/area_formula-1)<mp.mpf('1e-75')
                ratio=mp.fprod(mp.sin(alpha*x)/mp.sin(x) for x in (mp.pi*a/2,mp.pi*b/2,mp.pi*c/2))
                upper=alpha**3/mp.fprod(1-x*x/6 for x in (mp.pi*a/2,mp.pi*b/2,mp.pi*c/2))
                assert alpha**3<ratio<upper
                assert abs(4*area/mp.fprod(sides)-1/R)<mp.mpf('1e-75')
                rows.append({'k':k,'R':mp.nstr(R,25),'held_out':k in(13,27,41),
                             'defect':mp.nstr(defect,35),'area':mp.nstr(area,35),
                             'ratio':mp.nstr(ratio,35),'alpha_cubed':mp.nstr(alpha**3,35)})
    return {'status':'PASS','authority':'100-digit numerical corroboration, not interval certification',
            'rows':rows,'oracle_hash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--numerical',action='store_true');args=parser.parse_args()
    result=numerical_run() if args.numerical else exact_run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
