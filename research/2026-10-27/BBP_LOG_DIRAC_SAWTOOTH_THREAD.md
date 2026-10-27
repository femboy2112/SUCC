# Operation Logarithmic SUCC — authenticated BBP Dirac comb, arithmetic sawtooth and Mellin aliasing

**2026-10-27 · independent additive research child of SUCC PR #332.** Source-typed inputs: #323/#324 (original BBP positive Green tail), #330 (real/adic memory), #332 (all-rank transport), and READ-ONLY sibling #333 (the exact two-channel chiral source). Oily–Macaroni PR #310 supplies the existing scalar-weight no-go and Gamma-log grading. Original signed four poles, zero seed, historical proofs, archives and main remain unchanged. π normality and RH remain **OPEN**. Classical sampling/Euler–Maclaurin/Mellin facts are credited rather than claimed new.

## 0. Source, indexing and logarithmic coordinate

Use the original signed source, with **no changed forcing or seed**:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\qquad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

For n≥0 the inherited exact Green identity and strict bound are

$$
U_{n+1}=\pi16^n-T_{n+1},\qquad
0<T_{n+1}<\frac1{15(n+2)^2},\qquad
B:=\sum_{n\ge0}T_{n+1}=\frac{R-\pi}{15}<\infty,
$$

with R=Σ_{n≥1}r(n). All U_{n+1}>0. Let a=log16, g_h(t)=e(hπe^t), e(x)=exp(2πix), and define

$$
t_n=\log(U_{n+1}/\pi)=na-d_n,\quad
d_n=-\log(1-\epsilon_n)>0,\quad
\epsilon_n=\frac{T_{n+1}}{\pi16^n}.
$$

This is **one genuine logarithmic history selected by the original source**, not a probabilistic sampling prescription. The finite time-positions t_n are transcendental expressions but are specified exactly by rational U_{n+1} and π; no independent paths are invented. For a changed sign or non-positive carrier the correct chart must retain a sign bit, rather than declaring the history inadmissible.

## LS-1. Dirac comb and sawtooth are differential versions of the same sampling defect (CLASSICAL)

The bi-infinite reference comb and its continuous Haar reference are distributions

$$
\mathcal D_a=\sum_{j\in\mathbb Z}\delta_{ja},\qquad a^{-1}dt.
$$

With the right-open periodic Bernoulli sawtooth P_a(t)={t/a}−1/2, the distributional derivative is

$$
\boxed{\mathcal D_a-a^{-1}dt=-\partial_tP_a.}
$$

Every lattice point creates the −1 jump of P_a, and between lattice points P_a has derivative 1/a. These facts establish the equation directly on compactly supported smooth tests. The Dirac comb is not a pointwise function; the equality is in the distribution sense.

For a finite N set L=Na and let D_{a,N}=Σ_{j=0}^{N−1}δ_{ja}. With χ the indicator of the **open** interval (0,L), endpoint bookkeeping yields exactly

$$
\boxed{
D_{a,N}-\frac1a\mathbf1_{(0,L)}dt
=-\partial_t\bigl(P_a\mathbf1_{(0,L)}\bigr)
+\frac12(\delta_0-\delta_L).
}
$$

Test this against C¹ g to recover the exact finite Euler summation formula:

$$
\boxed{
\sum_{j=0}^{N-1}g(ja)-\frac1a\int_0^{Na}g(t)dt
=\frac{g(0)-g(Na)}2+
\int_0^{Na}P_a(t)g'(t)dt.
}
$$

This is classical Euler–Maclaurin's first-Bernoulli identity, not new arithmetic cancellation. Reference: NIST DLMF §2.10, https://dlmf.nist.gov/2.10; Vaughan's *Multiplicative Number Theory I*, Appendix B, https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/20.2_pp_495_519_Bernoulli_numbers_and_the_EulerMacLaurin_summation_formula.pdf.

## LS-2. Authenticated BBP arithmetic comb is a derivative of source impulses (NEW source-typed representation, PAPER-PROVED)

Let the actual finite BBP sampling measure be

$$
\mathcal D_{\mathrm{BBP},N}=\sum_{j=0}^{N-1}\delta_{t_j},\qquad
H_N(t)=\sum_{j=0}^{N-1}\mathbf1_{[t_j,ja)}(t).
$$

The original signed source ensures d_j=ja−t_j>0, so the indicated intervals are genuine. Their distributional derivatives are δ_{t_j}−δ_{ja}, hence

$$
\boxed{\mathcal D_{\mathrm{BBP},N}-D_{a,N}=\partial_tH_N.}
$$

Combining with LS-1 gives the source-weighted arithmetic sawtooth/Dirac identity

