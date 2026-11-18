# Endpoint coercivity: one source, one rational endpoint, all backward probes

**2026-11-16 research continuation of draft PR #657.**
**Verdict:** the source-norm equivalence survives audit; this round proves a
failure-class geometry theorem, an exact tail calibration, and a near-zero-seed
obstruction. It certifies a substantially larger finite interval. It does **not**
prove an eventual positive lower bound for the original source. R0 and pi
base-16 normality remain **OPEN**.

## 1. Origin, recovered state and preservation

Leah's requested target, retained verbatim:

> One original source. One finite rational endpoint for each shell. A family of backward computational probes. A precise distance from the zero-phase reference.
> Prove that this norm cannot collapse to zero along arbitrarily late shells, and R0 follows.

The live recovery found main at
`81be6b897ae980b801a3b9de9e22ef81e8360bfb` (Main XXVI) and draft #657 at
`1f04b869182ad68deb764637034d72b19352ca48`. The latter descends from the former.
All 24 existing PR files were recovered from that exact committed head; the
[input inventory](ENDPOINT_RECOVERY_MANIFEST.json) records Git blob hashes,
SHA-256 hashes and byte counts. This is a source inventory, not an independent
verification of every prior mathematical claim.

The [hole contract](ENDPOINT_COERCIVITY_HOLE_CONTRACT.md) was written before
the mathematical assault. Three delegated bearings separately constructed,
attacked and translated the problem; the parent independently checked proofs
and synthesized the results. Their later cross-audits are disclosed. These are
same-model research bearings with shared source premises, not external referees.

The prior chain is preserved and linked, including:

| Earlier idea | Committed mathematical record |
|---|---|
| Defects of incompatible windows can expose a hidden carrier | [Defect-window tomography](README.md) |
| Contextual zero, third observer and compensating boundary | [Typed zero and observer ledger](CONTEXTUAL_ZERO_THIRD_OBSERVER.md) |
| A -> B -> C analytic information transport | [Germs, jets and differential transport](TRANSPORTED_GERMS_AND_JETS.md) |
| Gamma dilation and a causal analytic seed | [Gamma source/window analysis](GAMMA_DILATION_ANALYTIC_SEED.md) |
| A Gamma instrument that retains signed phase | [Adaptive Gamma microscope](ADAPTIVE_GAMMA_ICE_CLIMB.md) |
| Hidden distinctions inside coarse observer fibers | [Source-shadow interferometry](SOURCE_SHADOW_INTERFEROMETRY.md) |
| Relative motion and asymptotic subjective rest | [Moving-frame construction](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md) |
| First-order noise and higher-order source coupling | [Movable observation boundary](MOVABLE_BOUNDARY_ORDER_LIFT.md) |
| Infinite forms, rational periodic shadows and the endpoint norm | [Virtual-field form metric](VIRTUAL_FIELD_FORM_METRIC.md) |

Each record retains its own theorem/finite/conjectural boundaries. This round
also corrects the VFM introduction's claim numbering to match its body.

## 2. The exact frontier and the work that was not counted twice

Keep the original source, without a seed or forcing change:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
\]

For `x=pi/16`, the source identity is `U_n+T_n=16^n x`, where
`0<T_n<r(n+1)/15`. Define

\[
R_B=\frac1B\sum_{k=1}^B\|U_{2B}/16^k\|_{\mathbb T}^2,
\quad E_B(x)=\frac1B\sum_{n=B}^{2B-1}\|16^nx\|_{\mathbb T}^2,
\quad A_B(x)=1-\Re W_B(x).
\]

The inherited bridge is valid:

\[
8R_B-\rho_B\le A_B(x)\le2\pi^2R_B+\rho_B,
\qquad \rho_B=\frac{8r(2B+1)}{225B}.
\]

Therefore `R0 iff liminf R_B>0`. This remains an equivalence, not a new
statistical lower bound. A direct additional comparison is

\[
|R_B-E_B(x)|<\frac{r(2B+1)}{225B}.
\tag{EC1}
\]

The existing [RI-02 inverse dictionary](../../2026-11-13/leah_gamma_twist/R0_INVERSE.md)
and [LGT-R0 current comparison](../../2026-11-12/leah_gamma_twist/INVERSE_R0.md)
already contain the nearest-integer carry equivalence and the bulk constants
225 and 289. This round reuses those ideas but does not count their rediscovery.

