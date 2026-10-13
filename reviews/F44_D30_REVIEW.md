# F44 — Independent D30 crucible review

**Verdict: SURVIVES / CLASSICAL, with minor manuscript repairs.** The complete
fixed-word law hypothesis is sufficient for the stated public-policy no-go.
No mathematical counterexample to that scoped theorem was found. The local
quantum-history argument also survives its autonomous, common Q-local
instrument hypothesis. This is a paper proof review plus **TESTED MODEL**
receipts, not LEAN-KERNEL PROVED and not physical attestation.

Reviewed author commit: `acc1942011cb8fbc7fdcd3e2e48d169af3d74bfc`.
The manuscript's Git blob is `d2043e8a0662389afc280e6e410afc19d8fca284`;
the live file matched that committed object. Reviewer D30 previously derived
the separate PDE dossier, did not derive F44, and read neither F44's probe nor
its receipt. The new probe imports no project modules. It checks the published
witness inputs independently; that is implementation independence, not blind
hypothesis discovery or independent physical evidence.

## Core proof audit

For a deterministic policy and a fixed transcript containing actions and
outcomes, policy consistency is a source-independent indicator. Multiplying
that indicator by the fixed-word law gives its probability. Therefore equality
of every fixed-word law gives equality of every adaptive transcript cylinder.
For randomized policies, condition on a source-independent tape and integrate.
This also covers persistent private random memory. If the postprocessor uses
that tape, retain it in the joint sample space before pushing forward; treating
its conditional law given history as automatically independent would be an
unnecessary shortcut. The manuscript already supplies the tape argument.

Finite alphabets give the usual product sigma algebra. Equal cylinder
probabilities determine equal infinite-path measures. Pad a stopped process
with a cemetery symbol, or use the disjoint finite/infinite transcript space;
any common measurable stopping/output map then has equal pushforward laws.
This includes the divergence event. No finite censoring check certifies actual
divergence. The independent probe explicitly labels its depth-three boundary
`censored`, not `diverged`.

The original-target criterion is also correct: on a nonempty realized terminal
fiber, a universally sound answer exists exactly when all compatible original
targets agree. Empty fibers require rejecting inconsistent evidence. A
singleton *current* carrier is insufficient after erasure. The probe preserves
two original targets in one reset carrier. Law-signature factorization is
distributional identifiability; it neither supplies an accessible finite
experiment nor makes overlapping outcome supports disjoint.

## Smallest hostile breaks of weakened premises

**Temporal-memory omission.** A fair hidden bit that is retained forever and a
fair bit refreshed after every read have identical one-time marginals at every
stage. Their two-read laws differ: `00` has probabilities `1/2` and `1/4`.
Thus replacing complete word laws by marginal laws breaks the theorem. A
model that uses a trivial carrier and a fresh fair kernel for both has silently
discarded the first process's memory. The source/carrier state must contain
all memory needed for the declared causal kernels, including instrument and
environment memory; source-dependent durations or action availability are
outcomes if publicly observable.

**Counterfactual/order shortcut.** Two source classes initialize a two-bit
carrier uniformly on even or odd parity. Reading either bit erases the other.
The first outcome is fair under both classes and prepares the same carrier
given its action/outcome. Every subsequent common action has the same law.
This proves equality for all word lengths, while a hypothetical simultaneous
read of both *original* bits would distinguish parity perfectly. Combining
answers from incompatible destructive histories invents an instrument. The
independent probe checks all 31 words through length four; the first-step
argument, rather than that finite enumeration, establishes the universal claim.

**Nonlocal evolution.** Equal reduced Q states guarantee local history equality
only when common instruments act autonomously on Q. Hidden Q–E interactions,
source-dependent local devices, or source-correlated auxiliary memory violate
that premise. In the independently reconstructed CNOT permutation, subsequent
Q-local X-plus probabilities are `1` for Bell and `1/2` for the mixture. The
manuscript correctly retains this hostile control. Autonomous unobserved
trace-preserving E dynamics need not be identity, but it must not couple back
to Q or supply a public outcome; the manuscript's identity-E premise is a
sufficient restriction, not a necessary one.

## Quantum certification audit

Independent rational matrices reproduce both `I/2` marginals and joint
XX-plus probabilities `1,1/2`, hence total variation `1/2`. The decisive
support certificate is stronger than an eigenvalue diagnostic:

\[
\rho_M-\tfrac12\rho_B
=\tfrac14(1,0,0,-1)(1,0,0,-1)^T\succeq0.
\]

For every positive effect E, its mixture probability is at least half its Bell
probability. Thus no conclusive Bell-identifying outcome can exclude the
mixture, and no single-copy procedure certifies the correct target with
probability one on both sources. This does **not** forbid one-sided zero-error
certification: XX-minus has Bell probability zero and mixture probability
`1/2`, so that outcome certifies the mixture. XX-plus remains ambiguous.
Requested wording repair: qualify “single-copy zero-error identification is
impossible” as “complete single-copy zero-error identification of both states
is impossible,” and explicitly retain the one-sided minus certificate.

The finite classical carrier C in section 3 is not literally the continuum of
density matrices on a finite-dimensional quantum register. Add one sentence
that the CP-history argument is a separate finite-dimensional quantum model;
its resulting transcript laws satisfy the same law-level policy proof. This
repairs the type boundary without changing the result.
If C is later generalized to a non-atomic classical carrier, define compatible
sources by `Pr_s(h)>0`, rather than requiring positive point probabilities
`Pr_s(h,c)>0`; the latter can be zero for every c. This is a future-extension
guard, not a defect of the manuscript's explicitly finite classical C.

## Exact typesetting repairs

At the reviewed commit, replace these three fragments:

1. Line 21: `(T$s$\ne T(t))` with `$T(s)\ne T(t)$`.
2. Line 23: `(D_A$s$=(L_s(a^n,\cdot))_{n,a^n})` with
   `$D_A(s)=(L_s(a^n,\cdot))_{n,a^n}$`.
3. Line 44, inside the display: `\bigl|\{T$s$:(s,c)\in B(h)\}\bigr|=1.`
   with `\bigl|\{T(s):(s,c)\in B(h)\}\bigr|=1.`

No edits to the author manuscript were made.

## Sources, receipt, and remaining step

[Watrous's primary text](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
Corollary 3.40 and equation 3.241, was checked directly and supports contraction
under positive trace-preserving maps. The author's Rothenberg PDF URL returned
a retrieval error; that citation remains unverified here, with no allegation
that it is incorrect. Neither citation is needed for the elementary equality
and explicit matrix calculations above.

The independent probe command is
`timeout 20s python reviews/F44_D30_probe.py > reviews/F44_D30_receipt.json`;
exit **0**, below the cap. It uses exact fractions, four rational CP
instruments, persistent-tape adaptive stopping, CNOT, XX support fibers,
the PSD factor, memory and destructive-order controls, and carrier reset.
Its finite checks do not promote universal claims.

The smallest remaining step is author/principal application of the three math
repairs and two wording/type clarifications. Acceptance of the scoped paper
arguments is supported; kernel formalization, empirical source correctness,
and acquisition of a genuinely new physical instrument remain separate.
