# Next round: source-relative log phase to joint carries

**Continuation:** the user's subsequent four-pole question was worked through in the
same research round. Read the [atomic/compiler handoff](FOUR_POLE_ATOMIC_NEXT_2026-10-26.md)
first for the current combined frontier. This document retains the exact source-relative
phase and carry obligations; none of its cancellation limitations has been removed.

**Mode:** research execution, exact source first. **pi normality: OPEN. RH: OPEN.**
Recheck current heads and AGENTS.md. This work branches from PR #306 at
`7989be5753341c5e74d570e8fea51e00129d2d0a`; no merge authorization is supplied here.

## Read the results before choosing the next target

1. [Source-bridge dossier](../research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md),
   especially the complete proofs and countermodels in sections 6–11.
2. [Current selected-pi frontier](../docs/PI_SELECTED_CATEGORICAL_FRONTIER.md).
3. The source hashes and exact [receipt](../research/2026-10-26/OILY_MACARONI_RECEIPT.json)
   and [validation](../research/2026-10-26/VALIDATION.md).

## Earned objects, available without any pi digit oracle

For `(d,v)=(3,2),(4,1),(5,1)`, let

$$
\int f(B)d\mu=\sum_{j\ge1}16^{-j}\sum_{d,v}v\int_0^d f(8j-7+u)du,
\quad T_n=\mathbb E_\mu(8n+B)^{-2}.
$$

The exact source fixes E B=7/2 and E B squared=55/3. Under the inverse-square tilted
law nu_n, put

$$
\eta_n=\mathbb E_{\nu_n}\log(1+B/(8n)),\qquad
\Psi_n(t)=\mathbb E_{\nu_n}\exp[-it\log(1+B/(8n))].
$$

Proved: eta_n is asymptotic to 7/(16n), T_n/eta_n squared tends to 4/49,
and the logarithmic source observable satisfies
`E(log Y_n-lambda^2)=(lambda-gamma)-eta_n`.
Also proved for every n at least 1:

$$
\frac1{(8n+7/2)^2}<T_n<\frac{(H_n-\log n-\gamma)^2}{16}.
$$

The finite source code gives exact rational enclosures for these quantities. Delta is a
reference log mean; lambda cancels from both error comparisons.

The normalized moving-frequency source map is now also proved. For `a=8n`, let
`q_n(B)=a log(1+B/a) mod 1` and `Theta_n(k)=Psi_n(2 pi k a)`. The exact law has
`B=K+V`, with V an independent uniform unit cell, so B modulo one is Haar. For every
fixed nonzero integer k:

$$
|\Theta_n(k)|\le\frac{7+55\pi|k|/3}{8n}
\left(1+\frac7{16n}\right)^2,\qquad
8n\Theta_n(k)\longrightarrow-\frac72-\frac{i}{2\pi k}.
$$

In particular `Theta_n(k)/eta_n -> -1-i/(7 pi k)` and
`|Theta_n(k)|^2/T_n -> 49/4+1/(4 pi^2 k^2)`. This is actual cancellation of the
auxiliary source pushforward. It has not been transported to the selected orbit.

## Two invalid shortcuts must not be revived

- For fixed N, `limsup_(h->infinity) |A_N(16h)|/|A_N(h)|<1` is false on the authentic
  rational prefix: common-denominator multiples give ratio 1. For fixed h, the difference
  between the two means is O_h(1/N), so a uniform strict ratio already implies bounded
  unnormalized sums. A numerical ratio near 1 is not evidence against normality.
- Even h kills a one-digit top Walsh coefficient, but cross-digit fourth-order terms
  survive. The exact two-digit parity law on bits `{0,4,5,6}` defeats all joint marginals
  of order at most three and even complete single-digit uniformity.

The old handoff is retained only as a superseded historical proposal. These corrections
do not exhaust or rule out every multiscale argument.

## The next construction must have an actual source and observable

Try to construct a typed interface from the proved moving-frequency source-circle
observable Theta_n, or the **relative** Mellin factor, to a signed joint carry observable.
Start with two hexadecimal digits and the authentic integer lift.
Explicitly enumerate the Walsh coefficients of the full word character at the selected h;
retain the cross-time products that survive even when individual digit coefficients vanish.

The construction must state its domain, map/kernel, normalized measure or amplitude, initial
selector, target observable, and residual. Its first acceptance gate is an exact commuting
identity or bounded transport theorem on those objects, not a scalar resemblance.
On the common carrier the actual orbit is exactly
`U_n=E_mu[16^n/B^2-(8n+B)^(-2)]`. Its character is the exponential of that expectation;
an expectation of exponentials is a different observable. Preserve this distinction.

There is a concrete difficulty to overcome: for each fixed t,

$$
1-|\Psi_n(t)|^2\le\frac{55t^2}{192n^2},
$$

so a sufficiently late product of these magnitudes is strictly positive. The harmonic
phase drift cannot be rebranded as a nonsummable modulus loss. The available choice
`t_n=16 pi k n` solves the auxiliary cancellation problem; it still needs a map and
uniform residual preserving the arithmetic phase and initial selector.

An alternative is a source-specific signed cross-block estimate that uses the exact
four-pole and integer-carry correlations. If either approach merely rewrites the selected
Weyl gate, label it a reformulation and isolate a weaker intermediate lemma.

## Mandatory discriminating controls

Use the existing authentic zero-seed source, its exact-forcing changed-seed twin, SS-08,
the carry-preserving controls, and the new matched-moment rational law

$$
\mu_*=(73/148)\delta_1+(75/148)\delta_{89/15}.
$$

This control shares the first two mixing moments, tail coefficients through n^-4, eta
coefficients through n^-2, and the leading relative-coherence loss. Its zero-seed orbit
is nevertheless nonnormal, with `T*_0=4021/7921` and normalized h=7921 Fourier sum tending
to 1. A proof must reject it by a full-source condition, not by a different variable name.
Also preserve the exact finite-conductor resonance and the cross-digit even-mode countermodel.

The stronger uniform-cell control must also be excluded. Take independent uniform
V on [0,1] and K=1,3,7 with probabilities 1/2,1/4,1/4, then B=K+V. It matches
the first two B moments AND the new Theta cancellation and first-order coefficient.
Yet its rational `T_cell(0)=185/672` gives a zero-seed nonnormal orbit with normalized
h=672 Fourier sum tending to one. Its forcing is not the four-pole source. A new
transport must distinguish this control explicitly; the unit-cell mechanism alone cannot.

## Quantifiers and deliverable

A fixed nonzero h estimate `S_N(h)=o(N)` for all h would prove normality; it is still missing.
The growing Fejer gate is stronger. If using a uniform mode bound `|A_N(h)|<=1-c_N`, it
needs `H_N(1-c_N)^2 -> 0`, not merely `c_N -> 1`.

Deliver one proved intermediate transport/inequality or a falsified candidate with its exact
control. Keep the surviving analytic bridges, preserve original source bytes, run AGENTS.md
validation, commit coherently, and use a draft research PR. Avoid repeated CI pushes.
