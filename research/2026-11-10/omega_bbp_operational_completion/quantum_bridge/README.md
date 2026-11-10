# Ω₄ × Ω₅ × Haar → finite quantum circuits: source-faithful dagger bridge

**Research date: 10 November 2026.** A source-first continuation of [Ω₄ × Ω₅ × Haar](../OMEGA_HAAR_WAVELET.md), [inverse-beta BBP root](../INVERSE_BETA_BBP_ROOT.md), and the selected [SUCC π-normality frontier](../../../../docs/PI_NORMALITY_FRONTIER.md). **Draft research only.** Original forcing, zero seed, import/provenance, Main XXII and formal Lean contracts are not modified. No quantum speedup, base-16 π normality, parity balance, RH proof, physical MERA implementation, or completed Ω-to-typed-lambda compiler is asserted.

## Executive verdict

**Proved within finite-dimensional linear algebra (paper and calibrated):** (i) dyadic Haar and 2/3 chronological butterflies have reversible orthogonal lifts; (ii) discarding Haar details requires a quantum measurement/instrument, not a unitary; (iii) the Ω₄/Ω₅ overlapping chronological projectors yield a concrete Hermitian Hamiltonian and a two-window orientation observable; (iv) a heralded two-path interferometer detects their commutator norm; (v) the sixteen inverse branches have an *actual 4-qubit parity-character eigenstate*, with a detectable **controlled** Möbius sign; (vi) the BBP finite rational phase sequence has a strict source-derived precision bound, so an ideal phase/Weyl circuit has an explicit finite-clock error budget.

**Open arithmetic:** all of these quantum probabilities are either source-only diagnostics or mathematically equivalent to the original Weyl sums. None gives their decay for the selected zero seed. The wrong-seed controls remain intact.

### Source conventions: do not shift π by 16

Write `q=1/16` and use the immutable four-pole source

\[
R(j)=\frac4{8j+1}-\frac2{8j+4}-\frac1{8j+5}-\frac1{8j+6},\quad r(n)=R(n-1).
\]

The **analytic** fixed-point fold from [INVERSE_BETA_BBP_ROOT](../INVERSE_BETA_BBP_ROOT.md) is \(B(0)=\sum_{j\ge0}q^jR(j)=\pi\). The **SUCC source-clock prefix** is

\[
P_L=\sum_{j=0}^{L-1}q^{j+1}R(j)\longrightarrow\pi/16.
\]

With the original zero seed, the common-horizon completed phase is \(Z_{n,L}=16^nP_L\), not \(16^nB_L(0)\); the actual completed phase is \(Y_n=16^{n-1}\pi\). The new tests verify every finite recurrence-plus-tail square and this one-factor-of-sixteen distinction.

## 1. What of Gemini's quantum mapping survives?

| Proposed bridge | Mathematical verdict | Essential restriction |
|---|---|---|
| A two-entry Haar butterfly equals Hadamard \(H=(1/\sqrt2)\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)\) | **Exact** as an orthogonal/unitary 2-amplitude gate | The full multiscale **Haar** transform is **not** generally \(H^{\otimes m}\), the **Walsh–Hadamard** transform |
| \(\Omega_4/\Omega_5\) source grouping as circuit clocks | Exact six-step clock diamond \((F^2)^3=(F^3)^2=F^6\) and exact 2/3 block transforms | The \(\Omega_k\) raw lambda AST does **not** execute quantum gates; the 3-block is a qutrit-size orthogonal operation, not one Hadamard |
| Coarse-grain/reverse as a dagger | **Exact** if all Haar detail slots / ancilla flags are retained | \(P\) alone is an orthogonal **projection**, not a deterministic unitary channel. Reversal after discard is impossible without missing details |
| Haar Ω tree = MERA | A **TTN-inspired or wavelet circuit** is constructible | MERA requires specified many-body tensor factors, isometries **and** inter-block disentanglers; none arises automatically from a 16-entry amplitude vector |
| ZX and categorical quantum computation | Sound correspondence for implemented H, phase, controlled permutations, measurements | `FdHilb` includes nonunitary morphisms; arbitrary \(\lambda x.xx\) is *not* a legal arbitrary-quantum-state cloner. Classical code/control can be copied |
| Möbius parity section = quantum phase | Four-qubit branch increment has an eigenstate with eigenvalue -1; controlled increment gives perfect ancilla interference | An *uncontrolled* global -1 is physically unobservable; this is a representation holonomy, not an established dynamical Berry phase or π-digit bias |
| Quantum Haar or Fourier circuit proves speedup | Efficient wavelet **transforms of preloaded amplitudes** are established prior art | State preparation, precision, output measurement, qubit routing and controlled-arithmetic costs must be counted |

