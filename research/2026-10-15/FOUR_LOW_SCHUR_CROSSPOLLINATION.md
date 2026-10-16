# Operation Proof Teeth — Swarm D: authentic four-low residual shorting

Date: 2026-10-15. Worktree: `SUCC-proof-teeth`, branch
`research/succ-yean-proof-teeth-ultra-2026-10-15`, base
`0f86ba2478a72bf90cf33a4ee192cb2265d992dd`. No commit/push by this worker.
**Original zero-shift Schur sign: OPEN. RH PROVED: NO.**

The new contribution is an explicit compressed-Neumann quotient residual,
the cross/resolvent parity theorem including its zero-shift hypotheses, and
rigorous obstructions to particular authentic-source trial certificates.
Parity of the low block alone, the four-moment high bound, the original
trial-residual inequality, and existence of a rank-four positive correction
are inherited. This note does not claim priority for the functional analysis.

## 1. Source and domain, with coordinates fixed

All operators below concern the **unmodified signed** completed Suzuki/Weil
source at `a=1/2`. The existing pinned adapter is
`observational_succ/source_weil_hierarchy.py`, Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, independently found at originating
SUCC commit `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc` (PR85). The adapter
`suzuki_legendre_source.py` supplies the existing exact polynomial pair and
source interval integrations. The six assigned modules and WB4 dossier were
read before introducing the new adapter.

