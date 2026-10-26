# Next π handoff: the carry bridge is paid; selected cancellation is not

Read the [synthesis](../research/2026-10-26/SELECTED_BRANCH_SYNTHESIS.md),
[claim ledger](../docs/CLAIM_SUPPLEMENT_SELECTED_BRANCH.md), and
[validation receipt](../research/2026-10-26/SELECTED_BRANCH_VALIDATION.md)
before extending this work. Recheck actual heads and CI. This continuation
starts from #312 at `0c306a889f425418c29cbea3193205fb80c0575e`, branch
`research/selected-branch-cross-energy-2026-10-26`. Sibling #311 was
inspected at `a34c4484059e667202b97d5ab4102560987b1406`, not merged.
No main branch, historical archive, or original source was changed.

**Status.** π normality, an authentic $o(N)$ signed Weyl estimate, and an
improvement to the order of the best selected absolute-loss theorem remain
OPEN. The completed result is a source-derived quantitative comparison and
two strengthened obstructions, with finite kernel proofs and exact instruments.

## What is no longer an unpaid assumption

For the complete original forcing, a positive scaled spill
$s_k^{(a)}=\lfloor\{16aU_{k-1}\}+a r(k)\rfloor$ forces
$L_a(k)=\max(0,\lfloor\log_{16}(4(k-1)^2/a)\rfloor)$ zero carries.
The explicit packing budget $B(N,a)$ is independent of measured Fourier
values and is $o(N)$ whenever $a=o(N^2)$.

Consequently the original selected digit/remainder-bin energies and actual
literal-carry/arrival-bin energies differ by at most
$4[B(N,1)+B(N,M)]/N$ per character, and their total defects by at most
$32[B(N,1)+B(N,M)]/N$. At the preset
$M_N=\max(2,\lfloor\log_2N\rfloor)$ the errors are $O(1/\log N)$.

The next parity proposition is exactly

$$\sum_b\widetilde p_b(\Phi_b-1/2)^2=o(1),\qquad
\Phi_b=\frac49+\frac19\Pr(c_{n+1}\text{ odd}\mid
\lfloor M_N\{U_{n+1}\}\rfloor=b).$$

Multiplication by 324 is the actual carry-conditioned parity energy.
This is a narrowed obligation, **not** a proved estimate. Proving parity
alone would still leave the quarter-turn/opposite-pair and other branch
interactions. A source-blind marginal or independent packet law is inadmissible.

## A weaker signed object that must not be discarded

The native `source_signed_certificate` retains the bin amplitude vector and
its phases. With $\tau_b=(b+1/2)/M$, it evaluates

$$\widetilde C_{N,M}(h)=N^{-1}\sum_{n=1}^N
e\bigl(h(c_{n+1}+\tau_{\lfloor M\{U_{n+1}\}\rfloor})/16\bigr).$$

Its distance from the actual normalized Weyl sum is at most
$\pi|h|/(16M)+\pi|h|\sum_{n=1}^Nr(n+1)/(8N)$ for every $N,M$.
Thus an all-$N$ signed estimate for this actual object at the fixed schedule
would suffice. Taking conditional absolute squares first can destroy the
cross-bin cancellation that this route needs. A new theorem must bound the
sum; another change of notation is not a result.

## Controls future arguments must survive

1. At $M=8N^2$ every authentic bin label changes. The exact polynomial
   proves this for every $N$, and Lean checks its positivity. Do not extend
   the subquadratic discontinuous transport into the critical band by
   pretending the errors stay sparse. Continuous signed transport remains valid.
2. At $M\ge Q_N$, the actual odd-conductor source has $E(h)=1$ and
   $\Delta=15$. Exact-tail conditioning does not contract. Odd inverse
   uniqueness and its discontinuity are inherited from Seinfeld SS-05/06;
   the new quantitative resolution consequence is in this round.
3. For any fixed finite band, one changed real seed with the **same entire
   forcing**, endpoint irrationality exponent two and donor-level logarithmic
   absolute loss cancels that band while all fine conditional energies
   approach one. A higher mode remains biased. The seed is negative and
   nonzero; no unsupported irrationality claim about the seed is allowed.
4. A single-bin even/odd balance can still have quarter-turn energy $1/2$.
   The opposite-pair term cannot be inferred from Gaussian coefficient holonomy.
5. Moving bins and changing digit labels both cost records. A bound counting
   only the latter is false. The universal constants 4 and 32 are sharp.
6. The selected singleton and the Haar sixteen-point inverse fiber form a
   noncartesian source square. A signed missing-point indicator detects it.
   A common category or lambda syntax does not change that source map.

Forcing signs, zero initialization, integer lifts, prime labels and carry
history remain nonnegotiable for a π theorem. The spill theorem itself works
for every initial seed, so it cannot supply the missing selector mechanism.

## Reproduction and proof authority

Use the repository's ordinary Python environment. Focused checks:

```sh
python -m unittest tests.test_selected_branch_arithmetic tests.test_selected_branch_operator tests.test_selected_branch_analytic tests.test_selected_branch_transport
python scripts/selected_branch_probe.py --verify
python scripts/check_selected_branch_lean.py --output /tmp/selected-branch-lean-review --dependency-project /path/to/matching/formal/mathlib_bridge
```

The dependency cache must match the pinned Lean 4.14.0 and all manifest
revisions. The checker rejects mismatches, exports ten exact finite types,
checks standard axioms and tests four paired controls. It does not prove
the analytic or infinite statements. The committed receipt records the
actual local cache used; it is not a portable promise that this path exists.
Run all four AGENTS.md native checks on the final combined source before
delivery. Preserve successful and failed raw logs; do not repeatedly trigger
large hosted suites during experiments.

No new research starts by resetting the existing worktree or merging main.
Use an isolated child of the live continuation head. The dossier is a
source-authenticated PAPER-PROVED result with exact finite corroboration;
external mathematical review and the selected cancellation theorem remain
outstanding.
