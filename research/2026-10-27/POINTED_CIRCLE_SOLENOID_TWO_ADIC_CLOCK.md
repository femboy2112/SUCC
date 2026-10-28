# Operation Pointed Circle → Solenoid → Authentic 2-Adic BBP Time Clock

**Research round:** October 27, 2026. **Branch base:** SUCC draft PR #319, `6a187a61b19e389ed61e336a5d1c208bd21d773a`, itself stacked over #317/#316 and the Seinfeld/carry chain. **Status:** CLASSICAL topological identifications, PAPER-PROVED source-specific all-time 2-adic permutation/equidistribution theorem, EXACT FINITE instruments, strong source-mutant NEGATIVE control, and an OPEN real-circle π-normality gate. Do not claim academic priority for established topology or number theory. No original four-pole source, seed, frozen archive, main, release or prior claim is altered.

## 0. Steelman: cut the circle at one reference point

The author's idea: place the `2^k` roots of unity on the circle, hold one marked origin while refining without bound, open the circle at that point and lay its arc flat, then track what the cut does to arithmetic information and inverse histories. This can be made completely precise, with **three logically distinct operations**:

1. `R_k={j/2^k mod 1}` contains exactly `2^k` points. Its union is countable and dense, **not itself a continuum**. Taking its completion in the circle metric gives `S¹`. If one first chooses an **orientation** and an **arc-length parameterization** with a marked reference, then cuts and completes in the Euclidean interval metric, the result is `[0,1]`, with **two boundary copies** of the marked circle point. Removing the marked point instead yields a space homeomorphic to `R`, which is not a compact continuum. A marked point alone does not choose orientation or metric normalization.
2. The 16- and 2-step inverse-limit circles are canonically equivalent by retaining every fourth dyadic level. The inverse-limit fiber above a circle point is `Z_16≅Z_2`. The **solenoid** is not a circle or an interval; its cut chart also contains this Cantor-like memory fiber. The seam rejoins the two cut endpoints by adding one to the adic memory coordinate.
3. The original rational BBP values have **odd denominators**, so there is one additional canonical *odd-torsion* inverse section. Its memory differs from the unwrapped real winding section by the actual 2-adic rational state `U_n`. That exact discrepancy is the bridge to a source-specific time-residue theorem.

This is a source-typed reading of the user's idea, not a claim that prime `2` uniquely implies a circle or that a compact solenoid is simply `R`.

### The seam is genuinely observable

For `epsilon=2^-k` with `k>=2`, compare `epsilon` and `1-epsilon`. Their circle distance is `2epsilon→0`, while their cut-interval distance is `1-2epsilon→1`. A chart change can therefore introduce **order-one coordinate jumps** at the cut without any large circle motion. The two metric completions of the same dyadic sample set do not preserve the same nearness relation at the seam. A proof involving cutoff, differentiation, Fourier energy or limiting measures must specify which topology/observable is being transported.

## 1. Solenoid presentation and the arithmetic seam odometer

Let `T=R/Z`. Define

\[
\Sigma_{16}=\{(x_0,x_1,\ldots)\in T^{\mathbb N}:16x_{k+1}=x_k\},
\qquad \Sigma_2=\varprojlim(T,\times2).
\]

Taking every fourth coordinate is an isomorphism `Σ₂→Σ₁₆`; its inverse inserts, between `x_k` and `x_{k+1}`, the three unique coordinates `8x_{k+1},4x_{k+1},2x_{k+1}` in the correct order. Consequently the character group is `Z[1/16]=Z[1/2]`, and the projection `π₀:Σ₁₆→T` has kernel `Z₁₆≅Z₂`.

Choose a real lift `t` of the base point `x₀`. For each level there is a residue `z_k mod 16^k` such that

\[
x_k=(t+z_k)/16^k\pmod1,\quad z_{k+1}\equiv z_k\pmod{16^k}.
\]

Thus `(t,z)` with `z∈Z₁₆` describes a solenoid point, and changing the *real cut lift* by one changes the adic label by negative one:

\[
\boxed{(t,z)\sim(t+1,z-1).}
\]

Equivalently, after cutting at the marked reference `t=0`, the chart's boundary copies obey

\[
\boxed{(1,z)\sim(0,z+1).}
\]

**This is an exact adding-machine/odometer seam**, not an arbitrary probabilistic update. It accounts for the integer winding forgotten by passage from the real line to a circle. The map `z→z+1` on `Z₁₆` is minimal/equidistributed *under its own iterates*, but that fact does **not** identify the sequence of seam traversals selected by the BBP orbit.

