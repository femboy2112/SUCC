# Covariance forge: stronger local cancellation, exact learning costs

**Pi base-16 normality: OPEN. RH: OPEN.** This is the next additive research
round after `47ec1ccf9d3579897abb94c047f3b4dc13b4cb70` in draft #544, on pinned
main `d32342d375f44ddf62221ad6aff2f534abdc0a03`. The former dossier is preserved.
All new work is in this namespace; source contracts and main-facing catalogs
are unchanged. This file is the current proof-frontier handoff.

## Strongest positive result: polynomial-time local-source cancellation

Let p_A be the largest p<=4A with p prime, p=1 mod8, and m_A=ord_p(16)
satisfying m_A^3>p. Use the actual original unwrapped BBP source

\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The prior PE theorem proves p_A~4A and complete clean prime cycles covering
asymptotically the actual epoch. The new result is

\[
\sup_{1\le h<p_A}\ \sup_{\deg P\le d_A}
\left|\frac1A\sum_{n=A}^{2A-1}
 e\bigl(h[U_n(0)]_{p_A}+P(n)\bigr)\right|\longrightarrow0
\quad\text{if }2^{d_A}=o(\log p_A).
\]

Here P is any real polynomial with unrestricted coefficients, including
coefficients chosen from the history. This includes all fixed degrees. It is
an actual uniform signed estimate for the original source's selected prime
component. It does **not** estimate the full real character e(hU_n).

The proof has three steps, with every cost retained:

1. Exact prime-clock autocorrelation plus the same classical BK theorem used
   in PE9 gives every temporal DFT coefficient the bound
   `|ahat_k|² <= 1/m+(1-1/m)p^(-gamma)`.
2. Repeated finite-window differencing cancels polynomial time phases while
   preserving the nonzero source coefficient
   `xi product_j(16^(h_j)-1) modp`. For degree d and suitable H,
   `|mean|^(2^d) <= 5^(2^d-1)[1/H+p^(-gamma)+d(H-1)/m]`.
3. Choose H=floor(sqrt(m/d)) and transfer complete cycles to the actual epoch.
   The bound is `eps_A+5 exp(-c log(p_A)/2^d_A)` for any fixed
   `0<c<min(gamma,1/6)` eventually. eps_A is the explicit interval-weight error
   from PE; only eps_A->0 is asserted here, not an all-epoch power rate.

See [CFS-1–7 proofs](spectral/THEOREMS.md) and the
[growing-degree corollary](GROWING_CHIRPS.md). The new result is relative to
the inspected SUCC frontier; worldwide priority and external refereeing are
not claimed. PNT/AP and BK remain declared classical inputs, not Lean theorems
proved by this package.

## What the learning observer can now certify

The observer must pay for both its complement prediction error and the
amount of prime-phase information revealed by its features. On a clean
clock, repeated cycles can first be folded exactly: nonperiodic replica
variation is orthogonal to the local character and contributes zero.

For the folded complement B and any declared history-feature projection P,
put u=conjugate(a)-Econjugate(a), v=B-EB. The exact identity is

\[
\operatorname{Cov}(a,b)=\langle Pu,Pv\rangle+
 \langle(I-P)u,(I-P)v\rangle.
\]

It gives the sharp norm bound

\[
|\operatorname{Cov}|\le
 \|Pu\|\|Pv\|+\|(I-P)u\|\|(I-P)v\|.
\]

Refining history decreases prediction error but can increase prime leakage.
Arbitrary one-dimensional learned models can already be perfectly resonant;
dimension alone supplies no saving. Cyclic-shift-invariant models are Fourier
subspaces, so the new clock theorem does control their leakage. The same
uniform bound supports adaptively chosen finite mixtures of temporal chirps:

\[
|W_A(h;0)|\le\rho_A K_A+\mathbb E|b-v|,
\quad v_n=\sum_j c_j e(P_j(n)),\quad K_A=\sum_j|c_j|.
\]

The still-unproved sufficient premise is rho_A K_A->0 and approximation
error->0 for the **original** complement. It is stronger than cancellation
alone, and is not advertised as a newly weaker normality equivalence.

This extends the previous LY theory's lawful transcripts and memory fibers
with an explicit quantitative certificate. It creates no incompatible
category hierarchy. Mathematical model dimension, stored bits, access
precision and exact source authentication remain separate resources.
The literal-zero source is already specified; learning here means finding
and certifying useful structure in its response, not making the source random.

