# Operation Minimum Geometry — the circle's one-kernel proof forge

**Date:** 2026-10-24. **Claim authority:** classical harmonic analysis and explicitly derived paper theorems, independently exact-tested finite oracles. **Not a proof of π normality or RH.** Scholarly novelty of the source-conditioned synthesis **UNVERIFIED**. No new Lean theorem or physical measurement.

**Pinned research parent:** SUCC Academic Main IX draft PR #250, `f986507851e34636f60bee657dcdf0771a934380`, `main` remains unmodified. This parent integrates the authenticated Circle Genesis, circle-time Kummer, Gamma/prime-carry, Duck and Secondary Circle sources. More recent **siblings** #252–#258 (actual BBP Green, Galois clocks and signed high-mode source) were inspected, **not silently merged**. Imported sources, source authorities and historic receipts remain untouched. Repository instructions: `AGENTS.md`, `docs/METHOD.md`, Academic Main IX integration report.

## 0. Steelman and falsifiable target

The author's “nature takes the stupidly clever minimal path” is tested as a **minimum-sufficient geometric action**: can one simple interaction from the metric circle (i) characterize the right global statistical geometry, (ii) construct it deterministically at low complexity, and (iii) force it on the **specific π-generated base-b arithmetic successor**?

(i) and (ii) are proved here. (iii) remains **UNVERIFIED**. The actual source-specific property needed is quantified below as an excess-potential bound; it is not automatically implied by metric circularity, degree-p maps, commuting diagrams, short programs or the arithmetic identity C/D=π.

Let `T=R/Z`, `z(t)=exp(2πit)`, squared chord `q(t)=|1-z(t)|²=2−2cos(2πt)`. For `b>=2`, the exact target orbit is `z_j=z(b^j α)`. Pi uses the **dimensionless phase** `α={π}`; angle π radians on the physical circle corresponds to phase 1/2 and is not the target. All circle maps `z -> z^n`, and chord polynomials `F_n(q(t))=q(nt)`, already exist in Circle Genesis #247.

## PGM-01. One rational chord kernel simultaneously contains Poisson, Gamma and all primes (CLASSICAL)

Choose the disk Poisson radius `r=1/2`, equivalently heat/height `t=log2` for the first-order spectral generator `|D|=(-d²/dθ²)^(1/2)` on the normalized circle. The resulting kernel is the **single chord expression**

`K(z,w)=3/(1+2|z-w|²)=(1−r²)/(1−2r cos(arg(z/w))+r²)`.

Its absolutely and uniformly convergent Fourier expansion is

`K(z,w)=1+2 Σ_(h>=1) 2^(−h) cos(h arg(z/w))`.

This is the classical Poisson semigroup `e^(−t|D|)` kernel. For general `t>0`, write

`P_t(x)=1+2 Σ_(n>=1)e^(−tn)cos(2π n x)`.

For `Re(s)>1`, Fubini/dominated convergence gives the **same circle source's spectral Mellin bridge**:

`∫_0^∞ t^(s−1)(P_t(x)−1)dt = 2 Γ(s) Σ_(n>=1)cos(2π n x)n^(−s)`.

At geometric origin x=0 this reduces to `2 Γ(s) ζ(s)=2 Γ(s) ∏_p(1−p^(−s))^(−1)` in the Euler product domain. Thus one Poisson semigroup links circle/chords, Gamma, integers and complete primes. At `x={π}` the cosine series is **additively phase-twisted** and has NO independent naive Euler product: PR #229's corrected mixed-phase cocycle is still indispensable. The ζ identity at x=0 is not a normality theorem for the x=π orbit.

**Source provenance:** Katznelson, *Introduction to Harmonic Analysis*, Poisson series; NIST DLMF §1.15(iii); classical Mellin of the exponential and Euler unique factorization. Energy minimization/positive definite kernels: Bilyk–Matzke–Vlasiuk (2022), arXiv:2110.04138. None is an originality claim.