Classical provenance: standard inverse-limit solenoids, Pontryagin duality for `Z[1/2]`, and the quotient `(R×Z₂)/Z`. See Larsen–Li, *The 2-adic ring C*-algebra of the integers and its representations*, §7 (https://citeseerx.ist.psu.edu/document?doi=f9a97aae705590f2a184359213962a52e404e3a9&repid=rep1&type=pdf); Gopal–Imam, *Periodic points of solenoidal automorphisms in terms of inverse limits*, Applied General Topology 2021 (https://doi.org/10.4995/agt.2021.14589). No new academic credit claimed for solenoid topology.

## 2. Genuine BBP cut-carry gauge and exact signed Fourier transport

Keep the source, unwrapped and in the same prescribed time coordinate:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\ U_{n+1}=16U_n+r(n+1),\quad x_n=\{U_n\}.
\]

Fix a reference mark `a∈[0,1)` (the ordinary SUCC circle uses `a=0`). In its oriented cut chart let `s_n={x_n-a}`, and define `d_n=⌊x_n-a⌋∈{-1,0}`. The new forcing offset is `r_a(n+1)=r(n+1)+15a`; let `c_{a,n+1}=⌊16s_n+r_a(n+1)⌋`. For the original mark put `c_{0,n+1}=⌊16x_n+r(n+1)⌋`, exactly the literal unwrapped integer carry.

The complete chart update and its gauge defect are

\[
\boxed{s_{n+1}=16s_n+r_a(n+1)-c_{a,n+1}},
\qquad
\boxed{c_{a,n+1}-c_{0,n+1}=d_{n+1}-16d_n}.\tag{PC-1}
\]

Proof: `s_n=x_n-a-d_n` and `x_{n+1}=16x_n+r-c_{0,n+1}`. Substitute and take the unique integral part. The defect is a **genuine coboundary**, so for every finite `N`,

\[
\boxed{\sum_{n=0}^{N-1}16^{N-1-n}(c_{a,n+1}-c_{0,n+1})=d_N-16^Nd_0.}\tag{PC-2}
\]

These identities are universal for affine circle maps, not new BBP inequalities. The source authenticity comes from retaining the literal four-pole `r`, the zero initial selector and the real integer lift, rather than treating the chart shift as a different forcing.

More importantly, the **complete signed character** is unchanged by cut choice:

\[
e(hx_n)=e(ha)\,e\!\left(\frac h{16}[c_{a,n+1}+s_{n+1}-r_a(n+1)]\right).
\tag{PC-3}
\]

If `s_{n+1}` is replaced by the exact midpoint of one of `M` equal cut bins and the **complete forcing is kept**, the error in the normalized signed Weyl mean is at most

\[
\boxed{\frac{\pi|h|}{16M}}.\tag{PC-4}
\]

This bound is independent of mark `a`, time horizon and source details, and holds at every finite `N`; for two different marked charts their signed midpoint estimates differ by at most `π|h|/(8M)`. It is stronger as a **representation budget** than a forcing-omitting estimator, but supplies **no signed saving**: it remains a quantized expression for the exact original Weyl mean. No normality can be inferred from the gauge-coboundary identity or from the fact that the seam is an odometer.

## 3. Two honest solenoid lifts and their exact 2-adic mismatch

The cancellation of even denominators in the four-pole rational expression yields

\[
\boxed{r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.}\tag{PC-5}
\]

Its reduced denominator, and the reduced denominator of every `U_n`, are odd. Let `G_odd⊂T` be the subgroup of rational phases of odd order. Multiplication by 16 is an automorphism of `G_odd`, so every `x∈G_odd` has a unique algebraic inverse-history section `σ_odd(x)∈Σ₁₆`, with coordinates `x_{-k}=16^{-k}x` **within `G_odd`**. This section is discontinuous in the ordinary circle topology (inherited Seinfeld SS-05/06).

There is a different natural lift of the **unwrapped state**: `ι_R(u)=[(u,0)]` in `(R×Z₁₆)/Z`. For `u∈Q` of odd denominator write `u=K+p/q`, `0≤p<q`, `q` odd. In the cut chart `(t,z)` above:

- winding lift `ι_R(u)` has `t=p/q`, `z=K∈Z₁₆`;
- odd-torsion inverse lift `σ_odd(p/q)` has the **same** circle coordinate and `z=−p q^{-1}∈Z₁₆`.

Hence their difference belongs to the fiber and equals precisely the ordinary rational state interpreted 2-adically:

\[
\boxed{\iota_R(u)-\sigma_{odd}(u\bmod1)=u\ \text{in the }Z_{16}\cong Z_2\text{ fiber}.}\tag{PC-6}
\]

