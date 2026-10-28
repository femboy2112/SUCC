#!/usr/bin/env python3
"""Separate SymPy calculation of mixed-clock and Hopf curvature formulas.

This is a second implementation, not an independent human witness.
"""
import sympy as s
n=s.symbols('n',integer=True,positive=True)
for p in (2,3,5,7,11):
    D=1/n-s.Add(*(1/(p*n+j) for j in range(p)))
    expected=s.Add(*(s.Rational(j,1)/(p*n*(p*n+j)) for j in range(1,p)))
    assert s.factor(D-expected)==0
    leading=s.limit(n**2*D,n,s.oo)
    assert leading==s.Rational(p-1,2*p)

# Independently reconstruct right Hopf connection A=Im(bar x dx)/(1+|x|²)
# on a two-plane x=s*v+t*w with source v=2, w=1+i.
t,u=s.symbols('t u',real=True)
# quaternion product in components is not imported from local source module.
def qmul(a,b):
    aa,bb,cc,dd=a;ee,ff,gg,hh=b
    return (aa*ee-bb*ff-cc*gg-dd*hh,
            aa*ff+bb*ee+cc*hh-dd*gg,
            aa*gg-bb*hh+cc*ee+dd*ff,
            aa*hh+bb*gg-cc*ff+dd*ee)
def qconj(a):return (a[0],-a[1],-a[2],-a[3])
v=(s.Integer(2),s.Integer(0),s.Integer(0),s.Integer(0))
w=(s.Integer(1),s.Integer(1),s.Integer(0),s.Integer(0))
x=tuple(t*v[i]+u*w[i] for i in range(4))
D=1+sum(y*y for y in x)
A_t=qmul(qconj(x),v)
A_u=qmul(qconj(x),w)
A_t=tuple(s.factor(y/D) for y in A_t[1:]);A_u=tuple(s.factor(y/D) for y in A_u[1:])
curvature=tuple(s.diff(A_u[i],t).subs({t:0,u:0})-s.diff(A_t[i],u).subs({t:0,u:0}) for i in range(3))
assert curvature==(4,0,0),curvature
# At origin A=0 so [A_t,A_u]=0, and dA is full F.
print('PASS independent SymPy: mixed braid n^-2 limits and source-plane Hopf F_0=4i')

# Independent Hamilton-coordinate calculation of the *source-chiral* square.
# From Main XIII: b=2, Tb=1+i, JTb=j-k, Jb=2j.
# The overlap product is a Bargmann/Pancharatnam loop, not a GR holonomy.
vertices=[(s.Integer(2),0,0,0),(s.Integer(1),s.Integer(1),0,0),
          (0,0,s.Integer(1),-s.Integer(1)),(0,0,s.Integer(2),0)]
def qadd(a,b):return tuple(a[i]+b[i] for i in range(4))
W=(s.Integer(1),0,0,0)
for j in range(4):
    L=qadd((s.Integer(1),0,0,0),qmul(qconj(vertices[j]),vertices[(j+1)%4]))
    W=qmul(W,L)
assert W==(109,-40,-28,-10),W
assert sum(z*z for z in W)==14365
print('PASS independent SymPy source T/J commuting square: exact quaternionic overlap (109,-40,-28,-10)')
