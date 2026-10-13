"""Bounded C24 classical controls; rational laws and exact symbolic logarithms.

No floating-point entropy, thermal simulation, compiler, or full test suite.
The universal claims are proved in C24.md; this checks finite witnesses only.
"""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.probe_coherence import DestructiveCarrier, InitialSource

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def add(*terms):
    out = defaultdict(F)
    for term in terms:
        for prime, coefficient in term.items():
            out[prime] += coefficient
    return {p: c for p, c in out.items() if c}


def scale(term, coefficient):
    return {p: coefficient * c for p, c in term.items() if coefficient * c}


def log(q):
    """Exact rational linear combination of log2(prime)."""
    q = F(q)
    assert q > 0
    out = defaultdict(F)
    for n, sign in ((q.numerator, 1), (q.denominator, -1)):
        p = 2
        while p * p <= n:
            while n % p == 0:
                out[p] += sign
                n //= p
            p += 1
        if n > 1:
            out[n] += sign
    return {p: c for p, c in out.items() if c}


def nonnegative(term):
    """Exponentiate after clearing rational denominators; compare integers."""
    denominator = lcm(*(c.denominator for c in term.values())) if term else 1
    numerator = denominator_product = 1
    for p, c in term.items():
        exponent = int(c * denominator)
        if exponent >= 0:
            numerator *= p ** exponent
        else:
            denominator_product *= p ** -exponent
    return numerator >= denominator_product


def marginal(atoms, keys):
    out = defaultdict(F)
    for row, mass in atoms:
        out[tuple(row[k] for k in keys)] += mass
    return dict(out)


def entropy(atoms, keys):
    return add(*(scale(log(p), -p) for p in marginal(atoms, keys).values()))


def union(*groups):
    return tuple(dict.fromkeys(k for group in groups for k in group))


def conditional(atoms, target, given=()):
    return add(entropy(atoms, union(target, given)), scale(entropy(atoms, given), -1))


def information(atoms, left, right, given=()):
    return add(conditional(atoms, left, given),
               scale(conditional(atoms, left, union(right, given)), -1))


def symbolic(term):
    return {str(p): str(c) for p, c in sorted(term.items())}


def check_case(name, prior, report, target):
    assert prior and all(p > 0 for s, z, p in prior)
    assert sum(p for s, z, p in prior) == 1
    assert len({(s, z) for s, z, p in prior}) == len(prior)
    fibers = defaultdict(list)
    for s, z, p in prior:
        fibers[(report(s, z), z)].append(s)
    atoms = []
    for s, z, p in prior:
        r = report(s, z)
        g = fibers[(r, z)].index(s)
        atoms.append((dict(S=s, Z=z, R=r, X=target(s, z), G=g), p))
    loss = conditional(atoms, ("S",), ("R", "Z"))
    assert loss == add(conditional(atoms, ("S",), ("Z",)),
                       scale(conditional(atoms, ("R",), ("Z",)), -1))
    info_loss = add(information(atoms, ("X",), ("S",), ("Z",)),
                    scale(information(atoms, ("X",), ("R",), ("Z",)), -1))
    assert info_loss == information(atoms, ("X",), ("S",), ("R", "Z"))
    bound = add(*(scale(log(len(fibers[key])), p)
                  for key, p in marginal(atoms, ("R", "Z")).items()))
    maximum = max(map(len, fibers.values()))
    assert nonnegative(loss) and nonnegative(info_loss)
    assert nonnegative(add(loss, scale(info_loss, -1)))
    assert nonnegative(add(bound, scale(loss, -1)))
    assert nonnegative(add(log(maximum), scale(bound, -1)))
    assert conditional(atoms, ("G",), ("R", "Z")) == loss
    assert conditional(atoms, ("S",), ("R", "Z", "G")) == {}
    return {
        "name": name,
        "atoms": [{**row, "probability": str(p)} for row, p in atoms],
        "loss_bits_exact_log2_prime_coefficients": symbolic(loss),
        "target_information_loss_bits_exact_log2_prime_coefficients": symbolic(info_loss),
        "mean_log_fiber_bound_exact_log2_prime_coefficients": symbolic(bound),
        "maximum_positive_support_fiber": maximum,
        "minimum_fixed_length_auxiliary_bits": (maximum - 1).bit_length(),
        "chain_rule_data_processing_fiber_and_embedding_checks": "PASS",
    }


def native_report(s, z):
    carrier = DestructiveCarrier.from_source(InitialSource(*s)).probe("a")
    trace = tuple((r.probe, r.outcome, r.refers_to_initial_source,
                   r.before_version, r.after_version) for r in carrier.trace)
    return (carrier.a, carrier.b, trace)


