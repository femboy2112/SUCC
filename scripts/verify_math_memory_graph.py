#!/usr/bin/env python3
"""Validate syntax, typed provenance and dependency DAG of curated SUCC memory.

This lint does NOT verify proofs, URLs, branch ancestry, or remote file existence.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

KINDS={"intuition","theorem","defined_comparison","conjecture","counterexample","open_obligation"}
STATUSES={"CLASSICAL","PROVED_LOCAL","TESTED_MODEL","OBSERVED","CONJECTURED","UNVERIFIED","REFUTED","OPEN"}
RELATIONS={"formalizes","candidate_bridge","specializes","shares_source_with","depends_on","motivates","shares_value_with","generalizes","complements","constrains","reduces_to","does_not_imply"}
SOURCES={"user_recollection","github_pr","web","main_repo_doc","new_proof"}


def validate(data: dict) -> list[str]:
    errors=[]
    nodes=data.get("nodes",[])
    edges=data.get("edges",[])
    if data.get("schema_version")!="0.1":errors.append("unsupported schema_version")
    if not isinstance(nodes,list) or not nodes:errors.append("nodes must be a nonempty list");return errors
    byid={}
    for i,n in enumerate(nodes):
        key=n.get("id") if isinstance(n,dict) else None
        if not isinstance(key,str) or not key.startswith("MM-"):
            errors.append(f"node[{i}]: missing canonical MM- id");continue
        if key in byid: errors.append(f"duplicate ID {key}")
        byid[key]=n
        if n.get("kind") not in KINDS:errors.append(f"{key}: unknown kind")
        if n.get("status") not in STATUSES:errors.append(f"{key}: unknown status")
        for field in ("title","statement","scope","limitation","next_probe"):
            if not isinstance(n.get(field),str) or not n[field].strip():
                errors.append(f"{key}: missing {field}")
        sources=n.get("provenance")
        if not isinstance(sources,list) or not sources:
            errors.append(f"{key}: empty provenance")
        else:
            for src in sources:
                if not isinstance(src,dict) or src.get("kind") not in SOURCES:
                    errors.append(f"{key}: invalid provenance source")
                    continue
                if src["kind"]=="github_pr":
                    if not (isinstance(src.get("pr"),int) and src.get("pr")>0 and
                            isinstance(src.get("head_sha"),str) and len(src["head_sha"])==40 and
                            isinstance(src.get("path"),str) and src["path"]):
                        errors.append(f"{key}: incomplete GitHub PR source pin")
                if src["kind"] in ("new_proof","main_repo_doc") and not src.get("path"):
                    errors.append(f"{key}: missing source path")
        if n.get("kind")=="open_obligation" and n.get("status")!="OPEN":
            errors.append(f"{key}: open obligation mislabelled")
    dependencies={x:set() for x in byid}
    for i,e in enumerate(edges):
        if not isinstance(e,dict):errors.append(f"edge[{i}]: invalid edge");continue
        a,b,rel=e.get("source"),e.get("target"),e.get("relation")
        if a not in byid or b not in byid:errors.append(f"edge[{i}]: unknown endpoint")
        if rel not in RELATIONS:errors.append(f"edge[{i}]: illegal relation {rel}")
        if not isinstance(e.get("evidence"),str) or not e["evidence"].strip():
            errors.append(f"edge[{i}]: missing evidence")
        if rel=="depends_on" and a in byid and b in byid:
            if a==b:errors.append(f"self-dependency {a}")
            dependencies[a].add(b)
    color={}
    def visit(node):
        if color.get(node)==1:errors.append(f"cyclic depends_on chain at {node}");return
        if color.get(node)==2:return
        color[node]=1
        for dep in sorted(dependencies[node]):visit(dep)
        color[node]=2
    for node in sorted(byid):visit(node)
    return errors


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path",type=Path,default=Path(__file__).resolve().parents[1]/"docs/math_memory/RELATION_GRAPH.json")
    args=parser.parse_args(argv)
    data=json.loads(args.path.read_text(encoding="utf-8"))
    problems=validate(data)
    if problems:
        for e in problems:print("FAIL:",e)
        return 1
    print(f"PASS: {len(data['nodes'])} typed nodes, {len(data['edges'])} typed edges; proofs NOT independently checked")
    return 0

if __name__=='__main__':raise SystemExit(main())
