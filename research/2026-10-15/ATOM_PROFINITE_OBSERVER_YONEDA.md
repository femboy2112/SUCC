# ATOM I — Bijective finite-observer reconstruction by modeling the test models

**2026-10-15, isolated branch** research/observer-tate-bijective-descent-2026-10-15; parent main 03db44203147a7b28d445bb9f970fa71360e78c4. No concurrent branch or archival source modified. CLASSICAL finite algebra/Stone duality ingredients. **RH PROVED: NO.**

## Exact object and theorem

Let the observation index be the directed divisibility poset of integers m>=2. An observer at stage m sees the actual source ring X_m=Z/mZ. A lawful refinement m|N is the reduction \(\pi_{N,m}:X_N\to X_m\). A model of the observer's model is its **ENTIRE finite test algebra**
\[
A_m=\mathbb Q^{X_m},
\]
with pointwise addition/multiplication and source-preserving pullback \(j_{m,N}f=f\circ\pi_{N,m}\). Its direct limit \(A_\infty=\varinjlim_mA_m\) is algebraically the ring of locally constant rational functions on the profinite completion.

**Canonical, genuinely BIJECTIVE theorem:**
\[
\boxed{\operatorname{Hom}_{\mathbb Q\text{-alg}}^1(A_\infty,\mathbb Q)
\cong\varprojlim_m X_m=\widehat{\mathbb Z}.}\tag{ATOM-I}
\]
This is an isomorphism with the inverse-limit topology if we give algebra characters the cylinder/idempotent evaluation topology. It does not assert category equivalence with physical observers.

**Proof at one finite stage.** For a∈X_m, let \(e_a(x)=1\) for x=a, zero otherwise. Then \(e_a^2=e_a\), \(e_ae_b=0\) for a≠b, \(\sum_ae_a=1\). A unital algebra map \(\lambda:A_m\to\mathbb Q\) sends each idempotent to 0 or 1. Exactly one must be 1. Since \(f=\sum_a f(a)e_a\), \(\lambda(f)=f(a)\) uniquely. Conversely evaluation at each a is a unital algebra character.

**Proof at infinite compatible stages.** Restriction of any character \(\lambda:A_\infty\to\mathbb Q\) to A_m selects one residue a_m. For m|N, equality of \(\lambda(f)\) and \(\lambda(f\circ\pi)\) forces \(a_N\bmod m=a_m\). Thus \((a_m)_m\) is an inverse-limit point. Conversely every coherent family defines evaluation on each A_m, and compatibility makes these definitions independent of which larger stage represents the function. These assignments are inverse bijections. The factorial moduli 2!,3!,4!,... are cofinal for divisibility, so the same result follows by factorial observer growth. **The code checks FINITE prefixes only; the unbounded theorem is the proof above.**

**Second dual, Fourier meaning.** Any continuous character of compact profinite \(\widehat Z\) factors through some finite quotient, hence \(\widehat{\widehat Z}\cong\mathbb Q/\mathbb Z\). The embeddings of finite residue Fourier labels are precisely \(\zeta_m\mapsto\zeta_N^{N/m}\). This explains how a second-order observer of stage functions recovers the lawful additive character frequencies.

## Source-realizability obstruction: compatible is not original integer

\(\mathbb Z\to\widehat{\mathbb Z}\) is injective and dense, NOT surjective. Construct a global profinite point with p=2 coordinate 1 and all odd p coordinates 0. For even m=2^a u with u odd, its CRT residue is \(x_m=u\,(u^{-1}\bmod2^a)\pmod m\). The stages m=2,6,24,120 give **1,3,9,105**, source-coherently. Every finite prefix has an integer representative. But a single integer realizing ALL levels must be divisible by 3^k for every k and therefore equal 0, contradicting its residue 1 mod 2. This is an exact mathematical source-map/no-ghost obstruction, not a physical measurement.

Two actual source integers 1 and 3 are indistinguishable to the mod-2 observer, but distinguished by mod-4 idempotents. A coarse toolkit's nonfaithfulness is repaired by lawful refinement, not by guessing hidden source identity. A model-of-model restricted to fewer than all idempotent events can remain nonfaithful forever.

## Receipt and acceptance

- Module observational_succ/tate_observer_completion.py: StageCharacter, factorial_observer_moduli, reconstruct_from_model_models, integer_source_prefix, profinite_ghost_prefix.
- Exact tests enumerate all atom evaluations for several finite rings and reject fractional/duplicate idempotents, untyped booleans and failed source pullback squares.
- A source ID string and the mathematical existence of a character do not authenticate a performed experiment or an original physical state.
- Full arithmetic \(\mathbb A_{\mathbb Q}\), the connected real place, global Poisson, source-specific Weil positivity, RH: **UNVERIFIED**.

**Verdict:** Classical reconstruction theorem proved in the declared algebraic/profinite category; actual integer/physical source realization and RH do not follow.
