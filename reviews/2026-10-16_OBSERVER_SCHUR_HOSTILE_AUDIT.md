# Independent hostile audit: the observer's Schur complement

**Verdict: the reviewed theorem package and exact source-family obstruction
survive within their stated domains. One complex-conjugation error was found,
reported and corrected. The original Suzuki four-low sign remains OPEN.
RH PROVED: NO.**

This audit uses independent theorem derivations and rational countermodels.
Only this review, `scripts/observer_schur_independent_audit.py`, and `audit*`
receipts were written. No Git command, product edit, agent creation, full suite,
Lean compilation, or numerical optimization was performed by this auditor.
Concurrent integration was preserved. Repository heads were read directly from
metadata without invoking Git; source hashes define the checked working files.

## Authority and provenance

The Aletheia method and provenance discipline were applied: agreement about an
algebraic claim is separate from identification of its generating source. The
finite models, direct sums and clamped biharmonic example are explicitly
synthetic. They are not alternative zeta functions or measurements of Suzuki.
The source-specific computation retains the authentic Gamma, contact, both pole
channels and prime-2 half-density at radius a=1/2.

The actual bytes of `source_weil_hierarchy.py` have Git-object digest
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, computed independently as
SHA1(`blob <length>\0` followed by file bytes). The originating source commit
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc` is the inherited provenance record;
its ancestry was not re-executed in this no-Git audit. The founding 72-entry
import manifest is a different provenance chain. Neither its presence nor a
source-label string establishes the later analytic source identity.

The inherited whole-high bound D>=20699/1000000 K_Q is an explicit dependency,
not independently re-proved here. The inherited signed-derivative enclosure
and source identification are likewise dependencies of the quantitative
compression theorem. The new source-pair obstruction was independently
integrated below, rather than accepted from the producer's helper routines.
No hosted CI status is inferred from local receipts.

## Finding H-01: wrong complex conjugation, corrected before freeze

The first inspected OS-05 draft displayed, for
G=[[a,z],[conj(z),d]], the square

    a |x + (conj(z)/a)y|² + (d-|z|²/a)|y|².

This is false for the declared matrix convention. With a=d=1, z=i, x=i,
y=1, the actual energy is 4 and that expression is 0. The correct square
uses **z/a**, giving 4. The real-symmetric tests did not detect this complex
error. The 2x2 PSD theorem itself remains correct. The principal notified the
owner; the final dossier records the correction and the producer added an
exact Gaussian-rational regression. The independent audit retains the original
counterexample permanently under `paper_mutant`. No product file was repaired
by this auditor.

## Observer energy, sign and envelope: independent derivation

For a real symmetric or complex Hermitian form B and linear O, fiber-constant
Q(u)=B(u,u) implies Q(z)=0 for z in ker O. Applying fiber constancy to u+z
then gives Re B(u,z)=0; applying it to iu+z gives the imaginary part. Thus
ker O is contained in the radical. The converse follows by expanding Q(u+z).
The criterion concerns the actual kernel and full cross terms, not merely
isotropy. The matrix [[0,1],[1,0]], observed through x, has isotropic hidden
kernel but energies -2 and 2 at (1,-1) and (1,1).

For bounded self-adjoint G=[[A,B],[B*,D]], observation P onto the low space,
the radical criterion says exact energy factors iff B=D=0. When D>=0 and
D is nonzero, every low fiber has a strictly positive point: choose a high
direction with positive D-energy and let its scalar coefficient grow. Hence
low-only sign factorization is equivalent to **global G>=0**. If D=0, sign
factorization instead holds iff B=0, allowing indefinite A. Neither assertion
requires an inverse or an envelope range condition. These distinctions survive
the independently enumerated rational controls.

For one fiber write F(h)=a+2 Re<h,b>+||D^(1/2)h||². If bounded below, optimizing
over scalar multiples and phases gives

    |<h,b>|² <= C ||D^(1/2)h||².

This defines a bounded functional on Ran D^(1/2), including the required
annihilation of ker D. Riesz representation on its closure yields
b=D^(1/2)c with the unique reduced c in (ker D)^perp. Conversely this equality
gives F(h)=a-||c||²+||D^(1/2)h+c||². The last square has infimum zero because
Ran D^(1/2) is dense in (ker D)^perp. Thus the finite-envelope criterion is
**actual square-root range membership**, not closure membership; failure means
minus infinity. Attainment requires the stronger b in Ran D. No bounded
zero-shift inverse is introduced.

For finite-rank low P, all-column range inclusion makes C=D^(-1/2)B* bounded;
the reduced definition also covers noninjective D. Consequently
m(x)=<x,(A-C*C)x>. With A>=alpha I, alpha>0, congruence proves
S0>=0 iff ||C A^(-1/2)||<=1. In infinite low dimension, pointwise strict
positivity of A would not suffice to make its inverse square root bounded.
Reflection intertwining passes to the reduced solution by uniqueness, so the
two parity sectors remain legitimate at zero shift. Parity alone proves no sign.

Finally, for r=B*-DU the exact Gram identity R0-L_U=(C-D^(1/2)U)*
(C-D^(1/2)U) gives both bracket directions. The upper quadratic value is
Q_G(x-Ux), so a genuinely negative **upper** direction supplies a source
counterexample. A negative **lower** bound does not. These conclusions remain
conditional on the source and range hypotheses when applied to Suzuki.

The standalone audit checks 196 rational two-coordinate forms, five explicit
linear observations per form, returned same-fiber witnesses, singular fibers,
and all 343 symmetric 2x2 integer matrices in its declared alphabet. Its oracles
use explicit kernels, scalar formulas and independent determinants rather than
the producer's nullspace or PSD implementation. Finite execution is separately
labelled and does not supply the infinite proof by enumeration.

## Compact approximation and fixed-source amplification

For compact T, strong orthogonal P_N converge uniformly on the compact closure
of T's unit-ball image. Applying this also to T* gives both one-sided norm
errors tending to zero, hence ||T-P_NTP_N||→0. Identity on l2 is the exact
noncompact counterexample, with norm error 1 at every stage.

For the interval source, the uniformly convergent genuine Gamma series and
the finitely many active hinges yield a continuous finite-window kernel.
Its derivative is L1 and L2 despite the logarithmic singularity. The weighted
Legendre estimate follows from integration by parts and Bessel applied to
e_j'/sqrt(j(j+1)) in L2((1/4-t²)dt). Each one-sided operator tail is bounded
by ||g'||1/(2 sqrt((N+1)(N+2))). Summing gives the stated operator bound;
counting the two omitted kernel-coordinate tails gives the stated
Hilbert-Schmidt squared bound ||g'||2²/[2(N+1)(N+2)]. Neither estimate controls
a zero-shift inverse.

The derivative response map R_Q is bounded, so its graph norm is equivalent
to L2 and high Legendre polynomials are dense in that graph. This does not
place the target in closure Ran R_Q. Orthogonal projection onto ker R_Q*
gives the exact residual obstruction. Nor does graph density make an arbitrary
energy-Galerkin sequence converge in the stronger residual norm.

The supplied direct-sum example was derived independently. For s=2^-j,

    D_j=[[s^8,s^7/2],[s^7/2,s^6]], K_j=(s^8/2)I, b_j=(s^5,0),

det(D_j-K_j)=s^14(1-s²)/4>0. Direct 2x2 inversion gives
D_j^-1 b_j=(4/(3s³),-2/(3s²)) and response 4s²/3. Summing from j=1 yields
R0=4/9, ||K^-1/2 b||²=2/3 and ||K^-1/2 D||HS²=841/5355.
All these are exact infinite geometric sums. At the odd stage 2j-1,

    R0-L_N=7s_j²/9,
    ||K^-1/2(b-DU_N)||²=1/2+2s_j²/3.

At the even stage 2j they are 4s_j²/9 and 2s_j²/3 respectively. The odd
residual floor includes all future blocks; it is not a truncated residual.
The map K^-1/2 D is Hilbert-Schmidt with dense range, so this example isolates
iteration failure even when range density is available. It is synthetic.

## Clamped source: range obstruction and failure for every trial

Let C be the inverse of the positive self-adjoint clamped biharmonic operator
on L2(0,1), with domain H4 intersection H0². H0² here means f=f'=0 at both
endpoints. Thus Ran C is precisely that domain. Put K=C², D=C(-d²)C, b=C1.
Integration by parts gives <u,Du>=||(Cu)'||²>=||Cu||², hence D>=K. D is
bounded positive injective self-adjoint compact. The relative map is
K^-1/2D=(-d²)C; applying this inverse square root is legitimate because D's
range lies in Ran C. This map is bounded compact, not an everywhere bounded
inverse of C.

For f=Cu, both integrals of f'' against 1 and t vanish. Conversely any H2
function g with these two vanishing moments is -f'' for a clamped H4 function
f, obtained by double integration. Therefore Ran((-d²)C)=H2 intersection
span{1,t}^perp and its L2 closure is span{1,t}^perp. Since K^-1/2b=1,

    ||K^-1/2(b-Du)||²=||1+(Cu)''||²=1+||(Cu)''||² >= 1.

The exact minimum is 1 at u=0. Nonetheless Ran C contains compactly supported
smooth functions and is dense in H0¹ in its H1 norm. The variational response
extends continuously to H0¹ and equals 1/12, attained there by
f_*(t)=t(1-t)/2. Its derivatives at the endpoints are nonzero, so f_* is not
clamped and no response vector attains this value in the original high carrier.

With low A=1/6 and the valid declared kappa=1, the true short is 1/12>0.
For **every** real or complex L2 trial let f=CU and c=||f''||. Evaluation via
f(t)=<f',1_[0,t]-t> gives ||f||²<=||f'||²/6. Integration by parts then gives
||f'||²<=c²/6 and |integral f|<=c/6. Consequently

    A-L_U-C_U <= -5/6+c/3-5c²/6
               = -4/5-(5/6)(c-1/5)² <= -4/5.

This is a failure of the whole conservative certificate family at kappa=1,
despite strictly positive true short. It is not a failure of every possible
stronger kappa or a theorem about Suzuki. The audit independently checks
C1=t²(1-t)²/24, the nonclamped optimizer and 25 actual clamped polynomial
trials. The paper argument, rather than those finite controls, supplies the
all-trial quantifier.

The added Gamma derivative-Gram bound also has the correct normalization:
each omitted rung's derivative has L1 norm 8/(4j+1)², giving
eta_J=8/(4J+1)²+2/(4J+1). Applying the elementary two-vector norm inequality
to every low linear combination proves
C_full <= (1+epsilon)C_J+(1+1/epsilon)eta_J² W.
The actual continuum C_J and source-identified W remain necessary hypotheses.
An undifferentiated O(J^-2) tail cannot replace eta_J.

## Authentic source: the whole degree-eight family is excluded

Set v=P2+c6 P6+c8 P8 and take high probes P6,P8,P10,P12, with all P_j=P_j(2t)
unnormalized. The independent variational restriction gives
C_quot(v)>=c(v)*K_probe^-1 c(v). Thus the sufficient criterion is bounded
**above** by the 3x3 form M=G_vv-kappa^-1 C* K_probe^-1 C. This upper bound
is on the sufficient criterion, not on the original source energy's sign.

The stored interval endpoints were parsed as Fractions. Independently expanding
every product showed that the stored criterion intervals contain the exact
interval expression. For symmetric entry errors, the maximum row sum of radii
dominates their operator norm, so M<=midpoint+rho I is a valid Loewner bound.
Independent Laplace determinants verify Sylvester positivity of its negative;
their consecutive ratios reproduce the producer's LDL pivots. Completing the
remaining negative 2x2 block gives the exact maximum at first coefficient 1.
Complex coefficients cannot increase that maximum: their imaginary part adds
a nonpositive quadratic contribution in the same real negative block.

The second source computation imports **no producer source helpers**. It reuses
the previous independent auditor's reviewed Rodrigues/correlation implementation
from `2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md`, extends its actual
integration to Gamma512, and recomputes all twelve required polynomial pairs.
It generates independent logarithm, Machin pi, Euler-Maclaurin contact and
half-density intervals; both pole channels and the prime-2 hinge are integrated
directly. The complete omitted Gamma operator tail is
4114/8602523649. The K Gram is independently integrated from polynomial
primitives. The resulting rational matrices again certify negative definiteness.

| Tested kappa | Independent uniform criterion upper, decimal display only |
|---|---:|
| 20699/1000000 | -0.0012827126625629321 |
| 1/10 | -0.00018209597367387136 |
| 1/5 | -0.00003844088834425296 |

Exact rational endpoints and all independent source-pair intervals are in the
audit receipts. The latter two kappas are hypothetical strengthened constants,
not newly proved source lower bounds. Monotonicity excludes every kappa<=1/5
for this family. It does not exclude arbitrary high responses, all degrees,
or improvements above 1/5. The independent source implementation is distinct
from the producer but shares the authentic arithmetic source and classical
remainder mathematics; it is not a second independent source lineage.

The piecewise response calculations remain numerical models. Their sampled
positive upper shorts and negative sufficient lower matrices have no certified
continuum residual-Gram error. The audit did not refit them, reinterpret their
error estimates as rigorous, or turn a failed lower certificate into a negative
original-source direction. The fake composite 6 is invisible to this window's
kernel support, so excluding it requires the source-tape law, not parity or
an observed kernel difference. All source-channel mutants preserve reflection;
reflection alone cannot authenticate Gamma, poles, contact or half-density.

### Final source-cap addendum

The final `source-schur-final.json` adds two correct, distinct upper bounds.
Twenty-five narrow checks independently validate them in
`audit-source-cap-addendum.json`. The source calculation integrates combined
polynomials directly, using the same separate Rodrigues/Gamma512 route as above.
It does not call the producer's source-pair or matrix routines.

For q=P5+(3/2)P7-(1/2)P11, primitive integration independently gives
<q,Kq>=68437/176125950. The independent whole-source self-pair interval is
contained in the producer's interval. Any genuine D>=kappa K must obey

    kappa <= <q,Gq>/<q,Kq>
          <= 13997479742430415646730052502637873 /
             17109250000000000000000000000000000
           < 0.818124.

This is an upper ceiling on a possible coercivity constant, not a proved lower
coercivity bound. In particular it leaves a gap above 1/5; it does not show that
improving kappa can never rescue the excluded polynomial family.

For the recorded frozen rational U, independently integrated intervals for
all same-parity pairs of v_i=P_i-U(P_i) are contained in the producer's H_U
intervals. Cross-parity entries are exactly zero. Recomputing the row-radius
majorant and both 2x2 principal-minor tests verifies the genuine order

    S0 <= H_U <= M_upper,
    S0_odd <= (1939731/4294967296) I_odd,
    S0_even <= (3654297/2147483648) I_even.

The raw form coordinates have metrics diag(1/3,1/7) and diag(1/5,1/9).
The exact tests were cW-M_upper>=0, not Euclidean eigenvalues of the raw form.
These positive upper caps do not bound S0 below by zero. The lower order
A-(75625/20699)I<=S0 remains inherited, conditional on its original response
bound; it was not newly independently derived by these cap computations.

## Formal application and capsule boundaries

The fixed bridge grammar reconstructs the entire natural affine word or cyclic
rational table. The independent mutation tests recompute matching packet hashes
after changing outputs, source/epoch, composition/normalization mapping, runtime
and Lean pins, requested universal authority, or retained obligations. Every
such tested mismatch is rejected. A deliberately relabelled packet accepted
under the same caller-supplied label remains model-only, explicitly retaining
source obligations and denying physical-source and universal-Python authority.
This is the correct semantic limit, not source authentication by token.

The three source obligations remain explicit: intended source identity/epoch,
execution of pinned Python text by the runtime, and independent external-source
identification. The fresh compiler can establish statements about serialized
mathematical objects. It does not prove arbitrary Python execution correct.
The replay script freshly compiles its local Lean import closure, records full
elaborated types and axioms, and separately hashes the reused external package
artifacts. It does not claim a complete external source rebuild. These are
distinct assumptions even with a successful kernel run.

The inherited capsule auditor correctly accepts structurally well-formed false
prose with matching bytes **without issuing semantic authority**. Its result
still has an empty theorem-proved list. The audit preserves and replays the old
transitive UNVERIFIED/REFUTED/TESTED_MODEL premise-laundering regressions and the
OPEN_TARGET/proved-authority contradictions. Ordinary hypotheses survive every
dependency edge. No structural capsule audit is represented as a kernel proof.

No Lean compiler was run by this auditor. Principal-generated local kernel
receipts and their negative controls are separate evidence, reviewed for their
declared scope; they cannot establish hosted CI or the original analytic sign.

The final principal replay was inspected after completion. Sixteen fresh
receipt checks verified the actual generated source/log hashes, code hashes,
successful exits and axiom budgets: three affine declarations (`normalized`,
`prime_admission`, `all_inputs`) and four retract declarations (`pull_columns`,
`average_columns`, `project_columns`, `retraction`). The recorded compiler is
Lean4.29.1. The axiom sets are within propext, Classical.choice and Quot.sound.
Both wrong-offset and omitted-average-normalization mutants actually exit 1.
`audit-formal-receipts.json` records this **receipt validation**, explicitly
not a second auditor kernel execution. The local build establishes no hosted CI.

## Reproduction, retained failures and remaining obligations

From the SUCC worktree, the standalone audit command is:

```sh
/tmp/succ-proof-teeth-py313/bin/python -B scripts/observer_schur_independent_audit.py --source-integrals --output research/2026-10-16/observer_schur_receipts/audit-final-py313.json
/tmp/succ-proof-teeth-py310/bin/python -B scripts/observer_schur_independent_audit.py --source-integrals --output research/2026-10-16/observer_schur_receipts/audit-final-py310.json
```

The script records command, interpreter, working directory, live metadata head,
every audited source hash before/after, exact results and failed checks. It
imports producer routines only as test subjects; the independent source
calculation uses the separate correlation representation. It writes no bytecode.
These checks are not a full unittest run or Lean kernel audit.

**Final stable receipts:** Python3.10.20 and Python3.13.13 each pass **4,109**
checks with zero failures and identical before/after input hashes within each
run. Elapsed times are 15.149s and 10.132s respectively. Both metadata heads
are `990e5493a3698f1124eb52e09d5febf80a5e6c5f`, branch
`research/observers-schur-complement-2026-10-16`. New files were being integrated;
this audit makes no claim that this head alone contains every audited file.
The receipt SHA256 maps identify the actual bytes. The separate final addendum
passes 25 exact checks, and formal receipt validation passes 16. The displayed
cap-replay command below was also executed successfully. Audit code is frozen;
principal full-suite, commit and publication work is outside this audit's scope.

The independent addendum's exact source intervals and the two finite metric
certificates can be replayed without recomputing any quadrature or fitting:

```sh
python3 -B - <<'PY'
from pathlib import Path
from fractions import Fraction as F
import json
r=json.loads(Path('research/2026-10-16/source-schur-final.json').read_text())
a=json.loads(Path('research/2026-10-16/observer_schur_receipts/audit-source-cap-addendum.json').read_text())
c=r['source_high_kappa_ceiling']
assert F(a['independent_K']) == F(c['K_energy'])
assert F(c['G_energy_interval'][0]) <= F(a['independent_high_G_interval'][0])
assert F(a['independent_high_G_interval'][1]) <= F(c['G_energy_interval'][1])
assert F(c['every_valid_kappa_upper']) == F(c['G_energy_interval'][1])/F(c['K_energy'])
u=r['certified_upper_short']
for i in range(4):
    for j in range(4):
        outer=u['H_U_full_source_entry_intervals'][i][j]
        inner=a['independent_H_U_intervals'][i][j]
        assert F(outer[0]) <= F(inner[0]) <= F(inner[1]) <= F(outer[1])
