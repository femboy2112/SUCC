#!/usr/bin/env python3
"""Bounded candidate search; ONLY the exact uniform checker certifies a result.

Searches finite phase menus and velocities. A solver status is neither a
general obstruction nor an exact infeasibility certificate. No finite-time
sampling is used: candidate constraints come from rational tangent intervals.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from math import gcd
import pathlib
import sys
import time

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.lonely_runner_uniform import (
    AffineRunner, UniformRule, resonance_interval, check_local_uniform,responsible_residues,
)


def solve(limit,max_odd,seconds,gain=1):
    import numpy as np
    from scipy.optimize import milp, Bounds, LinearConstraint
    from scipy.sparse import coo_matrix
    evens=tuple(range(4,limit+1,4))
    candidates=[]
    for v in evens:
        for alpha in (F(0),F(1,2)):
            for beta2 in range(-4,5):
                candidates.append(AffineRunner(v,alpha,F(beta2,2)))
    for v in range(1,max_odd+1,2):
        for alpha in (F(1,4),F(3,4)):
            for beta4 in (-1,0,1):
                candidates.append(AffineRunner(v,alpha,F(beta4,4)))
    cover_sets=set()
    for q in evens:
        # In this declared menu, resonance depends only on k mod 4 among
        # responsible units. Both classes occur by CRT; full checker later
        # enumerates all actual residues without this optimization.
        representatives=(1,next(k for k in range(3,q,4) if gcd(k,q//2)==1))
        for k in representatives:
            intervals=[]
            endpoints={F(-1),F(1)}
            for index,candidate in enumerate(candidates):
                interval=resonance_interval(q,k,candidate)
                if interval is not None:
                    intervals.append((index,*interval)); endpoints.update(interval)
            ordered=sorted(endpoints)
            probes=ordered+[(a+b)/2 for a,b in zip(ordered,ordered[1:])]
            for point in probes:
                cover=frozenset(i for i,a,b in intervals if a<=point<=b)
                assert cover
                cover_sets.add(cover)
    rows=[];cols=[];data=[];lower=[];upper=[]
    for cover in sorted(cover_sets,key=lambda x:tuple(sorted(x))):
        row=len(lower); lower.append(1);upper.append(np.inf)
        for index in cover: rows.append(row);cols.append(index);data.append(1)
    for v in sorted({c.velocity for c in candidates}):
        row=len(lower);lower.append(0);upper.append(1)
        for i,c in enumerate(candidates):
            if c.velocity==v: rows.append(row);cols.append(i);data.append(1)
    row=len(lower);lower.append(0);upper.append(len(evens)-gain)
    for i in range(len(candidates)): rows.append(row);cols.append(i);data.append(1)
    matrix=coo_matrix((np.array(data,dtype=float),(rows,cols)),
                      shape=(len(lower),len(candidates))).tocsc()
    started=time.monotonic()
    result=milp(np.ones(len(candidates)),integrality=np.ones(len(candidates)),
                bounds=Bounds(0,1),constraints=LinearConstraint(matrix,lower,upper),
                options={'time_limit':seconds,'mip_rel_gap':0,'presolve':True})
    report={'schema':'SUCC-local-uniform-finite-menu-search-v1','limit':limit,'required_gain':gain,
            'max_odd':max_odd,'seconds_limit':seconds,'elapsed_seconds':time.monotonic()-started,
            'phase_menu':{'even_alpha':['0','1/2'],'even_beta':'-2..2 in half steps',
                          'odd_alpha':['1/4','3/4'],'odd_beta':['-1/4','0','1/4']},
            'candidates':len(candidates),'constraints':len(lower),'solver_status':int(result.status),
            'solver_message':result.message,'claim_boundary':'finite menu; solver status not a general or exact infeasibility proof'}
    if result.x is not None:
        selected=[c for c,x in zip(candidates,result.x) if x>.5]
        selected_even={c.velocity:c for c in selected if c.velocity%2==0}
        rule=UniformRule(tuple(q for q in evens if q not in selected_even),
                         tuple(selected_even.values()),tuple(c for c in selected if c.velocity%2))
        certificate=check_local_uniform(rule)
        report['candidate']={'removed':rule.removed,
            'rephased':[(c.velocity,str(c.alpha),str(c.beta)) for c in rule.rephased],
            'added':[(c.velocity,str(c.alpha),str(c.beta)) for c in rule.added],
            'gain':rule.gain,'exact_local_uniform':certificate['local_uniform']}
        if not certificate['local_uniform']: report['candidate']['gap']=certificate['gap']
    return report


def solve_continuous(limit,max_odd,seconds,prime_factors,gain=1,extended=False):
    """Exact SMT search with continuous beta, restricted declared alpha menu.

    Interval chaining uses rational linear inequalities; no beta grid is
    imposed. Unknown or UNSAT is only a finite-support/menu search result.
    """
    import z3
    def smooth(n):
        for p in prime_factors:
            while n%p==0: n//=p
        return n==1
    evens=tuple(v for v in range(4,limit+1,4) if smooth(v))
    odds=tuple(v for v in range(1,max_odd+1,2) if smooth(v))
    even_alpha=(F(0),F(1,2))
    odd_alpha=(F(1,4),F(3,4))
    if extended:
        even_alpha=tuple(sorted(set(even_alpha+(F(1,4),F(3,4),F(1,3),F(2,3),F(1,6),F(5,6)))))
        odd_alpha=tuple(sorted(set(odd_alpha+tuple(F(k,8) for k in (1,3,5,7))+(F(1,3),F(2,3)))))
    choices=[(v,a) for v in evens for a in even_alpha]+[(v,a) for v in odds for a in odd_alpha]
    selected=[z3.Bool(f'use_{v}_{a.numerator}_{a.denominator}') for v,a in choices]
    beta={v:z3.Real(f'beta_{v}') for v in evens+odds}
    solver=z3.Solver();solver.set(timeout=int(seconds*1000))
    def rational(x):return z3.RealVal(str(x))
    for v in evens+odds:
        solver.add(z3.PbLe([(selected[i],1) for i,(w,_) in enumerate(choices) if w==v],1))
        bound=F(1)+F(v,min(evens));solver.add(beta[v]>=rational(-bound),beta[v]<=rational(bound))
    solver.add(z3.PbLe([(x,1) for x in selected],len(evens)-gain))
    cell_count=0
    for q in evens:
        signatures={}
        for k in responsible_residues(q):
            signature=tuple(i for i,(v,a) in enumerate(choices) if (F(v*k,q)+a).denominator==1)
            signatures.setdefault(signature,k)
        for signature,k in signatures.items():
            intervals=[]
            for i in signature:
                v,a=choices[i]
                left=rational(F(q,v))*(-1-beta[v])
                right=rational(F(q,v))*(1-beta[v])
                intervals.append((selected[i],left,right))
            solver.add(z3.Or([z3.And(use,left<=-1,right>=-1) for use,left,right in intervals]))
            for use,left,right in intervals:
                extension=z3.Or([z3.And(other,a<=right,b>right) for other,a,b in intervals])
                solver.add(z3.Implies(z3.And(use,right>=-1,right<1),extension))
            cell_count+=1
    started=time.monotonic();status=solver.check()
    report={'schema':'SUCC-local-uniform-continuous-beta-search-v1','limit':limit,
        'max_odd':max_odd,'prime_factors':prime_factors,'active_evens':evens,'odd_candidates':odds,
        'seconds_limit':seconds,'elapsed_seconds':time.monotonic()-started,
        'alpha_menu':{'even':list(map(str,even_alpha)),'odd':list(map(str,odd_alpha))},
        'required_gain':gain,
        'beta_domain':'all real beta, without grid, bounded without loss by 1+v/min(active_evens)',
        'cells':cell_count,'solver_status':str(status),
        'claim_boundary':'fixed support and alpha menu only; no general rule nonexistence conclusion'}
    if status==z3.unknown:report['solver_reason']=solver.reason_unknown()
    if status==z3.sat:
        model=solver.model();runners=[]
        for use,(v,a) in zip(selected,choices):
            if z3.is_true(model.eval(use)):
                b=model.eval(beta[v]);b=F(b.numerator_as_long(),b.denominator_as_long())
                runners.append(AffineRunner(v,a,b))
        seen={r.velocity for r in runners if r.velocity%2==0}
        rule=UniformRule(tuple(q for q in evens if q not in seen),
            tuple(r for r in runners if r.velocity%2==0),tuple(r for r in runners if r.velocity%2))
        certificate=check_local_uniform(rule)
        report['candidate']={'removed':rule.removed,
            'rephased':[(c.velocity,str(c.alpha),str(c.beta)) for c in rule.rephased],
            'added':[(c.velocity,str(c.alpha),str(c.beta)) for c in rule.added],
            'gain':rule.gain,'exact_local_uniform':certificate['local_uniform']}
        if not certificate['local_uniform']:report['candidate']['gap']=certificate['gap']
    return report


def main():
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=188)
    p.add_argument('--max-odd',type=int,default=135);p.add_argument('--seconds',type=float,default=30)
    p.add_argument('--continuous-beta',action='store_true')
    p.add_argument('--smooth-primes',default='2,3,5')
    p.add_argument('--gain',type=int,default=1);p.add_argument('--extended-phase',action='store_true')
    p.add_argument('--output',type=pathlib.Path);args=p.parse_args()
    if args.limit<4 or args.max_odd<1 or args.gain<1 or not 0<args.seconds<=300:
        p.error('positive bounded search parameters required')
    primes=tuple(int(p) for p in args.smooth_primes.split(','))
    if any(p<2 for p in primes):p.error('smooth factors must be at least two')
    report=(solve_continuous(args.limit,args.max_odd,args.seconds,primes,args.gain,args.extended_phase)
            if args.continuous_beta else solve(args.limit,args.max_odd,args.seconds,args.gain))
    text=json.dumps(report,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')


if __name__=='__main__':main()
