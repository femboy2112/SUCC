#!/usr/bin/env python3
"""Record and replay Main XXIV contribution provenance without a self-hash.

Generate after committing the assembled fronts. ``--integration`` names the Git
snapshot whose contribution bytes are recorded; the manifest itself and later
merge metadata are outside that byte-comparison scope. A check against a newer
ref is permitted only if every recorded destination/protected byte and every
required ancestry relation still matches. This tool is not a proof checker.

    python scripts/main_xxiv_manifest.py --inventory inventory.json --prs prs.json \
        --main <verified-main-xxiii> --integration HEAD --decisions decisions.json \
        --out manifest.json
    python scripts/main_xxiv_manifest.py --check manifest.json --integration HEAD

Decisions use ``paths`` keys ``<PR>:<original-path>`` (or an unqualified path),
with ``canonical_destination``, ``disposition``, ``reason`` and ``authority``.
Changed canonical bytes require a declared ``repaired`` or
``independent_equivalent_superseded`` decision. ``contributions`` keys are row
IDs and can supply precise claim/status/test-authority supplements. Source
hashes, ancestry and final byte identities are always derived from Git.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess
import sys


CATALOG = 'docs/math_memory/CLAIM_CATALOG.json'
SPECIAL = {
    585: [('initial', 0, 0), ('signed-tauberian', 1, 1),
          ('lambert', 2, 2), ('mellin-boundary', 3, 4)],
    592: [('microscope', 0, 0), ('fixed-depth-fingerprint', 1, 1)],
    595: [('rounds-i-ii', 0, 0), ('round-iii', 1, 1),
          ('round-iv-geometry', 2, 2), ('round-v-aperiodicity', 3, 3)],
}
CLAIMS = {
    576: 'Scott-Omega finite source weld and computational witnesses; #579 errata govern semantics.',
    577: 'Intellectual provenance and steelman/crucible source genealogy; documentary scope.',
    579: 'Capture-safe finite semantics, source-clock action, parity boundary payments and hostile repairs.',
    581: 'BBP computational graph resonance and source-mutant countermodels.',
    582: 'Finite dagger/unitary arithmetic models; scalable physical implementation unverified.',
    583: 'Intrinsic arithmetic carrier and Hamiltonian finite blocks.',
    584: 'Main XXIII source/semantic reconciliation, parity and operator-domain corrections.',
    585: 'Basel/CRT signed Weyl transport and Tauberian/Lambert/Mellin criteria; selected decay remains open.',
    586: 'Gaussian angular lattice bounds and certified BBP long-lag diagnostics; pullback saving open.',
    587: 'Completed prime-Archimedean Weil source and authenticated BBP defect; compare independent #588.',
    588: 'Completed Weil source with all-prime 3/2 ratio fiber; no completed positivity or normality conclusion.',
    589: 'Alternative typed zero-anchored Lambda-Haar implementation and hostile seed certificates.',
    591: 'Source-anchored typed Lambda compiler and exact signed Haar/CDF overlap identities.',
    592: 'Zero-seed radix microscope and fixed-depth signed Fourier fingerprints; no statistical contraction.',
    593: 'Signed 2-to-3 Haar joinings; Haar marginals and a null mixed mode do not imply independence.',
    594: 'Numerical categories, rational-cut presheaves and irrational Dedekind-Yoneda reconstruction.',
    595: 'Categorical arithmetic, geometric productive pi observer and finite aperiodicity certificates.',
    596: 'Finite-height Farey exclusion and coherent rational-cut restrictions under declared irrationality.',
    597: 'Exact symbolic seed recovery in Q+Q*pi/16 and certified finite signed observations.',
}


def git(*args: str) -> bytes:
    p = subprocess.run(['git', *args], capture_output=True)
    if p.returncode:
        raise ValueError(p.stderr.decode(errors='replace').strip())
    return p.stdout


def resolve(ref: str) -> str:
    return git('rev-parse', '--verify', ref + '^{commit}').decode().strip()


def ancestor(a: str, b: str) -> bool:
    p = subprocess.run(['git', 'merge-base', '--is-ancestor', a, b], capture_output=True)
    if p.returncode not in (0, 1):
        raise ValueError(p.stderr.decode(errors='replace').strip())
    return p.returncode == 0


@lru_cache(maxsize=None)
def tree(ref: str) -> dict[str, tuple[str, str, str]]:
    result = {}
    for item in git('ls-tree', '-r', '-z', ref).split(b'\0'):
        if item:
            meta, path = item.split(b'\t', 1)
            mode, kind, blob = meta.decode().split()
            result[path.decode()] = (mode, kind, blob)
    return result


@lru_cache(maxsize=None)
def digest(blob: str) -> dict[str, str]:
    return {'git_blob': blob, 'sha256': hashlib.sha256(git('cat-file', 'blob', blob)).hexdigest()}


def identity(ref: str, path: str) -> dict[str, str] | None:
    entry = tree(ref).get(path)
    if entry is None:
        return None
    mode, kind, blob = entry
    if kind != 'blob':
        raise ValueError(f'{ref}:{path}: expected file, found {kind}')
    return dict(digest(blob), mode=mode, kind=kind)


def changes(base: str, head: str) -> list[tuple[str, str]]:
    fields = git('diff', '--name-status', '--no-renames', '-z', base, head).split(b'\0')
    return [(fields[i].decode(), fields[i + 1].decode())
            for i in range(0, len(fields) - 1, 2)]


def source_groups(p: dict) -> list[tuple[str, str, str, list[str]]]:
    """Separate real checkpoints, retaining actual first-parent dependencies."""
    commits = p['own_commits']
    if p['number'] in SPECIAL:
        groups = SPECIAL[p['number']]
        if len(commits) != max(g[2] for g in groups) + 1:
            raise ValueError(f"PR #{p['number']} checkpoint count changed; audit grouping")
        return [(label, git('rev-parse', commits[start] + '^1').decode().strip(),
                 commits[end], commits[start:end + 1]) for label, start, end in groups]
    if p['number'] == 584:
        # Donor merges are inherited, not new discoveries made by the integrator.
        own = git('rev-list', '--first-parent', '--no-merges', '--reverse',
                  p['own_base'] + '..' + p['head']).decode().split()
        if not own:
            raise ValueError('Main XXIII has no integration-specific commits')
        return [('integration-corrections', git('rev-parse', own[0] + '^1').decode().strip(),
                 p['head'], own)]
    return [('contribution', p['own_base'], p['head'], commits)]


def normalized_origins(inventory: dict, prs: list[dict]) -> list[dict]:
    by_number = {p['number']: p for p in prs}
    result = []
    for row in inventory['prs']:
        p = dict(row)
        snap = by_number[p['number']]
        if p['head'] != snap.get('head_sha', snap.get('headRefOid')):
            raise ValueError(f"PR #{p['number']} frozen snapshots disagree")
        p['head'] = resolve(p['head'])
        p['own_base'] = resolve(p.get('own_base', inventory['main']))
        if not ancestor(p['own_base'], p['head']):
            raise ValueError(f"PR #{p['number']} actual fork is not an ancestor")
        p['own_commits'] = git('rev-list', '--reverse', p['own_base'] + '..' + p['head']).decode().split()
        p['head_tree'] = git('rev-parse', p['head'] + '^{tree}').decode().strip()
        p['url'] = snap.get('url', f"https://github.com/femboy2112/SUCC/pull/{p['number']}")
        result.append(p)
    if set(by_number) != {p['number'] for p in result}:
        raise ValueError('Frozen PR snapshot contains contributions absent from inventory')
    return sorted(result, key=lambda p: p['number'])


def protected_paths(baseline: str) -> set[str]:
    paths = tree(baseline)
    imported = json.loads(git('show', baseline + ':provenance/IMPORT_MANIFEST.json')) \
        if 'provenance/IMPORT_MANIFEST.json' in paths else {'entries': []}
    protected = {p for p in paths if p.startswith(('provenance/', 'docs/archive/'))}
    protected.update(x['destination_path'] for x in imported['entries'])
    protected.update(p for p in ('observational_succ/duck_bbp.py',
                     'observational_succ/integer_bbp_carrier.py',
                     'observational_succ/selected_orbit.py') if p in paths)
    return protected


def generate(inventory: dict, prs: list[dict], main: str, integration: str,
             decisions: dict | None = None) -> dict:
    decisions = decisions or {}
    main, final = resolve(main), resolve(integration)
    baseline = resolve(inventory['main'])
    origins = normalized_origins(inventory, prs)
    owned_paths = {p['number']: {path for _, path in changes(p['own_base'], p['head'])}
                   for p in origins}
    rows = []
    for p in origins:
        for label, parent, checkpoint, commits in source_groups(p):
            row_id = f"pr-{p['number']}-{label}"
            row = {'id': row_id, 'originating_pr': p['number'], 'url': p['url'],
                   'branch': p['branch'], 'head_commit': p['head'], 'head_tree': p['head_tree'],
                   'actual_own_parent': p['own_base'], 'contribution_parent': parent,
                   'contribution_commit': checkpoint,
                   'contribution_tree': git('rev-parse', checkpoint + '^{tree}').decode().strip(),
                   'contribution_commits': commits, 'claim': CLAIMS.get(p['number'], p['title']),
                   'claim_status': 'SCOPED_PAPER_OR_FINITE_RESULT; universal cancellation/normality/RH OPEN',
                   'integration_action': 'Retain source history and verify canonical destinations below.',
                   'post_integration_verification': 'Hash/mode/ancestry replay required by --check; final native and hosted receipts are separate authorities.',
                   'already_on_main_xxiii': ancestor(p['head'], main),
                   'inherited_from_prs': [q['number'] for q in origins
                                           if q['number'] != p['number'] and ancestor(q['head'], parent)],
                   'files': []}
            supplement = decisions.get('contributions', {}).get(row_id, {})
            for key in ('claim', 'claim_status', 'test_authority', 'integration_action', 'review_boundary'):
                if key in supplement:
                    row[key] = supplement[key]
            for status, path in changes(parent, checkpoint):
                source = identity(checkpoint, path)
                origin_head = identity(p['head'], path)
                # A source can evolve later in this PR or in a descendant repair.
                owners = [q for q in origins if path in owned_paths[q['number']] and
                          ancestor(p['head'], q['head'])]
                latest = [q for q in owners if all(ancestor(r['head'], q['head']) for r in owners)]
                effective = latest[0] if latest else p
                expected = identity(effective['head'], path)
                decision = decisions.get('paths', {}).get(f"{p['number']}:{path}",
                           decisions.get('paths', {}).get(path, {}))
                destination = decision.get('canonical_destination', path)
                actual = identity(final, destination)
                disposition = decision.get('disposition')
                if not disposition:
                    disposition = ('regenerated_catalog' if path == CATALOG else
                                   'deleted_in_origin' if source is None else
                                   'preserved' if actual == source else
                                   'evolved_in_source_ancestry' if actual == expected else 'UNACCOUNTED')
                if disposition in ('repaired', 'independent_equivalent_superseded', 'archived_alternative'):
                    if not decision.get('reason') or not decision.get('authority'):
                        raise ValueError(f'{row_id}:{path}: reviewed decision needs reason and authority')
                independent = [q['number'] for q in origins if q['number'] != p['number'] and
                               path in owned_paths[q['number']] and
                               not ancestor(q['head'], p['head']) and not ancestor(p['head'], q['head']) and
                               identity(q['head'], path) == origin_head and origin_head is not None]
                row['files'].append({'path': path, 'change': status,
                    'origin_role': 'new' if status == 'A' else 'inherited_modified_or_deleted',
                    'parent_identity': identity(parent, path),
                    'source_identity': source, 'origin_head_identity': origin_head,
                    'effective_source_pr': effective['number'], 'effective_source_identity': expected,
                    'independent_identical_prs': independent,
                    'canonical_destination': destination, 'final_identity': actual,
                    'source_equals_final': source == actual, 'disposition': disposition,
                    'decision': decision})
            if 'test_authority' not in row:
                row['test_authority'] = {
                    'kind': 'ORIGIN_RECEIPTS_ONLY; integration execution not inferred',
                    'entrypoints': [f['path'] for f in row['files'] if
                                    Path(f['path']).name.startswith('test_') or
                                    'VALIDATION' in Path(f['path']).name or
                                    Path(f['path']).suffix == '.log']}
            rows.append(row)
    return {'schema_version': 1, 'scope': 'Main XXIV contribution bytes and ancestry, not proof certification',
            'baseline_main': baseline, 'verified_main_xxiii': main,
            'integration_ref_at_generation': integration,
            'self_reference_policy': 'No final commit/tree self-hash; check with explicit --integration ref.',
            'input_sha256': {'inventory': hashlib.sha256(json.dumps(inventory, sort_keys=True).encode()).hexdigest(),
                             'prs': hashlib.sha256(json.dumps(prs, sort_keys=True).encode()).hexdigest()},
            'non_pr_numbers': [578, 580, 590],
            'deferred_non_pr_heads': [{'head': 'b26a607cc47b41f5f79e9ecd462c7891b42342d8',
                'disposition': 'DEFERRED', 'reason': 'Two-sheet Cayley parity sign mismatch at u=1/10; do not import.'}],
            'evidence_only_heads': [{'head': '397882d152bc752d402dbf47b829816db097bb7a',
                'disposition': 'Historical Main XXII validation evidence, not a mathematical donor.'}],
            'origins': [{k: p[k] for k in ('number', 'branch', 'head', 'head_tree', 'own_base')}
                        for p in origins],
            'expected_contribution_ids': [r['id'] for r in rows],
            'protected': [{'path': p, 'identity': identity(baseline, p)} for p in sorted(protected_paths(baseline))],
            'contributions': rows}


def check(data: dict, integration: str) -> list[str]:
    final = resolve(integration)
    errors = []
    origins = {p['number']: p for p in data['origins']}
    expected_groups = {}
    for p in origins.values():
        origin = dict(p)
        origin['own_commits'] = git('rev-list', '--reverse', p['own_base'] + '..' + p['head']).decode().split()
        for label, parent, checkpoint, commits in source_groups(origin):
            expected_groups[f"pr-{p['number']}-{label}"] = (parent, checkpoint, commits)
    if set(data['expected_contribution_ids']) != {r['id'] for r in data['contributions']}:
        errors.append('Contribution row coverage mismatch')
    if set(expected_groups) != {r['id'] for r in data['contributions']}:
        errors.append('Frozen-source checkpoint coverage mismatch')
    if set(origins) != {r['originating_pr'] for r in data['contributions']}:
        errors.append('Origin PR coverage mismatch')
    if not ancestor(data['verified_main_xxiii'], final):
        errors.append('Verified Main XXIII is not an ancestor of integration')
    if {p['path'] for p in data['protected']} != protected_paths(data['baseline_main']):
        errors.append('Protected path coverage mismatch')
    for p in data['protected']:
        if identity(data['baseline_main'], p['path']) != p['identity']:
            errors.append('Protected baseline identity mismatch: ' + p['path'])
        if identity(final, p['path']) != p['identity']:
            errors.append('Protected bytes changed: ' + p['path'])
    ids = set()
    for row in data['contributions']:
        if row['id'] in ids:
            errors.append('Duplicate contribution: ' + row['id'])
        ids.add(row['id'])
        origin = origins[row['originating_pr']]
        if (row['head_commit'], row['head_tree'], row['actual_own_parent'], row['branch']) != \
                (origin['head'], origin['head_tree'], origin['own_base'], origin['branch']):
            errors.append('Origin metadata mismatch: ' + row['id'])
        if expected_groups.get(row['id']) != (row['contribution_parent'], row['contribution_commit'],
                                               row['contribution_commits']):
            errors.append('Frozen-source checkpoint mismatch: ' + row['id'])
        for commit_key, tree_key in [('head_commit', 'head_tree'), ('contribution_commit', 'contribution_tree')]:
            if git('rev-parse', row[commit_key] + '^{tree}').decode().strip() != row[tree_key]:
                errors.append('Source tree mismatch: ' + row['id'])
        for parent, child in [(row['actual_own_parent'], row['head_commit']),
                              (row['contribution_parent'], row['contribution_commit']),
                              (row['contribution_commit'], row['head_commit']),
                              (row['contribution_commit'], final), (row['head_commit'], final)]:
            if not ancestor(parent, child):
                errors.append('Missing ancestry: ' + row['id'] + ':' + parent + ' -> ' + child)
        expected_paths = {p for _, p in changes(row['contribution_parent'], row['contribution_commit'])}
        if expected_paths != {f['path'] for f in row['files']}:
            errors.append('Contribution path coverage mismatch: ' + row['id'])
        for f in row['files']:
            name = row['id'] + ':' + f['path']
            if identity(row['contribution_commit'], f['path']) != f['source_identity']:
                errors.append('Source blob mismatch: ' + name)
            if identity(row['contribution_parent'], f['path']) != f['parent_identity']:
                errors.append('Inherited parent blob mismatch: ' + name)
            if identity(row['head_commit'], f['path']) != f['origin_head_identity']:
                errors.append('Origin head blob mismatch: ' + name)
            effective = origins.get(f['effective_source_pr'])
            if effective is None or identity(effective['head'], f['path']) != f['effective_source_identity']:
                errors.append('Effective source blob mismatch: ' + name)
            if identity(final, f['canonical_destination']) != f['final_identity']:
                errors.append('Final bytes changed: ' + name)
            disposition = f['disposition']
            if disposition == 'UNACCOUNTED' or (f['source_identity'] is not None and f['final_identity'] is None):
                errors.append('Unaccounted contribution: ' + name)
            elif disposition == 'preserved' and f['final_identity'] != f['source_identity']:
                errors.append('Preservation mismatch: ' + name)
            elif disposition == 'evolved_in_source_ancestry' and f['final_identity'] != f['effective_source_identity']:
                errors.append('Source evolution mismatch: ' + name)
            elif disposition == 'archived_alternative' and f['final_identity'] != f['origin_head_identity']:
                errors.append('Archive redirect is not byte-identical: ' + name)
            elif disposition == 'deleted_in_origin' and f['final_identity'] is not None:
                errors.append('Origin deletion not respected: ' + name)
            elif disposition == 'regenerated_catalog' and f['path'] != CATALOG:
                errors.append('Catalog exception used for another file: ' + name)
            elif disposition in ('repaired', 'independent_equivalent_superseded', 'archived_alternative'):
                if not f['decision'].get('reason') or not f['decision'].get('authority'):
                    errors.append('Unsupported reviewed decision: ' + name)
            elif disposition not in ('preserved', 'evolved_in_source_ancestry', 'deleted_in_origin', 'regenerated_catalog'):
                errors.append('Unknown disposition: ' + name)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory')
    parser.add_argument('--prs')
    parser.add_argument('--main')
    parser.add_argument('--integration', required=True)
    parser.add_argument('--decisions')
    parser.add_argument('--out')
    parser.add_argument('--check')
    args = parser.parse_args()
    if args.check:
        data = json.loads(Path(args.check).read_text())
    else:
        if not all((args.inventory, args.prs, args.main, args.out)):
            parser.error('generation requires --inventory, --prs, --main and --out')
        data = generate(json.loads(Path(args.inventory).read_text()), json.loads(Path(args.prs).read_text()),
                        args.main, args.integration,
                        json.loads(Path(args.decisions).read_text()) if args.decisions else {})
        Path(args.out).write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    errors = check(data, args.integration)
    print(json.dumps({'status': 'FAIL' if errors else 'PASS', 'contributions': len(data['contributions']),
                      'protected_paths': len(data['protected']), 'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError) as exc:
        print(f'Manifest error: {exc}', file=sys.stderr)
        sys.exit(2)
