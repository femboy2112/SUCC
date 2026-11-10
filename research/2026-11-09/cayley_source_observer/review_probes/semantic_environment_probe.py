"""Preserved independent environment-semantics review probe.

The generated-term, budget, omega and cofinality checks are copied from the
executed inline review. The final domain observation is explicitly updated
for the subsequently hardened SuccState API: float states must now fail.
This is a rerun, not a purported recovered earlier-run log.
"""
from fractions import Fraction as Q
from random import Random

from observational_succ import c_monoid_succ_embedding as cm
from observational_succ import omega_trace_interpreter as om
from observational_succ import scott_cofinal_schedule as sc

if not __debug__:
    raise RuntimeError("This review probe must run with assertions enabled")

rng = Random(271828)
B = 'B'
F = lambda a, b: ('F', a, b)
P = lambda a, b: ('P', a, b)
constants = {
    'zero': (B, 0), 'one': (B, 1),
    'inc': (F(B, B), lambda x: x+1),
    'twice': (F(B, B), lambda x: 2*x),
}


def gen(ty, ctx, depth):
    leaves = [cm.V(i) for i, t in enumerate(ctx) if t == ty] + [
        cm.CONST(n) for n, (t, v) in constants.items() if t == ty]
    if leaves and (depth <= 0 or rng.randrange(3) == 0):
        return rng.choice(leaves)
    if depth > 0 and rng.randrange(3) == 0:
        a = rng.choice((B, F(B, B), P(B, B)))
        return cm.APP(gen(F(a, ty), ctx, depth-1), gen(a, ctx, depth-1))
    if ty[0] == 'F' if isinstance(ty, tuple) else False:
        return cm.ABS(gen(ty[2], (ty[1],)+ctx, max(0, depth-1)))
    if ty[0] == 'P' if isinstance(ty, tuple) else False:
        return cm.PAIR(gen(ty[1], ctx, max(0, depth-1)),
                       gen(ty[2], ctx, max(0, depth-1)))
    if depth > 0:
        side = rng.randrange(2)
        pair = cm.PAIR(gen(B, ctx, depth-1), gen(B, ctx, depth-1))
        return cm.FST(pair) if side == 0 else cm.SND(pair)
    return cm.CONST('zero')


def ev(t, env):
    if t.tag == 'VAR':
        return env[t.idx]
    if t.tag == 'CONST':
        return constants[t.name][1]
    if t.tag == 'ABS':
        return lambda x: ev(t.body, (x,)+env)
    if t.tag == 'APP':
        return ev(t.f, env)(ev(t.a, env))
    if t.tag == 'PAIR':
        return ev(t.f, env), ev(t.a, env)
    if t.tag == 'FST':
        return ev(t.f, env)[0]
    if t.tag == 'SND':
        return ev(t.f, env)[1]
    raise AssertionError(t)


def values(ty):
    if ty == B:
        return -2, 0, 3
    if ty[0] == 'P':
        return tuple((x, y) for x in values(ty[1]) for y in values(ty[2]))
    if ty == F(B, B):
        return lambda x: x, lambda x: x+2, lambda x: -x
    raise AssertionError(ty)


def agree(a, b, ty):
    if ty == B:
        return a == b
    if ty[0] == 'P':
        return agree(a[0], b[0], ty[1]) and agree(a[1], b[1], ty[2])
    return all(agree(a(x), b(x), ty[2]) for x in values(ty[1]))


ctx = (B, F(B, B), B)
envs = ((-2, lambda x: x+1, 3), (5, lambda x: 2*x, 0))
count = 0
for _ in range(400):
    ty = rng.choice((B, F(B, B), P(B, B)))
    aty = rng.choice((B, F(B, B), P(B, B)))
    body = gen(ty, (aty,)+ctx, 3)
    arg = gen(aty, ctx, 3)
    redex = cm.APP(cm.ABS(body), arg)
    contracted = cm.beta_redex(redex)
    normal = cm.norm(redex, limit=20000)
    for env in envs:
        assert agree(ev(redex, env), ev(contracted, env), ty)
        assert agree(ev(redex, env), ev(normal, env), ty)
        count += 1

for size in range(1, 50):
    t = cm.CONST('zero')
    for _ in range(size):
        t = cm.APP(cm.ID, t)
    try:
        cm.norm(t, limit=size-1)
    except RuntimeError:
        pass
    else:
        raise AssertionError(('underbudget', size))
    assert cm.norm(t, limit=size) == cm.CONST('zero')


def paths(t, p=()):
    if t.tag == 'APP':
        return ((p,) if t.f.tag == 'ABS' else ()) + paths(t.f, p+('f',)) \
            + paths(t.a, p+('a',))
    if t.tag == 'ABS':
        return paths(t.body, p+('body',))
    return ()


for k in range(2, 14):
    for m in range(1, 16):
        t = om.Term(k, m)
        assert paths(t.syntax()) == t.redex_addresses()

cofinal_cases = 0
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                s = sc.AffineSchedule(a, b, c, d)
                assert sc.is_cofinal_schedule(s) == (b > 0 and d > 0)
                for N in range(6):
                    for L in range(6):
                        reachable = (b > 0 or a >= N) and (d > 0 or c >= L)
                        try:
                            k = s.dominates_after(N, L)
                        except ValueError:
                            assert not reachable
                        else:
                            assert reachable
                            n, l = s.at(k)
                            assert n >= N and l >= L
                            if k:
                                n, l = s.at(k-1)
                                assert n < N or l < L
                        cofinal_cases += 1

print({'semantic_environment_comparisons': count, 'minimal_budget_chains': 49,
       'omega_ast_holdouts': 180, 'affine_target_cases': cofinal_cases,
       'status': 'PASS'})

# Explicit change from the historical review: the root repaired this boundary.
try:
    cm.SuccState(0, 0.1)
except (TypeError, ValueError):
    float_rejected = True
else:
    float_rejected = False
assert float_rejected
print({'source_state_float_rejected_after_hardening': float_rejected,
       'non_source_admissible_but_cofinal': sc.AffineSchedule(0, 2, 0, 1).at(1)})
