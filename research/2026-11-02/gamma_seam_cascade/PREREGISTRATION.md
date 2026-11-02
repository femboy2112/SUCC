# Pre-registered Gamma seam / aggregate Haar tests

**Registered prior to evaluation (2026-11-02).** Parent: PR #465 exact head `70f4146d9bcb39e45026e88cc141ddad656f337d`. Original four signed BBP poles and literal `U_0=0` remain unchanged.

## Exact rational holdouts and fixed threshold

Use the inherited `finite_certificate.py` original-source `alpha_N`, Machin π interval and rational sine/cosine Taylor remainders; pass/fail is an **exact rational** strict comparison, not native floating point.

- `N=512`, harmonics `h=1,5,11`, intermediate dyadic half-window scales `L=16,32,64`.
- `N=1024`, harmonics `h=1,5,11`, intermediate dyadic half-window scales `L=32,64,128`.
- On every listed triple, preselect `W_(N,L)>(1/10)E_(N,L)`, where `W` is **aggregate** signed squared Haar difference and `E` is the aggregate child energy. All strict margins, passes, failures and ambiguous errors will be retained. The top-scale pair is deliberately excluded.
- This is same-reasoner preregistration, not independently blinded validation. The finite results cannot establish an all-horizon theorem.

## Falsification and controls

1. Original `r(n)` from both literal four signed poles and the independent combined rational form, exact `U_0=0`.
2. At every rational seam verify `R_(a,c)=R_(a,b)+16^(a-b)R_(b,c)`, with `R_(a,b)=sum_(j=a+1)^b16^(a-j)r(j)`. Wrong sign/scale mutations must be rejected.
3. Same-four-pole changed real seed `s=1/5-pi/16` gives **constant completed phase** `e(h16^n/5)=e(h/5)`. Its aggregate `W=0` for all pairs; a purported universal positive lower bound must fail.
4. Do not infer true signed cancellation from Gamma/Beta source positivity, merely small phase-error bounds, or aggregate finite positivity.

**PASS** means the exact rational inequality margin is positive after interval error. **AMBIGUOUS** means intervals do not decide. **REFUTED** means a mathematically decisive real violation, not a failed approximate probe. An all-prefix cascade theorem requires separate symbolic proof and an all-horizon original-source signed premise. π normality remains OPEN.