$$
\boxed{
\mathcal D_{\mathrm{BBP},N}-\frac1a\mathbf1_{(0,L)}dt
=-\partial_t(P_a\mathbf1_{(0,L)})
+\frac12(\delta_0-\delta_L)+\partial_tH_N.
}
$$

Against an arbitrary C¹ test g this is exactly

$$
\boxed{
\sum_{j=0}^{N-1}g(t_j)-\frac1a\int_0^{Na}g(t)dt
=\frac{g(0)-g(Na)}2+
\int_0^{Na}P_a(t)g'(t)dt
-\int_{\mathbb R}H_N(t)g'(t)dt.
}
$$

**This is the precise answer to the proposed Dirac-delta versus arithmetic sawtooth alternatives: both are exact and equivalent, while H_N is the source-dependent additional term.** The sign of the pulse integral is negative and was separately mutation-tested.

The source-local displacement is quantitatively controlled. Because π>3 and T_{j+1}<1/[15(j+2)²],

$$
0<\epsilon_j<\frac1{45\,16^j(j+2)^2}\le\frac1{180},\qquad
0<d_j\le\frac{\epsilon_j}{1-\epsilon_j}\le2\epsilon_j.
$$

Thus H=Σ_{j≥0}1_[t_j,ja) belongs to L¹(R), with

$$
\|H\|_1=\sum_jd_j
<\frac2{45}\sum_{j\ge0}\frac{16^{-j}}{(j+2)^2}
\le\frac8{675}.
$$

Accordingly the infinite comb difference is the distributional derivative of an L¹ source pulse field. **Do not call this finite total-variation distance between the two infinite atomic measures**: moving each Dirac mass, however slightly, has order-one total variation per site. It is a derivative/weak-test control. The Fourier test below has an unbounded logarithmic derivative, so this ordinary L¹ argument alone is not enough.

## LS-3. Exact finite-phase source correction and its convergent signed constant (PROVED LOCAL from inherited Green tail)

For g_h(t)=e(hπe^t), one has g_h(t_j)=e(hU_{j+1}) and g_h(ja)=e(hπ16^j). The pulse integral is not approximated; its exact integral is

$$
\boxed{
\int_{t_j}^{ja}g_h'(t)dt
=e(h\pi16^j)-e(hU_{j+1})
=e(h\pi16^j)\bigl(1-e(-hT_{j+1})\bigr).
}
$$

The source correction to the original real-circle Weyl sum is thus

$$
C_h=\sum_{j=0}^{\infty}e(h\pi16^j)
\bigl(e(-hT_{j+1})-1\bigr).
$$

This converges **absolutely for each fixed integer h** and obeys

$$
\boxed{|C_h|\le2\pi|h|B.}
$$

More precisely, writing S_N^{\mathrm{BBP}}=Σ_{j<N}e(hU_{j+1}) and S_N^\pi=Σ_{j<N}e(hπ16^j),

$$
\boxed{
\left|S_N^{\mathrm{BBP}}-S_N^\pi-C_h\right|
\le2\pi|h|\sum_{j\ge N}T_{j+1}
<\frac{2\pi|h|}{15(N+1)}.
}
$$

This refines the previously inherited O_h(1) Green transfer to an **explicit limiting correction constant with a quantitative tail**. It still does not establish that either Weyl sum is o(N).

For any h, Taylor's inequality |exp(ix)−1−ix|≤x²/2 gives an explicit **source linear-response** decomposition

$$
\boxed{C_h=-2\pi i h\sum_{j\ge0}T_{j+1}e(h\pi16^j)+E_h,\quad
|E_h|\le2\pi^2h^2\sum_{j\ge0}T_{j+1}^2
<\frac{2\pi^2h^2}{225}(\zeta(4)-1).}
$$

These constants are determined by the original π carrier and should not be interpreted as independent randomness or as a normality proof.

## LS-4. Exact smooth Mellin–Poisson alias decomposition (CLASSICAL, useful instrumentation)

For a smooth compactly supported window w on R and any nonzero real α, Poisson summation gives

$$
\boxed{
\sum_{n\in\mathbb Z}w(na)e(h\alpha e^{na})
=\frac1a\sum_{k\in\mathbb Z}\int_0^\infty
w(\log x)e(h\alpha x)x^{-1-2\pi ik/a}\,dx.
}
$$

For each fixed window this follows from ordinary Fourier Poisson summation applied to f(t)=w(t)e(hαe^t). Its Fourier transform is the displayed Mellin-type integral. The integer k modes are **sampling aliases**. The k=0 integral is the smooth logarithmic continuum contribution, not the full Weyl sum.