## Stronger countermodels narrow the missing source condition

[CF-A1–6](arithmetic/THEOREMS.md) construct positive rational, same-forcing
seeds s_A with **the exact original terminal denominator** d_(2A-1), and all
earlier denominators dividing the original cumulative denominator. They
preserve the selected prime clock, fixed additional prime observations,
linearly many 2-adic bits, and a linearly growing exact carry prefix, while
their signed complementary covariance tends to1. The source-forced denominator
reservoir from pinned #532 supports this construction; no external prime is
needed. Its proved 2-adic capacity per terminal time approaches
`5/log(2)-4`, approximately3.21347 bits.

Every such seed still fails literal-zero and chronological birth
authentication. Matching terminal support is weaker than matching the source
history. The quantifiers are `for every sufficiently large A, there exists
s_A`; this is not one fixed rational nonnormal seed.

[C1–C4](crucible/THEOREMS.md) also establish sharp rational height isolation,
the exact half-open carry fiber, a precision-versus-horizon minimax bound,
and a fixed wrong-forcing two-prime countermodel with both marginals exactly
zero but covariance above0.98. An exact zero tag or certified complete support
can isolate rational zero using finite data; no blanket memory-impossibility
claim is made.

## The integrated proof chain and the unpaid arrow

| Arrow | Exact support | Status | Failure if weakened |
|---|---|---|---|
| Literal source -> unwrapped history, carries, local/complement phases | Shared forcing, exact integer/Fraction oracles; `authenticate_history` | Proved and finitely replayed | Wrong seed, wrapped-only lift or pole mutation rejected |
| Source genealogy -> complete prime clocks covering every large epoch | Prior PE1–9; elementary order count and PNT/AP | Proved paper with classical inputs | Unclean pole transition invalidates a frozen clock |
| Prime clocks -> all temporal Fourier and budgeted polynomial cancellation | CFS1–2,7 and CF-R1 | New proved local-source bound | Shift equal to the full order makes difference coefficient zero |
| History model -> signed complement certificate | CFS3–6; `history_certificate.py` | Proved conditional bound; finite implementation | Learning the prime phase too well can destroy the saving |
| Original source -> vanishing certificate or signed covariance | No theorem here | **OPEN** | Terminal-support shadows preserve cheaper hypotheses while Cov->1 |
| Covariance decay -> full real Weyl decay | Exact `W=Cov+Ea Eb`, PE9 gives Ea->0 | Established conditional implication | Dropping covariance loses signed alignment |
| All fixed-h dyadic Weyl decay -> pi normality | Original Green tail, dyadic gluing, classical Weyl criterion | Established conditional implication | Finite holdouts and changing seeds do not satisfy all-epoch quantifiers |

The most promising unresolved target remains an original-zero estimate for
the **signed cross-spectrum**, with complete chronology and source support.
The new local estimates constrain candidate predictors but do not prove that
this source has one of the required low-complexity representations.
Sparse Fourier fitting was actually falsified in finite original-source cases;
its success is not an assumption in the proved local theorem.

## Research rounds, receipts and reproduction

[Experiments](EXPERIMENTS.md) records preregistered covariance, spectral and
history-model probes, including failures. The first two protocols and the
history protocol were committed and pushed before their measurements.
Independent algebra, separate modular recurrence/sum implementations, rational
interval containment, and hostile proof review provide distinct bearings.
All agents share a model, and several routes share the same source/BK input;
their agreement is not independent scholarly certification.

Run all new finite checks and the three cheap mandatory repository gates:

```sh
python research/2026-11-08/covariance_forge/validate.py --output /tmp/covariance-forge-replay
```

Use `--full` to additionally repeat the inherited native suite. The previous
12,147-test native pass is reused only with an explicit unchanged-input check;
new research tests and observations are reported separately. Outputs go to the
requested directory, preserving retained receipts. See [validation](VALIDATION.md)
for actual commands/results, source hashes and the final publication scope.

The next discriminating theorem would give a source-derived upper bound for
the signed residual left by a history projection. The next concrete probe is
a preregistered history-feature family with certified leakage **and** residual
decay across new scales; report failure if its bound stays near1. Do not infer
that increasing memory or matching more terminal arithmetic data will pay it.

**Pi base-16 normality: OPEN. RH: OPEN.**
