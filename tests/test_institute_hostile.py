"""Hostile cross-checks; schema fixtures do not authenticate kernel execution.

The trace controls and residue checks are finite tests. Universal conclusions
are derived separately in INSTITUTE_HOSTILE_AUDIT.md.
"""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import combinations, product
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import json
import random
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from observational_succ.institute_audit import audit_registry
from observational_succ.institute_causal import (
    SourceSystem, Step, distinguishing_word, refine_quotient,
)
from observational_succ.source_proof_certificate import CapsuleError, evidence_file
from scripts import institute_schur_probe as Gamma
from scripts import institute_eta_probe as Eta


class KernelTransportHostileTests(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        def git(*args):
            return subprocess.check_output(["git", *args], cwd=self.root,
                                           stderr=subprocess.DEVNULL, text=True).strip()
        git("init", "--quiet")
        (self.root / "Proof.lean").write_text("theorem fixture : True := True.intro\n")
        (self.root / "lean-toolchain").write_text("leanprover/lean4:v4.14.0\n")
        src = evidence_file(self.root, "Proof.lean", "LEAN_SOURCE")
        ax = dict(toolchain="leanprover/lean4:v4.14.0", declarations={"fixture": []})
        # Deliberately synthetic schema fixtures, NOT a claimed compiler run.
        receipt = dict(ax, source_sha256=src["sha256"], exit_code=0,
                       negative_control_exit_code=1)
        (self.root / "axioms.json").write_text(json.dumps(ax))
        (self.root / "receipt.json").write_text(json.dumps(receipt))
        git("add", ".")
        git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
            "commit", "--quiet", "-m", "synthetic schema fixture")
        a = dict(
            claim_id="A", authority="LEAN_KERNEL_PROVED", statement="Schema fixture",
            source="S", operations_relations="f", target_carrier="C",
            observation_morphisms="q", topology_measure="discrete",
            universal_property="factorization", comparison_maps="identity",
            source_identity="synthetic", source_epoch=0,
            hypotheses=["H"], dependencies=[], scope="UNIVERSAL",
            conclusion_mode="THEOREM_UNDER_HYPOTHESES", kernel_declarations=["fixture"],
            evidence=[src, evidence_file(self.root, "axioms.json", "AXIOM_MANIFEST"),
                      evidence_file(self.root, "receipt.json", "LEAN_RECEIPT")],
            access={k: "fixture" for k in ("permitted_observations", "constructible_witness",
                    "oracle", "probe_discrimination", "proof_theory", "execution_cost")},
            adversarial={k: "fixture" for k in ("domain_tests", "negative_examples",
                         "source_mutations", "replay")},
            signature=dict(source="S", carrier="C", topology="discrete"),
            quantifiers="all fixture objects", prior_art="fixture", novelty="none",
            next_discriminator="mutation", independent_check="fixture", proof_debt=[],
            git_sources=[dict(commit=git("rev-parse", "HEAD"), path="Proof.lean",
                              blob=git("rev-parse", "HEAD:Proof.lean"))])
        b = deepcopy(a)
        b.update(claim_id="B", dependencies=["A"])
        b["signature"]["topology"] = "completion"
        self.edge = dict(**{"from": "A", "to": "B"}, input=deepcopy(a["signature"]),
                         output=deepcopy(b["signature"]), authority="LEAN_KERNEL_PROVED",
                         obligation="continuity", evidence=b["evidence"][0])
        self.registry = dict(schema="SUCC_INSTITUTE_v1", claims=[a, b],
                             transports=[self.edge])

    def test_paper_comparison_cannot_feed_kernel_authority(self):
        self.edge.update(authority="PAPER_PROVED", kernel_declarations=["fixture"])
        with self.assertRaises(CapsuleError):
            audit_registry(self.registry, self.root)

    def test_kernel_comparison_needs_explicit_declarations(self):
        with self.assertRaises(CapsuleError):
            audit_registry(self.registry, self.root)

    def test_unknown_kernel_comparison_declaration_is_rejected(self):
        self.edge["kernel_declarations"] = ["unproved_transport"]
        with self.assertRaises(CapsuleError):
            audit_registry(self.registry, self.root)

    def test_declared_transport_remains_only_byte_integrity(self):
        self.edge["kernel_declarations"] = ["fixture"]
        result = audit_registry(self.registry, self.root)
        self.assertEqual(result["audit"], "CONTRACTS_AND_BYTES_VALID")
        self.assertEqual(result["theorems_proved_by_this_audit"], [])
        self.assertTrue(all(c["semantic_authority_issued"] is None for c in result["claims"]))


