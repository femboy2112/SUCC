"""Tiny Git fixtures: the Main XXV manifest must detect lost bytes, lost ancestry and touched archives."""
import copy
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'main_xxv_manifest.py'
spec = importlib.util.spec_from_file_location('main_xxv_manifest', SCRIPT)
manifest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manifest)


class StackManifestRegression(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.old_cwd = Path.cwd()
        os.chdir(self.root)
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Manifest fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.write('provenance/frozen.txt', 'archive\n')
        self.write('catalog.json', '{}\n')
        self.base = self.commit('base')
        self.git('checkout', '-b', 'round-one')
        self.write('research/one.md', 'first theorem\n')
        self.write('research/shared.md', 'draft\n')
        self.write('catalog.json', '{"one": 1}\n')
        self.first = self.commit('round one')
        self.git('checkout', '-b', 'round-two')
        self.write('research/two.md', 'second theorem\n')
        self.write('research/shared.md', 'repaired by round two\n')
        self.second = self.commit('round two')
        self.origins = [
            {'id': 'round-one', 'pr': 1, 'branch': 'round-one', 'head': self.first,
             'own_base': self.base, 'claim': 'fixture', 'claim_status': 'fixture'},
            {'id': 'round-two', 'pr': None, 'branch': 'round-two', 'head': self.second,
             'own_base': self.first, 'claim': 'fixture', 'claim_status': 'fixture'},
        ]

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.folder.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', *args], stderr=subprocess.DEVNULL, text=True).strip()

    def write(self, path, content):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)

    def commit(self, message):
        self.git('add', '.')
        self.git('commit', '-m', message)
        return self.git('rev-parse', 'HEAD')

    def build(self):
        return manifest.generate(self.origins, self.base, 'HEAD', ['provenance/frozen.txt'],
                                 regenerated=('catalog.json',))

    def test_stack_passes_and_later_documentary_commits_are_allowed(self):
        data = self.build()
        self.assertEqual(manifest.check(data, 'HEAD'), [])
        # a path rewritten by the later origin is not held to the earlier origin's bytes
        self.assertEqual(self.git('show', 'HEAD:research/shared.md'), 'repaired by round two')
        self.write('integration-note.md', 'receipt\n')
        self.write('catalog.json', '{"regenerated": true}\n')
        self.commit('integration documents and regenerated catalog')
        self.assertEqual(manifest.check(data, 'HEAD'), [])

    def test_silently_replaced_theorem_is_detected(self):
        data = self.build()
        self.write('research/one.md', 'silently replaced theorem\n')
        self.commit('bad replacement')
        self.assertTrue(any('Final bytes changed: round-one:research/one.md' in e
                            for e in manifest.check(data, 'HEAD')))
        self.write('research/one.md', 'first theorem\n')
        self.write('research/shared.md', 'silently replaced again\n')
        self.commit('bad replacement of the later origin')
        errors = manifest.check(data, 'HEAD')
        self.assertTrue(any('round-two:research/shared.md' in e for e in errors))
        self.assertFalse(any('round-one:research/one.md' in e for e in errors))

    def test_missing_ancestry_protected_bytes_and_empty_rows_fail(self):
        data = self.build()
        self.assertTrue(any('Missing ancestry: round-two' in e for e in manifest.check(data, self.first)))
        self.write('provenance/frozen.txt', 'mutant archive\n')
        self.commit('bad archive change')
        self.assertTrue(any('Protected bytes changed' in e for e in manifest.check(data, 'HEAD')))
        removed = copy.deepcopy(data)
        removed['origins'] = []
        self.assertIn('Contribution row coverage mismatch', manifest.check(removed, 'HEAD'))


if __name__ == '__main__':
    unittest.main()
