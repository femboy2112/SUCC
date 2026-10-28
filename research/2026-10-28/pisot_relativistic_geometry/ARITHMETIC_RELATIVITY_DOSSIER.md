# Operation ARITHMETIC RELATIVITY — Pisot clocks, Hopf gauge curvature and the SUCC/FUCC frame interface

**2026-10-28.** Branch: `research/pisot-hopf-arithmetic-relativity-2026-10-28`. Base: Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36` (verified post-Claude merger #343). Original quaternionic research archive from October 27 is imported unchanged under `research/2026-10-28/hopf_local_archive/`. All code here is new research; original source, real zero seed, archive and claim status remain unchanged. **RH, π normality and any physical gravitational interpretation: OPEN / UNVERIFIED.**

## 0. Steelman and source passport

**User hypothesis:** a family of Pisot-based circle observations coherently supports arithmetic successor and prime dilation, suggesting frame-dependent clock scales and perhaps a relativity-like failure of simultaneity under extreme arithmetic reference transformations. The strongest defensible construction is a source-labelled arithmetic event graph equipped with declared clock 1-cochains, a separate nontrivial SU(2) gauge bundle from the quaternionic Hopf projection, and exact compatibility tests with the original BBP recurrence. This is not a metric on physical spacetime and does not postulate that observer disagreement changes an underlying mathematical event.

The authenticated source is

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)=(120n²-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]`, `n>=1`, and `U_0=0`, `U_(n+1)=16U_n+r(n+1)`. Its chiral source is precisely the imported Main XIII module `observational_succ/rank_two_chiral_towers.py` with blob SHA `8305e09892f19007e0ae0538a60d05954b2def9e`, and `T^8=I/16` on the source's four-real-dimensional additive carrier `Q(i)⊕Q(i)`. It is **not** a quaternionic ring. The local quaternionic identification is strictly Q-linear, with gauge choices and source-partner choices recorded.

## 1. The exact SUCC/FUCC mixed-frame synchronization square

For integer `n>=1` and genuine prime `p`, the affine braid is `V_p S = S^p V_p`, so both paths `n -> n+1 -> p(n+1)` and `n -> pn -> pn+p` end at the **same arithmetic event**. Give a successor edge at n the harmonic clock length `d_H(n)=1/n` and assign every prime dilation edge an **independent** logarithmic clock offset `log p`.

Path 1 has length `1/n+log p` while path 2 has length `log p + Σ_(j=0)^(p-1) 1/(pn+j)`. Their exact path discrepancy is

`D_p(n)=1/n-Σ_(j=0)^(p-1)1/(pn+j)=Σ_(j=1)^(p-1) j/[pn(pn+j)]>0`.

This is a closed-loop sum of a nonexact **mixed clock 1-cochain**. For all `n>=1, p>=2`, define `L=(p-1)/[2n(pn+p-1)]`, `A=(p-1)/(2pn²)`, `R=(p-1)(2p-1)/(6p²n³)`. Then `0<L<=D_p(n)<A` and `0<A-D_p(n)<=R`. Consequently `D_p(n)=((p-1)/(2p))n^-2+O_p(n^-3)`. These inequalities are independently checked by exact fractions in the focused tests; their proof comes from comparing denominators termwise and the identity `1/x - 1/(x+j)=j/[x(x+j)]`.

**Discriminator: genuine curvature or coordinate mismatch?** The harmonic potential `τ_H(n)=H_(n-1)` makes successor edges `1/n`. Its *correct* dilation edge is `H_(pn-1)-H_(n-1)`, not `log p`; with these integrable edge weights every SUCC/FUCC square has exactly zero holonomy. The logarithmic potential `τ_L(n)=log n` makes dilation `log p` but gives successor `log(1+1/n)`; again every square closes. Therefore the nonzero `D_p(n)` is due to mixing frames, and cannot be promoted to intrinsic curvature or violation of arithmetic simultaneity. A genuinely unavoidable obstruction must survive coherent choice of a common potential or gauge (it does not here).

