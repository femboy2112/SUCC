# Lambert-W × zero-origin BBP: coupon coverage, signed returns and entropic amplification

**2026-11-08. Research-only paper derivations and reproducible finite computations.** Direct parent: draft SUCC #559 at `44a4a96d2180a66524f882e4a1d50309fc8c97a9`; protocol committed first at `c207e377143818f95ec12957849834e1d3113661`. Preserve the original four signed BBP poles, literal `U_0=0`, archive, integer-carry and historical provenance. **Base-16 π normality, and original-zero signed covariance decay, remain OPEN.** Classical information inequalities, coupon collector, Lambert W and Champernowne normality are not claimed as new discoveries. **SUCC already contains the strong Piatetski--Shapiro block-frequency criterion (HJA-03) and trimmed collision/entropy theorem (SCE-02); the finite cyclic Shannon/Rényi inequality below is an exact specialization of that existing mechanism.** This round contributes a Lambert-W-scheduled, explicitly testable and falsifiable interface to the original-source observable, plus the new exact BBP bulk certificate and holdout.

## Notation and the type firewall

For a finite digit string `d_0,...,d_(N-1) ∈ {0,...,15}`, define its **cyclic** length-k word at start i as `w_(i,k)=(d_i,...,d_(i+k-1))` with indices mod N; require `1≤k≤N`. Let `B=16^k`, `C_w=#{i:w_(i,k)=w}`, `p_w=C_w/N`, and

\[
D_k(N)=\sum_{w}(C_w-N/B)^2,
\quad E_k(N)=\frac{B}{N^2}D_k(N)=B\sum_wp_w^2-1. \tag{LWE0}
\]

For real entropies, use natural logarithms; `H_1(p)=-Σp log p` and `H_2(p)=-log Σp²`. The collision-entropy deficit is

\[
\Delta_k(N)=k\log16-H_2(p_k)=\log(1+E_k(N)). \tag{LWE1}
\]

`D_k` counts *symbolic* hexadecimal word collisions; it is NOT the #544 continuous-phase signed Weyl sum. Exact source provenance for this finite pi string is #557's `CERTIFIED_HEX_16384.txt` and the independently computed additional prefix in this branch.

## LWE-01 — Lambert-W is the inverse *coupon coverage* clock, not E_k itself (CLASSICAL)

For **independent uniform draws from B distinct words**, let T_B denote the first time all words have appeared. Classical coupon collection gives

\[
\mathbb ET_B=BH_B=B(\log B+\gamma)+\frac12+O(B^{-1}). \tag{1}
\]

Set `B=e^x=16^k`. Inverting the leading `N=e^x(x+γ)` with the principal Lambert function, `W_0(z)e^{W_0(z)}=z`, yields

\[
\kappa_W(N)=\frac{W_0(e^\gamma N)-\gamma}{\log16},\quad
B_W^{cont}(N)=\frac{N}{W_0(e^\gamma N)},\quad
k_W(N)=\max\{1,\lfloor\kappa_W(N)\rfloor\}. \tag{2}
\]

For large N, `k_W=log_16 N−log_16 log N+O(1)`; the integer floor makes a factor-16 staircase. At the continuous reference threshold `N=B(log B+γ)`, the independent-draw expected number of *missing* types is

\[
B(1-1/B)^N\longrightarrow e^{-\gamma}, \tag{3}
\]

and the classical coupon-cover limiting success probability is `exp(−e^(−γ))`. **Neither the independent coupon law nor its Gumbel limit is asserted for the overlapping, deterministic BBP digit stream.** `N E_k(N)` has iid expectation `B−1` for N≥2k by inherited FRH-06; it does NOT contain an intrinsic `k B` factor. The W clock is a *design choice*, not a physical constant.

## LWE-02 — exact signed collision/return-energy law (PROVED, all finite strings)

For N observed word starts, put `P=#{0≤i<j<N : w_i=w_j}`. Since `Σ_wC_w²=N+2P`,

\[
\boxed{D_k(N)=N(1-B^{-1})+2\sum_{0\le i<j<N}(\mathbf1_{w_i=w_j}-B^{-1}).}\tag{4}
\]

