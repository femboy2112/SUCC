"""Independent relation-lattice audit; candidate source is read-only.

The oracle selects the greatest lawful equivalence by exhaustive lattice
enumeration, rather than word enumeration or partition refinement.
"""
from itertools import product
from pathlib import Path
import hashlib, json, random, subprocess, sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--source', type=Path, required=True, help='Checkout of audited commit3490466 before RA-01 fix')
args = parser.parse_args()
SOURCE = args.source.resolve()
sys.path.insert(0, str(SOURCE))
from observational_succ.swarm_categories import (
    FiniteDynamics, stable_refinement, repair_base_change,
    InstrumentArrow, ReportComparison, belief_update, map_belief, quotient,
    CategoryError,
)

def partitions(n):
    result = set()
    for labels in product(range(n), repeat=n):
        first = {}
        result.add(tuple(first.setdefault(x, len(first)) for x in labels))
    return tuple(sorted(result))

def mask(p):
    return sum(1 << (x * len(p) + y) for x in range(len(p))
               for y in range(len(p)) if p[x] == p[y])

def stable(p, t):
    return all(p[x] != p[y] or p[t[x]] == p[t[y]]
               for x in range(len(p)) for y in range(len(p)))

def model(tables, reports=None):
    n = len(tables[0])
    actions = tuple('a'+str(i) for i in range(len(tables)))
    return FiniteDynamics('RA exact source', tuple(reports or (0,)*n),
                          actions, tuple(tables), actions)

counts = {}
first_failure = None
for n in range(1, 5):
    ps = partitions(n)
    ms = tuple(map(mask, ps))
    ts = tuple(product(range(n), repeat=n))
    st = tuple(tuple(stable(p, t) for p in ps) for t in ts)
    refine = tuple(tuple((m & ~r) == 0 for m in ms) for r in ms)
    repairs = []
    for ti, t in enumerate(ts):
        row = []
        for ri, r in enumerate(ps):
            best = max((ei for ei in range(len(ps)) if st[ti][ei] and refine[ri][ei]),
                       key=lambda ei: ms[ei].bit_count())
            assert stable_refinement(model((t,)), r)[0] == ps[best]
            row.append(best)
        repairs.append(tuple(row))
    failures = 0
    exact_pairs = 0
    commuting_pairs = 0
    for ai, a in enumerate(ts):
        for bi, b in enumerate(ts):
            criterion = all(not st[bi][ri] or st[bi][repairs[ai][ri]]
                            for ri in range(len(ps)))
            commute = all(repairs[ai][repairs[bi][ri]] ==
                          repairs[bi][repairs[ai][ri]] for ri in range(len(ps)))
            actual_exact = True
            for ri, r in enumerate(ps):
                joint = max((ei for ei in range(len(ps))
                             if st[ai][ei] and st[bi][ei] and refine[ri][ei]),
                            key=lambda ei: ms[ei].bit_count())
                sequential = repairs[ai][repairs[bi][ri]]
                if sequential != joint:
                    actual_exact = False
                    failures += 1
                    if first_failure is None:
                        first_failure = dict(n=n, initial=r, a=a, b=b,
                                             sequential=ps[sequential], joint=ps[joint])
            assert actual_exact == criterion
            assert not commute or actual_exact
            exact_pairs += actual_exact
            commuting_pairs += commute
    counts[f'n{n}'] = dict(action_pairs=len(ts)**2,
        initial_equivalences=len(ps), pair_relation_cells=len(ts)**2*len(ps),
        failed_relation_cells=failures, exact_action_pairs=exact_pairs,
        commuting_action_pairs=commuting_pairs)
assert first_failure['n'] == 4

# Independent source-map enumeration, arbitrary target equivalences. Reports
# are constant, emphasizing that the true repair equality does not use h.
maps = strict_maps = nonsurjective = noninjective = 0
for f in product(range(3), repeat=2):
    for tx in product(range(2), repeat=2):
        for ty in product(range(3), repeat=3):
            maps += 1
            if not all(f[tx[x]] == ty[f[x]] for x in range(2)):
                continue
            strict_maps += 1
            for p in partitions(3):
                lhs, rhs = repair_base_change(model((tx,)), model((ty,)), f, p)
                assert lhs == rhs
                nonsurjective += len(set(f)) < 3
                noninjective += len(set(f)) < 2
