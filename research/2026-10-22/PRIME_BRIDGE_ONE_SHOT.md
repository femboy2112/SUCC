# PRIME BRIDGE ONE-SHOT — Arithmetic ⇄ Analytic ⇄ EPR ⇄ 2-Adic Code

**2026-10-22. Parent main:** `b116841f12b41aaf7600da39bbb40577f25b6295`. **Research-only, no merge permission.** This is a source-scoped finite composition of established structures with new-to-SUCC explicit transport theorems. **It is NOT an ER wormhole, Einstein geometry, an RH proof, or a claim of academic novelty.** All proof obligations and counterexamples are preserved.

## 1. Classical ingredients and provenance

- Hedenmalm, Lindqvist, Seip, *A Hilbert space of Dirichlet series and systems of dilated functions*, Duke Math. J. 86 (1997), https://arxiv.org/abs/math/9512211. Defines square-summable Dirichlet/Bohr Hilbert space.
- Pastawski, Yoshida, Harlow, Preskill, *Holographic quantum error-correcting codes*, JHEP 06 (2015) 149, https://arxiv.org/abs/1503.06237, Appendix A.2: **the known three-qutrit perfect code**, not invented here.
- Bhattacharyya, Hung, Lei, Li (2018), https://arxiv.org/abs/1703.05445, and Hung, Li, Melby-Thompson (2019), https://arxiv.org/abs/1902.01411: genuine p-adic holographic context, *not imported here as a theorem about SUCC*.
- Internal precursors: SUCC PR #136 (`unit_prime_succ.py`) and merged PR #153 (`affine_pontryagin_transfer.py`). No preexisting source/archival files changed.

The new-to-project result is not the code or the arithmetic Hamiltonian. It is an **explicit exact commuting network** involving authenticated finite prime-power coefficients, reversibly sampled Dirichlet polynomials, the thermofield mirror, a geometric first shell, and operational two-leg operator reconstruction.

## 2. Global arithmetic ⇄ analytic theorem (classical)

Let `H=ell²(N_{>=1})`, `S e_n=e_{n+1}`, `V_p e_n=e_{pn}`, and `H₀ e_n=(log n)e_n` on `D(H₀)={a:sum (log n)²|a_n|²<∞}`.

Then `V_p S=S^p V_p` and `[H₀,V_p]=(log p)V_p` on the invariant finitely supported core. Define the Hardy–Dirichlet Hilbert space by coefficient norm and the transform

\[
\mathcal B(a)(s)=\sum_{n\ge1}a_n n^{-s},\qquad
\|\mathcal B(a)\|^2=\sum_{n\ge1}|a_n|^2.
\]

This is a unitary onto the *specified coefficient-norm image*. Point evaluation is bounded for `Re(s)>1/2` by Cauchy–Schwarz. For each fixed `sigma>1/2`, the coefficient recovery formula is

\[
a_n=\lim_{T\to\infty}\frac1{2T}\int_{-T}^T
 n^{\sigma+it}\mathcal B(a)(\sigma+it)\,dt.
\]

**Proof:** `sum |a_m|m^{-sigma}<∞`; interchange the convergent sum and bounded Cesàro means of `exp(it log(n/m))`, which converge to `delta_{nm}`. Do not claim finite uniform recovery for arbitrary Dirichlet series, or evaluation at `s=0` on the entire Hilbert space.

The conjugate operators `S_D=B S B^{-1}` and `M_{p^{-s}}=B V_p B^{-1}` satisfy the *same braid* `M_{p^{-s}} S_D=S_D^p M_{p^{-s}}`. This is representation coherence, not operator commutativity.

For `beta>1`, let

\[
|\Omega_\beta\rangle=\frac1{\sqrt{\zeta(\beta)}}
\sum_{n\ge1}n^{-\beta/2}|n,n\rangle.
\]

It has reduced density `rho=diag(n^{-beta}/zeta(beta))` and entropy `log zeta(beta)-beta zeta'(beta)/zeta(beta)`. The analytic two-variable representative is

\[
(\mathcal B\otimes\mathcal B)|\Omega_\beta\rangle(s,t)
=\frac{\zeta(s+t+\beta/2)}{\sqrt{\zeta(\beta)}}
\quad (\Re s,\Re t>1/2).
\]

The prime mirror relation follows termwise:

\[
(V_p\otimes I)\Omega_\beta
=p^{\beta/2}(I\otimes V_p^\dagger)\Omega_\beta.
\]

The mirror map is *order reversing* under operator composition and must be domain-checked where the inverse Schmidt diagonal is unbounded. It is not time travel, communication through entanglement, or a gravity theorem.

## 3. Finite exact analytic source chart

Restrict the actual arithmetic source to

\[
C=\operatorname{span}\{|1\rangle,|2\rangle,|4\rangle\},\qquad
T=P_CV_2P_C,\qquad T|0\rangle=|1\rangle,\ T|1\rangle=|2\rangle,\ T|2\rangle=0.
\]

