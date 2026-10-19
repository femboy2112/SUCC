#!/usr/bin/env python3
"""Read-only Git/GitHub research ancestry snapshot; PR labels are not ancestry."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import datetime as dt
import json
from pathlib import Path
import subprocess


def run(*args):
    return subprocess.check_output(args, text=True).strip()


def api(path):
    return json.loads(run("gh", "api", "repos/femboy2112/SUCC"+("/"+path if path else "")))


def pr(number):
    p = api(f"pulls/{number}")
    files, page = [], 1
    while True:
        batch = api(f"pulls/{number}/files?per_page=100&page={page}")
        files.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    sha = p["head"]["sha"]
    return dict(number=number, title=p["title"], state=p["state"], draft=p["draft"],
                merged_at=p["merged_at"], url=p["html_url"], body=p["body"],
                head=sha, head_ref=p["head"]["ref"], base=p["base"]["sha"],
                base_ref=p["base"]["ref"], files=[f["filename"] for f in files],
                check_runs=api(f"commits/{sha}/check-runs?per_page=100"))


def ancestor(a, b):
    return subprocess.run(["git", "merge-base", "--is-ancestor", a, b]).returncode == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prs", nargs="+", type=int, default=list(range(153,178)))
    parser.add_argument("--output", default="research/2026-10-18/institute/github_snapshot.json")
    args = parser.parse_args()
    repo = api("")
    default = repo["default_branch"]
    head = run("git", "rev-parse", "origin/"+default)
    with ThreadPoolExecutor(max_workers=3) as pool:
        prs = list(pool.map(pr, args.prs))
    for p in prs:
        for check in p["check_runs"]["check_runs"]:
            for key in list(check):
                if key not in ("id", "name", "head_sha", "status", "conclusion", "started_at",
                               "completed_at", "html_url", "details_url", "external_id"):
                    del check[key]
        p["integrated_by_ancestry"] = ancestor(p["head"], head)
        p["merge_base_default"] = run("git", "merge-base", head, p["head"])
        p["head_ancestors_in_snapshot"] = [q["number"] for q in prs
            if q["number"] != p["number"] and ancestor(q["head"], p["head"])]
        p["commits_since_default"] = int(run("git", "rev-list", "--count", head+".."+p["head"]))
    # Stable patch IDs detect copied changes independently of commit identity.
    commits = set()
    for p in prs:
        commits.update(run("git", "rev-list", "--no-merges", head+".."+p["head"]).splitlines())
    families = {}
    for commit in sorted(commits):
        diff = subprocess.check_output(["git", "show", "--pretty=format:", commit])
        patch = subprocess.check_output(["git", "patch-id", "--stable"], input=diff).decode().split()
        if patch:
            families.setdefault(patch[0], []).append(commit)
    record = dict(captured_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  default_branch=default, default_head=head, prs=prs,
                  duplicate_patch_families=[dict(patch_id=k, commits=v)
                      for k,v in families.items() if len(v)>1],
                  interpretation="Ancestry and byte/patch identity only; not theorem verification.")
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"path":str(path), "default_head":head, "prs":len(prs),
                      "duplicate_patch_families":len(record["duplicate_patch_families"])}))


if __name__ == "__main__":
    main()
