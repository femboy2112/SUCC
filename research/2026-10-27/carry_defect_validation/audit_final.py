"""Read-only final audit of frozen sources, native logs and finite kernel scope."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    snapshot = json.loads((OUT/'python_source_snapshot.json').read_text())
    actual = {str(p.relative_to(ROOT)): digest(p)
              for folder in ('observational_succ', 'tests')
              for p in sorted((ROOT/folder).rglob('*.py'))}
    assert actual == snapshot, 'production/test source changed after suite start'
    for name in ('focused', 'full_unittest', 'provenance', 'observer', 'ordinal'):
        record = json.loads((OUT/f'{name}_result.json').read_text())
        assert record['exit_code'] == 0 and record['production_test_sources_unchanged']
        assert digest(OUT/record['log']) == record['log_sha256']
    kernel = json.loads((OUT/'lean/kernel-observation.json').read_text())
    assert kernel['status'] == 'KERNEL_CHECKED'
    assert len(kernel['theorem_exports']) == 4
    assert len(kernel['negative_controls']) == 4
    assert all(x['passed'] for x in kernel['negative_controls'])
    for name, expected in kernel['source_hashes'].items():
        assert digest(ROOT/name) == expected, name
    for entry in kernel['commands']:
        assert digest(OUT/'lean'/entry['log']) == entry['log_sha256']
    for theorem in kernel['theorem_exports'].values():
        assert set(theorem['axioms']) <= {'propext', 'Classical.choice', 'Quot.sound'}
    assert not kernel['normality_proved']
    assert not kernel['bbp_forcing_and_analytic_limits_formalized']
    markdown = json.loads((OUT/'markdown_audit.json').read_text())
    for entry in markdown:
        assert digest(ROOT/entry['path']) == entry['source_sha256'], entry['path']
    mutations = json.loads((OUT/'receipt_mutation_results.json').read_text())
    assert all(x['expected_behavior_observed'] for x in mutations)
    for entry in mutations:
        assert digest(OUT/entry['log']) == entry['log_sha256']
    record = {'frozen_python_files': len(actual), 'all_native_logs_verified': True,
              'finite_lean_declarations': 4, 'paired_kernel_controls': 4,
              'rendered_documents_verified': len(markdown),
              'receipt_mutation_behaviors_verified': len(mutations),
              'normality_proved': False, 'numerical_onset_certified': False}
    (OUT/'final_audit.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record))


if __name__ == '__main__':
    main()
