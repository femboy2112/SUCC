# D30 — Nonlinear evolution through an observational quotient

## 1. Original question

When does a finite observer's projection determine its next velocity report?
The faithful SUCC proposal is a source-relative commuting evolution square:
the observer need not reconstruct every carrier mode, but the retained report
must determine its own derivative. This asks for exact autonomous closure,
with every admissible source quantified. Approximate, statistical, and
history-dependent closures are distinct questions.

Worktree: `research/swm-d30-2026-10-13`, immutable parent
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. Only new D30 files are added.

## 2. Existing mathematical context

The existing F1 observation-fiber theorem and DF source-update theorem already
identify the static and linear factorization conditions. Their native dossiers
are `FIELD_RELATIVE_CLOSURE_AND_OBSTRUCTION_CALCULUS.md` and
`DYNAMIC_FOURIER_VIRTUAL_ZERO_FRONTIER.md` dated 2026-10-12.

[Germano's original filtering paper](https://www.ams.jhu.edu/~eyink/Turbulence/classics/Germano92.pdf)
(1992, pp. 326–329, equations 15, 21, 24) states derivative-commutation
hypotheses and generalized stresses for filtered incompressible equations.
Its warning about Reynolds averaging rules applies directly to retaining
resolved–hidden products here. [Tao's own local-theory notes](https://terrytao.wordpress.com/2018/09/16/254a-notes-1-local-well-posedness-of-the-navier-stokes-equations/)
(2018, Leray-system section) supply the periodic pressure-elimination context.
Both were accessed 2026-10-13. These are classical ingredients; academic
novelty is unclaimed.

The import manifest names FuckingRH source commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`. Inspection in the local originating
repository confirmed that its foundations dossier and the frozen archival
copy both have Git blob `04408ed96bd369b5063868eb5ad5664824d18043`.
The exact source's observer/carrier interpretation remains separate from
this mathematical model. No imported path or archive is modified.

## 3. Proposed SUCC objects

Let (E) be a finite-dimensional real normed source space, (P:E\to E)
a linear projection, (V=\operatorname{im}P), and (H=\ker P). The source
report is (O(u)=Pu); its derivative target is (T(u)=PF(u)).
Source pairs in one fiber differ by (h\in H).

For the PDE instance use (\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2), real,
divergence-free smooth vector fields, Fourier convention (e^{ik\cdot x}),
and (P_N) retaining (|k|_\infty\le N) componentwise. Let (\mathbb L_k=
I-kk^T/|k|^2) for (k\ne0), and (\mathbb L_0=I). The zero mode is treated
explicitly, without evaluating the inverse-Laplacian pole. All these Fourier
multipliers commute with spatial derivatives. Normalize

\[
\|u\|_2^2=(2\pi)^{-2}\int_{\mathbb T^2}|u|^2
=\sum_k|\widehat u_k|^2.
\]

## 4. Candidate theorem

**C1 — CLASSICAL, with local derivation.** For any specified source set (D)
and (F:D\to E), a unique map (G:P(D)\to V) satisfying (PF=G\circ P)
exists iff

\[
\forall u,z\in D:\quad Pu=Pz\Longrightarrow PF(u)=PF(z).
\tag{1}
\]

**C2 — PROVED LOCAL; independent acceptance pending.** Suppose (D=E) and

\[
F(u)=Au+B(u,u)+f,
\]

with linear (A), bilinear (B), and constant (f). Equation (1) holds iff
all three conditions hold:

\[
PAh=0,\qquad P[B(v,h)+B(h,v)]=0,\qquad PB(h,h)=0
\tag{2}
\]

for every (v\in V,h\in H). The exact defect relative to the resolved
representative is

\[
\delta(v,h)=PF(v+h)-PF(v)
=PAh+P[B(v,h)+B(h,v)+B(h,h)].
\tag{3}
\]

Writing (b=\|B\|), (p=\|P\|), its norm is at most

\[
\|PA|_H\|\,\|h\|+pb(2\|v\|\|h\|+\|h\|^2).
\tag{4}
\]

Every finite Fourier Galerkin space (E_M) of such fields satisfies these
finite-dimensional hypotheses for (A=\nu\Delta), (\nu>0), and

\[
B(a,b)=-P_M\mathbb L((a\cdot\nabla)b).
\]

No infinite-dimensional bounded-bilinear claim is implicit in (4).

For a smooth incompressible solution, write (u=v+h). Under the stated
commuting-filter hypotheses, the exact discrepancy from the resolved
Galerkin derivative is

\[
-P_N\mathbb L\operatorname{div}
(v\otimes h+h\otimes v+h\otimes h).
\tag{4a}
\]

The familiar stress (\tau=P_N(u\otimes u)-v\otimes v) also contains
the resolved term (P_N(v\otimes v)-v\otimes v). Products of retained modes
need not themselves be retained. Thus a proposed resolved equation must
specify whether its nonlinearity includes the final projection; otherwise
different definitions of “defect” are being compared. A noncommuting filter
adds linear commutators such as (\nu(P\Delta-\Delta P)u), independently
of hidden stress. Projection identity, derivative commutation, and fiber
constancy are three separately checked requirements.

## 5. Proof attempt

For C1 define (G(Pu)=PF(u)); fiber constancy is precisely well-definedness,
and its converse follows by substitution. For C2 apply constancy to

\[
PF(v+th)-PF(v)=t\{PAh+P[B(v,h)+B(h,v)]\}+t^2PB(h,h)
\]

for all real (t). Both polynomial coefficients vanish. Taking (v=0)
separates (PAh); the remaining coefficient gives the cross condition.
Conversely every source is (v+h), and (2) kills (3). The triangle inequality
gives (4). Thus (G(v)=PF(v)) is polynomial. By classical local uniqueness
for finite-dimensional polynomial ODEs, on their common existence interval

\[
P\Phi_t(u)=\Psi_t(Pu).
\tag{5}
\]

This flow assertion uses local existence and uniqueness, not global PDE
regularity. For smooth PDE solutions only the instantaneous filtering identity
is asserted here.

## 6. Crucible

Set (N=1), (M\ge2), (f=0), and

\[
w=(0,1)\cos(2x)+(1,2)\cos(-2x+y).
\]

Each amplitude is perpendicular to its frequency. Therefore (\nabla\cdot w=0)
and (P_1w=0). Direct multiplication gives

\[
P_1(w\otimes w)=
\begin{pmatrix}1/2&1\\1&5/2\end{pmatrix}
+\begin{pmatrix}0&1/2\\1/2&2\end{pmatrix}\cos y.
\]

Consequently

\[
P_1\mathbb L\operatorname{div}(w\otimes w)
=-\tfrac12(1,0)\sin y,\qquad\|\cdot\|_2^2=1/8.
\tag{6}
\]

Viscosity projects to zero, so (0,w) have identical reports but derivatives
(0,\tfrac12(1,0)\sin y). Universal low-mode autonomous closure is **REFUTED**.
The retained simpler control (a=(0,1)\cos2x) has nonzero constant projected
stress (\operatorname{diag}(0,1/2)), whose divergence vanishes: stress alone
would be an insufficient receipt.

For (v=(0,1)\cos x), (h=(1,2)\cos(-2x+y)), the complete four-configuration
contrast (PF(v+h)-PF(v)-PF(h)+PF(0)) is
((1,1)\sin(-x+y)), norm squared (1). The hidden-only stress vanishes;
omitting Reynolds cross terms fails. This exact factorial contrast shows
non-additivity, with the bilinear derivation identifying its source.

An orthogonal filter (Q) onto constants and (\cos x+\cos2x) violates
derivative commutation. On (g=\cos x),

\[
(Q\Delta-\Delta Q)g=\tfrac32\cos2x,\quad\|\cdot\|_2^2=9/8.
\]

The probe rejects compressible/nonreal inputs and catches omitted Leray,
swapped derivatives, and omitted cross terms. A fresh frequency pair
((3,0),(-3,1)) with amplitudes ((0,1),(1,3)) reproduces (6).

## 7. Verdict

**SURVIVES:** exact fiber criterion and quadratic specialization, with written
proof and **TESTED MODEL** rational receipts. **FAILS:** unconditional nonlinear
low-mode closure, by (6). The proof and probe share one investigator and
are not independent witnesses. (\kappa): direct declared-source algebra;
(\phi): exact executable checks plus derivation; (\sigma): verified bytes,
unattested physical carrier; (\rho): controlled by preserved countermodels.
No result identifies an actual instrument or turbulent physical source.

## 8. Remaining obstruction

The smallest unresolved step is independent checking of C2 and the signed
Fourier witness. Next falsifier: independently expand the two cross products
and Leray multiplier at (k=(0,1)). A useful repair must restrict admissible
fibers or add state/history; finite training agreement cannot replace (1).

## 9. Cross-domain connection with actual maps

The actual maps are (u\mapsto Pu), (u\mapsto\Phi_tu), and
(v\mapsto\Psi_tv), with (5) as coherence law. The existing vacuum transverse
Maxwell model has linear (A=-S\partial_x), (S(E,B)=(B,E)), hence
(PA=AP) for a spectral filter and satisfies (2). Its vacuum, source-free,
(c=1) assumptions remain explicit. Lorentz transport uses invertible
coordinate/field intertwiners; lossy PDE quotient closure requires fiber
constancy instead. Neither map supplies Gamma/pole completion, Weil
positivity, physical ontology, or RH.

## 10. Deliverables

`D30_PDE_CLOSURE_PROBE.py` uses bounded finite support and Gaussian-rational
coefficients. `D30_PDE_CLOSURE_RECEIPT.json` records exact coefficients,
controls, source hashes, interpreter, and parent. The probe command is
`python research/2026-10-13/SWARM_ATLAS/D30_PDE_CLOSURE_PROBE.py > research/2026-10-13/SWARM_ATLAS/D30_PDE_CLOSURE_RECEIPT.json`;
exit **0**. Full suites, compilers, shared metadata, and imported/runtime
paths were outside this investigator's authorized scope.
