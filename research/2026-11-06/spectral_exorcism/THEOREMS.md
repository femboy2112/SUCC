# Operation SPECTRAL EXORCISM — frequency-ray rigidity and a mesoscopic collision certificate

**2026-11-06 · PROVED LOCAL CONDITIONAL CRITERIA, NOT π NORMALITY.** Strict additive child of PR #531, exact parent 06b46d5715153412215947a0e9ee4800c9bd9a5f. The original four-pole forcing, literal U₀=0, frozen proofs/Lean, provenance and main remain unchanged. Nothing here proves an authentic source-selected all-scale collision bound, RH, or base-16 π normality.

## 0. Authentic source, phases and type separation

Use the original rational four-pole source r(n)=(120n²−89n+16)/[(2n−1)(4n−1)(8n−7)(8n−3)], U₀=0, U_(n+1)=16U_n+r(n+1). Let x_n={U_n} and z_n={16^n β}, β=π/16. The original real tail T_n=Σ_(j≥1)16^(−j)r(n+j) satisfies U_n+T_n=16^nβ, T₀=π/16, 0<T_n<1/[15(n+1)²] for n≥1, and

    Σ_(n≥0)T_n < π/16 + 1/15 =: B_tail.

The 2-adic source V(n)=U_n and its next-bit clone from #527/#528 are inherited exact theorems. They do NOT define real Fourier characters. Real phases are always evaluated via the real rational x_n or completed z_n.

## 1. SE-01: the exact logarithmic spectral obstruction — PROVED LOCAL

Let b≥2 and z_n={b^nβ}. Define empirical μ_N=N^−1Σ_(n<N)δ_(z_n), and W_N(h)=N^−1Σ_(n<N)e(hz_n). Every weak subsequential limit ν of μ_N is invariant under T_b:x→bx mod1: T_b*μ_N−μ_N=(δ_(z_N)−δ_(z_0))/N. Thus

    νhat(h)=νhat(bh)=νhat(b²h)=...  for all integers h.

If ν is not Haar, there exists h₀≠0 with c=|νhat(h₀)|>0. Then for every H≥|h₀|,

    Σ_(1≤|h|≤H)|νhat(h)|²
       ≥ 2c²(1+floor(log_b(H/|h₀|))).

Hence non-Haar invariant measures have **at least logarithmically growing unweighted Fourier energy**. This is not a statement about the locations of ζ zeros.

Define G(H)=limsup_(N→∞)Σ_(1≤|h|≤H)|W_N(h)|², for fixed finite H. If

    lim_(H→∞) G(H)/log H = 0,

then every weak limit is Haar, hence μ_N→Haar and β is normal base b. The proof uses the fixed-H convergence of Fourier coefficients along a weakly convergent subsequence and the preceding frequency-ray lower bound. Conversely, if β is normal, G(H)=0 for every fixed H. Thus this o(log H) spectral condition is **equivalent** to normality in the b-orbit class; it is a reformulation with a potentially different arithmetic route, not an easier theorem automatically.

A bounded energy G(H)≤C uniform H is a stronger sufficient condition.

## 2. SE-02: Fejér positivity and exact source-pair collision representation — PROVED LOCAL

Let H≥1 and define the Fejér kernel

    F_H(t)=Σ_(|h|≤H)(1−|h|/(H+1))e(ht)
          = (1/(H+1)) |Σ_(j=0)^H e(jt)|² ≥0.

For any real phases y₀,...,y_(N−1), define

    C_(N,H)(y)=(1/N²)Σ_(n,m<N)F_H(y_n−y_m)
      =Σ_(|h|≤H)(1−|h|/(H+1))|W_N^y(h)|².

The zero mode contributes exactly 1; every other term is nonnegative. Thus C≥1. The pair kernel F_H(t) is peaked on circle separations O(1/H), giving a positive collision diagnostic with no invented phase orientation. The individual pair contributions are nonnegative, but the Fourier-mode energy decomposition still has a genuine nonuniformity defect C−1.

For any fixed h₀ and H≥2|h₀|, each frequency b^j h₀≤H/2 contributes weight ≥1/2. Hence a non-Haar invariant ν with coefficient c has Fejér energy ≥1+c²(1+floor(log_b(H/(2|h₀|)))). A uniform-in-H bound on limsup_N C_(N,H) forces Haar.

## 3. SE-03: a single MESOSCOPIC source-selected collision bound would prove π normality — PROVED CONDITIONAL / SOURCE BOUND OPEN

Fix 0<α<1/2 and set H_N=floor(N^α). Suppose the **actual original zero-seeded rational BBP phases** x_n={U_n} satisfy the following all-large-N estimate for some finite C:

\[
\boxed{
\sup_{N\ge N_0}
\frac1{N^2}\sum_{n,m<N}F_{\lfloor N^\alpha\rfloor}(x_n-x_m)
\le C.
}\tag{SE3-OPEN}
\]

Then π is base-16 normal. In fact the weaker estimate C_(N,H_N)(x)=o(log N) is also sufficient. **Neither estimate has been proved for the original source.**

**Proof of sufficiency:** For any weak limit ν of completed z_n and any fixed J, the finite frequencies h₀,16h₀,...,16^J h₀ are eventually inside H_N/2. The Fejér energy bound forces

    1 + (J+1)|νhat(h₀)|² ≤ C

along the subsequence (using both positive/negative frequencies, each with weight≥1/2). Since J is arbitrary, νhat(h₀)=0 for every h₀≠0. Thus ν=Haar, and all empirical measures converge. For o(log N), choose J_N proportional to log N, but weak convergence alone is not uniform over growing frequencies; instead for each fixed J the bound o(log N) is insufficient to force c=0. To justify the weaker condition rigorously, use the **exact finite orbit relation**:
    W_N(16^j h)−W_N(h)
      = (1/N) [Σ_(n=N)^(N+j−1)e(h z_n)−Σ_(n=0)^(j−1)e(h z_n)],
