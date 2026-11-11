"""Tiny Git fixtures test loss detection, ancestry and explicit repair scope."""
import copy
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'main_xxiv_manifest.py'
spec = importlib.util.spec_from_file_location('main_xxiv_manifest', SCRIPT)
manifest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manifest)


class ManifestLossRegression(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.old_cwd = Path.cwd()
        os.chdir(self.root)
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Manifest fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.write('provenance/frozen.txt', 'archive\n')
        self.write('baseline.txt', 'base\n')
        self.base = self.commit('base')
        self.git('checkout', '-b', 'research')
        self.write('research/result.md', 'finite theorem\n')
        self.head = self.commit('research contribution')
        self.inventory = {'main': self.base, 'prs': [{
            'number': 1, 'title': 'fixture result', 'branch': 'research',
            'head': self.head, 'own_base': self.base}]}
        self.prs = [{'number': 1, 'head_sha': self.head}]
        manifest.tree.cache_clear()
        manifest.digest.cache_clear()

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

    def build(self, ref='HEAD', decisions=None):
        return manifest.generate(self.inventory, self.prs, self.base, ref, decisions)

    def test_newer_documentary_commit_avoids_self_hash_but_rejects_lost_bytes(self):
        data = self.build()
        self.assertEqual(manifest.check(data, 'HEAD'), [])
        self.write('manifest-note.md', 'new integration receipt\n')
        self.commit('document manifest without self-hash')
        self.assertEqual(manifest.check(data, 'HEAD'), [])
        self.write('research/result.md', 'silently replaced theorem\n')
        self.commit('bad replacement')
        self.assertTrue(any('Final bytes changed' in e for e in manifest.check(data, 'HEAD')))

    def test_protected_bytes_and_missing_ancestry_fail(self):
        data = self.build()
        self.assertTrue(any('Missing ancestry' in e for e in manifest.check(data, self.base)))
        self.write('provenance/frozen.txt', 'mutant archive\n')
        self.commit('bad archive change')
        self.assertTrue(any('Protected bytes changed' in e for e in manifest.check(data, 'HEAD')))

    def test_missing_contribution_row_and_file_are_detected(self):
        data = self.build()
        removed = copy.deepcopy(data)
        removed['contributions'] = []
        self.assertIn('Contribution row coverage mismatch', manifest.check(removed, 'HEAD'))
        data['contributions'][0]['files'] = []
        self.assertTrue(any('path coverage mismatch' in e for e in manifest.check(data, 'HEAD')))

    def test_unreviewed_repair_fails_and_explicit_repair_is_pinned(self):
        self.write('research/result.md', 'corrected finite theorem\n')
        self.commit('reviewed repair')
        data = self.build()
        self.assertTrue(any('Unaccounted' in e for e in manifest.check(data, 'HEAD')))
        decisions = {'paths': {'1:research/result.md': {'disposition': 'repaired',
            'reason': 'Fixture correction with a retained hostile control',
            'authority': ['fixture proof review']}}}
        data = self.build(decisions=decisions)
        self.assertEqual(manifest.check(data, 'HEAD'), [])
        self.write('research/result.md', 'a further unreviewed edit\n')
        self.commit('later change')
        self.assertTrue(any('Final bytes changed' in e for e in manifest.check(data, 'HEAD')))

    def test_archival_redirect_requires_exact_origin_bytes(self):
        self.git('mv', 'research/result.md', 'research/result-alternative.md')
        self.commit('archive alternate implementation')
        decisions = {'paths': {'1:research/result.md': {
            'canonical_destination': 'research/result-alternative.md',
            'disposition': 'archived_alternative', 'reason': 'Avoid namespace collision',
            'authority': ['fixture independent alternative']}}}
        data = self.build(decisions=decisions)
        self.assertEqual(manifest.check(data, 'HEAD'), [])
        self.write('research/result-alternative.md', 'mutated archive\n')
        self.commit('bad archive')
        data = self.build(decisions=decisions)
        self.assertTrue(any('not byte-identical' in e for e in manifest.check(data, 'HEAD')))

    def test_identical_blob_symlink_substitution_is_not_preservation(self):
        data = self.build()
        blob = self.git('rev-parse', 'HEAD:research/result.md')
        self.git('update-index', '--cacheinfo', '120000,' + blob + ',research/result.md')
        self.git('commit', '-m', 'replace regular theorem with identical-blob symlink')
        self.assertTrue(any('Final bytes changed' in e for e in manifest.check(data, 'HEAD')))

    def test_checkpoint_erasure_and_protected_row_erasure_fail(self):
        data = self.build()
        forged = copy.deepcopy(data)
        row = forged['contributions'][0]
        row.update(head_commit=self.base, head_tree=self.git('rev-parse', self.base + '^{tree}'),
                   contribution_parent=self.base, contribution_commit=self.base,
                   contribution_tree=self.git('rev-parse', self.base + '^{tree}'),
                   contribution_commits=[], files=[])
        self.assertTrue(any('checkpoint mismatch' in e for e in manifest.check(forged, 'HEAD')))
        forged = copy.deepcopy(data)
        forged['protected'] = []
        self.assertIn('Protected path coverage mismatch', manifest.check(forged, 'HEAD'))


if __name__ == '__main__':
    unittest.main()
