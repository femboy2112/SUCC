# Principia Intermedia — constructive continuation supplement

## Coherent observer continuation, compulsory null seams, and arithmetic capacity

**Research date:** 2026-11-26. **Originating proposal:** Leah's same-carrier observers at distant or opposite endpoints, with an intermediate-value-shaped law for constructing agreeing observers and forcing a relative zero/seam crossing.

**Result:** a proved framework package with exact finite implementations, a genuine arithmetic observer-space example, and an original-source BBP null-to-crossing construction. The classical ingredients retain their attribution; no historical novelty, native RH reconstruction or pi-normality closure is claimed.

### The central arithmetic theorem

On the fixed carrier Q, consider all absolute-value observers with pointwise convergence. Any two can be joined continuously. A path between nontrivial endpoints can avoid the trivial absolute value **if and only if both endpoints belong to the same place**.

Thus every continuous path between ordinary and p-adic magnitude observers must pass through a single observer where

\[
 \log \nu(q)=0\quad\text{for every nonzero rational }q.
\]

The source is retained. This is a common magnitude-null seam, not erased arithmetic. The canonical path's one-sided derivatives recover the endpoint log-readout functions. A smooth flattened path can instead have every jet vanish at that same seam; analytic switching between distinct places is impossible. These are proved distinctions on one actual arithmetic carrier.

### The finite and continuous construction laws

| Problem | Exact result |
| --- | --- |
| Can the endpoints be joined at finite resolution? | Yes iff forward/backward reachable cones meet at one, equivalently every, cut; return a path or disjoint-cone obstruction. |
| Does every lawful path cross a specified seam? | Assuming an original path exists, yes iff deleting the seam removes endpoint connectivity. |
| What does finite granularity permit? | Edge jumps <=delta force a vertex within delta/2 of zero; values in hZ and jumps <2h force an exact vertex zero. Both thresholds are sharp. |
| Can reports agree around all loops? | Yes from anchor a iff every loop holonomy fixes a. |
| Can prescribed continuum endpoints be joined? | A compact-convex projection construction gives a section under Hausdorff continuity; a separate compact dyadic criterion is necessary and sufficient with one fixed modulus. |
| Does each scalar channel crossing imply a common null? | No. Simultaneous finite-block feasibility plus compactness, or a genuine multidimensional face-sign theorem, supplies the valid lift. |
| Can an orientation change force information loss? | Opposite determinant signs force a singular observer Jacobian, hence an infinitesimally invisible direction. |

### The BBP construction and its quantitative cost

For the original forcing, the existing Mellin measure has moments m_k=r(k+1). For each N, construct its unique monic degree-N polynomial P_N with its first N moment pairings zero. Those null constraints force **exactly N simple crossings in (0,1)**. Its source-resolvent germ has a zero of exactly order N, with a proved positive next jet.

A nonzero polynomial whose coefficients lie in (M/Q)Z has the exact source-dependent moment threshold

\[
 \max_{j\le D}|\langle u^j,P\rangle_\mu|
 \ge \frac{M}{Q\|H_{D+1}^{-1}\|_\infty}.
\]

The construction also exposes its cost: h_N=norm(P_N)^2<=4m_0 16^{-N}. Increasing null order does not yield a nonzero all-order-null field. Unit-norm normalization gives a weakly null family with no strong limit. The source is already available; the unproved application step is to transport an authentic zero-seeded late-shell counterhypothesis into simultaneous constraints that beat the paid arithmetic capacity.

## Read the dossier

| Document | Purpose |
| --- | --- |
| [RESEARCH_CONTRACT.md](RESEARCH_CONTRACT.md) | Exact target, hypotheses, dependency cut, novelty tax and predeclared falsifiers |
| [THEOREMS.md](THEOREMS.md) | PI-01–PI-09: finite extension, separator, granular IVT, holonomy, selection, refinement, joint nulls and rank seam |
| [ARITHMETIC_PLACE_SEAM.md](ARITHMETIC_PLACE_SEAM.md) | PS-01–PS-05: mandatory same-carrier arithmetic seam, retained germs and quantitative capacity |
| [BBP_MOMENT_SEAMS.md](BBP_MOMENT_SEAMS.md) | BM-01–BM-06: exact source-null fields, forced crossings, residual bounds and degeneration |
| [RH_ORACLE.md](RH_ORACLE.md) | Current primary-source oracle audit and the arithmetic hypotheses topology does not supply |
| [FRONTIER_AND_PROVENANCE.md](FRONTIER_AND_PROVENANCE.md) | Live repository reconstruction, inherited state, completed edges and next theorem |
| [CLAIMS.md](CLAIMS.md) | Claim states, domains, countermodels and remaining obligations |
| [VALIDATION.md](VALIDATION.md) | Actual executions, exact receipts, scope and limitations |
| [INTEGRATION.md](INTEGRATION.md) | Relationship to Book VII and PR #691: different nulls, L1 versus L2 fields, and the compact RH normalization contract |

## Code and reproduction

The three additive modules are:

- [principia_intermedia.py](../../../observational_succ/principia_intermedia.py): finite paths, seam deletion, sharp crossing, exact transport.
- [principia_place_seam.py](../../../observational_succ/principia_place_seam.py): retained rational source, exact prime-log readouts, oriented germs and denominator capacity.
- [principia_bbp_seams.py](../../../observational_succ/principia_bbp_seams.py): original-source moments, rational null polynomials and capacity.

Run from the repository root:

~~~sh
python -m unittest tests.test_principia_intermedia tests.test_principia_place_seam tests.test_principia_bbp_seams -v
python research/2026-11-26/principia_intermedia_continuation/independent_oracle.py
python research/2026-11-26/principia_intermedia_continuation/independent_place_oracle.py
python research/2026-11-26/principia_intermedia_continuation/source_moment_oracle.py
~~~

The first three commands use Python's standard library. The source-moment oracle additionally uses SymPy; its observed version is in the receipt. The package's universal mathematical authority is its paper proofs and identified classical inputs, not finite test counts.

## Integration boundary

Stacked on Principia Intermedia PR #691 at 863952de0eb4d7a039fea73f10606203308635ea, which preserves Principia Genesis PR #690 at c5757d48a6788e1513e4276b111f7cdad075055f and Main XXVI at 81be6b897ae980b801a3b9de9e22ef81e8360bfb. The concurrent #691 draft was discovered during publication, inspected, and preserved in full; this supplement occupies a separate directory. The separate #689 null-seed tower is cited at its exact head; it is not silently merged. Additions are three new modules, three new test modules, this research directory, and a navigation link from the preceding dossier.

Historical main statements that RH was open describe their dated research state. The new external RH verification reports are distinguished here from SUCC's still-incomplete native reconstruction. No historical source or ledger was rewritten. R0 and base-16 pi normality remain open in this work.
