# SUCC × 4D Yang–Mills: quantum computational graphs, Haar wavelets and genuine gauge quotients

**Status:** `PAPER-DERIVED` elementary finite/compact Haar identities, exact finite executable controls, and `OPEN` Yang–Mills continuation. Research continuation stacked on [SUCC draft PR #614](https://github.com/femboy2112/SUCC/pull/614), source head `0faa85a798de5b0b9af4d62295f405165b408eb7`; SUCC Main XXV parent `db9fb4b84672050efa79b13377f1e73364598a14`. No main merge, change to frozen BBP source or imported theorems, external Lean replay, or claimed Millennium-problem solution.

## 0. Truth boundary and why this specific continuation matters

The external [OpenAI October 2026 Yang–Mills source](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464) reports a formalized **existence** construction via a selected Wilson-lattice family, compatible correlations and reconstructed Wightman fields. The [external group review](https://github.com/yang-mills-group/YM/tree/55ba9fc36293b3f4d52c6b1f813169a0be76ee98) assesses the claimed existence theorem but explicitly does **not** establish uniqueness of the infinite-volume limit, confinement or the physical mass gap; [Clay still lists the mass-gap problem as unsolved](https://www.claymath.org/millennium/yang-mills-the-maths-gap/). The external review distinguishes the selected scalar OS bridge from the stronger full-field OS interface and asks for a separate assessment of source definitions. These are not silently imported as local SUCC kernel theorems.

The user hypothesis is that **SUCC's computational graphs are a finite constructive presentation of quantum linear algebra** and that its Haar cylinders and observer/pinbed wavelets should transport to lattice gauge theory. We test this under the strict distinction among three objects:

1. **Carrier coordinates:** a finite graph with oriented link variables and source/weight law.
2. **Quantum Hilbert space:** complex amplitudes on links with normalized Haar inner product and Gauss constraints.
3. **Observer/instrument:** a declared bank of gauge-invariant Wilson words, projections, conditional details, or transfer correlations.

A path count is not an experiment, a graph subdivision is not a physical RG step, positive finite kernels do not give continuum gaps, and a wavelet detail in a gauge-dependent coordinate is not necessarily a physical observable.

### Explicit existing SUCC ancestry (reviewed at Main XXV)

| Existing SUCC module | Actual overlap | What is **not** inherited |
|---|---|---|
| [`haar_successor_junction.py`](../../../observational_succ/haar_successor_junction.py), [`haar_pascal_successor.py`](../../../observational_succ/haar_pascal_successor.py) | Exact finite word-Haar detail `E_(k+1)-E_k`, and signed successor operator; orthogonal conditional decomposition | No source-selected π normality or YM transfer spectral bound |
| [`profinite_hilbert.py`](../../../observational_succ/profinite_hilbert.py), [`institute_atomic_haar.py`](../../../observational_succ/institute_atomic_haar.py) | Normalized-Haar cylinders, isometric finite quotient pullbacks and source-attested Haar pairings | The profinite integers are not gauge-group links; no automatic source-preserving map from \(\widehat{\mathbb Z}\) to compact simple Yang–Mills |
| [`quantum_records.py`](../../../observational_succ/quantum_records.py) | Exact real density matrices and Kraus instruments; measurement records distinct from physical-state reduction | A gauge twirl on density operators is not Gauss-law projection onto singlet vectors |
| [`yoneda.py`](../../../observational_succ/yoneda.py), [`source_path_projector.py`](../../../observational_succ/source_path_projector.py) | Free finite path categories, typed source selection, exact character constraints | Yoneda/path composition alone does not fix amplitudes, Hamiltonian, Wilson action or continuum limits |
| [`interacting_arithmetic_hamiltonian.py`](../../../observational_succ/interacting_arithmetic_hamiltonian.py) | Signed walks are coefficients of powers of a sparse quantum Hamiltonian; graph and matrix presentations agree | Arithmetic adjacency is not the 4D Wilson quantum Hamiltonian; its spectral law does not transfer |
| [`fourier_yoneda_pinbed.py`](../../../observational_succ/fourier_yoneda_pinbed.py) | Fourier bank can separate laws on a **specified** state/observable quotient | Its Haar target is not the interacting gauge-theory vacuum |
| [`holonomy_proof_transport.py`](../../../observational_succ/holonomy_proof_transport.py) and PR #614's [`yang_mills_gauge_oracle.py`](../../../observational_succ/yang_mills_gauge_oracle.py) | Path orientation, gauge quotient, 4D torus flat-holonomy counterexample, finite `S3` loop classes | GF(2) holonomy or finite `S3` is not the field strength of physical compact simple YM |
| [`hilbert_succ.py`](../../../observational_succ/hilbert_succ.py) | Hilbert **space-filling curve** is an efficient geometric scan in other work | The word “Hilbert” does not identify it with a Hilbert **space** proof |

Haar **measure** and Haar **wavelets** are different mathematical structures. The bridge here is the shared conditional-expectation geometry, not an equivalence of all their source objects. The new code imports the pinned `S3` multiplication from PR #614; other ties are independently derived formula-level connections, not untested adapter imports.

## 1. QG-01 — a genuine isometric source/refinement arrow for every finite gauge group

Let `G` be a **finite group**, with counting-normalized Haar law `m_G(g)=1/|G|`, and let the endpoints of an oriented coarse edge have **fixed external gauge frames**. Introduce an internal vertex, replacing one group label `g` by ordered link labels `(a,b)` satisfying `g=ab`. Write

\[
\mathcal H_0=L^2(G,m_G),\quad \mathcal H_1=L^2(G\times G,m_G\otimes m_G),\quad
(Jf)(a,b)=f(ab).
\]

For every (real or complex) `f`,

\[
\|Jf\|_1^2=\frac1{|G|^2}\sum_{a,b}|f(ab)|^2
=\frac1{|G|}\sum_g|f(g)|^2=\|f\|_0^2.
\]

The exact adjoint is

\[
(J^*F)(g)=\frac1{|G|}\sum_{a\in G}F(a,a^{-1}g),\quad
J^*J=I,\quad P=JJ^*=P^*=P^2.
\]

If the new internal gauge is `k`, its operation on functions is

\[
(U_kF)(a,b)=F(ak^{-1},kb).
\]

Changing variables `x=ak^{-1}` gives

\[
\boxed{PF(a,b)=\frac1{|G|}\sum_k(U_kF)(a,b)=J(J^*F)(a,b).}
\]

Thus `im(J)=H_1^{G_mid}` and `ker(J*)` is the **orthogonal complement of the internal-gauge singlets**. Every detail `(I-P)F` is killed by the internal-Gauss projection. The exact decomposition is

\[
\boxed{\|F\|^2=\|PF\|^2+\|(I-P)F\|^2.}
\]

The new coordinate dimension `|G|²` has not added a new **internal-gauge-invariant** dimension beyond `|G|`. With outer-vertex gauge frames *also* imposed, another gauge quotient is required: `|G|` is **not** asserted to be the global physical Hilbert-space dimension of a standalone open edge. This distinction is a mathematical boundary, not cosmetic wording.

**Compact group extension:** for any compact group with normalized Haar probability, Fubini and right invariance prove the same bounded isometric pullback and conditional-expectation identities on the corresponding `L²` spaces. The finite `|G|` dimension and orthogonal vector basis proofs do *not* carry over: delta functions are not `L²` vectors on non-discrete compact groups. SUCC executes only finite `Z_q` and finite nonabelian `S3` controls. This is classical representation/measure theory, newly connected to SUCC's existing finite-source presentation; worldwide novelty is not claimed.

## 2. QG-02 — precisely which Haar details are physical

For a finite alphabet `q>=2`, word depth `k>=0` and joint word distribution `p(w,a)`, let `p(w)=sum_a p(w,a)` and

\[
E_k=q^k\sum_w p(w)^2-1,\quad
E_{k+1}=q^{k+1}\sum_{w,a}p(w,a)^2-1.
\]

An exact expansion of the squares and `sum_a p(w,a)=p(w)` proves

\[
\boxed{E_{k+1}-E_k=q^{k+1}\sum_{w,a}\left(p(w,a)-p(w)/q\right)^2\ge0.}
\]

This is exactly the **conditional Haar detail geometry** of SUCC's existing 16-ary `haar_successor_junction.py` (there `q=16` and past/future orientations are kept distinct). In Hilbert notation the detail is `(I-JJ*)f`, i.e. the orthogonal residual to conditional averaging. This is classical Haar/martingale theory; our receipt matches the conditional expression by independent rational expansion for `q=2,3,16`.

But there are *two radically different interpretations* depending on the source map:

- **Pure subdivision:** `G -> G×G`, `g=ab`. The residual is nonzero as a function of **new link coordinates**, but lies in the *unphysical internal-gauge* complement and disappears after the Gauss constraint.
- **Actual added Wilson cycle:** the gauge-reduced finite abelian quotient grows `G^b -> G^(b+1)`. The new loop-coordinate detail can be gauge invariant; e.g. for `G=Z2`, `D(x,y)=(-1)^y` has zero conditional mean and squared norm 1, while `G^1` has no such independent `y` observable.

The assertion “refinement creates quantum information” is therefore false **without a source/gauge classification**. The repaired assertion is: source-preserving refinement can create **new physical Haar details iff the new quotient observables actually separate more gauge states** (in this finite abelian setting). Arbitrary numerical wavelet energy is not a mass or a photon/gluon count.

## 3. QG-03 — entanglement can arise solely from the computational factorization

Use the standard *counting-orthonormal* link basis `|g>` rather than the normalized-Haar function notation in §1. The correctly normalized isometric subdivision sends

\[
\boxed{|g\rangle\mapsto |\Psi_g\rangle=\frac1{\sqrt{|G|}}\sum_{a\in G}
|a\rangle\otimes|a^{-1}g\rangle.}
\]

Every term has product `g`, so `|Psi_g>` is an internal-gauge singlet. The reduced density is

\[
(\rho_A)_{a,a'}=\frac1{|G|}\sum_b \mathbf 1_{ab=g}\mathbf1_{a'b=g}
=\frac{\delta_{aa'}}{|G|}.
\]

Therefore the link-factorized reduced purity is **exactly** `tr(rho_A²)=1/|G|`, with Schmidt rank `|G|` and entropy `log |G|`. Yet the original coarse `|g>` is pure. The entanglement arises in the **extended-link tensor factorization**, not from a new gauge-invariant degree of freedom. This is a finite version of known gauge edge-mode entanglement. For a continuous compact group a delta `|g>` would be distributional and nonnormalizable; a physical extension requires smearing/representation cutoffs and boundary-algebra choices.

The `quantum_records.py` connection gives a second, independently checkable warning. In a `Z2` subdivision, take the exact normalized odd vector

\[
|\psi_-\rangle=\frac12\sum_{a,b\in\{0,1\}}(-1)^a|a,b\rangle.
\]

The nontrivial internal gauge sends `|psi_->` to its **negative**; its density `rho=|psi_-><psi_-|` is nevertheless unchanged by conjugation. Hence a **gauge-invariant density twirl does not imply** that the state is supported in the Gauss-law singlet subspace: `P|psi_->=0`, while the twirled density remains trace one. This refutes the conflation of a measurement-channel symmetry with physical-state constraint satisfaction.

### Exact kinematic controls

| Gauge group | Coarse dimensions (`G`,`G²`) | Internal-gauge singlets | Pure-gauge detail dimension | Link-factor purity |
|---|---:|---:|---:|---:|
| `Z2` | `(2,4)` | 2 | 2 | 1/2 |
| `Z3` | `(3,9)` | 3 | 6 | 1/3 |
| `S3` | `(6,36)` | 6 | 30 | 1/6 |

For `S3` the **different** two-loop space `G²/Ad(G)` has **11 simultaneous-conjugacy orbits**, as in PR #614; we checked Burnside's formula and exhaustive orbit enumeration. Separate Wilson trace marginals lose information that joint mixed words retain. The internal-gauge `G×G->G` quotient and the two-loop `G²/Ad(G)` quotient must never be conflated.

## 4. QG-04 — computational paths are exactly the finite linear-algebra amplitudes

Choose an orthonormal computational basis indexed by graph states `x`. For **any** finite linear operator `K` with matrix entries `K_(y,x)` and `n>=0`, repeated multiplication gives

\[
\boxed{\langle u,K^n v\rangle
=\sum_{x_0,\ldots,x_n}\overline{u(x_n)}v(x_0)
\prod_{j=1}^n K_{x_j,x_{j-1}}.}
\]

This identity is the promised rigorous mathematical sense in which a weighted **computation graph is a constructive basis dual** to ordinary finite quantum linear algebra. It is not a new quantum postulate or proof of computational advantage. **Signed and complex amplitudes must not be replaced with counts or positive probabilities.** A hostile `2×2` signed matrix has two nonzero paths whose amplitudes cancel exactly; its absolute path count would incorrectly report two.

To connect this with gauge interactions, construct a **single finite square plaquette** with four `Z2` links `x in {0,1}^4`. Each vertex gauge generator flips its two incident edges, so the physical quotient has two parity/Wilson classes, each containing eight configurations. Define

\[
(H\psi)(x)=\sum_{e=0}^{3}\bigl(\psi(x)-\psi(x\oplus2^e)\bigr)
+\lambda\left[1-(-1)^{\mathrm{parity}(x)}\right]\psi(x),\quad\lambda\ge0.
\]

This is a standard **finite Z2 Kogut–Susskind-style electric + magnetic** toy Hamiltonian. It commutes with every vertex star (proved by bit-flip commutation), is positive from the sum-of-squares electric and nonnegative magnetic terms, and descends to the two normalized gauge-invariant parity states. Exact graph-transition counts give

\[
\boxed{H_{\rm inv}=\begin{pmatrix}4&-4\\-4&4+2\lambda\end{pmatrix}},\qquad
\lambda_\pm=4+\lambda\pm\sqrt{\lambda^2+16}.
\]

For `lambda=1`, the matrix is `[[4,-4],[-4,6]]`, its determinant is 8 and the finite splitting is `2 sqrt(17)`. The reduction was calculated from all 16 graph states, **not fitted to the spectral formula**. This is not a four-dimensional nonabelian or continuum mass-gap result; the physical lattice spacing has not been sent to zero.

Take `K=I-H_inv/16` at `lambda=1`:

\[
K=\begin{pmatrix}3/4&1/4\\1/4&5/8\end{pmatrix}>0.
\]

For finite test vectors `f_i` and integer times `t_i>=0`,

\[
R_{ij}=\langle f_i,K^{t_i+t_j}f_j\rangle
=\langle K^{t_i}f_i,K^{t_j}f_j\rangle.
\]

Thus the **finite reflection-style matrix is a Gram matrix** and is PSD by exact square completion. This recreates a *small algebraic shadow* of the Osterwalder–Schrader reconstruction mechanism, but it supplies neither the actual four-dimensional Euclidean Schwinger functions nor OS support, locality, all arities, growth, or Wightman construction. That full theory is handled by the external checked construction, not by our toy model.

## 5. QG-05 — why product Haar transport is not Wilson-source RG transport

The normalized Haar reference on independent links pushes forward under `(a,b)->ab` to Haar. The **interacting Wilson law** is instead weighted by plaquette action and coupled to scale.

An exact, deliberately small countermodel uses two independent `Z2` plaquette-sign variables, each with weights `(w+,w-)=(3,1)`, hence probability `(3/4,1/4)`, and coarse plaquette sign defined as the *product* of fine signs. The fine pushforward probabilities are

\[
\left(\left(\frac34\right)^2+\left(\frac14\right)^2,\;2\frac34\frac14\right)
=\left(\frac58,\frac38\right).
\]

The untouched coarse `(3/4,1/4)` law differs by total variation **1/8**; its Wilson mean is **1/2**, whereas the fine product mean is **1/4**. For Haar weights `(1,1)` both laws agree. This is an exact source-transport defect under a coarse observable—not a literal Wilson block-spin formula for a four-dimensional compact-simple-group action. It establishes why simply reusing a bare action parameter at every refinement is *not* justified by Haar isometry.

The single-plaquette factor graph has `16` link states, `8` states in each gauge orbit, exact Haar-normalized partition `Z=(w++w-)/2=2` and exact Wilson expectation `(w+-w-)/(w++w-)=1/2`. This links the discrete quantum computation graph to the Euclidean statistical law while keeping the Hilbert kinematics and statistical source **separate**.

## 6. QG-06 — a viable wavelet/Schur attack on the genuine mass-gap *estimate*

The target requires a **quantitative physical-scale inequality on the authentic source**, not a statement that every finite matrix has a gap. Let `a` be physical lattice spacing, `T_a` a genuine source-derived positive self-adjoint contraction on a gauge-invariant Hilbert space with normalized vacuum `Omega_a`, `T_a Omega_a=Omega_a`. A sufficient *conditional* gap target is

\[
\boxed{\forall a\in(0,a_0),\ \forall f\perp\Omega_a,\qquad
\langle f,(I-T_a)f\rangle\ge m_0 a\,\|f\|^2,\quad m_0>0.}
\]

Indeed the spectral theorem puts `spec(T_a|Omega_a^perp) <= 1-m_0 a`, and, for `0<m_0 a<1`, the physical inverse correlation scale `-log(1-m_0a)/a>=m_0`. To conclude a continuum Yang–Mills spectral mass gap one must additionally establish that the actual OS/Wightman reconstruction carries these operators, physical-unit normalizations and bounds into the selected continuum theory **without introducing new gapless states**. This is deliberately not an asserted theorem about OpenAI's continuum witness.

SUCC's finite Haar/Schur machinery offers a concrete candidate **proof instrument**: after Gauss reduction, decompose a source-derived physical test space into orthogonal multiscale Haar/Peter–Weyl blocks `W_j` and estimate the full signed block form of `I-T_a`. A sufficient finite block dominance condition is

\[
\langle w_j,L_{jj}w_j\rangle\ge\left(m_0 a+\sum_{i\ne j}b_{ij}\right)\|w_j\|^2,\quad
\|L_{ij}\|\le b_{ij}=b_{ji},\quad L=I-T_a.
\]

Then Cauchy–Schwarz and `2xy<=x²+y²` prove `\langle w,Lw\rangle >= m_0 a\|w\|²` for all physical `w`. Every sign and cross-block term matters. A coarse **positive** Gram is not itself a strict lower bound on the physical orthogonal complement. Gauge-variant Haar blocks must be removed **before** claiming an improvement.

The finite two-state Haar-wavelet control makes the scaling issue concrete: the stochastic transfer `T=[[1-eps,eps],[eps,1-eps]]` has vacuum `1` and the mean-zero Haar wavelet `(1,-1)` with Rayleigh energy `2eps`. For `eps=a/4`, its normalized physical margin is `2eps/a=1/2` at every tested rational spacing. For `eps=a²`, the normalized margin is `2a->0` even though the finite transfer has positive spectral splitting at every cutoff. The law is a control, **not the Yang–Mills Wilson source**.

### What would be genuinely new for SUCC and possibly useful to physics

The hard new lemma would not be “Haar wavelets generate Hilbert space”; that is classical. It would be an **authenticated bound on physically gauge-invariant, Wilson-source-selected block interactions** with a positive margin uniform in the correct physical units and stable under the particular UV/IR extraction used in the externally checked hierarchy. The existing SUCC state/observer machinery could then be used to express, check, and possibly *discover* such a bound. A finite fitted ansatz, a formally commuting categorical diagram, or an unrelated arithmetic wavelet energy is not enough.

## 7. Steelman → crucible → verdict

| Proposed frame | Strongest legitimate result | Countermodel or test | Verdict |
|---|---|---|---|
| Computational graph is a finite dual of quantum linear algebra | Path amplitude expansion of `K^n` is exactly a sum over computational histories | Sign-canceling two-path test | **PROVED LOCAL; no speedup** |
| Haar wavelets diagnose physical refinements | Gauge-reduced conditional details represent new quotient observables if the quotient genuinely grows | Pure subdivision creates only internal-gauge detail | **PROVED LOCAL with source typing** |
| Quantum entanglement represents carrier geometry | Extended-link factorization admits entanglement after subdivision, even for one pure coarse link | Exact edge-mode purity `1/|G|`; no new invariant label | **REFUTES unrestricted inference** |
| Gauge-invariant density is a physical state | Only if its support is in the Gauss-law singlet sector | Odd `Z2` rank-one density survives twirl but not Gauss projection | **REFUTED in general** |
| Positive reflection Gram implies YM gap | Requires physical-scale uniform coercivity and stable continuum reconstruction | `eps=a²` versus `eps=a/4` | **REFUTED in general** |
| YM theorem implies physical gap | External October/review exclude such a claim | Group's combined checks scope and Clay status | **OPEN / no bridge** |

## 8. Reproducibility and next verdict-changing probe

Exact local test bundle (only PR #614 `yang_mills_gauge_oracle.py` and this new file, not a full SUCC clone):

```sh
python -m unittest discover -s tests -p 'test_ym_quantum_graph_duality.py' -v
python scripts/ym_quantum_graph_duality_probe.py
```

The source-compatible local baseline also replays the **19 inherited PR #614 finite tests**; see `FOCUSED_TEST_LOG.txt` for the 44/44 aggregate. An **independently decomposed, import-free** exact audit (`scripts/ym_quantum_graph_independent_audit.py`) reconstructs the 16×16-to-2×2 graph projection, S3 simultaneous-conjugation count, Z3 gauge projection, Haar conditional energy, interacting Wilson-law defect, and the gauge-odd density countermodel; its output is `INDEPENDENT_RECEIPT.json`. This is method/code triangulation, not an external mathematician or a new Lean check. All `Fraction` results are deterministic; no floating-point finite claim is given proof authority. The external Lean 4.32.0 / Mathlib / Comparator replay (documented at [YM review rerun](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/rerun.md), requiring substantial resources) was not run here. Neither were the SUCC full-suite, provenance, observer foundations and ordinal probes from `AGENTS.md`; they require a full checkout and must be checked on the **exact published head**. Inherited full-suite CI from PR #614 is not automatically CI for this child branch.

**Next discriminate rather than decorate:** build *source-realized* small-volume Wilson Schwinger two-point functions on genuine 4D lattice plaquettes (initially finite `Zq`, then an explicit compact-group representation truncation), select an actual reflection plane and time-positive test basis, construct Gauss-projected Haar/Peter–Weyl multiresolution blocks, check exact/sound interval reflection Gram and finite physical-scale Poincaré margins; compare with a massless transfer control and a Wilson-weight-mutated but Haar-identical control. Only then attempt to transport a proved uniform inequality into the pinned continuum witness, preserving its action, selected phase, normalization and order of limits.

**Claim boundary:** All new results here are finite classical algebra, source-relative diagnostics, or *conditional* criteria. We do not reproduce or extend the external four-dimensional existence proof. We do not prove uniqueness, confinement, a Yang–Mills mass gap, π normality, Goldbach, Collatz, or RH. We do not claim global scholarly priority for classical finite-group quantum mechanics, the Haar martingale, or gauge edge-mode entanglement.