**Cave map.** The object is the literal zero-selected rational endpoint; the
observable is its shell torus norm; the mechanism is exact transport plus
finite rational certification; the success predicate is an eventual constant
floor. The residual is possible concentration of the selected numerator in
the sparse family of cold forms. More invertible Gamma windows cannot exclude
that family, because they only recode the same selected phase.

## 3. A proved theorem about exactly which forms could defeat R0

For a fixed real `lambda>1`, put `M_B=floor(lambda B)` and `L_B=M_B-B`;
use B sufficiently large that `L_B>=1`.
Consider the exceptional set

\[
\mathcal E_\lambda=
\left\{y\in[0,1]:
\liminf_B\frac1{L_B}\sum_{n=B}^{M_B-1}\|16^ny\|_{\mathbb T}^2=0\right\}.
\]

The [complete proof](COLD_SHELL_EXCEPTIONAL_SET.md) establishes

\[
\boxed{\dim_H\mathcal E_\lambda=1/\lambda,\qquad
\mathcal E_\lambda\text{ is a dense }G_\delta.}
\tag{EC2}
\]

In particular the exact R0 failure set has Hausdorff dimension **1/2**.
This concerns R0 itself, whereas the inherited 7/8 dimension concerns failure
of a stronger sufficient carry event. Neither result decides membership of
the particular endpoint pi/16.

The finite ingredient is constructive. Write
`q_n=floor(16^n y+1/2)`, `t_n=16^n y-q_n`, and
`a_n=q_(n+1)-16q_n=16t_n-t_(n+1)`. The integer branch alphabet is -8 through 8.
An energy at most epsilon permits at most
`J=min(L_B,floor(289 L_B epsilon+17/4))` nonzero branches. It is contained in a
union of at most

\[
\boxed{(16^B+1)\sum_{j=0}^{J}\binom{L_B}{j}16^j}
\tag{EC3}
\]

intervals of diameter `16^(-M_B)`. Choosing the rounded start integer and the
sparse branch word reconstructs the rounded terminal integer. A binomial
cover gives the upper dimension bound; a widely separated forced-zero-block
construction and an explicit measure estimate give the matching lower bound.

**Earned gain:** failure has an exact finite coding constraint and a sharp
aspect-ratio dimension law. **Unpaid debt:** prove that the source-selected
BBP numerator eventually escapes enough of those coded classes. Measure zero
and dimension 1/2 cannot supply that one-point arithmetic exclusion.

## 4. The norm has a source-tail baseline that must be paid

For any seed s, write beta=x+s and define `R_B(s)` from `U_(2B)(s)`.
The [two-sided calibration](TERMINAL_TAIL_BASELINE.md) proves

\[
\boxed{|\sqrt{R_B(s)}-\sqrt{E_B(\beta)}|\le h_B,
\qquad h_B^2=\frac{T_{2B}^2(1-16^{-2B})}{255B}.}
\tag{EC4}
\]

The coherent wrong seed `s=-x` makes every completed phase exactly zero,
yet its raw norm is exactly `h_B^2`. Since `T_m=1/(64m^2)+O(m^-3)`,

\[
\boxed{R_B(-x)\sim\frac1{16711680\,B^5}.}
\tag{EC5}
\]

Thus a positive raw norm, even a polynomial floor, can be supplied entirely
by the unfinished tail. The wrong-seed control is generally irrational; it is
not mislabelled as an authentic rational BBP endpoint.

A useful, genuinely weaker next arithmetic target is the **pointwise eventual**
inequality

\[
\boxed{R_B(0)\ge\frac1{16711680\,B^5}.}
\tag{EC6 — OPEN FOR THE ORIGINAL SOURCE}
\]

The exact subleading bound `T_(2B)<1/((16B+1)(16B+2))` makes this enough for

\[
E_B(x)>\frac1{679173120\,B^7},\qquad v_{16}(x)\le1.
\tag{EC7 — PROVED CONDITIONAL}
\]

Here `v_16(y)=limsup_m[-log||16^m y||/(m log16)]`, matching the existing
restricted-exponent convention. The conclusion forbids exponentially cold
dyadic shells, but still does not imply R0. The square-marker endpoint
`sum_(j>=1)16^(-j^2)` satisfies the critical floor in the same-tail changed-seed
model while its shell energy tends to zero. It proves that EC6 is weaker than
R0, rather than a renamed equivalent target.

The inequality `liminf B^5 R_B>=1/16711680` is **not** sufficient: the coherent
locked control attains equality in that limit. The eventual pointwise
inequality in EC6 uses more information. No bound on `v_16(pi)` is promoted
because EC6 for the original zero seed remains unproved.

