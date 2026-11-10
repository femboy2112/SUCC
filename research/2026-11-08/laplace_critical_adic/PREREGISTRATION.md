# Preregistration — source-Laplace critical bridge (2026-11-08)

**Frozen parent:** PR #558 `46b96e61ea8a309546b399da328c9bfcc077ada2`. **Main untouched.** Original four signed BBP poles, U0=0, all source contracts unchanged.

**Question:** Can Laplace-scale analysis of the genuine additive-adelic character product produce a phase-sensitive source inequality, rather than merely an equivalent Abel/Cesaro statement?

## Declared algebra/theorems to test independently

1. Exact source density `Q(t)=4-2t^3-t^4-t^5` gives `r(n)=integral_0^1 t^(8n-8) Q(t) dt` and `R(z)=z integral_0^1 Q(t)/(1-z t^8) dt`. Source endpoint expansion should have coefficient 15/64 in `(1-z)log(1/(1-z))`.
2. Exact frequency Ward identity `G_h(z)=1+z G_(16h)(z)+z E_h(z)`, `E_h(z)=sum_n z^n e(16h U_n)(e(h r(n+1))-1)`.
3. A uniform source bound `(1-e^-t)|E_h(e^-t)| <= C min(1,t(1+sqrt(|h|)))` with explicitly declared C, and the critical double scaling `h*t² -> lambda`.
4. Source-only critical response `D_h(t)=t sum_n e^-tn(e(h r(n+1))-1)` should converge to `int_0^infty e^-x(e(15lambda/(64x²))-1)dx`. Show analytically that it is nonzero for lambda !=0, and has a square-root cusp as lambda->0. **This response is seed-blind and is NOT a Weyl mean.**
5. Wrong-seed control `s*=-pi/16` has fixed-h Laplace boundary 1 although original source density and Ward forcing are identical. At critical h~lambda/t², use `U_n(s*)=-T_n` for a distinct non-Haar scaling control.
6. Exact finite-epoch Laplace overlap `L_(A,h)(tau)=(1/A)sum_(n=A)^(2A-1)exp(-tau(n-A)/A)prod_p e(h[U_n]_p)`. Its discrete Fourier decomposition retains *all* cross terms; do not posit prime independence.

## Frozen numerical holdouts

Independent source-only critical scaling at `A in {160, 320, 640}`, `lambda in {1/64,1/8,1}`, with `t=1/A` and integer `h=round(lambda*A²)`. Also original signed-epoch Laplace readings at `A in {192, 320}`, `h in {1,3}`, `tau in {0,1/4,1}`; these epochs have already been used in #558 and are **NOT blind for the phase mean**. Critical-response diagnostics at A=160/320/640 are newly declared here before running.

## Outcome rules

- **PASS (finite identity):** exact rational/source recurrence/CRT equality or provably bounded numerical remainder under an independent implementation.
- **PARTIAL (new source invariant):** proved critical-scaling law or genuine analytically controlled pole/branch distinction with explicit wrong-seed controls, without selected mean decay.
- **FAIL:** a required identity breaks, a bound underestimates exact data, or a proposed decay claim survives coherent wrong seeds.
- **OPEN:** any asymptotic `lim_(A->infty) W_A(h)=0` for the original zero seed; any signed prime/complement spectral overlap bound implying it.

All novel proof statements must be scoped as paper derivations, not Lean/external peer review. Full SUCC native tests require an actual full checkout/hosted run, not inference from isolated tests.
