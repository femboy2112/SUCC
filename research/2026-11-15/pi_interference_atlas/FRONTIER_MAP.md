# Source-attached π interference atlas: frontier inventory

**Read-only provenance reconstruction, 2026-11-15.** Parent #643 is pinned at
`8097d9e802da1d83a615d8812e74279820f5ae7e`; working branch is
`research/pi-interference-atlas-2026-11-15`. This inventory was assembled from
the canonical Main XXV frontier, its route contract, Main XXIV/XXV handoffs,
the preserved Main XXI–XXIV frontier documents, the gearbox/tool atlases, and
the directly referenced proof dossiers below. It is a coverage map of those
**named families**, not a claim to enumerate every possible mathematical test.
It does not independently re-prove every inherited theorem or rerun their tests.

The unmerged #642 donor is kept separate and pinned in `TRANSLATION_NOTES.md`.
No π normality estimate, R0 estimate, parity theorem, source-independent proof
of an arithmetic premise, or physical interference apparatus is supplied by
this inventory.

## 1. Immutable source and response types

Throughout, unless a row explicitly declares another model,

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_{n+1}=16U_n+r(n+1),
\]

\[
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
Y_n=U_n+T_n=16^n\pi/16,\quad z_n=\{Y_n\},\quad e(t)=e^{2\pi it}.
\]

Use the **whole integer shell** \(I_B=\{B,\ldots,2B-1\}\), not a selected
subsequence, unless the row pays its selection/coverage cost. Write
\(\nu_B=B^{-1}\sum_{n\in I_B}\delta_{z_n}\) and
\(W_B(h)=B^{-1}\sum_{n\in I_B}e(hY_n)\).

| Type | What is retained | What may not be silently substituted |
|---|---|---|
| Raw arithmetic phase | Exact rational \(U_n\), zero seed, four poles and time label | A random seed, source moment match, Galois conjugate, or independent local-prime phase |
| Completed phase | \(Y_n=U_n+T_n\), including real future tail | Raw digit labels at a discontinuity; a fixed-mode tail estimate at an unpaid growing frequency |
| Literal carry | \(c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor\), including the letter 16 | An ordinary digit obtained by discarding overflow coordinatewise |
| Completed digit | \(d_n=\lfloor16z_n\rfloor\), with certified boundaries | The smooth character \(e(8z_n)\) for the digit parity \((-1)^{d_n}\) |
| Source clock / CRT label | Its exact map from the same source, full complement and winding | A full-period marginal or source-averaged distribution in place of the selected chronology |
| Random probe | Its independently declared law, retained label, sampling propensity and response | Randomization of the source, an unlogged phase clock, or copied samples treated as independent |
| Haar / conditional partition | Coordinate, base measure, sample law and refinement order | Seed Haar, source-\(x\) Haar, time-residue Haar and future-digit Haar as if identical |

For every fixed integer \(h\), raw/completed normalized Fourier means differ
by a vanishing, proved source-tail cost. That statement does **not** by itself
transport a discontinuous event, a growing band, or an independently selected
subsample. Authentication of the source and decay of its response are different
obligations.

## 2. Classification key

- **EQ:** equivalent to full base-16 normality, with every quantifier in the row.
- **SUFF:** sufficient with additional source/scale/coverage premises; necessity is not asserted.
- **WEAK:** a weaker normality rung or another explicitly restricted statistical target.
- **NEC:** a necessary consequence, not a sufficient criterion.
- **TRANSFER:** identity, reconstruction, calibration or comparison; no arithmetic decay follows.
- **SEPARATE:** a different source, arithmetic question, observer space, or physical model.

All source-selected limits below remain **OPEN** unless the row explicitly
identifies an inherited proved weak loss. An EQ row is a way to express the
open theorem, not evidence that the theorem is easier. A prescribed growing
schedule must not be replaced by an existential arbitrarily slow schedule.

## 3. Full-normality equivalents and faithful transports