## 5. A seed perturbation tending to zero erases a chosen winding block

Write `U_(2B)(0)=C+v`, `0<=v<1`, set `D=C mod16^B`, and choose

\[
s_B=-\frac{D+16^B}{16^{2B}}.
\]

Then `16^-B <= |s_B| < 2*16^-B`, and the [exact erasure theorem](TERMINAL_WINDING_ERASURE.md)
gives

\[
\boxed{R_B(s_B)=\frac{v^2(1-16^{-2B})}{255B}<\frac1{255B}.}
\tag{EC8}
\]

This preserves the entire forcing, every odd-primary component at every
clock, and the terminal fractional value. It rejoins the authentic circle
orbit exactly at clock 2B. It changes the seed and integer winding. A finer
dyadic correction reduces the raw norm below `16^(-2L)/(255B)` while preserving
all odd-primary components, with the completed tail still explicitly paid.

For each fixed perturbation the eventual orbit statistics are identical to
the original. The moving diagonal can nevertheless collapse. Both ordinary
iterated liminfs equal the authentic unknown liminf; an unconditional
noncommutation claim would be false. The manuscript states the valid
infimum/liminf quantifiers separately.

**Earned exclusion:** forcing, odd-prime data and approximate seed agreement
cannot support a lower bound uniform over all nearby seeds. The exact
zero-selected winding must participate in the missing estimate. This is a
sharpened specialization of SUCC's earlier dyadic-seed obstruction, not a
counterexample to the original source.

## 6. One endpoint certifies every integer shell in a finite range

The preregistered finite target was `A_B>2/5` for all integers
`16<=B<=4096`. Only the earlier shells 16,32,64,128,256 had supplied VFM's
displayed data; this run includes 3,840 additional integer shells beyond
that previously displayed VFM range.

Take `M=4096`, `d=6`, `Q=16^d` and the exact source endpoint `U_N` with
`N=2M+d=8198`. Let `C=floor(U_N)`. At clock `n<2M`, define

\[
a_n=\left\lfloor C/16^{2M-n}\right\rfloor\bmod Q.
\]

The true phase has a real lift inside `[a_n/Q,(a_n+2)/Q]` modulo an integer.
Indeed `U_N=C+v` with `0<=v<1`, and `0<T_N<1`; the unknown endpoint remainder
and tail together cost less than two units of the declared grid. The exact
lower distance numerator is

\[
\ell_n=\max(0,\min(a_n,Q-a_n-2)).
\]

Consequently, using integer prefix sums,

\[
E_B(x)\ge\frac{\sum_{n=B}^{2B-1}\ell_n^2}{BQ^2},
\quad A_B(x)\ge\frac{8\sum_{n=B}^{2B-1}\ell_n^2}{BQ^2},
\quad R_B\ge\frac{\sum\ell_n^2}{BQ^2}-\frac{r(2B+1)}{225B}.
\tag{EC9}
\]

The [certificate](ENDPOINT_SHELL_CERTIFICATES.json) stores every lower/upper
integer sum. Across **4,081** shells the smallest certified phase-loss bound is

\[
\boxed{\frac{247384815345917}{439804651110400}
\approx0.5624879471404642,\qquad B=25.}
\tag{EC10 — VERIFIED FINITE}
\]

Thus every shell in the tested interval has `A_B>1/2`. The stronger threshold
is a consequence of the executed exact certificate, not the preregistered
threshold and not an all-large-B statement.

The generator uses the combined rational four-pole expression and forward
recurrence. The [independent replay](ENDPOINT_SHELL_REPLAY.json) uses the literal
four fractions, reverse Horner summation, hexadecimal slicing and a moving-sum
recurrence. They match the endpoint hash and all 4,081 certificates exactly.
They share Python's Fraction library and the classical BBP/source-tail premises.
An additional audit checks all torus-interval extrema and deeper source bounds.

Reproduce from the repository root:

```sh
python scripts/endpoint_shell_certificate.py --output research/2026-11-16/defect_window_tomography/ENDPOINT_SHELL_CERTIFICATES.json
python scripts/verify_endpoint_shell_certificate.py research/2026-11-16/defect_window_tomography/ENDPOINT_SHELL_CERTIFICATES.json
python -m unittest discover -s tests -p 'test_endpoint_coercivity.py' -v
```

## 7. Reframe selection and dominance boundary

The candidates were evaluated after removing Gamma decoding as a proposed
source of statistical gain. Scores below are research-priority judgments on
0–5 scales, not truth probabilities. Columns are orthogonality, falsifiability,
intrinsic value, bridge potential, tractability and compression.

