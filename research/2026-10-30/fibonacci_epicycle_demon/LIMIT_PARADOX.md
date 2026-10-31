# SUCC — The degenerate observer at infinity: a noncommuting-limit crucible

**Status (2026-10-30):** mathematical results proved here about symbolic sequences, CONDITIONAL on the target sequence being base-16 normal. **π base-16 normality is not proved.** This file is an additive continuation of PR #397, with Main XVI as its original baseline. No edits to native BBP, U0=0, source provenance, archived contracts, or the signed selected recurrence.

## 1. The author's strongest paradox hypothesis

An observer continually preserves an internally coherent but wrong model of the hexadecimal digits by adding epicycles and exception rules. At every finite stage the updated theory explains every observed digit. Might the limit be a *single infinite*, internally coherent, **nonnormal** description of π that agrees with π at every finite observation? Might such a structure be inaccessible to an observer of the actual normal digits?

Answer: a **single** predicted infinite digit stream cannot be both exactly the target stream and nonnormal if the target is normal. The subtlety is the difference between (a) a different infinite model at each stage, (b) a single limiting infinite prediction, and (c) an internal latent representation plus a decoder. The first two are distinct quantifier orders; the third has a different observation map.

## 2. Limit-order counterexample — DISCLOSED, conditional

Let x=(x_1,x_2,...) be any base-b normal digit sequence, b>=2. Define a stage-N nonnormal prediction

\[
y^{(N)}=x_1x_2\cdots x_N0000\cdots.
\]

Every y^(N) is eventually zero and hence nonnormal, but y^(N) agrees with x through N. For each **fixed** digit index j, y^(N)_j=x_j for all N>=j; therefore y^(N)->x in the product / finite-prefix topology. The nonnormal sequences are not closed.

Let f_T(0;y) denote the proportion of digit zeros in its first T positions. Then

\[
\lim_{N\to\infty}\lim_{T\to\infty}f_T(0;y^{(N)})=1,\qquad
\lim_{T\to\infty}\lim_{N\to\infty}f_T(0;y^{(N)})=1/b.
\]

The nested limits do not commute. Normality is not continuous under digitwise convergence. The nonnormal *approximants* have a normal limit; there is no contradiction.

For every finite prefix w, an eventually-zero extension is nonnormal, while the extension obtained by appending any normal base-b digit sequence is normal. Neither class can be refuted by any **single finite prefix** when unrestricted.

A stage-N model's future predictions need not agree with the stage-(N+1) model's future predictions. Observed-prefix coherence is weaker than one globally compatible predictive history. Formal quantifier firewall:

\[
\forall N\;\exists y_N\in D:\, y_N[1\!:\!N]=x[1\!:\!N]
\quad\not\Rightarrow\quad
\exists y\in D\;\forall N:\, y[1\!:\!N]=x[1\!:\!N],
\]

where D is the family of nonnormal streams. The right side is false when x is normal.

## 3. A closed-class finite-horizon theorem — DISCLOSED, conditional

Use the compact full shift \(\Sigma^{\mathbb N}\), \(\Sigma=\{0,\dots,b-1\}\), with basic open cylinders [w] fixing a finite prefix. Let \(C\subseteq\Sigma^{\mathbb N}\) be a **closed** class of candidate model outputs. If \(x\notin C\), its complement is open, so some prefix cylinder [x_1...x_N] is disjoint from C. Hence **one finite N refutes every candidate in C as an exact complete-prefix predictor**.

In particular, any finite class of nonnormal deterministic predictions is closed, so if x is normal such a family has an eventual finite exclusion horizon. Conversely \(D=\{\text{all nonnormal streams}\}\) is dense (every cylinder contains an eventually-zero stream); it is not closed, and every cylinder intersects D. There is **no** finite universal exclusion horizon across the unrestricted D. All normal continuations are dense as well.

This is a clean operational boundary: the alleged "insurmountable" finite wall requires a controlled/closed model class, or a fixed probabilistic model with a calibrated evidence threshold. If the observer expands model capacity without bound, no horizon follows from normality alone.

## 4. Fixed nonnormal infinite models must differ on positive upper density — DISCLOSED, conditional

If x is base-b normal and y differs from x on \(D_N\) of the first N symbol positions, then for a fixed word w of length k, changing one symbol affects at most k starting positions. Denoting by \(C_w(z,N)\) the count of w starting at positions <=N,

\[
|C_w(x,N)-C_w(y,N)|\le k D_{N+k-1}.
\]

If D_N/N ->0, every finite-word frequency in y has the same limit as in x; thus y is normal. **Contrapositive:**

