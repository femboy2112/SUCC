#!/usr/bin/env python3
"""Independent holdouts for stochastic transport and F memory/quantum.

Oracle arithmetic is local event atoms, unpartitioned matrices and Kraus
products. Tested functions are called only after expected values are computed.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import platform
import random
import subprocess
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from observational_succ.causal_nerode_succ import SourceChart, SourceTransportError
from observational_succ.cambrian_stochastic_transport import (
    JointInstrument, joint_descent, source_filter, observer_filter, filter_history,
)


def compositions(total, width):
    if width == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, width - 1):
                yield (first,) + rest


def chart(epoch, reports):
    return SourceChart("audit-B-source", epoch, "audit-B-basis",
                       tuple(f"s{i}" for i in range(len(reports))), tuple(reports))


def event_atoms(rows, prior, receipt, receipts):
    # The fine law is built as literal atoms (initial state, final state, receipt).
    out = [Q()] * (len(rows[0]) // len(receipts))
    mass = Q()
    for i, row in enumerate(rows):
        for j in range(len(out)):
            for k, z in enumerate(receipts):
                if z == receipt:
                    atom = prior[i] * row[j * len(receipts) + k]
                    mass += atom
                    out[j] += atom
    return mass, tuple(v / mass for v in out) if mass else None


def aggregate(report, weights):
    return tuple(sum((w for r, w in zip(report, weights) if r == label), Q())
                 for label in sorted(set(report)))


def stochastic_oracles():
    rows = tuple(tuple(Q(v, 5) for v in xs) for xs in compositions(5, 4))
    priors = ((Q(1), Q()), (Q(), Q(1)), (Q(1,7), Q(6,7)),
              (Q(2,3), Q(1,3)), (Q(1,2), Q(1,2)))
    cases = filters = rejections = 0
    for q, p in product((("a", "a"), ("a", "b")), repeat=2):
        for a, b in product(rows, repeat=2):
            coarse_atoms = []
            for row in (a, b):
                coarse_atoms.append({(report, z): sum((row[2*j+k]
                                                     for j in range(2) if p[j] == report), Q())
                                     for report in set(p) for k, z in enumerate(("z", "w"))})
            expected = q[0] != q[1] or coarse_atoms[0] == coarse_atoms[1]
            instrument = JointInstrument("fresh-denominator-five", chart(0, q), chart(1, p),
                                         ("z", "w"), (a, b))
            result = joint_descent(instrument)
            assert result.descended == expected
            if expected:
                for prior in priors:
                    for z in instrument.receipts:
                        mass, posterior = event_atoms(instrument.rows, prior, z, instrument.receipts)
                        coarse_post = aggregate(p, posterior) if mass else None
                        fine = source_filter(instrument, prior, z)
                        coarse = observer_filter(instrument, aggregate(q, prior), z)
                        assert fine.evidence == coarse.evidence == mass
                        assert fine.posterior == posterior
                        assert coarse.posterior == coarse_post
                        filters += 1
            else:
                try:
                    observer_filter(instrument, (Q(1),), "z")
                except SourceTransportError:
                    rejections += 1
                else:
                    raise AssertionError("Nondescending joint source was accepted")
            cases += 1
    assert cases == 12544
    return {"joint_descent_cases": cases, "event_atom_filter_cases": filters,
            "nondescending_observer_rejections": rejections,
            "heldout_denominator": 5, "heldout_prior": "(1/7,6/7) and (2/3,1/3)"}


def history_oracle(instruments, prior, receipts):
    # Unnormalized event-path sum; no tested filtering, normalization or report helper.
    weights = list(prior)
    for instrument, receipt in zip(instruments, receipts):
        new = [Q()] * len(instrument.after.states)
        for i, value in enumerate(weights):
            for j in range(len(new)):
                for k, z in enumerate(instrument.receipts):
                    if z == receipt:
                        new[j] += value * instrument.rows[i][2*j+k]
        weights = new
    likelihood = sum(weights, Q())
    posterior = tuple(v / likelihood for v in weights) if likelihood else None
    return likelihood, aggregate(instruments[-1].after.observations, posterior) if likelihood else None


def history_checks():
    instruments = []
    q = ("a", "a", "b", "b")
    for epoch in range(4):
        rows = []
        for s in range(4):
            # Joint coarse rows match in each q fiber; fine hidden split does not.
            counts = (1+epoch, 2+s//2, 4, 3+epoch+s//2)
            coarse = tuple(Q(v, sum(counts)) for v in counts)
            split = Q(1+(s+epoch)%3, 4)
            fine = []
            for target in range(4):
                for z in range(2):
                    fine.append(coarse[2*(target//2)+z]
                                * (split if target % 2 == 0 else 1-split))
            rows.append(tuple(fine))
        instruments.append(JointInstrument(f"stage-{epoch}", chart(epoch, q), chart(epoch+1, q),
                                           ("z", "w"), tuple(rows)))
    prior = (Q(1,10), Q(2,10), Q(3,10), Q(4,10))
    for word in product(("z", "w"), repeat=4):
        likelihood, posterior = history_oracle(instruments, prior, word)
        observed = filter_history(tuple(instruments), prior, word)
        assert observed["possible"] and observed["likelihood"] == likelihood
        assert observed["posterior"] == posterior
    # A coarse-history-adaptive chooser is equivalent to a frozen selected path
    # on each word. The tested API executes that selected finite path.
    adaptive = 0
    for word in product(("z", "w"), repeat=4):
        chosen = []
        for epoch, original in enumerate(instruments):
            if epoch and word[epoch-1] == "w":
                flipped = tuple(tuple(row[2*j+1-k] for j in range(4) for k in range(2))
                                for row in original.rows)
                chosen.append(JointInstrument("public-adaptive-flip", original.before,
                                              original.after, original.receipts, flipped))
            else:
                chosen.append(original)
        likelihood, posterior = history_oracle(chosen, prior, word)
        observed = filter_history(tuple(chosen), prior, word)
        assert observed["likelihood"] == likelihood and observed["posterior"] == posterior
        adaptive += 1
    # Hidden-state selector breaks the premise even if EACH action descends.
    before, after = chart(0, ("same", "same")), chart(1, ("u", "v"))
    a = JointInstrument("always-u", before, after, ("z",), ((Q(1),Q()),)*2)
    b = JointInstrument("always-v", before, after, ("z",), ((Q(),Q(1)),)*2)
    mixed = JointInstrument("hidden-selector", before, after, ("z",),
                            ((Q(1),Q()),(Q(),Q(1))))
    assert joint_descent(a).descended and joint_descent(b).descended
    assert not joint_descent(mixed).descended
    return {"fixed_four_step_receipt_words": 16, "public_adaptive_selected_paths": adaptive,
            "hidden_state_selector_countermodel": "Each action descends; hidden selected mixture does not"}


def tv(a, b):
    return sum((abs(x-y) for x, y in zip(a, b)), Q()) / 2


def stability_checks():
    laws = tuple(tuple(Q(v,7) for v in xs) for xs in compositions(7,4))
    checked = unequal = nulls = 0
    for a, b in product(laws, repeat=2):
        epsilon = tv(a, b)
        for event in ((0,1), (2,3)):
            alpha, beta = sum((a[i] for i in event), Q()), sum((b[i] for i in event), Q())
            if not alpha or not beta:
                nulls += 1
                continue
            conditional = tv(tuple(a[i]/alpha for i in event), tuple(b[i]/beta for i in event))
            assert conditional <= epsilon / max(alpha, beta)
            unequal += alpha != beta
            checked += 1
    alpha, beta = Q(1,5), Q(3,5)
    p, q = (alpha,Q(),1-alpha,Q()), (alpha,beta-alpha,1-beta,Q())
    unequal_sharp = tv((p[0]/alpha,p[1]/alpha), (q[0]/beta,q[1]/beta))
    assert unequal_sharp == tv(p,q)/max(alpha,beta) == Q(2,3)
    rare = Q(1,10**6)
    p, q = (rare,Q(),1-rare,Q()), (Q(),rare,1-rare,Q())
    assert tv(p,q) == rare and tv((Q(1),Q()), (Q(),Q(1))) == tv(p,q)/rare == 1
    return {"positive_conditioning_cases": checked, "unequal_event_mass_cases": unequal,
            "null_events_excluded": nulls, "sharp_unequal_conditional_TV": unequal_sharp,
            "rare_event_mass": rare, "rare_conditional_TV": Q(1),
            "strong_bound": "epsilon / MAX(alpha,beta)"}


def matrix_product(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), Q())
                       for j in range(len(b[0]))) for i in range(len(a)))


def matrix_vector(a, v):
    return tuple(sum((x*y for x,y in zip(row,v)), Q()) for row in a)


def eye(n):
    return tuple(tuple(Q(i==j) for j in range(n)) for i in range(n))


def characteristic_check(d):
    # Independent Faddeev--LeVerrier coefficients and evaluated Cayley-Hamilton.
    n = len(d)
    b = eye(n)
    coefficients = []
    for k in range(1,n+1):
        db = matrix_product(d,b)
        coefficient = -sum((db[i][i] for i in range(n)),Q())/k
        coefficients.append(coefficient)
        b = tuple(tuple(db[i][j]+coefficient*Q(i==j) for j in range(n))
                  for i in range(n))
    assert all(v==0 for row in b for v in row)
    return tuple(coefficients)


def block_checks(f):
    rng = random.Random(2026101302)
    checked = memories = kernels = 0
    for h in (1,2,3):
        for case in range(24):
            r, m = 2, 2
            def random_matrix(rows,cols):
                return tuple(tuple(Q(rng.randrange(-3,4),rng.randrange(1,5))
                                   for _ in range(cols)) for _ in range(rows))
            A,B,C,D,E,H = (random_matrix(r,r),random_matrix(r,h),random_matrix(h,r),
                           random_matrix(h,h),random_matrix(r,m),random_matrix(h,m))
            if case % 4 == 0:
                C,H = tuple((Q(),)*r for _ in range(h)), tuple((Q(),)*m for _ in range(h))
            if case % 7 == 0:
                B = tuple((Q(),)*h for _ in range(r))
            characteristic_check(D)
            full = tuple(A[i]+B[i] for i in range(r)) + tuple(C[i]+D[i] for i in range(h))
            force = E+H
            state = tuple(Q(rng.randrange(-2,3),3) for _ in range(r+h))
            z0 = state[r:]
            inputs = [tuple(Q(rng.randrange(-3,4),5) for _ in range(m)) for _ in range(9)]
            xs, us = [], []
            system = f.BlockSystem(A,B,C,D,E,H)
            for u in inputs:
                xs.append(state[:r]); us.append(u)
                expected = tuple(x+y for x,y in zip(matrix_vector(full,state),matrix_vector(force,u)))
                observed = system.memory_successor(xs,us,z0)
                assert observed == expected[:r]
                state = expected
                memories += 1
            power = eye(h)
            independently_zero = []
            for k in range(2*h+4):
                first = matrix_product(matrix_product(B,power),C)
                second = matrix_product(matrix_product(B,power),H)
                independently_zero.append(all(v==0 for row in first+second for v in row))
                assert system.kernel(k) == first
                assert system.kernel(k,input_kernel=True) == second
                power = matrix_product(power,D)
                kernels += 2
            certificate = system.closure_certificate()
            assert certificate["all_hidden_initial_closure"] == all(v==0 for row in B for v in row)
            assert certificate["zero_hidden_initial_closure"] == all(independently_zero[:h])
            if certificate["zero_hidden_initial_closure"]:
                assert all(independently_zero)
            checked += 1
    # Initial term is indispensible; independently computed x1=Bz0=1.
    witness = f.BlockSystem(((Q(),),),((Q(1),),),((Q(),),),((Q(1,2),),),((Q(),),),((Q(),),))
    assert witness.memory_successor(((Q(),),),((Q(),),),(Q(1),)) == (Q(1),)
    # Nilpotent sharp delay h=4: all first h-1 coefficients vanish, last equals 1.
    h = 4
    D = tuple(tuple(Q(j==i+1) for j in range(h)) for i in range(h))
    B = ((Q(1),Q(),Q(),Q()),)
    C = ((Q(),),(Q(),),(Q(),),(Q(1),))
    delayed = f.BlockSystem(((Q(),),),B,C,D,((Q(),),),((Q(),),)*h)
    assert all(delayed.kernel(k) == ((Q(),),) for k in range(h-1))
    assert delayed.kernel(h-1) == ((Q(1),),)
    assert not delayed.closure_certificate()["zero_hidden_initial_closure"]
    return {"fresh_rational_block_systems": checked, "full_block_vs_memory_successors": memories,
            "independent_kernel_matrices": kernels, "Cayley_Hamilton_identities": checked,
            "sharp_delay_hidden_dimension": h, "omitted_initial_term_counterexample": "x1=1 versus 0"}


def transpose(a):
    return tuple(zip(*a))


def quantum_update(k,rho):
    raw = matrix_product(matrix_product(k,rho),transpose(k))
    mass = raw[0][0]+raw[1][1]
    return mass, tuple(tuple(v/mass for v in row) for row in raw) if mass else None


def quantum_checks(f):
    p0,p1 = ((Q(1),Q()),(Q(),Q())), ((Q(),Q()),(Q(),Q(1)))
    reset = ((Q(),Q(1)),(Q(),Q()))
    assert matrix_product(transpose(p1),p1) == matrix_product(transpose(reset),reset)
    densities = [((Q(k,17),Q()),(Q(),Q(17-k,17))) for k in range(18)]
    for v in ((Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        densities.append(tuple(tuple(a*b for b in v) for a in v))
    for rho in densities:
        assert quantum_update(p1,rho)[0] == quantum_update(reset,rho)[0]
    _, after_luders = quantum_update(p1,p1)
    _, after_reset = quantum_update(reset,p1)
    expected_luders = {"0":quantum_update(p0,after_luders)[0],"1":quantum_update(p1,after_luders)[0]}
    expected_reset = {"0":quantum_update(p0,after_reset)[0],"1":quantum_update(p1,after_reset)[0]}
    observed = f.quantum_backaction_witness()
    assert observed["future_luders_Z"] == expected_luders
    assert observed["future_reset_Z"] == expected_reset
    assert expected_luders != expected_reset
    # Exact bridge on the COMMUTATIVE diagonal density algebra only.
    # Compile each Kraus branch on a basis source into (next basis state,receipt)
    # atoms. Check output diagonality before declaring any finite-state kernel.
    compiled = []
    bridge_cases = 0
    for name, family in (("Luders", (p0,p1)), ("reset", (p0,reset))):
        rows = []
        for basis in (p0,p1):
            atoms = []
            for target in range(2):
                for k in family:
                    raw = matrix_product(matrix_product(k,basis),transpose(k))
                    assert raw[0][1] == raw[1][0] == 0
                    atoms.append(raw[target][target])
            assert sum(atoms,Q()) == 1
            rows.append(tuple(atoms))
        instrument = JointInstrument(f"quantum-diagonal-{name}", chart(0,("0","1")),
                                     chart(1,("0","1")),("0","1"),tuple(rows))
        assert joint_descent(instrument).descended
        compiled.append(instrument)
        for rho in densities[:18]:
            prior = (rho[0][0],rho[1][1])
            for label,k in zip(instrument.receipts,family):
                mass, posterior = quantum_update(k,rho)
                expected_diagonal = (posterior[0][0],posterior[1][1]) if mass else None
                kernel = source_filter(instrument,prior,label)
                observer = observer_filter(instrument,prior,label)
                assert kernel.evidence == observer.evidence == mass
                assert kernel.posterior == observer.posterior == expected_diagonal
                bridge_cases += 1
    assert compiled[0].rows != compiled[1].rows
    k0 = ((Q(1),Q()),(Q(),Q(3,5)))
    sigma = ((Q(1,10),Q()),(Q(),Q(9,10)))
    m_r, post_r = quantum_update(k0,p1)
    m_s, post_s = quantum_update(k0,sigma)
    after = abs(post_r[0][0]-post_s[0][0])
    assert after == Q(25,106) > Q(1,10)
    return {"fresh_exact_density_states":len(densities), "same_POVM_effects": True,
            "future_luders_Z":expected_luders, "future_reset_Z":expected_reset,
            "conditional_trace_distance":after, "unconditional_input_distance":Q(1,10),
            "conditioning_event_masses":(m_r,m_s),
            "diagonal_quantum_kernel_bridge_cases":bridge_cases,
            "Luders_basis_joint_rows":compiled[0].rows,
            "reset_basis_joint_rows":compiled[1].rows,
            "bridge_scope":"Diagonal densities and basis-preserving Kraus branches only; no coherent-input generalization"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--f-repo", default=str(BASE))
    parser.add_argument("--root-repo", default=str(BASE))
    parser.add_argument("--save", action="store_true")
    args = parser.parse_args()
    frepo,rrepo = Path(args.f_repo),Path(args.root_repo)
    fpath = frepo/"observational_succ/cambrian_f_closure.py"
    spec = importlib.util.spec_from_file_location("observational_succ.cambrian_f_closure",fpath)
    f = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = f
    spec.loader.exec_module(f)
    stpath = Path("observational_succ/cambrian_stochastic_transport.py")
    assert sha(BASE/stpath) == sha(rrepo/stpath), "Root tested module changed since audit checkout"
    f_sha = subprocess.check_output(["git","-C",str(frepo),"rev-parse","HEAD"],text=True).strip()
    assert sha(fpath) == "acc31e8357cea00387023341e6af883676699b9058c4b29d52e3eff88410e91a", "Frozen F module changed"
    dependencies = ("observational_succ/dynamic_boundary_inverse.py",
                    "observational_succ/quantum_records.py")
    for dependency in dependencies:
        assert sha(BASE/dependency) == sha(frepo/dependency), "F dependency differs from audit import"
    result = {"schema":"succ.cambrian.audit-b.v1", "status":"EXACT_FINITE_CONTROLS_PASS",
              "python":platform.python_version(),
              "source_heads":{"F_frozen":"21ef59994f11d488a31632f731f4e4d7d9adbc77",
                              "F_checkout_observed":f_sha,"root_observed":subprocess.check_output(["git","-C",str(rrepo),"rev-parse","HEAD"],text=True).strip(),
                              "root_ST7_sharpening":"484dc20", "audit_base":"01bf38fb282872cfe28362321809b30ea9f1b3f9"},
              "sha256":{"root_stochastic_module":sha(rrepo/stpath),"F_closure_module":sha(fpath),
                         "audit_script":sha(Path(__file__)),
                         **{dependency:sha(BASE/dependency) for dependency in dependencies}},
              "stochastic":stochastic_oracles(), "histories":history_checks(),
              "conditional_stability":stability_checks(), "block_memory":block_checks(f),
              "quantum":quantum_checks(f), "tested_own_cluster_A":False,
              "new_Lean_proofs":False,"empirical_source_authentication":False,
              "all_infinite_quantifiers_proved_by_enumeration":False}
    output = json.dumps(result,indent=2,sort_keys=True,default=str)+"\n"
    if args.save:
        (BASE/"research/2026-10-13/CAMBRIAN_AUDIT_B_RECEIPT.json").write_text(output)
    print(output,end="")