The founding import manifest has a different role: its 72 artifacts originate
at FuckingRH commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`. None of the six
assigned modules is an entry in that manifest. That historical commit object
is not in this checkout; `verify_provenance.py` verifies the manifest's actual
local blob records. The PR85 source commit/blob *is* locally accessible. We
do not conflate those chains. The receipt records all relevant SHA256s,
commands, the branch/head, and absence of source drift during the probe.

For `0<r<=1`, the full derivative used in the numerical route is

\[
 g'(r)=-4\sinh(r/2)+C_\infty/2+
 (\log2)/\sqrt2\,1_{r>\log2}
 -\operatorname{atanh}(e^{-r/2})-\arctan(e^{-r/2}).                 \tag{D1}
\]

Here `g` is even, `g(0)=0`, and `g'` is odd. The one real Gamma tower,
both signed pole channels, the original contact and the true prime-2 hinge
are retained. The derivative's logarithmic singularity is integrable.
No nontrivial zero coordinates, zero oracle, substitute covariance or
synthetic signed matrix is used to construct this source. The continuum
operator convention is the mean-zero compression of convolution by `g`.
The source reference is [Suzuki, v3, §§1 and 8](https://arxiv.org/html/2606.09096v3),
checked against the local source formula; numerical data here are source
integrals, not values read from that paper's spectral discussion.

Let

\[
 I=(-1/2,1/2),\quad H=L^2_0(I;\mathbb C),\quad
 (Vu)(t)=\int_{-1/2}^t u(s)\,ds,\quad K=V^*V.
\]

Let `P` project onto `l_j(t)=P_j(2t)`, `j=1,2,3,4`, and `Q=1-P` on `H`.
**Unnormalized** coordinates have Gram
`W=diag(1/3,1/5,1/7,1/9)`. Write
`e_j=sqrt(2j+1) l_j` for the **orthonormal** coordinates. If
`M_ij=<l_i,G l_j>`, then the orthonormal matrix is
`W^(-1/2) M W^(-1/2)`; `M` itself is a form matrix, not an operator matrix
for the Euclidean coordinate inner product. All numerical solves use the
orthonormal coordinates. All rational obstruction witnesses use the
unnormalized polynomials and explicitly insert `1/(2j+1)` in squared norms.

Set `A=PGP`, `B=PGQ`, `D=QGQ`, `K_Q=QKQ|QH`. The inherited WB4 analytic
theorem gives `D >= k K_Q`, with `k=1/50`, and in fact with
`k_*=20699/1000000`. Extension from smooth compact four-moment-null tests
to `VQH` requires density in `H_0^1` with the same four moments and continuity
of `<u,Gu>` in `u=f'`. Both hold: smooth approximation followed by four
fixed smooth moment corrections gives that density, and `G` is bounded.
No `k I` gap is asserted. `K_Q` and `D` are positive injective compact
operators; a bounded inverse of `D` at zero is neither assumed nor used.

## 2. Cross-block and resolvent parity, including the limit

**D-PARITY, PROVED conditional on the stated source/domain hypotheses.**
Let `J u(t)=u(-t)`. Evenness of `g` and symmetry of `I` imply `JG=GJ`;
mean-zero compression also commutes with `J`. Each low Legendre line is a
reflection eigenspace, hence `JP=PJ`, `JQ=QJ`. With `J_P,J_Q` denoting
the restrictions,

\[
 J_P B=B J_Q,\qquad J_Q B^*=B^* J_P,\qquad J_QD=DJ_Q.           \tag{D2}
\]

For every `lambda>0`, positivity of `D` gives a bounded
`(D+lambda I_Q)^(-1)` commuting with `J_Q`. Therefore

\[
 R_\lambda=B(D+\lambda I_Q)^{-1}B^*,\qquad
 J_P R_\lambda=R_\lambda J_P.                                  \tag{D3}
\]

This is the cross/resolvent conclusion beyond the previously known parity
of `A`. To pass to zero one must establish a finite response, not just
reflection symmetry. The following equivalent conditions do so:

1. `sup_(lambda>0) ||R_lambda|| < infinity`;
2. `Ran B*` is contained in `Ran D^(1/2)`;
3. the reduced map `T=D^(-1/2)B* : PH -> QH` is bounded.

These are the bounded factorization/range conditions of
[Douglas, Theorem 1](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf),
or follow directly from the spectral theorem and finite dimensionality of
`PH`. The source verifies them below. Spectral monotone convergence then
gives `R_lambda -> R_0=T*T` entrywise and **in norm on PH**. Passing D3 to
that norm limit yields a `2x2 odd + 2x2 even` split of `R_0` and `S_0=A-R_0`.
If one means the Schur complement of `G+lambda I_H`, its low block is
`A+lambda I_P-R_lambda`; this has the same zero limit.

No uniform norm limit for the infinite-dimensional high resolvent is claimed.
If the range condition fails, the parity sectors can each have divergent
responses; symmetry alone does not define a finite four-by-four `S_0`.

## 3. The exact compressed-K residual norm and completed square

Put `M={f in L2(I): <f,t^j>=0, j=0..3}` and let `Pi_M` be its orthogonal
projection. Integration by parts against `P_1',...,P_4'` gives

\[
 VQH=H_0^1(I)\cap M,\qquad \overline{VQH}^{L^2}=M.             \tag{D4}
\]

The second equality follows by smooth compact approximation and the four
moment corrections described above. This density is necessary; merely
observing four sampled moments would not justify the following equality.

**D-QUOTIENT, PROVED.** For every `F in H1(I)` and `r=QF` (constant
parts removed before projecting onto `H`),

\[
 \boxed{\|K_Q^{-1/2}r\|^2
  =\sup_{h\in QH}\{2\Re\langle r,h\rangle-\|Vh\|^2\}
  =\|\Pi_M F'\|^2.}                                          \tag{D5}
\]

Indeed `<r,h>=<F,h>=-<F',Vh>`. Replace `Vh` by its dense range in `M`
and complete the elementary square in `L2(M)`. The supremum is finite,
which proves `r in Ran K_Q^(1/2)` as well as the equality. This is an
unbounded **inverse square root on its domain**, not an inverse compact
operator applied to arbitrary `L2` vectors. Changing `F` by any low
polynomial or a constant leaves the right hand side unchanged, because
its derivative changes by a degree-at-most-three polynomial.

Let `U:PH -> QH` be any bounded finite-column trial. Since the original
`g'` is in `L1(-1,1)`, convolution and its weak derivative map `L2` into
`H1` on `I`; subtracting a mean changes no derivative. Thus
`F_x=G(x-Ux)` satisfies D5. The residual is

\[
 r_U=B^*-DU=QG(P-U),\quad
 C_U^{\rm quot}[x,y]=\langle\Pi_M F_x',\Pi_M F_y'\rangle.       \tag{D6}
\]

Consequently `r_U=K_Q^(1/2)E_K`, with `E_K*E_K=C_U^quot`. The form
inequality `D>=k K_Q` factors `K_Q^(1/2)` through `D^(1/2)` with norm
at most `1/sqrt(k)`. Hence `r_U in Ran D^(1/2)` and
`||D^(-1/2) r_U x||^2 <= C_U^quot[x,x]/k`. For `U=0` this proves the
range conditions needed in §2. No attainment of `DU=B*` in `QH` is required.

Now let `T=D^(-1/2)B*`, so `R_0=T*T`. Expanding the bounded finite-column
Gram gives the **exact completed square**

\[
 \begin{aligned}
 L_U&=BU+U^*B^*-U^*DU,\\
 R_0-L_U&=(T-D^{1/2}U)^*(T-D^{1/2}U)\\
        &=(D^{-1/2}r_U)^*(D^{-1/2}r_U),\\
 \boxed{A-L_U-k^{-1}C_U^{\rm quot}\preceq S_0\preceq A-L_U.}  \tag{D7}
 \end{aligned}
\]

Equivalently one can translate the variational supremum for `R_0` by
`Ux`; D5 controls the remaining linear functional. These are two
derivations of the same mathematical identity, not independent source data.
`L_U` need not itself be PSD for an arbitrary trial. If `U` respects
reflection, D6 and D7 inherit the two parity blocks (differentiation swaps
the parity of functions, but preserves orthogonality between the sectors).

## 4. What is wrong with treating A-L_U-50 C_U as a sign oracle

The original bound is **valid** when `C_U` is the full continuum Gram of
`(G(x-Ux))'`, or the appropriate larger projected derivative Gram. It is
a sufficient condition, not an identity or a necessary positivity test.
It requires the signed source, `U(PH) subset QH`, the whole-high coercivity
theorem, the range/domain conditions, all matrix cross terms, and rigorous
errors in `A,L_U,C_U`. A positive sampled matrix is insufficient; a negative
*lower* bound is not a negative direction for `G`.

The new exact quotient supplies a sharper correction. For orthonormal
`p_k=sqrt(2k+1)P_k(2t)`, `k=0..3`, define
`H_ki=<p_k,F_i'>`. Then

\[
 C_U^{\rm quot}=C_U^{\rm raw}-H^*H\preceq C_U^{\rm raw}.       \tag{D8}
\]

It also lies below the Gram of `(QF_i)'`. The two larger raw/projected
Grams need not be ordered relative to each other. Raw derivative energy
can persist even when the true residual `QF` vanishes: a nonconstant low
polynomial has zero quotient energy but positive derivative energy.
This is precisely the removable low-coordinate contribution, not a
license to discard source Gamma, contact, prime or poles.

Finite compression is another possible false shortcut:
`r_N*K_N^(-1)r_N` is a restricted supremum, generally a **lower** bound
on the full dual energy. It cannot serve as the upper `C_U` in D7 without
a proved tail bound. Conversely, it is useful for the certified obstruction
below. Nor does positivity of the omitted Gamma operator alone control
a differentiated residual: that requires a separate derivative-tail bound.

## 5. Actual rational source obstruction, including nonzero Galerkin trials

For a fixed rational polynomial `v=x-Ux` and nonzero rational `q in QH`,
D5 implies

\[
 C_U^{\rm quot}[x,x]\ge
 \frac{|\langle q,Gv\rangle|^2}{\langle q,Kq\rangle},\qquad
 (A-L_U)[x,x]=\langle v,Gv\rangle.                            \tag{D9}
\]

Existing source intervals compute the **complete signed** `G_J` polynomial
pairings. Its omitted Gamma tail satisfies the already-derived bound

\[
 0\preceq G-G_J\preceq\tau_J I_H,\quad
 \tau_J=\frac2{(4J+1)^2}+\frac{16}{(4J+1)^3}.                  \tag{D10}
\]

For `J=64`, enclose `<q,Gv>` by the interval for `<q,G_Jv>` plus/minus
`tau_J ||q|| ||v||`; the square-root upper is calculated with integer
arithmetic and directed rational rounding. Upper-bound `<v,Gv>` by
the upper interval endpoint plus `tau_J ||v||^2`. `K(q,q)` is the exact
existing primitive polynomial integral. Let `c` be the resulting lower
bound for the absolute cross pairing. Then

\[
 (A-L_U-50 C_U^{\rm quot})[x,x]
 \le (\langle v,G_Jv\rangle)_{\rm upper}
       +\tau_J\|v\|^2-50c^2/K(q,q).                         \tag{D11}
\]

Every operation in this certificate is rational with outward source
enclosures. Selection of `v,q` may be numerical, but the strict sign of
D11 is independently established by the exact bound for those frozen
polynomials. Finite tests are not the proof of D9–D11.

For `U=0`, the following **rigorous upper endpoints**, displayed rounded
for readability, are strictly negative. Their exact fractions are in the
receipt and the signs use those fractions:

| Low x (unnormalized) | High q | Upper endpoint for sufficient lower form |
|---|---|---:|
| `P1` | `P5` | `-0.002044062252770131` |
| `P2` | `P6` | `-0.006327058077283824` |
| `P3` | `P5` | `-0.000220610767402126` |
| `P4` | `P6` | `-0.004177418834903891` |

More decisively, a real-source degree-8 Galerkin trial was computed in
orthonormal coordinates and frozen in rational unnormalized coordinates.
The columns `v=x-Ux` and their higher witnesses give:

| x | v minus x | q | D11 upper endpoint |
|---|---|---|---:|
| `P1` | `(913417/2500000)P5-(9183071/125000000)P7` | `P9` | `-0.000796043677999481` |
| `P2` | `(771842481/10^9)P6+(198849247/10^9)P8` | `P10` | `-0.000084854421331419` |
| `P3` | `-(29894707/200000000)P5-(31551819/10^9)P7` | `P9` | `-0.000455114611666258` |
| `P4` | `(613869937/10^9)P6+(470749/8000000)P8` | `P10` | `-0.000222571892486908` |

**D-OBSTRUCTION, PROVED LOCAL:** neither the zero trial nor this specific
frozen nonzero degree-8 trial can satisfy the proposed sufficient matrix
criterion; this holds even with the improved quotient correction. Since
`C_raw >= C_quot`, the same obstruction applies to the raw derivative
criterion. This does **not** refute better trials, positivity of `S_0`,
local Weil positivity, or RH. It is a source-specific method obstruction,
not a changing-source compact diagonal toy.

## 6. Numerical trial response candidates and their limits

The full source matrix has a second construction, distinct from the finite
Gamma interval integrals. The existing exact pair polynomial
`rho_ij(r)=integral[P_i(y+r)P_j(y)+P_j(y+r)P_i(y)]dy` gives
`M_ij=integral_0^1 g(r)rho_ij(r)dr`. With `R_ij'=rho_ij` and
`R_ij(1)=0`, `g(0)=0` implies
`M_ij=-integral_0^1 g'(r)R_ij(r)dr`. This is integrated at 60 decimal
digits, retaining D1. A 12-mode replay at 80 digits differed by at most
`4.845e-56`, an internal quadrature/precision check, **not** a rigorous
source error estimate (the input contact interval is still finite width).

Independently, SciPy integrates `g'(x-y)P_j(2y)` directly in `y`, splitting
at the diagonal and true prime2 thresholds. Outer Gauss–Legendre panels
split at `0` and `±(log2-1/2)`. The 24-node-per-panel fit grid is followed
by a 48-node-per-panel evaluation of **frozen** trials; least-squares
responses are not refit on the latter. This second construction recovers
matrix pairings through `-integral (VP_i)(GP_j)'`. Its largest matrix
discrepancy at degree 20 is `3.517e-11`. Both methods share D1 and its
source constants; they are different implementations of one provenance
family, not two independent arithmetic sources.

All numbers in this table are **FINITE NUMERICAL ONLY**, using normalized
low coordinates. `N` means trial polynomials through degree N; the low
carrier stays four-dimensional. `A-L_U` is a continuum trial upper short
evaluated numerically, not the exact zero-shift Schur matrix.

| N | Trial | min eig(A-L_U) | min eig(A-L_U-50 Cquot) |
|---:|---|---:|---:|
| 4 | zero | `3.12739e-5` | `-0.121618` |
| 6 | Galerkin | `3.69560e-7` | `-0.0492008` |
| 8 | Galerkin | `2.39645e-7` | `-0.0497634` |
| 12 | Galerkin | `7.86174e-8` | `-0.0271492` |
| 20 | Galerkin | `7.29550e-8` | `-0.0162321` |
| 20 | quotient least squares | `7.46305e-8` | `-0.0155231` |

At N=20 Galerkin, raw residual Gram trace is `0.00091773347` and quotient
trace is `0.00044198327`, a factor about 2.08. The raw sufficient minimum
is `-0.0398241`. Thus the quotient improves the bound but does not resolve
sign. The polynomial candidates miss substantial continuum response
energy; positivity of their finite upper shorts does not close that gap.

For source-matched finite Gamma truncations at N=8, J=16,32,64 yield
negative numerical Schur minima roughly `-5.21e-4,-1.29e-4,-3.20e-5`,
while their omitted positive Gamma norm caps are approximately
`5.316e-4,1.276e-4,3.122e-5`. That resemblance is diagnostic, not a sign
certificate or an exact error bound for the nonlinear Schur map. The
untruncated source route is therefore retained; truncated negatives are
not promoted into a counterexample.

## 7. Sharper inherited scalar bound, without claiming unmodified sign

The probe re-runs the existing exact weighted-Bessel and signed derivative
certificates. Retaining their stronger `k_*=20699/10^6`, together with
`||g'||_1<11/40`, gives by D5–D7 and Young's inequality

\[
 R_0\preceq\frac{(11/40)^2}{k_*}I_P
       =\frac{75625}{20699}I_P <\frac{121}{32}I_P.             \tag{D12}
\]

Also `||G||<11/40`, since `g(0)=0` gives `||g||_1<=||g'||_1` on
`(-1,1)`. Hence the inherited positive-completion construction can use
the smaller explicit counterterm `4P`:

\[
 \langle u,(G+4P)u\rangle
 \ge\left(4-\frac{11}{40}-\frac{75625}{20699}\right)\|Pu\|^2
 =\frac{59151}{827960}\|Pu\|^2\ge0.                         \tag{D13}
\]

On the high-only nonzero subspace, inherited K-coercivity gives strict
positivity. There is no L2 spectral-gap claim. This arithmetic improvement
uses an already proved stronger constant; it is not a new source high
positivity theorem. The correction remains visible and cannot be removed
when discussing original Weil positivity.

## 8. Controls, claim ledger and next discriminator

Source controls remove the actual prime2 channel, duplicate the actual
Gamma contribution, change the actual contact by one, or delete the actual
poles; their low matrices change. Each mutation still has parity symmetry,
so reflection alone cannot authenticate the source. A matched non-Euler
extension adding a fake primitive6 hinge at `log6>1` is invisible on this
window. The live rational source checks verify `log6>1` and that 6 is not
a prime power, and reject the modified tape. This control is deliberately
outside the authentic object and is never used as a replacement source.
Low-polynomial lift and nonzero off-parity controls test quotient invariance
and rejection of false symmetry. Zero-oracle inputs are absent.

| Claim | Status and evidence | Boundary / next falsifier |
|---|---|---|
| Cross/resolvent parity survives lambda down to zero | PROVED under D>=kK and source range hypotheses; D2–D7 | A parity test alone cannot prove response finiteness |
| Exact quotient equals compressed-K dual energy | PROVED, D4–D6 | Requires H1 lift and moment-preserving density |
| Completed-square two-sided bracket | PROVED, D7 | Requires whole-high source coercivity, not finite eigenvalues |
| Zero and frozen degree-8 trials fail sufficient criterion | PROVED LOCAL, rational D11 receipts | Says nothing negative about actual G/S0 |
| N<=20 source trial comparisons | OBSERVED numerical | No rigorous full Gram quadrature error |
| Response cap and explicit correction sharpen | PROVED conditional on inherited source inequalities; re-run exact receipts | Modified operator only |
| Original four-low Schur sign; all radii; RH | OPEN / NOT PROVED | Need rigorously small whole-source quotient residual plus certified low margin |

The live epistemic issue is a **probe/approximation gap**, not a theorem
that the true source cannot be positive. Contact with source is direct
through pinned formula and intervals; survival of the numerical candidates
is distinct from source-map correctness. The source family is shared;
the single worker supplies no blind independent reasoner. The operational
reflection transport is an exact involution, not a physical quantum
interference claim. Commitment to RH positivity supplies no evidence.

The most discriminating next step is a better high response adapted to the
actual boundary/prime wavefront residual, followed by a rigorous enclosure
of `Pi_M (G(x-Ux))'`. Repeating the same degree-8 trial at greater numerical
precision cannot remove D11's strict obstruction. No broader sweep or
all-radius claim is included here.

## 9. Reproduction and deliverables

Owned files:

- `observational_succ/four_low_schur_proof_teeth.py`
- `tests/test_four_low_schur_proof_teeth.py`
- `scripts/four_low_schur_proof_teeth_probe.py`
- this note and `research/2026-10-15/four_low_schur_proof_teeth_receipts/`

Commands run from the isolated worktree:

```sh
OPENBLAS_NUM_THREADS=1 python scripts/four_low_schur_proof_teeth_probe.py --output research/2026-10-15/four_low_schur_proof_teeth_receipts/probe.json
python -m unittest discover -s tests -p 'test_four_low_schur_proof_teeth.py' -v
/tmp/succ-proof-teeth-py310/bin/python -m unittest discover -s tests -p 'test_four_low_schur_proof_teeth.py' -v
/tmp/succ-proof-teeth-py310/bin/python scripts/verify_provenance.py
/tmp/succ-proof-teeth-py310/bin/python scripts/observer_foundations_probe.py
/tmp/succ-proof-teeth-py310/bin/python scripts/ordinal_succ_report_probe.py
```

The numerical probe used **Python 3.12.3, numpy 2.5.0, mpmath 1.2.1,
scipy 1.18.0** from the already installed host. The last is an **undeclared
optional dependency** used for `scipy.integrate.quad_vec` and
`scipy.special.eval_legendre`. Exact numerical environment replay can install
`numpy==2.5.0 mpmath==1.2.1 scipy==1.18.0` in a separate compatible Python
3.12 environment. No environment installation or pyproject change was made
by this worker. Principal can declare a research extra for SciPy; do not
assume the shared Python 3.10 environment contains it. The exact polynomial,
source interval and obstruction code is stdlib-only. The Python 3.10 focused
test run explicitly skips two optional numerical tests; the host executes
them. The host mpmath version also differs from the repository's declared
`mpmath>=1.3` research extra and is reported rather than hidden.

`probe.json` stores full source matrices, both derivative grids, frozen U
columns, exact interval endpoints/tails, all eight obstruction certificates,
the scalar proof fingerprint, versions, commands and source/code hashes.
`validation.json` and individual logs retain the required check results.
Final focused validation: **11/11 tests pass on the host**; **9 pass and 2
SciPy-dependent tests skip on Python 3.10**. Provenance verification, observer
foundations and ordinal report probes exit 0. One Python 3.10 full-suite
command was launched with a predeclared 240-second limit and **timed out**;
the suite is incomplete, not reported as passing. Its exact command and
status are in `validation.json`. Per principal instruction it is not repeated;
integration/CI belongs to principal. `focused-final-validation.json` records
the final code hashes and focused reruns. No test count or successful probe
is presented as universal mathematical proof.
