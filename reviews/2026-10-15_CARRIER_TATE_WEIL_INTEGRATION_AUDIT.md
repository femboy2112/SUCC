# Integration audit: carrier, Tate, and signed Weil interfaces

**Date:** 2026-10-15. **Inspected parent:** `d239c27d3759de71de316180f48dfc097be6aff5`, with the uncommitted additions on `research/carrier-tate-weil-2026-10-15`. **Audit status:** no unresolved mathematical defect found in the reviewed zeta/Weil formulas after the corrections below. The character proof note is reviewed in the final section when available. **RH proved:** NO.

## Scope and provenance

This was a separate, initially read-only integration review of `tate_idelic_zeta.py`, `tate_weil_distribution.py`, `tate_chi4.py`, `tate_positivity_obstruction.py`, their tests, and the accompanying mathematical notes. `AGENTS.md`, the import manifest, and the inherited Gamma-ladder, arithmetic-source, rational-interval and compact-window implementations were inspected. No archival original was edited.

The reviewer and authors are collaborating agents in the same model/tool environment. This is a distinct derivation and implementation cross-check, **not externally independent mathematical review**, a proof-assistant verification, or an independent source family. The authors' external references were not independently fetched again during this integration pass. Universal conclusions depend on the explicitly stated classical analytic inputs.

## Concrete corrections made before integration

1. **Gamma growth on an unbounded half-plane.** An early TZ-04 sentence incorrectly bounded `|Gamma_R(s)|` by `Gamma_R(sigma)` for every `Re(s)>=sigma`. The Mellin integral proves only `|Gamma_R(s)|<=Gamma_R(Re(s))`; uniform bounds require a bounded real strip or another declared envelope. The exact counterexample `sigma=2,s=20` has ratio
   \[
   \Gamma_{\mathbb R}(20)/\Gamma_{\mathbb R}(2)=9!/\pi^9>9!/4^9>1.
   \]
   The author independently found the same error and corrected the note, preserving this control. The finite Euler exhaustion bound itself was unaffected.
2. **Root number is not a general information-theoretic kernel.** Differentiating a functional equation removes its displayed root-number constant, but the *full* logarithmic derivative plus self-duality can recover it. If a nonzero meromorphic function satisfies `F(s)=w F(1-s)` and has central order `m`, comparison of leading Laurent terms gives `w=(-1)^m`; `m` is the central residue of `F'/F`. Thus a changed root label on the same genuine function is not a second lawful source. The revised note, code and claim summary distinguish this from the genuine overall-scalar kernel and require the concrete upstream Fourier/Gauss-sum check. The author and reviewer independently identified this correction.
3. **Closed-strip zeros and contour dependencies.** The first contour statement summed only over the open critical strip, although its stated dependencies did not include a boundary zero-free theorem. It now sums over all zeros of the completed function, which lie in the closed strip by Euler nonvanishing and the functional equation. Boundary nonvanishing is unnecessary for this identity. The zero-count symbol in the quantitative tail is explicitly the **two-sided** count; this prevents a hidden factor-of-two convention change.
4. **Finite execution budget versus all-support theorem.** The `atoms` implementation inherits `ceil(R)<=10` from `CompactWeilSourceWindow`. Its docstring now states `0<R<=10`; the distribution and continuity theorems apply to every finite support radius. A resource cutoff is not a mathematical failure of cofinality.

## Reconstructed interfaces and bounds

The rational-chart quotient was rederived directly from finite valuations: choose `q=sgn(x_infinity) product_p p^v_p(x_p)` and divide every coordinate by `q`. The positive real coordinate is the idelic norm, the finite coordinates are units, and the residual rational ambiguity is removed by positivity. The quotient Haar measure is `dr/r du`, with norm-one volume one; the signed rational orbit already accounts for both real signs. Local multiplicative shells have mass one, and the Gaussian real integral therefore produces the full `Gamma_R(s)`.

For the Weil formula, the reviewer independently checked the Mellin inversion signs, the two half-Gamma contributions, the pole terms, the `n^(-1/2)` factor, and the odd-character contact/kernel pair. Writing
\[
\alpha=\varepsilon+1/2,\quad
D_g(x)=g(x)+g(-x)-2e^{-x/2}g(0),\quad
K_\varepsilon(x)=\frac{e^{-\alpha x}}{1-e^{-2x}},
\]
the contact is `log(q/pi)+psi((epsilon+1)/2)`, and the Gamma term is contact times `g(0)` minus the integral of `K D`. For a fixed compact support and `M_j=||g^(j)||_infinity`,
\[
|D_g(x)|\le(2M_1+M_0)x,
\quad (1-e^{-2x})^{-1}\le1+(2x)^{-1}.
\]
These give the stated C1 continuity budget and, at `a=2J+alpha`, the tail
\[
(2M_1+M_0)\left(\frac1{2a}+\frac1{a^2}\right).
\]
For C2 tests,
\[
|D_g(x)-g(0)x|\le(M_2+M_0/4)x^2
\]
gives precisely the accelerated subtraction `A_J-g(0)/(2a)` and the stated O(J^-2) bound. These are analytic truncation bounds under declared norm premises; none bounds floating quadrature error.