This is an exact observable-mismatch construction, not a numerical similarity. The reduction `u↦u mod 16^k` is well defined because its denominator is odd. The two lifts are different **source operations**: one remembers real winding, the other remembers the unique odd-torsion inverse. The latter by itself is *not* the true nonautonomous backward BBP history unless the forcing tape is also retained. Both lift the authenticated affine recurrence if the corresponding forcing is lifted and the correct group homomorphism is used.

## 4. Main positive theorem: exact all-level 2-adic time equidistribution

**Theorem PC-7 (PAPER-PROVED, new source-clock consequence in this research lineage, academic priority unverified).** Extend the canceled rational forcing `r(x)=A(x)/D(x)` from positive integers to every `x∈Z₂`; every denominator factor is odd, so this is well defined and 1-Lipschitz. For any two distinct `x,y∈Z₂`,

\[
\boxed{v_2(r(x)-r(y))=v_2(x-y).}\tag{PC-7a}
\]

**Proof.** `D(x)≡1 (mod 2)` for every 2-adic x, and `D(x)-D(y)∈2(x-y)Z₂` because each linear denominator factor has even slope. Further,

\[
A(x)-A(y)=(x-y)[120(x+y)-89],
\]

whose quotient by `(x-y)` is odd. Therefore

\[
\frac{r(x)-r(y)}{x-y}=
\frac{[120(x+y)-89]D(y)-A(y)(D(x)-D(y))/(x-y)}{D(x)D(y)}
\]

is a 2-adic unit. QED. **If a prior SUCC branch already records this exact isometry, credit it as inherited; the all-time permutation below remains an independently checked consequence.**

For each integer `k>=1` define the *time-index function*

\[
F_k(t)=\sum_{j=0}^{k-1}16^jr(t-j)\in Z_2.
\]

Because every `r(t-j)` is 1-Lipschitz, `F_k(t)=r(t)+16g_k(t)` with `g_k` 1-Lipschitz. By (PC-7a), **`F_k` is again a 2-adic isometry**. Hence it induces a bijection of `Z/16^k Z`.

The original zero-initial recurrence gives, for **every** `n>=k`,

\[
\boxed{U_n\equiv F_k(n)\pmod{16^k}}.\tag{PC-7b}
\]

All earlier source terms carry a factor of `16^k`, and their denominators are odd. Therefore

\[
\boxed{\{U_n\bmod16^k :k\le n<k+16^k\}=\mathbb Z/16^k\mathbb Z}\tag{PC-7c}
\]

**with every residue appearing exactly once**; the same holds in every subsequent completed block of `16^k` times. This is not a statement about the real fractional parts `{U_n}`.

For every fixed `k>=1`, every `a` with `16^k∤a`, and every `N`, complete time blocks cancel exactly in the `k`-th 2-adic character:

\[
\boxed{\left|\frac1N\sum_{n=1}^N
\exp\!\left(\frac{2\pi ia}{16^k}[U_n]_{16^k}\right)\right|
\le\frac{(k-1)+((N-k+1)\bmod16^k)}N}\tag{PC-8}
\]

when `N>=k` (for `N<k` use bound 1). In particular the **authentic** sequence `U_n∈Z₂` is Haar-equidistributed in `Z₂`, with an explicit rate for each fixed continuous additive character. This is a true asymptotic cancellation theorem, **but on the 2-adic character group**, not on the real-circle character group needed for π normality. The ordinary 2-adic and real embeddings of a rational do not share a continuous finite-observer Fourier transport identifying these two characters.

**Exact finite validation:** `F_k` was independently enumerated as a permutation at moduli 16, 256, 4096 and 65536, and verified against direct original rational recurrence prefixes. The universal statement is proved above and does not depend on these samples.

## 5. Hostile control: even perfect 2-adic Haar + correct leading BBP decay does NOT prove π normality

**Theorem PC-9 (PAPER-PROVED source-mutant counterexample).** Define

\[
T_n^*=\frac{n+1}{(2n+1)(4n+1)(8n+1)},\qquad n\ge0,
\quad r_n^*=16T_{n-1}^*-T_n^*,\quad U_n^*=16^n-T_n^*.
\]

Then `T_0^*=1` and `U_0^*=0`; the recurrence holds at every n. The tail is strictly decreasing and positive: the polynomial

\[
(n+1)D(n+1)-(n+2)D(n)=128n^3+440n^2+424n+133>0
\]

for `D(n)=(2n+1)(4n+1)(8n+1)`, so `r_n^*>0` for all n>=1. Every denominator is odd and

\[
\boxed{\lim_{n\to\infty}n^2r_n^*=\frac{15}{64}},
\]

matching the leading asymptotic coefficient of the *original* BBP source.

