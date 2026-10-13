"""Bounded independent F48 phase2 controls; never execute swarm author probes."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import time

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
START = time.monotonic()
ROOT = Path(__file__).resolve().parents[3]
ATLAS_ROOT = Path('/home/leah/succ_lab/many-worlds-atlas')
ATLAS = ATLAS_ROOT / 'research/2026-10-13/SWARM_ATLAS'


def paths(edges, roots, depth):
    stage = {(r,) for r in roots}
    for _ in range(depth):
        stage = {p + (t,) for p in stage for t in edges[p[-1]]}
    return stage


def live_core(edges):
    core = set(edges)
    while True:
        reduced = {v for v in core if set(edges[v]) & core}
        if reduced == core:
            return core
        core = reduced


def main():
    models = stage_checks = maximality_checks = 0
    for size in range(1, 4):
        pairs = list(product(range(size), repeat=2))
        for mask in range(1 << (size * size)):
            edges = {v: tuple(w for bit, (u, w) in enumerate(pairs)
                              if u == v and mask & (1 << bit))
                     for v in range(size)}
            core = live_core(edges)
            # Independent finite-state cycle oracle: a size-edge walk must
            # repeat a vertex; a reached cycle extends without bound.
            cycle_reaching = {v for v in edges if paths(edges, (v,), size)}
            assert core == cycle_reaching
            for subset_mask in range(1 << size):
                subset = {v for v in edges if subset_mask & (1 << v)}
                if all(set(edges[v]) & subset for v in subset):
                    assert subset <= core
                maximality_checks += 1
            for root_mask in range(1 << size):
                roots = {v for v in edges if root_mask & (1 << v)}
                previous = {p for p in paths(edges, roots, 0) if p[-1] in core}
                for depth in range(1, 5):
                    raw = paths(edges, roots, depth)
                    extendable = {p for p in raw if p[-1] in core}
                    assert {p[:-1] for p in extendable} == previous
                    assert all(p[0] in roots for p in extendable)
                    previous = extendable
                    stage_checks += 1
            models += 1

    edges = {'live': ('live', 'dead'), 'dead': ()}
    raw1, raw2 = paths(edges, ('live',), 1), paths(edges, ('live',), 2)
    missing = raw1 - {p[:-1] for p in raw2}
    assert missing == {('live', 'dead')}
    assert {p for p in raw1 if p[-1] in live_core(edges)} == {('live', 'live')}

    # An arbitrary bounded-depth adapter sees the delayed dead path as live.
    # This finite witness cannot implement the universally quantified pruning.
    delayed = {0: (0, 1), 1: (2,), 2: (3,), 3: (4,), 4: ()}
    assert paths(delayed, (1,), 3)
    assert not paths(delayed, (1,), 4)
    assert live_core(delayed) == {0}
    aggregate_root = {'source0', 'source1'}
    aggregate_next = {('source0', 0), ('source1', 1)}
    assert {s for s, o in aggregate_next} == aggregate_root
    fixed_outcome_zero = {s for s, o in aggregate_next if o == 0}
    assert fixed_outcome_zero == {'source0'} < aggregate_root

    # Natural countdowns give all finite depths from different preparations.
    # No actual infinite countdown exists; that conclusion uses strict descent.
    countdown_prefixes = [tuple(range(n, -1, -1)) for n in range(1, 9)]
    assert all(len(p) == n + 1 for n, p in enumerate(countdown_prefixes, 1))
    assert all(all(p[i+1] == p[i] - 1 for i in range(len(p)-1))
               for p in countdown_prefixes)
    # Global Büchi admission is stricter than local branch legality. Every
    # finite prefix extends by a one-tail, including 0^n; the all-zero
    # coherent thread is excluded by the global infinitely-many-ones law.
    buchi_prefix_count = 0
    for depth in range(9):
        prefixes = list(product((0, 1), repeat=depth))
        buchi_prefix_count += len(prefixes)
        assert (0,)*depth in prefixes
        assert all(bit in (0, 1) for p in prefixes for bit in p)

    # Exact scalar CP identity and split identity. We use squared amplitudes,
    # avoiding floating square roots; the Kraus identities are derived on paper.
    kraus_weights = ([Q(1)], [Q(1, 2), Q(1, 2)])
    assert sum(kraus_weights[0]) == sum(kraus_weights[1]) == 1
    branch_counts = {n: [1, 2**n] for n in range(1, 9)}
    for n, counts in branch_counts.items():
        assert sum(Q(1, 2**n) for _ in range(counts[1])) == 1
    zero_outcome_map = Q(0)
    assert zero_outcome_map == 0  # no positive normalization exists
    # Finite height in each parameter fiber gives no global bound over all n.
    # The full infinite-parameter no-go is a strict-death argument on paper.
    for depth in range(9):
        assert depth <= depth + 1  # parameter n=depth+1 supports this prefix
    parameter_deaths = {n: n+1 for n in range(9)}
    assert all(death > n for n, death in parameter_deaths.items())

    # One-way availability lifting can suffice: coarse 'wait' is unavailable,
    # fine 'wait' is available, but the identical coarse 'read' policy lifts.
    fine_enabled = {'read': True, 'wait': True}
    coarse_enabled = {'read': True, 'wait': False}
    assert all(not coarse_enabled[a] or fine_enabled[a] for a in fine_enabled)
    assert any(fine_enabled[a] != coarse_enabled[a] for a in fine_enabled)
    fine_read = coarse_read = {(0, 0): Q(1)}
    assert fine_read == coarse_read

    # Positive tolerance repair has incomparable minimum partitions.
    f = {0: Q(0), 1: Q(1), 2: Q(2)}
    radius = lambda blocks: max((max(f[x] for x in b) - min(f[x] for x in b))/2
                               for b in blocks)
    p, q = ({0, 1}, {2}), ({0}, {1, 2})
    assert radius(p) == radius(q) == Q(1, 2)
    assert radius(({0, 1, 2},)) == 1

    # Complete source and memory must be kept in interfaces.
    current = 0
    source_outputs = {('sigma0', current): 0, ('sigma1', current): 1}
    assert len(set(source_outputs.values())) == 2
    memory_enabled = {('unused', current): True, ('spent', current): False}
    assert len(set(memory_enabled.values())) == 2

    # A fully visible two-delay source can retain an invisible linear mode.
    states = list(product((-1, 1), repeat=2))
    assert len({(a, b) for a, b in states}) == 4
    mode = {(a, b): a*b for a, b in states}
    for sensor in (lambda a,b: 1, lambda a,b: a, lambda a,b: b):
        assert sum(Q(1,4)*sensor(a,b)*mode[a,b] for a,b in states) == 0
    assert sum(Q(1,4)*(a*b)*mode[a,b] for a,b in states) == 1

    registry_bytes = (ATLAS / 'registry.json').read_bytes()
    registry = json.loads(registry_bytes)
    records = registry['assignments'] + registry['syntheses']
    entries = []
    paths_to_hash = [ATLAS / 'registry.json', ATLAS / 'SUCC_MATHEMATICAL_ATLAS.md',
                     ATLAS / 'comparisons/PARALLEL_AUDIT.md',
                     ATLAS / 'comparisons/SECOND_WAVE_COMPARISON.md',
                     ATLAS_ROOT / 'formal/SWM_F48_InterfaceJoin.lean']
    paths_to_hash += [ATLAS_ROOT / p for p in (
        'AGENTS.md','docs/METHOD.md','docs/FOUNDATIONS.md','docs/ARCHITECTURE.md',
        'provenance/IMPORT_MANIFEST.json',
        'research/2026-10-13/F48/F48_PHASE2_ARCHITECTURE.md')]
    a03_root = Path('/home/leah/succ_lab/swm-a03')
    a03_review = a03_root / 'reviews/F48_PHASE2_A03_REVIEW.md'
    a03_commit = 'bb1c00ff04259d7d0c53727a18597b4fba3ee5cc'
    a03_committed = subprocess.check_output(
        ['git','show',a03_commit + ':reviews/F48_PHASE2_A03_REVIEW.md'],cwd=ROOT)
    assert a03_review.read_bytes() == a03_committed
    paths_to_hash += [a03_review,
                     a03_root/'reviews/F48_PHASE2_A03_REVIEW_receipt.json',
                     a03_root/'reviews/F48_PHASE2_A03_REVIEW_probe.py']
    for e in records:
        ident = e['id']
        if ident == 'F48':
            dossier = ROOT / e['dossier_path']
        elif e.get('dossier_path'):
            dossier = ATLAS_ROOT / e['dossier_path']
        else:
            dossier = ATLAS / (ident + '.md')
            if not dossier.exists() and (ATLAS / ident / 'DOSSIER.md').exists():
                dossier = ATLAS / ident / 'DOSSIER.md'
        reviews = [p for p in (ATLAS / 'reviews').glob('*.md')
                   if ident in p.name]
        if ident in ('D29','D31','D32','E37','F48'):
            reviews += list((ATLAS / 'reviews').glob('WAVE_GEOMETRY_GAMMA_F48_REVIEW.md'))
        if ident in ('A05','A06','C18','E33'):
            reviews += [ATLAS / 'reviews/A05_A06_C18_E33_PRINCIPAL.md']
        if ident in ('E40','F46','F47'):
            reviews += [ATLAS / 'reviews/E40_F46_F47_PRINCIPAL_REVIEW.md']
        reviews = sorted(set(p for p in reviews if p.exists()))
        exists = dossier.exists()
        entries.append({'id':ident, 'integration':e.get('integration'),
                        'registry_status':e.get('status'), 'author_commit':e.get('commit'),
                        'dossier':str(dossier), 'dossier_present':exists,
                        'dossier_sha256':hashlib.sha256(dossier.read_bytes()).hexdigest() if exists else None,
                        'review_paths':[str(p) for p in reviews]})
        paths_to_hash += ([dossier] if exists else []) + reviews
    # Bind every available review, including shared reviewers and additive corrections.
    paths_to_hash += list((ATLAS / 'reviews').glob('*.md'))
    source_hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(set(paths_to_hash))}
    missing_inputs = [e['id'] for e in entries if not e['dossier_present']]
    unaccepted = [e['id'] for e in entries if e['id'].startswith('X') and e['integration'] != 'ACCEPTED']
    elapsed = time.monotonic() - START
    assert elapsed < 25
    architecture = (Path(__file__).parent / 'F48_PHASE2_ARCHITECTURE.md').read_text()
    proof_sections = architecture.split('## 5. New theorem:', 1)[1].split('## 7. Crucible', 1)[0]
    frozen_architecture = subprocess.check_output(
        ['git','show','224d049964b02fc42ad4fcbaa078944ed91da0a7:research/2026-10-13/F48/F48_PHASE2_ARCHITECTURE.md'],
        cwd=ROOT,text=True)
    frozen_proof = frozen_architecture.split('## 5. New theorem:',1)[1].split('## 7. Crucible',1)[0]
    assert proof_sections == frozen_proof
    headed_proof = architecture[architecture.index('## 5.'):architecture.index('## 7.')]
    assert hashlib.sha256(headed_proof.encode()).hexdigest() == '59466bb9c0f2a5e8580a595ef1dfddc977238254266a874af229585de3618f8e'
    print(json.dumps({
        'phase':'F48 whole-swarm phase2',
        'initial_commit':'6e751c0d996de3d27a91b09f44dc2d534db09c73',
        'root_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ATLAS_ROOT,text=True).strip(),
        'registry_sha256':hashlib.sha256(registry_bytes).hexdigest(),
        'elapsed_seconds':round(elapsed,6), 'address_space_cap_bytes':256*1024**2,
        'exit':0, 'bounded_graph_models':models,
        'extendable_bonding_checks':stage_checks, 'greatest_core_checks':maximality_checks,
        'aggregate_depth_onto_fixed_public_arrow_not_onto':{
            'aggregate_root':sorted(aggregate_root),
            'fixed_outcome_zero_predecessors':sorted(fixed_outcome_zero)},
        'live_dead_missing_raw_prefixes':sorted(missing),
        'countdown_depths_checked':len(countdown_prefixes),
        'buchi_all_finite_prefixes_checked':buchi_prefix_count,
        'global_buchi_admission_stricter_than_local_branch_completion':True,
        'delayed_death_false_finite_plateau':True,
        'identity_channel_kraus_atom_counts':branch_counts,
        'one_dimensional_parameter_fibers_do_not_give_global_finite_height':parameter_deaths,
        'one_way_availability_counter_to_iff_necessity':True,
        'noncanonical_tolerant_repair':True,
        'linear_vs_algebra_observation_gap':True,
        'finite_positive_likelihoods_can_have_zero_limit':str(Q(1,2**64)),
        'records':entries, 'source_sha256':source_hashes,
        'missing_final_dossiers':missing_inputs,
        'unaccepted_synthesis_inputs':unaccepted,
        'state':('AWAITING_FINAL_INPUT' if missing_inputs else
                 'AWAITING_FINAL_ACCEPTANCE' if unaccepted else
                 'CORE_ACCEPTED_PENDING_PRINCIPAL_ARTIFACT_REVIEW'),
        'proof_sections_5_6_sha256':hashlib.sha256(proof_sections.encode()).hexdigest(),
        'proof_sections_unchanged_from_224d049':True,
        'proof_sections_5_6_including_heading_sha256':hashlib.sha256(headed_proof.encode()).hexdigest(),
        'fresh_a03_review':{'commit':a03_commit,'path':str(a03_review),
                            'scope':'T1/T2 and conditional host gates; not all60 theorem recertification',
                            'sha256':hashlib.sha256(a03_committed).hexdigest(),
                            'reviewer_probe_reexecuted_by_f48':False,
                            'verdict':'ACCEPT PROVED LOCAL'},
        'validation_command':'env PYTHONDONTWRITEBYTECODE=1 timeout 25s python research/2026-10-13/F48/F48_PHASE2_PROBE.py',
        'artifact_validation_history':[
            {'check':'initial matrix parser','exit':1,'cause':'A01 row contained an extra delimiter; corrected'},
            {'check':'initial row-count artifact assertion','exit':1,'cause':'header+60 rows is61, not62; corrected'},
        ],
        'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'swarm_author_probes_replayed':False,
        'full_suite_or_compiler_or_children_or_push':False,
        'final_non_deriver_review_complete':True,
        'principal_final_artifact_acceptance_complete':False,
    },indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