This is the *actual* signed interference correction to the count-space displacement; the individual collision indicators are nonnegative, but the centered off-diagonal terms can have both signs. The direct proof is the displayed expansion, requiring no randomness.

For **noncyclic** chronological windows, define `M=L−k+1` from L input digits, and `R_ell=Σ_(i=0)^(M−ell−1) 1_(w_i=w_(i+ell))`. Then

\[
D_k^{lin}(M)=M(1-B^{-1})+2\sum_{\ell=1}^{M-1}\left[R_\ell-\frac{M-\ell}{B}\right]. \tag{5}
\]

This is the discrete signed Green–Kubo/lag formulation. Cyclic counts at horizon L are a different instrument: **do not** insert them into (5) without their wrap boundaries. Under the *independent uniform digit* reference, even for overlapping windows, `E R_ell=(M−ell)/B`; the equality constraints on `k+ell` digits have exactly `ell` free digit coordinates. This null expectation is NOT source-selected sign control.

## LWE-03 — finite Shannon/Rényi amplification theorem (PROVED, deterministic)

**Theorem.** For **every** finite digit string of length N, integer depths `1≤t≤k≤N`, let `p_t` be its cyclic t-word law. Then

\[
\boxed{\left\lfloor\frac{k}{t}\right\rfloor
D_{KL}(p_t\|u_t)\le\log(1+E_k(N)),}\tag{6}
\]

where `u_t` is uniform on `16^t` words and the KL divergence is in nats. Furthermore, by Pinsker,

\[
\boxed{\|p_t-u_t\|_1
\le \sqrt{\frac{2\log(1+E_k(N))}{\lfloor k/t\rfloor}}.}\tag{7}
\]

*Proof.* Choose a uniformly random cyclic starting position I. The k-word `W_k=(d_I,...,d_(I+k−1))` can be partitioned into `q=floor(k/t)` successive nonoverlapping length-t blocks and one remainder of length <t. **Every one of these t-blocks has marginal law p_t**, because I shifted by any fixed offset remains uniform modulo N. Shannon subadditivity gives

`H_1(p_k)≤q H_1(p_t)+(k−qt)log16`.

Rényi-2 entropy never exceeds Shannon entropy, `H_2(p_k)≤H_1(p_k)`. Subtract from `k log16` and use `k log16−H_2(p_k)=log(1+E_k)` to prove (6). Standard Pinsker, `D_KL(p_t||u_t)≥||p_t-u_t||_1²/2`, proves (7). No limit, coupling, independence or BBP premise enters. QED.

**Contrapositive, the key signal amplifier:** if a fixed depth t has KL deficit at least `δ>0` along some horizons, then at any deeper k

\[
\boxed{E_k(N)\ge\exp(\delta\lfloor k/t\rfloor)-1.}\tag{8}
\]

Thus a persistent finite-depth digit bias *must* become an exponentially amplified collision-energy excess at growing observation depth. This is a mathematical expression of the user's recursive observer intuition, not a fitted model of π dynamics.

## LWE-04 — subexponential *Lambert-depth* collision deficit suffices for normality (PROVED implication, source premise OPEN)

Let `k(N)=k_W(N)` from (2). Then `k(N)→∞`, `k(N)~(log N)/(log16)` and for all sufficiently large N

\[
\frac{N}{16W_0(e^\gamma N)}<16^{k(N)}\le\frac{N}{W_0(e^\gamma N)}.\tag{9}
\]

**Theorem.** For any infinite hexadecimal digit sequence, if

\[
\boxed{\log(1+E_{k(N)}(N))=o(\log N)}\tag{10}
\]

along **every integer N**, then the sequence is normal in base 16. Proof: fix t; for N large k(N)≥t, and (7) implies `||p_t(N)−u_t||_1=o(1)` because floor(k/t) is order log N. Cyclic and ordinary noncyclic t-word frequencies differ by O(t/N). This holds for every fixed t, which is the definition of normality. QED.

