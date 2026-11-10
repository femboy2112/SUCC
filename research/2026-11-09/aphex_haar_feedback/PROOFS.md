# Aphex-shaped inverse-response feedback for SUCC's parity pinbed

**Research-only, 2026-11-09.** Additive child of draft #572, exact parent 259238b7d71277605b26ab0a391334b5891b0e3c. Original four signed BBP poles, literal U0=0, prior source/provenance, formal contracts, archived research and main unchanged. Base-16 normality of pi, even/odd hexadecimal digit balance, and RH remain OPEN.

## Source and interpretation

Track two of Aphex Twin's 1999 Windowlicker EP is titled by a formula, also called Formula or Equation. See Warp Records (https://aphextwin.warp.net/release/68151-aphex-twin-windowlicker) and MathOverflow (https://mathoverflow.net/questions/56489/where-does-aphex-twins-windowlicker-equation-come-from). There is no documented authoritative interpretation of M,D,F,C,alpha. Transcriptions differ on the final time-index n^{-1} versus n-1. This note is a NEW SUCC mathematical interpretation, not a recovered physical meaning of the music.

The expression has the form

\[
\Delta M_i^{-1}=-\alpha\sum_{n=1}^N D_i[n]
 \left[\sum_{j\in C[i]} F_{ji}[n-1]+F_i^{ext}[n-1]\right].
\]

We declare inverse response g=M^{-1}=g_ref+beta, not literal physical mass. The sum of incident and external forces is a source-authenticated feature x_n; D[n]=beta*x_n-y_n is a centered signed probe residual. The lag is a declared batch feature label. The epoch means below are retrospective, so this is not a causal streaming implementation without an explicit previous-window calibration.

## APH-01: Exact deterministic feedback theorem

From #572's original-source pi parity split s_n=a_n*b_n, with a_n the selected genuine balanced-prime sign and b_n the full real/CRT/winding complement, set x_n=a_n-mean(a), y_n=b_n-mean(b), V=mean(x²)>0, C=mean(x*y). Define

\[
L_A(\beta)=\frac1{2A}\sum_{n=A}^{2A-1}(y_n-\beta x_n)^2.
\]

Then L_A'(\beta)=V beta-C and

\[
\beta_{new}=\beta-\frac{\eta}{A}\sum_n
  (\beta x_n-y_n)x_n
=\beta-\eta(V\beta-C).
\]

For any real 0<eta<2/V, the exact quadratic decrease is

\[
L_A(\beta)-L_A(\beta_{new})
=\eta(1-\eta V/2)(V\beta-C)^2\ge0.
\]

The unique optimum is beta*=C/V. Starting at beta=0 with eta=1/V attains beta* in one batch update. All assertions are exact finite least-squares identities, not a pi asymptotic estimate or probabilistic independence theorem. Gain positivity g_ref+beta>0 is checked separately; unstable steps and V=0 are rejected in code.

## APH-02: The open arithmetic parity gate becomes a calibrated observer coefficient

The authentic original real digit parity mean satisfies the exact identity

\[
mean(s)=mean(a)mean(b)+C
       =mean(a)mean(b)+V\beta^*.
\]

By #572 PPP-04, conditional on #554/BEC's authentic balanced-prime all-frequency character bounds and its imported analytic inputs, mean(a)->0 and V=1-mean(a)²->1. Since |mean(b)|<=1, the zero-selected real parity balance condition is equivalent to beta*_A->0 across every integer epoch. **That limit remains OPEN.** Optimization convergence in the number of tuning steps for one finite A is NOT arithmetic convergence as A->infinity.

## APH-03: Exact original-zero and hostile coherent-seed distinction

Reuse the preregistered #572 p=1217, A=512 original-source window, not a new blind holdout:

~~~text
mean(a)            = -1/128
mean(b)            =  1/128
mean(real parity)  =  5/128
C                   = 641/16384
V                   = 16383/16384
beta*(original)     = 641/16383 ~ 0.0391259232131
~~~

The rational source-compatible p-integral coherent wrong seed from #572 retains the same prime sign a_n and the 2-adic clock but forces completed real parity s_n=+1. Therefore b_n=a_n, C_shadow=V, beta*_shadow=1 and the fitted residual energy is EXACTLY ZERO. This is a decisive negative control:

**Perfect training fit is not evidence of Haar.** The observer can model a maximally nonnormal trajectory perfectly while its fitted parameter records the non-Haar coupling.

Positive local p collision pressure is about 15.648 on this epoch, while source parity feature variance V is close to 1. High prime-support concentration need not make the one selected signed feature badly conditioned.

## APH-04: Graph interaction and rank firewall

The multichannel version uses an authenticated finite feature matrix X, with columns from prime source, global winding, lagged Haar child differences and causal history, and independent target y. Update

\[
g_{new}=g-\alpha X^\top(Xg-y)
\]

is exact gradient descent on (1/2)||Xg-y||². For frozen X and y and 0<alpha<2/||X||_2², the objective is nonincreasing. With positive diagonal gain G, rank(XG)=rank(X): gain tuning cannot repair the missing observational channel of an actually rank-deficient source clock. This is why #554's redesigned balanced time window is qualitatively different from changing sensor amplitudes.

The fitted coefficient is gauge dependent: rescaling x by c changes beta* by 1/c. Freeze normalizations and source imports. A fitted beta from the same window is not an independent test. For prospective prediction, train on one frozen epoch and validate on a disjoint source window without reusing outcomes.

## Claim ledger

- APH-01: PROVED LOCAL. Exact deterministic gradient descent, loss identity and stability interval.
- APH-02: EQUIVALENT REFORMULATION, conditional on #554's imported source-specific character bound. No pi parity theorem.
- APH-03: OBSERVED FINITE on the genuine source; source-preserving wrong-seed algebra is PROVED. REFUTED: zero fitted error implies Haar.
- APH-04: PROVED ALGEBRA. Matrix descent and rank invariance; no arithmetic mixing claim.
- Original-zero all-epoch beta*_A->0: UNVERIFIED / OPEN.
- Pi base-16 normality and RH: OPEN.

## Reproducibility

Production module observational_succ/aphex_haar_feedback.py and root-discovered tests tests/test_aphex_haar_feedback.py; six focused Python 3.13 tests PASS locally, including authentic #572 A512 full-source replay, original versus wrong seed, exact loss decrease, parity maximally biased with zero loss, zero-feature identifiability, and positive gain checks. The isolated local environment includes a disclosed test-only duck_bbp source fixture, **not committed**. Tested local Git blobs are 7c20a281f2be800b2fea17ca9f3941b1561930f7 and 0565994e7f0e9ae98ff3ddddd252228be619edc3. Full native repository suite, new Lean formalization, final-head hosted CI and independent scholarly refereeing are not asserted.

**Next theorem changing the verdict:** derive a true all-epoch original U0=0 bound forcing signed covariance C_A->0 (equivalently beta*_A->0), while rejecting the p-integral wrong-seed and retaining full source/all-prime CRT winding, real boundary corrections and phase. A feedback rule by itself cannot pay this arithmetic debt.
