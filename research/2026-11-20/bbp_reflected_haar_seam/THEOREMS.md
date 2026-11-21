# Reflected Haar source geometry: twelve exact theorem / crucible contracts

**Scope:** paper mathematics of the signed authentic BBP mask and explicitly declared auxiliary representations. Date: 2026-11-20. No academic priority claimed. `Q(t)` below is the Mellin numerator. `r(n)` remains unchanged. A root of `H` is not a rational BBP pole and is not automatically an attractor of π digit dynamics.

## RH-01. Source-selected factor circle and real involution (PROVED EXACT)

Original `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)` and `U0=0`. Its Mellin polynomial is

`Q(t)=4−2t³−t⁴−t⁵=(1−t)H(t)`, `H(t)=t⁴+2t³+4t²+4t+4`.

Direct multiplication gives

**`H(t)=(t²+2)(t²+2t+2)`**, roots `±i sqrt(2)`, `−1±i`, all simple with modulus `R=sqrt(2)` and left-semicircle arguments `π/2,3π/4,5π/4,3π/2`.

Substitution and expansion give the exact `2`-reciprocity

**`t⁴ H(2/t)=4 H(t)`** for `t≠0`.

For `t=R e^{iθ}`, the reflection `t↦2/t` equals complex conjugation. This reflection permutes both root pairs. It is an **involution**, not a contraction or an independently derived recurrence on a point representing a hexadecimal digit.

## RH-02. The four roots are an order-eight Fourier subset (PROVED EXACT)

With `w=t/R`, `w^8=1` at all four roots. More strongly,

**`t⁸−16=H(t)(t⁴−2t³+4t−4)`**.

The normalized root exponents are `m∈{2,3,5,6}` under `w=e^{2πim/8}`. The order-two character `χ4(w)=w⁴=(−1)^m` gives `+1` at `m=2,6` (`±i sqrt(2)`) and `−1` at `m=3,5` (`−1±i`). Complex conjugation `m↦−m (mod8)` preserves each character class. The character and its two classes are **source-filter root signatures**, not a claim that these frequencies occur as the actual real-phase frequencies of π.

## RH-03. Exact source-root algebra splitting by Haar-like parity projectors (PROVED EXACT)

Take the commutative four-dimensional algebra `A=Q[t]/(H)`. Since `t⁸=16` in `A`, `v=t⁴/4` satisfies `v²=1`. Define

**`e+=(1+v)/2`, `e−=(1−v)/2`**.

Then `e±²=e±`, `e+e−=0`, `e++e−=1`. Under the Chinese remainder isomorphism

`A ≅ Q[t]/(t²+2) × Q[t]/(t²+2t+2)`, 

`e+` corresponds to `(1,0)` and `e−` to `(0,1)`. The roots yield quadratic fields `Q(sqrt(−2))` and `Q(i)` respectively. Both ideals are source-selected and commute with the algebra's multiplication. These idempotents are the internal Fourier character projections of the source-filter **root algebra**; do not identify them with orthogonal projections on a physical Hilbert space without a specified representation and positive inner product.

## RH-04. A literal two-point Haar experiment on complementary arcs (EXACT CONDITIONAL MODEL)

Choose the LEFT semicircle of radius `R=sqrt(2)`, endpoints at angles `π/2` and `3π/2`. For any angular coordinate `θ∈[π/2,3π/2]`, its two endpoint distances are

`d+=R(θ−π/2)`, `d−=R(3π/2−θ)`, **`d++d−=L=πR`**.

Assume two coherent equal-magnitude input waves are independently transported to a **common calibrated receiver**, and choose an additional known relative phase `φ` and wavenumber `k`. Set

`v=(e^{ikd+}, e^{i(kd−+φ)})/sqrt(2)`;
`H2=(1/sqrt(2))*[[1,1],[1,−1]]`.

The output probabilities/intensities are

**`I±(θ;k,φ) = [1 ± cos(k(2d+−L)−φ)]/2`**, and `I++I−=1`.

At `k=2/R`, `φ=0`, the cosine is `cos(4θ)`. On **the four actual roots** this equals `χ4(w)=±1`, hence the `+` port occurs with unit probability on `t²+2` and the `−` port occurs with unit probability on `t²+2t+2`. Under an angular preparation error `|ε|`, the wrong-port intensity is `sin²(2ε)≤4ε²` provided the perturbed position stays in the declared arc. An unknown phase offset can swap ports (`φ=π`) or destroy discrimination; calibration is necessary.

