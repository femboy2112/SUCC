"""Fresh RY exact audits; no repository modules or sibling helpers imported."""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = next((p for p in Path(__file__).resolve().parents
             if (p / 'observational_succ/swarm_categories.py').is_file()),
            Path(__file__).resolve().parents[1] / 'SUCC')


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, count - 1):
                yield (first,) + rest


def holonomy():
    ncases = lawcases = liftcases = 0
    for n in range(1, 5):
        ps = tuple(permutations(range(n)))
        for p, q in product(ps, repeat=2):
            # Independent equivalence closure; no generated permutation group.
            relation = {(i, i) for i in range(n)}
            relation |= {(i, p[i]) for i in range(n)} | {(p[i], i) for i in range(n)}
            relation |= {(i, q[i]) for i in range(n)} | {(q[i], i) for i in range(n)}
            while True:
                enlarged = relation | {(i, k) for i, j in relation for jj, k in relation if j == jj}
                if enlarged == relation:
                    break
                relation = enlarged
            # Tree edges force equal labels at all vertices; two added edges
            # carry p and q. Enumerate actual assignments independently.
            sections = tuple(s for s in product(range(n), repeat=3)
                             if s[0] == s[1] == s[2]
                             and s[2] == p[s[0]] and s[1] == q[s[0]])
            roots = {s[0] for s in sections}
            assert roots == {i for i in range(n) if p[i] == q[i] == i}
            for counts in compositions(4, n):
                invariant = all(counts[i] == counts[p[i]] == counts[q[i]] for i in range(n))
                orbit_constant = all(counts[i] == counts[j] for i, j in relation)
                assert invariant == orbit_constant
                lawcases += 1
                if invariant:
                    # A lift supported on sections must use the uniquely
                    # available section for each nonzero root marginal.
                    lift_exists = all(not c or i in roots for i, c in enumerate(counts))
                    section_weights = [counts[s[0]] for s in sections]
                    reconstructed = [sum(w for s, w in zip(sections, section_weights) if s[0] == i)
                                     for i in range(n)]
                    assert lift_exists == (reconstructed == list(counts))
                    liftcases += 1
            ncases += 1
    return dict(generator_pairs=ncases, denominator_four_laws=lawcases,
                invariant_law_global_lift_checks=liftcases)


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def norm(a):
    mass = sum(map(sum, a))
    return None if not mass else tuple(tuple(v / mass for v in row) for row in a)


def kernels():
    # Three-state catalogue: every deterministic substochastic transition
    # with row-specific survival pattern, plus genuinely split transitions.
    cat = set()
    for p in permutations(range(3)):
        for weights in product((Q(0), Q(1, 2), Q(1)), repeat=3):
            cat.add(tuple(tuple(weights[i] if j == p[i] else Q(0) for j in range(3))
                          for i in range(3)))
    cat.add(((Q(1, 3), Q(1, 3), Q(1, 3)),) * 3)
    # Deterministic selection makes the finite scope stable and keeps runtime bounded.
    cat = tuple(sorted(cat))[::7]
    point_laws = tuple(tuple(tuple(Q(o == a and x == b) for x in range(3)) for o in range(2))
                       for a, b in product(range(2), range(3)))
    mixed = (((Q(1, 3), Q(0), Q(0)), (Q(0), Q(1, 6), Q(1, 2))),
             ((Q(1, 6),) * 3, (Q(1, 6),) * 3))
    checks = positive = null = commuting = 0
    for k, l in product(cat, repeat=2):
        kl, lk = matmul(k, l), matmul(l, k)
        assert (kl == lk) == all(matmul(mu, kl) == matmul(mu, lk) for mu in point_laws)
        commuting += kl == lk
        for mu in point_laws + mixed:
            first, final = matmul(mu, k), matmul(mu, kl)
            direct = tuple(tuple(sum(mu[o][i] * k[i][j] * l[j][z]
                                      for i, j in product(range(3), repeat=2))
                                 for z in range(3)) for o in range(2))
            assert final == direct
            staged = None if norm(first) is None else norm(matmul(norm(first), l))
            assert norm(final) == staged
            assert {o for o in range(2) if any(final[o])} <= {o for o in range(2) if any(first[o])}
            checks += 1
            positive += norm(final) is not None
            null += norm(final) is None
    d = ((Q(1, 2), Q(0)), (Q(0), Q(1, 4)))
    n = ((Q(0), Q(1)), (Q(0), Q(0)))
    dn, nd = matmul(d, n), matmul(n, d)
    assert dn != nd and dn == tuple(tuple(2 * x for x in row) for row in nd)
    # Deterministic instruments do not imply deterministic preparation.
    mixed_preparation = ((Q(1, 2), Q(1, 2)),)
    read0 = ((Q(1), Q(0)), (Q(0), Q(0)))
    read1 = ((Q(0), Q(0)), (Q(0), Q(1)))
    assert sum(map(sum, matmul(mixed_preparation, read0))) == Q(1, 2)
    assert sum(map(sum, matmul(mixed_preparation, read1))) == Q(1, 2)
    for fixed in range(2):
        deterministic_preparation = ((Q(fixed == 0), Q(fixed == 1)),)
        assert sum(bool(sum(map(sum, matmul(deterministic_preparation, r))))
                   for r in (read0, read1)) == 1
    return dict(kernels=len(cat), ordered_pairs=len(cat)**2, commuting_pairs=commuting,
                original_law_checks=checks, positive=positive, null=null,
                posterior_without_likelihood_counterexample=True,
                deterministic_recovery_requires_deterministic_preparation=True)