The rational `T(x)=(x+1)/D(x)` is a 2-adic isometry by exactly the same odd-slope argument as PC-7a. Therefore `r^*(x)=16T(x-1)-T(x)` is an isometry as well; the time-clock proof of PC-7 applies word-for-word. Its zero-initial states visit every residue modulo `16^k` once per completed period after the initial k−1 steps, for **every k**, and are Haar-equidistributed in `Z₂`.

But `U_n^*=16^n-T_n^*` satisfies `{U_n^*}=1-T_n^*→1=0` on the real circle, hence

\[
\boxed{\forall h\in\mathbb Z\setminus\{0\},\quad
\lim_{N\to\infty}\frac1N\sum_{n=1}^Ne(hU_n^*)=1.}\tag{PC-9}
\]

This is **maximal real-circle noncancellation**. It is a countermodel for the generic implication:

> positive odd-denominator source + source isometry + uniform 2-adic time distribution + matching leading BBP decay + zero seed ⇒ real-circle normality.

That implication is **REFUTED**, with exact source-mutant receipt. The authentic full four-pole forcing is different (already `r_1^*=2158/135` versus authentic `47/15`), and this counterexample does not refute a theorem genuinely using that entire original source. **Do not erase this witness by confusing 2-adic uniformity with selected real-circle mixing.**

## 6. Another hostile theorem: circle Haar need not lift to solenoid Haar

For each `m>=1`, put `q=16m+1`, and choose odd-torsion points

\[
x_{m,j}=\frac{16j}{q},\quad 0\le j<m.
\]

Their circle empirical measures tend to Haar: for each fixed integer `h≠0`, the Lipschitz/Riemann-sum comparison with `j/m` yields

\[
\left|\frac1m\sum_{j<m} e(hx_{m,j})\right|
\le\frac{44|h|}{7}\left(\frac1{2m}+\frac1{16m+1}\right)\to0.
\]

But their **unique odd-torsion** first inverse coordinates are `y_{m,j}=j/q∈[0,1/16)`, so the fractional solenoid character has

\[
\operatorname{Re}\frac1m\sum_{j<m}e(y_{m,j})
\ge 1-\frac{\pi^2}{128}>\frac{1447}{1568}>0.
\]

Thus even Haar convergence on the circle does not imply Haar convergence of the odd-torsion lift in `Σ₁₆`. A theorem demanding full solenoid equidistribution of the original arithmetic orbit would be **strictly stronger than necessary** for base-16 normality of π; avoid silently swapping these targets.

## 7. Exact remaining π-normality obligation and possible arithmetic leverage

The strongest selected real-circle bound in the inspected lineage remains Astra PR #317/#319's logarithmic absolute loss with coefficient `1/14` plus uniform periodic/mixed-lag extensions. To prove base-16 normality of π we still need

\[
\boxed{S_N(h)=\sum_{n=1}^Ne(hU_n)=o(N),\qquad\forall h\ne0.}
\]

What changed materially is that we can now **rule out an entire class of naive proof attempts** and target a real arithmetic joint law:

1. **Source-isometric modular clock is solved.** Every fixed 2-adic character cancels over completed time blocks, with no probabilistic averaging or conjectures. The memory discrepancy between the winding and torsion solenoid sections is exactly that clock.
2. **Mixed real/adic characters are not solved.** Need a genuinely source-specific estimate for real selected phases conditioned on the perfectly balanced `U_n mod16^k` clock, or a signed combination of its classes. P-adic marginal Haar by itself does not constrain those signed conditional phases (PC-9). Asking for full solenoid Haar would be an unjustified stronger goal (section 6).
3. **The chart cut is a gauge, not a free saving.** Its seam cocycle and signed source-character identity are exact; a new inequality must exploit the arithmetic *distribution of seam-crossing and phase interactions over time*, not the cocycle identity alone.
4. **Correct adversarial controls:** the new PC-9 counterfeit with identical 2-adic uniformity/leading decay and zero anchor, plus SS-08, the same-forcing changed-seed `V_n=-T_n`, sparse-digit irrationality-2 controls, packet-regrouping controls, and the h=4/h=8 cross-digit obstruction.

**Next theorem to earn:** prove source-specific real/2-adic joint-character cancellation or a genuinely growing signed block saving in an original four-pole, zero-anchored time ensemble. That would be a new mathematical result not supplied by solenoid topology, cofinality, Haar symmetries or the 2-adic isometry alone.

**Proof firewall:** every identity and inequality in the dossier has domain, quantifiers and an explicit source tag; local computational probes corroborate finite claims, not infinite assertions. No positive Gram, generic uniform measure, classical solenoid duality or independently postulated inverse sampling replaces the actual deterministic source.
