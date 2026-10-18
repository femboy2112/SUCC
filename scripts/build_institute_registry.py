#!/usr/bin/env python3
"""Materialize reviewed institute claim records and evidence hashes.

Claim text/authority here is a human-review surface. Rehashing is not a proof
promotion. The independent auditor validates contracts and the CI separately
executes the fixed Lean source with its axiom manifest.
"""
import json
from pathlib import Path
import subprocess
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.source_proof_certificate import evidence_file

ROOT = Path(__file__).resolve().parents[1]
BASE = '610efacf02556e1c5922bc5d4e87d0087f19b446'
PREFIX = 'research/2026-10-18/'


def git_source(path, commit=BASE):
    blob = subprocess.check_output(['git','rev-parse',commit+':'+path],cwd=ROOT,text=True).strip()
    return dict(commit=commit, path=path, blob=blob)


def evidence(path, kind='PAPER_PROOF'):
    return evidence_file(ROOT, path, kind)


def claim(cid, statement, hypotheses, signature, paper, *, authority='PAPER_PROVED',
          dependencies=(), debt=(), declarations=(), source_path='docs/FOUNDATIONS.md',
          prior='Classical mathematics specialized to explicitly declared source types.',
          novelty='PROJECT_LOCAL; academic novelty not established.',
          next_probe='Independent source and domain audit of the displayed quantified theorem.'):
    kernel = authority == 'LEAN_KERNEL_PROVED'
    open_target = authority == 'UNVERIFIED'
    finite = authority == 'EXACT_FINITE_CHECK'
    ev = [evidence(PREFIX+paper)]
    if kernel:
        ev += [evidence('formal/InstituteCausal.lean','LEAN_SOURCE'),
               evidence(PREFIX+'institute/kernel_receipt.json','LEAN_RECEIPT'),
               evidence(PREFIX+'institute/axioms.json','AXIOM_MANIFEST')]
    c = dict(claim_id=cid, authority=authority, statement=statement,
             source=signature['source'], operations_relations=statement,
             target_carrier=signature['carrier'], observation_morphisms='Precisely the maps in the cited theorem.',
             topology_measure=signature['topology'], universal_property='Only the equivalence/bound explicitly stated.',
             comparison_maps='Identity unless an explicit graph transport is recorded.',
             source_identity='Pinned mathematical source; no physical-source attestation.', source_epoch=0,
             hypotheses=list(hypotheses), dependencies=list(dependencies), evidence=ev,
             scope='FINITE_INSTANCE' if finite else 'UNIVERSAL',
             conclusion_mode='OPEN_TARGET' if open_target else 'INSTANCE_ONLY' if finite else 'THEOREM_UNDER_HYPOTHESES',
             access=dict(permitted_observations='Declared source grammar and cited test domain only.',
                         constructible_witness='Paper construction, Lean theorem, or exact finite receipt as labelled.',
                         oracle='No nontrivial zeta-zero inputs; no physical observation fabricated.',
                         probe_discrimination='Counterexamples and mutation controls in cited paper/tests.',
                         proof_theory='Core Lean4.14 for kernel claims; ordinary mathematics for paper claims.',
                         execution_cost='Commands and bounded runtimes retained in institute receipts.'),
             adversarial=dict(domain_tests='Availability, source identity, topology and zero-extension boundaries.',
                              negative_examples='Concrete failed claims retained in the cited paper.',
                              source_mutations='Exact source/normalization controls; see scoped test files.',
                              replay='python scripts/institute_audit.py; focused tests; verify_institute_lean.py'),
             signature=signature, quantifiers=statement, prior_art=prior, novelty=novelty,
             next_discriminator=next_probe, independent_check='Fresh-context hostile audit, principal replay; shared model family, not independent external referees.',
             proof_debt=list(debt), git_sources=[git_source(source_path)])
    if declarations:
        c['kernel_declarations']=['ObservationalSUCC.InstituteCausal.'+d for d in declarations]
    return c