This proof also gives **quantitative fixed-t distribution error** from any measured or proved upper bound on the high-depth energy via (7). In particular, each of the following increasingly permissive *source-selected hypotheses* suffices:

- `D_k(N)≤C N` (the previous diffusive gate, stronger than necessary);
- `D_k(N)≤N^{1+o(1)}`, or concretely `D_k(N)≤N(log N)^C` for a fixed C;
- `max_w C_w(N)≤N^{o(1)}`, or concretely `max_w C_w(N)≤(log N)^C` for a fixed C≥1.

For the third bullet, `Σp_w²≤(max C_w)/N` gives

\[
\boxed{1+E_k(N)\le\frac{16^k}{N}\max_w C_w(N).}\tag{11}
\]

At the W depth, `(16^k/N)≤1/W=O(1/log N)`; therefore the logarithm of the RHS is `o(log N)` whenever `max C_w=N^{o(1)}`. For the second bullet, `(16^k/N²) D≤ (D/N)/W`, giving the same conclusion. **These bounds remain UNVERIFIED for π; their derivation does not supply an arithmetic estimate.** They are strictly stronger than normality, as LWE-06 proves. This is not a new proof of a famous open theorem.

## LWE-05 — dense near-return epochs suffice; rare clumps are permitted (PROVED)

A more compatible version of (10) requires it **only at an increasing sequence of horizons N_j** with `N_j→∞` and `N_(j+1)/N_j→1`:

\[
\boxed{\log(1+E_{k(N_j)}(N_j))=o(\log N_j).}\tag{12}
\]

Then the sequence is still normal. Formula (7) establishes every fixed-t cyclic marginal approaches uniform on these horizons. For `N≤M` the cyclic t-word laws obey, by comparing their `M−t+1` and `N−t+1` linear starts and the two sets of `(t−1)` wrap starts,

\[
\boxed{\|p_{t,M}-p_{t,N}\|_1
\le\frac{2(M-N)+2(t-1)}{M}.}\tag{13}
\]

Let `N_j≤N≤N_(j+1)`, set M=N and N=N_j in (13); the bound vanishes because the relative checkpoint gaps do. Every fixed word therefore has the correct limiting frequency along *all* N. QED.

**This is a mathematically valid near-return/stable-point formulation.** It does not require exact histogram reset, forbids no finite clump, and does not extrapolate observations at a sparse geometric sequence of checkpoints (`N_j=2^j` does **not** satisfy the ratio-one hypothesis). It supplies another unproved original-zero source target, not a theorem that it occurs.

## LWE-06 — decisive normal-but-spiky counterexample (PROVED using classical normality existence)

Take a known base-16 normal sequence, e.g. the classical base-16 Champernowne concatenation. After copying `M_j=2^(2^j)` base digits (j≥2), insert a block of `L_j=2^(3·2^(j−2))=M_j^(3/4)` zeros, preserving the order of all other digits. The density of inserted symbols is zero: `Σ_(i≤j)L_i /M_j→0`, and similarly at all intermediate horizons. For any fixed t, only the inserted digits and O(t) windows at insertion boundaries differ from the unmodified normal path in o(N) positions. Thus the resulting infinite sequence **is still base-16 normal**.

At the completion N_j of the jth inserted zero block, `N_j~M_j` and the observed `0^k` word occurs at least `L_j−k+1` times, for `k=k_W(N_j)=O(log N_j)`. Since `N_j/16^k=O(log N_j)`,

\[
D_{k}(N_j)\ge (L_j-k+1-N_j/16^k)^2=N_j^{3/2+o(1)}. \tag{14}
\]

So the diffusive `D=O(N)`, every polylog-weighted `D≤N(log N)^C`, and even the subpolynomial-entropy condition (10) **fail** along these horizons, while normality remains true. Therefore **LWE-04 is strictly stronger than normality**, not another equivalent criterion and not a necessary anti-clumping principle. The dense-checkpoint criterion LWE-05 can tolerate sparse such spikes if there exist adequate checkpoints; their existence is a separate obligation.

## LWE-07 — fast exact source certificate for 40,960 π hexadecimal digits (PROVED finite enclosure + OBSERVED)

