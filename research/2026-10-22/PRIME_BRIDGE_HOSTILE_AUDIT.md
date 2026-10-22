# Prime Bridge: hostile audit and preserved countermodels

**Baseline:** `b116841f12b41aaf7600da39bbb40577f25b6295`.
**Research branch:** `research/prime-bridge-2026-10-22`.
**Audit type:** independently derived paper arguments and exact finite arithmetic;
not Lean certification, empirical physics, or an independent-model endorsement.
The auditors and constructors share a model family and repository context.

## Audit boundary and prior work

The audit read the repository research discipline, foundations and typed-boundary
policy, claim vocabulary, relevant roadmap/index entries, import manifest, and
the implementations and histories of `unit_prime_succ.py` and
`affine_pontryagin_transfer.py`. The originating arithmetic commits inspected
were `53c53e91bd1b46071d6437fed0e68c9b337892a0` (PR #136) and
`6febdec` / `c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d` (PR #153).
Their existing results are classical weighted-vector convergence and exact
finite rational-character transfer. Neither dossier had established full
Bost--Connes C*-faithfulness or KMS classification. No imported archival file
is changed by this audit.

The full original papers opened for the audit were Bost--Connes, IHES M/95/38;
Maldacena--Susskind, arXiv:1306.0533; Pastawski--Yoshida--Harlow--Preskill,
arXiv:1503.06237; and Heydeman--Marcolli--Saberi--Stoica, arXiv:1605.07639.
The direct PDF retrieval for arXiv:1703.05445 failed in this audit; no finding
here depends on its uninspected text. Other research lanes have their own
source-access records.

The EPR/ER identification in [Maldacena--Susskind, pp. 2--3]
(https://arxiv.org/pdf/1306.0533) concerns systems with an independently available
gravity description and explicitly discusses broader speculation. It does not
provide a theorem assigning a classical wormhole to an arbitrary vector.
[HaPPY, §4.1 and Appendix A.2](https://arxiv.org/pdf/1503.06237)
already contains the cut-rank argument and the three-qutrit code used here.
Thus their integration is new to SUCC, not an established novelty claim.

## H1. Cutoff mirror identities can hide their own leakage

**Status: PROVED LOCAL; monotone-residual assertion REFUTED.** Let
`H_N = span{|1>,...,|N>}`, `P_N` its projection, and

\[
Z_N=\sum_{n=1}^N n^{-\beta},\qquad
\Omega_N=Z_N^{-1/2}\sum_{n=1}^N n^{-\beta/2}|n,n\rangle.
\]

For the **full** multiplication isometry `V_p` on `ell²(N>=1)`, direct
coefficient comparison gives

\[
R_N=(V_p\otimes I)\Omega_N-p^{\beta/2}(I\otimes V_p^*)\Omega_N
=Z_N^{-1/2}\sum_{N/p<n\le N}n^{-\beta/2}|pn,n\rangle,
\]

and therefore

\[
\|R_N\|^2=1-\frac{Z_{\lfloor N/p\rfloor}}{Z_N}.
\]

All displayed sums are finite, so this identity needs no convergence theorem.
When `floor(N/p)` remains constant and positive, increasing `N` increases the
residual squared. In particular, `p=2,beta=2` gives

\[
\|R_2\|^2=\tfrac15 < \tfrac{13}{49}=\|R_3\|^2.
\]

The residual nevertheless tends to zero for fixed `p` and `beta>1`, by the
convergent series tail. Convergence does not imply cutoff-by-cutoff monotonicity.

Now replace `V_p` by the finite compression `P_N V_p P_N`. Both sides retain
only the terms `n<=floor(N/p)` and the compressed mirror identity holds
**exactly**. A finite-matrix equality that discards the leaked output cannot
certify infinite-source convergence. This is a positive calibration of the
compressed identity and a negative calibration of the proposed inference.

**Next falsifier:** compare full-output sparse residuals with compressed matrix
residuals on cutoffs not divisible by `p`; never identify the two probes.

## H2. A composite mutation is visible to every complete prime probe

**Status: PROVED LOCAL.** For a diagonal coefficient family, the prime mirror
condition is precisely

\[
d_p(n):=a_n-c_p a_{pn}=0\quad(n\ge1).
\]

Change only `a_6` by a nonzero complex number `delta`, starting from a source
that satisfies every relation. For **every** prime `p`, the outgoing equation
has `d_p(6)=delta`. In addition,

\[
d_2(3)=-c_2\delta,\qquad d_3(2)=-c_3\delta.
\]

Thus every full prime identity detects the mutation, with squared residual
`|delta|²` for `p` not dividing six and `(1+|c_p|²)|delta|²` for `p=2,3`,
before any common renormalization. A common nonzero renormalization scales all
these residuals and cannot make them zero. Probes restricted to `n=1` miss the
mutation completely. Cutoff probes may miss outgoing equations when `6p>N`.

This distinguishes an actual prime-indexed operator relation from a list of
amplitudes at prime-number indices.

## H3. Finite prime closure and phase-blind marginals do not reconstruct a source

**Status: PROVED LOCAL / REFUTED INFERENCES.** Suppose a nonzero square-summable
diagonal vector obeys all prime relations with finite complex `c_p`. Then
`c_p` cannot vanish, `a_1` cannot vanish, and unique factorization gives

\[
a_n=a_1\prod_p c_p^{-v_p(n)}.
\]

Square summability is equivalent to both `|c_p|>1` for every prime and
`sum_p |c_p|^{-2}<infinity`. The first condition follows along each prime-power
ray. With `q_p=|c_p|^{-2}`, nonnegative finite-product expansion and monotone
convergence give squared norm `|a_1|² prod_p(1-q_p)^{-1}`. This product is finite
exactly when `sum q_p` is finite: use `q<=-log(1-q)` and, eventually,
`-log(1-q)<=2q`. These hypotheses cannot be replaced by only one of the two.

For a finite set `P` of tested primes, write uniquely `n=m r`, with `m`
coprime to every member of `P` and `r` supported on `P`. The complete solution
is `a_n=b_m prod_{p in P}c_p^{-v_p(r)}`. The seed family `b_m` is free, subject
to square summability. Choose an omitted prime `q`, set `b_1=b_q=1` and all
other seeds zero, and normalize. Every `P` relation holds, but no coefficient
`c_q` can satisfy the complete `q` relation: the equation at `q` would require
nonzero `a_q=c_q a_{q²}=0`.

Even all reduced thermal marginals fail to determine the vector phase. The
families `a_n=n^{-beta/2}` and `a'_n=(-1)^{v_2(n)}n^{-beta/2}` have identical
left and right density operators after normalization, but different full
mirror coefficients at two. They are equivalent under a specified diagonal
local unitary, not identical as vectors in the fixed source basis.

**Composite-generator control:** a putative independent Fock coordinate for
six alongside two and three has an immediate collision:
`(v_2,v_3,v_6)=(1,1,0)` and `(0,0,1)` both map to the integer six. The map sends
orthogonal source basis vectors to the same target vector, so it is not an
isometric arithmetic identification. `V_6=V_2 V_3` remains a valid composite
semigroup operation; the invalid assertion is its independence as a prime mode.

## H4. The full bounded-operator algebra has a topology obstruction

**Status: PROVED LOCAL; unrestricted point-norm continuity REFUTED.** On
`H=ell²(N>=1)`, put `H_0|n>=log(n)|n>` and `T|n>=|n²>`. The map `T` is an
isometry. For `alpha_t=Ad(exp(itH_0))`,

\[
\alpha_t(T)|n\rangle=n^{it}|n^2\rangle,
\quad\|\alpha_t(T)-T\|=\sup_n|n^{it}-1|=2\quad(t\ne0).
\]

For the last equality, fix nonzero `t`, choose integers nearest
`exp((2k+1)pi/|t|)`, and let `k` grow. The relative rounding error tends to
zero, so the phases tend to minus one. Hence `alpha` is not point-norm
continuous on all `B(H)`. Its strong-operator/ultraweak continuity and its
von Neumann algebra Gibbs/KMS interpretation are different claims.

There is a clean positive repair. On the concrete norm-closed algebra
`C*(E(r),V_m: r in Q/Z,m>=1)`, `alpha_t(E(r))=E(r)` and
`alpha_t(V_m)=m^{it}V_m`. These formulas show norm continuity on finite
*-polynomials; uniform approximation and the isometric automorphisms extend
it to the closure. This proves a concrete C*-dynamical system. It does not by
itself prove faithfulness to the universal Bost--Connes presentation.

[Bost--Connes, §1 and §§4--6](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)
separates the C*-algebra, dynamics, and KMS states. The mere finite root-average
identity in the predecessor module cannot supply those additional levels.

## H5. Interacting Gibbs correlation is not automatically entanglement

**Status: PROVED LOCAL cross-check.** The bounded perturbation and min--max
argument for `H_g=H_0+g(S+S*)` is sound when the domain remains `D(H_0)` and
the eigenvalues are listed increasingly with multiplicity. A trace bound must
sum scalar eigenvalue comparisons. It cannot rely on operator monotonicity of
the exponential for arbitrary noncommuting operators.

There is a useful exact nonproduct theorem. For `beta>1,g!=0`, suppose the
normalized Gibbs density were a product under
`n=2^k m`, `m` odd. Its two faithful marginal densities have nonnegative
negative logarithms `K_1,K_2`, and

\[
-\log\rho_g=K_1\otimes I+I\otimes K_2.
\]

The two operators strongly commute. Since `x²,y²<=(x+y)²` for nonnegative
spectral variables, the domain of their sum lies in each separate operator
domain. Arithmetic basis vectors are in `D(H_g)=D(log rho_g)`, so the following
matrix elements are legitimate. Between `|2>=(1,1)` and `|3>=(0,3)`, each
local term has a zero factor from the untouched coordinate. But
`<2|(-log rho_g)|3>=beta*g`, a contradiction. Thus the state is not a product.
This proves prime/odd correlation. Mixed-state entanglement requires a further
criterion; nonproduct alone does not establish it.

For the pure unitary orbit from `(e_1+e_2)/sqrt(2)`, the minor
`D(t)=a_1(t)a_6(t)-a_2(t)a_3(t)` satisfies `D(0)=0,D'(0)=-i/2` under
`exp(it(S+S*))`. With operator norm at most two, each amplitude has
`|a|<=1,|a'|<=2,|a''|<=4`, hence `|D''|<=32`. Therefore
`|D(t)|>=|t|/2-16t²`, positive for `0<|t|<1/32`. This independently checks
the entanglement-growth route; it does not identify a geometric metric.

## H6. Nonuniform arithmetic weights preserve one recovery region

**Status: PROVED LOCAL; universal isometry-failure assertion REFUTED.** For
any probability vector `w=(w_0,w_1,w_2)` define, with arithmetic modulo three,

\[
W_w|s\rangle=\sum_{a=0}^2\sqrt{w_a}|a,a+s,a+2s\rangle.
\]

The three supports are disjoint, and every column has norm one. Hence
`W_w* W_w=I` for **every** `w`. Nonmaximal weights do not automatically
destroy isometry.

For shares `(1,2)` in zero-based indexing, the permutation decoder

\[
|b,c\rangle\longmapsto|c-b,2b-c\rangle=|s,a\rangle
\]

transforms the encoded vector to the logical input tensor the fixed state
`sum_a sqrt(w_a)|a>_0|a>_anc`. This is exact recovery of the full logical
matrix algebra after erasure of share zero, and gives an explicit intertwiner
for every logical operator.

For an input basis state `s`, the erased share-one density has diagonal weights
`w_{b-s}`. Independence of `s` requires `w_0=w_1=w_2`; share two has the same
requirement, with the invertible shift `2s`. Off-diagonal logical matrix units
reduce to zero by solving the two retained-coordinate equations. Thus **all
three singleton erasures are correctable if and only if the weights are
uniform**, whereas the distinguished erasure remains correctable for arbitrary
weights. This is a useful weakening, not a failed code hidden by normalization.

The rational amplitude choice `(1,1/2,1/4)` has squared norm `21/16` and
probabilities `(16/21,4/21,1/21)`. Exact partial-trace calculations below
confirm the asymmetry independently of the implementation lane.

## H7. Bond entropy is not a generic tensor-network min-cut capacity

**Status: PROVED LOCAL / REFUTED INFERENCE.** The generic cut bound is
`S(A)<=sum_{e in cut}log(D_e)`: expand the state over cut indices, bound Schmidt
rank by their number, and use entropy at most log rank. Replacing `log(D_e)` by
the original entropy of an arbitrary nonmaximal bond needs extra hypotheses.

For a single bond
`sqrt(4/5)|00>+sqrt(1/5)|11>`, apply the local contraction
`F=diag(1/2,1)` on the left. The successful branch has equal amplitudes, success
probability `2/5`, and after normalization is a Bell pair. Its entropy is
`log 2>H(4/5,1/5)`. A normalized tensor contraction can implement this
postselection. It is not a deterministic local channel and does not violate
average entanglement monotonicity. Rank capacity remains valid; an unqualified
weighted-entropy capacity does not.

## H8. Even the complete boundary vector need not determine graph geometry

**Status: PROVED LOCAL.** Let `C_d:C²->(C²)^{tensor d}` be the copy isometry
`C_d|i>=|i>^{tensor d}`. Compare two boundary-labelled networks:

1. A single four-output copy vertex `C_4` (four-leaf star).
2. A two-output root `C_2`, followed by `C_2` at each of its outputs (binary tree).

Both encoders are exactly `|i> -> |i,i,i,i>`. Hence they give the same full
boundary vector and every boundary-observable expectation for every logical
input, including the four-party GHZ state from `|+>`. Nevertheless, in the
unit-edge star every distinct boundary pair is distance two; in the binary
tree a pair from opposite branches is distance four. These are different
labelled metric trees, with no subdivision-equivalence preserving all boundary
distances. All local maps in this counterexample are isometries and every
edge has dimension two.

The example refutes geometry reconstruction from unqualified state/encoder
data, not geometry reconstruction under additional perfect-tensor, minimality,
symmetry, prescribed-graph, or metric hypotheses. A declared Bruhat--Tits
carrier supplies such geometric structure independently; encoding onto it is
not a derivation of that geometry from prime entanglement alone.

## H9. Full disjoint logical recovery is incompatible with noncommutativity

**Status: CLASSICAL / PROVED LOCAL.** Suppose `W` is an isometry and disjoint
boundary regions support operators `X_A,Z_B` obeying
`X_A W=W X` and `Z_B W=W Z`. They commute on the boundary. Consequently

\[
0=[X_A,Z_B]W=W[X,Z].
\]

Injectivity of `W` forces `[X,Z]=0`. Thus two disjoint regions cannot each
reconstruct a full noncommutative logical algebra. Two-of-three recovery is
consistent because its authorized regions overlap. A commuting classical
subalgebra can have a different access structure.

## H10. Local agreement, coherent descent, and arithmetic source realization differ

**Status: PROVED LOCAL / REFUTED INFERENCE.** Finite CRT gluing for distinct
coprime moduli is a genuine positive construction. If the observed modulus is
`M`, however, the integers `x` and `x+M` have identical residue reports and
different Archimedean values. Finite residue data cannot reconstruct that
value without a source-size/range promise or other observations.

For same-prime refinements, even existence requires the actual reduction
square: `x mod p²=1` and `x mod p=0` cannot be a single source when `p>1`.
Changing orientation or source epoch cannot be silently repaired by relabeling
one chart after observations have been collected.

At the completed level, the finite adele with coordinate zero at two and one
at every odd prime is a valid integral adele but is not the diagonal image of
any rational. If a rational maps to zero in `Q_2`, injectivity forces it to be
zero, contradicting the other coordinates. Every finite collection of finite
precision congruences nevertheless has a CRT integer realization. Thus
compatible finite witnesses need not produce an element of the original
diagonal rational source class. This is a source-realization obstruction, not
a failure of the adelic completion as a mathematical object.

## Exact independent calculation receipt

The following output was produced by a fresh Python 3.12 `fractions.Fraction`
calculation directly enumerating codeword pairs and partial traces; it did not
import any new Prime Bridge module. It establishes only the finite facts
listed. The general statements above have separate paper proofs.

```json
{
  "beta2_p2_cutoff_residual_squared": {"N2": "1/5", "N3": "13/49"},
  "weighted_code_norm_squared": "21/16",
  "weighted_code_gram_is_identity_after_normalization": true,
  "weighted_code_single_erasure_success_zero_based": [true, false, false],
  "weighted_code_pair12_decoder_correct": true,
  "weighted_probabilities": ["16/21", "4/21", "1/21"],
  "inequivalent_star_binary_copy_maps_equal": true,
  "filter_4_5_1_5_success_probability": "2/5"
}
```

The test performed all nine logical matrix-unit reductions for each of the
three singleton erasures, rather than checking only basis-state marginals.
This matters: equal diagonals alone would not establish Knill--Laflamme.

## H11. Bare intertwining can pass while quantum recovery fails

**Status: PROVED LOCAL / REFUTED SUFFICIENCY.** The finished code lane exposes
a stronger control than the initial weighted-isometry test. Suppose all three
`f_r` are nonzero and consider a retained pair `(i,j)` with erased coordinate
`e`. In the pair decoder coordinates `(k,t)`, the encoded amplitude is
`f_(t-e k)`. Define, separately in each `t` block,

\[
R_{ab}|b,t\rangle=\frac{f_{t-ea}}{f_{t-eb}}|a,t\rangle,
\qquad R_{ab}|k,t\rangle=0\quad(k\ne b).
\]

Conjugate by the pair's permutation decoder. Direct multiplication cancels
the input amplitude and gives `R_ab W_f=W_f E_ab`, for every logical matrix
unit, even on a pair whose erasure recovery fails H6. The assignments preserve
matrix-unit multiplication and the identity. They generally **do not preserve
adjoints**, because the reverse coefficient has reciprocal modulus, not equal
modulus. They therefore cannot be interpreted as a physical observable
representation or a CPTP recovery.

For `f=(1,1/2,1/4)` and retained pair `(0,1)`, the logical `E_10` representative
sends the pair label `(0,0)` to `(1,2)` with coefficient `1/2`; the `E_01`
representative sends `(1,2)` back to `(0,0)` with coefficient `2`. These are
not adjoints. Yet all nine matrix-unit intertwining equations pass exactly.
The full-support weighted code consequently refutes bare operator pushing as
a sufficient criterion for quantum error correction. The surviving criterion
is the *-preserving/unitary decoder or complete Knill--Laflamme condition,
both implemented by the positive recovery construction.

## Post-construction audit record

The finished five main dossiers, code interfaces, finite tests, and
`formal/PrimeBridge.lean` were read after their construction. The following
checks were performed independently in the auditor lane:

```text
python -m unittest discover -s tests -p 'test_arithmetic_tfd.py' -v
  11 tests, 0.062 seconds, OK

python -m unittest tests.test_arithmetic_entanglement \
  tests.test_interacting_arithmetic_hamiltonian \
  tests.test_padic_bulk_network tests.test_holographic_reconstruction -v
  51 tests, 2.676 seconds, OK
```

These are working-tree scoped focused runs, not CI or a claim about the full
repository. The root integration receipt supplies final commit-scoped checks.
The independent audit verified the interacting theorem's coefficient list,
`13|g|²+12|g|+3` remainder constant, Gibbs-log domain argument, path-support
cutoff bound, and free-prefix false-correlation witness. It also verified the
projective lattice parent classification and determinant reconstruction;
weighted and refined code access sets; and all finite-field decoder formulas
in the Lean source. The Lean source's finite counts and conditional recurrence
are narrower than complex-Hilbert and infinite analytic theorems. No local
kernel execution was available to this auditor, so source inspection does not
promote them to Lean-kernel certification.

One proof wording defect was found and reported to the arithmetic lane:
arbitrary finite-rank operators on `H` need not be entire analytic for
`Ad(exp(itH0))`. For example `|u><1|` with `u_n` proportional to `1/n` is
bounded rank one, but imaginary-time multiplication by `n^s` leaves `ell²`
when `s>=1/2`. Finite **number-basis matrix sums** are entire analytic and
are the correct objects in the matrix-unit KMS proof. The lane corrected the
wording; the KMS strip proof itself did not require the false broader claim.

The inspected paper hashes (SHA-256, before any subsequent integration-only
edits) were:

| File | SHA-256 |
|---|---|
| ARITHMETIC_ER_EPR_FOUNDATIONS.md | `d11b2a6fc7de2a16c10ffafea7e61ff9a02f976fb61115f97f39df69fac02de1` |
| PRIME_MIRROR_RIGIDITY.md | `447be725f2c321aceaba4197de1c08cdc6e46596b5b32153b984da7dd1b2b162` |
| INTERACTING_ARITHMETIC_TFD.md | `938a6f8e79fd0d0e1ffa10c36f9bc8680dc1e679d9805702abd0ef5f0e14a34e` |
| PADIC_GEOMETRIC_CARRIER.md | `87afc339618ca61b061cc0f60d24bf14308615a75f5ced699570ca5754ab4edb` |
| PADIC_BULK_RECONSTRUCTION.md | `9cfb17610ed1ab49cbdeacd3479ac53abb6e587c72d71a23607f242325b82892` |
| formal/PrimeBridge.lean | `cdceeb9277cae5d77b9fd9a848d2c893bf7a73f5408d2b2ac909c3b06c772582` |

Paper audit agreement is a checked derivation bearing, not an independent
reasoner probability or a blanket warranty for later edits.

The subsequent QEC-8 root-isotropy theorem was also checked algebraically:
under strictly positive amplitudes, swapping sites 1 and 2 preserves every
code image by `k -> -k`, whereas a permutation moving site zero requires a
cyclic shift of `f` to be proportional to `f`. Three shifts give `c^3=1`;
positivity forces `c=1` and hence uniform amplitudes. Thus the positive
arithmetic code retains exactly the two-element subgroup fixing its privileged
direction. Complex phases would require a broader classification, so the
positivity hypothesis is essential. The added focused test
`tests.test_holographic_reconstruction.TestHolographicReconstruction.test_geometric_root_isotropy_detects_arithmetic_direction_choice`
was separately run and passed; it checks all six site permutations against
actual `GL_2(F_2)` actions on the three projective lattice directions.

## H12. Quantitative rigidity survives the spectral-gap audit

The later [PRIME_MIRROR_STABILITY.md](PRIME_MIRROR_STABILITY.md) was audited
separately. For `D=I-cT*`, `|c|>1`, reverse triangle gives
`||D*y||>= (|c|-1)||y||`, so `ran D*` is closed and equals `(ker D)^perp`.
Writing `x=D*y` on that complement gives
`||x||²=<y,Dx><=||x||||Dx||/(|c|-1)`, the claimed local gap.
The prime kernel projections commute, and the exact inequality
`I-prod P_p <= sum(I-P_p)` proves the stated weighted infidelity bound.
The limit intersection is the unique rigidity line under the separately
proved summability hypotheses. In particular, finite-space compressed
residuals must not be substituted into this proof.

For a declared support `n<=P`, every omitted prime has `V_p*a=0`. The
remaining weighted error therefore has the rigorous majorant
`||a||²(1-2^-s)^-2 P^(1-2s)/(2s-1)` at `c_p=p^s`.
This proves the finite-to-infinite certificate with an explicit source-support
promise; no observed finite prefix is being promoted to an infinite law.

Two new focused stability tests passed in 0.068 seconds. A further **16 fresh
complex mutation controls** used `(N,s)=(30,1),(60,1),(16,2),(24,2)` and
`delta=0,1/100,-1/100,1/20`, replacing `a_6` by `a_6+delta+i delta/2`.
For every case the exact mirror-certified lower fidelity was no larger than
the independent rigorous lower bound

\[
\frac{|\sum_{n\le N}a_n n^{-s}|^2}
 {\|a\|^2\left(\sum_{n\le4N}n^{-2s}
       +(4N)^{1-2s}/(2s-1)\right)}.
\]

Every comparison used `Fraction` and Gaussian rational arithmetic. Floating
decimal displays were diagnostics only. Reproducible core of the extra probe:

```python
from fractions import Fraction as F
from observational_succ.arithmetic_tfd import (
    Gaussian, thermal_amplitudes, norm_squared,
    thermal_mirror_fidelity_certificate,
)
for n, s in [(30,1), (60,1), (16,2), (24,2)]:
    for delta in [F(0), F(1,100), F(-1,100), F(1,20)]:
        a = thermal_amplitudes(n, s)
        a[6] = a[6] + Gaussian(delta, delta/2)
        cert = thermal_mirror_fidelity_certificate(a, n, s)
        overlap = sum((v*F(1,k**s) for k,v in a.items()), Gaussian())
        numerator = overlap.norm_squared()/norm_squared(a)
        m = 4*n
        z_upper = sum((F(1,k**(2*s)) for k in range(1,m+1)), F())
        z_upper += F(1,(2*s-1)*m**(2*s-1))
        assert cert['fidelity_lower'] <= numerator/z_upper
```

## H13. Critical-state extension: algebra and topology audit

The proposed limit on the concrete arithmetic algebra also passes a direct
relation check. For the dense monomials `V_m E(r) V_n*`, the Gibbs expectation
is zero unless `m=n`; otherwise it is
`m^-beta zeta(beta)^-1 sum_l l^-beta exp(2 pi i l r)`.
For nonzero rational `r`, periodic zero-mean phases have bounded partial sums,
and Abel summation bounds this numerator uniformly as `beta` decreases to
one. Thus the proposed limit is
`psi(V_m E(r) V_n*)=delta_mn m^-1 delta_(r=0)`.
Root averaging is compatible: its Haar coefficient is exactly
`(1/m) delta_(r=0)`. Norm-one states and dense-word approximation give a state
limit on the concrete norm closure. The KMS identity passes on the invariant
entire word algebra because its frequency factors vary continuously with beta;
the usual dense analytic-algebra strip argument extends it to the closure.
This is a different statement from a normal Gibbs density at beta one,
which H4 and the foundation dossier explicitly exclude. No universal
Bost--Connes faithfulness or KMS classification follows from this audit.

## Remaining verdict-changing obligations

- Preserve the scoped audit and rerun changed fixtures at integration; the
  successful focused checks above are not a blanket approval of later edits.
- Upgrade internal thermal correlation to entanglement only with an applicable
  mixed-state witness or classification theorem.
- Specify a unique geometric class and an observable-completeness theorem
  before asserting inverse geometric reconstruction.
- Establish refinement-compatible code maps if proceeding beyond the one-ball
  finite code. A larger graph alone is not such a theorem.
- Supply genuine all-place source compatibility, including the Archimedean
  factor, before calling any local product an arithmetic/geometric duality.
- No argument here identifies the signed completed Weil form, proves RH, or
  verifies gravitational field equations.
