# Compact source compression and the missing relative approximation theorem

Round II, compactness/Galerkin lane, 2026-10-16. Initial head
`5d6d717312eebee648d3cfb092875eb4120bb4b3` on
`research/observers-schur-complement-2026-10-16` in `SUCC-observer-schur`.
This lane changes only its assigned module, test, probe, dossier and
`compact*` receipts. No staging, commits, pushes, full-suite execution or
agents were performed by this lane. **Original Suzuki four-low sign OPEN;
RH NOT PROVED.**

The useful distinction is now sharp. The original compact signed operator
has an explicit finite-rank operator-norm approximation rate. High Legendre
polynomials are dense for the bounded projected-derivative response graph.
Neither fact establishes that the desired response lies in its range
closure, or that energy Galerkin iterates converge in the stronger residual
norm. Two different fixed-source countermodels below separate those issues.
They are mathematical synthetic models, never replacement zeta sources.

## Sources, definitions and authority

Read before implementation: `AGENTS.md`, `docs/METHOD.md`, the import
manifest, the previous mega-round and claim supplement, the four-low dossier
and independent audit, the source-gluing dossier, and actual modules
`source_weil_hierarchy`, `signed_gprime_enclosure`, `suzuki_legendre_source`,
`suzuki_moment_schur`, `tate_suzuki_shorting`, `one_object_residual_schur`,
`one_object_relative_residual` and `four_low_schur_proof_teeth`.
Historical failures in the inherited dossier remain unchanged.

The source is the byte-checked PR85 Suzuki adapter, Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, originating at
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. The probe compares seven inherited
source hashes against the previous signed-source receipt and checks them
again after execution. The older 72-entry import manifest belongs to the
distinct FuckingRH import lineage; its hash is recorded without pretending
it introduced PR85. No archival source is edited.

For the actual source let I=(-1/2,1/2), H=L²₀(I), and G be mean-zero
compression of convolution by the full even Suzuki g. P projects onto
Legendre modes 1,...,4 and Q=1-P. K=V*V, where Vu(t)=∫_{-1/2}^t u(s)ds;
K_Q=QKQ on QH. Write D=QGQ and b=QGP. The inherited source coercivity is
D≥κK_Q, κ=20699/1000000; the present lane does not re-certify that separate
weighted-Bessel proof. Its polynomial/synthetic controls do not establish it.

The full source retains real Gamma, contact, both signed pole channels and
the true prime-2 half-density. On 0<r≤1 its derivative is

    g'(r) = -4 sinh(r/2) + C_infinity/2
            + (log 2)/sqrt(2) 1_{r>log 2}
            - atanh(exp(-r/2)) - atan(exp(-r/2)).

