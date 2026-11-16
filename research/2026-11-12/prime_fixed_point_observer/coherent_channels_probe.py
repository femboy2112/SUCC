"""Exact finite controls for present-output coherence and recovery.

The inherited Gaussian-rational scalar/matrix operations are reused. The
channel, complement, Choi contraction, recovery and record-overlap oracles
below are separate local implementations. This is not a device experiment,
an objective-collapse simulation, or an infinite arithmetic certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random

from twin_correlation_probe import (
    Q, Z, ONE, IM, add, adjoint, apply, conjugate, density, diag, eye,
    inner, matrix, multiply, norm2, scaled, tensor, trace, transpose,
)


def zero(rows, cols):
    return matrix([[0] * cols for _ in range(rows)])


def unit(rows, i, j):
    return matrix([[int(a == i and b == j) for b in range(rows)]
                   for a in range(rows)])


def outer(vector):
    return tuple(tuple(a * b.conj() for b in vector) for a in vector)


def summatrices(items, rows, cols):
    result = zero(rows, cols)
    for item in items:
        result = add(result, item)
    return result


def is_trace_preserving(kraus):
    d = len(kraus[0][0])
    return summatrices((multiply(adjoint(e), e) for e in kraus), d, d) == eye(d)


def channel(kraus, x):
    b = len(kraus[0])
    return summatrices((multiply(multiply(e, x), adjoint(e)) for e in kraus), b, b)


def complement(kraus, x):
    return tuple(tuple(trace(multiply(multiply(a, x), adjoint(b)))
                       for b in kraus) for a in kraus)


def twin_density(kraus):
    """Direct coefficient contraction, without the fidelity trace formula."""
    b, d = len(kraus[0]), len(kraus[0][0])
    result = zero(b * d, b * d)
    for e in kraus:
        vector = tuple(e[i][j] for i in range(b) for j in range(d))
        result = add(result, scaled(outer(vector), F(1, d)))
    return result


def target_twin(v):
    b, d = len(v), len(v[0])
    vector = tuple(v[i][j] for i in range(b) for j in range(d))
    return scaled(outer(vector), F(1, d))


def frobenius2(a):
    return sum((x.abs2() for row in a for x in row), F(0))


def fidelity_from_twin(kraus, v):
    value = trace(multiply(target_twin(v), twin_density(kraus)))
    assert value.im == 0
    return value.re


def fidelity_trace(kraus, v):
    d = len(v[0])
    return sum((trace(multiply(adjoint(v), e)).abs2() for e in kraus), F(0)) / (d * d)


def residual(kraus, v):
    d = len(v[0])
    cs = tuple(trace(multiply(adjoint(v), e)) / d for e in kraus)
    value = sum((frobenius2(add(e, scaled(v, -c)))
                 for e, c in zip(kraus, cs)), F(0)) / d
    return value, cs


def kl_condition(kraus):
    """Full all-pairs matrix criterion, not just diagonal logical inputs."""
    d = len(kraus[0][0])
    for a in kraus:
        for b in kraus:
            g = multiply(adjoint(a), b)
            if g != scaled(eye(d), g[0][0]):
                return False
    return True


def record_channel(records):
    d, e = len(records), len(records[0])
    assert all(len(record) == e and norm2(record) == 1 for record in records)
    return tuple(diag(tuple(records[j][a] for j in range(d))) for a in range(e))


def record_gram(records):
    return tuple(tuple(inner(b, a) for b in records) for a in records)


def marginal_first(rho, b, d):
    return tuple(tuple(sum((rho[i*d+j][k*d+j] for j in range(d)), Z)
                       for k in range(b)) for i in range(b))


def marginal_second(rho, b, d):
    return tuple(tuple(sum((rho[i*d+j][i*d+k] for i in range(b)), Z)
                       for k in range(d)) for j in range(d))


def partial_transpose_second(rho, b, d):
    return tuple(tuple(rho[i*d+l][k*d+j]
                       for k in range(b) for l in range(d))
                 for i in range(b) for j in range(d))


def rational_unitary(rng, d):
    u = eye(d)
    if d > 1:
        pairs = [(F(3,5), F(4,5)), (F(5,13), F(12,13)),
                 (F(7,25), F(24,25))]
        for _ in range(d + 2):
            i, j = rng.sample(range(d), 2)
            c, s = rng.choice(pairs)
            a = [list(row) for row in eye(d)]
            a[i][i], a[i][j] = Q(c), Q(-s)
            a[j][i], a[j][j] = Q(s), Q(c)
            u = multiply(matrix(a), u)
    phases = [ONE, -ONE, IM, -IM, Q(F(3,5),F(4,5))]
    return multiply(diag([rng.choice(phases) for _ in range(d)]), u)


def main():
    counts = Counter()
    witnesses = {}

    def check(group, condition, context=""):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group], context))

    check("scalar_calibration", IM * IM == Q(-1))
    check("scalar_calibration", Q(F(3,5), F(4,5)).abs2() == 1)
    check("scalar_calibration", inner((IM,), (IM,)) == ONE)
    rng = random.Random(2026111217)

    # Known fixed isometry, mixed-unitary mutation, and untouched holdout d=7.
    for d, trials in [(1,3), (2,6), (3,4), (5,2), (7,1)]:
        for trial in range(trials):
            u, v = rational_unitary(rng, d), rational_unitary(rng, d)
            check("unitary_positive", multiply(adjoint(u),u) == eye(d), (d,trial))
            matched = (scaled(u,F(3,5)), scaled(u,F(4,5)))
            changed = (scaled(u,F(3,5)), scaled(v,F(4,5)))
            for name, kraus in [("matched",matched), ("changed",changed)]:
                check("channel_trace_preservation", is_trace_preserving(kraus), (d,trial,name))
                direct = fidelity_from_twin(kraus,u)
                formula = fidelity_trace(kraus,u)
                error, cs = residual(kraus,u)
                check("fidelity_direct_trace", direct == formula, (d,trial,name))
                check("fidelity_residual", error == 1-direct, (d,trial,name))
                check("fidelity_range", 0 <= direct <= 1, (d,trial,name))
                check("coefficient_norm", sum(c.abs2() for c in cs) == direct, (d,trial,name))
            check("fixed_output_positive", twin_density(matched) == target_twin(u), (d,trial))
            check("fixed_output_positive", kl_condition(matched), (d,trial))
            for i in range(d):
                for j in range(d):
                    x = unit(d,i,j)
                    check("full_matrix_unit_transport", channel(matched,x) == multiply(multiply(u,x),adjoint(u)))
                    expected = matrix([[F(9,25),F(12,25)],[F(12,25),F(16,25)]])
                    check("full_complement_constancy", complement(matched,x) == scaled(expected,int(i==j)))

    # Trace-preservation mutation cannot enter the theorem's hypotheses.
    check("mutation_controls", not is_trace_preserving((scaled(eye(2),F(3,5)),)))
    bad = (diag((1,F(3,5))), matrix([[0,F(4,5)],[0,0]]))
    check("amplitude_damping", is_trace_preserving(bad))
    check("amplitude_damping", not kl_condition(bad))
    check("amplitude_damping", fidelity_from_twin(bad,eye(2)) == F(16,25))
    check("amplitude_damping", residual(bad,eye(2))[0] == F(9,25))

    # Syndrome noise is recoverable even though the raw current output is mixed.
    v0 = matrix([[1,0],[0,0],[0,1],[0,0]])
    v1 = matrix([[0,0],[1,0],[0,0],[0,1]])
    kraus = (scaled(v0,F(3,5)),scaled(v1,F(4,5)))
    check("syndrome_recovery", is_trace_preserving(kraus))
    check("syndrome_recovery", kl_condition(kraus))
    for i in range(2):
        for j in range(2):
            x = unit(2,i,j)
            y = channel(kraus,x)
            decoded = add(multiply(multiply(adjoint(v0),y),v0),
                          multiply(multiply(adjoint(v1),y),v1))
            check("syndrome_recovery", decoded == x, (i,j))
            check("syndrome_complement", complement(kraus,x) == scaled(diag((F(9,25),F(16,25))),int(i==j)))
    pure = density((Q(F(3,5)),Q(F(4,5))))
    mixed = channel(kraus,pure)
    check("syndrome_mixed_output", trace(multiply(mixed,mixed)) == Q(F(337,625)))
    # Apply decoding directly to the current joint B,R matrix.
    r = twin_density(kraus)
    dec = add(multiply(multiply(tensor(adjoint(v0),eye(2)),r),tensor(v0,eye(2))),
              multiply(multiply(tensor(adjoint(v1),eye(2)),r),tensor(v1,eye(2))))
    check("syndrome_twin_recovery", dec == target_twin(eye(2)))

    # Equal environment marginals on basis states can hide superposition leakage.
    signs = [1,1,-1,-1]
    hidden = tuple(matrix([[F(1,2) if i==a else 0,
                           F(signs[a],2) if i==a else 0]
                          for i in range(4)]) for a in range(4))
    check("hidden_superposition_leak", is_trace_preserving(hidden))
    check("hidden_superposition_leak", complement(hidden,unit(2,0,0)) == scaled(eye(4),F(1,4)))
    check("hidden_superposition_leak", complement(hidden,unit(2,1,1)) == scaled(eye(4),F(1,4)))
    check("hidden_superposition_leak", complement(hidden,unit(2,0,1)) == scaled(diag(signs),F(1,4)))
    check("hidden_superposition_leak", not kl_condition(hidden))

    # Pure replacement is not preserved logical information.
    replacer = (matrix([[1,0]]),matrix([[0,1]]))
    check("pure_replacement", is_trace_preserving(replacer))
    check("pure_replacement", channel(replacer,pure) == eye(1))
    check("pure_replacement", twin_density(replacer) == scaled(eye(2),F(1,2)))
    check("pure_replacement", not kl_condition(replacer))

    eta0 = (ONE,Z)
    cases = [
        ("equal",(ONE,Z),F(1),F(1)),
        ("partial",(Q(F(3,5)),Q(F(4,5))),F(4,5),F(17,25)),
        ("orthogonal",(Z,ONE),F(1,2),F(1,2)),
        ("opposite",(-ONE,Z),F(0),F(1)),
        ("quarter_phase",(IM,Z),F(1,2),F(1)),
    ]
    for label,eta1,fidelity,purity in cases:
        records = (eta0,eta1)
        ks = record_channel(records)
        g = record_gram(records)
        rho = twin_density(ks)
        gamma = g[0][1]
        check("records_trace_preservation", is_trace_preserving(ks),label)
        check("records_current_fidelity", fidelity_from_twin(ks,eye(2)) == fidelity,label)
        check("records_purity", trace(multiply(rho,rho)) == Q(purity),label)
        check("records_individual_marginals", marginal_first(rho,2,2) == scaled(eye(2),F(1,2)),label)
        check("records_individual_marginals", marginal_second(rho,2,2) == scaled(eye(2),F(1,2)),label)
        check("records_coarse_agreement", rho[0][0]+rho[3][3] == ONE,label)
        pt = partial_transpose_second(rho,2,2)
        det = pt[1][1]*pt[2][2]-pt[1][2]*pt[2][1]
        check("records_partial_transpose", det == Q(-gamma.abs2()/4),label)
        check("records_partial_transpose", (det.re < 0) == (gamma != Z),label)
        check("records_exact_gram", rho[0][3] == gamma/2,label)
        distance = sum(norm2(tuple(a-b for a,b in zip(left,right)))
                       for left in records for right in records)
        check("records_pairwise_distance", distance/8 == 1-fidelity,label)
        witnesses[label] = {"gamma_re":str(gamma.re),"gamma_im":str(gamma.im),
                           "fixed_fidelity":str(fidelity),"joint_purity":str(purity),
                           "pt_middle_determinant":str(det.re)}
    phase = diag((ONE,-ONE))
    phase_k = record_channel((eta0,(-ONE,Z)))
    check("phase_calibration", fidelity_from_twin(phase_k,phase) == 1)
    check("phase_calibration", kl_condition(phase_k))
    check("phase_calibration", fidelity_from_twin(phase_k,eye(2)) == 0)

    # More than two logical labels, including held-out d=7 record choices.
    bank = [eta0,(Z,ONE),(Q(F(3,5)),Q(F(4,5))),
            (Q(F(5,13)),Q(F(12,13))),(IM,Z),(-ONE,Z)]
    for d in (3,4,7):
        for trial in range(3):
            records = tuple(rng.choice(bank) for _ in range(d))
            ks = record_channel(records)
            rho, gram = twin_density(ks), record_gram(records)
            gram_purity = sum(z.abs2() for row in gram for z in row)/(d*d)
            total = tuple(sum((record[a] for record in records),Z) for a in range(2))
            f = norm2(total)/(d*d)
            distance = sum(norm2(tuple(a-b for a,b in zip(left,right)))
                           for left in records for right in records)
            check("multilevel_record_identity", trace(multiply(rho,rho)) == Q(gram_purity),(d,trial))
            check("multilevel_record_identity", fidelity_from_twin(ks,eye(d)) == f,(d,trial))
            check("multilevel_record_identity", distance/(2*d*d) == 1-f,(d,trial))
            check("multilevel_record_identity", marginal_second(rho,d,d) == scaled(eye(d),F(1,d)),(d,trial))
            check("multilevel_record_identity", residual(ks,eye(d))[0] == 1-f,(d,trial))

    # Reversible computed records dephase exactly between distinct f-fibers.
    f = [0,1,0,2,1]
    records = tuple(tuple(Q(int(k==value)) for k in range(3)) for value in f)
    ks = record_channel(records)
    for i in range(len(f)):
        for j in range(len(f)):
            x = unit(len(f),i,j)
            check("computed_record_fibers", channel(ks,x) == scaled(x,int(f[i]==f[j])),(i,j))
    # Differing signs become indistinguishable after crossing distinct fibers.
    plus,minus = (ONE,ONE,Z,Z,Z),(ONE,-ONE,Z,Z,Z)
    check("computed_record_irrecoverability", channel(ks,density(plus)) == channel(ks,density(minus)))
    check("computed_record_irrecoverability", density(plus) != density(minus))

    # Fresh environments compose overlaps; reusing a record can erase it.
    left = (ONE,Z)
    right = (Q(F(3,5)),Q(F(4,5)))
    for n in range(1,7):
        a,b = (ONE,), (ONE,)
        for _ in range(n):
            a = tuple(x*y for x in a for y in left)
            b = tuple(x*y for x in b for y in right)
        check("fresh_record_product", inner(b,a) == Q(F(3,5)**n),n)
    cnot = matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    check("reused_record_recoherence", multiply(cnot,cnot) == eye(4))
    state = (Q(F(3,5)),Z,Q(F(4,5)),Z)
    once = apply(cnot,state)
    twice = apply(cnot,once)
    check("reused_record_recoherence", twice == state)
    check("reused_record_recoherence", marginal_first(density(once),2,2)[0][1] == Z)
    check("reused_record_recoherence", marginal_first(density(twice),2,2)[0][1] == Q(F(12,25)))

    source = Path(__file__)
    dependency = source.with_name("twin_correlation_probe.py")
    return {
        "status":"PASS", "exact_checks":sum(counts.values()), "groups":dict(counts),
        "witnesses":witnesses,
        "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "shared_scalar_dependency_sha256":hashlib.sha256(dependency.read_bytes()).hexdigest(),
        "dimensions": {"main":[1,2,3,5],"holdout":7,"record_holdouts":[3,4,7]},
        "scope":"Exact finite Gaussian-rational current-channel controls; universal statements have written proofs. No physical collapse law, history-comparison access, or arithmetic asymptotic follows.",
        "provenance":"Reuses existing Gaussian-rational primitives; direct Choi contractions, Kraus residuals, complementary channels and full-matrix-unit recovery are separate calculation paths, not independent-model testimony.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    report = main()
    rendered = json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output is not None:
        args.output.write_text(rendered)
    print(rendered,end="")