The phase for mode k is 2π(hαe^t−kt/a). It has a real stationary point precisely when k/(ahα)>0 and t=log(k/(ahα)) lies inside the sampling window. Hence relevant alias indices scale as k~ahαe^t, exponentially large across long logarithmic observation times. Smooth weighting or finitely many fixed Mellin frequencies cannot simply discard these moving aliases.

For any α≠0 and integer h≠0 the **continuous** logarithmic mean vanishes:

$$
\left|\int_0^T e(h\alpha e^t)dt\right|
\le \frac1{\pi|h\alpha|},\qquad
T^{-1}\int_0^T e(h\alpha e^t)dt\to0.
$$

Proof: change variables x=e^t and integrate e(hαx)/x by parts, bounding both endpoints and the remaining x^−2 integral. But if α=1 and a=log16, every discrete sample e(h16^n)=1: continuum Haar does **not** imply sampled Haar. This is a decisive negative control for a shortcut through the continuous flow.

For 0<Re(s)<1 and c=hα≠0, the standard oscillatory Mellin integral is

$$
\int_0^\infty e(cx)x^{s-1}dx
=\Gamma(s)(2\pi|c|)^{-s}e^{i\pi s\,\mathrm{sgn}(c)/2}.
$$

Its Laurent finite part at s=0 is **−γ−log(2π|c|)+iπ sgn(c)/2**. Thus Euler–Mascheroni is naturally present as a universal **Mellin normalization constant**, but it is present even for α=1. It does not select π or suppress the aliases without additional arithmetic input. Infinite Mellin/Poisson sums require the stated windows or an explicit distributional regularization; do not interchange unsmoothed divergent sums without proof.

## LS-5. Why scalar Gamma/Oily weighting cannot itself prove normality (PROVED conditional no-go)

For any |z_n|≤1 and scalar weights w_n=c+ε_n,

$$
\boxed{
\left|N^{-1}\sum_{n\le N}w_nz_n
-cN^{-1}\sum_{n\le N}z_n\right|
\le N^{-1}\sum_{n\le N}|\epsilon_n|.
}
$$

If |ε_n|=O(1/n), this difference is O(log N/N), **uniformly over all phase sequences**, including the worst possible nonnormal controls.

- The Euler–Mascheroni harmonic normalization H_n−log n=γ+O(1/n) has this form. Weighting samples by it simply multiplies the ordinary Weyl mean by γ asymptotically. Centering by γ makes the normalized weighted mean vanish for *every* sequence, including z_n≡1, so that success is vacuous.
- The source-graded Oily–Macaroni observer of PR #310 has |W_{n,q}(z)−C_q(z)|≤8/(8n+3). For the dyadic primitive observer with |C_q(z)|≥4/25 it is asymptotically a nonzero scalar multiple of the original selected Weyl mean. This precise obstruction is **inherited**, not a newly discovered PR #310 result. It also means a scalar Oily weight on the Dirac spikes cannot produce a new cancellation estimate.

**Non-scalar possibilities remain open**: a dynamically correlated weight depending on the actual source's pole/valuation/branch history **and** the Mellin alias index k can carry information absent from scalar Gamma weights. However, a weight built using the target Weyl sum itself is circular. The user-suggested arithmetic sawtooth is justified as a representation; any claim that it enforces equidistribution requires a genuinely discriminating signed estimate.

## LS-5b. Genuine Euler–Mascheroni counterterms cancel between the two chiral source channels (NEW scoped corollary of #333)

This gives the user's Euler–Mascheroni intuition a more **source-specific** interpretation than merely multiplying a sawtooth by γ.

From the actual rank-two Gaussian chiral source tapes recorded in #333, let

$$
r_\pm(n)=\sum_{j=0}^7\frac{c_j^\pm}{8(n-1)+j+1},\qquad
\sum_jc_j^\pm=\pm\frac{15}{4}.
$$

Define the exact rational harmonic counterterms

$$
\boxed{a_+(n)=r_+(n)-\frac{15}{32n},\qquad
 a_-(n)=r_-(n)+\frac{15}{32n}.}
$$

Because 1/(8n+j−7)−1/(8n)=−(j−7)/[8n(8n+j−7)], each a_±(n)=O(n^−2) **with an explicit constant**:

$$
|a_\pm(n)|\le\frac{C_\pm}{n^2}\quad(n\ge2),\qquad
C_\pm=\frac1{32}\sum_{j=0}^7|c_j^\pm|(7-j).
$$

Hence A_±=Σ_{n≥1}a_±(n) converges absolutely, with truncated error at N at most C_±/N. The two uncoupled cumulative sources satisfy