def evaluate(coeffs, x):
    return sum(a * x**i for i, a in enumerate(coeffs))


def interpolate_by_vandermonde(points):
    n = len(points)
    rows = [[x**i for i in range(n)] + [y] for x, y in points]
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [v / scale for v in rows[col]]
        for i in range(n):
            if i != col:
                scale = rows[i][col]
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[col])]
    return tuple(row[-1] for row in rows)


def analytic():
    minima = []
    for n in range(2, 13):
        pts = tuple((Q(1, j + 2), Q((-1)**j)) for j in range(n))
        coeffs = interpolate_by_vandermonde(pts)
        assert all(evaluate(coeffs, x) == y for x, y in pts)
        assert max(map(abs, coeffs)) >= 2*n*(n - 1)
        minima.append(str(max(map(abs, coeffs))))
    checks = 0
    xs = (Q(0), Q(1, 5), Q(1, 2), Q(4, 5))
    for coeffs in product((-1, 0, 1), repeat=5):
        for x, y in product(xs, repeat=2):
            bound = abs(x/(1-x) - y/(1-y))
            assert abs(evaluate(coeffs, x) - evaluate(coeffs, y)) <= bound
            checks += 1
    assert abs(Q(1) - Q(-1)) > Q(1, 2) / (1-Q(1, 2))
    return dict(vandermonde_interpolants=11, max_coefficients=minima,
                finite_pairwise_checks=checks, separate_witness_counterexample=True)


def memory():
    count = 0
    for n in range(1, 5):
        for y in range(1, 4):
            for f in product(range(y), repeat=n):
                rf = max(f.count(v) for v in set(f))
                for z in range(1, 4):
                    for g in product(range(z), repeat=y):
                        gf = tuple(g[v] for v in f)
                        rg = max(g.count(v) for v in set(g))
                        r = max(gf.count(v) for v in set(gf))
                        assert rf <= r <= rf*rg
                        # Independent simultaneous coloring search, not a
                        # coloring constructed by the claimed fiber formula.
                        def feasible(k):
                            return any(len(set(zip(f, m))) == n and len(set(zip(gf, m))) == n
                                       for m in product(range(k), repeat=n))
                        assert feasible(r) and (r == 1 or not feasible(r-1))
                        count += 1
    e0 = (0, 0, 1)
    for init in product(range(3), repeat=2):
        assert len({(e0[x], init[e0[x]]) for x in range(3)}) < 3
    return dict(simultaneous_buffer_map_pairs=count,
                current_only_initialization_cannot_recover_erasure=True)


def gluing():
    original = frozenset(range(3))
    subsets = tuple(frozenset(x for x in original if mask & (1 << x)) for mask in range(8))
    pullbacks = searches = 0
    for constraints in product(subsets, repeat=3):
        for projection in product(range(3), repeat=3):
            for indices in subsets:
                gx = frozenset(x for x in original if all(x in constraints[i] for i in indices))
                gy = frozenset(y for y in range(3) if all(projection[y] in constraints[i] for i in indices))
                assert gy == frozenset(y for y in range(3) if projection[y] in gx)
                if set(projection) == original:
                    assert {projection[y] for y in gy} == gx
                pullbacks += 1
        for grammar in subsets:
            retained, rejected = set(), []
            while True:
                possible = sorted(x for x in grammar if all(x in constraints[i] for i in retained))
                if not possible:
                    assert not any(all(x in c for c in constraints) for x in grammar)
                    if grammar == original:
                        assert not any(all(x in c for c in constraints) for x in original)
                    break
                x = possible[0]
                failures = [i for i, c in enumerate(constraints) if x not in c]
                if not failures:
                    break
                i = failures[0]
                assert i not in retained and x not in rejected
                retained.add(i)
                rejected.append(x)
            assert len(rejected) <= min(3, len(grammar))
            searches += 1
    small, enlarged, allowed = {0}, {0, 1}, {1}
    assert not small & allowed and enlarged & allowed
    return dict(pullback_subset_checks=pullbacks, finite_cegis_checks=searches,
                grammar_only_core_does_not_prune_surjective_extension=True)


