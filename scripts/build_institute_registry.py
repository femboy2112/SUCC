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
          dependencies=(), debt=(), declarations=(), kernel_artifacts=None, source_path='docs/FOUNDATIONS.md',
          prior='Classical mathematics specialized to explicitly declared source types.',
          novelty='PROJECT_LOCAL; academic novelty not established.',
          next_probe='Independent source and domain audit of the displayed quantified theorem.'):
    kernel = authority == 'LEAN_KERNEL_PROVED'
    open_target = authority == 'UNVERIFIED'
    finite = authority == 'EXACT_FINITE_CHECK'
    ev = [evidence(PREFIX+paper)]
    if kernel:
        artifacts = kernel_artifacts or ('formal/InstituteCausal.lean',
            PREFIX+'institute/kernel_receipt.json', PREFIX+'institute/axioms.json')
        ev += [evidence(path, kind) for path, kind in zip(artifacts,
            ('LEAN_SOURCE','LEAN_RECEIPT','AXIOM_MANIFEST'))]
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
        c['kernel_declarations']=[d if '.' in d else 'ObservationalSUCC.InstituteCausal.'+d for d in declarations]
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
    # Round II is additive in the same graph; INS-01..14 retain their IDs.
    policy_sig=dict(source='Declared source-indexed nondeterministic relation',
                    carrier='arbitrary states, outcomes and well-founded public policy trees',
                    topology='set-level sure safety; no probability or infinite-run theorem')
    policy_h=['E is the entire declared relation S x A x O x S; a policy sees only retained outcomes.',
              'Policies are well-founded public trees; the Horizon predicate separately imposes uniform finite depth.']
    causal_artifacts=('formal/round2/PublicBelief.lean', PREFIX+'round2/causal_kernel_receipt.json', PREFIX+'round2/causal_axioms.json')
    residue_artifacts=('formal/round2/ResidueTransfer.lean', PREFIX+'round2/operators_lean_receipt.json', PREFIX+'round2/operators_axioms.json')
    round2=[
      claim('INS.ROUND2.FORWARD',
        'For every subset S of primes, a nonzero bounded complex-linear forward-only intertwiner in either direction between the atomic shifts and normalized additive-Haar dilations exists iff sum_(p in S)1/p is finite. In the convergent case a unitary exists; in the divergent case every such intertwiner is zero.',
        hh+['All intertwining conclusions quantify only over bounded complex-linear maps and subsets of genuine primes; forward-only claims impose no adjoint equation on the map.'],
        haar,'ROUND2_OPERATORS.md',dependencies=('INS.HAAR.00',),
        prior='Classical Euler products, finite-group coset transfer, Fourier/Bessel bounds and Wold shell construction. Related Dirichlet-convolution obstructions in Hilberdink; exact academic priority unknown.',
        next_probe='Search exact arithmetic representation prior art and formalize the measure/Fourier argument beyond the checked residue core.'),
      claim('INS.ROUND2.COMPLETION',
        'For finite F subset G, normalized avoidance vacua have overlap sqrt(alpha_G/alpha_F) and squared distance 2(1-sqrt(alpha_G/alpha_F)). For every eventually exhaustive sequence of finite prime sets with divergent reciprocal sum, every choice of exact finite-prime unitary intertwiners converges WOT to zero, while preserving each basis norm. Uniformly bounded asymptotically forward-intertwining sequences also converge WOT to zero.',
        hh+['All intertwining conclusions quantify only over bounded complex-linear maps and subsets of genuine primes; forward-only claims impose no adjoint equation on the map.',
            'For the escape assertion, each fixed selected prime is eventually included, its reciprocal sum diverges, and the finite maps are unitary; the asymptotic variant assumes a uniform operator norm bound and WOT intertwining defects tending to zero.'],
        dict(source=haar['source'],carrier=haar['carrier'],topology='Hilbert norms and WOT explicitly distinguished; no strong or norm convergence of unitaries'),
        'ROUND2_COMPLETION.md',dependencies=('INS.ROUND2.FORWARD',),
        prior='Classical Haar continuity, weak-operator compactness and unitary adjoint identities; arithmetic specialization.',
        next_probe='Sharp quantitative decay for specified finite Fourier test families and exact priority comparison.'),
      claim('INS.ROUND2.GRAM',
        'For every N>=1, the normalized GCD Gram of U_n1 is gcd(m,n)/sqrt(mn), with determinant product(phi(n)/n)>0, norm squared at least H_N and the exact divisor Rayleigh value R_N. R_N=(2/pi^2)(log N)^2+O(log N). More generally a fixed consistent synthesis extends boundedly from ell2 iff all finite Grams share one uniform upper bound.',
        hh+['Natural initial segment 1..N; all spectral finite certificates use exact rational bounds.',
            'The general Bessel completion criterion uses fixed vectors in one complete Hilbert target, consistent columns and one bound uniform over all finite index sets.'],
        dict(source=haar['source'],carrier='finite GCD Grams; consistent synthesis into a fixed Hilbert space',topology='quadratic order and Hilbert operator norm'),
        'ROUND2_OPERATORS.md',dependencies=('INS.HAAR.00',),
        prior='Smith GCD determinant and classical Bessel criterion; Bondarenko-Seip critical GCD bounds and Hilberdink. No optimal largest-eigenvalue asymptotic claimed.',
        next_probe='Improve certified spectral brackets and compare arithmetic lower bounds to critical GCD spectral theory.'),
      claim('INS.ROUND2.WEIGHT',
        'For every sequence 0<w_n<infinity, J(e_n)=n^-1/2 delta_n extends continuously ell2(w)->weak Dprime(Zhat) iff Cw^2=sum1/(n*w_n)<infinity; equivalently it is bounded into measures with exact TV operator norm Cw. The forward and original backward actions are bounded exactly when sup w_pn/w_n and sup w_n/w_pn are finite. Summability alone does not bound the forward action; the weighted Hilbert adjoint is different.',
        hh+['D is the locally constant LF test space, with weak distribution dual; all weights are finite and strictly positive.',
            'Distribution actions are opposite-test-adjoint transposes; no Hilbert star-equivalence is asserted.'],
        dict(source=haar['source'],carrier='weighted ell2, finite measures and locally constant test dual',topology='weighted Hilbert norm; total variation; weak distribution topology'),
        'ROUND2_COMPLETION.md',dependencies=('INS.HAAR.00',),
        prior='Classical weighted Hilbert duality, total variation and Bruhat distribution transposition; exact project interface criterion.',
        next_probe='Formalize measure-valued extension and derive optimal domain choices for a specified bounded source-action grammar.'),
      claim('INS.ROUND2.POLICY',
        'For every relation E, belief B and well-founded public policy P, belief sure-safety iff P is source-safe from every s in B. The same-controller existence equivalence holds at each finite Horizon n; Boolean private existential choices need not glue to one public action. For guard_j enabled iff s differs from j, its uniform availability is equivalent to absence of j from the belief.',
        policy_h,policy_sig,'ROUND2_CAUSAL.md',authority='LEAN_KERNEL_PROVED',kernel_artifacts=causal_artifacts,
        declarations=tuple('ObservationalSUCC.Round2.PublicBelief.'+d for d in ('belief_safe_iff_all_sources','uniform_controller_iff','private_choices_do_not_glue','guard_safe_iff_absent','differing_beliefs_have_separating_guard')),
        prior='Classical knowledge-set/sure-safety games and quantifier separation; new precise kernel specialization.'),
      claim('INS.ROUND2.QUOTIENT',
        'For every q:S->Q and relation E, an exact representative-wise relational quotient exists iff projected successor predicates are constant on each fiber; every such quotient commutes with full belief update and preserves and reflects every public policy safety judgment.',
        policy_h+['Exactness means down(qs,a,o,y) iff exists t:E(s,a,o,t) and qt=y, for each fixed s. Off-image behavior is unconstrained.'],
        policy_sig,'ROUND2_CAUSAL.md',authority='LEAN_KERNEL_PROVED',dependencies=('INS.ROUND2.POLICY',),kernel_artifacts=causal_artifacts,
        declarations=tuple('ObservationalSUCC.Round2.PublicBelief.'+d for d in ('exact_quotient_exists_iff','quotient_enabled_iff','image_post_iff','source_policy_descent_iff','belief_policy_descent_iff')),
        prior='Classical relational coalgebra/bisimulation quotient, strengthened project kernel beyond deterministic partial actions.'),
      claim('INS.ROUND2.INTERFACE',
        'For finite declared sources, equality of safe menus and report successors along common safe prefixes iff all public finite-policy safety judgments and all shared-safe-policy possible transcripts agree. Trace equivalence alone fails. For every n>=1 an n-state source has 2^n-1 reachable beliefs with pairwise different safe menus, forcing that many states in any exact deterministic explicit menu monitor.',
        policy_h+['Finite complete source tables; original tags immutable; initial full support; no absent transition is replaced by a failure event.',
            'The exponential bound is explicit monitor state size, not winning-controller memory or a new complexity-class lower bound.'],
        dict(source=policy_sig['source'],carrier='finite source-indexed belief interfaces and complete public policy experiments',topology='exact finite support; stochastic kernels separate'),
        'ROUND2_CAUSAL.md',dependencies=('INS.ROUND2.POLICY',),
        prior='Classical process semantics, partial-observation games and subset construction; source-bound counterexamples and exact independent oracles new to SUCC.',
        next_probe='Mechanize weakest safe-interface theorem; test an explicitly specified quantitative stochastic extension against exact kernel mutations.'),
      claim('INS.ROUND2.RESIDUE',
        'For natural q,r,t,n, a fixed inverse residue multiplier transfers n mod q=r mod q to tn mod q=1 mod q; positive multiplication is injective. A multiplicatively closed predicate is retained and t<=C,n<=N implies tn<=CN. Existence of inverse representatives and harmonic divergence are not kernel claims.',
        ['Explicit modular inverse equality, residue membership and multiplicative closure hypotheses; t>0 for injectivity.'],
        dict(source='natural multiplication and declared modular equalities',carrier='Nat and multiplicatively closed predicates',topology='discrete algebra; no series or Hilbert completion'),
        'ROUND2_OPERATORS.md',authority='LEAN_KERNEL_PROVED',kernel_artifacts=residue_artifacts,
        declarations=tuple('ObservationalSUCC.Round2.'+d for d in ('residue_transfer','transfer_injective','controlled_monoid_transfer')),
        prior='Elementary modular arithmetic and cancellation; scoped algebra core of the paper finite-group transfer.')
    ]
    for c in round2:
        c['git_sources'].append(git_source('research/2026-10-18/INSTITUTE_ATOMIC_HAAR.md' if c['claim_id'] not in ('INS.ROUND2.POLICY','INS.ROUND2.QUOTIENT','INS.ROUND2.INTERFACE') else 'research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md','e42096ec0186228dd0f748767599e470f2ca2e1d'))
        module = 'causal' if c['claim_id'] in ('INS.ROUND2.POLICY','INS.ROUND2.QUOTIENT','INS.ROUND2.INTERFACE') else 'completion' if c['claim_id'] in ('INS.ROUND2.WEIGHT','INS.ROUND2.COMPLETION') else 'operators'
        c['evidence'] += [evidence('observational_succ/round2_'+module+'.py','IMPLEMENTATION'),
                          evidence('tests/test_round2_'+module+'.py','ADVERSARIAL_TESTS')]
        if c['claim_id']=='INS.ROUND2.GRAM':
            c['evidence'].append(evidence(PREFIX+'ROUND2_COMPLETION.md'))
        c['independent_check']='Principal derivation and separate authoring-stream review, alternative exact oracles and kernel runs; shared model/source lineage, not external referees.'
    claims.extend(round2)
    table={c['claim_id']:c for c in claims}
    for c in claims:
        if not c['claim_id'].startswith('INS.ROUND2.'):
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
    for target in round2:
        for dep in target['dependencies']:
            parent=table[dep]
            if parent['signature'] != target['signature']:
                transports.append(dict(**{'from':dep,'to':target['claim_id']},
                    input=parent['signature'],output=target['signature'],authority='PAPER_PROVED',
                    obligation='Explicit source-preserving restriction/extension and topology obligations proved in the cited Round II manuscript; no finite-to-infinite promotion.',
                    evidence=target['evidence'][0]))
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