def main():
    causal=dict(source='Declared partial labelled source system', carrier='arbitrary sets, finite action words', topology='set-level; no completion')
    haar=dict(source='positive-integer multiplication and profinite additive Haar', carrier='ell2(N+) and L2(Zhat,Haar)', topology='Hilbert norm; strong operator limits explicitly distinguished')
    dist=dict(source=haar['source'], carrier='c00 and locally constant test-function dual Dprime(Zhat)', topology='inductive-limit tests and weak dual; specified weighted domains')
    gamma=dict(source='original one-real-Gamma with d_j=4j+1', carrier='zero-extended H1_0 and H2_0 interval primitives', topology='Fourier multiplier and L2 action norm')
    schur=dict(source='original signed Suzuki source blob 0cc8510b71d178fc79e8d410a86d8b6014cf9178', carrier='four low modes and original infinite K-relative high space', topology='K primitive completion; source-relative Schur order')
    ch=['q is surjective onto the declared quotient carrier.', 'Actions are partial deterministic maps S x A -> Option(L x S); labels retained exactly.']
    hh=['Normalized additive Haar on Zhat.', 'Operators use the sqrt(p) cutoff-division normalization and preserve the stated adjoint identities.']
    gh=['J is an integer at least 1; d=4J+1.', 'Authentic single real Gamma multiplier m_J is the displayed positive infinite sum.']
    claims=[
      claim('INS.CAUSAL.01','For all such S,A,L,q, fiber congruence iff a commuting quotient exists and every finite accepted word lifts from every source representative.',ch,causal,'INSTITUTE_CAUSAL_DESCENT.md',authority='LEAN_KERNEL_PROVED',declarations=('quotient_exists_iff_fiber_congruent','run_naturality','every_representative_lifts','lawful_quotient_iff'),source_path='formal/NoGhost.lean',prior='Partial Mealy coalgebra congruences, Silva et al. arXiv:1302.1046v2; classical specialization.'),
      claim('INS.CAUSAL.02','For every relational source edge and finite report word, reachability iff one complete source path; no path iff a constructive backward exclusion; source-invariant edges preserve source along paths.',['Arbitrary relation S x L x S; finite word.', 'Source-identity preservation assumes each edge preserves that identity.'],causal,'INSTITUTE_CAUSAL_DESCENT.md',authority='LEAN_KERNEL_PROVED',declarations=('reachable_iff_single_source_path','path_preserves_source','exclusion_refutes_path','no_path_iff_excluded'),source_path='formal/NoGhost.lean'),
      claim('INS.CAUSAL.03','For every declared finite deterministic system, Moore refinement terminates at the coarsest lawful refinement of current reports; separate pair-BFS supplies actual finite distinguishing words.',['Complete finite declared state/action tables; current observation and exact cost labels.'],causal,'INSTITUTE_CAUSAL_DESCENT.md',prior='Classical Nerode/Moore minimization and bisimulation; no new academic priority.'),
      claim('INS.HAAR.00','For every positive integer a, mu(aA)=mu(A)/a; U_a is isometric, U_a* f(x)=a^-1/2 f(ax), and U_a U_a* is multiplication by 1_(aZhat).',hh,haar,'INSTITUTE_ATOMIC_HAAR.md',authority='CLASSICAL_IMPORTED',prior='Haar uniqueness, finite-index scaling and CRT; proof reproduced in Section1.'),
      claim('INS.HAAR.01','Every bounded complex-linear all-prime shift-and-adjoint intertwiner in either direction is zero; finite Mobius projectors converge strongly to the atomic vacuum and zero respectively.',hh,haar,'INSTITUTE_ATOMIC_HAAR.md',dependencies=('INS.HAAR.00',),prior='Classical Haar/Euler/Wold ingredients; exact SUCC calibration proved here.'),
      claim('INS.HAAR.02','For every subset S of primes, a nonzero bounded star-intertwiner exists iff sum_(p in S)1/p is finite; then the restricted tuples are unitarily equivalent and all intertwiners are multiplicity-space maps.',hh,haar,'INSTITUTE_ATOMIC_HAAR.md',dependencies=('INS.HAAR.00',),prior='Finite Wold: Sarkar1304.7454. Infinite-sequence caveats: Dan-Guo1907.05815v2. Exact prior art of this arithmetic threshold remains unresolved.'),
      claim('INS.HAAR.03','All algebraic star-intertwiners c00->Dprime correspond exactly to unit-supported distributions eta through J_eta e_n=n^-1/2(m_n)_*eta; nonzero eta gives injection.',hh+['D is the locally constant test space with its inductive-limit topology; distribution actions transpose the opposite test adjoints.'],dist,'INSTITUTE_ATOMIC_HAAR.md',dependencies=('INS.HAAR.00',),prior='Classical distribution transposition and clopen support separation; project-local classification.'),
      claim('INS.HAAR.04','The canonical weighted Dirac map is continuous on X=sum |a_n|/sqrt(n)<infinity and weighted ell2(n^s), s>0, but its c00 graph from unweighted ell2 to weak Dprime is not closable.',hh+['D is the locally constant test space with its inductive-limit topology; distribution actions transpose the opposite test adjoints.','eta=delta_1 for the canonical map.'],dist,'INSTITUTE_ATOMIC_HAAR.md',dependencies=('INS.HAAR.03',),prior='Classical summability and harmonic residue equidistribution; no academic priority established.'),
      claim('INS.GAMMA.01','For every J>=1 and real xi, the two-sided logarithmic envelope (1) holds; shift2 is optimal uniformly within its stated logarithmic upper-bound family.',gh,gamma,'INSTITUTE_ARITHMETIC_ANALYSIS.md',source_path='observational_succ/source_weil_hierarchy.py',prior='Classical convex midpoint/trapezoidal quadrature and digamma series; source-specific inequality newly implemented.'),
      claim('INS.GAMMA.02','For every bounded interval I, Gamma_tail action is bounded by13/[16(d-2)]||Fprime|| on H1_0 and2/(d-2)^2||Fsecond|| on H2_0.',gh+['Zero extension is in H1(R), or H2(R) with both value and derivative trace zero for the second estimate.'],gamma,'INSTITUTE_ARITHMETIC_ANALYSIS.md',dependencies=('INS.GAMMA.01',),source_path='observational_succ/source_weil_hierarchy.py',prior='Classical Plancherel and proved multiplier envelope; precise operator domains retained.'),
      claim('INS.SCHUR.PREMISES','The complete pinned PR177 source adapter and inherited all-high K-relative coercivity inequalities satisfy every analytic hypothesis needed for the reported S4 enclosure.',['Original source identity alone is insufficient to prove its analytic estimates.'],schur,'INSTITUTE_ARITHMETIC_ANALYSIS.md',authority='UNVERIFIED',debt=('Full independent audit of inherited infinite-high coercivity and all source adapters not performed in this run.',),source_path='observational_succ/source_weil_hierarchy.py',next_probe='Independently certify the inherited high inequalities and adapter identities on the same primitive domain.'),
      claim('INS.GAMMA.03','Conditional on the explicitly assumed source premises, the same J8 trials and errors yield strictly improved original Schur lower bounds; both computed lower blocks remain non-PSD.',gh+['Zero extension is in H1(R), or H2(R) with both value and derivative trace zero for the second estimate.','Original source identity alone is insufficient to prove its analytic estimates.','ASSUME:INS.SCHUR.PREMISES'],schur,'INSTITUTE_ARITHMETIC_ANALYSIS.md',dependencies=('INS.GAMMA.02','INS.SCHUR.PREMISES'),debt=('INS.SCHUR.PREMISES',),source_path='observational_succ/source_weil_hierarchy.py',next_probe='Use the actual residual spectral distribution to reduce the remaining source-relative upper error.'),
      claim('INS.RH.OPEN','Original S4>=0 and all-radii signed completed Weil positivity remain unresolved.',['All source, topology and infinite-high response obligations must be discharged.'],schur,'INSTITUTE_ARITHMETIC_ANALYSIS.md',authority='UNVERIFIED',debt=('First-window sign not decided.', 'All-radii requirement separate and open.'),source_path='observational_succ/source_weil_hierarchy.py',next_probe='Source-authenticated infinite high-response bound strong enough to decide the first sign; then separate all-radii analysis.'),
      claim('INS.SCHUR.METHOD_NOGO','For each retained J24 parity pair T,M and positive kappa, kappa*T11-M11<0; hence for every eta>0 and every positive semidefinite D, T-[(1+eta)M+D]/kappa is not positive semidefinite, including zero error allowance D=0.',
            ['T,M,kappa are precisely the retained rational J24/M192/P18 decomposition; M is positive semidefinite and kappa>0.',
             'The conclusion concerns only the displayed sufficient-bound family, not the actual signed source form.'],
            dict(source='Pinned PR177 J24 rational decomposition',carrier='two-by-two real symmetric matrices',topology='finite-dimensional quadratic order'),
            'INSTITUTE_ARITHMETIC_ANALYSIS.md',source_path='observational_succ/source_weil_hierarchy.py',
            prior='Classical quadratic-order obstruction and Young inequality; exact source-instance certificate is new to this project.',
            next_probe='Change the legal trials, residual geometry or proved high-response bound; reducing column error budgets alone cannot repair these retained matrices.')
    ]
    table={c['claim_id']:c for c in claims}
    for c in claims:
        c['evidence'].append(evidence(PREFIX+'INSTITUTE_HOSTILE_AUDIT.md','HOSTILE_REVIEW'))
        if c['claim_id'].startswith('INS.CAUSAL.'):
            c['evidence'] += [evidence('observational_succ/institute_causal.py','IMPLEMENTATION'),
                              evidence('tests/test_institute_causal.py','ADVERSARIAL_TESTS')]
        if c['claim_id'].startswith('INS.HAAR.'):
            c['evidence'] += [evidence('observational_succ/institute_atomic_haar.py','IMPLEMENTATION'),
                              evidence('tests/test_institute_atomic_haar.py','ADVERSARIAL_TESTS')]
        if c['claim_id'].startswith('INS.GAMMA.'):
            c['evidence'] += [evidence('scripts/institute_schur_probe.py','IMPLEMENTATION'),
                              evidence('tests/test_institute_schur.py','ADVERSARIAL_TESTS')]
    for cid in ('INS.GAMMA.01','INS.GAMMA.02','INS.GAMMA.03'):
        table[cid]['evidence'].append(evidence(PREFIX+'INSTITUTE_GAMMA_RECEIPT.json','EXACT_FINITE_CALIBRATION'))
    table['INS.GAMMA.03']['evidence'].append(evidence(PREFIX+'INSTITUTE_GAMMA_SCHUR_REPLAY.json','EXACT_SOURCE_REPLAY'))
    table['INS.GAMMA.03']['evidence'].append(evidence(PREFIX+'INSTITUTE_GAMMA_SCHUR_J24.json','EXACT_SOURCE_REPLAY'))
    for path,kind in (
      (PREFIX+'INSTITUTE_GAMMA_ETA_SOURCE.json','EXACT_SOURCE_DECOMPOSITION'),
      (PREFIX+'INSTITUTE_GAMMA_ETA_SEARCH.json','EXACT_FINITE_CALIBRATION'),
      ('scripts/institute_eta_probe.py','IMPLEMENTATION'),
      ('tests/test_institute_hostile.py','INDEPENDENT_RECONSTRUCTION'),
      ('tests/test_institute_eta.py','ADVERSARIAL_TESTS')):
        table['INS.SCHUR.METHOD_NOGO']['evidence'].append(evidence(path,kind))
    for cid in ('INS.GAMMA.03','INS.SCHUR.PREMISES','INS.SCHUR.METHOD_NOGO'):
        table[cid]['git_sources'].append(git_source('observational_succ/original_continuum_residual.py',
                                                   'f309d9104ba480c1999c962af1df7c50f19e1bfe'))
    transports=[]
    for source,target,obligation in (
      ('INS.HAAR.00','INS.HAAR.03','Locally constant domain invariance and opposite-test-adjoint transpose; this is not a bounded Hilbert transport.'),
      ('INS.GAMMA.02','INS.GAMMA.03','Insert the proved Gamma action norm in the original residual error ledger on identical H2_0 trials; preserve source-conditional K geometry.')):
        transports.append(dict(**{'from':source,'to':target}, input=table[source]['signature'],output=table[target]['signature'],authority='PAPER_PROVED',obligation=obligation,evidence=table[target]['evidence'][0]))
    aliases={c['claim_id']:f'INS-{i:02d}' for i,c in enumerate(claims,1)}
    for c in claims:
        c['research_label']=c['claim_id']
        c['claim_id']=aliases[c['claim_id']]
        c['dependencies']=[aliases[d] for d in c['dependencies']]
        c['hypotheses']=[('ASSUME:'+aliases[h[7:]]) if h.startswith('ASSUME:') else h
                         for h in c['hypotheses']]
        c['proof_debt']=[aliases.get(d,d) for d in c['proof_debt']]
    for e in transports:
        e['from'],e['to']=aliases[e['from']],aliases[e['to']]
    registry=dict(schema='SUCC_INSTITUTE_v1', claims=claims, transports=transports,
                  semantics='Recorded authorities are not issued by the integrity auditor. Finite evidence cannot establish the displayed universal statements.')
    path=ROOT/PREFIX/'institute/theorem_registry.json'
    path.write_text(json.dumps(registry,indent=2)+'\n')
    print('Wrote',len(claims),'reviewed records to',path)


if __name__ == '__main__':
    main()
