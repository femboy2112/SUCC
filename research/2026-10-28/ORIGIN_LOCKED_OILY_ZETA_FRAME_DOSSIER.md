# Operation ORIGIN-LOCKED OILY → ALL PRIME PHASES → ZETA

**2026-10-28; draft research child of SUCC PR #346, ultimately based on Main XIII.** This is a mathematical response to the proposal that computation is physically/source-origin-locked even when it represents other arithmetic frames. **Status:** classical algebra and new-to-SUCC source-typed synthesis (paper proofs, exact finite tests); no external originality assertion, verified Lean proof, physical Lorentz model, measurement of the Planck constant, π-normality or RH proof. Never modify the original BBP forcing or zero seed. Our word *observer* means an explicitly defined mathematical readout/covariance, not a physical consciousness.

## 0. Recover the source contract without confusing frames with changed histories

Relevant source-preserving documents already in `main`:

* `research/2026-10-12/COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md`: frame/covariance vs actual causal evidence; coordinate simultaneity is not event knowledge.
* `research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md`: lawful quotient iff source-fiber congruence; no free source replacement.
* `research/2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md`: actual S/V_p braid and one common zeta Gibbs detailed-balance law, not literal S=V_p.
* `research/2026-10-15/TATE_IDELIC_ZETA_RECONSTRUCTION.md`: actual all-place Gaussian/prime-shell continuation; analytic continuation/Poisson must not be inferred from a finite transfer matrix.
* `research/2026-10-28/WAVEFRONT_OSCILLATOR_COMPLETION_AND_CAUSAL_INVERSE.md` in parent research: authentic positive Oily `u,v,M`, two-loop source, BBP original selected carry firewall.
* `research/2026-10-28/PRIOR_FIELD_CAUSAL_INFLATION_AND_BBP_FIREWALL.md` in PR #346: declared prior vs selected history.

**Question:** Can an arithmetic observer anchored to one original integer/source history compare other possible decompositions/frames without silently transporting the actual source to a different carrier? Which Fourier and real tilts can be viewed from the same origin?

**Typing:** A *frame change* on a linear realization `R=(M,b,ell)` is simultaneous transport `(G^-1 M G,G^-1 b,ell G)` for invertible G. Its scalar source readout `ell M^j b` is invariant for every j. A *parameter deformation* of M usually changes its trace and is therefore NOT a passive change of basis. A *source successor* n→pn changes the arithmetic source and, as proved below, the dimension of its minimal path fiber. The three operations must not be identified.

## 1. Original Oily two-loop source and its hyperbolic/parabolic boundary

The original SUCC positive source has, for x in [0,1],

`u=x-x²/2,  v=x²/2,  M(x)=[[u,1],[0,v]],  b=e₂,  ell=e₁^T`.

The actual packet is

`p_j(x) = (1-x)/4 · ell M(x)^(j+1) b`.

For **all x>0** define `q=sqrt(uv)` and `eta=(1/2)log(u/v)`. Then

`q^-1 M = [[exp(eta),q^-1],[0,exp(-eta)]] ∈ SL(2,R)`, and

`tanh(eta) = (u-v)/(u+v) = 1-x`.

This is an exact hyperbolic *parameterization* of the source rates, not a physical Lorentz boost. As x→1, eta→0 and q→1/2, but the normalized matrix tends to

`[[1,2],[0,1]]`, **parabolic nontrivial unipotent** rather than the identity.

The source coupling survives the eigenvalue collision. `M(1)=(1/2)I+N` with `N²=0,N!=0`; hence

`ell M(1)^(j+1)b = (j+1)/2^j`, and the source-normalized Oily endpoint weights are `w_j=(j+1)/2^(j+2)`.

For `M(q_+,q_-,c)=[[q_+,c],[0,q_-]]`, the general marked response is

`ell M^(j+1)b = c Σ_(a+b=j) q_+^a q_-^b`.

Its grade Hankel 2×2 minor `h0*h2-h1² = -c² q_+ q_-` is nonzero for c,q_+,q_- nonzero, *including q_+=q_-*. Thus its exact source input-output minimal linear dimension remains two at the collision. By contrast, the symmetric-power trace/character depends only on eigenvalues and does not detect the off-diagonal c. The counterfeit c=0 shares all eigenvalue characters and has identically zero marked off-diagonal response.