**Physical boundary:** the two distances above are complementary endpoint geodesics, NOT automatically a specular mirror path to the same receiver. A literal reflected round trip from a wall at `L` back to a detector at zero has length `2L−s`, rather than `L−s`. A passive slit plus a mirror needs a scattering matrix, appropriate reference phases and a common interference endpoint; circular curvature alone does not specify wave energy, frequency or reflectivity. The result is an exactly realizable two-channel model, not evidence of a particular photon experiment or actual BBP-digit location on this circle.

## RH-05. The same two quadratic factors are the 11/5 split in the declared Fibonacci evaluator (PROVED EXACT)

For the PREVIOUSLY DECLARED SUCC auxiliary Fibonacci matrix `M=[[0,1],[1,−1]]`, `M²=I−M`, hence

`(M²+2I)=3I−M`, `M²+2M+2I=3I+M`.

Their determinants are respectively **`11` and `5`**, and their product is `det H(M)=55`. In fact `H(M)=[[8,1],[1,7]]`, recovering earlier PR #670. The `+` Haar root class is the `t²+2` factor (det11), while `−` is the `t²+2t+2` factor (det5). This is an exact shared-source polynomial/algebraic **label correspondence**. It does not authenticate the auxiliary Fibonacci evaluator as the actual π real-circle successor, nor guarantee transfer of a causal phase signal between the 11- and 5-adic places.

## RH-06. Exact eight-step contractive impulse of a source-derived inverse-mask filter (PROVED EXACT)

As a SEPARATELY DECLARED auxiliary scalar filter, let `A(z)=1/H(z)=Σ_(n≥0) a_n z^n`, analytic for `|z|<R`. The cyclotomic factorization gives

**`1/H(z) = (1/4−z/4+z³/8−z⁴/16)/(1−z⁸/16)`**.

Hence the first block is exactly

`(a0,...,a7)=(1/4,−1/4,0,1/8,−1/16,0,0,0)`, and

**`a_(n+8)=a_n/16` for every `n≥0`**.

Thus `b_n=R^n a_n` obeys `b_(n+8)=b_n`: **eight-step periodic normalized angular data with a strict radial `1/16` contraction per cycle**. Partial fractions further show `a_n=Σ_j c_j t_j^(−n)`, with all `|t_j^(−1)|=1/sqrt(2)<1`; these are stable inverse-root oscillatory modes. The exact H² norm is

**`Σ_(n≥0)|a_n|² = 37/255`**.

This is genuinely Pisot-*esque* only as an auxiliary stable oscillatory recurrence. The zeros of `H` are not fixed points of the original nonautonomous BBP real-phase dynamics; neither the inverse filter nor its convergence is automatically an allowable physical propagation law. Signed finite motifs are not automatically probability measures.

## RH-07. Source-specific *additional* winding-index jump (PROVED EXACT; CLASSICAL ARGUMENT PRINCIPLE)

For `ρ>0`, define the analytic circle symbol `q_ρ(z)=Q(ρz)` for `|z|=1`. The root positions are `t=1` and the four roots at `|t|=sqrt(2)`. Provided `ρ≠1,sqrt(2)`, the argument principle gives

**`wind(q_ρ,0)=0`** for `0<ρ<1`, **`=1`** for `1<ρ<sqrt(2)`, and **`=5`** for `ρ>sqrt(2)`.

For the Hardy Toeplitz operator `T_(q_ρ)` the index is `−wind`: **`0,−1,−5`**. At exactly the critical radii the symbol vanishes on the circle, so the Fredholm index is **undefined**, not a half-integer or a conserved physical charge. The first jump is the *DC-root* `t=1`; the extra source-selected jump of four comes from the simultaneous four-root circle. The individual quadratic factors contribute winding jumps of two each at `sqrt(2)`, resolved by RH-03/04. This is an **index of the chosen source-mask analytic multiplication operator**, not an index theorem about π digit statistics or the unilateral journal itself. It answers the request for a source-specific analytic winding **in this declared operator class**, beyond the universal chronology shift index, with the latter kept separately typed.

## RH-08. The same source supports a centered spectral quotient (PROVED EXACT)

Set `w=t/R`. The self-reciprocal normalized polynomial satisfies

`H(Rw)/4 = w⁴+sqrt(2)w³+2w²+sqrt(2)w+1`.

For `w≠0`, dividing by `w²` and setting `u=w+w^(−1)` gives

