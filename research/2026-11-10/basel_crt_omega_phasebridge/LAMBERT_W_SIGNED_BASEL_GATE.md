# Lambert-W inversion of the authentic BBP × signed Basel phase budget

**Date:** 2026-11-10. **Proposed additive child of SUCC research PR #585**, based on Main XXIII candidate PR #584.  
**Claims:** finite source-specific approximation/certification theorems (paper proofs with exact rational executable controls). The signed cancellation bound, π base-16 normality, RH, and physical Ω interpretation remain **OPEN**.  
**Authentic source:** `R(j)=4/(8j+1)-2/(8j+4)-1/(8j+5)-1/(8j+6)`, `P_L=Σ_(j=0)^(L-1)16^(-j-1)R(j)`, `P_∞=π/16`, initial seed `s=0`. This file does **not** alter frozen source contracts or parent papers.

## The object and why W really appears

The previous [signed Basel theorem](SIGNED_BASEL_TAUBERIAN.md) defines, for nonzero integer Fourier mode `h` and the authentic selected real lift `Y_n=16^nπ/16`, the absolutely convergent complex tail

\[
F_h(A)=\sum_{n=A}^\infty \frac{e^{2\pi ihY_n}}{n^2},\qquad A\ge 11.
\]

The **unproved** statement `A F_h(A)→0` for every fixed `h≠0` is equivalent to base-16 normality of π, not a consequence of the unsigned Basel identity. Lambert `W` provides an **exact inversion of the finite-source precision requirement**, because the BBP future has exponential precision in `L`, suppressed by `L^{-2}`, and the Basel observer itself weighs time by `n^{-2}`. This advances the *finite auditable instrument*, not the missing asymptotic cancellation estimate.

### T1. A source-faithful, finite signed Basel certificate (DISCLOSED, elementary proof)

Fix integers `A≥11`, `R≥1`, `h≠0`. Set `M=A R` and choose any source horizon `L≥1`. Define the finite original-source readout

\[
G_{h;A,R,L}=A\sum_{n=A}^{M}\frac{e^{2\pi ih16^nP_L}}{n^2}
\]

and the **entirely rational** amplification observable

\[
S_{A,M}=A\sum_{n=A}^{M}\frac{16^n}{n^2}>0.
\]

Use the previously authenticated BBP positive-moment tail inequality

\[
0<P_\infty-P_L<\frac{16^{-L}}{(8L+1)(8L+2)},
\]

and `|e^{ix}-e^{iy}|≤|x−y|`. The archimedean bound `2π<44/7` and `(8L+1)(8L+2)≥64L²` give the **source-selected rational phase error**

\[
\left|A\sum_{n=A}^{M}\frac{e^{2\pi ih16^nP_\infty}-e^{2\pi ih16^nP_L}}{n^2}\right|
<\frac{11|h|}{112}\frac{S_{A,M}}{L^2 16^L}.
\tag{1}
\]

Independently, integral comparison bounds the discarded infinite Basel tail:

\[
A\sum_{n=M+1}^\infty\frac1{n^2}\le\frac A M=\frac1R.
\tag{2}
\]

Let the exact rational threshold be

\[
\boxed{B_{h;A,R}=\frac{11|h|R}{112}\,S_{A,AR}
=\frac{11|h|AR}{112}\sum_{n=A}^{AR}\frac{16^n}{n^2}.}
\tag{3}
\]

For every integer `L≥1` satisfying **the exact integer-rational comparison**

\[
\boxed{L^2 16^L\ge B_{h;A,R},}
\tag{4}
\]

combining (1)–(2) proves

\[
\boxed{\left|A F_h(A)-G_{h;A,R,L}\right|<\frac2R.}
\tag{5}
\]

The strict inequality is safe: (1) is strict. The proof uses only source authentication and positive estimates, and is valid for any phase seed *provided the same seed is retained on both sides*; it says nothing about phase cancellation.

**Certification note.** `P_L` and `B_{h;A,R}` are rational. Each `h16^nP_L` has an exactly computable rational residue modulo 1 **after preserving the integer lift**. A separate outward enclosure for sine/cosine converts `G` to a rigorous complex interval. An ordinary unbounded-precision floating sum is not itself such an interval certificate.

### T2. Lambert W is precisely the inverse source-horizon clock (DISCLOSED)

Write `λ=log16`. For `B=B_(h;A,R)>0` the strictly increasing function `x↦x²16^x` on `x>0` has unique positive inverse

\[
\boxed{L_*(B)=\frac{2}{\lambda} W_0\!\left(\frac{\lambda}{2}\sqrt B\right).}
\tag{6}
\]

