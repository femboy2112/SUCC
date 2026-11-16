# BBP causal joining: the two-adic normality question and time-labelled phase probes

**2026-11-15; additive research continuation of SUCC #646.** Status: TT-01..TT-05 are classical/source-specific paper derivations with bounded finite smoke tests, **not** a proof that their open decay hypotheses hold for π. The original four BBP residues and literal `U_0=0` are unchanged. The root-of-unity proof of `F(0)=0` in #646 is a cited paper premise, not independently Lean-checked here. No publication/merge permission.

## 0. Two different Z_2 coordinates, both essential

Fix original `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`; `x=π/16`, `T_n=∑_{j>=1}16^(-j)r(n+j)`, `z_n={U_n+T_n}={16^n x}`. Put

- `F(t)=∑_{j>=0}16^j r(t-j)` in `Z_2`. Prior #646 (BC-0 through BC-4) shows `F(0)=0`, `F(n)=U_n` in `Z_2`, and `F` is an isometric bijection of `Z_2`.
- `b_0=ρ(x)=∑_{j>=0}d_(j+1)16^j` in `Z_2`, using the *Euclidean-circle* base-16 expansion of `x`, with its unambiguous regular expansion. Define the radix-digit left shift `σ(b)=(b-(b mod16))/16` and `b_n=σ^n(b_0)=ρ(z_n)`.
- `a_n=F(n)` and `G=F∘(+1)∘F^(-1)`, so `(a_(n+1),b_(n+1))=(G(a_n),σ(b_n))`.

`a_n` and `b_n` are **not equal**. The former is the arithmetic 2-adic image of the *full rational lift*, while the latter is digit-reversed *real circle* information obtained by real evaluation and the authentic Green tail. Source passport `U_n=m_n+c_n/d_n`, `d_n` odd, gives `a_n mod q=m_n+c_n d_n^(-1) mod q`, whereas `z_n={c_n/d_n+T_n}`. The integer winding, odd cofactor, signed forcing, real circle metric and tail are all needed. Arbitrary independent joining of these streams is not an authenticated realization of π.

## TT-01. The exact 2-adic normality question (classical equivalence; π OPEN)

Let `m` be Haar probability on `Z_2`, and define empirical measures on `Z_2×Z_2`

`μ_N=(1/N)∑_(n=0)^(N-1) δ_(a_n,b_n)`.

**Theorem.** For any real `x` with a fixed canonical base-16 expansion (keeping the same authentic zero-source arithmetic clock `F(n)` as a declared observation coordinate),

`x is base-16 normal  ⇔  μ_N -> m⊗m weak-*`.

**Proof.** The reverse implication follows by projecting onto the digit coordinate: the `k`-digit cylinders of `b_n` are the length-`k` real base-16 words starting at time n. In the forward direction, normality means `(1/N)Σδ_(b_n)->m`. Fix `q=16^k`. The source isometry makes `n↦F(n) mod q` a permutation of the `q` residues, so conditioning on any arithmetic carrier cylinder is equivalent to selecting exactly one arithmetic progression `n≡r mod q`. Normality of `x` gives uniform future-word frequencies on every such progression (the classical arithmetic-progressions/base-power normality theorem). One self-contained justification: any weak limit of the `q` progression-specific digit distributions is invariant under `σ^q`; their average is Haar. Each is absolutely continuous with respect to Haar, and Haar is ergodic under `σ^q` (a Bernoulli shift); hence every limit is Haar. This establishes all product cylinders and weak-* convergence. The family `q=16^k` is cofinal among 2-power moduli. QED.

**Critical distinction:** Product Haar is a **single-time asymptotic marginal**. At two times, the coordinates are exactly related by `G^ell` and `σ^ell`. The full process retains its deterministic causal graph even under normality. No joint independence of successive observations is claimed. This is a reformulation of the open statement, not a new saving.

## TT-02. The full causally time-coupled law (classical conditional theorem)

For any fixed finite list of nonnegative lags `ell_1,...,ell_s`, any continuous test `H` on `(Z_2×Z_2)^s`, normality of x is equivalent to the complete collection of limits