The translated nonnegative bump has `g(0)=0`, one negative arithmetic atom, nonpositive Gamma term, and a bounded pole contribution. The rational zeta margin `-19/75` is valid. It is correctly excluded from the nonzero autocorrelation cone, whose origin value is a positive L2 norm.

The separate normalized-source obstruction also survives rederivation. With `D=x d/dx+1/2` and `A=(16/3)(D^2-1/16)`, the first Gaussian polynomial is
\[
1-32u+\frac{64}{3}u^2,
\]
and its Mellin multiplier is `P(s)=1+(16/3)s(s-1)`. Origin/integral normalization, all finite Euler factors, and pole residues are preserved. The odd compact test gives the negative auxiliary-divisor bound `-128/99225`. The complete canonical upper estimate `c+59b<4` and the resulting complete modified-source bound at multiplicity 4096 are consistent. This is a signed, deliberately modified Archimedean source; it is not a counterexample to canonical Weil positivity or RH.

## A different Gamma diagnostic that was actually executed

Using mpmath at **40 decimal digits**, the reviewer compared two Gamma representations on the noncompact Schwartz probes `g(x)=exp(-t*x*x)` with `t=0.6,2.3`, for both `(q,epsilon)=(1,0)` and `(4,1)`. This is a diagnostic extension of the Gamma term alone, not use of those tests in the compact arithmetic oracle.

The first calculation directly integrated the spatial renormalized kernel above. The second used the independently specified Gaussian Fourier transform and integrated
\[
\frac1\pi\int_0^\infty
\sqrt{\pi/t}\,e^{-u^2/(4t)}
\left[\log(q/\pi)+\Re\psi\left(\frac{\varepsilon+1/2+iu}{2}\right)\right]du.
\]

| Parity | Gaussian parameter t | Spatial minus spectral result |
| --- | --- | --- |
| 0 | 0.6 | 0 at the working precision |
| 0 | 2.3 | approximately `-2.2958874e-41` |
| 1 | 0.6 | approximately `-1.1479437e-41` |
| 1 | 2.3 | approximately `-7.5333805e-42` |

The evaluation used spatial breakpoints `0,1,3,infinity` and spectral breakpoints `0,1,3,8,infinity`. No zero positions or zeta/L evaluations were used. This cross-route agreement checks both Gamma parity conventions beyond the inherited tent adapter. It is **not an interval certificate**, a numerical sign proof, or evidence for RH.

## Character integration follow-up

Before the character proof note was written, its code and tests were inspected. The ramified local character is nonzero on `Q_2^times` and must not be confused with the Dirichlet coefficient `chi4(2)=0`. Its two-coset transform has the expected `-i/2` factor at the adopted finite Fourier orientation, and its multiplicative integral is one. The diagonal sign/ramified/unramified character product was checked algebraically.

The odd-theta error budgets were independently derived. For `3tN^2>=2`, the monotone Gaussian comparison gives `4/(3t) exp(-3tN^2/4)`. For `t>=1`, separating the first term and integrating the remaining absolute Gaussian sum gives `(10/3) exp(-3t/4)`. The split completed integral has powers `(s-1)/2` and `-s/2`; differentiating r times adds `(log t/2)^r`, bounded by `t^r/2^r`. These are the constants used by `completed_theta_error` and do not cover finite quadrature error.

The completed `TATE_CHI4_ARITHMETIC_CRUCIBLE.md` was subsequently inspected in full. No further mathematical defect was found. In particular:

* Its real test is exactly `x exp(-pi*t*x*x/4)`. With `dx/|x|` and the real sign character, this gives the declared Gamma factor without an extra two; the split theta integral consequently has prefactor `1/2`.
* The full Fourier relation is `Phi_hat_t(a)=t^(-3/2) Phi_(1/t)(4a)`, with 4 acting at **every** place. It correctly claims invariance up to rational dilation, not literal self-duality. The separate factors `2i` and `-i/2` cancel, and diagonal dilation permutes the rational sum.
* The all-place finite support intersects the diagonal in exactly the odd integers. The full signed integer theta sum has the correct extra factor two upon restriction to positive n. Its continuation uses the entire split integral, not a continued Euler product.
* The character, conductor, ramified local integral, local convergence domains, global absolute-convergence half-plane, absent zero-mode poles and signed prime-power tape are mutually compatible. The claimed rational interval mutation rejection depends on the explicitly stated tail estimates; an overlap is correctly only a consistency result.

The corrected Gamma bound and root-number code docstring were reread after their edits. The working-tree `git diff --check` command produced no whitespace error at this review checkpoint. Full repository validation and remote CI are the integrating principal's responsibility; this review does not claim to have run or observed them.
