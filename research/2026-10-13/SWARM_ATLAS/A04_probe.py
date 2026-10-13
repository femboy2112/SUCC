"""SWM-A04: exact tiny cover/section oracle; no project-module imports.

Conventions: permutations are maps; mul(a,b) means a after b.
Bounds: S3, all 41 two-loop sheet transports through degree three,
all 36 source generator pairs, and all 36 two-vertex frame gauges.
"""
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import platform
import subprocess


def mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inv(a):
    return tuple(a.index(i) for i in range(len(a)))


def generated(gens, degree):
    identity = tuple(range(degree))
    seen, todo = {identity}, [identity]
    for at in todo:
        for gen in gens:
            after = mul(gen, at)
            if after not in seen:
                seen.add(after)
                todo.append(after)
    return frozenset(seen)


def subgroups(group):
    elements = sorted(group)
    identity = tuple(range(len(elements[0])))
    result = []
    for mask in range(1 << len(elements)):
        candidate = frozenset(e for i, e in enumerate(elements) if mask >> i & 1)
        if identity in candidate and all(mul(a, b) in candidate
                                        for a in candidate for b in candidate):
            result.append(candidate)
    return result


def fixed(group, degree=3):
    return tuple(x for x in range(degree) if all(h[x] == x for h in group))


def normal(subgroup, group):
    return all(mul(mul(h, k), inv(h)) in subgroup for h in group for k in subgroup)


def core(subgroup, group):
    return frozenset(k for k in subgroup
                     if all(mul(mul(h, k), inv(h)) in subgroup for h in group))


def sections(source_gens, sheet_gens):
    degree = len(sheet_gens[0])
    return tuple(q for q in product(range(3), repeat=degree)
                 if all(q[sigma[y]] == source[q[y]]
                        for source, sigma in zip(source_gens, sheet_gens)
                        for y in range(degree)))


def connected(gens):
    return len({h[0] for h in generated(gens, len(gens[0]))}) == len(gens[0])


def raw_holonomy(vertices, edges, root):
    """Independent raw path-state enumeration, without tree residuals."""
    adj = {v: [] for v in vertices}
    for u, v, p in edges:
        adj[u].append((v, p))
        adj[v].append((u, inv(p)))
    start = (root, (0, 1, 2))
    seen, todo = {start}, [start]
    for u, transport in todo:
        for v, p in adj[u]:
            state = (v, mul(p, transport))
            if state not in seen:
                seen.add(state)
                todo.append(state)
    return frozenset(p for v, p in seen if v == root)