## PGM-02. One fixed geometric scalar is equivalent to full normality (CLASSICAL, paper proof)

For any Borel probability μ on T, define

`E(μ)=∬K(z(x),z(y))dμ(x)dμ(y)`.

Absolute Fourier convergence, positivity and Fubini give the **exact sum of squares**

`E(μ)=1+2Σ_(h>=1)2^(−h)|μ_hat(h)|²`.

Hence `E(μ)>=1`, and `E(μ)=1` iff every nonzero Fourier coefficient vanishes, iff `μ=Haar`. This is the unique minimum, strictly convex along distinct probability measures.

For the actual orbit empirical measures `μ_N^α=N^(-1)Σ_(j<N)δ_(T_b^j α)` define

`E_N(α)=1/N² Σ_(j,k<N)3/[1+2q((b^j−b^k)α)]`.

**Theorem:** For any fixed integer b>=2 and any real α,

`α is normal in base b  <=>  E_N(α)->1`.

Proof, `=>`: Weyl gives `A_(h,N)(α)->0` for each fixed h and the Fourier weights are summable, so dominated convergence. Proof, `<=`: for each h>=1,

`|A_(h,N)(α)|² <= 2^(h−1)(E_N(α)−1)`.

The energy limit kills every fixed frequency; Weyl finishes. **No growing frequency band is necessary**, unlike a Fejér band; the one rational chord function includes every harmonic with positive (but exponentially decreasing) weight. There is still no uniform finite numerical gap separating Haar from arbitrary non-Haar measures (PGM-08).

## PGM-03. Exact Haar-origin benchmark for any expanding base (PAPER/CLASSICAL)

For every N>=1 and b>=2, with initial x Haar-uniform,

`∫_T E_N(x) dx = 1+2/N`.

Proof: diagonal pairs contribute K(0)=3. For j≠k, `(b^j−b^k)x` is Haar-distributed because its multiplier is a nonzero integer, so the expected pair kernel is `∫K=1`. Therefore the integral equals `[3N+(N²−N)]/N²=1+2/N`. This is an *ensemble expectation*, not an estimate for the selected π phase.

For a finite uniform m-gon and any h, the exact root-of-unity average of `|A_(h,N)|²` is `N^(−2)` times the count of pairs `(j,k)` satisfying `m | h(b^j−b^k)`. If `m>H(b^(N−1)−1)`, every frequency `1<=h<=H` has the **exact diagonal** mean `1/N`. An exact band and geometric-tail interval is implemented. The selected vertex x=0 instead always has `E_N(0)=3`. Spatial Haar fairness does not select a generic source orbit.

## PGM-04. Deterministic *minimal* geometry: an exact rational greedy builder (PAPER)

Let `z_0` be any circle point and `Φ_n(z)=Σ_(j<n)K(z,z_j)`. The Haar average is exactly n:

`∫ Φ_n(z) dHaar(z) = n`.

Since Φ_n is continuous and nonconstant for every nonempty finite sample, the open set `{z:Φ_n(z)<n}` is nonempty. Rational Pythagorean circle points

`z(t)=((1−t²)/(1+t²), 2t/(1+t²)), t∈Q`, plus `−1`, are dense. Thus an exact rational arithmetic search **terminates for each n** and can choose `z_n` with `Φ_n(z_n)<=n`, even without access to trigonometric values or random draws.

Let `S_N=N²E_N`. Its update under a chosen next point is

`S_(n+1)=S_n+2Φ_n(z_n)+K(0) <= S_n+2n+3`.

Base `S_1=3`. Induction yields

**`E_N <= 1+2/N` for every N>=1**, so the deterministic rational-circle point sequence is equidistributed. This is a general kernel-herding/greedy-energy phenomenon, not a novel physical law. The exact Python implementation uses `Fraction` and refuses exhausted finite search budgets; the paper search is unbounded but each step terminates.