### Euler–Mascheroni is precisely the cumulative mismatch of these two clocks

Since `1/n-log((n+1)/n)>0`, telescoping yields

`Σ_(n=1)^N [1/n-log(1+1/n)] = H_N-log(N+1) -> gamma`.

For Fibonacci times `F_k=(phi^k-psi^k)/sqrt5`, with `psi=-phi^-1`, the classical harmonic asymptotic gives

`H_(F_k) = k log(phi) - (1/2)log 5 + gamma + O(phi^-k)`.

This is the source-typed connection: golden ratio sets the effective clock *slope* along the Fibonacci/Pisot return subclock and Euler gamma sets the limiting *intercept*. It does **not** canonically derive the previously declared Ω=`phi^-1-gamma` from a unique frame or equate physical metric time with H_n.

The same two-rate idea holds for the quadratic Pisot units `β_m=(m+sqrt(m²+4))/2` (root of x²−mx−1). If `β'_m=-β_m^-1`, then `Tr(β_m^k)=β_m^k+(β'_m)^k` is an integer and `|β_m^k−Tr(β_m^k)|=β_m^-k`; consequently its *algebraic return attenuation* has exact logarithmic slope `log β_m`, a possible arithmetic redshift parameter, with no physical time postulated. The code tests integer companion recurrence and trace in exact Z arithmetic.

## 2. An authenticated second clock: Chiral BBP contraction versus real BBP expansion

The source's exact eight-step identity `T^8=I/16` yields for every x and every integer n>=0:

`16^n T^(8n) x = x`.

Thus eight **source tap steps** match one real 16-fold BBP expansion in inverse scale. This is an actual source-anchored two-clock synchronization law, not a numerically fitted relation. But the state `T^n b` tends to zero and its ordinary complex phases tend to 1, as the Main XIII rank-two source paper already warns. The authentic increasing selected `U_n` sequence must be transported separately; it cannot be replaced by shrinking impulse orbit phases.

Another exact clock is `C_n=U_n/16^n=Σ_(j=1)^n 16^-j r(j)`, which has positive tick `C_n-C_(n-1)=16^-n r(n)` and tends to `π/16` by the original BBP identity. This is a *finite-range/Zeno-style arithmetic time parameter*, not a finite physical elapsed lifetime or a conclusion about normality. It explicitly retains the genuine zero initial seed.

### Prime-scale commutator on the **real BBP state**, not the integer clock

For `S_n(u)=16u+r(n+1)` and `V_p(u)=pu`, exact algebra yields

`V_p S_n(u)-S_n V_p(u)=(p-1)r(n+1)`.

This commutator is independent of u, recovers the literal four-pole source for each p>1, and vanishes asymptotically as `O_p(n^-2)`; it is **not** the same SUCC/FUCC braid as `V_p S=S^p V_p` on natural-number indices. Source-commutator oscillatory phases become asymptotically 1 for fixed Fourier character and therefore do not imply a signed Weyl saving. A wrong-source scalar forcing can reproduce the same structural identity; using the exact four original poles is necessary for authentication, not sufficient for normality.

## 3. The genuinely nontrivial curvature already present in the Hopf bundle

The quaternionic right-Hopﬁ principal bundle `S^3 -> S^7 -> S^4` is a classical principal `Sp(1)≈SU(2)` gauge bundle, not a physical Lorentzian manifold. In the anchored stereographic chart `(x,1)`, its standard connection one-form (in a specified right-gauge convention) is

`A_x(v) = Im(conj(x) v)/(1+||x||²)`.

Its curvature is the quaternion-valued two-form `F=dA+A∧A`. At x=0, A=0 and

`F_0(v,w)=Im(conj(v)w-conj(w)v)=2 Im(conj(v)w)`.