### Anchoring removes unearned frame freedom

If a coordinate change G is required to preserve the literal input `e₂` and output `e₁^T` (not just transform them), then G must be a lower shear `[[1,0],[c,1]]`. Conjugating the original M by this shear gives diagonal entries `u+c` and `v-c` when source coupling is one. If the exact original labelled u and v must also be preserved, c=0. **So the Oily source/input/output/diagonal passport fixes this frame completely.** General invertible passive frame changes remain legal only if b,ell and all readout/source labels are transported with M.

### Source frame singularity is real, but not a spacetime horizon

At a generic q>0 let `q_±=q exp(±eta)`, and take the upper source matrix with coupling c0>0. The diagonal source can be conjugated into it by shear `[[1,h],[0,1]]` with `h= -c0/(2q sinh eta)`. As eta→0, h diverges. At eta=0, the source matrix is non-diagonalizable while `qI` is diagonalizable. There is no regular diagonal frame through the collision.

Changing eta from real to imaginary **does not give a physical Lorentz transform**: real eta≠0 yields normalized trace `2 cosh eta >2`, imaginary eta=iθ yields trace `2 cos θ ∈[-2,2]`. Similar matrices must share trace. The analytic continuation connects different spectral *regimes*, not two passive frames of one unaltered source. The diagonal imaginary phase factors are unitary; the complete upper triangular matrix with nonzero coupling is generally not unitary even for imaginary eta.

## 2. Every genuine prime has a two-channel Oily-type character

For a genuine prime p and s>1, |Re τ|<s−1, put

`q_+=p^(-s+τ)`, `q_-=p^(-s-τ)`, `M_p=[[q_+,1],[0,q_-]]`.

Its source-marked grade response is the symmetric-power character

`h_(p,j)(s,τ)=p^(-sj) Σ_(a=0)^j exp[(2a-j)τ log p]`
`=p^(-sj) sinh((j+1)τ log p)/sinh(τ log p)`;

at τ=0 it equals `(j+1)p^(-sj)`. The local two-mode partition is

`Z_p(s,τ)=1/((1-q_+)(1-q_-))`.

The product over *genuine* primes (in its absolute-convergence half-plane) is

`Z_2(s,τ)=∏_p Z_p(s,τ)=ζ(s−τ)ζ(s+τ)`.

At τ=0, the Dirichlet coefficient is `d(n)` and not 1. The Oily endpoint q=1/2 coincides exactly with the **local p=2, s=1, τ=0 factor**, although the all-prime global ζ(1) partition diverges. This is a classical prime-mode transfer analogy, not an asserted original-source map from every prime to the four-pole BBP packet x.

The τ-even character has a source-relative second-order response

`∂²_τ h_(p,j)(s,0) = (log p)² p^(-sj) [j(j+1)(j+2)/3]`.

Divide by the τ=0 character to obtain a conditional variance `j(j+2)(log p)²/3`. This is a state/prime-dependent curvature of the *virtual path phases*, not a universal physical Planck constant.

## 3. Arithmetic-origin fibers and the precise obstruction to freely moving between n

Let `H_pairs=ell²(N_{≥1}×N_{≥1})` with basis |a,b>, product projection `π(a,b)=ab`. It decomposes orthogonally as

`H_pairs = ⊕_(n≥1) H_n`, `H_n=span{|a,b>:ab=n}`, `dim H_n=d(n)`.

At each fixed original arithmetic source n, define the uniform virtual-path state

`|ω_n> = d(n)^(-1/2) Σ_(ab=n)|a,b>`.

**Origin-lock theorem (OLZF-04).** The map `J:ell²(N_{≥1})→H_pairs`, `J|n>=|ω_n>` is an isometric embedding; the n-label is preserved exactly. However the one-channel prime action `A_p|a,b>=|pa,b>` does not intertwine the usual prime SUCC/FUCC action `V_p|n>=|pn>` with J:

`J† A_p J|n> = sqrt((v_p(n)+1)/(v_p(n)+2)) |pn>`.

The squared overlap/fidelity is