**Interpretation:** a computationally simple *free-choice* circle dynamics produces Haar statistics without randomness. Its energy bound exactly matches the Haar-origin **expected** energy from PGM-03. The point-choice freedom is fundamental: a base-b digit successor has only ONE lawful next state and is NOT allowed to switch to the current greedy minimizer.

## PGM-05. Exact action-regret identity and equivalent asymptotic criteria (PAPER; converse added)

For an arbitrary actual path `z_0,...,z_(N-1)` define the source-action **signed** excess

`a_n=Φ_n(z_n)−n`, `n>=1`, and `a_0=0`.

Counting unordered pairs once yields the exact identity

**`E_N=1+2/N + (2/N²)Σ_(n=1)^(N−1)a_n`.**

Thus a given base-b point α is normal iff `Σ_(n<N)a_n=o(N²)` (the equivalence itself is another form of PGM-02; not a new π proof).

Let `r_n=max(0,a_n)`, and the stronger true geometric regret `ρ_n=Φ_n(z_n)−min_z Φ_n(z)>=0`. Because `min_zΦ_n<=n`, `a_n<=ρ_n`, so

`1 <= E_N <= 1+2/N +(2/N²)Σ_(n<N)r_n <=1+2/N+(2/N²)Σ_(n<N)ρ_n`.

**Sufficient source criterion:** if the actual π-selected T_b orbit satisfies `Σ_(n<N) r_n = o(N²)` (or the pointwise larger minimum-relative regret sum is subquadratic), then π is base-b normal. A power bound `Σ r_n = O(N^(2−δ))`, `0<δ<=1`, implies `E_N−1=O(N^(−δ)+N^(−1))` and for each fixed h, `|A_(h,N)|=O_h(N^(−δ/2))`. **Neither regret estimate is currently proved for π.** Merely declaring nature minimizes effort supplies no bound.

**Converse correction, SCE-01 (2026-10-24):** both subquadratic regret conditions are also necessary for normality. The sharp uniform bound `|Φ_n(z)/n−1|² <= 2(E_n−1)` follows from weighted Fourier Cauchy–Schwarz. Thus `E_n→1` makes each positive or minimum-relative regret `o(n)`, and weighted Cesàro summation makes either cumulative sum `o(N²)`. All these asymptotic criteria are equivalent. Their different finite/rate bounds remain useful, but the positive-part formulation alone does not escape the original theorem. See [full proof and a different collision-entropy sufficient target](PI_SOURCE_COLLISION_ENTROPY.md).

## PGM-06. π's actual first action is NOT a literal greedy minimizer (REFUTATION)

At n=1 the potential `Φ_1(z)=K(z,z_0)` has its unique minimum at the antipode `z=−z_0`, where K=1/3. Under binary expanding dynamics the forced successor is `z_1=z_0²`, so the first step is antipodal **only if** `z_0=−1`, i.e. starting phase α=1/2. But α={π} is irrational and unequal 1/2. Hence π's first binary successor is not the minimizer. This kills the naive `π chooses each geometric successor by immediate greedy minimization` mechanism **without rejecting subquadratic cumulative excess**.

Additionally, independently Machin-checked Wallis/Kummer intervals and outward rational cosine Taylor certificates on the actual π-selected orbit establish `E_4(π)>3/2` and `E_6(π)>4/3`. By PGM-03 these exceed the finite Haar-origin expectation at those horizons. Accordingly the exact cumulative signed excess is positive at N=4 and N=6. These are **finite source-certified exceptions**, not failures of possible N→∞ normality or a proposed asymptotic regret condition.

## PGM-07. One initial chord suffices to reconstruct the full future energy (PAPER)

Circle Genesis provides `F_m(q(z))=q(z^m)`, `F_m◦F_n=F_mn`. The actual orbit pair difference factors as

`b^j−b^k = b^k(b^(j−k)−1)`, `j>k`.

Therefore

`q(z(b^j α),z(b^k α))=F_(b^j−b^k)(X_α)=F_(b^k)(F_(b^(j−k)−1)(X_α))`,