\[
y\text{ nonnormal},\ x\text{ normal}\quad\Rightarrow\quad
\limsup_{N\to\infty}D_N/N>0.
\]

More quantitatively, if \(\delta_w=\limsup_N |C_w(y,N)/N-b^{-k}|>0\), then \(\limsup_N D_N/N\ge \delta_w/k\). This does NOT imply a uniform lower bound on *every* long window, and the positive constant may depend on the proposed model. For an eventually-all-zero y, the exact mismatch density tends to \(1-1/b\).

A model can retain an entirely different internal representation or selection map while its decoded external output is normal. The conclusion applies to literal predictions in the **same base, index clock, and full observation channel**; not to a selected subsequence (e.g. only indices whose digits equal zero), coordinate reset, or a latent label that is never decoded into predicted digits.

## 5. The surprising short-code no-go for naive epicycle complexity

A proof that model-repair **description length** must grow linearly cannot follow from normality alone. π is a computable constant (this does not presuppose its normality). A uniform algorithm can compute its first N hexadecimal digits. For each integer N, the program:

    generate the first N hexadecimal digits of pi; then emit zeros forever

describes an eventually-zero, nonnormal prediction y^(N) with fixed interpreter/source routine plus a self-delimiting encoding of N, using O(log N) bits of stage-specific program description. Each model retrospectively fits its own N observations. The model class changes with N and uses the genuine π algorithm as a subroutine, so this does NOT validate a blind epicycle observer's predictive ability.

If instead this observer commits **before** the next outcome to "the next digit is zero" after every revision, then on an assumed normal π its long-run one-step success rate is only 1/16, with 15/16 errors. For a fixed full-support biased probabilistic predictor, the correct prequential log-evidence penalty is the KL theorem FEO-05 in RESEARCH.md. In-sample fit and out-of-sample predictive performance MUST NOT be conflated.

## 6. Relating the result to SUCC's finite/infinite boundary

There are two independent limiting coordinates: N = observer-revision depth; T = digit-frequency evaluation horizon. The product-topology limit fixes each finite observation, while Cesàro normality looks at asymptotic frequencies over growing horizons. Without a *uniform-in-N* tail-frequency or prediction-risk bound, swapping their order is invalid.

The SUCC source-relative/literal-carry program adds an additional firewall: even if an auxiliary positive posterior family has a mathematically perfect Fibonacci/Gamma clock, the actual zero-seeded four-pole orbit's selected digit statistics do not follow from it. Same-forcing coherent seed s*=-π/16 refutes any source-only normality implication.

One valid route toward π normality would be a new **selected, original-source, seed-zero-sensitive** theorem ruling out successful finite-state gambling on π's base-16 digit stream. By Schnorr–Stimm this is normality-equivalent, so simply restating it as a criterion is not a proof. A genuinely new all-horizon source-to-digit estimate or occupancy certificate would be required; contrast with normal Stoneham controls and the coherent counterseed.

## 7. Verdicts and discriminating experiments

- **DISCLOSED, conditional:** limit-order counterexample; topology/closed-class finite horizon; density-zero edit preservation and positive-upper-density mismatch.
- **REFUTED:** "every finite correct-looking nonnormal theory forces one globally correct nonnormal limit"; "all nonnormal candidate theories share a finite rejection horizon"; "linear repair-code growth follows from normality"; "normality implies computational incompressibility or unpredictable digits".
- **CONJECTURED / optional operational model:** epicycle cost ledger that includes exceptions, selection metadata, preprocessing and honest prequential prediction.
- **UNVERIFIED:** π base-16 normality; a canonical source-locked Fibonacci time law; a source-derived native gauge/selection mechanism; a new selected signed Weyl inequality.

**Next falsifier:** Predeclare a constrained predictor family C (bounded code/memory/allowed reset) and a future unseen digit interval. Test frozen predictions, charged revisions, full 16-digit/finite-block held-out frequencies, and exact zero-seed-vs-coherent-seed controls. The closed-class theorem is logical; it must not be marketed as quantitative π normality or as a bound on computationally unrestricted prediction.

References: PR #397 (source passport and proofs), Schnorr–Stimm finite-state martingale characterization as quantified in Lutz & Mayordomo et al., *Asymptotic Divergences and Strong Dichotomy*, STACS 2020 (https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2020.51), and computable normal examples in Becher et al., *A zoo of computable binary normal sequences*, PNAS 2012 (https://doi.org/10.1073/pnas.1215998109).

**Root validation, hosted CI, Lean and blind mathematical review NOT RUN on this additive file.**