so |difference|≤2j/N.
For j up to J_N=floor((α/2)log_16 N), all frequencies |16^j h|≤H_N/2 for sufficiently large N, and the phase errors are uniformly O(log N/N). Thus the Fejér energy C_(N,H_N)(z)−1 is ≥J_N (|W_N(h)|−O(log N/N))_+². If C_(N,H_N)(z)=o(log N), then W_N(h)→0 for every fixed h. Weyl gives normality. This quantitative argument also proves the stronger uniform C version directly.

**Important:** This is an all-horizon **mesoscopic pair-collision upper bound**, not merely the lower bound C≥1 or an already-proved finite certificate. It is a concrete alternative to PR #531's open Poisson-energy contraction.

## 4. SE-04: original-source rational-to-real collision transport at H=o(√N) — PROVED LOCAL

For the exact original source, z_n={U_n+T_n} and x_n={U_n}. Since

    |F_H'(t)| ≤ Σ_(|h|≤H)2π|h| ≤ 2π H(H+1),

the mean-value theorem and pairwise circle differences give

\[
\boxed{
|C_{N,H}(z)-C_{N,H}(x)|
\le \frac{4\pi H(H+1)}{N}\sum_{n=0}^{N-1}T_n
<\frac{4\pi H(H+1)}{N}\left(\frac{\pi}{16}+\frac1{15}\right).
}\tag{SE4}
\]

The proof uses |(z_n−z_m)−(x_n−x_m)| on the real lift ≤T_n+T_m and counts each T_n exactly 2N times. Thus for H_N=floor(N^α), 0<α<1/2, the error tends to zero as N→∞. **This is a genuine uniform mesoscopic source-to-completed-orbit bridge**, with a rigorous original four-pole tail constant, independent of any unproved digit distribution. It does NOT supply an upper bound for C itself.

The finite original rational source has exact odd denominators, integer carries, 2-adic state and rational numerator reconstruction from #528. Therefore C_(N,H)(x) is a well-typed real function of the full source/carry/denominator chronology, not a 2-adic character in disguise. It is a candidate for analytic pair-count bounds using arithmetic separation. A source-selected inequality on it must distinguish the rational isometric H-shadow and the coherent wrong seed.

## 5. SE-05: an exact finite-to-infinite certificate obstruction — PROVED LOCAL

For any irrational β, any integer b≥2, and any finite L, let β_L=floor(b^L β)/b^L. Then |β−β_L|<b^(−L), and for all n≤L,

    ||{b^nβ}−{b^nβ_L}||_T ≤ b^(n−L).

But for n≥L, {b^n β_L}=0. Hence β_L is nonnormal, while its first L−d observations approximate β to circle accuracy ≤b^(−d) for every fixed d. In the **same BBP forcing**, choose real seed s_L=β_L−π/16; then the completed trajectory has β_L and the same original forcing and all its source moments. This seed is not the authentic literal zero and need not lie in Q₂; it is a hostile finite-certification model, NOT a counterexample to the genuine π orbit.

Any theorem whose hypotheses involve only finitely many approximate real-phase observations and source-only constants, with no literal-zero-selective asymptotic hypothesis, cannot exclude this control. Exact rational original-zero certificates remain useful but must be threaded through an all-scale analytic estimate, not extrapolated from finite values.

## 6. SE-06: exact dyadic clock energy ESCAPE identity and the RH analogy's boundary — PROVED LOCAL

For N=2^m, define the nested clock-residue energies E_(k,m)(h) from PR #531. The exact parallelogram identity gives

    E_(k+1,m)−E_(k,m)
      = 1/(4·2^k) Σ_(j<2^k)|B_(j,0)−B_(j,1)|² ≥0.

Summing k=0,...,m−1 yields

\[
\boxed{
1-|W_N(h)|²
=\sum_{k=0}^{m-1}\frac1{4·2^k}
\sum_{j<2^k}|B_{j,0}-B_{j,1}|².
}\tag{SE6}
\]

Thus π normality would require **full energy escape** (RHS→1) for each h≠0, not merely some strictly positive contrast. The 2-adic next-bit flip is a statement about valuations, not a lower bound on these complex phase contrasts.

RH's Weil positivity is a nontrivial arithmetic criterion tied to the signed completed explicit formula; here every squared branch contrast and every Fejér kernel is positive for **all sequences**. Hence their positivity alone is vacuous for π normality. The nontrivial step is a source-selected **quantitative upper bound on collisions** or **quantitative lower bound on total energy escape**, not a fake identification with RH's zeros.

## 7. Claim boundaries

**PROVED LOCAL:** frequency-ray replication and log lower bound for non-Haar invariant measures; Fejér kernel identity and positivity; conditional mesoscopic collision normality criterion; original-source mesoscopic rational-to-real transport O(H²/N); exact finite-prefix periodic approximants; dyadic energy escape identity. **REFUTED universal shortcuts:** positivity⇒Haar, 2-adic clone⇒real antiphase, source-moment alone⇒normality, finite approximate phases⇒all-horizon distribution. **OPEN:** the source-selected all-horizon collision bound SE3 or any true signed Weyl saving for original literal-zero π; RH.

**Next decisive proof:** establish for some 0<α<1/2 a uniform C_(N,floor(N^α))(x)≤C or even o(log N) from the authentic four-pole source and zero seed, with exact carry/denominator constraints, and refute the same estimate for H-shadow and coherent wrong seed. This would be a genuine proof of base-16 π normality, so no novelty/priority claim is made without complete proof and hostile external review.
