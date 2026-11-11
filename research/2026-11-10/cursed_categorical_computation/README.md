# Cursed categorical computation: coherent numerical arrows

This dossier develops the user's request for deliberately strange computation
paths, including arrows encoded by numbers that open into coherent families
and categories. It contains exact constructions, source-preserving obligations,
countermodels, executable rational probes, and an explicit statistical boundary.

## Reading map

| File | Content |
|---|---|
| [ROUND_I.md](ROUND_I.md) | Tiny categories, averaging oscillators, the bicyclic origin, source-gauge countermodels, digit randomization, and inverse-beta source recursion. |
| [ROUND_II.md](ROUND_II.md) | Numerical Karoubi completion, affine ideal categories and Möbius inversion, rational matrix corners, family functors/spans, signed groupoids, and FRACTRAN. |
| [DEDEKIND_YONEDA.md](round_iii_dedekind/DEDEKIND_YONEDA.md) | Round III: exact irrational category, rational restricted Yoneda, Isbell/MacNeille cuts, locators, and labelled enclosure diagrams. |
| [COMPUTATION_GRAPH.md](round_iii_dedekind/COMPUTATION_GRAPH.md) | Integer Pell and Stern–Brocot machines; authentic BBP interval bounds; certified digits and Fourier observers; discontinuity controls. |
| [RATIONAL_ARITHMETIC_COMPILER.md](round_iii_dedekind/RATIONAL_ARITHMETIC_COMPILER.md) | Cut convolution; rational quadratic matrices; Q(pi) as Q(t); natural-number arrow codes; finite-power functor families; enriched Isbell completion. |
| [Circle/line observer — Round IV](../circle_line_lr_observer/README.md) | Geometry-derived matrix and rational-rotation sources; productive L/R program; conic equivalence, metric cocycle, and explicit Fourier precision schedule. |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Scoped proof, finite-check, refutation, and open-obligation labels. |
| [SOURCES.md](SOURCES.md) | Pinned repository context and checked primary mathematical sources. |
| [VALIDATION.md](VALIDATION.md) | Exact validation scope and publication checkpoints. |
| [round_ii_probe.py](round_ii_probe.py) | Standalone standard-library exact regression probe. |
| [round_ii_receipt.json](round_ii_receipt.json) | Saved finite execution with script hash and control outcomes. |

## The useful result

For every monoid M, its Karoubi envelope is equivalent to the category of
idempotent principal right M-sets eM and equivariant maps. Opening each such
family into its category of elements over BM gives another equivalent
presentation. The projection to BM retains the multiplication labels. This is
an actual arrow-to-number-to-family/category bridge, with maps, composition,
identities, and reconstruction supplied in Round II.

For the load-bearing positive affine clock monoid, numerical codes
2^(a-1)(2b+1) preserve the noncommuting product (a,b)(c,d)=(ac,ad+b). Its principal
ideal category is equivalent to the one-object monoid category, but ideal
inclusions must be retained to recover each particular clock operation. The
affine incidence inverse has the exact sparse form

$$
\mu_{\mathrm{Aff}}(a,b)=\mu(a)(\mathbf1_{b=0}-\mathbf1_{b=a}).
$$

These constructions help compile and audit computations. The source and
observer remain part of the mathematical object: forgetting them can identify
the authentic forcing with zero forcing while changing phase observations.

## Round III: the two Isbell constructions meet the source

The irrational category is the full order category on R minus Q. It is
isomorphic to the category of nonempty proper MacNeille fixed rational cuts
having no greatest element. Rational restricted Yoneda preserves and reflects
all its order arrows. The labels are essential: bare lower-cut categories
for different endpoints are all isomorphic countable dense orders.

The concrete source gets a rational interval graph. With
pi_N=sum_(n=1)^N 16^(1-n)r(n), the proof supplies

$$
0<\pi-\pi_N<\frac{16^{1-N}}{(8N+1)(8N+2)},\qquad
0<16^{N-1}\pi-U_N<\frac1{(8N+1)(8N+2)}.
$$

Exact interval arithmetic certifies individual floor decisions after checking
integer margins, and continuous circle characters with explicit error budgets.
The pi results are compared with a separately implemented Machin interval name.
For sqrt(2), Pell recurrence supplies a uniform hexadecimal floor schedule.
The same cut graph recovers the inherited source-specific two-prime witness
Im(a_6-a_3-a_2+a_1)<1-sqrt(3), with eight exact phase-cell certificates and a
coherent wrong-seed control. Its scope is finite and explicitly retained.

Classical transcendence gives Q(t) isomorphic to Q(pi). Polynomial identities
decide equality of rational expressions; the cut of pi decides their real
order by terminating rational enclosure refinement. The nonconstant-expression
floor theorem follows because such expressions evaluate to irrational values.
This is a specific computable ordered field, not an oracle for arbitrary reals.

At the categorical level, the Ab-enriched reflexive completion of the
one-object field Q(t) is FinVect_Q(t), hence equivalent to FinVect_Q(pi).
Its matrix skeleton has both canonical natural-number arrow codes and an exact
presentation by finite-power functors G_n(V)=V^n with all natural transformations.
The same matrix category appears as corners of Q(t)<S,T | TS=1>.

Thus Isbell conjugacy makes rational upper/lower-bound cuts in the order case
and algebraic double-dual fixed vector spaces in the enriched field case. The
enrichments differ and are explicitly retained. The completed source constant,
its rational computations, and the previous round's numerical-arrow families
now have a common, auditable set of translations.

Three additional exact probes and saved receipts live in round_iii_dedekind/.
They test completion/coding, Pell/BBP observers, and symbolic field/functor
operations. They are research scripts with explicit finite scopes, not additions
to a claimed full SUCC execution compiler.

## Boundary and provenance

This is additive research based on Main XXII at
`43886e830cee5ff6d6b37719e18d809819673bd9`. Unmerged donor results are cited at
their inspected snapshots, not silently integrated as new main theorems. No
frozen source, historical seed, existing claim status, or CI workflow is changed.

The fixed source has U_0=0, U_n=16U_(n-1)+r(n), and
sum_(n>=1)16^(1-n)r(n)=pi. The alternate partial sums P_n use weights 16^(-n),
so P_infinity=pi/16. The distinction is retained throughout.

No categorical equivalence or finite run here proves pi normality, original-zero
parity balance, or RH. The next load-bearing obligation is a source-derived
signed-cancellation bound, with the evaluator and residual transported exactly.