No nontrivial zero coordinates are inputs. Suzuki's source convention and
mean-zero compression were checked against [the primary paper, §§1,2,8](https://arxiv.org/html/2606.09096v3).
The compact-operator facts are classical; see also
[Melrose, Hilbert spaces, Propositions 3.11–3.12](https://math.mit.edu/~rbm/18-102-S18/Chapter3.pdf).
The proofs below are supplied in full for this application. No academic
priority is asserted. These are `PAPER_PROVED` statements, with separately
identified exact finite/enclosure executions, **not Lean kernel proofs**.

## CG-01 — strong projections approximate compact operators in norm

**PAPER_PROVED, classical.** On any Hilbert space let T be compact and
P_n orthogonal projections with P_n x→x for every x. Then

    ||T-P_n T P_n|| → 0.

No nesting is necessary. Strong convergence is uniform on a compact set:
choose a finite ε-net, use convergence on its centers and ||1-P_n||≤1.
Apply this to the compact closure of T's unit-ball image, obtaining
||(1-P_n)T||→0. The adjoint T* is compact (approximate T in norm by finite
rank maps and take adjoints), so ||T(1-P_n)||=||(1-P_n)T*||→0. Finally

    T-P_nTP_n=(1-P_n)T+P_n T(1-P_n)

proves the assertion. This argument covers signed/self-adjoint and general
compact T. Conversely, if finite-rank P_n give this norm convergence, T is
compact because norm limits of finite-rank maps are compact.

**Exact negative control.** On ℓ² take P_n onto the first n standard
coordinates. P_n→1 strongly, but for T=1,
||T-P_nTP_n||=||1-P_n||=1, witnessed by e_{n+1}. A compact diagonal
T e_j=j^{-p}e_j, p>0, instead has exact error (n+1)^{-p}. These examples
do not require identifying the profinite Hilbert carrier with Suzuki's
interval carrier; all source projections below are defined on the interval.

## CG-02 — genuine finite-window compactness and derivative regularity

**PAPER_PROVED, source-derived.** On each bounded interval the Gamma kernel
series has terms -4(1-exp(-(4j+1)|r|/2))/(4j+1)². Their absolute values
are bounded by the summable sequence 4/(4j+1)². Thus the series converges
uniformly to a continuous even kernel. The remaining pole/contact terms
are continuous and the prime-power hinges are locally finite. Consequently
g(x-y) is a continuous, hence square-integrable, kernel on the finite square.
The integral operator is Hilbert–Schmidt: approximate its L² kernel by
finite sums f_i(x)h_i(y); the induced operator-norm error is bounded by the
kernel L² error. Mean-zero compression preserves compactness and symmetry.
The high compression D is likewise compact.

At a=1/2, the displayed derivative has only an integrable logarithmic
singularity at zero and a finite jump at log 2. It belongs to L¹∩L²(-1,1).
The existing exact whole-cell enclosure is replayed, yielding

    ||g'||_1 < 11/40,        ||g'||_2² < 4/25.

It integrates a logarithmic majorant on the first cell and outward rational
function enclosures on all remaining cells, not sample-point quadrature.
`original_source_cancellation_certificate(4096)` supplies the sharper
actual rational endpoints recorded in the receipt. Young's inequality on
zero-extended inputs gives

    ||(Gu)'||_2 ≤ ||g'||_1 ||u||_2.

The weak derivative of a mean subtraction is zero. Differentiating the
uncompressed kernel is valid in the weak Sobolev sense; no finite derivative
at r=0 or global Lipschitz constant for full g is presumed. The derivative
integral map is also Hilbert–Schmidt, because its kernel is g'(x-y)∈L²(I²).

## CG-03 — explicit Legendre compression bound for the authentic G

**PAPER_PROVED, source-derived with replayed exact enclosure.** Let E_N
project in L²(I) onto normalized Legendre modes e_0,...,e_N, where
e_j(t)=sqrt(2j+1)P_j(2t). Let P_N be its restriction to H, modes 1,...,N.
Set λ_N=(N+1)(N+2). For f∈H¹(I),

    ||(1-E_N)f||² ≤ λ_N^{-1}∫_I (1/4-t²)|f'(t)|²dt
                  ≤ (4λ_N)^{-1}||f'||².                    (CG.1)

To prove it, the Legendre equation is -(w e_j')'=j(j+1)e_j,
w=1/4-t². Its boundary term vanishes. Integration by parts shows
∫w e_i'e_j'=j(j+1)δ_ij. Bessel's inequality applied to the orthonormal
weighted derivatives e_j'/sqrt(j(j+1)) in L²(wdt) gives
Σ_{j≥1}j(j+1)|<f,e_j>|²≤∫w|f'|². Sum over j>N and use completeness
of polynomials in L². This proves CG.1 without presupposing that Legendre
partial sums converge in the unweighted H¹ norm.

CG.1, CG-02 and self-adjointness now imply

    ||G-P_N G P_N|| ≤ ||g'||_1/sqrt(λ_N)
                    < 11/[40 sqrt((N+1)(N+2))]
                    ≤ 11/[40(N+1)].                        (CG.2)

Indeed each one-sided compression error is at most ||g'||_1/(2sqrt λ_N),
and the triangle decomposition in CG-01 has two such terms. There is also
the independent Hilbert–Schmidt estimate

    ||G-P_N G P_N||_HS² ≤ ||g'||_2²/(2λ_N).                 (CG.3)

For the uncompressed kernel, the squared coefficients omitted by the
two-sided projection are bounded by the sum of the x-tail and y-tail
energies. Apply CG.1 in each variable. Each integrated weighted derivative
is ≤||g'||²_{L²(-1,1)}/4, since the overlap length 1-|r|≤1. Mean-zero
compression cannot increase the Hilbert–Schmidt norm. This proves CG.3.

If G_J contains the first J genuine Gamma terms, the inherited positive
tail estimate gives

    ||G-P_N G_J P_N|| ≤ ||g'||_1/(N+1)
                         + 2/(4J+1)²+16/(4J+1)³.          (CG.4)

This concerns exact compression entries. A numerical matrix, midpoint
kernel or interval midpoint requires its own matrix-entry error in addition.
These are operator errors, **not inverse, response or Schur errors**.
N=20 gives the simpler true-source spatial bound 11/840; it is a useful
uniform bound but much too coarse to infer the small low Schur sign.

## CG-04 — what polynomial graph density actually proves

Let M={f∈L²(I): ∫t^j f=0, j=0,...,3}. The inherited exact quotient identity is

    ||K_Q^{-1/2}QF|| = ||Π_M F'||,      F∈H¹(I).

Define R_Q:QH→M by R_Q u=Π_M(Gu)', and R_P:PH→M similarly. CG-02 implies
||R_Q||≤||g'||_1, and R_Q is compact Hilbert–Schmidt. The polar unitary
of V|QH identifies R_Q with -K_Q^{-1/2}D, and R_P with
-K_Q^{-1/2}b; signs and unitary do not change residual Grams.

**PAPER_PROVED.** High polynomials span{e_5,...,e_N} are dense in the graph
norm (||u||²+||R_Q u||²)^{1/2}. For any u∈QH its orthogonal Legendre
truncations u_N→u in L², and

    ||R_Q(u-u_N)|| ≤ ||g'||_1||u-u_N|| → 0.

The graph norm is equivalent to L² because R_Q is bounded. Thus replacing
any fixed admissible L² trial by high polynomials loses no asymptotic
residual accuracy. If b=DU for an actual finite-column L² response U,
projecting those columns supplies vanishing residuals, with that inequality.
This last premise is stronger than b∈Ran D^{1/2}; the latter does not assert
that a minimizing high vector exists.

**Exact closure criterion, PAPER_PROVED.** Let Z be the orthogonal
projection of M onto ker R_Q*. Set E=Z R_P. For every finite-column U,

    (R_P-R_Q U)*(R_P-R_Q U) ≥ E*E.                          (CG.5)

Decompose the residual orthogonally into E and its component in
closure Ran R_Q. Conversely, approximate each of the finitely many
columns of (1-Z)R_P by elements R_Q u; columnwise convergence implies
operator-norm convergence because PH is finite dimensional. Therefore

    inf_U ||R_P-R_Q U|| = ||Z R_P||,
    inf_U ||R_P-R_Q U||=0 iff every target column ⟂ ker R_Q*.

There need not be a minimizing U. The same infimum holds over high
polynomial columns by graph density. If E*E≥βI, CG.5 is a uniform
residual floor β. Least-squares residuals over nested polynomial spaces
converge to E*E in their finite low Gram matrices; ordinary energy Galerkin
need not minimize this norm (CG-07). Neither source coercivity nor compact
regularity establishes that E=0 (CG-08).

A useful **additional sufficient hypothesis** in abstract K coordinates is
D=K^{1/2}S K^{1/2}, where K>0 is injective and S is bounded self-adjoint
with κI≤S≤CI. Then R=K^{-1/2}D=S K^{1/2} has dense range, since S is
boundedly invertible and Ran K^{1/2} is dense. Also D≤CK. The present
source analysis supplies no such bounded upper relative factor S. This is
a conditional repair, not an identified property of the genuine Suzuki D.

## CG-05 — convergence of response energy, and its stronger-norm debt

**PAPER_PROVED, conditional classical Galerkin theorem.** Let D be bounded
positive injective on a high Hilbert space, let b have finitely many columns
in Ran D^{1/2}, and let H_N be nested finite subspaces with dense union.
The exact Galerkin response U_N solves <v,D U_N x>=<v,bx> for v∈H_N.
It exists uniquely because each finite compression of D is positive
definite. Put t=D^{-1/2}b, with its actual inverse-square-root domain.
Then D^{1/2}U_N x is the orthogonal projection of tx onto D^{1/2}H_N.
The union of those spaces is dense: approximate any u in H by H_N,
use bounded D^{1/2}, then density of Ran D^{1/2}. Thus

    L_N=U_N*D U_N = t*Π_{D^{1/2}H_N}t ↑ t*t=R0,
    ||R0-L_N|| →0,              A-L_N ↓ S0.                 (CG.6)

The norm convergence follows from finitely many columns. It requires no
bounded D^{-1} and no attainment b∈Ran D. Finite response energies are
**lower** bounds for R0; finite shorts are **upper** bounds for S0.

CG.6 controls ||D^{-1/2}(b-DU_N)||². The source sufficient certificate
requires C_N=||K^{-1/2}(b-DU_N)||² instead. D≥κK supplies the inequality
in the wrong direction to deduce C_N→0. If additionally D≤CK, Douglas
factorization gives ||K^{-1/2}D^{1/2}||≤sqrt C and

    C_N ≤ C (R0-L_N) →0.

All these are Gram/Loewner inequalities on the finite low carrier.
Without that extra upper relative control, CG-07 refutes the implication.

For the actual source, the inherited range theorem and κ bound allow CG.6
for exact high Legendre Galerkin matrices. No uniform convergence rate in
the relative residual is obtained. L² graph density in CG-04 is not a
statement that these particular iterates converge in L² or in that graph.

## CG-06 — norm convergence does not make zero-shift shorting continuous

**PAPER_PROVED counterexample, synthetic changing cross source.** On
ℂ⊕ℓ² take D=K=diag(j^{-2}), A=1/2 and b_m=e_m/m. All G_m=[A,b_m*;b_m,D]
are compact self-adjoint and converge in operator norm to diag(A,D),
since the difference norm is 1/m. The same D≥K holds throughout, and
b_m∈Ran D^{1/2} with ||D^{-1/2}b_m||=1. Yet R0(G_m)=1 and R0(limit)=0,
so S0 changes from -1/2 to +1/2. The exact vector (1,-m e_m) has energy
-1/2. The source b_m changes with m; this is not a counterexample to the
fixed-source Galerkin theorem CG-05. It exposes the missing relative norm.

At each λ>0 the response is 1/(1+λm²)→0, whereas its λ↓0 limit is 1
for every m. The two limits do not interchange. More generally, for positive
D,E and compatible b,c,

    ||b*(D+λ)^{-1}b-c*(E+λ)^{-1}c||
      ≤ (||b||+||c||)||b-c||/λ + ||c||²||D-E||/λ².          (CG.7)

Expand first in b,c using ||(D+λ)^{-1}||≤1/λ, then use the resolvent
identity. This proves positive-shift stability and explicitly displays
why no uniform zero-shift bound follows. Injective compact D cannot have
a positive uniform L² lower gap on an infinite high carrier: such a gap
would make its inverse bounded and the identity compact.

## CG-07 — fixed-source Galerkin can miss the relative norm forever

**PAPER_PROVED explicit synthetic counterexample.** On H=⊕_{j≥1}ℝ² put
s_j=2^{-j} and

    D_j = [[s_j^8, s_j^7/2], [s_j^7/2, s_j^6]],
    K_j = (s_j^8/2) I_2,                 b_j=(s_j^5,0).

These define bounded positive injective compact D,K. D_j-K_j has leading
minor s_j^8/2 and determinant s_j^14(1-s_j²)/4, both strictly positive;
therefore D≥K globally. The relative map R=K^{-1/2}D is bounded and even
Hilbert–Schmidt, with

    ||R||_HS²=Σ_j(2s_j^8+s_j^6+2s_j^4)
             =2/255+1/63+2/15.

The source is in Ran K^{1/2}: ||K^{-1/2}b||²=Σ2s_j²=2/3. Direct
two-by-two inversion gives

    <b_j,D_j^{-1}b_j>=(4/3)s_j²,
    D_j^{-1}b_j=(4/(3s_j³), -2/(3s_j²)).

Thus R0=4/9 is finite, but the infinite response vector is not in ℓ².
Observe coordinates in their fixed order, both of block 1, then block 2,
and so on. After N=2j-1 coordinates, the partial response in block j is
u_j=(s_j^{-3},0); its residual is (0,-s_j^4/2). Consequently

    R0-L_{2j-1}=(7/9)s_j² →0,
    ||K^{-1/2}(b-DU_{2j-1})||²=1/2+(2/3)s_j² →1/2.

After N=2j coordinates the formulas instead are

    R0-L_{2j}=(4/9)s_j²,
    ||K^{-1/2}(b-DU_{2j})||²=(2/3)s_j² →0.

All future blocks are included through exact geometric sums; the displayed
residual is not a truncated Gram. Thus the full Galerkin sequence has
convergent response energy but nonconvergent relative residual despite a
compact Hilbert–Schmidt residual map and dense trial union. Here Ran R is
dense (each finite block is invertible), so the failure is iteration choice,
not the closure obstruction in CG.5. For A=1/2 the genuine synthetic short
is 1/18>0, yet the κ=1 sufficient lower certificates tend to -4/9 along
the odd subsequence. Negative sufficient lower bounds do not imply negative
original energy even for a completely solvable fixed compact source.

## CG-08 — a range gap, and failure of every trial at a stated κ

**PAPER_PROVED synthetic boundary counterexample.** Work on H=L²(0,1).
Let L be the clamped biharmonic operator d⁴/dt⁴ with
Dom L=H⁴(0,1)∩H²₀(0,1); H²₀ means f=f'=0 at both endpoints.
It is positive self-adjoint via the closed form ∫|f''|² on H²₀.
Coercivity follows from the endpoint Poincaré inequalities. Lax–Milgram
gives its inverse C; in one dimension integrating the equation f''''=u
four times gives H⁴ regularity with the four clamped boundary conditions.
Thus C is bounded positive self-adjoint injective, Ran C=Dom L, and compact
by the compact interval Sobolev embedding. This is a declared classical
form/regularity construction, not inferred from finite polynomial tests.

Define K=C², D=C(-d²/dt²)C and b=C1. Integration by parts gives

    <u,Du>=||(Cu)'||² ≥ ||Cu||² = <u,Ku>.

D is bounded, positive injective self-adjoint and compact; equivalently
D=(∂C)*(∂C). The equality to C(-∂²)C follows on its actual domain.
Moreover R=K^{-1/2}D=-∂²C is bounded compact (C maps into H⁴, and
the image after two derivatives is compact in L²). It is not a bounded
inverse of a compact operator. For f=Cu, clamped endpoints imply

    ∫ f''=0,          ∫t f''=0.

In fact closure Ran R=span{1,t}^⊥. Every smooth h satisfying those two
moments is -f'' for f(t)=-∫_0^t(t-s)h(s)ds with all four clamped traces;
this f is smooth, hence in Ran C. Smooth functions with these two moments
are dense in the corresponding L² subspace: smooth approximation followed
by two fixed smooth moment corrections proves it. This proves the closure.

But K^{-1/2}b=1, a unit vector in ker R*. Thus for **every** u∈H,

    ||K^{-1/2}(b-Du)||²=||1+(Cu)''||²
                       =1+||(Cu)''||² ≥1.                 (CG.8)

The infimum is 1, attained by u=0. Relative coercivity and compact
regularity alone therefore do not imply the target lies in the range closure.

The actual D-relative response is nevertheless finite and exact:

    R0 = sup_{f∈Ran C} [2 Re∫f-||f'||²] = 1/12.           (CG.9)

Indeed C_c^∞⊂Ran C, and this subspace is dense in H¹₀ for the H¹ norm.
The functional is H¹-continuous. Its maximizer over H¹₀ is
f_*(t)=t(1-t)/2, since -f_*''=1, and square completion gives
2 Re∫f-||f'||²=1/12-||(f-f_*)'||². Its derivatives at the endpoints are
nonzero, so f_*∉H²₀ and the supremum is **not attained** in Ran C.
This uses density in H¹₀, not false density of clamped functions in an
incompatible H² graph. Douglas range theory also supplies
b∈Ran D^{1/2} from K≤D. No contradictory inverse vector is constructed.

For a particularly strong control take low A=1/6 and use the valid κ=1.
The true short is A-R0=1/12>0. Nevertheless **every L² trial** fails the
conservative sufficient lower bound by a fixed margin:

    A-L_U-||K^{-1/2}(b-DU)||² ≤ -4/5.                       (CG.10)

Here the low space is one-dimensional, f=CU and
L_U=2 Re∫f-||f'||². To verify CG.10, the endpoint identity representing
f(t) by f' gives |f(t)|²≤t(1-t)||f'||². Integrating yields
||f||²≤||f'||²/6. With c=||f''||, integration by parts gives
||f'||²≤||f||||f''||, hence ||f'||≤c/sqrt6 and ||f||≤c/6.
Using CG.8,

    A-L_U-C_U ≤ A-1+c/3-(5/6)c²
              ≤ A-1+1/30 = -4/5.

This includes complex trials, using real parts and absolute values.
The bound uses the declared conservative κ=1; it is not an impossibility
claim for every stronger coercivity constant or every different certificate.
The source is the clamped biharmonic model, **not Suzuki or zeta**. Its
role is to disprove an unjustified automatic range/approximation promotion.

## CG-09 — a genuine whole-Gamma derivative remainder for residual Grams

**PAPER_PROVED, inherited scalar bound plus matrix integration.** Reuse
`tate_suzuki_shorting.original_gamma_derivative_l1_tail`; no duplicate source
kernel is introduced. On mean-zero inputs the omitted constant Gamma
terms vanish, leaving Σ_{j≥J}4/d_j² exp(-d_j|r|/2), d_j=4j+1. Each weak
derivative has whole-line L¹ norm exactly 8/d_j². The decreasing integral
comparison gives

    η_J = 8/(4J+1)²+2/(4J+1),
    ||Π_M((G-G_J)v)'|| ≤ η_J ||v||.                         (CG.11)

Differentiated Gamma tails converge in L¹, justifying termwise weak
differentiation. The mean-zero compression subtracts constants, whose
derivatives vanish. Young's inequality and Π_M's contraction prove CG.11.
For a column map W:PH→H, let C_J be the genuine continuum Gram of
Π_M(G_J W)', and let V=W*W. For every ε>0,

    C_full ≤ (1+ε) C_J+(1+1/ε)η_J² V.                      (CG.12)

Apply ||a+b||²≤(1+ε)||a||²+(1+1/ε)||b||² to each linear combination of
columns; this proves the full Loewner inequality including off-diagonals.
It remains valid with independent PSD upper bounds for C_J and V. The
finite helper verifies rational PSD inputs and computes the right side,
but **cannot infer their source identification from their PSD or hashes**.
It lists those undischargeable hypotheses explicitly.

This supplies a continuum Gamma derivative tail, distinct from the smaller
O(J^{-2}) undifferentiated operator tail in CG.4. Replacing η_J by that
operator tail would be invalid. The remaining actual-source analytic debt
is a certified C_J for the selected response columns and controlled spatial
integration; increasing floating precision is not that certificate.

## Claim ledger, falsification routes and handoff

| ID | Status and domain | What survives | Boundary / next discriminator |
|---|---|---|---|
| CG-01 | PAPER_PROVED, compact Hilbert operators | Strong orthogonal compression gives norm convergence | Identity is exact noncompact counterexample |
| CG-02 | PAPER_PROVED, genuine finite-window kernel | Compact self-adjoint G; at a=1/2 derivative map HS | No positive gap, no inverse convergence |
| CG-03 | PAPER_PROVED + exact source enclosure | Legendre O(1/N) operator tail and Gamma norm tail | Exact compression or separately bounded entry errors required |
| CG-04 | PAPER_PROVED | Polynomial relative graph density; exact range-closure criterion | Genuine source target/kernel pairing remains to be resolved |
| CG-05 | PAPER_PROVED conditional | Exact Galerkin upper shorts converge from above | No relative-residual rate without stronger hypotheses |
| CG-06 | REFUTED implication, exact synthetic family | Norm perturbation alone does not control zero short | Does not refute fixed-source monotone response convergence |
| CG-07 | REFUTED implication, fixed compact synthetic source | Energy Galerkin can fail K-residual convergence | Different least-squares/basis scheduling can repair this example |
| CG-08 | PAPER_PROVED synthetic range obstruction | Compactness + D≥K do not imply range density; all-trial κ=1 failure | No unproved identification with Suzuki; no all-κ claim |
| CG-09 | PAPER_PROVED conditional source bound | Entire omitted Gamma derivative controlled in Gram/Loewner norm | Whole-continuum C_J and actual trial Gram still required |

The proof routes and controls are distinguished: weighted Sturm–Liouville
algebra is checked by exact polynomial differentiation/integration; block
responses are checked using independent 2×2 rational inversion and geometric
sums; clamped controls check actual fourth derivatives and both boundary
moments. These are different representations in one lane, not independent
researchers. The principal supplied the sharpened -4/5 clamped certificate
and requested the Gamma matrix tail audit; this lane checked and integrated
both derivations. Removing finite tests leaves the stated paper proofs;
removing source identification leaves only abstract conditional mathematics.

For the source-facing next step: establish whether each of the actual four
columns Π_M(G e_i)' is orthogonal to ker R_Q*, or derive a certified residual
directly without claiming general dense range. Use residual least squares
or another verified approximation method when energy Galerkin is unstable
in the relative norm. Combine an actual continuum truncated Gram with CG.12.
Only then can the sufficient Loewner bracket be quantitatively closed.
Operator norm convergence in CG.2 cannot discharge those obligations.

The different convergence requirements must remain separate:

| Requirement | Mathematical content | What it does not establish |
|---|---|---|
| Strong projections | P_N u→u for each u | Uniform identity approximation |
| Compact compression | ||G-P_NGP_N||→0 | Compact inverse or zero-shift response continuity |
| Form core | Density in the closed form norm, including its domain | Does not follow merely from Hilbert density |
| Bounded response graph | u_N→u and R_Q u_N→R_Q u | Does not put R_P into closure Ran R_Q |
| D-relative response | ||D^{-1/2}(b-DU_N)||→0 | Does not force the K-relative residual to vanish |
| K-relative residual | ||K^{-1/2}(b-DU_N)||→0 | Gives the stated residual bracket only with genuine coercivity/source data |
| Positive-shift resolvent | Bounds uniform for λ bounded away from zero | Does not allow λ↓0 without a separate uniform estimate |

The inherited unbounded-form counterexample is retained in
[`SOURCE_GLUING_PROOF_TEETH`, bounded positivity section](../2026-10-15/SOURCE_GLUING_PROOF_TEETH.md):
A e_0=-e_0 and A e_n=4n⁴e_n, with the Hilbert-dense span of
v_n=e_0+e_n/n. Its form is positive on that span but negative at e_0.
Weighted Cauchy–Schwarz and Σn^{-2}<2 prove positivity; v_n→e_0 in
Hilbert norm proves density after recovering each e_n. That convergence
fails in the form norm. This existing counterexample is not rebranded as
a new result or new test execution by this lane.

## Reproduction and receipts

The probe is serial, stdlib plus existing exact modules, and runs only
`test_compact_galerkin.py`. It records exact rational outputs, source and own
file hashes before/after, commands, interpreter, branch/head and all focused
test output. Tests in this lane do not count as kernel proofs. Other lanes,
full suites, provenance gates and CI remain under principal integration.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  /tmp/succ-proof-teeth-py310/bin/python -B scripts/compact_galerkin_probe.py \
  --output research/2026-10-16/observer_schur_receipts/compact-py310.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  /tmp/succ-proof-teeth-py313/bin/python -B scripts/compact_galerkin_probe.py \
  --output research/2026-10-16/observer_schur_receipts/compact-py313.json
```

The initial 19-test development check passed before adding the clamped and
Gamma controls. Final receipt counts and statuses are authoritative for the
frozen lane bytes; no historical CI result is represented as a new CI run.
