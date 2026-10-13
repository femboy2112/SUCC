"""Render the F48 validation matrix from owned annotations and frozen receipt."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

# ID; typed objects/maps; load-bearing conditions; limitation/no-go; next lemma.
ROWS = '''
A01;P(X), FinSet^X, f* and dependent sums; commuting square, complete comparison; predicate BC needs onto, witnesses need bijection; mechanize witness-family BC
A02;C→Set^(Jop), actual precomposition; free finite DAG paths, reachable precursors; object separation does not imply arrow faithfulness; nonfree separation plus lawful precursor access
A03;integral primitive torsor sheaf, overlap walk maps; exact shared darts, connected charts, every overlap component; modular LCM shadows hide integral periods; nonabelian source-retaining descent
A04;π1→Sym(X), equivariant sections on covers; connected graph, finite nonempty fiber, invertible transport; nonregular deck-invariance fails descent; formalize full kernel-pair and core-index bounds
A05;Lan_K ⊣ K* ⊣ Ran_K in FinSet/P; finite diagrams, exact tag-preserving maps; empty comma products create candidates without receipts; supported Kan-extension admission
A06;E↦intersection of all action pullbacks; complete total stationary source, lawful homomorphisms; report-only maps fail repair naturality; partial/history-indexed congruence repair
A07;weighted record spans and apex 2-cells; full boundary interface, normalized rational input rows; equal kernels need not admit apex maps; partial-domain weighted history composition
A08;history category→[0,∞] enriched homs; same complete endpoint, subadditive costs; fresh/spent switching breaks triangle; budget-interface policy composition
B09;source trace→all-finite images→inverse family; discrete reports, complete profiles, actual restrictions; raw prefixes are not complete-source stages; explicit list/Finset and extendability adapters
B10;finite-shadow infima→minimum source cost; continuous probes, Hausdorff source, finite compact-sublevel cost; Polish source and expensive chosen sequence do not decide minimum escape; kernel formalization of capped FIP
B11;partial mismatch extractor, product-state BFS; complete finite source, effective contexts and mismatch; no total selector for arbitrary computable target; explicit bounded target grammar
B12;partial records, directed union, context pullback; finite discrete alphabet, closed source image; ideal completion can add unsupported records; source-retaining partial-domain translation
B13;proof inclusions and finite birth-support extraction; nested syntax, premises and actual finite rule instances; omega union adds no limit-only finitary proof; nonidentity inference-preserving syntax transport
B14;cylinder decision→discrete/Sierpinski target; relative clopen/open fibers, c.e. family for effectiveness; pointwise termination need not have uniform horizon; effective homogeneous-cylinder certificates
B15;X→O^(A*) final deterministic trace; total stationary deterministic coalgebra; equal relational/probability traces need not be bisimilar; typed branching determinization
B16;state→continuation residual; complete deterministic word behavior, fixed stationary controller; observer storage, source memory and external schedule differ; incomplete-sample partition completion
C17;joint nonnegative law T_(h,a,o), natural pushforward; original/current law square for all Dirac rows; removing zero loses impossible-word opcartesian lift; partial-domain law functor
C18;G(u,v)=uv/s, Bayes, marginal projection; positive normalization, CI and supported rank-one likelihood; marginals/support do not determine joint law, duplicate receipt doubles evidence; measurable separator gluing
C19;CP history→original effect and positive-support class; fixed original finite dimension, common branches and complete memory; no deadline or positive infinite-event probability; noncomputable witness selection and apparatus audit
C20;source-blind stochastic triangle F=EK; same original parameters, all finite decisions/rewards; one-shot dominance misses carrier destruction; full stateful instrument simulation
C21;robust belief reachability and max-plus private cost; stationary original/current relations, safe actions, nonnegative cost; scalar zero Bellman value need not terminate; compare budget lift with private-path enumeration
C22;occurrence-word quotient and per-report squares; causal ancestry retained, enabling persistence, declared independence; endpoint/total-channel equality is insufficient; contextual independence with shared memory
C23;conditional e-wealth and optional projection; full calibrated null laws, common public adapted policy; crossing is no posterior truth or deductive certificate; law recalibration under changed intervention
C24;deterministic retained map, conditional loss, auxiliary embedding; complete accessible side information and joint law; logical entropy/cardinality gives no joules; physical memory and cyclic-reset account
D25;bounded itinerary qf=Gq; complete boundary-excised source words, fixed language; boundary fixed point defeats everywhere flip; certified changed source language
D26;realized itinerary, buffered truncation, affine return conjugacy; actual original source, constant return time2; every finite B-word does not realize B∞; variable return-time cocycle
D27;observable algebra pullback J, Koopman/PF adjoints; full measurable algebra or continuous compact quotient; linear dictionary and a.e. factor differ from pointwise full algebra; source-specific full-algebra invariance
D28;Lipschitz error recurrence→report budget; certified trajectory tube and report metric; folds/constant reports defeat universal lower debt; monotone co-Lipschitz source tube
D29;proper full-flow semiconjugacy and isolation pullback; locally compact full flows, proper onto map; isolation does not universally preserve Conley index; index-pair homotopy equivalence
D30;projection P, derivative PF, source-fiber closure; complete source space, linear P, stated quadratic/Galerkin domain; hidden stress accelerates resolved modes; closure repair on restricted physical fibers
D31;Lorentz source/probe/record covariance; declared maps, discrete conditional laws, transported policy/cost/ancestry; geometry supplies no delivered event, continuous singleton inference fails; non-atomic inference contract
D32;delay map O_k, original/current target rows; known stationary source/dimension, passive or known backaction; finite Hankel rank is no unknown-source upper bound; source-attested readout backaction
E33;affine monoid normal form and residue groupoid; genuine domain, nonunit actions kept outside inverses; relations do not identify Euler source; source-sensitive matched non-Euler discriminator
E34;prime jets, full valuations, diagonal square; verified prime, positive source, explicit unit/residue budget; fixed-depth exact successor valuation impossible; bounded source unit/height certificate
E35;full Mahler coefficients→continuous extension and clock maps; entire tail tending0, same-depth1-Lipschitz for clock naturality; finite coefficients and local CRT limits need no diagonal source; uniform source-tail modulus
E36;Dirichlet log/exp and mixed-defect decomposition; normalized Q-algebra source, coefficientwise restrictions; formal completion is not analytic convergence; full source absolute norm/tail bounds
E37;finite factorial Mellin→Gamma and Schwartz term; connected analytic domains, compact convergence, declared tail domination; counterfeit arithmetic shares Gamma; genuine completed source-form identification
E38;source tape→signed completed distribution/form; original prime powers, poles/Gamma, half-density and smooth test core; magnitude/covariance positivity cannot identify signed Weil form; one-interval source-faithful form-error bound
E39;complete prime halo cut and retained residue-voltage map; every source vertex/dart and boundary certificate; residue loop need not lift to periodic prime path; minimal source-retaining arithmetic refinement
E40;delay-resolvent map and source/basis similarity; complete finite linear source, regular spectral parameter; scalar target changes and unknown dimension defeat zero identification; quantitative compact-domain response bound
F41;unitriangular source→behavioral action→cover tower; complete named finite action family, fixed readout; minimal observer states differ from holonomy trivialization degree; arbitrary-modulus faithful action formalization
F42;read/pre/meet source-surjection genes; complete supplied constructors and retained witness defects; search cannot invent unavailable constructor or sensor; fresh noncommuting two-action verifier
F43;opaque endpoint signatures→law classes, action quotient; fixed primitive-variable grammar and frozen complete tables; learned laws do not recover hidden order or family identity; separately authored larger grammar/source, no holdout replay
F44;source→complete fixed-word laws→public adaptive output; source-blind policy/randomness, complete admitted source law; computation cannot split old operational equivalence; genuine authorized target-relevant law refinement
F45;fair retained occurrences→nonnegative cost sum; mandatory originals, exhaustive legal scheduling, common cost/lower bound; weighted debt convergence is no finite completion or computable modulus; lawful alternative summable discharge
F46;source-fiber radius, conflict coloring, exact repair; rational L∞ targets and unconstrained decoder; positive tolerance lacks coarsest repair, midpoint may be unrealizable; legal one-carrier tolerant encoder
F47;calibration H/D, atomic pair averages, decoded invariant; known affine units/origins, committed events, covered blocks; raw agreement is no source-time lock, dyadic means need no finite equality; sharp calibration-error propagation
F48;private-prefix fibration, incidence sheaf, pruning adapter; complete σ/memory/resource interfaces and all local branches; Kraus atoms and global fairness cannot be inferred from local prefixes; mechanize greatest surjective subsystem and lawful policy map
X01;retained receipt limit E→labelled image closure; continuous discrete labels, compact/coercive supported receipt space; compact source alone misses empty receipt fiber; kernel supported-image exchange
X02;holonomy orbit R/J and Reynolds projection; exact reported update commutation with JR; invariant laws cannot supply equivariant atomic selector; joint orbit law and source-target adapter
X03;integral periods→bounded modular guard/CEGIS; actual integer access or proved generator bound, complete grammar; adaptive finite modular menu always leaves LCM alias; partial/history-dependent retained counterexample grammar
X04;itinerary phase and exact-future residual quotient; strongly connected graph and all finite word realization; finite residual image is weaker than current phase autonomy; source-image proof when legal words are missing
X05;joint causal garbling→adaptive proof policy; prepared joint square, one-way safe availability lifting, public decoder/cost; marginal squares and private cost claims fail; history-indexed stochastic carrier simulation
X06;cost-labelled residual interface→memory/path geometry; complete stationary actions, left-cancellative charge monoid; summability differs from finite control/storage memory; partial-action budget path lifting
X07;positive ideal functor→greatest attained zero face; directed all finite ideals, common maps, finite-height original cone; positive finite support gives neither infinite mass nor quantum copy; complete apparatus-memory ideal functor
X08;affine prime itinerary→local balls and max-plus precision; genuine intermediate domains, cap and full offsets, ambient valuation; demand is itinerary invariant, not reduced groupoid/source-minimal depth; prime-realizable sharp-depth witnesses
X09;supported analytic receipts→jets/order/precision cost; connected Hol domain, continuous labels, compact cost sublevels; complex coefficients use usual topology, cap covers every order/precision; source-labelled completed form plus uniform test estimate
X10;future algebra π*C(Q), Hilbert H/W, PF resolvent; compact continuous source and stipulated invariant probability; future U-closure not reducing, two-delay recovery can miss ab in linear sector; nonlinear dictionary and inverse-time closure
X11;CP support dominance, negative-information choice, periodic generator; fixed originals, filter-complete necessity, exact rational numerals, closed no-input generator; promised qubit bound μ+λ≤N is sharp, stationary report word lacks deadline; formalize promised cycle bound with full current interface
X12;greatest hereditary feasible complex and exact face images; complete original/current/memory, homogeneous legality, lawful source squares; facet widening invents source/current, no canonical tolerant partition; nondeterministic branch-indexed exact-image hereditary repair
'''.strip()


def link(path):
    parts = Path(path).parts
    try:
        i = parts.index('2026-10-13')
    except ValueError:
        return path
    suffix = '/'.join(parts[i+1:])
    return suffix.removeprefix('F48/') if suffix.startswith('F48/') else '../' + suffix


def main():
    receipt = json.loads((HERE/'F48_PHASE2_RECEIPT.json').read_text())
    records = {r['id']:r for r in receipt['records']}
    rows = [line.split(';') for line in ROWS.splitlines()]
    assert all(len(row)==5 for row in rows)
    assert {row[0] for row in rows} == set(records) and len(rows) == 60
    out = ['# F48 whole-swarm validation matrix', '',
           'All IDs below are **owned PR49 IDs**. PR50/51 comparisons remain branch-qualified in the phase2 architecture. Status is frozen from the hashed root registry in [receipt](F48_PHASE2_RECEIPT.json); it is not a new replay or proof promotion. Mathematical core, typed maps, domains and obstructions were inspected across all available author dossiers and reviews. Missing review files are not invented.', '',
           'A = root accepted classical/paper result; K = only named kernel subclaims. All twelve synthesis inputs are accepted in this frozen snapshot. Fresh A03 review accepts F48 T1/T2 and the conditional type gates, without recertifying every input theorem. Final principal artifact review remains pending. Read each linked dossier and available review for the full quantifiers.', '',
           '| Slot / evidence | Status | Typed object and actual arrow | Required domain / hypotheses | Preserved boundary or no-go | Next small lemma |',
           '|---|---|---|---|---|---|']
    for ident, arrow, conditions, boundary, lemma in rows:
        e=records[ident]
        label=f'[{ident}]({link(e["dossier"])})' if e['dossier_present'] else ident+' (missing)'
        if e['review_paths']:
            label += ' / ' + ', '.join(f'[R{i+1}]({link(p)})' for i,p in enumerate(e['review_paths']))
        if ident=='F48': status='Initial A; K injection core; A03 phase2 A; principal artifacts pending'
        elif e['integration']=='ACCEPTED': status='A'
        else: status='TENTATIVE' if e['dossier_present'] else 'AWAITING_FINAL_INPUT'
        if ident in ('A01','B09','C19','X07'):status += '; K named core'
        out.append('| '+ ' | '.join([label,status,arrow,conditions,boundary,lemma])+' |')
    out += ['', 'The strongest admitted architecture is a network of typed functors with separate original-source, lawful-access, probability, proof, resource and completion gates. Support is not joint law; cone positivity is not source identification; convergence is not an executed limit or finitary proof. Aggregate E_n depth surjectivity does not imply onto restriction on a selected public-history arrow. Kraus families retain index multiplicity without supplying observed private paths. All synthesis inputs and fresh A03 core review are accepted; final principal artifact review remains pending.', '']
    (HERE/'F48_VALIDATION_MATRIX.md').write_text('\n'.join(out))


if __name__=='__main__':main()