`F_p(n)=d(n)/d(pn)=(v_p(n)+1)/(v_p(n)+2)<1`.

**Proof:** A_p maps the d(n) uniformly supported paths bijectively onto the subset of the d(pn) paths for which p divides the first coordinate. The overlap with the uniform next-fiber state is `d(n)/(sqrt(d(n)d(pn)))`. Since `d(pn)/d(n)=(j+2)/(j+1)` for j=v_p(n), the formula follows. It applies to every n and genuine p; it is not inferred from numerical samples.

Thus J V_p and A_p J are distinct; restoring true source-coherent V_p in the pair representation requires recohering the newly available paths. The correct source-preserving action on the image of J is `J V_p J†`, while its action off that image requires an additional extension choice. A passive frame change cannot supply the missing paths because source-fiber dimensions change. This sharpens the distinction between observer basis change and a genuine successor edge.

The compensated effective prime shift is a nonconstant occupation-dependent gain 

`V_p = C_p · sqrt((v_p(N)+2)/(v_p(N)+1))`

**with composition order understood on the original domain**, where `C_p=J† A_p J`; written componentwise, multiply each |n> by the square-root gain **before** applying C_p. The required single-step amplitude pump is at most sqrt(2), but no source-independent constant fixes all prime-exponent levels.

### The Euler–Mascheroni source-path cost

For n=p^j, the sequential coherent-projection success factors are `F_j=(j+1)/(j+2)`. Their product after J rungs is

`∏_(j=0)^(J−1) F_j = 1/(J+1)`.

The exact negative logarithm is `log(J+1)`. If the finite observer accounts for the incremental shrinkage by the usual harmonic linearization `1/(j+1)` rather than the exact log, its accumulated discrepancy is

`H_J − log(J+1) → gamma`.

This is an **exact** realization of the γ finite part from the Oily two-channel grade multiplicity and origin-locked prime recoherence. It is **not** an inevitable causal entropy defect: the harmonic approximation and the choice of one-sided channel action are declared. The identity is classical, and the new-to-SUCC content is the source-fiber/coherence interpretation.

## 4. Source-faithful single-zeta lift versus free doubled zeta

For s>1 define `|ψ_s> = ζ(s)^(-1/2)Σ_n n^(-s/2)|n>`. The source-preserving lift through J is

`J|ψ_s> = ζ(s)^(-1/2) Σ_(a,b≥1) [(ab)^(-s/2)/sqrt(d(ab))]|a,b>`.

Its squared mass over all paths with product ab=n is precisely `n^(-s)/ζ(s)`; **no double counting** occurs. The free independent two-mode state

`|ψ_s>⊗|ψ_s> = ζ(s)^(-1)Σ_(a,b)(ab)^(-s/2)|a,b>`

has squared source marginal `d(n)n^(-s)/ζ(s)^2`. The two states and their n-marginals differ even though both are built from the same formal path pairs. Their different normalizations are necessary to preserve the declared source. A finite positive cutoff gives exact Fraction regression tests of the distinction.

For a fixed n define the origin-locked phase observable

`χ_n(t)=<ω_n| exp(it D)|ω_n>`, with `D|a,b>=log(a/b)|a,b>`.

It factorizes over n's genuine prime-power factors, with local character

`χ_(p^j)(t)=sin((j+1)t log p)/[(j+1)sin(t log p)]`, extended continuously at removable singularities. The source index n does not move. The imaginary tilt exp(itD) is unitary on the original pair Hilbert space and preserves the **marginal distribution of n** (it changes relative path phases). In contrast, a real exponential tilt exp(τD/2) changes the path probabilities and requires renormalization; it is not a passive change of frame.

The conditioned variance is

`Var(D | product=n) = Σ_(p^j||n) [j(j+2)/3](log p)^2`.

It vanishes at n=1 and varies with n and p, directly refuting an unqualified identification with a nonzero universal physical h-bar. That it is generated from the source-indexed finite path fiber remains mathematically useful.

### A quantitative distinction in the critical zeta susceptibility

Let q_p=p^(-s). Under the **single-zeta source law** N~n^-s/ζ(s), the p-exponent J has geometric distribution `(1−q)q^j`. Choosing a path uniformly within each n-fiber yields source-locked imbalance variance

