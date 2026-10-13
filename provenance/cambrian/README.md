# Exact Cambrian local commit history

The connected GitHub API publishes an integration commit with the tested content
tree. Its commit identity differs from the local history because the API supplies
its own author/committer metadata. This archive preserves the exact original six
worker commits, eight audit commits and integrated research snapshot, including
the original E30 paper assertion and its separately reviewed correction. It is
not a replacement for the protected historical import archive.

`BUNDLE_MANIFEST.json` lists all fifteen branch tips, the prerequisite, sizes and
SHA-256 hashes. The bundle ends at the integration snapshot before adding the
bundle itself; it cannot recursively contain its own packaging commit.

In a checkout containing PR48 commit `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`:

```sh
python -c "import base64,pathlib; p=pathlib.Path('provenance/cambrian/CAMBRIAN_COMMITS.bundle.base64'); pathlib.Path('/tmp/CAMBRIAN_COMMITS.bundle').write_bytes(base64.b64decode(p.read_bytes()))"
git bundle verify /tmp/CAMBRIAN_COMMITS.bundle
git bundle list-heads /tmp/CAMBRIAN_COMMITS.bundle
git fetch /tmp/CAMBRIAN_COMMITS.bundle 'refs/heads/*:refs/remotes/cambrian-archive/*'
```

The final fetch creates only archive remote-tracking references. It does not
change the current branch, main, defaults, tags or working files.
