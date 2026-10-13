import Cache.Requests
open Cache IO Hashing Requests System in
-- Original pinned source hashes/download/unpack; only selected dependency roots.
-- Browser-widget release fetching and global Mathlib.lean hashing are excluded.
def main : IO Unit := CacheM.run do
  validateLeanTar
  let paths := [FilePath.mk "Mathlib/Topology/Constructions.lean", FilePath.mk "Mathlib/Topology/Compactness/Compact.lean", FilePath.mk "Mathlib/Topology/Homeomorph.lean", FilePath.mk "Mathlib/Topology/Separation/Basic.lean"]
  let memo ← StateT.run (paths.toArray.mapM getFileHash) { rootHash := ← getRootHash }
  let hashes := memo.2.hashMap
  IO.println s!"Selective dependency modules: {hashes.size}"
  downloadFiles hashes false false
  unpackCache hashes false