Choose the two **source-derived** distinct directions `v=b=2` and `w=T b=1+i` from Main XIII. Exact arithmetic gives `F_0(b,Tb)=4i` (nonzero). The independent SymPy oracle differentiates `A` on the plane `x=s b + t Tb` to obtain the same result without importing the implementation. The usual quaternionic Hopf connection is the BPST SU2 instanton with nontrivial characteristic class; this is **classical** gauge geometry (not new gauge theory and not Einstein curvature). It is *not* proof the original time trajectory sweeps a two-parameter surface: the authentic source orbit n↦T^n b is only one-dimensional, so any smooth two-form pulled back to an actual one-dimensional path is zero. Our plane `s b + t Tb` is a declared counterfactual **probe family**, not the observed time history.

An exact rational Wilson-loop finite probe uses the unnormalized quaternionic link `L(x,y)=1+conj(x)y` for the chart section `(x,1)` and the rectangle `0,eps*v,eps*(v+w),eps*w,0`. The loop product is not identity for `eps>0`. For v=b, w=Tb, its imaginary i-component is exactly `4 eps² + 20 eps⁴` (unnormalized overlap), and reversing the loop conjugates the quaternion. Two independent source-span planes yield generally noncommuting loop factors. The unnormalized scalar/imaginary magnitudes depend on the normalization; the curvature coefficient and the conjugacy class of the normalized loop carry the invariant geometric information. Under arbitrary right local gauge choices link products conjugate at the basepoint, so the real trace or imaginary norm is invariant. **No measured gravitational holonomy is claimed.**

The odd chiral successor changes right versus left Hopf gauge; its two-step returns to the original chart and acts as a finite-order quarter-turn on S4. The full exact proof and hostile controls are imported in the frozen local dossier, not relabeled as a new discovery here.

### A new source-defined discrete chiral square — actual ordered quaternionic phase, no guessed plane

The two-parameter tangent plane above is useful but was freely interpolated. There is also an **exact finite four-vertex source square** using the original chiral successor T and original chirality J. The Main XIII source proves `TJ=JT`, hence for each `n>=0` the marked vertices

`X_n=T^n b`, `T X_n`, `J T X_n`, `J X_n`

form a closed T/J square. These are genuine points of the **decaying chiral source**, not independently fabricated marginal observations. The chart-section quaternionic overlap of successive vertices is `L(x,y)=1+conj(x)y`. Define the ordered Bargmann/Pancharatnam-type loop invariant

`W_n = L(X_n,TX_n) L(TX_n,JTX_n) L(JTX_n,JX_n) L(JX_n,X_n)`.

For `n=0` the four exact source vectors are `2`, `1+i`, `j−k`, `2j`, and Hamilton multiplication yields

`W_0 = 109 − 40i − 28j − 10k`, `||W_0||²=14365`, and the **gauge-invariant rational real-trace ratio** `(Re W_0)²/||W_0||² =11881/14365`.

This is a genuinely nontrivial source-composed quaternionic **relative phase** despite the commuting T/J state operations. Under vertexwise right quaternionic gauges, the complete overlap product is conjugated at its basepoint; its normalized real part (up to an orientation convention) is invariant. The independent SymPy oracle and standard-library Fraction code agree exactly. A finite Bargmann overlap is not automatically a path-ordered exponential of the smooth Hopf connection along some unique interpolating loop; we do not claim a physical gravitational or direct causal holonomy.

**Falsifying limit:** `||T^n b||²=4·2^-n`, and all four square vertices have norms at most `||T^n b||`. Each overlap differs from `1` in norm by at most `4·2^-n`; consequently

`||W_n−1|| <= (1+4·2^-n)^4−1`, which is summable in n.

Thus even this source-authenticated loop phase becomes **asymptotically trivial**, with no stand-alone signed Weyl cancellation. The same W_n arises for every alternative seed of the separate growing real BBP recurrence because it uses only the decaying source b,T,J. Therefore the existing coherent changed-seed control survives this stronger construction. Source-specific gauge curvature is mathematically real, but still has not reached the zero-seeded carry-selection gate.

## 4. Two exact general-relativity firewalls