**`H(Rw)/(4w²)=u(u+sqrt(2))`.**

On `|w|=1`, `u=2cosθ`. Reflection `w↔1/w` identifies each conjugate pair; the four complex roots become the two REAL quotient values `u=0` and `u=−sqrt(2)`. These are root-coordinate values, **not** automatically attracting dynamical fixed points. A source-derived invariant `u` is not a physical attractor without a declared time update `u↦F(u)` and calibrated link to source trajectories.

## RH-09. The matched-leading-jet mutant breaks the common circle and Haar root identity (EXACT HOSTILE)

Take the previously admitted original-source mutant `Q*(t)=Q(t)+(1−t)²=(1−t)H*(t)` with `H*=H+1−t=t⁴+2t³+4t²+3t+5`. It retains `Q*(1)=0` and `Q*'(1)=Q'(1)=−15`, but

`t⁴ H*(2/t)−4H*(t)=t⁴−2t³+4t−4 ≠0`.

It cannot even have all four roots on **any** common circle. To prove this without relying on numerical root finding: for real monic `P(t)=t⁴+a t³+b t²+c t+d` with all roots on a circle `|t|=R`, root conjugation/reciprocity gives `t⁴ P(R²/t)=dP(t)`, hence `R⁴=d` and `c=aR²`; therefore necessarily `c²=a²d`. For `H*`, `c²=9` while `a²d=20`. Contradiction. Thus the original single-radius four-root jump and exact port classification are **not generic consequences of Q(1)=0 and Q'(1)=−15**. The mutant still has an analytic winding by ordinary root counting, not the same two-scale pattern.

## RH-10. Fourier symmetry is not source-to-phase dynamics (REFUTED SHORTCUT)

The original four-pole forcing, source mask `Q`, root algebra, reciprocal symmetry, `1/H` impulse, winding, Haar root port assignments and prime-filter determinants are all unchanged by the explicit homogeneous counterseed `s=−π/16`. But its completed real orbit is `Y_n=16^n(π/16+s)=0` for all n. This seed violates the authentic `U0=0` root selector; the control defeats **only source/seed-blind claims** that RH-01–08 force R0 or π normality. A shift `s=1/16` further aliases all later circle phases while differing in unwrapped seed. Existing #677 emphasizes that a source-only journal can have infinite Hankel rank with a locked completed real orbit. No map from actual hexadecimal digit state `θ_n={16^nπ/16}` to this four-root arc is established.

## RH-11. Conservation is properly typed (EXACT)

The two-point Haar transform is unitary and conserves its explicitly normalized input Hilbert norm. The optional inverse mask `1/H` is dissipative/contractive in its response coefficients (a_(n+8)=a_n/16), not a unitary carrier and not energy conservation. The chronologically retained BBP journal still satisfies the original `P_n+G_n(1)=π/16` but conserves this *scalar source value*, not an unspecified thermodynamic entropy. Normalized geodesic arc length `L=πR` is geometric and does not by itself imply constant kinetic energy or quantum reflection amplitudes. No Bose-Einstein condensate, nonclassicality or physical superfluid mechanism is inferred.

## RH-12. Actual source-to-real-phase gate (UNVERIFIED)

A substantive π theorem would require a **source-authenticated, forward-accessible map** from the actual original-zero-seeded BBP arithmetic history (four signed poles, full prime/cofactor, integer carry, exact terminal tail) into the circle-root parity observer or a related signed two-path witness. It must preserve the actual real phase and calibrated reference instead of mapping arbitrary phases to chosen roots, and must be independent of the target Weyl shell. Then prove a positive, uniform signed correlation or geometric domain-wall lower bound on EVERY sufficiently late shell; retain the wrong-seed, mutant, clock/frame and finite-terminal controls. Neither a two-port root sorter, topological index jump, signed impulse motif nor correct Gaussian smoothing currently proves R0, base-16 π normality or RH.

### Verdict

**PROVED within declared polynomial/filter/observer domains:** RH-01–09/11; classical antecedents include algebraic CRT, two-point Fourier/Haar, Hardy shifts, Toeplitz index/winding, analytic stable linear filters. **REFUTED:** direct source-root-to-π-orbit interpretation without a source-faithful factor map, naive constant-energy curvature inference, common-circle conclusion from DC root or leading jet alone. **UNVERIFIED:** source-selected all-shell real-phase transfer, physical superfluid analogy, and uniqueness of this mathematical representation among all possible source-filter constructions.