def raw_trace(model, state, word):
    """Literal table replay, independent of production pair search/refinement."""
    trace = [model.observation[state]]
    for action in word:
        edge = model.transitions.get((state, action))
        if edge is None:
            return tuple(trace + [("unavailable", action)])
        state = edge.target
        trace.append((action, edge.outcome, edge.cost, model.observation[state]))
    return tuple(trace)


class MathematicalHostileControls(unittest.TestCase):
    def test_replay_rejects_beyond_pinned_source_domain_before_execution(self):
        # The pinned source itself supports only J=1..24, even though the
        # general Gamma coefficient theorem has no such finite cutoff.
        for cutoff, degree in ((25, 80), (64, 80), (0, 80), (8, 0), (8, 257),
                               (True, 80), (8, True)):
            with self.subTest(cutoff=cutoff, degree=degree):
                with patch.object(Gamma.subprocess, "run", side_effect=
                                  AssertionError("invalid request reached execution")):
                    with self.assertRaises(ValueError):
                        Gamma.replay_pr177(cutoff, degree)

    def test_four_state_two_action_trace_search(self):
        rng = random.Random(20261018)
        states, actions = ("s0", "s1", "s2", "s3"), ("a", "b")
        words = [w for size in range(5) for w in product(actions, repeat=size)]
        checked = 0
        for index in range(96):
            transitions = {}
            for state, action in product(states, actions):
                if rng.randrange(4):
                    transitions[state, action] = Step(
                        rng.choice(states), rng.choice(("yes", "no")),
                        rng.choice((Q(0), Q(1, 3), Q(2))))
            model = SourceSystem(
                "hostile-" + str(index), "declared-finite-table", states, actions,
                {s: "root" for s in states},
                {s: rng.choice(("x", "y")) for s in states}, transitions)
            q, _ = refine_quotient(model)
            for left, right in combinations(states, 2):
                witnesses = [w for w in words if raw_trace(model, left, w) !=
                             raw_trace(model, right, w)]
                witness = distinguishing_word(model, left, right)
                self.assertEqual(q[left] == q[right], not witnesses)
                self.assertEqual(witness is None, not witnesses)
                if witness is not None:
                    self.assertNotEqual(raw_trace(model, left, witness),
                                        raw_trace(model, right, witness))
                    self.assertEqual(len(witness), len(witnesses[0]))
                checked += 1
        self.assertEqual(checked, 576)

    def test_exact_harmonic_residue_discrepancy_controls(self):
        last_norm = Q(2)
        for size in (1, 2, 11, 37, 128, 512):
            harmonic = sum((Q(1, n) for n in range(1, size + 1)), Q())
            self.assertLess(Q(1) / harmonic, last_norm)
            last_norm = Q(1) / harmonic
            for modulus in (2, 3, 7, 11):
                masses = [sum((Q(1, n) for n in range(1, size + 1)
                               if n % modulus == residue), Q())
                          for residue in range(modulus)]
                self.assertEqual(sum(masses, Q()), harmonic)
                for mass in masses:
                    # Abel summation gives this bound for every N, m, r.
                    self.assertLessEqual(abs(mass - harmonic / modulus), 1)
                    self.assertLessEqual(abs(mass / harmonic - Q(1, modulus)),
                                         Q(1) / harmonic)