`lim_(N->∞) (1/N) Σ_(n=0)^(N-1) H((a_(n+ell_i),b_(n+ell_i))_i)
 = ∫_(t,b) H((F(t+ell_i),σ^(ell_i)b)_i) dm(t) dm(b)`.

The forward implication follows from TT-01 by composing H with the continuous maps `(a,b)↦(G^ell a,σ^ell b)`. The converse chooses `s=1,ell_1=0` and projects to digit cylinders. The law retains overlapping digit constraints: if future coordinates at two time taps overlap, their values are NOT independent and inconsistent cylinder prescriptions have probability zero. The clock graph is likewise deterministic. These are mandatory positive controls for any purported source-coupled 'Higgs' experiment.

## TT-03. A signed original-source two-time character interferometer (exact normality selection rule)

For `q=16^k`, `χ_(q,j)(a)=exp(2πi j (a mod q)/q)`. For fixed positive integer lag `ell`, fixed integers h,j and clock characters a,b, define on the shell `[B,2B)`:

`I_(B;q,ell)(h,j;a,b)=(1/B)∑_(n=B)^(2B-1) χ_(q,a)(F(n)) conj(χ_(q,b)(F(n+ell))) exp(2πi(h z_n-j z_(n+ell)))`.

The real digit shift gives the **exact**, not approximately independent, identity `z_(n+ell)={16^ell z_n}`. Hence `I_B` is a labelled source-clock weight times the real Weyl mode `H=h-16^ell*j`. The source-only clock reference is finite and exactly computable:

`K_(q,ell)(a,b)=q^(-1)∑_(r=0)^(q-1) χ_(q,a)(F(r)) conj(χ_(q,b)(F(r+ell)))`.

**Selection law if x is normal:** `I_B -> 0` for `H!=0`, and `I_B -> K_(q,ell)(a,b)` for `H=0`, with all parameters held fixed. Conversely, requiring these limits for all settings implies normality (include a=b=j=0 and h !=0). In fact the nonzero modes converge to zero for each fixed clock character by TT-01. No positive-energy inference and no source-derived rate for π are asserted. K can be nonzero for nontrivial carrier character choices; this matters for genuine calibration and wrong-seed controls.

## TT-04. A nontrivial four-pole-derived phase mixer with a stable, two-readout inverse

Exactly in the original source, at every `n∈Z_2`,

`F(n) mod16 = -n + 2*(n mod2) mod16`.

**Finite proof certificate:** `F(n)≡r(n) mod16`, each denominator is odd, and the congruence follows from all 16 residue classes n mod16. Consequently, for `ω=exp(2πi/16)`, the time-coupled carrier phase

`w_n=ω^(F(n)-F(n+1))=ω^(-1)*(1 if n even else i)`.

This is not a freely selected random phase. It is an exact original-four-pole *source-character difference across two times*.

Define `M_B(h)=(1/B)Σ_(n=B)^(2B-1) w_n exp(2πi h z_n)`. For even B put `W_B(h)=B^-1 Σ exp(2πi h z_n)` and `E_(B,h)=2/B*(exp(2πi h z_(2B))-exp(2πi h z_B))`. Direct even/odd splitting, and `z_(n+1)={16 z_n}`, give the **finite exact reconstruction**

`W_B(h)= [ω/(1+i)]*[M_B(h)+M_B(16h)] - [i/(2*(1+i))]*E_(B,h)`;

`|W_B(h)-ω/(1+i)*(M_B(h)+M_B(16h))| <= sqrt(2)/B`.

Thus for every fixed nonzero integer h, controlling **both time-labelled probe phases h and 16h**, with their known orientation, is sufficient to control the original phase (and vice versa). The inversion is stable and only requires two fixed settings; no large B sampling assumption is used in the identity. Because `|W_(B+1)(h)-W_B(h)|=O(1/B)`, even-B shell limits suffice. It follows that base-16 normality is equivalent to `M_B(h)->0` for every fixed h≠0 on even shells. This is another exact instrument, not an arithmetic estimate.

