# A shared-basis knowledge channel: sparse path/value deltas, boundary codes, and RH constraints

**Date:** 2026-10-11. **Status:** user-originating hypothesis, proved-local/classical math, independently tested exact finite toy models, proposed research program. **No** result about gravitational holography or the truth/provability of RH follows from these toys. Stacked on the verified proof-carrier-backaction PR #12 and prior SUCC observer/provenance work, with no changes to main or the historical RH import.

## 1. Originating insight and what is genuinely new to this research direction

The maintainer proposes that two equally capable observers A,B share the indefinite mathematical basis \(\mathcal B=(1,2,3,\ldots)\), with each number serving as a mutually interpreted *address/direction*, not necessarily as the mathematical magnitude of an observation. A wishes to communicate a newly discovered mathematical or empirical finding C. A does not send its entire model or full historical path: it locates B's *last known field position*, describes the path displacements in that basis and sends the corresponding value deltas. Illustrative packet:

\[
A \longrightarrow T\big((1,4,5),(1,1,1)\big)\longrightarrow B.
\]

The choice of braces in the original intuition is not yet a declaration that the steps commute. There are **two mathematically distinct interpretations**:
1. Sparse coordinates of a difference in a shared additive (abelian) module, where order does not matter;
2. An ordered sequence of state-changing local operations, where a path must be replayed in order and a carrier state/basis can transform between steps.

The maintainer additionally suspects that holographic or mathematical boundary encoding is **load-bearing**, drawing motivation from Susskind, entropy, black holes, and the apparent difficulty of interpreting the zeta zero set. This is an important hypothesis to investigate with explicit encoding/reconstruction theorems, but not a license to equate the zeta critical line with an actual black-hole horizon. The code constructs a deliberately restricted, exact mathematical *boundary representation* to distinguish reconstructability, source-class limitations and measurement precision.

## 2. Finite-support sparse SUCC update theorem

Let \(V=\mathbb Q^{(\mathbb N)}\) be the free vector space of rational sequences with **finite support** and named basis \(e_1,e_2,\ldots\). A finite window \(\mathcal B_N=(e_1,\ldots,e_N)\) is used in the executable laboratory. B has known starting position \(s_B\in V\), A has position \(s_A\in V\). A packet contains the shared basis version, authenticated/trusted starting-state anchor, ordered coordinate addresses \(i_1,\ldots,i_r\), and values \(v_1,\ldots,v_r\), plus an endpoint commitment:

\[
\boxed{s_A=s_B+\Delta,\quad
\Delta=\sum_{j=1}^r v_j e_{i_j}.}
\]

For \((1,4,5)\) and \((1,1,1)\),
\(\Delta=e_1+e_4+e_5\).
The **exact finite catch-up theorem** is immediate: if both parties interpret the same basis/version, start at the same anchored position, and the source values are genuine or otherwise correctly justified, the receiver reconstructs exactly the asserted position by applying those finite coordinate additions.

The packet **does not** contain the rest of \(s_B\) or \(s_A\). The result is a sufficient *relative* representation, not the globally shortest bit encoding or cryptographic source authentication. The shared dictionary, proof library, past receiver state, source-table assumptions, causal provenance and sender verification cost must be charged when comparing actual information budgets.

**Negative controls:** same packet from a different initial vector produces a different endpoint; changed mathematical basis version/anchor is rejected; duplicate addresses, impossible directions, mismatched outcome values and forged endpoint digests are rejected.

## 3. A sparse set is not necessarily a complete path

For noncommuting state transitions, replace a vector-basis action by \(U_{i,v}:S\to S\). The path packet must be ordered:

\[
\boxed{
s_A = U_{i_r,v_r}\circ\cdots\circ U_{i_1,v_1}(s_B).
}
\]

The laboratory demonstrates with the exact directions/values in the user's example:
- \(U_{1,1}(s)=s+1\)
- \(U_{4,1}(s)=2s\)
- \(U_{5,1}(s)=s+1\).

