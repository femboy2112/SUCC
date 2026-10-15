"""Read-only local Git push audit: synthetic bare remote, no network, no mutations."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"scripts"/"audit_local_push_state.py"


def git(repo,*argv):
    run=subprocess.run(["git","-C",str(repo),*argv],capture_output=True,text=True)
    if run.returncode:
        raise AssertionError(f"git {argv} failed: {run.stderr}")
    return run.stdout.strip()


class ReadOnlyRemoteCommitAuditTests(unittest.TestCase):
    def test_local_only_commit_and_untracked_files_are_reported_without_pushing(self):
        with tempfile.TemporaryDirectory() as d:
            base=Path(d)
            remote=base/"remote.git"
            local=base/"local"
            subprocess.run(["git","init","--bare",str(remote)],
                           capture_output=True,check=True)
            subprocess.run(["git","init",str(local)],
                           capture_output=True,check=True)
            git(local,"config","user.email","test@example.invalid")
            git(local,"config","user.name","Source-only auditor")
            git(local,"checkout","-b","main")
            (local/"README.txt").write_text("original\n")
            git(local,"add","README.txt")
            git(local,"commit","-m","initial")
            git(local,"remote","add","origin",str(remote))
            git(local,"push","--set-upstream","origin","main")
            remote_head=git(remote,"rev-parse","refs/heads/main")

            (local/"README.txt").write_text("local next commit\n")
            git(local,"add","README.txt")
            git(local,"commit","-m","unpushed local source")
            git(local,"branch","scratch-only")
            (local/"new-untracked.txt").write_text("uncommitted\n")
            head_before=git(local,"rev-parse","HEAD")
            status_before=git(local,"status","--porcelain=v1","-uall")

            run=subprocess.run([sys.executable,str(AUDIT),
                                "--repo",str(local),"--json"],
                               capture_output=True,text=True,check=True)
            report=json.loads(run.stdout)
            branches={r["branch"]:r for r in report["branches"]}
            self.assertTrue(report["may_have_local_unpushed_work"])
            self.assertEqual(report["current_branch"],"main")
            self.assertEqual(branches["main"]["upstream"],"origin/main")
            self.assertEqual(branches["main"]["ahead"],1)
            self.assertEqual(branches["main"]["behind"],0)
            self.assertIsNone(branches["scratch-only"]["upstream"])
            self.assertEqual(branches["scratch-only"]["classification"],
                             "NO_UPSTREAM_UNKNOWN_REMOTE_RELATION")
            self.assertEqual(len(report["commits_not_on_fetched_remote_refs"]),1)
            self.assertIn("unpushed local source",
                          report["commits_not_on_fetched_remote_refs"][0])
            self.assertTrue(any("new-untracked.txt" in s
                                for s in report["worktree_changes"]))
            self.assertEqual(git(remote,"rev-parse","refs/heads/main"),remote_head)
            self.assertEqual(git(local,"rev-parse","HEAD"),head_before)
            self.assertEqual(git(local,"status","--porcelain=v1","-uall"),
                             status_before)

            strict=subprocess.run([sys.executable,str(AUDIT),
                                   "--repo",str(local),"--strict"],
                                  capture_output=True,text=True)
            self.assertEqual(strict.returncode,2)
            self.assertEqual(git(remote,"rev-parse","refs/heads/main"),remote_head)

    def test_clean_fetched_upstream_reports_no_local_unpushed_work(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)
            subprocess.run(["git","init",str(path)],capture_output=True,check=True)
            git(path,"config","user.email","test@example.invalid")
            git(path,"config","user.name","Auditor")
            (path/"a.txt").write_text("x")
            git(path,"add","a.txt")
            git(path,"commit","-m","root")
            run=subprocess.run([sys.executable,str(AUDIT),"--repo",str(path),"--json"],
                               capture_output=True,text=True,check=True)
            report=json.loads(run.stdout)
            self.assertFalse(report["worktree_changes"])
            # With no fetched remotes, local commits appear as local-only.
            self.assertTrue(report["commits_not_on_fetched_remote_refs"])
            self.assertTrue(report["may_have_local_unpushed_work"])
            self.assertTrue(all(b["upstream"] is None for b in report["branches"]))


if __name__=="__main__":
    unittest.main()
