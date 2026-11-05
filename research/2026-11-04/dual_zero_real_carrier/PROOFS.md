# Operation Dual Zero × Cayley R-Support — exact rational/real carrier for the original BBP source

**Research date:** 2026-11-04. **Provenance:** additive descendant of SUCC #500 at `bf103c4a25bbd83b6cfbad1dd77895928300ddd9` (which contains #499/#497 and restored primal code). Parallel Gamma Prybar #501 is *read-only context*, not an incorporated ancestry. The original four signed BBP poles, literal `U_0=0`, historical theorem contracts, old Lean and main are unchanged. The first projector/Cayley/cyclotomic identities were derived **before** this round's GitHub preregistration and were marked developmental, never passed off as blinded discovery. The independent finite holdouts were tested afterward.

**Status:** DZ-01–09 are elementary/classical paper identities applied to the authentic SUCC source and calibrated by exact tests, NOT a proof of π normality or a world-first theorem. The exact tangent degree is classical (Calcut, *Rationality and the Tangent Function*, Proposition 2). The source-dependent exponential rates inherit paper-proved but externally unrefereed SUCC #497/#499 arithmetic theorems. The original signed fixed-frequency Weyl, source-selected `J=o(K)`, signed completed Weil form, RH and π normality are all **OPEN**.

## Source and two meanings of zero

Let `e(x)=exp(2πi x)`. For an odd integer `M>=3`, put `H_M=Z/MZ`, and let `|a>` be the standard basis of `C[H_M]`. On this space

- `X|a>=|a+1>` (shifts source position), `Z|a>=e(a/M)|a>` (measures character);
- `|u_M> = M^{-1/2} Σ_a |a>` is the *uniform ensemble vector*, not any actual SUCC orbit;
- `P_freq0=|u_M><u_M| = M^{-1} Σ_j X^j` is the trivial Fourier-mode projector;
- `P_phase0=|0><0| = M^{-1} Σ_h Z^h` is the source phase-zero projector.

The two universal characters `e(0*a/M)=1` and `e(h*0/M)=1` are two different evaluations of the same bi-character. They are NOT equal projections.

### DZ-01 — Exact dual-zero interference/projector theorem

Character orthogonality proves both projector formulas. The discrete Fourier transform `F_M` interchanges them (for the declared `+` exponential Fourier convention; either orientation gives the same projections). Both have trace one and rank one, but

```
tr(P_freq0 P_phase0) = 1/M,
P_freq0 P_phase0 P_freq0 = P_freq0/M,
P_phase0 P_freq0 P_phase0 = P_phase0/M,
||[P_freq0,P_phase0]||_HS² = 2(M-1)/M².
```

Proof: `|<0|u_M>|²=1/M`; sandwich formulas for rank-one projectors are immediate. In the two-dimensional span of `|0>` and `|u_M>`, the commutator has squared HS norm `2s²(1-s²)` with `s²=1/M` and vanishes elsewhere. For `M>1` the projections do NOT commute. The product is literally a finite sum over alternative position/character paths, but it is a **classical finite character sum**, not a quantum path integral or a proof of source-selected Haar mixing.

**Precision:** although both zero conventions produce scalar `1`, their overlap tends to **zero**, not one, as M→infinity. This is the first obstruction to treating a trivial frequency and a phase-fixed source as the same universal state.

### DZ-02 — Rational and real Cayley interval carrier, including reciprocal arctangent

For `t∈R∪{∞}=RP^1(R)` define the *algebraic circle map*

```
C(t) = (1+i t)/(1-i t),   C(∞)=-1.
```

For finite t it is `exp(2i arctan t)`. The inverse for `z != -1` is `t=-i(z-1)/(z+1)`. It is a homeomorphism `RP^1(R) -> S¹` (the source has to declare circle orientation, not an observed Haar law). Its rational restriction is a bijection `RP^1(Q) -> S¹(Q)`, where the codomain means points whose real and imaginary coordinates are rational. Indeed, for reduced t=m/n,

```
C(m/n) = (n²-m²+2imn)/(n²+m²).
```

If an odd p≡3 mod4 divided `m²+n²`, then `-1` would be a square modulo p unless p divided both m,n, contradicting coprimality. If m,n both odd, `m²+n²≡2 mod8` and the numerators are both even, so the factor 2 cancels. Hence every *reduced coordinate denominator* of a rational Cayley point is ODD and its odd primes are all `1 mod4`—the classical Gaussian split-prime filter. This applies to the rational **chart coordinate**, not automatically to SUCC's actual source phase.

For t>0,

