# Exact-source original angular/radial observer-lag finite probe

**Diagnostic only** — no inference about the asymptotic signed Weyl gate from three finite epochs. This is a source-faithful test of the *COUPLED* process, not only the analytically simpler radial ghost. The source is the original eight-tap signed BBP vector \(P=(4,0,0,-2,-1,-1,0,0)\) with literal \(U_0=0\). The probe keeps complete rational modular phase carries by iterating the authentic source as \`fractions.Fraction\`; simultaneously recomputes angular Y and radial Z and checks \((Y_n+Z_n)\bmod1=U_n\bmod1\) at **every step**. Only the complex exponential is evaluated in floating point.

## Observer comparisons

For \(A\in\{128,256,512\},h=1\), set \(H_A=16^{\lfloor\log_{16}(A^2\log A)\rfloor}\), \(q=H_A/A^2\), and consider
\[
C^\ell_A(I)=A^{-1}\sum_{n\in I}e(H_A(Y_n+Z_{n+\ell})).
\]
The full-epoch magnitude \(|C^\ell_A([A,2A))|\) and maximal consecutive subinterval magnitude \(M^\ell_A=\max_I|C^\ell_A(I)|\) were computed with exact rational phases before the final floating exponential.

| A | H | q | lag -2 M | lag -1 M | genuine lag 0 M | lag +1 M | lag +2 M |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 128 | 65,536 | 4 | 0.135320883 | 0.137519062 | 0.138677044 | 0.137603845 | 0.136481239 |
| 256 | 65,536 | 1 | 0.076096555 | 0.076693351 | 0.077069600 | 0.077229330 | 0.077177191 |
| 512 | 1,048,576 | 4 | 0.054923657 | 0.058030412 | 0.059676855 | 0.060958192 | 0.061294200 |

For the source-authentic \(A=512\), lag 0, \(q M^0_{512}=4(0.059676855)=0.238707420\), recovering to the displayed precision the independently reported **0.238707419–0.238707420** finite interval in [sibling PR #505](https://github.com/femboy2112/SUCC/pull/505). This is a source/calculation cross-check with shared original BBP data, **not** independent verification of any asymptotic theorem.

The observed lag dependence at A=512 raises M from lag -2 through lag +2; at A=128 it reverses after lag zero; at A=256 the maximum is slightly displaced. Thus the finite data do **not** support any universal assertion that delaying a radial frame improves the original coupled cancellation. The lagged original-source values are not new source orbits and change the observation map; only ell=0 is the original π gate.

The reproducible stdlib source is [original_coupled_probe.py](original_coupled_probe.py). Its \`--verify\` flag separately asserts exact source-gluing and the parent/sibling A=512 finite calibration, prints \`ORIGINAL_COUPLED_OBSERVER_FINITE_REPLAY_PASS\` and the full JSON. A locally matching direct Fraction implementation was executed and passed; run the committed script on a checkout to verify the exact remote bytes. No native full SUCC suite or hosted exact-head CI success is inferred.

**Research consequence:** radial one-factor phase bounds, flat Wilson links, and an arbitrarily well-tuned observer Jacobian do not bound the genuine \(\ell=0\) angular–radial mixed maximal-subinterval Weyl character. This remains the load-bearing source-selected obstruction to proving π base-16 normality.