The authentic r(n) satisfies the algebraic identity

`r(n)=(120n²−89n+16)/[(2n−1)(4n−1)(8n−7)(8n−3)]>0`

and the **classical imported** BBP identity `π=Σ_(n≥1)16^(1−n) r(n)`. Let K=N+G, Q=16^K and let

\[
L=\sum_{n=1}^{K}\left\lfloor Q\,16^{1-n}r(n)\right\rfloor\in\mathbb Z. \tag{15}
\]

Each term-floor loss is <1, so the K-term loss is <K. The monotone original source and geometric tail give

`Q Σ_(n>K)16^(1−n)r(n) ≤ (16/15)r(K+1)<1` for `K≥2`

(using inherited source envelope `r(m)≤47/(15m²)`). Hence

\[
\boxed{L\le Q\pi<L+K+1.}\tag{16}
\]

If `floor(L/16^G)=floor((L+K+1)/16^G)`, the entire first N fractional hexadecimal digits of π are fixed by that one integer division; *the integer-part 3 is removed afterward*. This does not use a π digit table or floating rounding. It is a new efficient implementation of classical BBP summation, not a novel π formula. For `N=40,960`, `G=24`, `K=40,984`, the two floors coincide. The same output's first 16,384 characters match #557's separately generated, per-step zero-origin rational source certificate exactly. The implemented full-source four-pole and simplified forms agree algebraically and in independent finite checks.

**Protocol qualification:** The preregistered first attempt to replay each full rational state was halted at n≈12,288 because of the severe increasing common denominator cost, **before any new holdout statistic was examined**. The replacement uses the exactly equivalent BBP signed forcing and the stronger *global rational interval* above, with identical frozen N and observables. The source is still the unique zero-seeded recurrence through the exact Green identity. These are two algorithms observing the same invariant, not two statistically independent digit samples. This distinction is disclosed in the validation record.

## LWE-08 — finite held-out π observations and hostile controls (OBSERVED)

The exact N=40,960 source certificate yields at its **Lambert depth k=3**:

- all **4096 of 4096** possible k=3 words seen at least once; the first chronological occurrence of full depth-3 coverage is at digit position **31,816** (no cyclic wrap);
- `D_3=40,850`, `D_3/N=0.997314453125`, `E_3=817/8192=0.0997314453125`, `Δ_3≈0.0950660094`, maximum individual word count 23 (average count 10);
- the signed pair term in (4) is exactly **−50**, while the diagonal contribution is `N(1−1/4096)=40,950`;
- the reference independent-coupon mean complete-coverage time at k=3 is `4096 H_4096≈36,434.3456`. This is NOT the expected cover time for overlapping actual BBP windows.

Before the scheduled Lambert depth transition, at N=32,768 the selected depth k=2 has `D_2/N≈1.010498`, `E_2≈0.0078926`; after the depth transition at N=36,864, k=3 has `D_3/N≈0.992513`, `E_3≈0.11028`. **Most of the apparent raw-energy jump is the factor-16 increase in observed word types, not an observed physical energy injection.**

The 16 seeded same-histogram shuffles at N=40,960 have `D_3/N∈[0.955078125,1.034228516]` and max word counts between 21 and 27; the real source is inside both observed ranges. Sorting the identical digits gives `D_3/N≈2546.37`, period-16 cycling gives 2550 and a constant sequence gives 40950. The signed first-64 linear-lag return correction for the source is approximately −51.46; the *all-lag* cyclic and noncyclic correction are different instruments and are recorded separately. This finite evidence does not establish an all-N rate or a mechanism that actively counteracts clumps.

## LWE-09 — exact cyclic trimmed-source entropy inequality (PROVED specialization of inherited HJA/SCE)

