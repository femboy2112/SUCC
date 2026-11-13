# Yang–Mills to SUCC: the dependency cut

Date: 2026-11-13. Base: Main XXV
`db9fb4b84672050efa79b13377f1e73364598a14`.

## Object and acceptance criteria

The user asked whether the newly reported OpenAI four-dimensional quantum
Yang–Mills result is real, whether SUCC can use it, and whether SUCC can reproduce
the proof. Success in this round means a pinned primary-source assessment,
an honestly scoped reproduction, and a proved interface showing exactly what a
transfer would require. It does not mean renaming an arithmetic model as QFT.

The external construction establishes existence in its stated class. Its
published assessment leaves the physical mass gap and infinite-volume uniqueness
open. The source audit records its precise domains and validation authority.

## H1: preserve a source-bound state through reconstruction

- **Statement.** If a unital star-homomorphism `Phi: A -> B` between unital
  C*-algebras preserves the declared normalized positive state, it induces an
  isometry of their GNS spaces onto the target cyclic subspace. Dynamics and
  spectral conclusions require a separate intertwining condition.
- **Truth state.** Classical reconstruction fact; paper proof reproduced in
  `TRANSFER_THEOREMS.md`. No instantiated Yang–Mills/BBP map is supplied.
- **Weak sufficient form.** Equality of all products `omega_A(a* b)` with their
  transported moments suffices for the Hilbert isometry. A complete algebra and
  its dynamics are needed for the full field-theoretic interpretation.
- **Edge closed.** Authenticated correlations -> faithful observer-space
  reconstruction. It does not close arithmetic statistical decay.
- **Novelty tax.** An explicit proof contract and application of classical GNS,
  not a new existence proof or priority claim.
- **Cheapest falsifier.** A wrong state or nonintertwining Hamiltonian. The
  existing arithmetic doubled Liouvillian supplies the latter control.
- **Boundary.** Finite exact moment checks do not prove all-moment agreement.

## H2: a source-specific common expansion with a controlled stability margin

**Sharper form retained after the algebraic audit:** contraction of every
direction is unnecessary. For target readout `L`, it suffices to construct
`B_r` such that `L = B_r (I-A_r)` and `||B_r|| epsilon_r -> 0`. The exact
finite-dimensional factorization exists iff `ker(I-A_r)` is invisible to `L`.
Thus target-invisible coherent directions can remain. The contraction version
below is a convenient sufficient certificate, not a necessary definition of
normality, gauge equivalence, or a successful comparison.

Let `K` be a compact class of candidate limiting states for one authenticated
source. On a fixed finite family of target observables, let `x(s)` be the complex
vector read from state `s in K`. Seek, for every sufficiently small scale `r`,

    x(s) = A_r x(s) + b_r + R_r(s),   for EVERY s in K,

where the **same** `A_r`, `b_r` and observable identification are chosen before
`s`. Let positive weights `w_i` satisfy

    sum_j |(A_r)_ij| w_j <= q_r w_i,       q_r < 1,
    |R_r(s)_i| <= epsilon_r w_i,           uniformly in s,
    epsilon_r / (1 - q_r) -> 0.

- **Proved conditional conclusion.** Every pair satisfies
  `||x(s)-x(t)||_w <= 2 epsilon_r/(1-q_r)`, hence all states have the same
  target-observable values. A measure-determining observable family upgrades
  this to equality of states; a separately identified reference state fixes
  which state it is.
- **Current arithmetic truth state.** The abstract implication is proved;
  construction of such an expansion for the zero-seeded BBP source is **OPEN**.
- **External leverage.** The inspected theorem `YMReview.OPE.phase_difference`
  subtracts two states using a common coefficient system. It supplies the
  comparison pattern, not the contraction hypothesis above.
- **Weakest sufficient form used here.** Target-reader factorization on a
  complete family relevant to the target, with `||B_r|| epsilon_r -> 0`.
  Contraction is one sufficient certificate. No uniform control of arbitrary
  moving-lag maxima is required.
- **Novelty tax.** The abstract estimate is classical stability algebra. An
  arithmetic expansion is not progress until its hypotheses are derived from
  the original forcing without assuming normality. A scalar identity merely
  restating the desired decay fails this test.
- **Known traps.** Shared coefficients alone allow distinct states. Small
  remainders with `q_r -> 1` can leave order-one differences. A finite observable
  family can miss non-Haar states. Separate existential source witnesses do not
  compose. Quantitative identification of a selected arithmetic state with a
  Wilson state is absent.
- **Cheapest falsifiers.** `A=I`, zero remainder, two distinct values; and
  `A_N=1-1/N`, `R_N=+/-1/(2N)`, states `+/-1/2`. Both are exact.
- **Fresh test region.** Unfitted rational matrices with unequal weights and
  changed signs, exact residual mutations, and large N in the closing-margin
  control. These calibrate the algebra, not an infinite arithmetic estimate.
- **Next lamp.** Derive an explicit carry-conditioned or block-scale operator
  for the authentic BBP source, identify its observable domain and boundary
  terms, and bound the residual divided by its stability margin. Test the
  source/seed assumptions on the coherent wrong seed before claiming decay.

## H3: reproduce an actual Wilson positivity slice

For SU(2), integrate one plaquette with the Wilson weight. Reduce its holonomy
to Haar measure, recover the exact Catalan trace moments, construct positive
even Taylor approximants and prove a uniform observable error bound. Keep
ordinary state positivity separate from Euclidean reflection positivity.

**Scope:** a genuine compact-group/Wilson finite-volume calculation and a
controlled one-variable limit. No four-dimensional ultraviolet renormalization,
infinite-volume extraction, all-field OS reconstruction or mass gap is claimed.
The proof and exact hostile controls live in `WILSON_REFLECTION_SLICE.md`.

## Publication boundary

The dossier is additive research on a separate branch. Original imported sources
and historical contracts remain byte-identical. Published upstream checking
results, locally executed integrity checks, exact Python probes, and paper proofs
carry separate labels. Full upstream Lean/Comparator replay is not claimed.