for p in u['parity_operator_upper_caps'].values():
    c=F(p['operator_eigenvalue_upper'])
    m=[[c*F(p['low_coordinate_metric'][i][j])-F(p['upper_form_matrix'][i][j]) for j in range(2)] for i in range(2)]
    assert m[0][0]>=0 and m[1][1]>=0 and m[0][0]*m[1][1]>=m[0][1]*m[1][0]
print('Exact independent source interval containment and parity upper caps PASS')
PY
```

`audit-independent-initial.json` preserves the initial 3,997 passing checks.
`audit-independent-source-py313.json` preserves the first 4,108-check independent
source run. A later Python3.10 run passed the mathematical/API checks but its
stability gate detected concurrent edits to the principal bridge and replay
script; the failed stability receipt is retained as
`audit-intermediate-py310-drift.json`, with its full log. It is not counted as
a stable-source pass. The corrected complex identity is likewise retained as
a real defect and counterexample, not erased by the final pass.

The consequential missing source lemma is identification or control of the
actual target's component in ker R_Q*, together with a source-certified whole
continuum residual Gram for a useful response. Dense polynomials, compact
compression, finite response-energy convergence and source hashing do not
discharge these debts. The clamped example proves that automatic promotion
would be false, and the authentic degree-eight certificate rules out one whole
trial family. Neither result settles the original Suzuki sign.