Starting at \(s_B=0\), the ordered sequence \((1,4,5)\) produces \(0\mapsto1\mapsto2\mapsto3\), whereas the permutation \((4,1,5)\) produces \(0\mapsto0\mapsto1\mapsto2\).

Thus a *set* of touched addresses can correctly encode an additive difference but cannot always encode a **path through a state-changing field**. The exact finite action-decoder checks the basis version, actual starting position and terminal commitment. For a geometric/category-theoretic generalization, this is the location where coordinate charts, connection/parallel transport, composition and holonomy matter. The test does not pretend to have constructed a physical gauge connection.

## 4. Proofs reduce message cost only under justified source constraints

Suppose the shared mathematical language already includes a **verified fact about the admissible update family**: on the declared support \(I=(1,4,5)\), all valid deltas satisfy

\[
v_1=v_4=v_5.
\]

Then A need only send the **one independent value** \(v_1=1\), and B reconstructs \((1,1,1)\) using that law. This precisely implements the maintainer's proof-as-question-graph-rewiring: the relation eliminates two independent value obligations.

Our exact finite model represents the law by a named, versioned family of admissible candidate deltas. The verifier exhaustively checks each candidate; encoders reject a delta with coefficients (1,1,2). The decoder refuses to expand one value without a matching previously verified rule and rechecks that the reconstructed delta belongs to the declared source class.

**Caution:** validating a law over a *declared candidate family* does not prove that all possible real-world source updates belong to that family. Nor does shortening three value tokens to one prove a minimal total binary communication cost, since the support indices, basis, proof identification and decoder count toward the complete protocol.

Within a shared candidate universe in which the support is **exactly three of six possible directions** with all values known to equal 1, there are \({6\choose3}=20\) possible supports. An exact, one-shot fixed-length binary message identifying every support requires \(\lceil\log_2 20\rceil=5\) bits. A 5-bit enumerative index attains that *restricted* information-theoretic bound. Different priors or source-specific side information yield different costs.

## 5. A genuine mathematical *boundary encoding*, not gravitational holography

The shared integer basis naturally admits an analytic Fourier realization. Encode the user's sparse delta in a polynomial

\[
\boxed{F_\Delta(z)=z+z^4+z^5.}
\]

Evaluate it on the unit circle \(z=e^{it}\), giving an exact angular/boundary signal
\[
F_\Delta(e^{it})=e^{it}+e^{4it}+e^{5it}.
\]

**Six-mode reconstruction theorem (CLASSICAL).** If a source is promised to be a polynomial of degree at most 5 with rational coefficients, values at the six distinct sixth roots of unity \(\zeta^j\), \(j=0,\ldots,5\), uniquely determine all six coefficients:
\[
\boxed{
a_n=\frac16\sum_{j=0}^5F(\zeta^j)\zeta^{-jn},
\qquad n=0,\ldots,5,\quad\zeta=e^{2\pi i/6}.
}
\]
**Proof:** Substitute \(F(\zeta^j)=\sum_{k=0}^5 a_k\zeta^{jk}\), exchange sums and use \(\sum_{j=0}^5\zeta^{j(k-n)}=6\) if \(k=n\bmod6\), zero otherwise. Since 0≤k,n≤5, no frequency aliases remain.

The standalone standard-library exact module implements \(\mathbb Q(\zeta_6)\) as pairs \(a+b\zeta_6\) with \(\zeta_6^2=\zeta_6-1\), independently computes forward evaluations and inverse Fourier reconstruction, and exhaustively tests rational coefficient cases.

**Fatal mutation: remove the source-class bound.** The nonzero polynomial \(z^6-1\) vanishes at **all six** sample points. The boundary observations of \(F=0\) and \(G=z^6-1\) are identical, though the functions differ. Similarly \(z^7\) and \(z\) give identical samples. The finite boundary representation is therefore not faithful for arbitrary higher-degree source families.

This cleanly distinguishes **information represented in boundary data** from **information uniquely recoverable with an assumed source class**. Six boundary values contain exactly enough for a known six-mode function; they do not describe an arbitrary infinite-mode bulk.