def run():
    identity = (0, 1, 2)
    a, b = (1, 0, 2), (0, 2, 1)
    group = generated((a, b), 3)
    assert len(group) == 6 and not fixed(group)
    source_gens = (a, b)
    covers = []
    assignment_count = 0
    for degree in (1, 2, 3):
        connected_count = admitting = section_count = 0
        for sheet_gens in product(tuple(permutations(range(degree))), repeat=2):
            assignment_count += 1
            if not connected(sheet_gens):
                continue
            connected_count += 1
            found = sections(source_gens, sheet_gens)
            admitting += bool(found)
            section_count += len(found)
            assert all(len(set(q)) == 3 for q in found)
        covers.append(dict(degree=degree, connected=connected_count,
                           admitting_section=admitting, sections=section_count))
    assert assignment_count == 41
    assert all(x['admitting_section'] == 0 for x in covers[:2])
    assert covers[2]['admitting_section'] > 0

    # The orbit cover uses the very same a,b permutations on its three sheets.
    q = identity
    assert sections(source_gens, source_gens) == (q,)
    decks = tuple(d for d in permutations(range(3))
                  if all(mul(d, g) == mul(g, d) for g in source_gens))
    assert decks == (identity,)
    assert all(q[d[y]] == q[y] for d in decks for y in range(3))
    assert q[0] != q[1]  # Same base vertex, different values: no descent.
    stabilizer = frozenset(h for h in group if h[0] == 0)
    assert stabilizer == frozenset((identity, b))
    assert len(core(stabilizer, group)) == 1
    assert not normal(stabilizer, group)
    assert b != identity and b[q[0]] == q[0]  # Nonflat pulled-back law.

    # Independent finite subgroup oracle for both minimum formulas.
    field_checks = 0
    for gens in product(tuple(permutations(range(3))), repeat=2):
        h = generated(gens, 3)
        subs = subgroups(h)
        orbit_min = min(len({g[x] for g in h}) for x in range(3))
        cores = [core(frozenset(g for g in h if g[x] == x), h) for x in range(3)]
        regular_min = min(len(h) // len(c) for c in cores)
        assert orbit_min == min(len(h) // len(k) for k in subs if fixed(k))
        assert regular_min == min(len(h) // len(k) for k in subs
                                  if normal(k, h) and fixed(k))
        field_checks += 1
    assert field_checks == 36
    s3_subs = subgroups(group)
    s3_normal = [k for k in s3_subs if normal(k, group)]
    assert len(s3_subs) == 6 and len(s3_normal) == 3
    assert min(len(group) // len(k) for k in s3_subs if fixed(k)) == 3
    assert min(len(group) // len(k) for k in s3_normal if fixed(k)) == 6

    # Fresh nonfaithful-orbit control: natural 3-label plus sign 2-label action.
    # A regular double cover admits one section but cannot trivialize S3.
    a5, b5 = a + (4, 3), b + (4, 3)
    mixed_group = generated((a5, b5), 5)
    mixed_subs = subgroups(mixed_group)
    assert len(mixed_group) == 6 and fixed(mixed_group, 5) == ()
    mixed_orbits = sorted({tuple(sorted({h[x] for h in mixed_group}))
                           for x in range(5)})
    mixed_min = min(len(orbit) for orbit in mixed_orbits)
    mixed_regular_min = min(len(mixed_group) // len(k) for k in mixed_subs
                            if normal(k, mixed_group) and fixed(k, 5))
    assert mixed_min == mixed_regular_min == 2
    sign_cover = ((1, 0), (1, 0))
    sign_section = (3, 4)
    assert all(sign_section[sigma[y]] == source[sign_section[y]]
               for source, sigma in zip((a5, b5), sign_cover) for y in range(2))

    # Gauge/source controls: transport at a second vertex must be rooted.
    c = (1, 2, 0)
    edges = ((0, 1, c), (1, 1, mul(mul(c, a), inv(c))),
             (1, 1, mul(mul(c, b), inv(c))))
    original = raw_holonomy((0, 1), edges, 0)
    assert original == group
    gauge_checks = 0
    for g0, g1 in product(tuple(permutations(range(3))), repeat=2):
        gauges = (g0, g1)
        changed = tuple((u, v, mul(mul(gauges[v], p), inv(gauges[u])))
                        for u, v, p in edges)
        actual = raw_holonomy((0, 1), changed, 0)
        expected = frozenset(mul(mul(g0, h), inv(g0)) for h in original)
        assert actual == expected
        # A non-descending section stays lawful after vertexwise gauge change.
        tree = (identity, c)
        for u, v, p in edges:
            residual = mul(mul(inv(tree[v]), p), tree[u])
            for y in range(3):
                left = gauges[v][tree[v][residual[y]]]
                right = mul(mul(gauges[v], p), inv(gauges[u]))[gauges[u][tree[u][y]]]
                assert left == right
        gauge_checks += 1
    commutator = mul(mul(mul(inv(b), inv(a)), b), a)
    parity = (-1) ** sum(commutator[i] > commutator[j]
                         for i in range(3) for j in range(i + 1, 3))
    assert commutator != identity and parity == 1
    assert fixed(generated((a,), 3)) == (2,)  # Nonflat base positive control.
    assert fixed(generated((identity,), 3)) == (0, 1, 2)
    return {
        'status': 'TESTED MODEL', 'exact': True,
        'parent_sha': '5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
        'python': platform.python_version(),
        'command': 'python research/2026-10-13/SWARM_ATLAS/A04_probe.py',
        'exit_code': 0, 'source_generators': source_gens,
        'holonomy_order': len(group), 'base_sections': 0,
        'connected_cover_oracle': covers, 'cover_assignments': assignment_count,
        's3_orbit_cover': {'degree': 3, 'section': q, 'deck_maps': decks,
                          'deck_invariant': True, 'descends': False,
                          'fiber_pair_counterexample': [0, 1],
                          'pulled_back_holonomy_order': len(stabilizer)},
        'minimum_section_cover_degree': 3,
        'minimum_regular_section_cover_degree': 6,
        'minimum_full_trivializing_cover_degree': 6,
        'all_s3_subgroups': len(s3_subs), 'normal_s3_subgroups': len(s3_normal),
        'nonfaithful_orbit_control': {'orbits': mixed_orbits,
                                     'minimum_section_cover_degree': mixed_min,
                                     'minimum_regular_section_cover_degree': mixed_regular_min,
                                     'full_trivializing_degree': len(mixed_group),
                                     'regular_double_cover_section': sign_section},
        'source_generator_pair_checks': field_checks,
        'vertex_gauge_checks': gauge_checks,
        'even_nonidentity_commutator': commutator,
        'finite_search_is_universal_proof': False,
        'lean_compilation': 'NOT RUN', 'full_suite': 'NOT RUN',
        'probe_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_sha256': {p: sha256(Path(p).read_bytes()).hexdigest() for p in (
            'observational_succ/nonabelian_local_global.py',
            'observational_succ/voltage_cover_synthesis.py',
            'observational_succ/holonomy_proof_transport.py',
            'formal/EODCS_CausalDescent.lean')},
        'git_parent': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
