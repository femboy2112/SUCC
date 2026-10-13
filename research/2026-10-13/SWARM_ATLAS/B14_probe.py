#!/usr/bin/env python3
"""Exact bounded controls; no continuum classifier or mathematical proof engine."""
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys

PARENT = '5eb09e7cba36ec01b8f9d6834b78b5766fd93935'


def sparse_tail(length):
    bits, gap = [], 1
    while len(bits) < length:
        bits.extend([1] + [0] * gap)
        gap += 1
    return tuple(bits[:length])


def first_one(index, length):
    return tuple(int(i == index) for i in range(length))


def main():
    pair_count = 0
    for depth in range(9):
        for prefix in itertools.product((0, 1), repeat=depth):
            zero_extension = prefix + (0,) * 16
            sparse_extension = prefix + sparse_tail(16)
            assert zero_extension[:depth] == sparse_extension[:depth] == prefix
            assert zero_extension[depth] != sparse_extension[depth]
            # These finite bits demonstrate contact/overlap, not infinite labels.
            assert int(zero_extension[depth] == 0) != int(sparse_extension[depth] == 0)
            pair_count += 1

    # Calibration: a genuine clopen predicate has a single-bit answer.
    clopen_count = 0
    for word in itertools.product((0, 1), repeat=8):
        answer = bool(word[0])
        assert all(bool((word[:1] + suffix)[0]) == answer
                   for suffix in itertools.product((0, 1), repeat=3))
        clopen_count += 1

    # Calibration: seen-one recognition accepts a positive prefix and waits on 0^N.
    assert next((i + 1 for i, bit in enumerate((0, 0, 1, 0)) if bit), None) == 3
    assert next((i + 1 for i, bit in enumerate((0,) * 64) if bit), None) is None

    reads = []
    for index in range(32):
        source_window = first_one(index, index + 1)
        stop = next(i for i, bit in enumerate(source_window) if bit)
        assert stop == index
        assert (stop % 2 == 0) == (index % 2 == 0)
        reads.append(stop + 1)

    delayed = []
    for horizon in range(17):
        even = horizon + horizon % 2
        odd = horizon + (1 - horizon % 2)
        assert even % 2 == 0 and odd % 2 == 1
        assert first_one(even, horizon) == first_one(odd, horizon) == (0,) * horizon
        delayed.append({'horizon': horizon, 'even_first_one': even, 'odd_first_one': odd})

    # Exact finite block controls for g: boundaries, marker positions, growing runs.
    sample = (1, 0, 1, 1, 0, 1)
    blocks = tuple(tuple([bit] + [0] * (i + 1)) for i, bit in enumerate(sample))
    encoded = tuple(itertools.chain.from_iterable(blocks))
    assert len(encoded) == sum(i + 2 for i in range(len(sample)))
    assert sum(encoded) == sum(sample)
    assert [len(b) - 1 for b in blocks] == [1, 2, 3, 4, 5, 6]

    here = Path(__file__).resolve().parent
    manifest = json.loads(Path('provenance/IMPORT_MANIFEST.json').read_text())
    archival = []
    for name in ('INFINITE_REALIZATION_LIMITS.md', 'OBSERVATIONAL_SUCC_FOUNDATIONS.md'):
        path = 'provenance/origins/fuckingrh/research/2026-10-10/' + name
        entry = next(e for e in manifest['entries'] if e['destination_path'] == path)
        blob = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
        assert blob == entry['destination_git_blob_sha']
        archival.append({'path': path, 'git_blob': blob, 'manifest_match': True})
    origin_object = subprocess.run(['git', 'cat-file', '-t', manifest['source_commit']],
                                   capture_output=True, text=True)
    result = {
        'schema': 'B14-bounded-controls-v1', 'status': 'TESTED MODEL',
        'source_parent': PARENT,
        'import_source_commit': manifest['source_commit'],
        'import_origin_object_check': {'command': 'git cat-file -t ' + manifest['source_commit'],
                                       'exit_code': origin_object.returncode,
                                       'stdout': origin_object.stdout.strip(),
                                       'stderr': origin_object.stderr.strip()},
        'paper_proof_status': 'CLASSICAL; independently written paper derivations; not kernel-checked',
        'primary_sources': [
            {'url': 'https://www.math.uic.edu/~marker/math512/dst.pdf',
             'locator': 'Definition 1.7, Lemma 1.14, Definition 2.39, Example 2.43, Theorem 2.52',
             'accessed': '2026-10-13'},
            {'url': 'https://arxiv.org/pdf/1204.3763', 'locator': 'Sections 3-4',
             'accessed': '2026-10-13'}],
        'command': 'python research/2026-10-13/SWARM_ATLAS/B14_probe.py',
        'exit_code': 0, 'python': sys.version.split()[0],
        'bounds': {'maximum_prefix_depth': 8, 'extension_bits': 16,
                   'parity_sources': 32, 'maximum_delayed_horizon': 16},
        'controls': {'opposite_extension_prefix_pairs': pair_count,
                     'clopen_words': clopen_count,
                     'open_seen_one_positive_read': 3,
                     'open_seen_one_zero_window': 64,
                     'parity_read_counts': reads,
                     'delayed_opposite_parity_pairs': delayed,
                     'marker_input': sample, 'marker_output': encoded},
        'archival_blobs': archival,
        'artifact_sha256': {name: hashlib.sha256((here / name).read_bytes()).hexdigest()
                            for name in ('B14.md', 'B14_probe.py')},
        'limitations': ['No continuum classification was executed.',
                        'No completeness, Baire, or compactness theorem is proved by this probe.',
                        'Finite-extension infinite labels are justified only by B14 paper proofs.',
                        'No full suite or compiler run; principal integration validation remains.'],
    }
    (here / 'B14_receipt.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'prefix_pairs': pair_count,
                      'clopen_words': clopen_count, 'parity_sources': len(reads),
                      'delayed_pairs': len(delayed), 'exit_code': 0}))


if __name__ == '__main__':
    main()