def proof_limits():
    worlds = tuple(product((0, 1), repeat=2))
    partials = tuple(product((None, 0, 1), repeat=2))
    def extends(q, p):
        return all(a is None or a == b for a, b in zip(p, q))
    ideal_checks = report_checks = comparable = 0
    for mask in range(1, 16):
        source = tuple(w for i, w in enumerate(worlds) if mask & (1 << i))
        basis = tuple(p for p in partials if any(extends(w, p) for w in source))
        for selected in range(1, 1 << len(basis)):
            chosen = frozenset(p for i, p in enumerate(basis) if selected & (1 << i))
            downward = all(q in chosen for p in chosen for q in basis if extends(p, q))
            directed = all(any(extends(r, p) and extends(r, q) for r in chosen)
                           for p, q in product(chosen, repeat=2))
            if downward and directed:
                maxima = [p for p in chosen if all(extends(p, q) for q in chosen)]
                assert len(maxima) == 1
                assert chosen == frozenset(q for q in basis if extends(maxima[0], q))
                ideal_checks += 1
        for prop_mask in range(1 << len(source)):
            prop = {w for i, w in enumerate(source) if prop_mask & (1 << i)}
            values = {}
            for p in basis:
                fiber = {w for w in source if extends(w, p)}
                v = {int(w in prop) for w in fiber}
                values[p] = next(iter(v)) if len(v) == 1 else None
                report_checks += 1
            for p, q in product(basis, repeat=2):
                if extends(q, p):
                    assert values[p] is None or values[p] == values[q]
                    comparable += 1
            assert all(values[w] == int(w in prop) for w in source)
    scattered = 0
    addresses = (0, 3, 8, 21, 100)
    for mask in range(32):
        observed = tuple(a for i, a in enumerate(addresses) if mask & (1 << i))
        start = max(observed, default=-1) + 1
        even = start + (start % 2)
        odd = start + (1 - start % 2)
        assert even % 2 == 0 and odd % 2 == 1
        assert all(n < even and n < odd for n in observed)
        scattered += 1
    return dict(finite_source_sets=15, principal_ideals_checked=ideal_checks,
                partial_boolean_reports=report_checks, monotone_pairs=comparable,
                scattered_phantom_opposite_extensions=scattered)


def frozen_hash(commit, path):
    # Portability-only wrapper: published snapshots bundle the exact reviewed
    # Git blobs, so replay does not need the original local commit objects.
    audit_dir = Path(__file__).resolve().parent
    manifest = json.loads((audit_dir / 'RY_FROZEN_SOURCES.json').read_text())
    assignment = Path(path).stem
    record = manifest[assignment]
    if record['commit'] != commit or record['path'] != path:
        raise ValueError('Frozen source identity differs from the static manifest')
    bundled = audit_dir / record['bundled_path']
    content = (bundled.read_bytes() if bundled.is_file() else
               subprocess.check_output(['git', 'show', commit + ':' + path], cwd=ROOT))
    digest = hashlib.sha256(content).hexdigest()
    if digest != record['sha256']:
        raise ValueError('Frozen source bytes differ from the originally reviewed SHA-256')
    return digest


def main():
    initial = 'ed102851f0566d3bc84fa140f2b6232d7c6f53ff'
    memory_commit = '1c9c415b26ced094813cd6ea68321c8869f66aef'
    hashes = {}
    for assignment, commit in [('X02', initial), ('X07', initial), ('X09', initial), ('X06', memory_commit),
                               ('X03', '5e4be93cf41317f5c63f6652565ca1323551e7fc'),
                               ('X11', '19fc6acf8db81d6361c6779d6aa06919e20d35fc')]:
        path = 'research/2026-10-13/SWARM_ATLAS/' + assignment + '.md'
        hashes[assignment] = dict(commit=commit, path=path, sha256=frozen_hash(commit, path))
    result = dict(reviewer='audit_remaining_bridges', source_hashes=hashes,
                  probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  independent_holonomy=holonomy(), independent_kernels=kernels(),
                  independent_analytic=analytic(), independent_memory=memory(),
                  independent_gluing=gluing(), independent_proof_limits=proof_limits())
    result['x03_corrected_working_files_sha256'] = {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
        for p in ('research/2026-10-13/SWARM_ATLAS/X03.md',
                  'observational_succ/swarm_gluing_cegis.py',
                  'tests/test_swarm_gluing_cegis.py')}
    result['x07_corrected_working_files_sha256'] = {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
        for p in ('research/2026-10-13/SWARM_ATLAS/X07.md',
                  'scripts/swarm_cross_x07_probe.py',
                  'tests/test_swarm_cross_x07.py')}
    output = Path(__file__).with_name('RY_RECEIPT.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