counts['base_change'] = dict(candidate_maps=maps, strict_maps=strict_maps,
    equivalence_cells=strict_maps*5, nonsurjective_cells=nonsurjective,
    noninjective_cells=noninjective)

# All subsets of an origin/current product, including nonsaturated sets.
source = model(((2,2,2), (1,0,2)), (0,0,1))
q = (0,0,1)
target = quotient(source, q)
pairs = tuple(product(range(3), repeat=2))
belief_cells = 0
for bits in range(512):
    belief = frozenset(pair for i, pair in enumerate(pairs) if bits >> i & 1)
    for a in source.actions:
        for o in (0,1):
            raw = frozenset((origin, source.step(current,a))
                            for origin,current in belief if source.reports[current] == o)
            mapped_raw = frozenset((q[x],q[y]) for x,y in raw)
            mapped = frozenset((q[x],q[y]) for x,y in belief)
            abstract = frozenset((origin,target.step(current,a))
                                for origin,current in mapped if target.reports[current] == o)
            assert raw == belief_update(source,belief,a,o)
            assert mapped_raw == abstract
            assert abstract == belief_update(target,map_belief(belief,q),a,o)
            assert {q[x] for x,_ in raw} == {x for x,_ in abstract}
            belief_cells += 1
counts['belief_cells'] = belief_cells

# Nonfactorable original targets and state-dependent action costs are omitted
# hypotheses for any stronger transport claim. They are explicit countermodels
# outside the stated constant-target-on-q-fibers/total-common-action boundary.
target_gate = {'source_reports': [0,0], 'transition': [0,0], 'quotient': [0,0],
               'original_target': [0,1], 'concrete_target_values': [0,1],
               'no_quotient_decoder': True}
assert not any(all(decoder == x for x in (0,1)) for decoder in (0,1))
availability_gate = {'state_dependent_costs': [0,1], 'behavioral_quotient': [0,0],
                     'cost_does_not_factor': True}

# General widths, unused labels, nonsquare carriers and report garblings.
rng = random.Random(781621)
def arrow(dom, cod):
    width = rng.randrange(3)
    alphabet = tuple(product(range(2),repeat=width))
    return InstrumentArrow(dom,cod,tuple(rng.randrange(cod) for _ in range(dom)),
        alphabet, tuple(rng.choice(alphabet) for _ in range(dom)), width)
def garble(before):
    width = rng.randrange(3)
    alphabet = tuple(product(range(2),repeat=width))
    mapping = tuple(rng.randrange(len(alphabet)) for _ in before.alphabet)
    reports = tuple(alphabet[mapping[before.alphabet.index(r)]] for r in before.reports)
    after = InstrumentArrow(before.domain,before.codomain,before.transition,
                            alphabet,reports,width)
    return ReportComparison(before,after,mapping)
for _ in range(500):
    I,J,K = arrow(2,3), arrow(3,1), arrow(1,2)
    p,q,r = garble(I),garble(J),garble(K)
    pp,qq,rr = garble(p.after),garble(q.after),garble(r.after)
    assert I.then(J).then(K) == I.then(J.then(K))
    assert p.horizontal(q).horizontal(r) == p.horizontal(q.horizontal(r))
    assert p.then(pp).horizontal(q.then(qq)) == p.horizontal(q).then(pp.horizontal(qq))
    assert InstrumentArrow.identity(2).then(I) == I
    assert I.then(InstrumentArrow.identity(3)) == I
counts['random_2category_cases'] = 500

# Negative control: non-intertwining report-preserving map must be rejected.
try:
    repair_base_change(model(((0,1),)),model(((0,2,2),)),(0,1),(0,0,1))
except CategoryError:
    mutation_rejected = True
else:
    raise AssertionError('non-intertwining source map accepted')

# API boundary finding: unavailable action is checked only if a state survives.
invalid_action_empty = belief_update(source,frozenset(),'missing',0)
invalid_action_filtered = belief_update(source,frozenset({(0,0)}),'missing',9)
assert invalid_action_empty == invalid_action_filtered == frozenset()

receipt = dict(status='scoped_pass_with_low_api_finding',
    audited_commit=subprocess.check_output(['git','rev-parse','HEAD'],
        cwd=SOURCE,text=True).strip(), counts=counts,
    minimal_mixed_failure=first_failure, target_gate=target_gate,
    availability_gate=availability_gate, mutation_rejected=mutation_rejected,
    invalid_action_returns_empty=True,
    probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(receipt,indent=2))