`I_anchor(s)=Σ_p (log p)^2 q_p(3−q_p)/[3(1−q_p)^2]`.

In contrast, two *unconditioned independent* zeta integer channels yield

`I_free(s)=2 Σ_p (log p)^2 q_p/(1−q_p)^2 = 2 (log ζ)''(s)`.

The exact difference identity is

`I_anchor(s)=(log ζ)''(s) − (1/3)Σ_p (log p)^2 q_p²/(1−q_p)^2`.

The second sum converges even at s=1, whereas `(log ζ)''(s)∼(s−1)^(-2)`. Therefore

`lim_(s→1+) (s−1)² I_anchor(s)=1`,
`lim_(s→1+) (s−1)² I_free(s)=2`.

**The origin-locked single-source fiber model has exactly half the leading critical susceptibility of the free doubled field.** This is a rigorous difference in **prior/source typing**, not a derived physical relative-velocity law or quantum uncertainty inequality. The prime p=2 at q=1/2 provides a finite calibration: source-locked local variance =`(5/3)(log 2)^2` versus free doubled local variance=`4(log 2)^2`.

## 5. Global critical bridge: Gamma sum, Laplace difference, and cancellation of the first gamma correction

Let `A,B` be independent positive integers with zeta Gibbs law `P_s(n)=n^-s/ζ(s)`. Put s=1+ε, ε>0, `X_ε=εlog A`, `Y_ε=εlog B`. For every t≥0,

`E exp(−t X_ε)=ζ(1+ε(1+t))/ζ(1+ε) → 1/(1+t)`.

Hence the two rescaled channels converge jointly to independent Exp(1) variables; their sum tends to Gamma(2,1) and difference to centered Laplace(0,1).

The source-origin-normalized two-mode real tilt is

`M_ε(δ)=E exp[δ(X_ε−Y_ε)] = ζ(1+ε(1−δ))ζ(1+ε(1+δ))/ζ(1+ε)^2`

for |δ|<1. It converges exactly to `1/(1−δ²)`. For δ=it this is the characteristic function `1/(1+t²)`. Thus the real reweighting and imaginary phase views are the MGF and characteristic function of the **same** declared difference variable, not physical Lorentz-equivalent observers.

Set γ=Euler's constant and γ₁=the first Stieltjes constant. From the classical Laurent series `ζ(1+z)=1/z+γ−γ₁z+O(z²)` derive, for fixed |δ|<1,

`log M_ε(δ) = −log(1−δ²) − (2γ₁+γ²)δ² ε² + O_δ(ε³)`.

**There is no O(ε) term**: the Euler–Mascheroni correction is common to both channels and cancels in the normalized relative response at first order. It survives as the familiar `E log Gamma(2,1)=1−γ` in the limiting *total* channel, and appears in source-locked harmonic-vs-log recoherence above. Neither statement identifies these global zeta channels with SUCC's authenticated four-pole positive Oily law; the same Gamma shape can come from multiple valid sources.

## 6. Explicit firewall and independent falsification tasks

1. **Eigenvalue-only counterfeit**: replace the offdiagonal 1 in the original Oily matrix by 0. Every symmetric-power character and the full Euler product are unchanged; the source-marked Oily readout disappears. Therefore no zeta partition/character theorem alone authenticates BBP's positive packet coupling.
2. **Frame counterfeit**: conjugate M but hold b and ell fixed; scalar readouts change. A real parameter deformation with different trace is not a passive change of observer basis.
3. **False physical identification**: hyperbolic τ and elliptic it are distinct conjugacy regimes of complexified SL2, not two physical Lorentz frames of the same field. The full upper Jordan matrix is not unitary on the usual positive Hilbert norm when τ is imaginary.
4. **Double-counting counterfeit**: free independent two-mode Gibbs assigns n mass proportional to d(n)n^-s, not n^-s. Only the explicit source-labelled isometry J supplies the latter when lifted into pair space.
5. **False universal Planck scale**: origin-fiber variance is exactly zero at n=1, depends on p and exponent at other n, and is not an iℏI commutator.
6. **Fake arithmetic primes/composites**: using an independent p=4 channel on top of p=2 creates multiple encodings for n=4. Only genuine primes are primitive prime modes; composites must be products of actual prime transitions.
7. **Selected-zero-seed BBP firewall**: the true expanding original four-pole `U_0=0` real circle orbit is separate from the positive Oily grades, the zeta Gibbs prior, and the source-locked multiplicative fibers. Changed-seed coherent controls satisfy all positive spectral identities. Signed Weyl cancellation / base-16 π normality and RH remain OPEN.