### Stability and finite-precision obstruction

Even if a full exact inverse exists, a finite-precision measurement of a boundary/interior analytic code need not support robust reconstruction. For \(0<r\le1\), sample at \(r\zeta^j\). Mode \(n\) appears multiplied by \(r^n\), so exact inversion divides by \(r^n\). For \(r=1/2\), mode five contributes only \(1/32\) per unit coefficient. The implemented finite-precision apparatus rounds rational coordinates in the cyclotomic field to increments \(1/8\); the isolated fifth-mode polynomial \(z^5\) then has **the same rounded samples as zero** at all six points, although exact samples distinguish them.

This is a precise toy *conditioning/precision horizon*: exact source uniqueness is not sufficient for fixed-precision observational distinguishability. The rounding convention is a toy finite measurement channel, not an actual black-hole entropy calculation.

### Relation to Susskind's holography

Susskind's original *The World as a Hologram* (https://arxiv.org/abs/hep-th/9409089) and Bousso's review (https://doi.org/10.1103/RevModPhys.74.825) concern the gravitational relationship between entropy/information and surfaces. Actual modern AdS/CFT bulk reconstruction has a much stronger **quantum-error-correcting-code** structure, with recoverability conditioned on code subspaces and boundary regions (Almheiri–Dong–Harlow, https://arxiv.org/abs/1411.7041; Harlow, https://arxiv.org/abs/1607.03901). The exact sixth-root Fourier code is a mathematical analogy to encoding/reconstruction but contains **no gravitational metric, Bekenstein–Hawking area law, entanglement wedge, operator-algebra QEC or quantum entropy bound**. The project should not promote a gravity hypothesis on the basis of this finite code.

## 6. The RH distinction: critical-line *values* versus zeros alone

The Riemann Hypothesis is still unsolved (Clay Mathematics Institute, https://www.claymath.org/millennium/Riemann-Hypothesis/). The critical line \(\Re(s)=1/2\) is an **axis of the completed function's symmetry**, not a literal event horizon or analytic-domain boundary. The completed \(\xi(s)\) is entire; the nontrivial zeros are known to lie in the critical strip, and RH conjectures that *all* lie on the critical line.

There is a particularly sharp *positive* reconstruction theorem here:

**Identity theorem:** an entire function's **exact full values** on any line segment (or other set with an accumulation point inside its domain) determine the entire function uniquely. Thus \(\xi(1/2+it)\) as a complete exact function of continuous \(t\) is, abstractly, sufficient to specify \(\xi\) globally. This is about mathematical uniqueness, **not** finite sampling, stable numerical continuation, an effective proof of RH, or what a finite observer can measure. Source: standard holomorphic identity theorem; https://people.maths.ox.ac.uk/hewitt/publications/C5_6_notes.pdf.

**But critical-line *zero locations alone* are not the same as the full function values.** Build the following explicit zero-only countermodel preserving two relevant symmetries. Let \(w=s-\frac12\) and
\[
F(s)=1+w^2,\qquad
G(s)=(1+w^2)(1-16w^2).
\]
Both are entire functions, real on the real \(s\)-axis and symmetric under \(s\mapsto1-s\). Both have exactly the same critical-line zeros \(s=1/2\pm i\), but \(G\) additionally has off-line zeros \(s=1/4,3/4\). Indeed, on \(w=it\), the added factor is \(1+16t^2>0\).

**This is NOT a counterexample to RH.** Neither function is the actual completed zeta function; they do not satisfy its Euler-product, completion, prescribed functional growth and arithmetic source constraints. It demonstrates only that **an arbitrary symmetric entire function's on-line zero locations do not, by themselves, certify the absence of off-line zeros**. The lab verifies the indicated algebraic zeros exactly using rational Gaussian pairs, and explicitly refuses to infer anything about true \(\xi\).

This addresses the maintainer's "data seems visible on a horizon" intuition rigorously: one can have a representation whose complete values mathematically determine a global object, yet a highly impoverished projection (only the observed zeros, or finite noisy evaluations) is insufficient for reconstruction.

### What a load-bearing holographic RH mechanism would require

A serious mathematical candidate would need:
1. A **source-derived** arithmetic “bulk” class grounded in the actual Euler/prime-power, half-density, completed Gamma/Archimedean and test-function domains; no zero location read into the construction as an input.
2. A precisely defined, checkable **encoding map** from that class to a boundary or observer-data algebra, with semantically meaningful finite probes and a proof of its structural invariants.
3. A theorem showing the relevant target (the full completed Weil positivity criterion, or an equivalent RH property) **factors through** those accessible observations and has a valid *certificate*; uniqueness of analytic continuation alone is not sufficient.
4. **Quantified injectivity/continuity/stability** or explicit recoverability bounds on the chosen source/proof code subspace, with correct entropy/information accounting if a holographic bound is asserted.
5. Real negative controls with non-Euler/mutated sources and proof that a purported RH inference survives domain, completion and provenance checks.

The degree-limited Fourier demonstration is a useful calibration: it proves an exact decoder when the code subspace makes reconstruction legal, loses information when the source class grows, and loses robust information under finite resolution even when an exact inverse exists. It does not establish any of the missing RH-specific maps.

## 7. Ledger, hostile controls and next decisive experiments

Proposed ledger entries O109–O117:

- **O109 PROVED LOCAL / TESTED MODEL:** correct basis-indexed finite-support relative packet reconstructs receiver-anchored state for a declared additive free-module basis.
- **O110 PROVED LOCAL / TESTED MODEL:** state-dependent frame actions require an ordered path; same direction/value multiset can produce different endpoints.
- **O111 PROVED LOCAL / TESTED MODEL:** independently verified source-class equal-coefficient law compresses three value obligations to one without guessing an unknown outcome or implying global bit optimality.
- **O112 CLASSICAL / TESTED MODEL:** exact degree≤5 polynomial is recovered from six sixth-root boundary values by a rational inverse DFT.
- **O113 PROVED LOCAL:** unrestricted higher polynomial modes alias the same finite boundary samples (e.g. \(z^6-1\)).
- **O114 PROVED LOCAL / TESTED MODEL:** exact radial decoding does not ensure decoding after fixed finite-precision quantization; high modes can be rendered indistinguishable.
- **O115 CLASSICAL + explicit counterexample:** full exact line values uniquely determine an entire function, but line-zero locations alone fail to determine arbitrary symmetric entire functions or their off-line zeros.
- **O116 CLASSICAL counting / FINITE MODEL:** 20 possible three-of-six supports require five fixed binary bits for universal source-exact support identification, given the common basis and fixed support-cardinality restriction.
- **O117 UNVERIFIED:** the proposed arithmetic/RH holographic correspondence, physical entropy bound or proof-coherence horizon follows from this basis/Fourier toy.

**Positive controls:** exact \((1,4,5),(1,1,1)\) update; two observers with different starting states cannot reuse the same anchored packet; changed basis fails; honest certified value sharing; exact arithmetic Fourier inversion; known code subspace and perfect measurement.

**Negative controls:** forged proof family with unequal deltas; noncommuting path permutation; unbounded high-mode root alias; finite-precision blindness; entire symmetric functions sharing all critical-line zero locations yet differing elsewhere.

**Highest-value next round:** jointly optimize **basis-conditioned path complexity, proof-induced question graph contraction and boundary reconstruction capability**. Define the minimal stable continuation-preserving delta, including the cost of the shared basis/verifier. Then test a nontrivial geometry where the local basis itself changes with the carrier and has a connection/holonomy; after that, try a source-derived analytic/arithmetic operator family with strict RH firewall.

**Verdict:** the maintainer's tuple is already an exact and effective mathematical design pattern. The holographic extension is an interesting, source- and precision-conditioned reconstruction program, not a proved physical/RH relation. The central lesson is to distinguish the mere existence of an encoding, its uniqueness on a chosen class, its stable probe-level recoverability, and its certificate authority.
