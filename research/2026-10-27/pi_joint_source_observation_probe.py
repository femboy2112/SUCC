"""Independent exact audit of joint BBP numerator/denominator collision laws."""
from collections import Counter
from fractions import Fraction
import json

def add(*polys):
    out=[Fraction(0)]*max(map(len,polys))
    for p in polys:
        for i,c in enumerate(p):out[i]+=c
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def scale(p,c):return [c*v for v in p]
def mul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return add(out)
def compose(p,q):
    out=[Fraction(0)]
    for c in p[::-1]:out=add(mul(out,q),[c])
    return out

AA=[16,-89,120];DD=[21,-206,712,-1024,512]
HH=add(scale(AA,930),[-1243]);tt=[-89,240]
assert add(scale(DD,3375),scale(mul(AA,AA),-120),scale(AA,-2746),[3781],scale(mul([0,1],HH),8))==[0]
assert add(scale(DD,50625),scale(compose(DD,[Fraction(89,120),-1]),-50625),mul(tt,HH))==[0]
assert add(scale(HH,16),scale(mul(tt,tt),-31),[27359])==[0]
assert 27359==109*251

def A(x):return 120*x*x-89*x+16
def D(x):return (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
def H(x):return 930*A(x)-1243

def expected(p,L):
    q=p**L
    if p in [109,251]:return q if L==1 else q+(p-1)*p**(L-1)
    if p==31:return q
    square=pow((27359*pow(31,-1,p))%p,(p-1)//2,p)==1
    return q+2 if square else q

def count_collisions(keys):return sum(c*c for c in Counter(keys).values())

rows=[]
for p,Lmax in [(7,4),(11,3),(13,3),(17,2),(19,2),(23,2),(29,2),(31,3),(37,2),(41,2),(43,2),(109,2),(251,2)]:
    for L in range(1,Lmax+1):
        q=p**L
        counts=Counter((A(x)%q,D(x)%q)for x in range(q))
        actual=sum(c*c for c in counts.values())
        pred=expected(p,L)
        assert actual==pred,(p,L,actual,pred)
        if p in [109,251] and L>=2:
            assert sum(c==p for c in counts.values())==p**(L-2)
            assert all(c in [1,p]for c in counts.values())
        rows.append({'p':p,'L':L,'actual':actual,'predicted':pred})

shift_rows=[]
for p in [7,11,31,109]:
    for L in [1,2,3] if p in [7,11] else [1,2]:
        q=p**L
        for shift in [0,1,2,p,p*p,-p]:
            ss=shift;b=0
            if ss==0:b=L
            else:
                while b<L and ss%p==0:ss//=p;b+=1
            actual=count_collisions((A(x)%q,A(x+shift)%q)for x in range(q))
            pred=q+b*(p-1)*p**(L-1)
            assert actual==pred,(p,L,shift,actual,pred)
            shift_rows.append({'p':p,'L':L,'shift':shift,'actual':actual,'predicted':pred})

# Calibrated false claims: generic formula cannot be extended to exceptional
# primes, and a shift divisible by p does not retain one-step injectivity.
assert expected(109,2)>109**2+2
assert expected(251,2)>251**2+2
assert count_collisions((A(x)%49,A(x+7)%49)for x in range(49))>49
print(json.dumps({'status':'all exact algebra and collision checks passed','joint_ad':rows,'shifted_numerator':shift_rows},indent=2))