class YoungBudgetHostileControls(unittest.TestCase):
    def test_strict_squaring_branches_and_degenerate_boundary(self):
        # Exact square roots here provide a separate scalar oracle.
        for m, e, energy, expected in ((1, 1, -2, True), (1, 1, 3, True),
                                       (1, 1, 4, False), (1, 1, 5, False),
                                       (0, 1, Q(1, 2), True), (0, 1, 1, False),
                                       (1, 0, 1, False)):
            T = ((Q(energy), Q(0)), (Q(0), Q(energy)))
            M = ((Q(m), Q(0)), (Q(0), Q(m)))
            result = Eta.triangle_obstruction(T, M, Q(1), (Q(e), Q(0)), (Q(1), Q(0)))
            self.assertEqual(result["triangle_certificate_strictly_negative"], expected)
            self.assertEqual(expected, energy < (isqrt(m) + e)**2)
            self.assertFalse(result["genuine_source_negative"])
        # The equality boundary need not be attained at a finite eta.
        identity = ((Q(1), Q(0)), (Q(0), Q(1)))
        self.assertLess(Eta.lower(identity, identity, Q(1), (Q(0), Q(0)), Q(1))[0][0], 0)
        # A bad fixed eta is not automatically a universal obstruction.
        T = ((Q(5), Q(0)), (Q(0), Q(5)))
        self.assertLess(Eta.lower(T, identity, Q(1), (Q(1), Q(0)), Q(1, 4))[0][0], 0)
        self.assertGreater(Eta.lower(T, identity, Q(1), (Q(1), Q(0)), Q(1))[0][0], 0)

    def test_scalar_and_diagonal_penalties_dominate_triangle_with_mixed_signs(self):
        M = ((Q(1), Q(2)), (Q(2), Q(4)))
        c, errors = (Q(1), Q(-2)), (Q(1, 3), Q(2, 5))
        # c'Mc=9, sum |ci|delta_i=17/15; cancellation in M is retained.
        triangle = (Q(3) + Q(17, 15))**2
        zero = ((Q(0), Q(0)), (Q(0), Q(0)))
        for eta in (Q(1, 7), Q(1, 2), Q(1), Q(3), Q(17)):
            for theta in (None, Q(1, 7), Q(1, 2), Q(1), Q(3), Q(17)):
                matrix = Eta.lower(zero, M, Q(1), errors, eta, theta)
                penalty = -sum((c[i]*matrix[i][j]*c[j]
                                for i in range(2) for j in range(2)), Q())
                self.assertGreaterEqual(penalty, triangle)

    def test_sealed_j24_decomposition_and_nominal_obstruction(self):
        root = Path(__file__).resolve().parents[1] / "research/2026-10-18"
        source_path = root / "INSTITUTE_GAMMA_ETA_SOURCE.json"
        source = json.loads(source_path.read_text())
        receipt = json.loads((root / "INSTITUTE_GAMMA_ETA_SEARCH.json").read_text())
        self.assertEqual(sha256(source_path.read_bytes()).hexdigest(),
                         receipt["source_decomposition_sha256"])
        # The original source's clamped polynomials are retained verbatim;
        # Legendre primitives and norms use different formulas below.
        clamped = {1: (Q(15, 16), 0, -75, 0, 1050, 0, -5040, 0, 7920),
                   0: (0, Q(105, 8), 0, -490, 0, 5292, 0, -22176, 0, 32032)}

        def primitive(n):
            p = [Q(0)] * (n + 2)
            for j in range(n // 2 + 1):
                k = n - 2*j
                p[k + 1] = Q((-1)**j * factorial(2*n - 2*j),
                    2**n * factorial(j) * factorial(n-j) * factorial(k)) * 2**k / (k+1)
            p[0] = -sum((v * (-Q(1, 2))**i for i, v in enumerate(p)), Q())
            return p

        def derivative(p):
            return [i*p[i] for i in range(1, len(p))]

        def norm2(p):
            return sum((a*b / Q(2**(i+j) * (i+j+1))
                for i, a in enumerate(p) for j, b in enumerate(p) if (i+j) % 2 == 0), Q())

        def sqrtup(x):
            scale = 10**10
            k = isqrt(x.numerator * scale**2 // x.denominator)
            if Q(k*k, scale**2) != x:
                k += 1
            bound = Q(k, scale)
            self.assertGreaterEqual(bound**2, x)
            if k:
                self.assertLess((bound - Q(1, scale))**2, x)
            return bound

        for parity, data in source["four_original_parity_Schur_blocks"].items():
            rec = receipt["blocks"][parity]
            M = [[Q(v) for v in row] for row in data["surrogate_QE_action_residual_gram_exact"]]
            self.assertEqual(M[0][1], M[1][0])
            self.assertTrue(M[0][0] >= 0 and M[1][1] >= 0 and
                            M[0][0]*M[1][1] >= M[0][1]**2)
            energy = [[[Q(v) for v in pair] for pair in row]
                      for row in data["genuine_signed_qJ_intervals"]]
            tail = [[Q(v) for v in row] for row in data["genuine_infinite_Gamma_tail_lower_Gram"]]
            tail_psd = tail[0][0] >= 0 and tail[1][1] >= 0 and tail[0][0]*tail[1][1] >= tail[0][1]**2
            self.assertEqual(tail_psd, data["source_tail_matrix_is_PSD"])
            if not tail_psd:
                tail = [[Q(0)]*2 for _ in range(2)]
            radius = [sum(((hi-lo)/2 for lo, hi in row), Q()) for row in energy]
            T = [[sum(energy[i][j])/2 + tail[i][j] - (radius[i] if i == j else 0)
                  for j in range(2)] for i in range(2)]
            errors = []
            for index, coef, finite in zip(data["indices"], data["fitted_high_coefficients"],
                                          data["finite_source_action_error_each"]):
                p, q, cp = primitive(index), primitive(5 if index % 2 else 6), clamped[index % 2]
                h = [(p[i] if i < len(p) else Q(0)) - (q[i] if i < len(q) else Q(0)) -
                     Q(coef)*(cp[i] if i < len(cp) else Q(0))
                     for i in range(max(len(p), len(q), len(cp)))]
                dh, ddh = derivative(h), derivative(derivative(h))
                for poly, x in product((h, dh), (-Q(1, 2), Q(1, 2))):
                    self.assertEqual(sum((a*x**i for i, a in enumerate(poly)), Q()), 0)
                errors.append(Q(finite) + min(Q(13, 1520)*sqrtup(norm2(dh)),
                                             Q(2, 9025)*sqrtup(norm2(ddh))))
            self.assertEqual(T, [[Q(v) for v in row] for row in rec["source_energy_lower_matrix"]])
            self.assertEqual(M, [[Q(v) for v in row] for row in rec["continuum_residual_Gram"]])
            self.assertEqual(errors, [Q(v) for v in rec["combined_action_errors"]])
            kappa = Q(data["source_kappa"])
            self.assertGreater(kappa, 0)
            self.assertTrue(all(d >= 0 for d in errors))
            witness = rec["triangle_obstruction_witness"]
            self.assertEqual([Q(v) for v in witness["direction"]], [Q(1), Q(0)])
            m, t, e = M[0][0], T[0][0], errors[0]
            H = kappa*t - m - e*e
            self.assertEqual((t, m, e, H, 4*m*e*e - H*H), tuple(Q(witness[k]) for k in
                ("source_energy_lower", "finite_residual_norm_squared", "error_norm_upper",
                 "H", "four_m_e_squared_minus_H_squared")))
            self.assertEqual(kappa*t-m, Q(witness["nominal_gap_kappa_t_minus_m"]))
            self.assertLess(kappa*t-m, 0)
            self.assertLess(H, 0)
        self.assertFalse(receipt["genuine_S4_sign_decided"])
        self.assertFalse(receipt["RH_proved"])


if __name__ == "__main__":
    unittest.main()