```
arctan t + arctan(1/t) = π/2,
C(1/t) = - C(t)^(-1).
```

The first identity is exact with the principal real branches; for t<0 the arctangent sum is `−π/2`, with the same circle equation. The four rational unit-interval charts `C(u)`, `C(1/u)`, `C(−1/u)`, `C(−u)` for u∈[0,1] cover the oriented four quarter arcs, with endpoints 1,i,−1,−i,1 and the appropriate chart orientations. The infinity endpoints are real/projective, not silently identified with zero inside Q.

### DZ-03 — Source phase → cyclotomic real algebraic tangent (exact degree)

Let the **actual** source phase be `x=a/M mod1` in lowest terms with odd `M>1`, and `ζ=e(x)`, a primitive M-th root. Its *correct* Cayley tangent coordinate is

```
t(x) = tan(πa/M) = -i (ζ-1)/(ζ+1).
```

`ζ != -1` since M is odd; this coordinate is real and finite. Let `K=Q(i,ζ)`. Conversely `ζ=(1+it)/(1-it)`; therefore `K=Q(i,t)`. Since `M` is odd, `i∉Q(ζ)`: otherwise `Q(ζ,i)` would contain a primitive 4M-th root, contradicting `φ(4M)=2φ(M)>φ(M)`. Hence `[K:Q]=2φ(M)`. Because t is real, `[Q(i,t):Q(t)]=2`. Thus **for every reduced odd M>1**,

```
[Q(t(x)):Q] = φ(M).
```

For M=1, t=0 and degree1. This is an application of **classical** cyclotomic degree theory, not a novel irrationality proof; see J. S. Calcut, *Rationality and the Tangent Function*, Proposition 2, https://www2.oberlin.edu/faculty/jcalcut/tanpap.pdf . An exact **integer** polynomial certificate for t, with no pi digits as an input, is

```
R_M(T)=(1−iT)^φ(M) Φ_M((1+iT)/(1−iT)),
```

which lies in `Z[T]`, is irreducible and has degree φ(M) for odd M>1. `R_3(T)=3−T²`; `R_5(T)=T⁴−10T²+5`; `R_35` has degree 24. **The source's integer numerator a/M determines the correct real root/branch; the polynomial alone has φ(M) competing roots.** That is a legitimate observer-source selection obligation, not an oracle for π digits.

**Crucial false chart:** For the primal's first state `Y_1=109/35`, its source circle phase is `4/35` and its *true* tangent is algebraic irrational of degree 24. The **different** rational chart point `C(4/35)=(1209+280i)/1241` with `1241=17·73` is not the original phase `e(4/35)`: one lives in `Q(i)`, the other has root-of-unity order35. The latter requires `tan(4π/35)`, not t=4/35.

### DZ-04 — Actual BBP source algebraic-degree asymptotics and zero-projector overlap

Let `D_N^U=den(U_N)` and `D_N^Y=den(Y_N)` for the actual unwrapped **zero-seeded** original and `χ_-4`-primal states. Both are odd (the source and the primal have explicit odd forcing denominators). Every prime dividing either D_N comes from some source rational denominator of size at most `8N`, because integer radix multiplication adds none. For any such odd D,

```
0 <= log(D/φ(D))
   = sum_{p|D} log(p/(p−1))
  <= sum_{p|D}1/(p−1)
  <= H_(8N−1) <= 1+log(8N).
```

Thus the **exact all-N inequality** is `D/[e·8N] <= φ(D) <= D` for N≥1. Inherit #497's paper source theorem `log D_N^U=(6+o(1))N` and #499's `log D_N^Y=(8+o(1))N`. Then the source-selected REAL tangent coordinate's algebraic degrees obey

```
log deg_Q tan(π U_N)  = (6+o(1))N,
log deg_Q tan(π Y_N)  = (8+o(1))N.
```

On its **instantaneous minimal** finite cyclic carrier `C_D`, the exact two-zero projector overlap is `1/D`, so the *negative log overlap* has exactly the same exponent 6N or 8N. This is a cross-typed equality of **growth rates**, not a probability of actual source truth, digit entropy, coherent quantum amplitude, or source-selected signed cancellation. For time-compatible carrier inclusions use the cumulative `M_N=lcm_{j<=N}den r(j)` instead of the possibly nonnested D_N.

### DZ-05 — Reciprocal chart forces a new 2-primary interface

If x=a/M mod1 is reduced, M odd, and t=tan(πx), the reciprocal chart has phase

```
x' = 1/2 − x mod 1,
C(1/t)=e(x')= -conj(e(x)).
```