**Firewall G1 — signature/topology:** S4 with its natural round metric is *Riemannian* (positive definite). A closed smooth manifold with nonzero Euler characteristic admits no smooth globally nondegenerate Lorentz metric. `χ(S4)=2`. Thus S4 itself cannot be a four-dimensional Lorentzian spacetime. Its punctured chart is R4 and can carry a locally chosen Lorentz metric, but no such global metric extends smoothly and nonsingularly to S4; alternatively `R × S3` supports familiar 3+1 Lorentz metrics, and `R × S4` supports a 4+1-dimensional Lorentz metric. A time coordinate, causal cones and metric field must be declared and validated, rather than inferred from circle factors or a Hopf projection.

**Firewall G2 — source adequacy and curvature type:** the BPST instanton curvature is an SU(2) *internal-gauge* curvature. GR's Riemann curvature is a tensor of the Levi-Civita connection on a Lorentzian tangent bundle. Nonzero F for the canonical Hopf bundle is not nonzero Einstein curvature; neither entails the other. The SUCC/Hopf construction supplies no stress-energy tensor, causal light cones, equivalence-principle derivation or physical clock observable. There is no mathematical basis for saying the physical simultaneity principle fails.

An even stronger no-go: the fixed source chiral Hopf two-step map is an order-four isometry, not a hyperbolic/chaotic or equidistributing dynamical system. The anchored latitude obeys a Möbius recurrence `B'=(3B-1)/(3-B)`. Writing `E=||x||²`, `B=(E-1)/(E+1)=tanh((log E)/2)` conjugates this nonlinear latitude map to a **uniform** shift `log E' = log E - log2`. Its apparent altitude-dependent rate is an exact coordinate-compression effect, not a newly derived gravitational time dilation. It is a useful control precisely because it removes the superficial relativistic illusion.

## 5. Four correlated Pisot directions: precise carrier, limitations and source gap

A degree-five Pisot unit θ solving `θ^5−θ^4−θ³−θ²−θ−1=0` provides four irrational phase directions `θ,θ²,θ³,θ⁴`. Reduction modulo 5 gives an exact irreducibility certificate:

`x^(5^5)≡x mod P(x)` and `gcd(P, x^5−x)=1` in `F5[x]`.

For a prime-degree polynomial this proves irreducibility over F5 and hence over Q. θ is a Pisot number: `(x−1)P(x)=x^5(x−2)+1`, and Rouché on radii `r>1` arbitrarily near 1, with `r^5(2−r)>1`, forces four non-leading roots of P strictly inside the unit circle while the unique >1 root stays outside. Therefore `1,θ,...,θ⁴` are Q-independent. Kronecker–Weyl yields a dense equidistributed orbit

`X_n=(e(nθ),e(nθ²),e(nθ³),e(nθ⁴)) ∈ T4`.

Its based smash quotient `T4/W ≅ S4` with fat wedge `W={at least one coordinate equals 1}` is a **topological** S4 observer. Prime powers `z→z^p` descend to S4 (degree `p^4`), while the torus SUCC rotation **does not** descend because W is not invariant under translation. Separately the quaternionic Hopf `S7→S4` is a *different* sphere model, with SU2 fibers; equating these two quotient maps or inserting the Pisot phases into the BBP readout without a source-preserving intertwiner is UNVERIFIED. Any irrational direction already makes a countable dense circle successor orbit; Pisot specificity is the contracting algebraic trace-return clock, not generic circle density.

## 6. Test matrix / claim ledger