**Primary prior art:** Fijany & Williams, [Quantum Wavelet Transforms](https://arxiv.org/abs/quant-ph/9809004) (1998); Vidal, [MERA](https://arxiv.org/abs/quant-ph/0610099) (2006); Selinger–Valiron, [Quantum Lambda Calculus](https://doi.org/10.1017/S0960129506005238) (2006); Coecke–Duncan, [ZX-calculus](https://arxiv.org/abs/0906.4725) (2009). We do not claim priority for Haar gates, quantum wavelet circuits, Stinespring dilations or controlled phase detection.

## 2. Source-driven two-route quantum echo

Let \(P_2\) average chronological neighbors \((0,1),(2,3),(4,5)\) and \(P_3\) average consecutive triples \((0,1,2),(3,4,5)\) in \(\mathbb C^6\). Their overlapping **lossy** observations yield

\[
C=[P_2,P_3]=P_2P_3-P_3P_2,\quad C^*=-C,\quad C^3=-\frac29C,\quad \gamma=\frac{\sqrt2}{3}.
\]

The previous dossier proves the rank-two active plane and positive source area \(\mathscr A_n=\langle r_n,Cr_{n+1}\rangle>0\), with \(r_n=(R(n),\ldots,R(n+5))\) and \(\mathscr A_n\sim 675/(128n^9)\). We now make its measurement semantics explicit.

First, **a low-pass measurement is not a unitary**. An isometric extension of an orthogonal projection \(P\) is

\[
V_P|v\rangle=|0\rangle\otimes P|v\rangle+|1\rangle\otimes(I-P)|v\rangle,\quad V_P^*V_P=I.
\]

This retains a *coherent branch flag*. It extends to a unitary on a larger Hilbert space. Postselecting flag \(0\) yields the trace-decreasing map \(v\mapsto Pv\), not a deterministic gate. Both the 2- and 3-block analysis butterflies are unitary before this postselection.

**Quantum echo, conditioned on successful low-pass steps:** On the path qubit \(|+\rangle\), apply \(P_2P_3\) to arm \(0\) and \(P_3P_2\) to arm \(1\) through their dilation-and-flag implementations. After a path Hadamard, the unnormalized \(|-\rangle\) output amplitude is exactly \(Cv/(2\|v\|)\) for a normalized input \(v/\|v\|\). Therefore its **unconditional joint success-and-minus** probability is

\[
\boxed{p_-(v)=\frac{\|Cv\|^2}{4\|v\|^2}.}
\]

The previous source norm asymptotics give an exact new leading signal for the genuine four-pole window:

\[
\boxed{p_-(r_n)\sim\frac{11}{18}\,n^{-2}.}
\]

The measurement requires both heralding flags and the correct path normalization. Dividing by the success probability would give a *different conditional statistic*. The associated lossless two-route diagram does **not** imply \(P_2P_3=P_3P_2\): it preserves the nonzero defect as a measurable amplitude.

## 3. The exact Hermitian chronology/chirality witness

The anti-Hermitian \(C\) generates a legitimate unitary one-parameter family:

\[
H_C=iC=H_C^*,\qquad U_C(t)=e^{-itH_C}=e^{tC}.
\]

The active 2D real plane rotates by angle \(\gamma t\), and

\[
e^{tC}=I+\frac{\sin(\gamma t)}\gamma C+
\frac{1-\cos(\gamma t)}{\gamma^2}C^2.
\]

**One real source window does not reveal orientation:** \(\langle r_n,iC r_n\rangle=0\). The nonzero quantity is a *two-time* antisymmetric pairing. Put two consecutive real windows in a coherent time-qubit register:

\[
|\Psi_n\rangle=\frac{|0\rangle\otimes r_n+|1\rangle\otimes r_{n+1}}
{\sqrt{\|r_n\|^2+\|r_{n+1}\|^2}},\qquad
H_{\mathrm{ch}}=\sigma_y\otimes(iC).
\]

Since both factors are Hermitian, \(H_{\mathrm{ch}}\) is a valid Hermitian observable on \(\mathbb C^2\otimes\mathbb C^6\) (embeddable into four qubits with four inert basis states). Direct matrix multiplication gives

\[
\boxed{\chi_n=\langle\Psi_n|H_{\mathrm{ch}}|\Psi_n\rangle
=\frac{2\langle r_n,Cr_{n+1}\rangle}
{\|r_n\|^2+\|r_{n+1}\|^2}>0.}
\]

Exchanging the time bins or interchanging the observer order reverses its sign. The *same source* may be read in the opposite coherent computational perspective. Its sign is thus a **relative, source-driven chirality**, not a physical arrow that any arbitrary basis must recognize. With \(R(n)\sim (15/64)n^{-2}\),

\[
\boxed{\chi_n\sim16n^{-5}.}
\]

A second useful exact identity is

\[
\langle\Psi_n|H_{\mathrm{ch}}^2|\Psi_n\rangle
=\frac{\|Cr_n\|^2+\|Cr_{n+1}\|^2}
{\|r_n\|^2+\|r_{n+1}\|^2}
\sim\frac{22}{9}n^{-2}.
\]

Consequently the variance of direct projective readout is \(\sim (22/9)n^{-2}\). The shot variance/mean-squared ratio is \(\sim(11/1152)n^8\): even with ideal state preparation, *ordinary independent projective sampling* of this weak directional signal has high cost. An optimized quantum estimation oracle might change resource scaling; no such algorithm is supplied. We have **an exact observable, not a quantum speedup**.

## 4. Sixteen inverse branches become four qubits and one path qubit

For completed circle dynamics \(t\mapsto16t\pmod1\), the inverse branches \(s_k(t)=(t+k)/16\) have labels \(k\in\mathbb Z/16\mathbb Z\). The associated character states live naturally on **four address qubits**:

\[
|\chi_m\rangle=\frac14\sum_{k=0}^{15}e^{2\pi imk/16}|k\rangle,\qquad
S|k\rangle=|k+1\pmod{16}\rangle.
\]

Then \(S|\chi_m\rangle=e^{-2\pi im/16}|\chi_m\rangle\). For the parity sector,

\[
\boxed{|\chi_8\rangle=H^{\otimes4}|0001\rangle,
\qquad S|\chi_8\rangle=-|\chi_8\rangle.}
\]

This is an **exact four-qubit Hadamard realization of the parity packet** \(H_8\), not a claim that the full sixteen-way Fourier transform equals \(H^{\otimes4}\). A controlled \(S\) on a fifth path qubit initialized in \(|+\rangle\) sends it to \(|-\rangle\) and a final path Hadamard yields outcome 1 with certainty. The m=0 character instead gives outcome 0. A concrete 5-qubit [OpenQASM 3 gate sketch](CIRCUIT.qasm) compiles the controlled 4-bit increment using high-to-low controlled-X gates; its entire 32-entry **classical gate truth table** is verified, but a QASM compiler/hardware runner was unavailable. Further hardware connectivity, noise and compilation-cost analysis is open.

The minus sign is globally invisible if \(S\) is applied without the reference qubit. Relative interferometry operationalizes the *monodromy of the chosen parity line bundle*—it is **not** by itself a source-specific π statistic or a measured geometric Berry phase. For the real \(\theta_n\) orbit, the exact twisted identity from the predecessor dossier remains

\[
(-1)^{d_n}e^{\pi i(2j+1)\theta_{n+1}}
=e^{2\pi i\,8(2j+1)\theta_n}.
\]

So the low-pass branch, parity detail, and future phase *multiply to the old Weyl target*. The full source/CRT winding and literal integer lift remain load-bearing.

## 5. A true quantum-style circuit for the old Weyl criterion—and its honest limit

For a **dyadic epoch** \(A=2^m\) and phase frequency \(h\in\mathbb Z\), define an ideally preloaded m-qubit pure state

\[
|\psi_{A,h}\rangle=\frac1{\sqrt A}\sum_{n=A}^{2A-1}
 e^{2\pi i h16^nP_\infty}|n-A\rangle,
\qquad P_\infty=\pi/16.
\]

Then applying \(H^{\otimes m}\) and measuring zero gives

\[
\boxed{\Pr(0^m)=\left|\frac1A\sum_{n=A}^{2A-1}
 e^{2\pi i h16^nP_\infty}\right|^2=|c_A(h)|^2.}
\]

For a non-dyadic \(A\), one can embed the \(A\)-entry register in \(2^{\lceil\log_2 A\rceil}\) dimensions and use a prepared uniform \(A\)-mask; the all-epoch theorem does **not** follow merely from experiments on \(A=2^m\). This is a quantum **re-expression of Weyl's criterion**, not a bound on \(c_A(h)\). Efficient construction of the controlled BBP phases, initial state preparation and repeated readout is not demonstrated.

The wrong-seed control is decisive: with rational finite prefix \(P_L\), choose the rational seed \(s=-P_L\) and evaluate \(16^n(s+P_L)=0\). Every supplied phase is 1, so the circuit reports \(\Pr(0^m)=1\), despite exactly the same forcing. With the mathematical real seed \(s=-\pi/16\), this persists for the completed orbit. No source-only Hadamard or wavelet circuit can eliminate this shadow.

### New strict, source-specific finite-horizon phase budget

Since \(P(x)=(1-x)(x^2+2)(x^2+2x+2)\) is nonnegative and its two quadratic factors are at most 3 and 5 on \([0,1]\),

\[
0<R(j)=\int_0^1x^{8j}P(x)\,dx
<\frac{15}{(8j+1)(8j+2)}.
\]

Hence for every integer \(L\ge1\) and \(n\ge0\), geometric summation proves

\[
\boxed{0<16^n(P_\infty-P_L)<
\frac{16^{n-L}}{(8L+1)(8L+2)}.}
\]

For the epoch \(A\le n<2A\), \(L\ge2A\), and fixed h, let \(\delta_{A,L}(h)\) bound the difference of exact and prefix mean phases. The unit-circle Lipschitz inequality gives

\[
\boxed{\delta_{A,L}(h)\le
\frac{2\pi|h|16^{2A-1-L}}{(8L+1)(8L+2)},\quad
|\Pr_{\rm true}(0^m)-\Pr_{\rm prefix}(0^m)|\le 2\delta_{A,L}(h).}
\]

At \(L=2A\), the mean-phase error is \(O_h(A^{-2})\), proved with **exact rational source plus an analytic tail bound**. If h grows with A, it retains an explicit h-dependent precision debt. Discontinuous digit-parity readout still needs boundary-strip control; this smooth Fourier budget does not pay it.

## 6. Full SUCC connections and honest separation of goals

- **Ω₃ inverse-beta fold:** the *classical* source computation has a typed recursive context \(F(g)(n)=R(n)+qg(n+1)\) and a bounded analytic fixed point. This is the control/evaluation plane, not the quantum no-cloning-violating self-application of unknown qubits. The original \(\lambda x.xx\) can duplicate a *classical piece of code*, not an arbitrary quantum state.
- **Ω₄/Ω₅ six-step source diamond:** the exact arithmetic folds commute. Their **overlapping chronological low-pass measurements** create a rank-two noncommuting defect. If instead we choose independent CRT row/column tensor-factor projections, they commute: the oscillator is *observer- and time-partition-specific*, not a universal curvature of SUCC or the primes.
- **#565 recursive Haar / 16-child transfer:** the 16-address register gives a reversible *complete* Fourier/Walsh packet before any detail discard. It is compatible with the principle of retaining all sixteen children and the future tail; an actual conditional temporal-Haar contraction remains UNPROVED.
- **#572 complete CRT / #574 Aphex two-fiber contrast:** the m=8 packet isolates a parity representation but cannot replace all older prime powers, CRT winding, prime-conditioned complementary sign or real future-tail crossing. An observed branch-Hadamard result is not the conditional contrast \(\beta_A^*\to0\).
- **#544 carried phase / Cayley pinbed:** the rigorous finite source-clock quantum bound above can be combined with the retained integer lift and source-vs-observer phase precision. The circle quotient forgets digit branch labels: a quantum unitary can only reverse it if they are stored as a witness/ancilla.
- **SUCC/FUCC arithmetic factor ontology and ER=EPR ideas:** tensor products, dagger maps and TFD-like states are coherent *candidate modeling languages* for arithmetic observers, not demonstrated equivalences to the Hilbert space of prime factorizations or physical spacetime. A many-body MERA requires additional specified site Hilbert spaces, cross-block disentanglers, and a physically motivated/variational Hamiltonian; a source-index amplitude wavelet is not one.
- **Source-selected π normality:** the authentic initial seed, four poles, carry history and Archimedean signed correlations are still necessary; no cancellation follows from unitary implementability, positivity of \(\mathscr A_n\), exact monodromy, or a finite Hadamard circuit.

### Source-only reweighting no-go

Since \(n^5\chi_n\to16\), any putative weighted phase mean on an epoch satisfies

\[
\left|\frac1A\sum_{n=A}^{2A-1}n^5\chi_n e(hY_n)
-16\frac1A\sum_{n=A}^{2A-1}e(hY_n)\right|
\le\sup_{n\ge A}|n^5\chi_n-16|\to0.
\]

Therefore this positive orientation weight alone is **asymptotically equivalent to the old Weyl target**. On the coherent counterseed, both remain nonvanishing. To progress, we must prove a new *conditional signed source–branch covariance*, not just build an increasingly accurate representation.

## 7. Claim ledger, probes, and boundaries

| Claim | Verdict | Evidence / next meaningful challenge |
|---|---|---|
| Two-/three-entry orthogonal butterfly, full Haar Parseval, 16-character parity state and controlled monodromy | **DISCLOSED** finite exact linear-algebra statements | Fast deterministic tests with phase/energy controls; actual physical gate synthesis UNVERIFIED |
| Dagger/isometric detail-preserving coarse-graining; nonunitary postselection boundary | **DISCLOSED** | Test ancilla norm/reconstruction; trace preservation fails for lowpass-only |
| Source Ω₄/Ω₅ heralded defect \(p_-\sim11/(18n²)\) | **DISCLOSED** conditional on the previous exact source asymptotics; numerically CALIBRATED | Mutate projection order, forcing poles, use independent second implementation |
| Hermitian chirality \(\chi_n>0,\ \chi_n\sim16/n^5\), variance \(\sim22/(9n²)\) | **DISCLOSED** conditional on the previous source-area theorem; finite matrix CALIBRATED | Reverse clock, mutate source, source-only weights and different basis/partitions |
| \(\Pr(0^m)=|c_A(h)|²\), phase precision bound | **DISCLOSED** as finite-dimensional/analytic identities | Wrong-seed constant phase; check all n/L indexing; no efficient oracle asserted |
| MERA, AdS/CFT, physically entangled BBP carrier, quantum advantage, Ω→quantum lambda compiler | **UNVERIFIED** | Need many-body tensors, typed calculus, gate synthesis, resource accounting and independent physical model |
| Original-zero odd-eight cancellation, parity balance, π base-16 normality, RH | **OPEN** | Must obtain asymptotic source-specific signed estimate surviving PPP-08 and seam controls |

**Independent witness scope:** the stand-alone tests are same-team code checks, not independent mathematical referees. A second numerical linear-algebra implementation is logged in [VALIDATION](VALIDATION.md). \(\pi\) base-16 normality remains OPEN. The strongest new mathematical result is a **precisely measurable source-driven quantum chirality and an explicit phase precision budget**, neither of which itself pays the signed cancellation debt.