$$
\boxed{
\begin{aligned}
\sum_{n=1}^N r_+(n)
  &=\frac{15}{32}\log N+\frac{15}{32}\gamma+A_++O(N^{-1}),\\
\sum_{n=1}^N r_-(n)
  &=-\frac{15}{32}\log N-\frac{15}{32}\gamma+A_-+O(N^{-1}).
\end{aligned}}
$$

On authentic gluing, the logarithmic divergences and the **Euler–Mascheroni finite parts cancel exactly**:

$$
\boxed{\sum_{n\ge1}r(n)=A_++A_-.
}
$$

This is an exact source-linked use of γ: the constant is the common *harmonic-to-logarithmic conversion* in two opposite chiral channels. It is not an unexplained extra constant that must be multiplied into the sampling kernel. Independent finite Fraction checks verified the source tapes, harmonic remainders, and the rigorous O(1/N) remainder bounds. **The cancellation occurs in the source before the BBP expansion; it is not yet cancellation of e(hU_n).**

## LS-6. Rank-2 logarithmic unit lattice typing (CLASSICAL structural constraint)

The independent log directions a_2=log2 and a_3=log3 generate the rank-two free abelian group Z log2+Z log3. Since log2/log3 is irrational by unique prime factorization, the group is **dense in R**. Consequently the full two-sided pushforward

$$
\sum_{(n,m)\in\mathbb Z^2}\delta_{n\log2+m\log3}
$$

is **not locally finite**; it is not an ordinary Radon Dirac comb on R. Treating it as such produces a fake distribution. Restricting to n,m≥0 or to finite windows restores local finiteness, but creates a growing-density semigroup, not a periodic 1D comb.

The correct complete logarithmic unit lattice retains the non-Archimedean valuation coordinates:

$$
\ell(2)=(\log2,-\log2,0),\qquad
\ell(3)=(\log3,0,-\log3).
$$

Its integer span is a **discrete rank-two lattice** in x_infty+x_2+x_3=0, and projects densely to the single real log coordinate. This is exactly why SUCC needs a source/history-sensitive full S-adic carrier for rank 2. The authentic base-16 recurrence is the fourfold binary microreturn, not a primitive independent logarithmic direction. The full all-rank carrier of #332 can carry this distinction.

The chiral rank-two **Gaussian** source in sibling #333 is a separate rank notion, not automatically an S-unit Z² action. In that branch the source pieces r_±(n) have ±15/(32n) leading terms, which cancel in the original r(n)=15/(64n²)+O(n^−3). Their logarithmically divergent cumulative channels therefore combine into the summably decaying source needed for LS-2 and LS-3. This is genuine *inherited source-level signed cancellation*, but cannot yet be promoted to a signed π orbit cancellation theorem.

## LS-7. A narrowly targeted next proof gate, rather than another reparametrization

For fixed h≠0, write the regular rank-one sampling defect as

$$
\mathfrak D_N(h)=\int_0^{Na}P_a(t)g_h'(t)dt.
$$

The other components in LS-2 are an O_h(1) source-pulse correction, an O(1) endpoint term, and a bounded continuum integral. Therefore **π base-16 normality is equivalent to**

$$
\boxed{\mathfrak D_N(h)=o(N)\quad\text{for every fixed }h\ne0.}
$$

This statement is deliberately labelled **EQUIVALENT, not an advance on the existing Weyl bound**. The actual next problem is deriving a *new* inequality for the signed, moving Mellin alias collection from the full four-pole/zero-selected source, preferably with source-chiral cancellation applied before taking absolute values. Test against unchanged-forcing selector −T_n (signed logarithmic chart required), #320's zero-seeded nonnormal source mutant, rational α=1, and the rank-2 bulk/trace counterexamples of #332/#334. Prediction before testing: finite stationary alias modes are insufficient, a passive scalar Gamma/Oily weight cannot help, and rank-two full-lattice projection requires adic provenance.

## Reproducibility and scope

The Python stdlib Fraction module observational_succ/logarithmic_sampling_succ.py uses exact original four signed poles, finite Green truncations, exact polynomial sawtooth/source-pulse integrals, source chiral controls, scalar-weight invariance and rational log-shift enclosures. The focused tests and an independently authored exact probe were executed locally. The finite tests cannot establish an infinite normality theorem or rigorously certify a transcendental numerical phase. Full native SUCC suite, provenance, Lean, hosted GitHub CI and third-party review are independent pending gates.

**Claim statuses:** LS-1/LS-4/LS-6 CLASSICAL; LS-2/LS-3 source-typed PAPER-PROVED conditional on inherited Green identities; LS-5 exact universal scalar-weight no-go and inherited Oily instance; LS-7 π cancellation OPEN. Scholarly novelty of the combined kernel is unverified.