The constant-circle coherent counterseed `s=-x` gives `z_n=0` and `M_B(h)=ω^(-1)*(1+i)/2` for every even B and h. A genuine source-coupled signed detector therefore distinguishes this coherent fake at any fixed harmonic. Forgetting the carrier phase label or averaging an unknown Gamma clock can create a false inference; the full complex orientation and original seed authentication are essential.

## TT-05. High-resolution source kicks are also finite temporal Green lags

For every n,k≥1, with q=16^k and finite source lag `Δ_k(n)=∑_(j=1)^k16^(k-j)r(n+j)=U_(n+k)-q U_n`, the true completed identity yields

`q T_n = Δ_k(n)+T_(n+k)`.

So the order-one critical circle kick near `q~64n²` is *exactly* a k-time source innovation plus a new small future correction. The `qT_n<1` circle seam is `D_(n,k)=1[{q{U_n}}+qT_n≥1]`. For an original rational prefix register `A_(n,k)=floor(q{U_n})`, define the **finite digit-grid** means `C_B^π(t)=B^(-1)Σ exp(2πi t A'_(n,k)/q)` and `C_B^U(t)=B^(-1)Σ exp(2πi t A_(n,k)/q)`. These are not the continuous circle characters `exp(2πi t z_n)`. At the signed high frequency h=q/2 their difference equals

`C_B^π(q/2)-C_B^U(q/2) = -(2/B)Σ_(n=B)^(2B-1) D_(n,k)*(-1)^A_(n,k)`.

To retain BOTH time and carrier orientation, define the exploratory paired probe

`P_(B,k)=B^(-1)Σ w_n D_(n,k) (-1)^A_(n,k)`.

**Calibrated expected responses:** Under an expressly hypothetical independently uniform circle-prefix null (the source is NOT asserted to follow it), each D has probability qT_n and is independent of A, so `E[P]=0` for even q. Under the coherent same-forcing wrong real seed `s=-x`, `U_n(s)=-T_n`, so for `qT_n<1`, `A=q-1`, `D=1`, and `P=-ω^(-1)(1+i)/2` on even B. For genuine zero-seeded BBP, the probe is exactly computable at every finite shell using rational Green bounds; samples must not be treated as an all-B estimate.

**Critical firewall:** A normal x is not known to make the moving-depth `P_(B,k(B))->0` when `q≈n²`; normality only forces fixed-resolution statistics. At q≫B the B sampled carrier addresses are all distinct; naïve conditional frequencies cannot identify the q-cell distribution. The time-labelled source graph offers additional lawful settings but no proven asymptotic saving. Probe design must distinguish an *arithmetic* inequality from a *randomized readout* concentration inequality.

## Verdict-changing next steps

1. **Source clock × real passport:** lift the full signed original residues, `m_n=floor(U_n)`, odd denominator d_n, numerator remainder, prime CRT cofactor and exact Green tail into a joint time-labelled source action. Infer a genuinely original-zero restriction on `I_(B;q,ell)` or the fixed h/16h mixer. A bound on chosen gamma variance, a `q/B` Parseval norm, or a finite sample is insufficient.
2. **Fixed-resolution theorem vs moving critical experiment:** retain parallel fixed `(q,ell,h,j,a,b)` limits and prescribed moving q≈64B²; an unbounded-frequency or moving-lag claim requires an independent uniformity theorem. Preselect windows, negative seed and rational periodic controls, and compare phase-rotated two-readout inversion to directly computed `W_B(h)` on fresh shells.
3. **Reconstruction protocol:** require measured carrier phases, signed complex quadratures, the exact frequency relationship h↔16h, source-time labels, and known index sampling probabilities. Use independent sampled time indices and calibrated concentration only for finite readout uncertainty; no number of positive clicks proves the all-B limit.
4. **Formalization:** translate TT-04 finite character/carry algebra and TT-05 exact finite source lag into Lean after separate proof review of inherited BC-0. Check all exact-hostile mutants and run AGENTS.md full gates at the specific commit before integration.

**Claim status:** TT-01/02 classical equivalent criteria; TT-03 signed selection law conditional on normality; TT-04/05 paper-proved finite identities; original-zero fixed-mode asymptotic estimates and π normality remain OPEN. Source and physical-particle Higgs couplings are NOT inferred.