Its reduced denominator is **exactly 2M**, because M−2a is odd and coprime to M. Hence reciprocal arctangent gluing does NOT act internally on SUCC's original odd-denominator rational phase carrier. It requires a declared 2-primary extension, preserving the old odd arithmetic component. For every integer h,

```
e(hx') = (−1)^h conjugate(e(hx)).
```

The absolute Weyl sum and triangular collision energy are unchanged under this global circle reflection. The real half-turn parity `(−1)^h` is an **additive circle character**; it is *not* the multiplicative Dirichlet character `χ_-4(p)` used by the prime-character source quotient. A source-specific signed mixing estimate cannot be conjured from this symmetry alone.

### DZ-06 — Exact naturality of the finite Fourier projector under conductor refinement

For odd M|M'=kM, inject the old basis via `ι|a> = |ka>` into the larger cyclic carrier. With

```
(F_M f)(h) = M^(−1/2) Σ_a e(ha/M) f(a),
```

the exact diagram satisfies

```
(F_M' ι f)(h) = sqrt(M/M') (F_M f)(h mod M).
```

Proof: substitute the subgroup support, factor out 1/sqrt(M') and compare with the old Fourier normalization. Its squared scale is M/M'. The finite Haar unit `|u_M>` becomes uniform on a SUBGROUP under ι, not `|u_M'>`. Thus finite-source conductor growth does NOT canonically select Haar on the completed circle; its Fourier transform has alias copies that must be controlled. The family of uniform probability measures on the entire cyclic groups does converge weakly to real Haar as M→∞, but this is a different **ensemble** from the time-selected SUCC source.

### DZ-07 — Gamma angular kernel is the *quarter-Haar Jacobian*, not selected Haar

The real/Cayley circle angle is `θ=2 arctan t`. Differentiation gives the exact normalized Haar reference on the compactified real line:

```
C^* (dθ/(2π)) = dt/[π(1+t²)] ,  t∈R.
```

The point at ∞ has zero Haar mass. Each of the four unit-interval charts in DZ-02 carries Haar mass 1/4, with `∫_0^1 dt/(1+t²)=π/4`. SUCC's prime-derived primal transfer is exactly

```
K_ang(t)=4/(1+t²)
```

after its source-marked `t=1-x` reversal. Therefore `K_ang(t)dt/π = 4dt/[π(1+t²)]` on [0,1] is exactly **Haar conditioned to the first quarter-arc**. This equality is between classical deterministic measures and the **complete scalar BBP kernel**, NOT a distribution theorem for actual chronological Y_n. Uniform u sampling on [0,1] has mean 1/2, while this quarter-Haar density has mean `2 log 2/π<1/2`; a uniform interval grid is NOT a Haar sample without the Jacobian. In particular a bounded empirical histogram or flat measure density cannot be supplied to SUCC's observer as an unearned premise.

### DZ-08 — Full original source on real projective tangent carrier, with exact rational dynamic formula

Let `x_n={Y_n}` or `{U_n}`, with exactly the same genuine forcing `r(n+1)` and literal zero seed as its chosen source; take `t_n=tan(πx_n)` and `s_n=tan(πr(n+1))` as algebraic real source coordinates. Put

```
A16(t)+i B16(t) = (1+it)^16,
A16(t)=Σ_{k=0}^8 (−1)^k binom(16,2k) t^(2k),
B16(t)=Σ_{k=0}^7 (−1)^k binom(16,2k+1)t^(2k+1).
```

Because the Cayley map takes rational tangent addition to multiplication on the unit circle, the source-forced recurrence is **EXACTLY**

```
 t_(n+1) = [B16(t_n)+s_n A16(t_n)] / [A16(t_n)−s_n B16(t_n)]
```

as an equality in `RP^1(R)`, including the projective pole case. In parallel retain the unwrapped integer/rational U_n (or Y_n) and literal carry—this circle/tangent chart does not replace the source's integer lift. Every coefficient of the rational dynamical map is an integer; its sole forcing parameter s_n is an algebraic number determined from the authenticated rational source by DZ-03. No π digit sequence, normality, Haar, or arbitrary sample path is used as construction input.

The reference Cauchy measure is invariant under each such real map because `×16` is a circle covering preserving Haar and multiplication by the source-forcing phase is a circle rotation. **But invariance does not establish mixing of one trajectory**: the unforced fixed phases `1/3`, `1/5`, `1/15` yield irrational fixed tangent coordinates whose exact cyclotomic minimal polynomials divide `B16(t)-tA16(t)`. This is an all-integer algebraic negative control, not a floating test.

### DZ-08b — Endogenous radial null as the decisive anti-Haar witness

The SAME authentic original BBP source's radial complement `Z_N=U_N−Y_N` is STRICTLY positive with `0<Z_N<1/(32N+16)` for every positive N (#499). Europa #500 independently reports `log den(Z_N)=(8+o(1))N` and its matching pair-denominator survival. Therefore the EXACT cyclotomic tangent coordinates `tan(π Z_N)` have algebraic degrees `exp((8+o(1))N)` by DZ-03/04, and the corresponding *two-zero finite-projector overlap* is `exp(−(8+o(1))N)`; nevertheless their REAL phases converge to zero and their empirical measure tends to the Dirac mass at the circle origin, not Haar. This is an actual, zero-seeded, within-source, **signed channel** control, not a mutated source or a random Galois average. A successful new zero-naturalness argument must distinguish angular Y from radial Z by source orientation, not by denominator growth, cyclotomic degree or unit-normalization alone.

### DZ-09 — A legitimate real-observer equidistribution gate (equivalent, not proved)

For real/projective empirical measures `ν_A=A^{-1}Σ_{A<=n<2A} δ_{tan(πY_n)}` on `RP^1(R)`, the Cayley homeomorphism gives

```
ν_A -> Cauchy(dt/[π(1+t²)]) weakly
     iff A^(-1)Σ_{n=A}^{2A-1} C(t_n)^h -> 0 for every integer h !=0
     iff source-selected angular fixed-h Weyl decay on epochs.
```

The analogous full-prefix and original/primal comparisons are already handled by SUCC's Weyl transport. This is a source-faithful coordinate change, NOT an independent route to the open decay. The reference Cauchy distribution has *no absolute first moment*, so a supposed proof through polynomial moments on the noncompact R coordinate is invalid unless appropriately truncated/bounded or reexpressed on compact `RP^1(R)`. Its correct test space consists of bounded continuous functions on the compactification. The Cauchy reference is obtained from the **declared circle geometry**, never inferred from finite source histograms.

### Resulting claim ledger

| Claim | Status and prior art | Missing for π |
|---|---|---|
| DZ-01 | Classical finite Fourier, exact projector compositions | Selected temporal off-diagonal signed cancellation |
| DZ-02 | Classical stereographic/Cayley Gaussian rational atlas; explicit split/inert denominator filter | Source map into *actual* cyclotomic phase, not guessed rational tangent |
| DZ-03 | Classical Calcut/tangent cyclotomic degree; exact branch selection | Source-specific real mixing law |
| DZ-04 | New-to-SUCC composition with #497/#499 paper denominator asymptotics | Galois degree/prime mass is NOT Haar entropy |
| DZ-05 | Classical reciprocal arctangent, new typed 2-primary SUCC boundary | Directed source asymmetry preserved after reflection |
| DZ-06 | Exact finite Fourier refinement map | Source-selected phase orientations not uniform ensemble |
| DZ-07 | Classical Haar Jacobian + *existing* SUCC Gaussian primal | Scalar period measure not time-orbit law |
| DZ-08 | Exact tangent-angle conjugacy of authentic source | No spectral-gap/mixing deduction, periodic hostile controls |
| DZ-09 | Classical homeomorphic weak-* transport | All-horizon original selected Weyl saving OPEN |

**Explicit next verdict-changing task:** Transport the signed `0-frequency-row versus phase0-column`0 commutator through the *ACTUAL, ZERO-SEEDED chronological source* and derive a new bound on the source-selected (not ensemble) nontrivial character amplitudes. Calibrate against real-algebraic fixed points, radial π-null projection, prime-cofactor CRT ghost and coherent wrong seed. Unless a source-dependent inequality rejects all of them for an authenticated reason, no further "zero naturality" or "arctan chart" identity advances π normality.

### Primary provenance and citations

- SUCC source: PR #500 Europa Weyl README, source-selected finite Weyl form; #499 PRIMAL_QUOTIENT_THEOREM; #497 selected prime saturation; original Oct26 TWO_QUADRATIC_ATOMS; #501 Prybar is sibling context only.
- J. S. Calcut, *Rationality and the Tangent Function*, Sections 2–3, especially Proposition 2 (exact cyclotomic tangent degrees): https://www2.oberlin.edu/faculty/jcalcut/tanpap.pdf
- NIST DLMF §§4.23–4.24 (arctangent and tangent addition): https://dlmf.nist.gov/4.24
- Classical Fourier/Pontryagin duality and finite Fourier representations; these methods are not claimed new.