| ID | Statement | Claim status | Adversarial control / next discriminator |
|---|---|---|---|
| AR-01 | Mixed harmonic/log prime clocks yield positive braid defect and exact n^-2 asymptotic | DISCLOSED (paper algebra + exact Fraction) | Coherent harmonic or log potential kills defect |
| AR-02 | Gamma is the accumulated harmonic–log clock mismatch; along Fibonacci time phi is the rate | CLASSICAL (telescoping+Binet) | Re-index/center choice changes intercept |
| AR-03 | Quadratic Pisot trace returns at exactly beta^-k | CLASSICAL (algebraic trace) | Irrational non-Pisot rotation still dense |
| AR-04 | True BBP chiral tap clock `16^n T^(8n)=I` and compact positive C_n→π/16 | SOURCE-EXACT (Main XIII identity) | Original seed and signed poles retained |
| AR-05 | Real BBP prime-scale commutator equals `(p−1)r(n+1)` | DISCLOSED (exact source arithmetic) | Same structural equation holds for any forcing |
| AR-06 | Hopf F_0(b,Tb)=4i; rational rectangle overlap is nonzero and orientation-sensitive | CLASSICAL connection + SOURCE-SPECIFIC DIRECTIONS | Collinear control zero; one-dimensional orbit cannot detect 2-form |
| AR-06B | Source T/J square yields exact quaternionic Bargmann invariant W0=109−40i−28j−10k, but Wn→1 summably | SOURCE-EXACT overlap + CLASSICAL gauge invariance | Same forcing changed real seed leaves it unchanged; signed Weyl gate OPEN |
| AR-07 | No global Lorentz signature on smooth S4 due χ=2 | CLASSICAL OBSTRUCTION | Use R×S3 or punctured S4 with explicit metric, not implicit GR |
| AR-08 | Finite two-step SUCC/Hopf map gives gravitational dilation/equidistribution | REFUTED (finite-order action; rapidity translation) | Need new authentic cross-time source and metric |
| AR-09 | All authentic BBP signed Weyl sums are o(N) | OPEN / UNVERIFIED | Actual zero-seeded carries, changed-seed hostile control |
| AR-10 | One sourced four-Pisot torus has a canonical quaternionic Hopf lift | UNVERIFIED | Explicit source-labelled intertwiner and right/left gauge check |

**Test authority:** The imported `hopf_source_exact.py` is preserved byte-for-byte; dedicated bridge tests compare it with actual Main XIII `rank_two_chiral_towers.py` only when a full worktree is available. Local isolated validation covers 55 direct old+new passed tests, plus 2 deferred bridge tests, one exact F5 irreducibility checker and an independent SymPy differential oracle. Two Main XIII bridge tests were *not executable in isolated local scratch*; CI on the new branch must execute them against the full checkout. No full native suite or GitHub CI has been performed at the time of this local report.

## 7. Verdict and next falsifying work

**Survives:** source-preserving Hopf observers, exact signed four-pole tomography with retained companion, two-chart parity transport, one coherent Pisot four-torus construction, and two mathematically distinct sources of apparent clock mismatch/holonomy. **Fails:** a single chart with autonomous odd Hopf successor; the inference from a nonclosed mixed clock to intrinsic physical curvature; and the inference from the compact S4 observer to global Lorentzian spacetime.

**Next decisive probe:** specify a *genuine* source-labelled two-parameter family using actual arithmetic source degrees of freedom, build a Hopf connection whose Wilson loops depend on the zero-seeded `U_n` carry and differ on the unchanged-forcing `U_0=−π/16` coherent control; then formulate a quantitative signed Fourier implication with uniform N savings. Without this, the construction remains nontrivial exact geometry but cannot solve π normality.

## Sources / provenance

- Main XIII integration PR #343: https://github.com/femboy2112/SUCC/pull/343
- Original source chiral PR #333 (code incorporated in Main XIII): https://github.com/femboy2112/SUCC/pull/333
- SUCC/FUCC source affine braid: `research/2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md`
- Main XII mathematical memory, corrected golden-gamma lineages: `docs/math_memory/INDEX.md` and PR #342.
- SU2 Hopf instanton connection: T. Waldron, J. London Math. Soc. 2022, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12672 (connection in chart).
- Classical four-sphere gauge charge: Clay Mathematics Proceedings, https://www.claymath.org/wp-content/uploads/2022/03/cmip011c.pdf
- Lorentz topology, Euler characteristic: https://link.springer.com/article/10.1007/s11005-026-02152-x
- Compact Lie quotient and Hopf fibration: https://link.springer.com/article/10.1007/s12220-022-00954-8
