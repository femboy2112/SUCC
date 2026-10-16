#!/usr/bin/env python3
"""Regenerate independent source intervals, then replay the two parity caps.

This principal replay uses the prior auditor's Rodrigues implementation, never
producer source or matrix helpers. It is not a new independent source lineage.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
start = time.monotonic()
review = ROOT/'reviews/2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md'
code = review.read_text().split('```python\n', 1)[1].split('\n```', 1)[0]
code = code.split('start=time.monotonic()', 1)[0]
ns = {}
exec(compile(code, str(review)+'::definitions-only', 'exec'), ns)
p = ROOT/'research/2026-10-16/source-schur-final.json'
raw = p.read_bytes()
r = json.loads(raw)
J = 512
tau = F(2, (4*J+1)**2)+F(16, (4*J+1)**3)
cache = {}

def pair(i, j):
    key = tuple(sorted((i, j)))
    if key not in cache:
        rho = ns['rho'](ns['leg'](i), ns['leg'](j))
        assert ns['integ'](rho) == 0
        contact = ns['scale'](ns['CONTACT'], ns['integ']([F()]+rho)/2)
        poles = ns['scale'](ns['add'](ns['epair'](rho,F(-1,2)),ns['epair'](rho,F(1,2))),-4)
        prime = ns['mul'](ns['WEIGHT'],ns['hinge'](rho))
        gamma = ns['sumiv'](ns['scale'](ns['epair'](rho,F(4*k+1,2)),F(4,(4*k+1)**2)) for k in range(J))
        z = ns['sumiv']((contact,poles,prime,gamma))
        error = tau/min(2*i+1,2*j+1)
        cache[key] = z[0]-error,z[1]+error
    return cache[key]

def form(v,w):
    return ns['sumiv'](ns['scale'](pair(i,j),a*b) for i,a in v.items() for j,b in w.items() if a*b and (i+j)%2==0)

def contained(a,b):
    return F(b[0])<=a[0]<=a[1]<=F(b[1])

checks=[]
def check(name, condition):
    checks.append((name,bool(condition)))
    if not condition: raise AssertionError(name)

q={5:F(1),7:F(3,2),11:-F(1,2)}
gq=form(q,q)
primitive=lambda n:[F()]+[a/F(i+1) for i,a in enumerate(ns['leg'](n))]
kq=sum((a*b*ns['integ'](ns['pmul'](primitive(i),primitive(j))) for i,a in q.items() for j,b in q.items()),F())
c=r['source_high_kappa_ceiling']
check('high source enclosure',contained(gq,c['G_energy_interval']))
check('exact K pairing',kq==F(c['K_energy']))
check('Rayleigh division',F(c['every_valid_kappa_upper'])==F(c['G_energy_interval'][1])/kq)
u=r['certified_upper_short']
U=[[F(a) for a in row] for row in u['frozen_rational_U_P5_to_P8_by_P1_to_P4']]
v=[dict([(i+1,F(1))]+[(j+5,-U[j][i]) for j in range(4)]) for i in range(4)]
h=[[form(v[i],v[j]) if (i-j)%2==0 else (F(),F()) for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):check(f'full H interval {i},{j}',contained(h[i][j],u['H_U_full_source_entry_intervals'][i][j]))
boxes=[[tuple(map(F,z)) for z in row] for row in u['H_U_full_source_entry_intervals']]
radius=max(sum(((b-a)/2 for a,b in row),F()) for row in boxes)
upper=[[(a+b)/2+(radius if i==j else 0) for j,(a,b) in enumerate(row)] for i,row in enumerate(boxes)]
check('Loewner majorant',upper==[[F(a) for a in row] for row in u['S0_upper_form']])
for name,ix in (('odd',(0,2)),('even',(1,3))):
    z=u['parity_operator_upper_caps'][name];cap=F(z['operator_eigenvalue_upper'])
    W=[[F(i==j,2*i+3) for j in ix] for i in ix]
    check(name+' metric',W==[[F(a) for a in row] for row in z['low_coordinate_metric']])
    M=[[cap*W[i][j]-upper[ix[i]][ix[j]] for j in range(2)] for i in range(2)]
    check(name+' PSD',M[0][0]>=0 and M[1][1]>=0 and M[0][0]*M[1][1]>=M[0][1]*M[1][0])
check('source receipt stable',raw==p.read_bytes())
out={'status':'PASS','checks':checks,'independent_pair_count':len(cache),
     'source_receipt_sha256':sha256(raw).hexdigest(),'independent_definitions_sha256':sha256(code.encode()).hexdigest(),
     'replay_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'independent_high_interval':gq,'independent_K':kq,'independent_H_intervals':h,
     'argv':sys.argv,'elapsed_seconds':time.monotonic()-start,'original_S0_sign':'OPEN',
     'source_helpers_imported':False,'producer_matrix_helpers_imported':False}
print(json.dumps(out,default=str,indent=2))