where `X_α=q(z(α))` is **one scalar**. In particular the *entire sequence* `E_N(α)` is a deterministic rational-polynomial functional of this initial chord and the authorized multiplier b, without an orientation label. The Python independent fast-Chebyshev implementation exactly agrees with direct `Q[i]` circle powers for multiple bases and rational Pythagorean sources.

This is **target-sufficient** information for normality/energy, not a complete faithful quotient for arbitrary translations or complex phase-observation actions. The earlier carry-safe source/future-information constraints are retained.

## PGM-08. A single nonnormal orbit can look arbitrarily energy-perfect (REFUTATION + EXACT FORMULA)

Let `α_r=1/3^r`, r>=1, in base 2. By the lifting-the-exponent valuation `v_3(4^(3^k)−1)=k+1`, 2 is a primitive root modulo every `3^r`, and the selected orbit has period `2*3^(r−1)` and is uniformly distributed among the units modulo 3^r. It is therefore periodic and nonnormal.

Set `s=3^(r−1)`, `q=3s`. Ramanujan's primitive q-root character sum, normalized by φ(q)=2s, is 1 when q|h, −1/2 when s|h but q∤h, and 0 otherwise. Substitution into the exact Poisson square-energy formula gives

**`lim_(N→∞) E_N(α_r) = 1 + 1/[2(2^s−1)] + 3/[2(2^q−1)]`.**

Every limit is **strictly above 1**, but the deviation tends extremely rapidly to zero as r grows. Already r=4 gives a strictly nonnormal selected orbit with limiting energy gap <10^(−8). Independent integer cyclotomic reduction against Φ_(3^r) proves 244 finite root identities; no approximate roots are used.

**Verdict:** One fixed geometric energy contains all harmonics and is a complete **limit** discriminator, yet no fixed positive numerical threshold certifies normality. This is an exact source/probe sensitivity wall. It coexists with the PR #249 3-adic periodic near-Haar chord/Hankel phenomenon, which is related but has a different readout.

## PGM-09. π-source finite certification with separate angle and orbit errors (PAPER + EXACT MODEL)

The authenticated parent PR #231 supplies strict rational `L<π<U` by Wallis/Gamma/Kummer, without π digits. A dyadic rational center β with actual paid error `ε=max(|β−L|,|U−β|)` satisfies `|π−β|<ε`. For each reduced rational turn τ∈[−1/2,1/2], compute cos(2βτ) from exact rational Taylor terms through degree 2k, with outward error

`4^(2k+2)/(2k+2)! + 2|τ| ε`.

The latter pays **π as radian conversion constant** independently of π's role as the orbit starting number; no statistical independence is assumed. Transform `cos` to a squared chord and apply monotonic `K(q)=3/(1+2q)` to obtain true rational rectangles for each rational-midpoint pair, then sum them.

Since `|d K(q(t))/dt|<=24π<96`, the **true π energy versus its center β** obeys the exact source budget

`|E_N(π)−E_N(β)| < [96 ε/N²] Σ_(j,k<N)|b^j−b^k|`.

The sum is an exact source integer. Clip the certified output to the universal `[1,3]`. For finite n, this procedure is sound, provided the Wallis parent theorem and standard Taylor remainder are sound. Its resource inputs (Wallis stage, dyadic precision and Taylor order) are *actual integers* and underresolution returns a wide honest interval, not a false digit-statistic theorem.

**Finite source witnesses**: stage n=4096, b=2 gives strict rational enclosures `E_4>3/2` and `E_6>4/3`. The independent Machin alternating-series enclosure of π and a separate finite floating holdout both agree with these rational intervals. These are calibrated finite observations only; they do not show the energies converge to 1 or diverge.

## PGM-10. Equivalent π target: subquadratic geometric excess from authenticated source (UNVERIFIED)

Set `X_π=2−2cos(2π²)`, the single chord value from inserting the dimensionless circle ratio π into the arithmetic angle chart. For fixed integer b>=2, define the **actual** source-constrained nonnegative excess

