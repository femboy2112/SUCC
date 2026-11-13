"""Post-derivation RI-01 audit controls, separate from its constructor.

This reviewer shares a model family and BBP source provenance with the
constructor.  Exact finite assertions do not machine-prove the universal
lemma.  The paper audit covers RI-01 through RI-7 only, excluding later
block-ratio extensions, RI-02 and RI-03.  The published irrationality bound
is imported, not re-proved here.
"""
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
import argparse
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name):
    spec = spec_from_file_location("audit_"+name, HERE/(name+".py"))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    r = load("r0_probe")
    g = load("gamma_prime_probe")
    assertions = 0

    def check(condition, label):
        nonlocal assertions
        if not condition:
            raise AssertionError(label)
        assertions += 1

    # Independent constraint elimination: set y=16x+jump and differentiate
    # the resulting one-variable quadratic, instead of using inverse Gram.
    for left in range(13):
        for right in range(13):
            for jump in (-3, -1, 1, 4):
                a = sum((Q(1, 256**j) for j in range(left+1)), Q())
                b = sum((Q(256**j) for j in range(right+1)), Q())
                x = -16*b*jump/(a+256*b)
                y = a*jump/(a+256*b)
                energy = a*b*jump*jump/(a+256*b)
                row = r.gram_minimizer(left, right, jump)
                check((row["x"], row["y"], row["energy"]) == (x, y, energy),
                      "direct one-variable quadratic versus inverse Gram")
                k = max(left, right)
                check(energy >= Q(jump*jump)/(256+Q(255, 256**(k+1)-1)),
                      "one-sided endpoint lower bound")

    # Genuine integer lifts of an inhomogeneous orbit.  Negative h tests the
    # sign absorbed into p/(15|h|), and backward construction keeps all q small.
    for length in range(2, 10):
        for h in (-7, -1, 1, 3):
            forcing = [Q(1, 10000+j) for j in range(1, length+1)]
            for branch in (-3, -1, 0, 2):
                for terminal in (Q(-1, 32), Q(), Q(1, 32)):
                    q = [Q()]*(length+1)
                    q[-1] = terminal
                    for j in range(length-1, -1, -1):
                        q[j] = (q[j+1]-h*forcing[j])/16
                    check(all(abs(v) < Q(1, 16) for v in q), "local arc")
                    fixed = -Q(branch, 15)
                    ell = [0]
                    for j in range(length):
                        ell.append(16*ell[-1]+branch)
                    x = [(fixed+q[j]-ell[j])/h for j in range(length+1)]
                    check(all(x[j+1] == 16*x[j]+forcing[j] for j in range(length)),
                          "literal source recurrence after integer lift")
                    chosen = -branch if h > 0 else branch
                    inverse = x[0]+sum((forcing[j-1]/16**j for j in range(1, length+1)), Q())
                    bound = (2+abs(h)*abs(forcing[-1]))/(15*abs(h)*16**length)
                    check(abs(inverse-Q(chosen, 15*abs(h))) <= bound,
                          "RI-4 denominator, sign and terminal coefficient")

    # Source-selected Green indexing, using only finite rational source data.
    # finite_pi is an explicit BBP partial sum; no transcendental digit oracle.
    for m in (1, 2, 3, 5, 9):
        transitions = 7*m-1
        terminal = 8*m
        depth = terminal+13
        finite_pi = 16*g.orbit(depth)/16**depth
        finite_tail = sum((g.forcing(terminal+j)/16**j for j in range(1, 14)), Q())
        prefix = g.orbit(m+1)+sum((g.forcing(m+1+j)/16**j
                                  for j in range(1, transitions+1)), Q())
        check(prefix == g.orbit(terminal)/16**transitions,
              "block states U_(m+1) through U_(8m)")
        check(16**m*finite_pi-prefix == finite_tail/16**transitions,
              "RI-5 factor16 and q=15|h|16^m indexing")
        check(16*(Q(2, 15)+Q(1, 64*(8*m-1)**2)+Q(1, 64*(8*m)**2)) < 3,
              "RI-5 upper coefficient")

    q = (Q(-1, 16),)+(Q(),)*20
    residuals = tuple(q[j+1]-16*q[j] for j in range(len(q)-1))
    check(residuals == (Q(1),)+(Q(),)*19,
          "boundary-ceiling control: exact energy F(1/16), nonconstant residual")

    proof = (HERE/"R0_INVERSE.md").read_text()
    first = proof.index("## RI-01:")
    next_section = proof.find("\n## ", first+1)
    section = proof[first:next_section if next_section >= 0 else None]
    return {
        "status": "observed exact finite controls plus separately stated same-model paper audit",
        "baseline": g.BASELINE,
        "execution_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "assertions_passed": assertions,
        "gram_parameter_cases": 13*13*4,
        "inverse_arc_cases": 8*4*4*3,
        "source_green_cases": 5,
        "boundary_control": "q0=-1/16, q1=...=q20=0; forcing0; residuals1,0,...; exact energy kappa_star",
        "paper_audit": {
            "scope": "RI-01 finite lemma and RI-4 through RI-7 as read; no later block-ratio extension, RI-02 or RI-03 audit",
            "finding": "no mathematical defect found in this pass",
            "checked": [
                "quiet-transition selection and pairwise-integer residual normalization",
                "single-defect energy cost and local-only cosine coefficient",
                "window endpoints and denominator 255+delta_left+delta_right",
                "constant-branch lift signs for both frequency orientations",
                "source-selected block start, factor16, denominator and exponent",
                "uniform-in-band contradiction and complete-block counting",
                "strict fixed-c scope, non-effective onset, and no R0 consequence",
            ],
            "not_a_machine_proof": True,
            "external_independence": False,
        },
        "inputs": [
            {"path": str((HERE/f).relative_to(ROOT)), "sha256": sha(HERE/f)}
            for f in ("R0_INVERSE.md", "r0_probe.py", "gamma_prime_probe.py")
        ],
        "RI01_section_sha256_at_execution": hashlib.sha256(section.encode()).hexdigest(),
        "audit_code_sha256": sha(Path(__file__).resolve()),
        "primary_import": {
            "authors": "Doron Zeilberger and Wadim Zudilin",
            "statement": "mu(pi) <= 7.103205334137... < 15/2",
            "url": "https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html",
            "published_pdf": "https://msp.org/cnt/2020/9-4/moscow-v9-n4-p06-s.pdf",
            "verification_scope": "published theorem statement verified on primary author page; proof imported, not reproduced",
        },
        "provenance": "same model family; separate algebraic implementation; shared BBP source and standard Fraction arithmetic",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
        print(json.dumps({"assertions_passed": result["assertions_passed"],
                          "output": str(args.output),
                          "RI01_section_sha256_at_execution": result["RI01_section_sha256_at_execution"],
                          "inputs": result["inputs"]}, indent=2))
    else:
        print(text)