Indeed `u=(λ/2)L` gives `(u e^u)²=(λ²/4)B`, and `W_0(z)e^{W_0(z)}=z`. Therefore the **exact smallest allowed positive integer horizon** is

\[
\boxed{L=\max(1,\lceil L_*(B)\rceil),}
\tag{7}
\]

which in executable code is obtained without trusting a floating W value by comparing the two rational integers in (4). The numerical W computation is a convenient prediction only; the certificate is the integer inequality. See [NIST DLMF §4.13](https://dlmf.nist.gov/4.13) for real branch conventions.

### T3. Link to SUCC's *existing* Lambert-W entropy clock, and asymptotic three-log compression

[SUCC Lambert Entropy Forge, LWE-01](../../2026-11-08/lambert_entropy_forge/THEOREMS.md) already uses

\[
w_A=W_0(e^\gamma A),\quad k_W(A)=\left\lfloor\frac{w_A-\gamma}{\log16}\right\rfloor
\]

to schedule an independent **coupon-collector reference** for fine digit words. Its coupon benchmark is not a theorem about deterministic π digits. Reuse this pre-existing W scale solely to choose an **independent Basel observation horizon**, for example

\[
R_A=1+\lceil w_A\rceil,\qquad M_A=A R_A,\qquad B_A=B_{h;A,R_A},\quad L_A=\max(1,\lceil L_*(B_A)\rceil).
\]

For each *fixed* `h≠0`, `R_A→∞`, `R_A~log A` and (5) implies

\[
\boxed{A F_h(A)\longrightarrow0\quad\Longleftrightarrow\quad
G_{h;A,R_A,L_A}\longrightarrow0.}
\tag{8}
\]

Thus all nonzero Fourier modes satisfying the finite signed gate (8) is precisely another normality-equivalent criterion—not a proof of the gate.

A sharper, source- and weight-specific fact is that `n=M` exponentially dominates the rational amplification sum:

\[
\sum_{n=A}^{M}\frac{16^n}{n^2}
=\frac{16^M}{M^2}\left(\frac{16}{15}+o(1)\right)
\quad\text{when }M=A R_A\to\infty,\ R_A\to\infty.
\tag{9}
\]

Proof: write `n=M-j`, pull out `16^M/M²`, and use geometric domination of the fixed `j` factors `16^{-j}(M/(M-j))²`; split at `j=M/2` to dominate the remaining part exponentially, since `M/A=R_A→∞` but `A≥11`. Equation (3) consequently gives

\[
B_A=\frac{11|h|}{105}\,\frac{16^{M_A}}{M_A}(1+o(1)).
\tag{10}
\]

Take logarithms of the real equation `L_*²16^{L_*}=B_A`, noting `L_*/M_A→1`, to obtain

\[
\boxed{L_*(B_A)=M_A-3\log_{16}M_A+
\log_{16}\!\left(\frac{11|h|}{105}\right)+o(1).}
\tag{11}
\]

The integer `L_A` differs from this by less than one plus `o(1)`. **The `3 log_16 M` saving is a precision/computation fact, not a signed harmonic cancellation fact.** Its coefficient reflects the reciprocal-square BBP tail, the reciprocal-square Basel observation, and the macroscopic normalization `AR=M`. Substituting a merely bounded source tail would change the coefficient. Check it against finite exact integer thresholds rather than extrapolating fitted values.

The number of *orbit observation points* `M−A+1` is still `Θ(A log A)` and the rational prefix size is huge. W does not create computational efficiency sufficient to infer asymptotic normality from finite data.

### T4. A second, independent real W branch: the alias-amplification microscope

The phase sensitivity at the `n`th index under a perturbation of the completed phase `α` is controlled (only in absolute value) by `16^n/n²`. For a target amplification `Q≥16`, the large real solution of

\[
\frac{16^x}{x^2}=Q,\qquad x\ge1
\]

is

\[
\boxed{x_+(Q)=-\frac2{\log16}\,W_{-1}\!\left(-\frac{\log16}{2\sqrt Q}\right).}
\tag{12}
\]

This is the **negative** real Lambert branch (the principal branch returns the other, subunit solution for large Q). The statement locates a sensitivity threshold; it gives no lower bound on the distance of `16^nπ` from an integer, no phase distribution, and no oscillatory cancellation. For `Q=16^n/n²`, the formula returns `n` exactly for integer `n≥1`.

### T5. An exact base-16 Fourier-index transport inherited by the signed Basel tail

For any completed phase `α` and `F_h(A;α)=Σ_(n≥A)n^(-2)e(h16^nα)`, use `a_n(16h;α)=a_(n+1)(h;α)` to get

\[
F_{16h}(A;\alpha)=\sum_{m=A+1}^\infty\frac{a_m(h;\alpha)}{(m-1)^2}.
\]

Subtract `F_h(A+1;α)` and telescope the positive weights, yielding the exact universal bound

\[
\boxed{\left|F_{16h}(A;\alpha)-F_h(A+1;\alpha)\right|\le\frac1{A^2}.}
\tag{13}
\]

This permits reducing the *list of necessary fixed-frequency checks* to indices `h` **not divisible by 16**: any `h=16^j q` is handled by iterating (13) for fixed `j`. It does not establish decay for those primitive modes. The Fourier-index relation is a classical shift identity, not a new source-specific theorem.

## Crucible: what W does **not** prove

1. **Coherent wrong seed:** `s*=−π/16` produces `α=0`, `a_n=1`, `A F_h(A;s*)=Aζ(2,A)→1` for each `h`, despite satisfying the same W clock and unphased Basel/Ω identities. `s_L=−P_L` is a distinct rational *finite common-horizon* control.
2. **Periodic rational phase:** `α=1/255`, `h=255` yields `a_n=1` for every n. Large exponential derivative/amplification alone gives no cancellation.
3. **Irrational sparse-spike phase:** `α=Σ_(j≥1)16^{−m_j}` with `m_j=2^(2^j)` is irrational and has separated isolated base-16 digits. For `A_j=2m_j` and the W observation horizon `M_j=A_jR_(A_j)`, eventually `M_j<m_(j+1)`. On the whole window `n∈[A_j,M_j]`, all past digits yield integral contributions and all future digits give a fractional remainder bounded by `(16/15)16^{M_j−m_(j+1)}`. Therefore `a_n(h;α)=1+o(1)` uniformly for any fixed `h`, `A_j F_h(A_j;α)→1`, and `G_(h;A_j,R,L)→1` under the accuracy budget (5). **Irrationality, an increasing `16^n/n²` gain, and Lambert scheduling do not force normality.**
4. **Fake sources and PPP-08:** finite source matching and local CRT primaries do not force the real signed complement. Every genuine source-selected saving must reject matched extra-pole mutants and SUCC's p-integral wrong-seed shadow.
5. **Continuous-phase trap:** integrating `e(i c16^x)/x²` over the real line may show strong continuous oscillation, but does not control integer sampling, where exact resonances survive. A stationary-phase estimate for a smooth interpolation is not a bound on the discrete selected sum.

## Claim ledger and next verdict-changing probe

- **DISCLOSED (scoped algebra):** T1 finite source-selected bound (1)–(5); exact principal W inverse (6)–(7); asymptotic precision compression (9)–(11); negative-branch sensitivity scale (12); mode transport (13). Existing Basel↔Weyl equivalence is **imported** from `SIGNED_BASEL_TAUBERIAN.md`.
- **OBSERVED (local):** focused exact `Fraction` tests, independent `mpmath` finite-phase smoke, wrong-seed, periodic, sparse-digit controls; no external blind review or formal Lean check.
- **REFUTED:** "Lambert-W inverts the exponential derivative, therefore π normality follows"; wrong-seed and irrational sparse-phase countermodels are concrete witnesses.
- **OPEN / UNVERIFIED:** `G_(8k;A,R_A,L_A)→0` for the authentic zero seed for each odd `k` (conditional parity-word input), and `G_h→0` for every nonzero integer `h` (full normality). These require new **signed arithmetic cancellation**, not just increasingly accurate finite readouts.

**Next probe:** pre-register fixed odd-eight `h=8`, select non-dyadic A, compute certified rational-source phases with the exact W horizon (4), and project the signed sum against the complete 2/3-CRT, all-odd-prime and Archimedean carry ledger. Require a source-specific proof of *asymptotic* saving (or a rigorously certified counterexample to a proposed rate) which fails on both coherent and PPP-08 wrong-seed controls. Do not fit an asymptotic exponent from finite measurements.

## Reproduction

`test_lambert_basel_gate.py` covers original source, strict tail, exact integer threshold, W0 and W_-1 inverses, 3-log asymptotic calibration, rational windings, source phase budget, coherent/periodic/sparse-digit adversaries, and bounded-tail truncation. Run only that focused test module; PR #584's costly native suite/hosted CI is **not** a prerequisite to inspect this additive research artifact and is not claimed to have passed here.

Sources: `SIGNED_BASEL_TAUBERIAN.md`, `PHASE_OBSERVER.md`, `PROOFS.md` in this directory; prior SUCC `research/2026-11-08/lambert_entropy_forge/THEOREMS.md`; and [DLMF §4.13](https://dlmf.nist.gov/4.13).