| Candidate | O/F/I/B/T/C | Verdict |
|---|---|---|
| Another backward carry-density equivalence | 1/4/2/2/5/2 | Already in RI-02; reuse without novelty claim |
| Prime-denominator-only coercivity | 3/5/3/3/3/4 | Nearby-seed winding erasure refutes the seed-blind inference |
| Sparse cold-form cover and exact exceptional geometry | 5/5/4/4/5/5 | Chosen proof product; EC2–3 established |
| Source-selected norm above the coherent tail threshold | 4/5/4/5/2/5 | Chosen next arithmetic rung; EC6 remains OPEN |
| Longer finite scans | 1/5/2/2/5/2 | Executed once with a fresh range and independent implementation |

This frame improves the old one for classifying collapse and calibrating tiny
energies: it identifies a sparse-form cover, a sharp dimension law, an exact
tail floor and a stronger source-authentication obstruction. It does not
dominate by supplying the missing selected arithmetic bound, because no such
bound was obtained.

Primary literature was checked against the actual claims. Lagarias's
[perturbed-radix analysis](https://arxiv.org/html/math/0101055v2) already separates
general tail transport from the unproved special-source normality hypothesis.
Chen's [moving-digit-mean paper](https://arxiv.org/abs/1809.08000) is relevant
prior art for dimension spectra; no exact theorem transfer or global novelty
claim is made. The [historical Zeilberger–Zudilin result](https://arxiv.org/abs/1912.06345v2)
is not asserted to be the latest irrationality record and is not needed by
the new self-contained proofs.

## 8. Claim ledger and exact remaining cut

| Claim | Status | Boundary |
|---|---|---|
| VFM source-norm/R0 equivalence | PROVED PAPER, re-audited | Equivalent reformulation; no new saving |
| EC2–3 cold-set dimension and finite sparse cover | PROVED PAPER | All real endpoints; no pi membership verdict |
| EC4–5 norm calibration and quintic coherent baseline | PROVED PAPER | Wrong-seed baseline is a control, not the source |
| EC6 implies EC7 | PROVED CONDITIONAL | EC6 for the original source remains OPEN |
| Square-marker strict separation from R0 | PROVED PAPER | Changed-seed control proves logical weakness only |
| EC8 near-zero winding erasure | PROVED PAPER | Refutes seed-blind uniform coercivity |
| EC9–10 finite interval | VERIFIED FINITE | Exactly 16<=B<=4096 |
| liminf R_B(0)>0 | OPEN | Missing original-numerator/carry exclusion |
| All-mode Weyl cancellation and pi normality | OPEN | Further signed estimates required after R0 |

The next discriminating arithmetic task is to exclude the original rational
endpoint from the critical ball

\[
R_B<1/(16711680B^5)
\]

for every sufficiently late B, or prove another estimate with a documented
advantage over that threshold. A second genuinely weaker rung is divergence
of the number of nonzero balanced branches on every late shell; it would
exclude bounded-support cold forms but still allow sublinear support.
Neither intermediate follows from the dimension calculation or finite scan.

## 9. Self-contained execution handoff

> Recover the current SUCC main and draft #657 heads; read AGENTS.md, the
> source contract, this report and the three theorem manuscripts. Retain
> r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U_0=0 and U_n=16U_(n-1)+r(n).
> Attack the eventual pointwise inequality R_B >= 1/(16711680 B^5), with
> R_B=(1/B) sum_(k=1)^B ||U_(2B)/16^k||_T^2, as a strictly weaker rung below
> R0. Its proved consequence is v_16(pi)<=1; do not assert that consequence
> until the original-source premise is proved. Use the sparse balanced-branch
> cover to isolate the selected numerator/cofactor obstruction. Preserve
> exact source and integer winding. Nearby dyadic seeds preserve all odd
> primary components while erasing a shell, so a seed-blind prime argument
> must fail. The coherent tail alone contributes asymptotically
> 1/(16711680 B^5); a liminf inequality with equality is insufficient.
> Do not rediscover RI-02, replace time by random prime clocks, or regard
> invertible Gamma decoding as a saving. Return a complete proof, a calibrated
> counterexample to a narrower proposed mechanism, or a precise surviving
> arithmetic obligation. Commit only audited additive research with scoped
> claims on a non-main branch under the active owner's authorization.

See [validation receipts](ENDPOINT_COERCIVITY_VALIDATION.md) for actual command
outcomes and the distinction between paper proofs, exact finite checks and CI.