The labels `0,1,2` are prime-depth *indices*, not a cyclic SUCC clock. The Dirichlet polynomial `F_a(s)=a_0+a_1 2^{-s}+a_2 4^{-s}` has the exact source-to-samples map at `s=1,2,3`. Its inverse is

\[
\begin{bmatrix}a_0\\a_1\\a_2\end{bmatrix}
=\begin{bmatrix}
1/3&-2&8/3\\
-4&20&-16\\
32/3&-32&64/3
\end{bmatrix}
\begin{bmatrix}F(1)\\F(2)\\F(3)\end{bmatrix}.
\]

This is a full rational inverse **on this 3-dimensional chart**, not on the infinite source.

## 4. A genuine first Bruhat–Tits shell, with a standard exact code

For the `PGL₂(Q₂)` Bruhat–Tits tree, choose lattice `L₀=Z₂²`. The index-two sublattices between `2L₀` and `L₀` correspond to lines of `F₂²`, equivalently kernels of the forms `(1,0),(0,1),(1,1)`. Hence the source geometric vertex has **exactly three** genuine neighboring classes.

Attach a three-valued quantum system to each neighboring branch, labeled by positions `x=0,1,2 in F₃`. **This choice of F₃ alphabet is external to the Q₂ geometry**, not a canonical arithmetic identification.

Use the **classical** [[3,1,2]]_3 encoding

\[
W|i\rangle=\frac1{\sqrt3}
\sum_{j\in\mathbb F_3}|j,j+i,j+2i\rangle,\quad i\in\mathbb F_3.
\]

Its three supports are disjoint size-three sets, so `W†W=I`. This is one p-adic star, **not** an infinite tensor network or a p-adic CFT.

### AEPB-01 (classical, proved explicitly): any two-leg bulk reconstruction

Choose any visible pair of branch positions `x≠y` with observed values `u,v` and let `z` be the omitted position. Compute

\[
i=(v-u)(y-x)^{-1}\pmod3,\quad
j=u-ix,\quad k=j+iz.
\]

The map `(u,v)↔(i,k)` is a 9-state basis permutation, defining a two-leg unitary `D_{xy}`. Direct substitution gives, for every `|i>`,

\[
(D_{xy}\otimes I_z)W|i\rangle
=|i\rangle_{\mathrm{logical}}
\otimes\frac1{\sqrt3}\sum_{k=0}^2|k\rangle_{\mathrm{anc}}|k\rangle_z.
\]

Thus arbitrary unknown bulk input, even entangled with an external reference, can be recovered from **each** of the three choices of two visible legs. Every operator on the logical space has a two-leg boundary representative, without no-cloning violations.

### AEPB-02 (new-to-SUCC scoped intertwiner): authentic compressed prime transport

Define the explicit two-leg map `T_{xy}` in decoded coordinates: `|i,k>↦|i+1,k>` for `i=0,1`, and `|2,k>↦0`. Its direct computational-basis action is implemented by `pair_decode` / `pair_encode` / `two_leg_prime_shift` in `arithmetic_epr_star.py`. The erased branch is unchanged.

Substitute the codeword formula to prove

\[
(T_{xy}\otimes I_z)W=WT
\quad\text{and}\quad
(T_{xy}^\dagger\otimes I_z)W=WT^\dagger
\]

for all three distinct choices `(x,y)`. This is real operator reconstruction, not a graph illustration.

### AEPB-03 (new-to-SUCC finite EPR transport): every one of nine region pairs

At `beta=2`, the finite normalized prime-depth thermofield state is

\[
|\omega\rangle=(4|0,0\rangle+2|1,1\rangle+|2,2\rangle)/\sqrt{21}.
\]

The exact mirror law is

\[
(T\otimes I)\omega=2(I\otimes T^\dagger)\omega.
\]

Encode both sides with `W`. For *any* left two-leg region `A` and right two-leg region `B`, the reconstruction theorem gives

\[
(T_A\otimes I)(W\otimes W)\omega
=2(I\otimes T_B^\dagger)(W\otimes W)\omega.
\]

**All nine pairs pass exact integer support comparison**. The physical vector has 27 support words with common amplitude denominator `3 sqrt(21)`. The factor 2 comes from the genuine arithmetic coefficients; the code alone does not supply it. **Mutation:** coefficients `(4,2,2)` remain valid qutrit code data but violate the factor-two mirror identity in all nine pair tests.

### AEPB-04 (classical exact entropy splitting): one bond plus logical bulk

For every logical density matrix `rho`, the same decoder yields

\[
D_{xy}\,\operatorname{Tr}_z(W\rho W^\dagger)\,D_{xy}^\dagger
=\rho\otimes I_3/3.
\]

Thus `S(visible pair)=S(rho)+log3` and `S(erased leg)=log3`. For the thermal finite source `rho=diag(16,4,1)/21`,

