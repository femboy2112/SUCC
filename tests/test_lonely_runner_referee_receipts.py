import json
from pathlib import Path
import tempfile
import unittest

from scripts.lonely_runner_referee_receipts import deterministic_gzip, pack, verify


class RefereeReceiptTests(unittest.TestCase):
    def test_deterministic_roundtrip_preserves_original_before_removal(self):
        raw = b'{"proof": "finite exact receipt", "n": 21}\n'
        self.assertEqual(deterministic_gzip(raw), deterministic_gzip(raw))
        self.assertEqual(deterministic_gzip(raw)[4:8], bytes(4))
        with tempfile.TemporaryDirectory() as temp:
            source, archive = Path(temp)/"source", Path(temp)/"archive"
            source.mkdir()
            (source/"census-n21.json").write_bytes(raw)
            index = pack(source, archive, remove_raw=True)
            self.assertEqual(index["file_count"], 1)
            self.assertFalse((source/"census-n21.json").exists())
            self.assertEqual((archive/"census-n21.json").read_bytes(), raw)
            self.assertEqual(verify(source), index)
            data = json.loads((source/"receipts-index.json").read_text())
            data["files"][0]["raw_sha256"] = "0"*64
            (source/"receipts-index.json").write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "integrity"):
                verify(source)

    def test_conflicting_archive_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            source, archive = Path(temp)/"source", Path(temp)/"archive"
            source.mkdir(); archive.mkdir()
            (source/"census-n21.json").write_text("new")
            (archive/"census-n21.json").write_text("old")
            with self.assertRaisesRegex(ValueError, "conflict"):
                pack(source, archive, remove_raw=True)
            self.assertEqual((source/"census-n21.json").read_text(), "new")
            self.assertEqual((archive/"census-n21.json").read_text(), "old")


if __name__ == "__main__":
    unittest.main()
