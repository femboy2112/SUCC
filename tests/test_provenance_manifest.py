"""Exact Git-blob checks prevent unnoticed rewriting of imported evidence."""
import hashlib
import json
import unittest
from pathlib import Path

from scripts.verify_provenance import git_blob_sha, verify


class ImportedSourceProvenanceTests(unittest.TestCase):
    def test_original_source_files_are_present_with_pinned_git_blobs(self):
        result = verify()
        self.assertEqual(result["status"], "SOURCE_PROVENANCE_VERIFIED")
        self.assertEqual(result["source_commit"],
                         "ba075348b7bcc66d938b3e0ca96c26e95bba340a")
        self.assertEqual(result["items"], 72)
        self.assertEqual(result["mechanical_namespace_migrations"], 55)
        self.assertEqual(result["byte_identical_research_archives"], 17)
        self.assertFalse(result["establishes_mathematical_truth"])

    def test_git_blob_sha_matches_known_reference(self):
        # Git's standard empty-file object identity.
        self.assertEqual(git_blob_sha(b""),
                         "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391")
        self.assertEqual(
            git_blob_sha(b"hello\n"),
            hashlib.sha1(b"blob 6\0hello\n").hexdigest())


if __name__ == "__main__":
    unittest.main()
