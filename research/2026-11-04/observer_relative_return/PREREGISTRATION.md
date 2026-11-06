# Operation Two-Clock Return × Observer-Relative Boundary Flux — preregistration

Research draft, November 4, 2026. Strict additive child of [SUCC draft PR #504](https://github.com/femboy2112/SUCC/pull/504) at immutable parent \`f3327bdce023fe3f68d4c5431b5a7c2b53dac2ed\`. Sibling #503/#505 critical chirp drafts **read only**, not inherited. Original signed four-pole source, literal U_0=0, all archive and formal contracts, production and main untouched. **No merge/tag/release/publication.**

This document **does not claim blind discovery**. The frame-lag asymptotic and its endpoint constants were derived interactively before the preregistration, as development leads. The following finite holds are prospectively nominated before running the new probe: independent epochs A=307, 953, 1901, 4099, 8191; artificial critical-frequency ratios q=H/A^2 chosen near 16,32,64; fixed observer lag ell=1 or 2; source-only radial states from the original #499/504 exact tap vector. The numbers used to fit the proposed theorem are **none**; its constants derive analytically from the known radial tail. A critical actual SUCC schedule \`H_A(h)=|h|16^floor(log_16(A^2 log A/|h|))\` must be analyzed separately: at practicable A, q can be small, so early finite tests are not evidence of the asymptotic sharp-boundary limit.

## Proposed all-time proofs (not yet independently tested)

1. Source-clock transfer: \`Z_(n+ell)=16^ell Z_n + sum_(j=1)^ell 16^(ell-j) r_rad(n+j)\`, hence \`Z_(n+ell)-Z_n\` is cancellation of order 1/n source and amplified outstanding balance, leaving \`-ell/(32 n^2)+O_ell(n^-3)\`. The repayment need not be simultaneous in a source- vs observer-time perspective.
2. Exact observer-frame Wilson link: \`W_(n,m)=e(H(Z_m-Z_n))\`; satisfies \`W_(n,m) W_(m,k)=W_(n,k)\`, and all loop holonomies are 1. This is a flat **gauge** identity, not stochastic independence/quantum transport.
3. For fixed nonzero signed ell, \`C_A,ell(H)=A^-1 sum_(n=A)^(2A-1) e(H(Z_(n+ell)-Z_n))\` and \`q=H/A²~log A\` show \`C=8/(pi i ell q)*(8 e(-ell q/128)-e(-ell q/32))+O_ell(q^-2+q/A)\`. Therefore its sharp-epoch magnitude is bounded ABOVE and BELOW by constants times 1/log A, not \`o(1/log A)\`.
4. Replacing the sharp epoch by a fixed C∞ bump \`w(n/A)\` supported strictly in (1,2) gives a signed difference-frame response \`O_(m,w,ell)(q^-m+q/A)\` for each fixed m, i.e. a smoothing-induced apparent **stronger** cancellation; this cannot be substituted for the full sharp-window or maximal-subinterval original Weyl gate.
5. Fixed-h time-lagged source \`Y_n+Z_(n+ell)\` differs from original \`U_n=Y_n+Z_n\` by a summable perturbation \`O_ell(n^-2)\`; its fixed-h Weyl normality status is therefore equivalent to original, not an independent result.
6. Original coupled temporal signal \`e(HU_n)\` remains unbounded by the relative-lag radial response alone. Positive test is source-labelled exact identities; negative tests include \`Y_n=-Z_(n+ell)\` companion, \`Z_n+16^n/5\` seed-twist with 16≡1 mod5, coherent wrong seed, and a sign-flipped observer orientation.

## Prospectively declared numerical and exact calibrations

- Exact Fraction recurrence identity at n in (1,2,17,53,101) and ell in (1,2,5); exact line/circle Wilson cocycle for arbitrary rational test nodes, no floating tolerance.
- Independent evaluation: derive \`Z_(n+ell)-Z_n\` both from finite recurrence and from a 24-step **difference of future negative-source tails**; require absolute error less than 1e-12 for n>=307 (truncation exponentially below this), using separately computed numerator products, not difference of two rounded Z floats.
- For artificial q≈16,32,64 at proposed A, compare exact finite lag sum to continuum integral and analytic endpoint main term. Do **not** require a misleadingly tight threshold at q=16; compare residual against the provable \`O(q^-2+q/A)\` envelope with a generous diagnostic constant.
- For original schedule, report signed q and observed residuals without fit. Negative/mutation controls must expose any attempt to declare “relative cancellation = original π normality.”
- No requirement to run the full ≈11k SUCC suite for this additive research step. Run focused local stdlib tests; hosted exact-head CI may run separately and must not be awaited or falsely reported as passed.

**Pass:** rigorous all-horizon source-specific relative-frame theorem with explicit correct obstruction to the original signed-Weyl target, plus reproducible independent calibrated probes. **Fail:** silently treating an eight-root analytic ensemble or observer twirl as selected time Haar; hiding nonzero boundary terms; asserting root-of-unity/Frobenius signs are additive Weyl characters; or claiming \`o(log^-1 A)\` for a sharp lagged radial mean contradicted by the endpoint term.

The original selected high-depth maximal-subinterval Weyl estimate, original coarse current, base-16 π normality and RH are **OPEN** unless a new discriminating signed source estimate genuinely proves otherwise.