def main():
    fair = [(b, None, F(1, 2)) for b in (0, 1)]
    cases = [check_case("erase_fair_bit", fair, lambda s, z: 0, lambda s, z: s),
             check_case("copy_to_blank_keep_both", fair, lambda s, z: (s, s), lambda s, z: s),
             check_case("erase_biased_full_support_bit", [(0, None, F(1023, 1024)),
                        (1, None, F(1, 1024))], lambda s, z: 0, lambda s, z: s),
             check_case("erase_two_correlated_bits", [((b, b), None, F(1, 2))
                        for b in (0, 1)], lambda s, z: (0, 0), lambda s, z: s)]
    factorial = {}
    for correlated, retained in product((0, 1), repeat=2):
        prior = ([(b, b, F(1, 2)) for b in (0, 1)] if correlated else
                 [(b, c, F(1, 4)) for b, c in product((0, 1), repeat=2)])
        case = check_case(f"side_copy_{correlated}_record_{retained}", prior,
                          lambda s, z: (0, s) if retained else 0, lambda s, z: s)
        cases.append(case)
        factorial[f"{correlated}{retained}"] = case["loss_bits_exact_log2_prime_coefficients"]
    assert factorial == {"00": {"2": "1"}, "01": {}, "10": {}, "11": {}}
    source = [((a, b), None, F(1, 4)) for a, b in product((0, 1), repeat=2)]
    cases.append(check_case("native_read_a_overwrite_b", source, native_report,
                            lambda s, z: s[0] ^ s[1]))
    cases.append(check_case("native_with_retained_initial_b", source,
                            lambda s, z: (native_report(s, z), s[1]), lambda s, z: s[0] ^ s[1]))
    assert [c["loss_bits_exact_log2_prime_coefficients"] for c in cases[:2]] == [{"2": "1"}, {}]
    assert cases[3]["loss_bits_exact_log2_prime_coefficients"] == {"2": "1"}
    assert cases[-2]["target_information_loss_bits_exact_log2_prime_coefficients"] == {"2": "1"}
    assert cases[-1]["target_information_loss_bits_exact_log2_prime_coefficients"] == {}
    gates = [lambda b, c: (b, b ^ c), lambda b, c: (b ^ c, c)]
    assert all(len({gate(*x) for x in product((0, 1), repeat=2)}) == 4 for gate in gates)
    assert all(gates[1](*gates[0](b, 0)) == (0, b) for b in (0, 1))
    swap = [(dict(B=b, M=b, E=e, Bp=e, Ep=b), F(1, 4))
            for b, e in product((0, 1), repeat=2)]
    assert information(swap, ("B",), ("M",)) == {2: F(1)}
    assert information(swap, ("Bp",), ("M",)) == {}
    assert marginal(swap, ("E",)) == marginal(swap, ("Ep",))
    noisy = [(dict(S=0, R=r), F(1, 2)) for r in (0, 1)]
    assert add(entropy(noisy, ("S",)), scale(entropy(noisy, ("R",)), -1)) == {2: F(-1)}
    exhaustive = 0
    for outputs, targets in product(product((0, 1), repeat=4), repeat=2):
        check_case("bounded_map_control", [(s, None, F(1, 4)) for s in range(4)],
                   lambda s, z: outputs[s], lambda s, z: targets[s])
        exhaustive += 1
    tracked = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
               "observational_succ/probe_coherence.py", "observational_succ/entropy_transport.py",
               "observational_succ/proof_backaction_debt.py", "observational_succ/voyager_profinite_frontier.py",
               "formal/EODCS_VoyagerMemoryDebt.lean",
               "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
               "research/2026-10-13/SWARM_ATLAS/C24.md",
               "research/2026-10-13/SWARM_ATLAS/C24_probe.py"]
    print(json.dumps({
        "schema": "C24-exact-finite-information-v1", "immutable_parent": BASE,
        "import_source_commit": "ba075348b7bcc66d938b3e0ca96c26e95bba340a",
        "import_source_commit_object_available_locally": False,
        "status": "TESTED MODEL; universal statements have prose PROVED LOCAL proofs",
        "command": "python -B research/2026-10-13/SWARM_ATLAS/C24_probe.py > research/2026-10-13/SWARM_ATLAS/C24_receipt.json",
        "probe_exit_code": 0, "cases": cases,
        "symbolic_basis": "sum coefficients[p] * log2(p); omitted coefficients are zero",
        "inequality_checker": "exact integer product comparison after clearing rational denominators",
        "complete_factorial": {"cells": factorial, "mixed_difference_bits_exact": "1",
                               "meaning": "model non-additivity; no physical mechanism inferred"},
        "global_copy_and_controlled_reset_permutations_checked": True,
        "swap_control": {"initial_information_bits_exact": "1", "final_information_bits_exact": "0",
                         "reservoir_marginal_unchanged": True, "heat_exact_under_H_reservoir_zero": "0",
                         "is_reset_to_standard_state": False, "empirical_measurement": False},
        "excluded_stochastic_control": {"H_S_minus_H_R_bits_exact": "-1",
                                        "deterministic_report_hypothesis_satisfied": False},
        "additional_uniform_four_source_binary_maps_checked": exhaustive,
        "sha256": {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in tracked},
        "no_physical_source_authentication_or_empirical_thermodynamic_validation": True,
        "no_compiler_or_full_suite_run": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