This addresses an important defect of any untrimmed high-depth test: **normal sequences may have sparse giant clumps**. Let `G ⊆ {0,...,N−1}` be an arbitrary retained subset of `M=(1−δ)N` original start times; retain the original cyclic depth-k words, and define their conditional law `q_k`. Set `C_G=16^k Σ_w q_k(w)^2`. The retained subset need NOT be shift-invariant. The **full N-position law** satisfies `p_k=(1−δ)q_k+δ r_k` for some law `r_k`, and Shannon concavity yields `H_1(p_k)≥(1−δ)H_1(q_k)≥(1−δ)(k log16−log C_G)`. Combining with the *full-window* cyclic entropy subadditivity from LWE-03 gives for every t≤k:

\[
\boxed{\lfloor k/t\rfloor\,D_{KL}(p_t^{full}\Vert u_t)
\le\delta k\log16+(1-\delta)\log C_G.}\tag{17}
\]

This is a finite deterministic inequality: **no independence or stationarity is assigned to the retained positions**. If at `k=k_W(N)` and all N (or dense near-return checkpoints), there exist retained subsets with `δ_N→0` and `log C_{G_N}=o(log N)`, then by (17) every fixed depth t becomes uniformly distributed and the original digit sequence is normal. The original zero-seed arithmetic premise is **OPEN**.

This is a cyclic-window, zero-boundary version of the SUCC October `PI_TRIMMED_JOINT_ENTROPY.md` theorem (HJA-08/SCE-02); the proof uses the full cyclic sampling law and therefore does not incur the noncyclic `O(k/N)` boundary term. Our new `trimmed_cyclic_entropy_bound` is an explicitly scoped, deterministic implementation selecting the **earliest fixed number of occurrences per word** and preserving the source-time labels. A synthetic sample with a 500-symbol zero spike demonstrates that trimming reduces collision excess but never licenses a normality claim from one finite sample. The key next task is to prove the above bounds with `δ→0` from the authentic four-pole source, rather than fitting a threshold after observing the output.

## LWE-10 — exact next source-selected proof gate (OPEN)

The bridge to normality now has two complementary formulations:

1. **Entropy-growth gate (new useful strength):** prove `Δ_{k_W(N)}(N)=o(log N)` for all integer N, or on dense relative-gap checkpoints. A sufficient stronger estimate is `sup_{w at depth k_W(N)} C_w(N)≤N^{o(1)}`; this asks for subpolynomial occupation of shrinking digit cylinders, not full signed prime-phase independence.
2. **Existing #544 source-signed gate:** prove the original-zero, all-epoch real complement forcing-corrected signed-lag covariance decays. The new entropy bridge supplies **no bound** on that covariance, and cannot simply be substituted for it by positive Parseval identities. Transport from BBP prime/carry source to the required microscopic word occupancy is UNVERIFIED.

**The missing arithmetic step remains:** an independent original-zero, all-N or dense-checkpoint estimate showing that enough of the four-pole source's real phase fails to accumulate in recurring tiny cylinders. The coherent wrong-seed, dyadic epoch ghosts, periodic completions, normal-but-spiky counterexample, and same-source analytic deformations are required negative controls. Nothing in this dossier proves base-16 π normality.

## References

- SUCC #557 and #559 (original certified BBP source, exact digit-word Fourier sectors, de Bruijn flow, and iid comparison); do not reattribute their proofs.
- SUCC `research/2026-10-24/PI_HYPOTHESIS_A_SYNTHESIS.md` (strong Piatetski–Shapiro criterion) and `PI_TRIMMED_JOINT_ENTROPY.md` (source-trimmed collision bridge); this work refines their scheduling and cyclic finite constants, not their classical idea.
- NIST DLMF §4.13, Lambert W, https://dlmf.nist.gov/4.13
- Mitzenmacher–Upfal, *Probability and Computing*, standard coupon-collector and Gumbel threshold; https://randall.math.gatech.edu/Randalgs/mitzbook.pdf
- Bugeaud, *Distribution modulo one and Diophantine approximation*, Champernowne example, https://staff.dc.uba.ar/becher/aa/Bugeaud2012.pdf
- Classical Rényi entropy ordering, Shannon subadditivity, Pinsker/KL inequality; all finite applications are explicitly derived above.
- SUCC #544 current signed-lag/chronological carry drafts, separate source/authority scope.