**Highest-value next research hinge:** construct a genuine source-preserving intertwiner from the ORIGINAL zero-seeded BBP carry/phase dynamics into this origin-fiber pair system, retaining the changed-seed discriminator. Then test whether the source-locked interference character χ_n yields any true sublinear signed Weyl estimate, rather than merely another positive averaged measure. The absence of such an arrow is NOT filled by analogical Lorentz or quantum language.

## 7. Claim-ledger summary (local namespace only)

| Claim | Exact statement | Status |
|---|---|---|
| OLZF-01 | Oily u,v define eta with tanh eta=1−x; x=1 normalized matrix nontrivial parabolic | PAPER-PROVED; original source |
| OLZF-02 | Marked input/output invariant under fully transported passive G; anchored labels rigidify triangular basis | PAPER-PROVED; algebra |
| OLZF-03 | Prime two-mode characters yield ζ(s−τ)ζ(s+τ), but do not recover source coupling | CLASSICAL + exact counterfeit |
| OLZF-04 | Arithmetic source-fiber J is isometric and naive A_p fails source-coherent commutation by sqrt((j+1)/(j+2)) | PAPER-PROVED; genuine primes |
| OLZF-05 | Product fidelity 1/(J+1) and harmonic-vs-log defect tends gamma | CLASSICAL/PAPER-PROVED under chosen cost convention |
| OLZF-06 | Source-lift Jψ_s has n^-s/ζ(s) marginal; independent double mode has d(n)n^-s/ζ(s)^2 | PAPER-PROVED; exact cutoff tests |
| OLZF-07 | Origin-locked χ_n(t) factorizes over genuine prime powers and has variance Σ j(j+2)(log p)^2/3 | PAPER-PROVED; finite test |
| OLZF-08 | Source-anchored susceptibility grows like 1/(s−1)^2, doubled free one like 2/(s−1)^2 | CLASSICAL/PAPER-PROVED; Euler product region |
| OLZF-09 | Critical zeta double field gives Gamma2 total and Laplace difference, with no linear gamma correction in normalized response | CLASSICAL/PAPER-PROVED; independent mpmath control |
| OLZF-10 | Real-vs-imaginary τ are passive physical Lorentz transforms of the same M | REFUTED by invariant traces |
| OLZF-11 | These observations determine physical ħ or prove π-normality/RH | UNVERIFIED, with concrete zero-variance and changed-seed controls |

## 8. Reproduction and authority

- `observational_succ/origin_locked_oily_zeta.py`, `tests/test_origin_locked_oily_zeta.py`: standard-library Fraction exact core; no imported artifacts modified.
- `observational_succ/zeta_wavefront_regeneration.py`, `tests/test_zeta_wavefront_regeneration.py`: recovery of the preceding partial SUCC zeta wavefront work, including Gibbs detailed balance, prime regeneration and fake composite controls.
- `scripts/origin_locked_two_mode_oracle.py`: independent SymPy (finite source/gauge/variance) and high-precision mpmath (critical Gamma/Laplace and Stieltjes coefficient) independent checks.
- `scripts/zeta_wavefront_independent_oracle.py`: earlier independent theta/Mellin zeta and source Oily Gamma control; has not been represented as a Lean kernel proof.
- All universal analytical results stated with direct derivations; analytic continuation is taken from SUCC's actual classical Tate/Poisson source, not inferred from finite source simulations.

**Primary classical references**: Bost–Connes (1995) arithmetic statistical mechanics; SUCC's already integrated `TATE_IDELIC_ZETA_RECONSTRUCTION`; standard `SL(2)` symmetric-power character identity; classical zeta Laurent expansion and Tauberian/Laplace convergence; NIST DLMF 25.2 (zeta pole, Stieltjes constants). No claim of independent publication priority.
