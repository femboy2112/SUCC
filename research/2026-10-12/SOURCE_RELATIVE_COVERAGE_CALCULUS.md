# Source-relative SUCC coverage: collision, transport, and constructive lower bounds

**Research checkpoint:** October 12, 2026 UTC; based on [SUCC Gaussian moat PR #23](https://github.com/femboy2112/SUCC/pull/23) at commit b606b78bb8ea716fd30fe858043b971c0d43a788.

**Evidence status:** classical finite probability and elementary Gaussian arithmetic, with complete derivations below; exact source-relative software certificates and adversarial controls. Mathematical novelty and independent scholarly priority are **UNVERIFIED**. No claim to reproduce OpenAI's Gaussian moat existence theorem for every step bound, and no physical/quantum/RH inference.

## Objects and source-identity obligations

A coverage frame contains an explicitly declared finite alphabet \(\Omega\), an actual probability measure \(P\), a strictly positive reference probability \(\pi\), a source identifier, an observation name, and a causal epoch. Changing the observer or source must transport **both** \(P\) and \(\pi\), through a declared kernel. Equal labels are not authentication of two real events. Independence requires a distinct proof obligation; a checked Boolean assumption does not manufacture it.

The target relevant to OpenAI, *Bounded-Step Walks on Gaussian Primes* (September 26, 2026), is \((\tau,\beta)\)-coverage of a field \(G\) with \(p\) residues:
\[
\#\{u:P(u)<\tau/p\}<p^{1-\beta}.
\]
Their [primary coverage transfer argument](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex) uses geometric sampling, conditional repeated continuations, a joint entropy budget, and small-list tests. The following finite theorems are valid in their domains but do **not** automatically satisfy those arithmetic hypotheses.

## C1. Sharp lower bound on reference-relative coverage

Fix \(0<\tau<1\). Let
\[
E=\{x:P(x)<\tau\pi(x)\},\qquad
\kappa=\chi^2(P\|\pi)=\sum_x\frac{(P(x)-\pi(x))^2}{\pi(x)}.
\]
Then
\[
\boxed{\pi(\Omega\setminus E)\ge\frac{(1-\tau)^2}{\kappa+(1-\tau)^2}.}\tag{C1}
\]
**Proof.** If \(E=\varnothing\), the statement is immediate. Otherwise set \(e=\pi(E)\), \(a=P(E)\). We have \(0<e<1\), since \(e=1\) would give \(1=a<\tau\). Also \(a<\tau e\). Apply Cauchy-Schwarz on \(E\) and its complement:
\[
\kappa\ge\frac{(a-e)^2}{e}+\frac{(a-e)^2}{1-e}
=\frac{(e-a)^2}{e(1-e)}
>\frac{(1-\tau)^2e}{1-e}.
\]
Rearrange. This is a classical two-cell divergence bound, sharp in the limiting sense: assign relative density \(\tau\) on \(E\), uniform relative density on the complement, then perturb the former slightly below \(\tau\).

For Haar reference on \(p\) residues this becomes
\[
\boxed{\#E\le\frac{p\kappa}{\kappa+(1-\tau)^2}.}\tag{C1p}
\]
The certificate is computed entirely with exact Fractions, not approximated Shannon entropies.

## C2. Pair-collision identity and genuine Gaussian source

For a random variable \(X\) on a \(p\)-point group with law \(P\), and an **independent** copy \(X'\),
\[
\boxed{\chi^2(P\|U_p)=p\Pr(X=X')-1.}\tag{C2}
\]
This follows by expanding the square: \(1+\chi^2=p\sum_xP(x)^2\).

Take a Gaussian integer \(Y=x+iy\) and a genuine split Gaussian prime \(\pi=a+bi\), with rational prime norm \(p=a^2+b^2\). The map
\[
\phi_\pi(x+iy)=bx-ay\pmod p
\]
is surjective, has \((\pi)\) as kernel, and has \(p\) possible values. For **independent samples** \(Y,Y'\) under the same declared source law,
\[
\boxed{\kappa_\pi=p\Pr[\pi\mid(Y-Y')]-1.}\tag{C2g}
\]
The computation is therefore a finite count of authentic source-difference divisibilities. Falsified norms such as \(25\), or inert and ramified replacements offered as split factors, are rejected by the source checker.

## C3. How much of a prime batch must be covered?

Consider \(k\) coordinates from the **same source and epoch**, with references \(\pi_c\), actual laws \(P_c\), and average divergence \(\overline\kappa\). Let \(0<t<1\). Call coordinate \(c\) deficient if
\[
\pi_c\{x:P_c(x)<\tau\pi_c(x)\}\ge t.
\]
By C1, each deficient coordinate has
\(\kappa_c\ge(1-\tau)^2t/(1-t)\). Summing and applying Markov's elementary counting inequality gives
\[
\boxed{\frac{\#\{\mathrm{covered\ coordinates}\}}k
\ge\max\left(0,1-\frac{\overline\kappa(1-t)}{(1-\tau)^2t}\right).}\tag{C3}
\]
**There is no assumption of independence between coordinates.** A coordinate budget for a different source or epoch is not silently added.

For OpenAI's signed Gaussian coordinate family \(p_c\in[T,2T]\), a failure of \((\tau,\beta)\)-coverage has exceptional Haar mass at least \(p_c^{-\beta}\ge(2T)^{-\beta}\). Setting \(t=(2T)^{-\beta}\) gives
\[
\boxed{\mathrm{fraction\ failing}\le
\overline\kappa\,\frac{(2T)^\beta-1}{(1-\tau)^2}.}\tag{C3g}
\]
This is a genuinely sufficient lower-bound coverage theorem. **The missing arithmetic bridge is to prove** \(\overline\kappa=O(T^{-\beta})\) for the appropriate true-prime, geometrically sampled checkpoint law. That may be much stronger than OpenAI's available Shannon entropy control and might fail on an authentic source; do not confuse this sufficient condition with a proved Gaussian moat result.

**Exact batch control:** 99 uniform distributions modulo 5 and one distribution \((0,1/4,1/4,1/4,1/4)\) share one declared source context. With \(\tau=1/2,t=1/5\), the mean divergence is \(1/400\), giving at least \(24/25=96\%\) covered coordinates, while direct counting gives \(99\%\).

## C4. Functorial data processing under lawful observer maps

Let \(K:X\rightsquigarrow Y\) be a finite stochastic kernel. Transport both actual \(P\) and reference \(\pi\): \(P'=KP\), \(\pi'=K\pi\). Then
\[
\boxed{\chi^2(KP\|K\pi)\le\chi^2(P\|\pi).}\tag{C4}
\]
**Proof.** Put \(r(x)=P(x)/\pi(x)-1\). For any output \(y\) with positive reference,
\[
\frac{(KP)(y)}{(K\pi)(y)}-1=\mathbb E_\pi[r(X)\mid Y=y].
\]
Conditional Jensen for the square, followed by total expectation, gives C4. Thus C1's **certified lower bound** cannot worsen under lawful postprocessing. Kernel composition is associative and preserves this inequality.

Do not replace \(K\pi\) by a guessed uniform reference. A uniform four-state source mapped three-to-one onto one output and one-to-one onto another has true output law/reference \((3/4,1/4)\); calling its reference \((1/2,1/2)\) fabricates a divergence and a coverage failure. This is source-map inadequacy, not a physical property.

This is classical \(f\)-divergence data processing; see [Sason (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7514244/). The contribution here is a typed and exactly checked ObsSUCC source-to-observer interface.

## C5. Correlated, source-changing updates

Let \(Y,U\) be arbitrarily correlated random variables in a finite abelian group \(G\), and \(Z=Y+U\). Denote Haar measure by \(U_G\). Then
\[
\boxed{\chi^2(P_Z\|U_G)\le
\mathbb E_U\,\chi^2(P_{Y\mid U}\|U_G).}\tag{C5}
\]
**Proof.** On \((Y,U)\), put reference \(U_G\otimes P_U\); map \((y,u)\mapsto y+u\). Each fixed translation preserves Haar, so this reference pushes to Haar. Apply C4. The input divergence expands to the stated conditional average.

If \(Y\perp U\), then the RHS is \(\chi^2(P_Y\|U_G)\). Without independence, the unconditional contraction can fail: for \(Y\) uniform on \(\mathbb Z/5\) and \(U=-Y\), \(Z=0\) always, and the divergence jumps \(0\to4\). The correctly charged conditional divergence is exactly \(4\). An observer action may modify the source and its proof obligations without violating data processing.

## C6. Constructive SUCC coverage from independent primitive steps

For a cyclic clock \(\mathbb Z/q\), take \(q-1\) independent increments in \(\{0,1\}\) with \(\Pr(+1)=a\), \(0<a<1\). Every residue \(k=0,\ldots,q-1\) then has probability
\[
\binom{q-1}{k}a^k(1-a)^{q-1-k}
\ge \min(a,1-a)^{q-1}.
\]
Hence the entire outcome space has the exact pointwise probability floor \(\alpha/q\), where
\[
\boxed{\alpha=q\min(a,1-a)^{q-1}.}\tag{C6a}
\]
For odd \(q\), \(q-1\) **nonzero** independent \(+1/-1\) steps also cover every residue: their endpoint is \(2k-(q-1)\), and multiplication by \(2\) permutes the residues.

More generally, if an independently sampled block increment law satisfies \(\nu\ge\alpha U_q\) pointwise as measures, write \(\nu=\alpha U_q+(1-\alpha)\rho\). Haar absorbs convolution, so \(m\) independent blocks obey
\[
\boxed{\nu^{*m}\ge[1-(1-\alpha)^m]U_q.}\tag{C6b}
\]
This is a classical Doeblin minorization argument and an **actual constructive lower-bound SUCC coverage theorem**, subject to its explicit independence assumption. At \(q=5,a=1/2\), four 0/1 steps give \(\Pr(\mathrm{any\ given\ residue})\ge1/16\), so the \(\tau=1/4\) floor \(1/20\) holds for every residue. Two blocks certify \(\alpha_2=135/256\). These randomly composed walks need **not** visit distinct vertices and are **not** constrained to Gaussian primes.

## C7. Exact obstruction for short bounded-step Gaussian samples

Let \(z_0,\ldots,z_L\) be distinct Gaussian integers connected by steps of length at most \(D\), and let \(\pi\) have rational prime norm \(p\). If \(DL<\sqrt p\), then no two points have the same residue modulo \(\pi\). Otherwise, \(\pi\mid(z_j-z_k)\) forces
\[
p\mid N(z_j-z_k),\qquad
0<N(z_j-z_k)\le D^2L^2<p,
\]
a contradiction. Thus any random-time distribution supported on that segment **misses at least \(p-(L+1)\) residues**. It cannot have \((\tau,\beta)\)-coverage when
\(p-(L+1)\ge p^{1-\beta}\).

A four-point unit-step segment has nine missing residues modulo the factor \(2+3i\) of norm \(13\), verified exactly. This is the reason short words and high local distinctness do not automatically supply near-complete residue coverage; the source proof's long continuations matter.

## C8. Independent-source collision potential tensorization

For separately justified independent product sources,
\[
\boxed{1+\chi^2(P_1\otimes P_2\|\pi_1\otimes\pi_2)
=(1+\chi^2(P_1\|\pi_1))(1+\chi^2(P_2\|\pi_2)).}\tag{C8}
\]
Expand \(1+\chi^2(P\|\pi)=\sum_xP(x)^2/\pi(x)\); the independent product sum factors. Correlated duplicate reports are **not** product sources. The software requires an explicit independence declaration and never claims it is physical attestation.

## Proof receipts, controls, and next falsifier

The additive module observational_succ/coverage_lower_bounds.py computes all weights, thresholds, exact Markov transports, C1/C2/C3 certificates, correlated translations, Gaussian residues and C6 blocks using Python Fraction only. tests/test_coverage_lower_bounds.py includes exhaustive small rational source laws, independent and correlated updates, source/epoch mismatch, coarse reference forgery, fake norms, grid and short-segment Gaussian controls, kernel composition, and tensor assumptions. scripts/coverage_lower_bounds_probe.py emits a JSON receipt; no numerical entropy approximation enters a certificate.

**Positive source calibration:** the \(65\times65\) integer-lattice serpentine path is a self-avoiding unit-step finite walk. Its 4,225 points project **uniformly** into both factors of 5 and both factors of 13. It is not a Gaussian-prime-only walk. In particular, it cannot be offered as a Gaussian moat proof.

**Main open probe:** using OpenAI's real sampled-time and signed-prime setup, compute and independently bound the mean authentic Gaussian pair-collision excess in C3. Predict either a \(T^{-\beta}\) bound (a stronger sufficient path to coverage) or construct a source-faithful family showing that collision energy is too demanding despite the paper's entropy/short-list coverage mechanism. Preserve genuine prime versus fake-composite and source-dependent-update controls.

**Claims not earned:** independent all-\(D\) finite-sieve existence, any RH positivity, physical infinite computation, physical independence or quantum effects, and research priority. Failure of a particular collision bound does not invalidate OpenAI's theorem or other possible SUCC proofs.


## C9. Authentic Gaussian sieve-Haar law: exact coverage and mixing debt

Fix distinct rational split primes \(p\equiv1\pmod4\), each with Gaussian conjugate factors \(\pi_p,\overline\pi_p\), and period \(Q=\prod p\). Choose \(Y\) **uniformly among residues modulo \(Q\mathbb Z[i]\) not divisible by any of these factors**. This is a genuine periodic-sieve source law, but **not** the time law of a prime-only walk.

By the Gaussian CRT, \(\mathbb Z[i]/(p)\cong\mathbb F_p\times\mathbb F_p\). The conjugate Gaussian-factor reductions are the two coordinates. Conditioning on avoiding both factors restricts their values to \((\mathbb F_p^\times)^2\), still uniformly. Distinct rational primes factor independently by CRT. Therefore for each signed Gaussian factor \(\pi\) of norm \(p\),

\[
\boxed{P(\phi_\pi(Y)=u)=\begin{cases}
0&u=0,\\[2pt]1/(p-1)&u\ne0.
\end{cases}}\tag{C9a}
\]
Consequently its single-coordinate Haar chi-square divergence is exactly
\[
\boxed{\kappa_\pi=\frac{1}{p-1}},\qquad
\boxed{\#E_\tau=1,\quad C_\tau=\frac{p-1}{p}\quad(0<\tau<1).}\tag{C9b}
\]
For every \(0<\beta<1\) it satisfies OpenAI's \((\tau,\beta)\)-coverage condition since \(1<p^{1-\beta}\). The total survivor count is
\[
\boxed{|\mathcal A(P)\bmod Q|=Q^2\prod_{p\in P}(1-1/p)^2=\prod_{p\in P}(p-1)^2.}\tag{C9c}
\]

**General exact mixing-debt decomposition.** For **any** probability law \(\mu\) on \(\mathbb F_p\) with \(\mu(0)=0\), let \(\delta_u=\mu(u)-1/(p-1)\) for \(u\ne0\). Since \(\sum_{u\ne0}\delta_u=0\), direct square expansion yields
\[
\boxed{\chi^2(\mu\|U_p)=
\underbrace{\frac{1}{p-1}}_{\mathrm{forbidden\ zero}}
+
\underbrace{p\sum_{u\ne0}\delta_u^2}_{\mathrm{nonuniform\ source\ mixing\ debt}}.}\tag{C9d}
\]
Thus the arithmetic sieve forces an **irreducible baseline** of \(1/(p-1)\); the actual additional obligation for an avoiding walk is to control its nonzero-residue mixing debt. An arbitrary avoiding deterministic walk need not sample those residues uniformly. This prevents treating C9a as a Gaussian moat proof.

**Exact reproduction:** for the two true split primes \(5=(1+2i)(1-2i)\), \(13=(2+3i)(2-3i)\) up to associates, \(Q=65\). Exactly \(4^2\cdot12^2=2304\) of the \(65^2=4225\) residues survive the genuine sieve. Both norm-5 coordinates have \(\kappa=1/4\), one missing residue and covered Haar mass \(4/5\). Both norm-13 coordinates have \(\kappa=1/12\), one missing residue and covered mass \(12/13\). An independent finite enumeration confirms the theorem; counterfeit composite norms, duplicate prime factors and resource-cap overreach are rejected.

The Python certificate lives in observational_succ/coverage_sieve_crt.py with tests/test_coverage_sieve_crt.py and scripts/coverage_sieve_crt_probe.py. A useful **next discriminator** is to estimate the second term of C9d from the actual sampled walk checkpoint law and true-prime difference counts, rather than assuming sieve-Haar sampling.