| ID | Named family and exact response | Quantifiers / logical strength | Main control and provenance |
|---|---|---|---|
| F01 | Fixed-mode Weyl: \(W_B(h)\to0\), or raw/prefix versions | **EQ:** every fixed nonzero integer \(h\), every integer \(B\to\infty\). No power rate is required. | Coherent same-forcing seed; finitely many modes do not suffice. [P0], [P1] |
| F02 | Completed word frequencies: \(p_{N,k}(w)\to16^{-k}\) | **EQ:** every fixed depth \(k\), every word \(w\), all large horizons. | A periodic de Bruijn word passes its finite tested depths. [P0], [JC], [LWE] |
| F03 | Basel tail and shell: \(F_h(A)=\sum_{n\ge A}n^{-2}e(hY_n)\); \(B_A(h)=[F_h(A)-F_h(2A)]/\sum_{A\le n<2A}n^{-2}\) | **EQ:** \(AF_h(A)\to0\), or \(B_A(h)\to0\), for every fixed \(h\ne0\) and all integer \(A\). | Absolute Basel energy \(O(A^{-1})\) is not the required signed little-oh. [P0], [P2] |
| F04 | Chronological Ω-Haar directed trace realizing \(F_h\) | **TRANSFER/EQ after F03:** exact six-frame construction, its stated starting-index domain and directed phase retained. | An unphased norm or an arbitrarily inserted projection is a different quantity. [P2], [OT] |
| F05 | Weighted Fejér lag response \(R_{B,L,h}\), defined in §7 below | **EQ as an all-mode family:** for every fixed \(h\ne0\), \(R_{B,L(B),h}\to0\), for any prescribed \(L(B)\to\infty\), \(L\le B\). IAD-02 removes the schedule choice. | This is not a per-single-mode equivalence; fixed-point mixtures distinguish \(W(1)\) from lag mode 15. [IAD] |
| F06 | Bounded carry innovation: shell mean of \(\Phi_h(\lfloor U_n\rfloor,c_{n+1})\) | **EQ:** all fixed \(h\ne0\); comparison to raw Weyl is \(O_h(\log B/B)\). The response is read after one transition. | Averaging the *reference* next digit uniformly is not the actual carry law. Literal 16 and the integer lift are retained. [EI] |
| F07 | Signed carry/arrival bin decoder \(\widetilde C_{N,M}(h)\) in §7 | **EQ:** all fixed \(h\ne0\) and any prescribed \(M_N\to\infty\), using the displayed finite source-error bound. | Squaring conditional bins removes cross-bin cancellation and changes the gate. [P1], [SB] |
| F08 | Deep zero-seed cylinder energy \(\mathcal E_{N,K}(h)=16^K\int_0^{16^{-K}}\lvert N^{-1}\sum_{n<N}e(h16^n(\pi/16+s))\rvert^2ds\) | **EQ:** all fixed \(h\ne0\), \(K=N-o(N)\). | At \(K=o(N)\), it tends to zero for *every* source, including a locked one. [MS] |
| F09 | Signed zero-child flux \(\sum_{K=0}^{N-1}\mathcal J_{N,K}(h)\), where \(\mathcal J_{N,K}=\mathcal E_{N,K+1,0}-\mathcal E_{N,K}\) | **EQ:** the flux tends to zero for all fixed modes, by \(\lvert W_N(h)\rvert^2=N^{-1}+\sum_K\mathcal J_{N,K}+O_h(N^{-1})\). | Details are signed, not nonnegative chronological Haar energies; a fixed-depth fingerprint does not bound the growing sum. [MS] |
| F10 | Reversible 112-state clock observer: \(c_n=(d_n+q_n+\sigma_n)\bmod16\), \(q_{n+1}=(q_n+3d_n+2\sigma_n)\bmod16\), period-7 \(\sigma_n\) | **EQ:** full block normality of output \(c\), not one-symbol balance. The inverse and finite source clock are retained. | An unaccounted normal auxiliary tape can manufacture normal output from constant input. [JC, J13–J16] |
| F11 | Fixed-radius Clausen energy \(Q_{1/2}(\nu_B)=\sum_{h\ge1}2^{-h}\lvert W_B(h)\rvert^2/h\) and finite causal Clausen cut | **EQ:** energy \(\to0\); cut differs from its negative by \(O(B^{-1})\). | Fixed positive summable weights are a compact encoding of all modes, not a new signed estimate. [FA] |
| F12 | Golden fixed-aperture energy \(E_a(\nu)=\lVert\nu*\nu_a-1\rVert_2^2\), \(a=(\sqrt5-1)/2\) | **EQ:** \(E_a(\nu_B)\to0\). Its exact pair kernel is \((b-\lVert t\rVert)_+/b-b\), \(b=a^2\). | Irrational aperture gives every nonzero Fourier weight positive. A generic arc-grid bound needs orbit rigidity to imply Haar. [GA] |
| F13 | Poisson energy \(\mathcal P_B=\sum_{h\ge1}2^{-h}\lvert W_B(h)\rvert^2\) | **EQ:** \(\mathcal P_B\to0\). Exactly \(\mathbb E_{I,J}[(P_{1/2}(Y_I-Y_J)-1)/2]\). | Already SCE-01 with normalization \(E_B=1+2\mathcal P_B\); the current click packaging must credit that exact predecessor. [SCE] |
| F14 | Positive/greedy Poisson regret: \(R_N=\sum_{n<N}[\Phi_n(z_n)-n]_+\), \(Q_N=\sum_{n<N}[\Phi_n(z_n)-\min_z\Phi_n(z)]\) | **EQ:** either is \(o(N^2)\), with \(\Phi_n(z)=\sum_{j<n}P_{1/2}(z-z_j)\). | SCE-01 corrects older wording that regarded positive regret as asymptotically stronger. [SCE] |
| F15 | Mesoscopic near-pair budget \(B_A(t)=A^{-2}\#\{(n,m)\in I_A^2:\lVert z_n-z_m\rVert<t\}\) | **EQ:** there exists finite \(C\) and \(\delta_j\downarrow0\) with \(\limsup_A B_A(2\delta_j)\le2C\delta_j\) for every \(j\). | Includes diagonal; ×16 invariant shell limits are essential. The inherited phrase “fix any C” needs the correction in §10. [FC, C3-1] |
| F16 | One shrinking-scale pair budget | **EQ:** there exist finite \(C\) and \(\delta_A\downarrow0\) with \(B_A(2\delta_A)\le2C\delta_A\) eventually. | Diagonal forces \(\delta_A\ge(2CA)^{-1}\); a fixed microscopic exclusion radius alone is insufficient. [FC, C3-2] |
| F17 | Critical-carry factorization: log-scale stationarity LS **and** source-lattice uniformity H2* | **EQ jointly:** exact definitions in §7. Each factor separately is weaker. | Nonstationary calibrated same-forcing seeds satisfy the carry family without normality. Actual admissibility must be used. [FB], [FA] |
| F18 | Sixteen-child future projector defect \(D(\nu_B)=W_1(\nu_B,Q\nu_B)\), \(Q=CT_*\) | **EQ on actual completed orbit:** \(D\to0\) is sufficient by the endpoint-paid inequality; normality also gives \(D\to0\) by continuity at Haar. | \(Q\) replaces only the first digit and preserves the genuine future; it is idempotent, not a strict contraction. Interval chart matters. [P0], [P2] |
| F19 | Fourier–Yoneda observation surfaces | **TRANSFER/EQ in their separate contracts:** #541 Bernoulli \(B_2\) inverse \(\mu=\lambda-\tfrac12D^2F\); #543 forward first-order inverse; #542 finite two-tone/backward convolution. | #542 and #543 multipliers differ by conjugation; learning/pinning a path does not make it typical. [A21], [A23] |

## 4. Weaker rungs, necessary consequences and independent auxiliary targets

Let \(\mathcal M(\xi)\) be the compact set of shell limit measures of the
actual ×16 orbit. All inequalities below have a positive margin **uniform over
all sufficiently large integer shells**; a different margin on each shell is
not enough.

| ID | Named target / response | Strength and quantifiers | Control / provenance |
|---|---|---|---|
| F20 | R0: \(\limsup_B\Re W_B(1)<1\) | **WEAK:** equivalent to \(\delta_0\notin\mathcal M\), positive lower shell density of binary changes, and the corresponding real Basel margin. | Pairwise differences are globally phase-blind: fixed orbits 0 and 1/15 have identical pair responses but different R0. [P0], [P3], [LMF] |
| F21 | R1: \(\limsup_B\lvert W_B(1)\rvert<1\) | **WEAK:** excludes every single ×16 fixed-point mass \(\delta_{j/15}\); R1 implies R0. | \(\xi=1/15\) satisfies R0 and fails R1. [LMF] |
| F22 | R2 = CH: \(\limsup_B\Re W_B(15)<1\) | **WEAK:** positive lower density of hexadecimal changes; excludes shell limits supported on the fixed-point set. | Long alternating runs of digits 1 and 2 satisfy R1 but fail CH. R2 is an alias, not a new rung. [LMF], [CF] |
| F23 | CH_k: \(\limsup_B\Re W_B(16^k-1)<1\) | **WEAK:** for each specified fixed \(k\), positive lower density of \(d_n\ne d_{n+k}\); CH_k implies CH_j when \(j\mid k\). | Periodic \(0F\) satisfies CH and fails CH_2. [LMF] |
| F24 | AM: \(\forall h\ne0,\limsup_B\lvert W_B(h)\rvert<1\) | **WEAK:** equivalent to all CH_k and to excluding every finitely supported shell limit. Margins may depend on fixed \(h\). | An infinite atomic periodic-mixture limit can satisfy AM with zero entropy. [LMF] |
| F25 | E: every \(\nu\in\mathcal M\) has positive metric entropy | **WEAK:** normality implies E implies AM; E is not maximal entropy. | Fair digits 0/1 interpreted in base16 give entropy \(\log2\), not Haar entropy \(\log16\). [LMF] |
| F26 | LS alone | **WEAK:** macroscopic subwindows have the same empirical law as the whole shell, uniformly over declared relative lengths. | It must be combined with H2* for normality; arbitrary stationary non-Haar orbit laws are controls. [FB] |
| F27 | H2* alone | **WEAK:** all fixed critical-carry gaps \(k\), uniform admissible source-lattice scales away from the upper endpoint. | Same-forcing nonstationary seeds refute H2* alone implying normality. [FB] |
| F28 | One-digit parity balance \(\mathbb E_B(-1)^{d_n}\to0\) | **WEAK:** one digit character; source-clock convention \((-1)^{\lfloor Y_n\rfloor}\) is shifted by one index with error \(\le2/B\). | Uniform parity does not imply all digit modes or parity words. [P0], [PPP] |
| F29 | Odd-eight smooth gate \(W_B(8k)\to0\) for every odd integer \(k\) | **WEAK/SUFF:** sufficient for every fixed parity word; strictly weaker than full normality and stronger than parity-word fairness alone. | Jump/boundary control is part of the proof. \(e(8t)\) alone is not digit parity. [PB], [PS] |
| F30 | Two-fiber/Aphex complement contrast \(\beta_B^*=(u_+-u_-)/2\) | **Conditional equivalence to parity**, if imported prime marginal \(m_B=\mathbb E a\to0\): \(\mathbb E(ab)=\beta_B^*+m_B(u_++u_-)/2\). | Both fibers must be populated; full complement includes old prime powers, winding and tail. A perfectly fitted counterseed has \(\beta^*=1\). [P0], [TFH], [PPP] |
| F31 | Restricted irrationality exponent / saving–exponent law | **NEC:** a fixed real Fourier saving forces a restricted radix exponent below 1, with the stated quantitative law. | Exponent 0 examples can still fail R0, R1 or CH; Diophantine separation alone is insufficient. [RDT], [CF], [LMF] |
| F32 | Tail seam density \(B^{-1}\sum_{I_B}\mathbf1[\{Y_n\}<T_n]\to0\) (“Target A”) | **SEPARATE from the weak savings:** normality supplies boundary decay, but seam-free behavior and CH/exponent savings do not imply each other in the control class. | ZSC-05 W1/W2/W3 controls; W3 has CH and positive seam density. [CF] |
| F33 | Proven GB12 logarithmic reinforcement loss and dose amplification | **PROVED weak source separation:** for fixed \(h\), large uncomputed-onset \(m\), \(\lvert\sum_{m<n\le8m}e(hU_n)\rvert<7m-1/14\); reference-click hit probability \(>1/(196m)\). | \(M=\lceil196m\log m\rceil\) repetitions amplify a finite hit; vanishing per-query margin is not R0. No explicit universal onset was extracted. [GB], [PC] |
| F34 | R0/CH for \(\xi_*=\log(16/15)\), a proper zero-seeded member of V | **SEPARATE intermediate source:** same definitions as F20/F22 applied to \(\xi_*\), not π. Imported restricted bound removes one obstruction, not the medium-scale estimate. | A theorem for one period in V does not prove π's theorem. [P3], [RDT] |
| F35 | Approximation and effectivity tasks: \(A_n\pi-B_n\), prescribed \(v_2(A_n)-v_2(B_n)\), RDT starting indices, \(\Lambda(1,16,1)\) enclosure, Baker source check | **SEPARATE arithmetic/effectivity obligations**, not automatically finite phase-grammar responses. | The defining approximants/imports must be supplied before an experiment is claimed. [P3], [RDT] |

The proved ladder is
\(N\Rightarrow E\Rightarrow AM\Rightarrow CH_k\Rightarrow CH_j
\Rightarrow CH=R2\Rightarrow R1\Rightarrow R0\) for \(j\mid k\),
with the appropriate fixed/all-\(k\) reading. Every π rung in that chain is OPEN.
Thresholds in interval \(W_1\) or \(D\) such as \(1/4\), \(1/60\), and
\(1/[4(16^k-1)]\) are **sufficient margin tests**, not equivalent definitions.

## 5. Prescribed-scale positive energies and signed arithmetic gates

| ID | Named family / exact response | Strength and scale | Main control / provenance |
|---|---|---|---|
| F36 | IMW matrix purity \(D_{N,H}=\operatorname{tr}(A_{N,H}^2)-H=2\sum_{j=1}^{H-1}(H-j)\lvert S_N^U(j)/N\rvert^2\) | **SUFF** at prescribed \(H_N\to\infty\) with \(D/H_N\to0\); **EQ** only for existence of an arbitrarily slow schedule. | Positive Gram matrix alone supplies no bound; moving source twists obstruct uniform operator convergence. [P1], [OSP] |
| F37 | OSP conductor-flat innovation \(\frac2{N^2H_N}\sum_{m<N:Q_{m+1}=Q_m}m(q_{m,H_N}-H_N)\) | **SUFF:** limsup \(\le0\), with \(H_N=\max(2,1+\lfloor\sqrt{\lfloor\log_2N\rfloor}\rfloor)\). Birth contribution is already bounded. | Selected innovation need not be bounded by its cyclotomic trace. \(Q_n\) is monotone forcing conductor, not final reduced denominator. [P1], [OSP] |
| F38 | PSF conductor-birth-censored carry-profile purity | **SUFF** at prescribed \(H\asymp(\log N)^{3/2}\); generally source transfer needs \(\sqrt H\log H=o(\log N)\). | Censored profile is a declared observable, not an independent source; all future boundary costs remain. [P1], [PSF] |
| F39 | Critical Fejér energy \(C^x_{A,A}=\sum_{\lvert h\rvert\le A}(1-\lvert h\rvert/(A+1))\lvert c_A^x(h)\rvert^2\) | **SUFF:** \(o(\log A)\) on every A or relative-gap-dense checkpoints. Uses proved ×16 frequency-ray rigidity. | Uniformly bounded finite samples do not prove the limit; a fixed finite Fejér kernel is not characteristic. [ET] |
| F40 | All-radius anticlustering \(\#\{(n,m):\lVert x_n-x_m\rVert\le\delta\}\le A+KA^2\delta\) | **SUFF:** one finite K, every radius and all large actual source shells. | Nongeneric grids on an arc can satisfy K=3 and remain non-Haar; source orbit rigidity is indispensable. [ET], [GA] |
| F41 | Polylog Fourier band \(\sum_{1\le\lvert h\rvert\le q_A^2}\lvert c_A(h)\rvert^2=o(K_A)\) | **SUFF:** \(K_A=\lfloor\log_{16}\log A\rfloor\), \(m_A=16^{K_A}\), \(q_A=m_A/2\). | Band ⇒ tent J ⇒ canonical E; converse J ⇒ band is false. [SC], [A21] |
| F42 | Common-origin tent energy \(J_{A,q}=qA^{-2}\sum_{n,t}(1-q\lVert x_n-x_t\rVert)_+\) | **SUFF:** \(J_{A,m_A/2}=o(K_A)\). Exact Fourier weights are sinc-squared. | Translate the bin origin jointly for all points; independently translating each point changes the source statistic. [SC] |
| F43 | Canonical cylinder energy \(E_{A,m}=m\sum_jp_j^2\) at \(m=m_A\) | **SUFF:** \(E=o(\log m)\) on its inherited horizon schedule. | Diagonal sample floor and canonical bin boundaries must be paid; this E includes baseline 1, unlike LWE/TDH E. [SC], [A21] |
| F44 | Signed unit-child successor energy \(J_j=16^{j+1}\sum_{w,a}[p_{j+1}(wa)-p_{j+1}(w,a-1)]^2\) | **SUFF:** \(j(N)\to\infty\), \(16^{j(N)}/N\to0\), \(J_{j(N)}\to0\). | Child-label successor is not chronological successor; endpoint cost \(4\cdot16^j/N\). [TDH] |
| F45 | Lambert-depth collision deficit \(\log(1+E_{k_W(N)}(N))\), \(E_k=16^k\sum_wp_w^2-1\) | **SUFF, strictly stronger:** \(o(\log N)\), all N or checkpoints with ratio tending to1; \(k_W=\log_{16}N-\log_{16}\log N+O(1)\). | A normal word with sparse large zero clumps fails this prescribed-scale gate; the iid coupon law is only a clock design. [LWE] |
| F46 | Trimmed joint collision/entropy \(C_G=16^d\sum_wq_G(w)^2\) | **SUFF:** \(d\to\infty\), vanishing removed fraction, \(\log C_G=o(d)\), all horizons/dense coverage; arbitrary slow source-adapted depth gives an equivalence. | The retained subset need not be stationary; apply entropy to the full original window. Source-to-completed cell transport costs factor2. [TJ], [SCE], [LWE] |
| F47 | J20 reversible-output growing entropy deficit | **SUFF:** \(k\mid L\), \(k\to\infty\), \(k/L\to0\), \(kL/A\to0\), and \((k/L)\Delta_C(L)\to0\). | Full source/state budget \(\log112\) and endpoint entropy terms remain; depths above \(\log_{16}A\) meet a sample-count obstruction. [JC] |
| F48 | Conditional branch energies, arrival energies and parity variance | **SUFF for their stated branch/parity gate:** use \(M_N=o(N^2)\) for arrival transport; prescribed parity \(M\asymp\log N\). | At \(M\ge Q_N\), exact conditioning gives energy1 and defect15. Full-clock conditioning cannot mix. [P1], [SB] |
| F49 | Selected real prime-window collision \(K_p(1)\) | **SUFF:** \(K_p(1)=p^{o(1)}\) on every large good \(p=8u+1\), \(\operatorname{ord}_p16>\sqrt p/\log p\), at fixed depth \(\lfloor(2/5)\log_{16}p\rfloor\). | Selected real cells, not dyadic residues or Galois averages; good-prime relative density and carry transport are part of the proof. [SCE] |
| F50 | Selected prime/complement sum \(\sum_{t\in W_p}e(4h16^t/p)e(hw_t)\) | **Arithmetic gate only:** stated local power saving and its exceptional-prime/coverage hypotheses; no unconditional local-to-global normality implication. | Dropping \(w_t\), old prime powers or winding replaces the target. Local Haar alone is paid, joining is not. [P1 Route D], [PPP] |
| F51 | Harmonic Fejér mixture \(N^{-1}\sum_{k<K_N}w_{K_N,k}\lvert W_{k,N}(h)\rvert\) | **SUFF:** tends to0 for every fixed nonzero h; exact weights/cutoff in §7. | Naive signed \(1/k\) lag kernel is negative at K4, angleπ. Correct positive mixture still requires signed source saving. [HM] |
| F52 | Sparse/mesoscopic van der Corput lags | **SUFF for full normality:** for every fixed nonzero integer h, there is \(\delta_h>0\) such that every fixed integer \(j\ge1\) has \(\limsup_B\Re c^U_{j\ell_0(B)}(B;h)\le0\), where \(\ell_0(B)=\lceil(2+\delta_h)\log_{16}B\rceil\); B runs through all integers. | The response is the raw two-time lag, equivalent here to the completed lag by uniform \(O_h(B^{-2})\) transport. One narrow lag band supports only a small differencing set; untwisted innovation cancellation alone is seed-blind. [IAD-06] |
| F53 | Conditional innovation/history decoupling | **TRANSFER / unpaid conditional gate:** if history phase is approximated in a filtration, conditional innovation norm equals conditional completed lag norm up to the declared error. | Calling this “decoupling” does not remove the original phase estimate. Full chronology conditioning has modulus1. [IAD-05] |
| F54 | Return-fiber energy \(R_{Q,M}(h)=Q^{-1}\sum_{a<Q}\lvert M^{-1}\sum_{t<M}e(hU_{a+tQ})\rvert^2\) | **SUFF** if it vanishes for every fixed nonzero mode on all integer horizons N=QM, or checkpoints with consecutive ratio tending to1; a prescribed growing Q can be stronger than normality. | Fixed-N refinement increases R to1; shared fiber label must be glued, not independently redrawn. [FG] |
| F55 | Golden spatial × dyadic-time fiber energy \(G_{Q,M}^{gold}=Q^{-1}\sum_a E_a(\mu_a)\) | **SUFF:** \(G\to0\) on all integer horizons or checkpoints with consecutive ratio tending to1. \(G=E_a(\mu)+\text{between-fiber variance}\). | It is monotone nondecreasing under fixed-N refinement. Q=N gives the locked-point energy, not a contraction. [GA-05] |
| F56 | Gaussian-angle source pullback | **Conditional SUFF:** a map from actual BBP times to a full Gaussian disk with phase error \(\le c/q\), multiplicity \(\le BA/M_R\), uniform c,B and suitable growing q. | Complete disk/primitive-direction equidistribution is a different source; the alignment map is not established. [GC-06] |
| F57 | Fekete energy and stronger microscopic pair budgets | **SUFF, not necessary:** the inherited Fekete lower-energy premise or all-scale bounds. | Sparse near-repeats can preserve normality while violating these strong budgets. Pure microscopic exclusion is too weak. [FC] |

## 6. Finite interaction, observation and separate-model families

These rows prevent a complete response catalogue from being mistaken for a
complete catalogue of proved arithmetic estimates.

| ID | Family / response | Exact scope | Key control / provenance |
|---|---|---|---|
| F58 | Four-bit Walsh/factorial cells: \(16Z-Q_0=\sum_{\varnothing\ne A\subseteq\{1,2,3,4\}}M_A\) | **TRANSFER:** complete finite-character inversion. A selected highest-order saving is an additional arithmetic obligation, not implied by proper marginals. | Uniform even-parity law has all proper marginals uniform but nonzero top interaction. [P1 Route C], [TJ] |
| F59 | Joint conditioned collision chain \(\log C_d=\sum_{k<d}\log[1+\mathbb E_{\xi_k}\chi^2(q_v\Vert u)]\) | **TRANSFER:** prefix weights are proportional to squared actual mass; correlated reference version also retained. | Product-of-marginals substitution misses parity/base5 triple constraints. A decoder needs its exact reference pushforward. [TJ] |
| F60 | Finite deterministic-lag characters \(e(\sum_j a_jY_{n+j})\) | **TRANSFER:** equals \(e(P(16)Y_n)\), \(P(X)=\sum_ja_jX^j\). Haar benchmark is \(\mathbf1_{P(16)=0}\), not product-Haar over lag coordinates. | \((Y_n,Y_{n+1})\) lies on the graph \(y=16x\); character \((-16,1)\) is identically1 even under normality. See `TRANSLATION_NOTES.md`. |
| F61 | Retained source-clock echo \(e((h-16K)U_n+KU_{n+1})=e(hU_n+Kr(n+1))\) | **TRANSFER:** calibrated random probe frames with known node gaps, conditioning and sampling law. | Independent rows, whitening, resource growth and inverse noise cost matter. This does not force the phase vector mean to vanish. [PC] |
| F62 | Referenced frame residual \(\mathbb E_K\lvert F_c(K)-F_1(K)\rvert^2\) | **Conditional EQ to R0:** the across-B frame condition needs a uniform \(\eta\le\eta_*<1\), fixed h1 and the B-dependent normalization. | A pairwise magnitude-only frame without reference has global-phase gauge and cannot recover R0. [PC-06] |
| F63 | Gamma clock rotation / recorded compensation | **TRANSFER/SEPARATE randomization:** conditional multipliers, exact recorded-clock compensation and inverse averaged-channel noise budgets are distinct. | A forgotten independent clock can make a locked source look Haar; imported randomness is not π cancellation. [PC], donor #642 HD07 |
| F64 | Intrinsic Oily/source-\(x\) Haar variance, reversible Markov Gamma leakage | **SEPARATE source/partition theorem:** authentic continuous source measure can have a Haar variance decomposition; a declared finite reversible generator has Gram leakage identities. | Neither source coordinate x nor a chosen Markov generator is the temporal π phase law. Nonreversibility can reverse the defect sign. [AH] |
| F65 | Seed-cylinder coarse energy and fixed-depth signed fingerprints | **TRANSFER / proved finite-scale information:** fixed K asymptotic and signed first h8 packet; no deep-scale bound. | Universal coarse decay and positive \(N^{-2}\) packet do not imply digit parity or normality. [MS] |
| F66 | CDF chronological opposite-sign overlap \(\Omega\), high/low word junctions and conditional Haar | **TRANSFER; SUFF after new bounds:** exact telescopes and finite constants, with full future and endpoint terms. | No automatic statistical contraction; child successor, chronological successor and source revelation are distinct. [P0], [TDH], [AH] |
| F67 | Finite source authentication / observational equivalence / adaptive evidence | **TRANSFER:** only within a declared source class, policy, likelihood, transcript and resource contract. | Equal all-word output laws defeat all transcript-only policies; matching finite observations never universally authenticates an unrestricted source. [FSA] |
| F68 | Cayley/source-clock/Scott–Ω/affine observer architecture | **TRANSFER in repaired domains:** source-attached coordinate maps and guarded finite semantic identities. | Historical capture-unsafe reductions, invented redex addresses and finite-prefix cofinality claims are withdrawn; full faithful C-monoid/source compilation remains unverified. [A23], [OT] |
| F69 | Prime/2-adic/Pascal/Lucas/Galois quotient Haar and moving-frequency losses | **TRANSFER / own-domain estimates:** exact quotient laws, selected weak losses and clock naturality. | Spatial Haar, denominator growth, Galois Haar and seed-blind moving bands do not prove real temporal Haar. [G], [P1], [A21] |
| F70 | Mixed arithmetic-label / angular-radial correlations | **TRANSFER or SEPARATE:** bounded-variation labels reduce exactly to original prefix sums; non-BV prime labels can be independent of normality in both directions. | Correct Haar baseline need not be zero for carry-coupled functions; reflection changes orientation without changing normality. [FC] |
| F71 | Other bases and mixed-base joining | **SEPARATE:** base16 implies multiplicatively dependent powers of2; base3/base10/base11/10 and product joining need independent theorems. | Correct marginals do not prove product Haar. [P1 Route E], [G] |
| F72 | Completed Weil/Li/RH, prime fixed points and Goldbach | **SEPARATE:** authentic completed form on its full legal test domain, or independently valid equivalent arithmetic predicates. | A positive Hilbert surrogate, finite jets, finite positive compressions, or finite Goldbach checks do not settle the universal statement. [P0 §8], [P1 Route F], [P3], [GFT] |

The following two named canonical obligations have separate entries because
neither is exhausted by an identity already listed above.

| ID | Named family / exact target | Strength and quantifiers | Main control / provenance |
|---|---|---|---|
| F73 | Positive defect thresholds: shell \(\limsup_B D(\nu_B)<1/4\Rightarrow R1\), \(<1/60\Rightarrow CH\), \(<1/[4(16^k-1)]\Rightarrow CH_k\); the same shell thresholds hold for \(W_1(\nu_B,\lambda)\). Prefix \(\limsup_ND_N<15/256\Rightarrow R1\), \(<1/256\Rightarrow CH\). | **SUFF explicitly for the specified weaker rung, not full normality.** Interval cost on [0,1], \(D(\nu)=W_1(\nu,Q\nu)\), \(D_N=D(\mu_N)\); every fixed integer \(k\ge1\), all integer shells/prefixes, and a strict eventual margin. | Finitely many subthreshold shells do not establish a limsup. The lift 1 at the interval endpoint matters. The coherent control has D=15/32; W3 satisfies CH far above its sufficient threshold. Only the shell constants 1/4 and 1/60 are asserted sharp here. [P0 §9], [LMF-04/05] |
| F74 | Route C selected highest-order interaction: prove a nontrivial/power-saving bound for \(M_{\{1,2,3,4\}}\) over the original source window in \(16Z-Q_0=\sum_{A\ne\varnothing}M_A\), with the four-pole Fourier jet at the recorded branch point. | **AUXILIARY / conditional arithmetic target; OPEN.** The canonical contract does not specify a unique window growth, rate exponent or normalization sufficient to define a quantitative asymptotic claim. Those must be supplied; no automatic full-normality implication is asserted. | F58 is the finite Walsh identity, not this estimate. Uniform even-parity data have every proper marginal uniform and a biased full interaction. A bound at one event/window does not supply all-word/all-horizon equidistribution. [P1 Route C] |

## 7. Exact definitions supporting compact rows

### Weighted lags and harmonic lags are different responses

For F05 set \(p_n=n^{-2}/\omega_B\), \(\omega_B=\sum_{I_B}n^{-2}\), and

\[
R_{B,L,h}=\frac{2B}{L}\sum_{\ell=1}^{L-1}(1-\ell/L)
\Re\sum_{n=B}^{2B-1-\ell}p_np_{n+\ell}
e\big(h(16^\ell-1)Y_n\big).
\]

IAD proves \(\lvert B_B(h)\rvert^2\le4/L+2\max(R_{B,L,h},0)\).
The exact positive moving-block energy relation proves all-mode equivalence
for every growing schedule. Replacing every signed term by its absolute value
creates a different sufficient condition; no converse is licensed by this
identity.

For F51 instead,

\[
w_{K,k}=H_K^{-1}\sum_{L=k+1}^K\frac{L-k}{L^3},\quad
W_{k,N}(h)=\sum_{n=1}^{N-k}e\big(h(16^k-1)U_n\big),
\]

\[
K_N=b_N+3\lfloor\log_{16}b_N\rfloor,
\qquad b_N=\lfloor\log_{16}N\rfloor.
\]

Its source-forcing error is at most
\(\frac{88\lvert h\rvert}{1575}\frac{16^K}{NH_KK^3}\).
These positive harmonic weights are classical Fejér mixtures, not the invalid
signed \(1/k\) shortcut.

### Critical carries retain their lattice and local stationarity

Let \(S_k(n)=\sum_{j=1}^k16^{k-j}r(n+j)\), \(d=m+k\),
\(x_n=\{U_n\}\), \(\theta=\{16^dx_n\}\),
\(\delta=\{16^mS_k(n)\}\), and \(b_n=\mathbf1[\theta+\delta\ge1]\).
The carry response is \(J^{carry}_{A,m,k}=A^{-1}\sum_{I_A}(b_n-\delta_n)\).
It is not the tent energy J or the child-successor energy J.

LS requires, for every fixed \(\eta>0\),

\[
\sup_{1\le a<b\le8,\ b-a\ge\eta}
D\big(\mu_{[aA,bA)},\mu_{[A,2A)}\big)\longrightarrow0.
\]

H2* requires, for every fixed \(k\ge1\) and \(\eta>0\), convergence of
\(J^{carry}_{A,d-k,k}\) to0 uniformly over **admissible** pairs \((A,d)\)
with \(c_A(d)=16^d/(64A^2)\le1-\eta\). Admissibility means the actual
tail inequalities used in [FB], including \(16^dT_n\le1\) on the shell.
The closed-form admissibility equivalence checked through \(d\le200\) is not
a proved universal replacement for those hypotheses.

### Conditional arrival and signed decoder

Put \(y_n=\{U_n\}\), \(j_n=\lfloor16y_n\rfloor\),
\(t_n=\{16y_n\}\). Conditional energies are formed from the actual empirical
records \((\lfloor Mt_n\rfloor,j_n)\), or arrival records
\((\lfloor My_{n+1}\rfloor,c_{n+1}\bmod16)\). In arrival bin b,
\(\Phi_b=4/9+\Pr(c_{n+1}\text{ odd}\mid b)/9\), and exactly

\[
\widetilde E_{N,M}(8)=324\sum_b\widetilde p_b(\Phi_b-1/2)^2.
\]

The weaker signed response retains cross-bin cancellation:

\[
\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N
e\left(\frac{h(c_{n+1}+\tau_{\lfloor My_{n+1}\rfloor})}{16}\right),
\qquad\tau_b=(b+1/2)/M,
\]

with error to \(S_N^U(h)/N\) at most
\(\pi\lvert h\rvert/(16M)+[\pi\lvert h\rvert/(8N)]\sum_{n=1}^Nr(n+1)\).

For the distinct OSP row F37, the unnormalized Fejér polynomial is
\(F_H(t)=\lvert\sum_{k=0}^{H-1}e(kt)\rvert^2\), and
\(q_{m,H}=m^{-1}\sum_{j=1}^mF_H(U_{m+1}-U_j)\). In a fixed horizon
all steps use the same width H; its Haar baseline is H, not 1.

### Source conditional Haar is not arbitrary averaging

For the full sixteen-child projector,
\(B_a(y)=(a+y)/16\), \(C\mu=16^{-1}\sum_a(B_a)_*\mu\),
\(Q=CT_*\), \(T(y)=\{16y\}\). Thus \(Q^2=Q\): future is retained.
For equal consecutive half-blocks with signed CDF defects \(H_-,H_+\),

\[
D_{2M}=\tfrac12(D_-+D_+)-\Omega_M,\qquad
\Omega_M=\int\min(\lvert H_-\rvert,\lvert H_+\rvert)
\mathbf1_{H_-H_+<0}.
\]

Any contraction proof still needs an original-source lower bound on this
opposite-sign overlap and a bound comparing the two child defects, with odd
block/endpoint corrections. There is no universal strict contraction.

## 8. What “finite response compiler covers a family” can mean

1. A fixed finite Fourier/Walsh polynomial can be compiled **exactly**, provided
   its source-labelled primitive phases and clocks are already available.
2. A bounded characteristic energy with infinitely many modes can be compiled
   as an infinite randomized response or a finite truncation with a proved
   tail. It is not literally a single finite polynomial.
3. A digit event needs authenticated digit access or a boundary-paid Fourier
   approximation. Logs, reciprocals of conditional masses, minima, entropy,
   limsups, support and “every shell” are nonlinear/limit operations applied
   to reconstructed finite data; they are not silently members of the
   quadratic phase grammar.
4. A named external source model, an undeclared phase oracle, an arithmetic
   approximation family or an unspecified physical interaction is not compiled
   merely by assigning it a label. Its representation and resource contract
   are additional inputs.

The catalogue therefore certifies **coverage with an explicit type and gap**,
not equal implementation depth for every row. Finite reconstruction, exact
sampling expectation and an asymptotic arithmetic upper bound are three
separate assertions.

## 9. Provenance index

Paths below are repository-relative. Named statements were read from these
files; inherited mathematical claims retain their original authority labels.

- **[P0]** `docs/PI_NORMALITY_FRONTIER.md`.
- **[P1]** `docs/PI_FRONTIER_CONTRACT.md`.
- **[P2]** `docs/MAIN_XXIV_HANDOFF.md`.
- **[P3]** `docs/MAIN_XXV_HANDOFF.md`.
- **[G]** `docs/PI_GEARBOX_ATLAS.md`.
- **[A21]** `docs/archive/PI_NORMALITY_FRONTIER_MAIN_XXI_2026-11-09.md`.
- **[A23]** `docs/archive/PI_NORMALITY_FRONTIER_MAIN_XXIII_2026-11-11.md`; the
  Main XXII and XXIV archived frontiers were also checked for named additions.
- **[OT]** `docs/MAIN_XXIII_TOOL_ATLAS.md`.
- **[LMF]** `research/2026-11-12/frontier_rungs/LIMIT_FACES.md`.
- **[RDT]** `research/2026-11-12/frontier_rungs/RESTRICTED_EXPONENT.md`, as
  scoped by [P0]/[P3]; no present-best irrationality-measure claim is made.
- **[IAD]** `research/2026-11-11/innovation_arithmetic_decoupling/THEOREMS.md`.
- **[CF]** `research/2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md`.
- **[FA]** `research/2026-11-05/main_xx_forge/front_a/PROOFS.md`.
- **[FB]** `research/2026-11-05/main_xx_forge/front_b/PROOFS.md`.
- **[FC]** `research/2026-11-05/main_xx_forge/front_c/PROOFS.md`.
- **[ET]** `research/2026-11-06/epoch_critical_transfer/THEOREMS.md`.
- **[GA]** `research/2026-11-07/golden_aperture_fejer/THEOREMS.md`.
- **[SC]** `research/2026-11-03/selected_current_front/PROOFS.md`.
- **[FG]** `research/2026-11-06/fejer_gamma_split/THEOREMS.md`.
- **[MS]** `research/2026-11-10/zero_seed_microscope/MICROSCOPE_THEOREMS.md`.
- **[EI]** `research/2026-11-08/chronology_carry/crucible/EXPLICIT_INNOVATION.md`.
- **[TDH]** `research/2026-11-09/tenacious_d_haar/PROOFS.md`.
- **[JC]** `research/2026-11-06/joint_character_entropy/THEOREMS.md`.
- **[LWE]** `research/2026-11-08/lambert_entropy_forge/THEOREMS.md`.
- **[SCE]** `research/2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md`.
- **[TJ]** `research/2026-10-24/PI_TRIMMED_JOINT_ENTROPY.md`.
- **[HM]** `research/2026-10-24/PI_HARMONIC_MIRROR_SUCC_FORGE.md`.
- **[OSP]** `research/2026-10-25/OPERATION_SPECTRAL_PURITY.md` and its
  `SPECTRAL_PURITY_INNOVATION.md`, as indexed by [P1].
- **[PSF]** `research/2026-10-25/PI_SELECTED_PHASE_FORGE.md`, as indexed by [P1].
- **[SB]** `research/2026-10-26/SELECTED_BRANCH_SYNTHESIS.md`, as indexed by [P1].
- **[GB]** `research/2026-10-27/GLOBAL_BRANCH_COERCIVITY.md`.
- **[PPP]** `research/2026-11-09/pi_parity_pressure/PROOFS.md`.
- **[TFH]** `research/2026-11-09/aphex_two_fiber_haar/PROOFS.md`.
- **[PB]** `research/2026-11-10/main_xxiii/PARITY_BOUNDARY.md`.
- **[PS]** `research/2026-11-10/main_xxiii/PARITY_SCOPE.md`.
- **[GC]** `research/2026-11-10/gaussian_circle_long_lag/THEOREMS.md`.
- **[PC]** `research/2026-11-15/pi_carrier_collision/THEOREMS.md`, inherited #643.
- **[AH]** `research/2026-11-15/observer_haar_causal_volume/THEOREMS.md`.
- **[FSA]** `research/2026-11-14/source_auth_field_frontier/THEOREMS.md`.
- **[GFT]** `research/2026-11-14/gauge_frontier_bridge/THEOREMS.md`.

## 10. Superseded wording, unresolved coverage and review boundaries

- **Power saving is not required for normality.** [G] §3 uses that phrase;
  the canonical requirement is \(o(N)\) for every fixed nonzero mode.
- **C3-1's “fix any C” equivalence has a constant defect.** Haar satisfies
  \(B_A(2\delta)\to4\delta\), so the stated bound \(\le2C\delta\) cannot
  be necessary for a fixed \(C<2\). The sound catalogue uses **there exists
  finite C**. The sufficiency proof and C3-2's existential statement survive.
- **Finite source-lattice admissibility is not all-depth proof.** The archive
  records a closed-form test through depth200; the response uses actual
  tail admissibility, not extrapolation.
- **A prescribed rate is stronger than an existential slow schedule.** This
  matters for purity, collision depth, return fibers and entropy. No rate is
  inferred from normality without its own proof.
- **Poisson overlap is exact.** F13 is an inherited SCE-01 statistic under an
  affine normalization. F11/F12 are other already inherited characteristic
  kernels. Their new response interface must not be billed as a new theorem
  that one scalar can characterize normality.
- **Single-mode versus all-mode.** IAD-02's schedule equivalence is an all-mode
  statement. A claim that every fixed-h Weyl mean is equivalent to its own
  fixed-h lag response would be false.
- **Prototype calibration is not physical realization.** Phase preparation,
  controlled physical interference, quantum speedup, and source acquisition
  remain separate contracts. The atlas defines mathematical responses.
- **No claim of final completeness beyond the audited entrypoints.** All
  named families found there are represented by F01–F74, including separate
  and unsupported-input rows. A newly found independent target should receive
  a new row or an explicit mapping; it must not be hidden under “all.”
