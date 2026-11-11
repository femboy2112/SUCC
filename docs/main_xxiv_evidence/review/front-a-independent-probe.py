from fractions import Fraction as Q
import random
from unittest.mock import patch
from observational_succ import zero_anchored_lambda as z
from observational_succ import zero_anchored_haar as h

rng=random.Random(20261111)
def gen(depth,context=()):
    if depth==0:
        return z.Variable(rng.randrange(len(context))) if context and rng.randrange(2) else z.Literal(Q(rng.randrange(-9,10),rng.randrange(1,10)))
    choice=rng.randrange(5)
    if choice==0:
        return z.Apply(z.Apply(z.Primitive('add'),gen(depth-1,context)),gen(depth-1,context))
    if choice==1:
        return z.Apply(z.Primitive('divide16'),gen(depth-1,context))
    if choice==2:
        return z.Apply(z.Lambda(z.RAT,gen(depth-1,(z.RAT,)+context)),gen(depth-1,context))
    if choice==3:
        return z.Primitive('forcing:'+str(rng.randrange(1,16)))
    return gen(0,context)
def env(term,ctx=()):
    if type(term) is z.Literal: return Q(term.value)
    if type(term) is z.Variable: return ctx[term.index]
    if type(term) is z.Lambda: return lambda v:env(term.body,(v,)+ctx)
    if type(term) is z.Apply: return env(term.function,ctx)(env(term.argument,ctx))
    name=term.name
    if name=='add':return lambda a:lambda b:a+b
    if name=='divide16':return lambda a:a/16
    if name.startswith('forcing:'):
        n=int(name.split(':')[1]);return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    raise AssertionError(name)
for i in range(500):
    term=gen(6)
    expected=env(term)
    program=z.compile_term(term)
    for strategy in ('normal','applicative'):
        receipt=z.run(program,max_steps=10000,strategy=strategy)
        assert receipt.status=='FINITE_REDUCTION_VERIFIED'
        assert receipt.value==expected,(i,strategy,receipt.value,expected)
    blocked=z.run(program,max_steps=0)
    assert blocked.status in ('FINITE_REDUCTION_VERIFIED','UNRESOLVED_BUDGET')
    if blocked.status=='UNRESOLVED_BUDGET':assert blocked.value is None
print('PASS: 500 generated closed typed terms, two reduction strategies, independent environment/polynomial source oracle; exhausted budgets preserve unresolved status')
# A direct independent rational CDF implementation exercises branch seams.
def defect(points,q):
    mass={}
    for k in points:
        x=Q(k,q);mass[x]=mass.get(x,Q())+Q(1,len(points))
        for a in range(16):
            y=Q(a,16)+(16*x%1)/16
            mass[y]=mass.get(y,Q())-Q(1,16*len(points))
    accum=out=previous=Q()
    for x in sorted(mass):
        out+=(x-previous)*abs(accum);accum+=mass[x];previous=x
    assert accum==0
    return out
for _ in range(300):
    q=16**rng.randrange(1,4)
    left=tuple(rng.randrange(q) for _ in range(5))
    right=tuple(rng.randrange(q) for _ in range(5))
    result=h.signed_block_overlap(left,right,q)
    assert result.early==defect(left,q)
    assert result.late==defect(right,q)
    assert result.combined==defect(left+right,q)
    assert result.combined==(result.early+result.late)/2-result.overlap
print('PASS: 300 randomized exact CDF/overlap partitions including branch seams')
