"""Exact Gaussian/Machin Pade controls. No numerical or all-scale inference."""
from fractions import Fraction as F
from math import comb
import json
class G:
 def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
 def __add__(self,o):
  if not isinstance(o,G):o=G(o)
  return G(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return G(-self.a,-self.b)
 def __sub__(self,o):return self+-o
 def __mul__(self,o):
  if not isinstance(o,G):o=G(o)
  return G(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  if not isinstance(o,G):o=G(o)
  d=o.a*o.a+o.b*o.b
  return self*G(o.a/d,-o.b/d)
 def __pow__(self,n):
  if n<0:return G(1)/(self**(-n))
  z=G(1);t=self
  while n:
   if n&1:z=z*t
   t=t*t;n//=2
  return z
 def __eq__(self,o):return self.a==o.a and self.b==o.b
 def conj(self):return G(self.a,-self.b)
 def norm(self):return self.a*self.a+self.b*self.b

def v2(x):
 x=F(x)
 if not x:return None
 def vi(n):
  n=abs(n);return (n&-n).bit_length()-1
 return vi(x.numerator)-vi(x.denominator)
def vg(z):return F(v2(z.norm()),2)
def coeffs(n):
 Q=[F(comb(n,k)*comb(2*n-k,n)) for k in range(n+1)]
 P=[F(0)] + [sum(Q[k]*F((-1)**(m-k+1),m-k) for k in range(m)) for m in range(1,n+1)]
 return P,Q
def ev(P,z):
 out=G()
 for c in P[::-1]:out=out*z+c
 return out

def pade(n,q):
 z=G(0,2)/G(q,-1);P,Q=coeffs(n)
 return ev(P,z)/ev(Q,z),ev(Q,z)

def atan_interval(q,terms):
 s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),F())
 next_term=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
 return min(s,s+next_term),max(s,s+next_term)
def pi_interval(terms):
 a,b=atan_interval(5,terms);c,d=atan_interval(239,terms)
 return 16*a-4*d,16*b-4*c

i=G(0,1);alpha=lambda q:G(q,1)/G(q,-1)
assert alpha(5)**4/alpha(239)==i
rows=[];counts={'pade_order':0,'denominator_valuation':0,'machin_valuation':0,'real_interval':0,'mutations':0}
for n in range(1,21):
 P,Q=coeffs(n)
 for m in range(n+1,2*n+1):
  assert sum(Q[k]*F((-1)**(m-k+1),m-k) for k in range(n+1))==0
  counts['pade_order']+=1
 for j in range(6):
  m=2*n+1+j
  a=sum(Q[k]*F((-1)**(m-k+1),m-k) for k in range(n+1))
  b=F((-1)**j*comb(n+j,j),(2*n+j+1)*comb(2*n+j,n))
  assert a==b;counts['pade_order']+=1
for n in [4,8,16,32,64]:
 for q in [3,5,7,17,239,1001]:
  _,Q=pade(n,q);assert vg(Q)==1;counts['denominator_valuation']+=1
 p5,Q5=pade(n,5);p239,Q239=pade(n,239)
 B=2*(4*p5.b-p239.b)
 # GP-02: n=2^k, so the exact proved integer lower bound is n-2k-4.
 bound=n-2*(n.bit_length()-1)-4
 assert v2(B)>=bound;counts['machin_valuation']+=1
 lo,hi=pi_interval(2*n+10)
 # Use simplified proven Archimedean bound.
 upper=F(16,(2*n+1)*5**(2*n+1))+F(4,(2*n+1)*239**(2*n+1))
 assert max(abs(lo-B),abs(hi-B))<upper;counts['real_interval']+=1
 rows.append({'n':n,'v2_B':v2(B),'safe_theorem_lower':bound,'B_numerator_bits':B.numerator.bit_length(),'B_denominator_bits':B.denominator.bit_length(),'pi_error_upper':str(upper)})
# Non-power-of-two n is not covered by exact denominator lemma.
assert vg(pade(3,5)[1])!=1;counts['mutations']+=1
# An actual out-of-scope positive tilt exists at n=3, but its primitive
# integer-normalized error is >1 and RDT-02(c) is therefore silent.
l5,_=pade(3,5);l239,_=pade(3,239)
b3=2*(4*l5.b-l239.b)
assert b3==F(1072231967,341301560) and v2(b3)==-3
pi_lo,pi_hi=pi_interval(16)
assert b3.numerator-b3.denominator*pi_hi>1493
assert b3.numerator-b3.denominator*pi_lo<1494
counts['mutations']+=1
# Corrupt Machin coefficient destroys torsion identity.
assert alpha(5)**3/alpha(239)!=i;counts['mutations']+=1
holdouts=[]
for n,q in [(128,31),(128,257),(256,3)]:
 _,Q=pade(n,q)
 assert vg(Q)==1
 holdouts.append({'n':n,'q':q,'denominator_valuation':str(vg(Q))})
print(json.dumps({'counts':counts,'fresh_denominator_holdouts':holdouts,'rows':rows,'mutation_denominator_n3_q5':str(vg(pade(3,5)[1])),'out_of_scope_tilt':{'n':3,'b':str(b3),'v2_b':v2(b3),'primitive_error_interval':[1493,1494]}},indent=2))
