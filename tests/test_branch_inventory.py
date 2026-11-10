"""An older-main fork must not be charged with main's later additions."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'branch_inventory.py'


class InventoryForkRegression(unittest.TestCase):
    def test_own_diff_uses_fork_point_when_main_has_advanced(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root,
                                               stderr=subprocess.DEVNULL, text=True).strip()
            git('init', '-b', 'main')
            git('config', 'user.name', 'Inventory fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            (root / 'base').write_text('base\n')
            git('add', 'base'); git('commit', '-m', 'base')
            fork = git('rev-parse', 'HEAD')
            git('checkout', '-b', 'research')
            (root / 'research-only').write_text('research\n')
            git('add', 'research-only'); git('commit', '-m', 'research')
            research = git('rev-parse', 'HEAD')
            git('checkout', 'main')
            (root / 'later-main').write_text('main\n')
            git('add', 'later-main'); git('commit', '-m', 'main advanced')
            prs = root / 'prs.json'
            prs.write_text(json.dumps([dict(number=1, title='research',
                headRefName='research', headRefOid=research, baseRefName='main')]))
            out = root / 'inventory.json'
            result = subprocess.run([sys.executable, str(SCRIPT), '--main', 'main',
                '--integration', 'research', '--prs', str(prs), '--repo', 'fixture/repo',
                '--out', str(out), '--no-ci'], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            row = json.loads(out.read_text())['prs'][0]
            self.assertEqual(row['own_base'], fork)
            self.assertEqual(row['own_commits'], [research])
            self.assertEqual([(f['status'], f['path']) for f in row['own_changed_files']],
                             [('A', 'research-only')])
