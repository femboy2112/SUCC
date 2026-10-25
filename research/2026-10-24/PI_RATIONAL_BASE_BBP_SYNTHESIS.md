# Operation Rational-Base Carry Forge: Pascal 3/2 ↔ 11/10 ↔ decimal and BBP

**2026-10-24 | RESEARCH DRAFT | π NORMALITY OPEN.** Parent [#275](https://github.com/femboy2112/SUCC/pull/275) at 7c5d5b8856a1d132fb941ae40c946c0565918b36; source/Mahler proofs from [#272](https://github.com/femboy2112/SUCC/pull/272). Siblings [#273](https://github.com/femboy2112/SUCC/pull/273) and [#274](https://github.com/femboy2112/SUCC/pull/274) consulted, not merged. Main untouched, no historical archives edited, no new Lean authority or scholarly priority claim.

## Result in one paragraph

The integer rational-base p/q algorithm produces exact finite Pascal-additive objects. The low L digits in this algorithm are equivalent to the integer modulo p^L, **not** to a modulus q^L. In particular, 11/10 suffixes of the actual BBP literal integer lift are an 11-adic observer even though the evaluation denominators are powers of 10 (supported at 2 and 5). We prove an exact prime-11 clock and an authentic source-labelled Fourier/carry decomposition. Separately, the k-th *Pascal difference* of the positive base-11 source gives exponentially accurate rational approximants to the decimal π orbit, with error below (2/3)^k π/16. Yet a sharp counterexample shows that all-depth 11/10 suffix uniformity alone does **not** imply real-circle or hexadecimal normality. The missing theorem is authentic real source-selected signed Fourier cancellation, or a genuine cumulative carry loss.

## 1. Classical rational-base algorithm and long additive objects

For coprime integers p>q≥1, recursively divide

$$
qN_i=pN_{i+1}+a_i,\qquad 0\le a_i<p,\quad N_0=N,\quad N_L=0.
$$

Every nonnegative integer N terminates, and

$$
\boxed{N=\frac1q\sum_{i=0}^{L-1}a_i(p/q)^i.}
$$

This is the canonical rational-base **integer** expansion, not the Rényi greedy real β-expansion. It is classical (Akiyama–Frougny–Sakarovitch, [original treatment](https://www.irif.fr/~cf/publications/AFSwords05.pdf)). For p=q+1,

$$
N_{i+1}=N_i-\left\lceil N_i/p\right\rceil,\qquad
\boxed{N=\sum_{j=0}^{L-1}q^{-j-1}\sum_{i=j}^{L-1}\binom ij a_i.}
$$

The second formula expands (1+1/q)^i and exchanges two finite sums: an exact Pascal-additive representation with source-conditioned carries. Integer p has least-to-most significant digits 0,1,...,p−1. Thus (210) in radix 3/2 represents 3 and (A9876543210) in radix 11/10 represents 11 (A=digit 10). All identities are directly checked by independent rational arithmetic.

The number of digits satisfies L(N)=log(N)/log(p/q)+O_{p,q}(1) by the bounds (q/p)^i N−p/(p−q)≤N_i≤(q/p)^iN. For the BBP integer lift C_n=floor U_n≈16^n π/16, its 11/10 representation has length

$$
L_{11/10}(C_n)=\frac{\log16}{\log(11/10)}\,n+O(1)
\approx29.09016\,n+O(1).
$$

This establishes huge structured additive forms, **not** digit frequencies.

## 2. The unexpected direction: 11-adic addresses, 10-adic denominators

Telescope the first L digit steps:

$$
q^LN=\sum_{i=0}^{L-1}a_ip^iq^{L-1-i}+p^LN_L.
$$

Since q is invertible modulo p^L, the word w=(a_0,...,a_{L−1}) uniquely specifies the residue

$$
\boxed{r_w\equiv q^{-L}\sum_{i=0}^{L-1}a_ip^iq^{L-1-i}\pmod{p^L}.}
$$

Conversely, congruent N modulo p^L have exactly the same first L digits, by induction on the division steps. Therefore **all** p^L words occur once as low-digit words modulo p^L. The compatible infinite decoder is a prefix-ultrametric isometry of sets Z_p↔digit words; no additive isomorphism is claimed.

For 11/10: a_0=10N mod11=−N mod11; the low L digit positions are determined by N modulo 11^L. The evaluated sums have denominators 10^{i+1}, reflecting primes 2 and 5. Confusing these two typed coordinates is a false arithmetic transfer.

## 3. Authentic BBP integer-lift observer and exact 11 clock

Keep the original source **unchanged**:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

Writing U_n=C_n+y_n, where C_n is the **literal** integer floor and y_n∈[0,1), gives

$$
c_n=\lfloor16y_{n-1}+r(n)\rfloor,\quad
\boxed{C_n=16C_{n-1}+c_n
=\sum_{j=1}^{n}16^{n-j}c_j.}
$$

No centered *pair* carry is substituted for c_n. For every integer modulus m, the exact additive character is

$$
\boxed{e(aC_n/m)=\prod_{j=1}^{n}e(a16^{n-j}c_j/m),\qquad e(x)=e^{2\pi ix}.}
$$

The source's rational-base 11/10 suffix is the preceding mod-11^L decoder applied to C_n. Moreover

$$
\boxed{\mathrm{ord}_{11^L}(16)=5\cdot11^{L-1}.}
$$

Proof: ord_11(16)=5 and v_11(16^5−1)=1; apply the standard odd-prime lifting-of-exponents lemma. This is an index-two subgroup of the unit group at every level. Therefore the homogeneous 16-clock cannot alone fill every nonzero residue, and the source carries must be retained. This **does not** show their frequencies are uniform.

## 4. Source-specific 11 → 10: take the k-th Pascal difference

Write E for integer-index forward shift and Δ=E−I. The already proved positive base-11 source operator is

$$
H_{11}=(I+2E)/3,\quad H_{11}(16)=11,\quad
\boxed{H_{11}-I=(2/3)\Delta.}
$$

Let V_j=H_{11}^jU_0. Its **k-th difference in j** is

$$
\boxed{D_k=\sum_{j=0}^{k}(-1)^{k-j}\binom kj V_j
=(H_{11}-I)^kU_0=(2/3)^k\Delta^kU_0.}
$$

From the original positive BBP tail U_n=16^nα−T_n, with α=π/16, T_n=∫_0^1t^n dρ(t), ρ positive and total mass α, define R_k=∫(1−t)^k dρ(t). The identity above becomes

$$
\boxed{D_k=10^k\frac{\pi}{16}-(-2/3)^kR_k},
\qquad 0<R_k<\frac{\pi}{16}\quad(k\ge1),
$$

and hence the **rigorous geometric real error**

$$
\boxed{|D_k-10^k\pi/16|<(2/3)^k\pi/16.}
$$

The inherited BBP endpoint estimate gives R_k~Γ(1/8)/(32k^{1/8}). The inherited Mahler profile gives the independent exact dyadic valuation

$$
v_2(D_k)=3k-s_2(k)-1,
$$

so D_k→0 in the 2-adic metric even while its real trajectory follows powers of 10. One must not equate those topologies.

This decimal filter is a **specialization of the previously proved signed-Pascal family**, not an entirely new source normality theorem. Its new role here is the exact factorization through the *positive* base-11 filter and the rational-base integer carry lift. For every consecutive pair q,q+1 with 1≤q≤15, H_{q+1}=((15−q)I+qE)/15 yields H_{q+1}−I=(q/15)Δ, and geometric error when q<15. Thus 3/2 and 11/10 instantiate one operator family.

## 5. An authenticated mixed real/11-adic Fourier instrument

For a good-prime selected window W, m=11^L, word w and its integer residue r_w, set

$$
\mathcal F_W(h,a;m)=|W|^{-1}\sum_{n\in W}e(hy_n+aC_n/m).
$$

Finite character orthogonality gives an **exact source-selected identity**:

$$
\boxed{
|W|^{-1}\sum_{\substack{n\in W\\\mathrm{suffix}_L(C_n)=w}} e(hy_n)
=\frac1m\sum_{a=0}^{m-1}e(-ar_w/m)\mathcal F_W(h,a;m).
}
$$

All actual BBP source states, zero-initial selection, literal integer carries and real endpoints remain. An estimate only at h=0 controls 11/10 digit frequencies, not real-circle Fourier cancellation. Bounding all h≠0 including a=0 simply includes the original Weyl-sum obstruction. The next theorem must exploit *signed source-specific correlations*, for example in the authentic zero-centered carry pair mask and conditional p=11 fibers.

## 6. Sharp counterexample: all-depth 11/10 suffix fairness without real normality

Take independent fair binary symbols d_j∈{0,1}, and let P_n=∑_{j=1}^n16^{n-j}d_j. For each m coprime with 16, the finite-state chain P_{n+1}=16P_n+d_{n+1} mod m has uniform stationary law (both possible transition maps are permutations). It is irreducible: with T=ord_m(16), a block of length mT returns the starting state modulo m, except that choosing r ones at positions with exponents multiples of T shifts it by any prescribed r modulo m. The all-zero state has a self-loop, so the chain is aperiodic. Classical finite-state Markov ergodicity gives asymptotically uniform residues for every such m simultaneously, almost surely (countable intersection).

Choose any sequence on this full-measure event. The real number x=∑d_j16^{-j} contains **only digits 0 and 1** in base 16 and is not normal. Nevertheless the rational-base 11/10 low words of its integer prefixes P_n are uniformly distributed for *every fixed length L* because they biject with P_n modulo 11^L. This changes the source formula and is **not a counterexample to the real BBP theorem**; it refutes a source-agnostic implication from rational-base digit balance to hexadecimal normality.

## 7. Finite receipts and actual remaining debt

The source, tests and probe in this PR were run independently using exact Python Fraction arithmetic, not floating-point BBP states. Five genuine good-prime windows p=73,137,281,521,1153, lengths 27,51,105,195,432, gave mod11 uniform TV respectively 85/297, 82/561, 124/1155, 197/2145, 73/1584. An independent rigorous 560-term Machin interval certified actual π integer-lift agreement on those **finite windows only**; an untested near-one carry boundary can change the floor elsewhere.

Selected successor-close *pair* carries at p=137,281,521 and radii 1/4,1/16 were tabulated by equality of C_s modulo 11, retaining all diagonals and separate off-diagonal counts. For p=521, radius 1/4, same-label offdiagonal count E=1716, central Z=112; different-label E=17116, Z=1044. A finite proximity to 1/16 is not a scale-uniform estimate.

**Precisely open:** Prove a nontrivial source-specific signed mixed Fourier bound, an all-scale real central-carry contraction, or a genuine same-law independent-multiplier invariance plus all-scale collision dimension. The existing rational-base digit-frequency theorem for integers (Morgenbesser–Steiner–Thuswaldner, [arXiv:1203.4919](https://arxiv.org/abs/1203.4919)) does **not** apply to the specific BBP-selected integer lifts as a free consequence, and does not prove pi normality.

Read [RBP claim supplement](../../docs/CLAIM_SUPPLEMENT_RATIONAL_BASE_PI.md), [production module](../../observational_succ/pi_rational_base_carry.py), [exact tests](../../tests/test_pi_rational_base_carry.py), and [reproducible probe](../../scripts/pi_rational_base_carry_probe.py). **No Lean theorem, independently peer-reviewed novelty claim, or π-normality proof is asserted.**