\[
S(\rho)=\log21-\frac{24}{7}\log2,\qquad
S(\text{visible pair})=\log3+\log21-\frac{24}{7}\log2.
\]

This is the familiar **code-theoretic** area-plus-logical-entropy identity in an arithmetic interface. It is not a gravitational RT/QES derivation.

## 5. Sharp no-go results from hostile controls

### AEPB-N1: naive source compression does not preserve all SUCC composition

On the full source, `V₂S=S²V₂`. On `C={1,2,4}` define `T=PV₂P` and `B=PSP`. Then

\[
TB|1\rangle=|4\rangle,\qquad B^2T|1\rangle=0.
\]

So `TB≠B²T`. Full endpoint-projected compositions `PV₂SP=PS²V₂P` are still equal; the obstruction comes from **projections between path steps**. Any true global SUCC duality must preserve source-supported paths or specify controlled exit/error data. A finite code does not silently restore the lost braid.

### AEPB-N2: infinite arithmetic entanglement cannot fit into a finite boundary code

For every `beta>1` the global TFD has infinite Schmidt rank. No linear isometry from `ell²(N)` to a finite 3-qutrit boundary exists. For any pure state `phi` of Schmidt rank at most `D`, the standard Schmidt/Ky Fan estimate gives

\[
|\langle\Omega_\beta,\phi\rangle|^2
\le\frac{\sum_{n=1}^{D}n^{-\beta}}{\zeta(\beta)},\qquad
D_{\mathrm{tr}}\ge\sqrt{1-
\frac{\sum_{n=1}^{D}n^{-\beta}}{\zeta(\beta)}}.
\]

Our specific `{1,2,4}` chart captures probability `(1+2^{-beta}+4^{-beta})/zeta(beta)`, **not** all of it. For `beta=2` it omits `1-21/(16 zeta(2))` (~0.20209568).

For ordinary prefix `1..N`, the normalized squared error in the prime mirror identity at `beta=2` is *exactly*

\[
\varepsilon_{N,p}^2=
\frac{\sum_{\lfloor N/p\rfloor<n\le N}n^{-2}}
{\sum_{n\le N}n^{-2}}.
\]

It tends to zero but is **not pointwise monotone**: `epsilon_{2,2}²=1/5`, `epsilon_{3,2}²=13/49>1/5`. The tests explicitly kill false claims of finite exactness or monotonic convergence.

## 6. Independent analytic bonus: bounded SUCC interactions do not change the Gibbs threshold

Define `H_g=H₀+g(S+S†)` for real `g` on `D(H₀)`. The interaction norm is at most `2|g|`. Bounded self-adjoint perturbation preserves self-adjointness and compact resolvent, and min–max on ordered eigenvalues gives

\[
\log n-2|g|\le\lambda_n(H_g)\le\log n+2|g|.
\]

For all `beta>0`, `Tr(exp(-beta H_g))` is finite **iff beta>1**, and for `beta>1`

\[
e^{-2\beta|g|}\zeta(\beta)
\le\operatorname{Tr}(e^{-\beta H_g})
\le e^{2\beta|g|}\zeta(\beta).
\]

Do not use the false general rule that exponential is operator-monotone in Loewner order: the proof compares **ordered eigenvalues**. This establishes the exact critical-temperature boundary, not a new interacting gravity theory.

## 7. Verification, source status, next decisive lamp

Run (from repo root):

    PYTHONPATH=. python -Werror -m unittest discover -s tests -p test_arithmetic_epr_star.py -v
    python scripts/arithmetic_epr_star_probe.py

**Observed locally:** 12 exact tests pass on Python 3.13; paper derivations above do not inherit Lean proof authority from those tests. The generated finite receipt also records SHA-256 hashes of the exact source and test modules. No existing archive or source manifest has been changed.

**Ledger:**
- AEPB-01 and AEPB-04: **CLASSICAL / explicit paper proof + exhaustive exact finite tests**.
- AEPB-02 and AEPB-03: **PROVED LOCAL / new-to-SUCC compositional construction**; academic novelty not assessed.
- AEPB-N1: **REFUTED** naive fully compositional three-state compression by exact counterexample.
- AEPB-N2: **REFUTED** finite exact realization of entire infinite TFD by Schmidt rank.
- AEPB-05: **CLASSICAL / paper proof**, not kernel formalization.
- Source-canonical multi-depth p-adic/adelic holography, quantum gravity, original signed Weil positivity and RH: **UNVERIFIED/OPEN**.

**Verdict-changing next probe:** produce a compatible, source-indexed diagram for **both** `S` and `V_p` on a cofinal family of arithmetic charts, accounting for paths that leave finite sectors, and construct multi-depth Bruhat–Tits code maps whose refinement and two-sided operator reconstruction commute *without defining every map by conjugation*. Either demonstrate a nontrivial limit with uniform norm/source-error bounds or prove its obstruction. That—not another finite EPR pair—is the remaining geometric bridge.
