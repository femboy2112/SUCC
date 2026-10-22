# Observation-pinned intrinsic geometry — SUCC source rigidity and reality calibration

**Date:** 2026-10-22. **Research-only stacked draft** based on reciprocal SUCC/FUCC Pascal `research/reciprocal-succ-fucc-pascal-2026-10-22@735c4176979fad802c4888048892f009b38a3b3b` (PR #236), which depends on PRs #235 and #234. No alterations to main, imported source archives, signed Weil inputs or proof-authority defaults. **Classical mathematical ingredients; new-to-SUCC synthesis; academic novelty UNVERIFIED. No real physical observation was performed. RH and gravitational ER=EPR remain unproved.**

## 1. Proposed rigidity principle, with hypotheses visible

The user's conjectural philosophy is that the mathematics selects a *family* of structures, and a physically performed special observation selects one member. We can prove a **conditional** version if the source model family has been independently constrained.

Declare an oriented arithmetic source with origin 0, actual one-event successor S(n)=n+1, source-authenticated prime multipliers V_q(n)=qn, and compatible finite *ring* quotients C_k of orders p^k for one unknown prime p. Each quotient and bonding map preserves the original source, origin, addition, multiplication and oriented successor. Crucially, the **entire** compatible procyclic p-power family is a hypothesis; no finite observation alone proves it.

Suppose an independent and complete first-level instrument measures a faithful primitive cycle of p distinct phases, including the return to the marked origin and the single-step orientation. Within this declared family, the measurement fixes the candidate prime p, after which all the compatible source structure is unique **up to source-preserving isomorphism**. The epistemically independent question of whether the physical source really belongs to this family remains an open empirical probe.

## 2. OPIG-01 — full source tower forces its p-adic ball geometry (classical)

Each q_k(n) is the n-fold successor of q_k(0)=0; since the generator has exactly p^k distinct phases, the unique oriented source-preserving normal form is

\[
q_k(n)=n\bmod p^k,\qquad
\mathbb Z_p=\varprojlim_k \mathbb Z/p^k\mathbb Z,\qquad
\mathbb Q_p=\operatorname{Frac}(\mathbb Z_p).
\]

This is an inverse-limit ring theorem and not a finite computation. The rooted coset tree is completely determined: a vertex (k,r) is r+p^k Z_p, with parent (k-1,r mod p^{k-1}), and its exactly p children are

\[
(k+1,r+jp^k),\qquad j=0,\ldots,p-1.
\]

The end space is Z_p; Haar probability assigns every depth-k cylinder mass p^{-k}. If **distance is defined** to equal the normalized Haar mass of the smallest common ball, then

\[
d_p(x,y)=p^{-v_p(x-y)}
\]

for distinct points. This is a natural exact metric convention, not a proof that measured physical proper distance must equal it: d_p and d_p² have the same source balls and topology. A finite matching residue only bounds distance and cannot prove global equality.

## 3. OPIG-02 — the prime is identifiable by multiplicative collapse

For m=p^v u, with u invertible mod p^k, multiplying the full clock by m has

\[
|\operatorname{im}V_m|=p^{\max(k-v,0)},\qquad
|\ker V_m|=p^{\min(v,k)}.
\]

Proof: u is a permutation, while multiplying by p^v erases exactly min(v,k) digits. Thus among authenticated rational **prime** multipliers q, the unique contracting one on the p-clock is q=p; the others are permutations. This gives a physically implementable **second independent source probe** after initial clock calibration: check the number of distinct outcomes from the multiplier. A fake primitive 6 contracts at both 2 and 3, demonstrating the need for a prime-source passport.

## 4. OPIG-03 — no arbitrary rays: SUCC/FUCC intrinsically acts on the genuine Bruhat–Tits tree

A key mathematical upgrade from Prime Bridge I and II: rather than selecting three tree rays and attaching a code, use the arithmetic affine semigroup's **faithful projective representation**

\[
\rho(a,b)=\left[\begin{pmatrix}a&b\\0&1\end{pmatrix}\right]
\in \mathrm{PGL}_2(\mathbb Q_p),
\qquad n\mapsto an+b.
\]

Matrix multiplication realizes the entire positive-affine law exactly:

\[
\rho(a,b)\rho(c,d)=\rho(ac,ad+b).
\]

In particular the original SUCC/FUCC law V_q S = S^q V_q is preserved without choosing a tree encoding or fitting parameters. Declare an additional **rank-two free module** Z_p², then form the entire standard Bruhat–Tits tree T_p from homothety classes of rank-two Z_p-lattices in Q_p². Its vertices/edges are source-defined and its degree is p+1, with root neighbors the full projective line P¹(F_p).

At the standard root [Z_p²]:

* Arithmetic SUCC \(\rho(S)=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\) is integral invertible and fixes the root. On its complete first shell it acts as z→z+1 on F_p, one p-cycle, and fixes infinity.
* A genuine multiplier V_q with q≠p is a p-adic unit, hence \(\rho(V_q)=\mathrm{diag}(q,1)\) fixes the root.
* The unique nonunit prime multiplier V_p sends the root to an adjacent vertex and determines the bi-infinite standard apartment of lattice classes \(L_j=p^jZ_pe_1+Z_pe_2\), with graph displacement |j|. Its projective fixed endpoints are 0 and infinity.
* On the compact source Z_p, V_p:z→pz is a contraction by exactly 1/p with **unique fixed point 0**. In source coordinate x=n−1 the law becomes x→px+(p−1), with unique compatible fixed point −1 represented at depth k by p^k−1.

**This is a non-arbitrary geometry-and-action forced within the stated source completion plus rank-two projectivization category.** Its representation is standard arithmetic geometry, not an original gravitational duality. The rank-two lift is an extra axiom; the projective inverse is not identical to the partial Hilbert adjoint V_p† on positive integers, and the action does not determine a unique quantum state, holographic code, Einstein metric or ER wormhole.

## 5. First-shell prediction, followed by hostile holdout

The source-operator fingerprint on the *complete* first Bruhat–Tits shell is a p-cycle plus exactly one fixed direction; values verified independently from homogeneous projective matrices:

| Candidate p | Root degree | SUCC finite cycle | Additional fixed direction | V_p root displacement |
|---|---:|---:|---:|---:|
| 2 | 3 | 2 | 1 | 1 edge |
| 3 | 4 | 3 | 1 | 1 edge |
| 5 | 6 | 5 | 1 | 1 edge |
| 7 | 8 | 7 | 1 | 1 edge |

A genuine local field with residue field F_{p^f} instead has p^{f−1} such p-cycles, so observing only one without full-shell coverage does not determine f.

**Crucial second-level counterexample:** Z/p²Z and F_p[t]/(t²) both have p² elements and reduce to the same F_p first level. Their respective complete local fields Q_p and F_p((t)) therefore yield identical first-shell degree p+1. But p·1 is nonzero in Z/p²Z and zero in F_p[t]/(t²): multiplication by p has image size p versus 1. This held-out second-level observable splits these two models, rather than recycling the observation that selected p.

## 6. Why no single finite observation proves global truth

**Finite-horizon counterfeit.** For any fixed measured depth K, choose a different prime q and the lawful cyclic quotient orders m_k=p^k for k≤K, and m_k=p^k q for k>K. Every source readout through K matches the rigid p-power tower exactly, and the compatible reductions are legal, but at K+1 a new branch factor appears. The strict p-power-family hypothesis is what rules it out—not the observation alone.

**Hidden-state alias.** A four-state physical clock 0→1→2→3→0 viewed through parity gives 0,1,0,1,..., indistinguishable from a genuinely two-state clock by that one sensor. Observing a quotient does not identify the hidden physical carrier.

**Metric/state nonuniqueness.** Even the full p-adic source determines only specified geometry and source symmetry, not a unique gravitational spacetime or EPR quantum state. Different positive states and correlation kernels can share the same PGL₂ geometry.

These are proved counterexamples against **unconditional** pinning, but leave the conditional uniqueness theorem intact.

## 7. Physically performable sanity check, specified before data collection

1. Identify an **independent physical process** with a marked reset and reproducible one-step operation. Name the source and independently calibrated sensors, test for aliases/hidden states, and declare the candidate family first. A computer clock built to enact modular arithmetic validates that apparatus—not fundamental spacetime.
2. Record at least two complete primitive cycles, including every distinguishable phase and the return to the same initial phase; independently verify event orientation.
3. Hide the second-stage sensor reports until after deriving the higher-source predictions. Then test p²-level structure, proper carry and the multiplication-by-p image cardinality p, rather than 1. For a binary counter this is the difference between a legitimate mod-4 carry and a characteristic-two or aliased clock.
4. If the physical carrier independently has two source channels realizing the projective action, test the complete first-shell (p-cycle + fixed direction) and the one-edge dilation, rather than declaring an artificially rendered tree an observation.
5. Separate source-map adequacy, finite evidence, mathematical uniqueness within the family and speculative physical ontology in the claim ledger.

**Physical experimental status: UNVERIFIED.** All supplied transcripts in the software suite are synthetic countermodels or synthetic calibration examples. No observer has measured a physical Bruhat–Tits tree in this work.

## 8. Next proof frontier

The arithmetic action and its *natural local field geometry* now exist with genuine source provenance; the next unmet target is unique **quantum state/dynamics selection**. Construct rival positive states or holographic kernels with the same SUCC/FUCC/PGL₂ symmetry, predict distinct held-out measurable correlators, and determine whether a physically calibrated source measurement chooses one state up to explicit gauge. Neither geometry alone nor positivity of a generic Gibbs covariance identifies the signed completed Weil form.

**Sources:** classical profinite and p-adic arithmetic, Serre's *Trees*, the lattice-theoretic PGL₂(Q_p) construction in https://www.osti.gov/pages/servlets/purl/1425489 (Appendix A). Internal provenance: SUCC PIG-01–07 in `docs/CLAIM_SUPPLEMENT_PRIME_JET_GENESIS.md`, exact local Tate observer modules, and the reciprocal Pascal PR #236. Academic novelty not claimed.