`R_(b,N)(π)=Σ_(n=1)^(N−1) [ Σ_(j=0)^(n−1) 3/(1+2 F_(b^n−b^j)(X_π)) − n ]_+`.

An independently obtained estimate `R_(b,N)(π)=o(N²)` would prove π normal in base b by PGM-05; `O(N^(2−δ))` would give explicit fixed-h Weyl power savings. SCE-01 proves the unquantified subquadratic condition is equivalent to normality, so this remains a reformulation until a source-specific estimate is supplied. The needed proof must come from the original geometric π source, the actual BBP/Green memory, or authenticated signed prime-clock interference—not from defining “lawful” as minimal-energy or using fitted finite data as a holdout.

**Two independent falsification axes:** (a) replace π by nonnormal 3-adic periodic or sparse-square irrational sources while preserving all unmarked circle laws; (b) preserve the π source but mutate the action (fake composite prime, phase sign/origin, dropped CRT twiddle, lost BBP carry) and verify that the proposed estimate truly uses the authentic history. No unearned asymptotic estimate is claimed.

## PGM-11. Complexity of generator is not entropy of trajectory (CLASSICAL DISTINCTION)

Our exact rational greedy algorithm is deterministic and has a short description yet generates an equidistributed sequence. The constant point x=0 also has an extremely short geometric description yet its observed sequence is maximally nonnormal. A computable normal constant such as Champernowne's number has a short program and normal digit statistics; finite Kolmogorov description complexity does not, by itself, specify an individual orbit's Birkhoff genericity. “Stupidly clever minimum path” is a useful **hypothesis about an actual selection functional**, not a proved law of geometry or nature.

## PGM-12. Source/proof boundary and next verdict-changing instrument

**Classical:** Poisson Fourier kernel, Γ Mellin, Euler product, exact Haar expectation and basic equidistribution. **Paper-proved:** rational greedy O(1/N), exact action-regret identity, target-sufficient one-chord future, rational π source energy transport and 3-adic Ramanujan energy. **TESTED MODEL:** finite rational circle, cyclotomic and source-oracle examples. **UNVERIFIED:** source-specific subquadratic regret/cancellation, π normality, any RH equivalence, real-world universal energy minimization, scholarly priority, Lean formalization of this round.

**Next probes:** (1) exploit BBP positive Green tail and *signed* high-mode interference from sibling PRs #252–#258 to estimate the **actual** potential-excess sum, not average absolute values; (2) compare the one-kernel energy route with PR #247 Fejér collision energy and PR #248 min-plus prime-cost routes on held-out sources; (3) search for a source-derived drift/compensation law with authenticated orientation/CRT memory and a quantified nonlinear error; (4) attempt a genuinely unbounded analytic power bound for r_n or cumulative signed excess, with independent math verification. A proof of the target itself under a renamed assumption is not a breakthrough.

### Reproduction

~~~sh
python -m unittest discover -s tests -p 'test_poisson_circle_minimal.py' -v
python scripts/poisson_minimal_independent_oracle.py
python scripts/poisson_minimal_probe.py --output /tmp/poisson-minimal.json
cmp /tmp/poisson-minimal.json research/2026-10-24/POISSON_MINIMAL_GEOMETRY_RECEIPT.json
~~~

**External foundational references:** DLMF §1.15 Poisson kernel <https://dlmf.nist.gov/1.15>; Katznelson *Introduction to Harmonic Analysis* (classical Fourier); Bilyk–Matzke–Vlasiuk, *Positive definiteness and the Stolarsky invariance principle* <https://arxiv.org/abs/2110.04138>; López-García–McCleary, *Asymptotics of greedy energy sequences on the unit circle and the sphere* <https://arxiv.org/abs/2007.06109> (a **different** power-distance kernel, not the present r=1/2 Poisson kernel); established Wallis/Kummer source in SUCC PR #231 and circle chord law #247.
