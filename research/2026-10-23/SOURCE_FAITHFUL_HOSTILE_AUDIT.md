# Independent hostile audit: what the carry register repairs

**Date:** 2026-10-23. **Input:** CARRY THE TRUTH execution contract and parent
`5e2ba04c8b4ab627b6b0add588609c347346a1a2`. The audit first derived the controls
below without reading the new implementation lanes, then inspected their
implementations. This is another same-model derivation, **not an independent
external referee or a kernel proof**. Universal statements below have explicit
paper arguments; finite runs are calibration only.

## 1. Baseline and provenance distinctions

The actual inherited implementations already contain substantial parts of the
requested framework:

| Parent implementation | Existing mathematical content | What must not be called new here |
| --- | --- | --- |
| `reciprocal_succ_fucc.py` | One-based residue clock, controlled successor carry, Hilbert adjoint with a zero sector, mixed-radix coordinate change | Discovery of the residue coordinate formula or affine relation |
| `observation_pinned_geometry.py` | Source-labelled p-adic quotient tower, nonunit multiplication kernel, separately specified physical probes | A finite cyclic multiplier becoming the positive-integer isometry |
| `witt_carry_learning.py` | Mixed/equal-characteristic carry countermodels and factorial/profinite observer limits | A finite digit tree uniquely selecting a completion topology |
| `future_safe_quotient.py`, `noncommuting_proof_transport.py`, `operational_yoneda_descent.py` | Finite Moore/Mealy refinement, preserved availability/cost/source tags, distinguishing futures, source-relative Yoneda controls | The general principle that behavioral equivalence must be stable under continuation |
| `spectral_boundary_rigidity.py`, `reality_pin_geometry.py` and `test_reality_pin_hostile.py` | Canonical response realization, source-conditioned coordinate recovery, positive cyclic path/triangle isoresponse | Cyclicity alone identifying physical topology |
| `reality_pin_arithmetic.py`, `reality_pin_quantum_global.py` | Genuine arithmetic entries, exact interval budgets, inherited Gibbs-state nonstationarity | New physical measurements or a proof of named-point passive cyclicity |

The live branch ancestry is recorded separately in `SOURCE_FAITHFUL_LIVE_BASELINE.json`.
The prompt's word “ancestors” is a research-dependency request, not a Git fact:
in particular PRs #239 and #241 are comparison branches, not automatically
inherited results of parent #244. Their source must be inspected at its own
commit before importing any claim.

This audit separately read `bidirectional_source_histories.py` at
`6b50a7828cb9350aa391a5469cde8454b8a0b95c` and `boundary_port_geometry.py` at
`bed4716ce72d139cd1bb782e7a1ca4a50b014b28`. The first retains complete labelled
histories in its split/concatenation law and distinguishes clock receipts from
equal endpoints. The second stores the full `(Lambda,W,R)` port jet so later
Woodbury updates are meaningful; `Lambda` alone is insufficient. These are
important existing comparison examples of future-dependent missing state.
`git merge-base --is-ancestor` returned false for those two commits and true for
the recorded #236, #238, #240, #242 and #243 heads against parent #244.

The new-to-project leverage is therefore the complete Hilbert channel algebra,
explicit composition/memory defects, correctly typed continuum comparisons,
and their executable source controls. Academic novelty remains **UNVERIFIED**.

## 2. Classical records do not replace a coherent residue factor

Let `H=ell²(N>=1)` and `W_a e_(a(m-1)+r+1)=e_m tensor e_r`.
The coherent tensor factor is an exact unitary coordinate change. In contrast,
measuring residue and retaining the classical outcome applies

`Delta(rho)=sum_r (I tensor |r><r|) rho (I tensor |r><r|)`.

For `a=2`, the states `(e_1+e_2)/sqrt(2)` and `(e_1-e_2)/sqrt(2)` are
orthogonal, but after `W_2` and residue dephasing both give
`|1><1| tensor I_2/2`. They can no longer be distinguished even if the
classical outcome is retained. This is an exact two-dimensional counterexample
to “the classical carry record repairs every quantum source state.”

**Repair:** retain the residue/environment coherently, or explicitly restrict
the theorem to classical diagonal states. The minimal dimension statement
also needs its hypothesis: for a quotient-fiber-preserving isometry sending
the `a` source basis vectors of one quotient block into `|m> tensor E`,
orthogonality forces `dim(E)>=a`. There is no such lower bound from abstract
separable-Hilbert dimension alone.

There is an important positive restriction. On the multiplier range,

`W_a V_a rho V_a* W_a*=rho tensor |a-1><a-1|`.

Tracing out residue therefore recovers `rho` exactly. Uniform-residue
postselection is a **different channel**, with success probability `1/a`.
Neither statement licenses subsequent successor dynamics after a general
residue erasure.

## 3. The future repair is relative to the declared probe language

For the quotient probe `q_a(n)=floor((n-1)/a)+1`, two source labels in the same
block with residues `r<s` are separated at the successor time `a-s`: the larger
residue has carried and the smaller has not. Hence all-successor future
equivalence is equality on `N>=1`; the worst separation horizon in one block is
`a-1`. At `a=2`, labels `1,2` have the same current report and different reports
after one successor.

This does **not** mean every source quotient requires an extra carry register.
The residue probe `n mod a`, with successor and integer multiplication, is
already stable under these actions. Nor does a finite horizon require full
source recovery: before the first distinguishing carry, some residues remain
aliased. The exact sufficient state is relative to actions, probes, available
histories and any declared cost/availability observations.

The general arbitrary-carrier theorem is classical behavioral semantics.
The map `B:x -> (o(w x))_(w in A*)` gives the coarsest future-safe refinement of
`o`: for every surjective future-safe quotient `q:X->Y`, there is a unique
map `h:Y->B(X)` with `B=h q`. This is a
useful universal property, not a claim that the function space can be stored or
physically probed. For partial actions, availability must either be genuinely
observed, included in an explicit abstract interface, or excluded from the
observable signature. The parent implementations already enforce this gate.

## 4. One-step compression does not determine all compressed futures

Write `A_a=(I tensor <u_a|)W_a`, where `u_a` is the normalized uniform residue
vector. A direct count of residues gives, for `k=qa+r`, `0<=r<a`,

`A_a S^k A_a*=S^q[(1-r/a)I+(r/a)S]`.

Consequently, for `a>=2`,

`A_a S² A_a*-(A_a S A_a*)²=-(S-I)²/a²`.

The defect is nonzero, for example on `e_1`. A one-step compression treated as
an autonomous transition throws away information that returns in two steps.
This is an exact operator identity, not an asymptotic numerical effect.

For the bilateral clock Laplacian `L_h=h^-2(2I-S-S*)`, the same computation
gives

`A_a L_h A_a*=a L_(ah)`.

The coefficient `a` is not an authenticated change of physical diffusivity.
It is the compressed-generator artifact. At fixed `h`,

`A_a L_h² A_a*-(A_a L_h A_a*)²=A_a L_h(I-A_a*A_a)L_h A_a* >=0`.

Thus compressing the heat semigroup is generally different from exponentiating
the compressed generator. This exact second-derivative discrepancy is the
smallest useful failed heat diagram. The new heat manuscript supplies the
continuum topology and bounds; no interchange of time derivative and continuum
limit follows merely from semigroup convergence.

This general mechanism belongs to projection/memory theory. The source
specialization is useful, but the existence of unresolved memory is classical;
see Chorin–Hald–Kupferman, *Optimal prediction and the Mori–Zwanzig
representation of irreversible processes* (2000),
<https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf> and
<https://pmc.ncbi.nlm.nih.gov/articles/PMC16175/>.

## 5. A sharp topology warning for continuum FUCC

The block-overlap defect alone does not prove a representation-independent
operator no-go. In fixed `ell²(N>=1)`, normalized blocks `u_M`, `V_p u_M` and
`u_(pM)` all converge weakly to zero while retaining norm one. Their persistent
pairwise distance has no contradiction with that weak convergence.

A stronger correctly typed statement uses canonical step embeddings

`J_h e_n=h^-1/2 1_((n-1)h,nh]` into `L²(R_+)`,
`T_h=J_h V_p J_h*`, and `D_p f(x)=p^-1/2 f(x/p)`.

Then `T_h -> p^-1/2 D_p` weakly and
`||T_h f||=||J_h* f|| -> ||f||` for every `f`. Therefore for `p>1` the operators
have no strong limit. Here is a paper proof of the weak statement. On continuous
compactly supported functions, `T_h f` differs in local `L²` by a vanishing
amount from `1_(terminal cells) f(x/p)`. In each block of length `ph`, the
terminal cell has length `h`; Riemann sums therefore give weak average `1/p`.
Thus the weak limit is `(1/p)f(x/p)=p^-1/2 D_p f`. Density and `||T_h||<=1`
extend it to all `L²`. The norm identity follows from the step projections
`J_h J_h* -> I` strongly. A hypothetical strong limit would have to equal the
weak limit, whose norm is `p^-1/2||f||`, contradicting the norm identity for
nonzero `f`.

The same calculation gives the all-state sharp defect
`||T_h f-D_p f||² -> 2(1-p^-1/2)||f||²` under these embeddings: expand the
square, use the norm identity, and pair the weak limit with the fixed vector
`D_p f`. The nonvanishing block example is a special case of this correctly
typed statement.

Yet for bounded uniformly continuous position multipliers `M_b`,

`T_h* M_b T_h -> D_p* M_b D_p=M_(b(p x))` strongly.

Indeed, on the `n`th input cell the conjugated multiplier is the average of `b`
on the terminal output cell `((pn-1)h,pnh]`, followed by the input step
projection. This differs uniformly from `b(px)` by at most its modulus of
continuity at `ph`, and the step projections converge strongly. Hence correct
position-observable limits coexist with defective Hilbert amplitude limits.
This guards against both overclaiming convergence and overclaiming failure.

## 6. Equal phase magnitudes are not mixed-radix naturality

In positional digits `R=r+a s`, an additive character of conductor dividing
`ab` pulls back as

`exp(2 pi i k R/(ab))=exp(2 pi i k r/(ab)) exp(2 pi i k s/b)`.

The first denominator is `ab`, not `a`. Replacing it by an arbitrary local
character omits a twiddle/transport factor. With radices `(2,3)` and `R=1`,
the naive product of first nontrivial local characters has exponent `1/2` in
one read order and `1/3` in the reversed read order. Both have magnitude one;
they are different phases. A pure factor swap is not the authenticated
positional mixed-radix map. CRT coordinates use another declared map and must
not be substituted silently.

Likewise, the half-density `a^-1/2` exists for every integer radix `a>=2`.
It authenticates neither primality nor a particular Gamma/pole/contact
completion. A primitive-generator gate is essential if one claims a von
Mangoldt source rather than a generic logarithmic multiplier.

## 7. Clock geometry does not choose a unit or a completion

For a cycle of `N` vertices with edge length `h`, the ball of radius `R` is
isometric to its signed grid image whenever `Nh>4R`; the latter is within `h`
of `[-R,R]`. Thus `h->0, Nh->infinity` gives the real line. By contrast,
`h->0, Nh->L in (0,infinity)` gives a circle, `Nh->0` gives a point, and
`h->c>0` gives the lattice `cZ`. If `h->infinity`, every fixed-radius ball is
eventually a singleton, also giving a pointed point. Oscillating scales need
not converge; even distinct scale regimes can share the point limit.

The factorial inverse limit uses quotient bonding maps and profinite topology.
The geometric blow-up uses a scale depending on the level, with one discrete
successor moving by `h` rather than a fixed positive real length. There is no
continuous map `F:Zhat->R` satisfying `F(x+1)=F(x)+c` for `c!=0`: its compact
image would contain the unbounded set `F(0)+nc`. The blow-up does not provide
such an `F` and therefore does not evade that obstruction.

The finite clock multiplier `e_n -> e_(pn mod N)` has fiber size
`d=gcd(p,N)`, rank `N/d`, nonzero singular values `sqrt(d)`, and a kernel of
dimension `N-N/d`. It cannot be identified with the injective positive-integer
FUCC isometry when `d>1`, even if its local point map approximates `x->px`.

## 8. Physical and signed-source gates remain independent

For the arithmetic model `M=gK+bI`, the three off-diagonal entries identify
`sigma=log(M13/M15)/log(5/3)`, `g=M13*3^sigma`, and `lambda=M23/g`, under
`g>0`, `sigma>1` and authenticated source coordinates. They contain no
information about `b`. An additive scalar operator shift is not an arbitrary
additive bias attached separately to each reported entry. Source-labelled
polarization preparations can cancel a common energy-reading offset, but
their physical availability is another premise.

The parent positive cyclic path/triangle counterexample survives every
abstract scalar-response reconstruction. No carry theorem alone selects its
physical graph. Likewise, unitary coordinate transport preserves the signed
Weil form's truth conditions; it does not prove its sign. Any claimed gain in
the four-low-mode Schur complement must exhibit the actual transformed
off-diagonal blocks and a sharper bound, not merely a positive residue norm.

## 9. Calibration and audit status

An implementation-independent Python/Fraction probe in this audit checked:

- one-based reconstruction and successor carry for radices `2,3,5,7`, source
  labels `1..149`;
- separation of every pair of residues within each tested quotient block;
- compressed successor coefficients by direct source-residue counting at
  times `0,1,2,a-1,a,a+1,2a+3`;
- the exact two-state quantum dephasing counterexample;
- the unequal `1/2` versus `1/3` mixed-radix phase exponents.

All checks passed; they calibrate the paper derivations and do not execute the
universal quantifiers. The scripts in the implementation lanes provide the
persisted executable regression suite. Exact outcomes and whole-repository
validation belong to the principal validation receipt, not to this audit's
testimony.

Classical behavioral-semantics provenance: J. J. M. M. Rutten,
*Universal coalgebra: a theory of systems* (2000), institutional record
<https://ir.cwi.nl/pub/48>, paper <https://ir.cwi.nl/pub/48/0048D.pdf>.
This audit uses its provenance to classify the abstraction; the elementary
word-kernel proof above is independently stated in this round's observer
manuscript.

**Verdict:** the exact carry/defect repair survives within its source and
topology contracts. Classical-record quantum repair, autonomous one-step
compression, magnitude-only source authentication, and unqualified
completion identification fail with explicit witnesses. Physical realization,
named arithmetic passive cyclicity and completed Weil positivity remain
separate open obligations.

## 10. Audit after the construction lanes were written

The following manuscript arguments and their corresponding new Python modules
were then read directly. This is a mathematical audit of supplied arguments,
not a replacement for their executable test receipts.

- **Carry:** the one-based adjoints, channel composition, continuum weak
  limit, energy-domain cocycle and minimal defect factorization survive. The
  initially written tensor-character assertion missed the radix-one exception:
  with `a=1` every character on the b-factor is a character of the source. The
  manuscript was corrected to require `a>=2`. Its proposed disclosed-loss
  category was also made precise by taking arrows modulo environment-unitary
  equivalence, so the associativity and identity laws hold on actual classes.
- **Memory:** elimination recurrence (M3) has the correct order and indices.
  The reduced-denominator argument in M3 is valid: at a root of `1-z t^a`,
  its numerator is `(z-1)^2 t/[a z(1-t)^2]`, nonzero for `z!=0,1`.
  The manuscript correctly distinguishes a bilateral/formal phase fiber from
  the unilateral source shift. No spectrum of the latter was silently used.
- **Observers:** the arbitrary-carrier universal-factorization direction,
  finite-horizon partitions, exact separator cost and affine energy-calibration
  formulas survive. The code compares entries to the parent's separately
  assembled source matrix and retains the per-entry-bias countermodel.
- **Heat:** the `4R` metric threshold, complete subsequential scale list,
  dispersion/tail/quadrature estimate, embedded semigroup proof, Mellin
  normalization and factor-a diffusivity defect survive. The strong semigroup
  proof uses an especially useful check: weak convergence at `2t` gives norm
  convergence at `t`. The rational error constants bound the analytic constants
  conservatively; they are not fitted to numerical observations. The even-N
  hypothesis of the finite Fourier chart must remain explicit (factorial
  clocks satisfy it eventually).
- **Signed-source transport:** the two-multiplier crowding proof, compact-seed
  damping threshold and resolution-cost squeeze in
  `SOURCE_FAITHFUL_WEIL_AUDIT.md` survive direct inspection. For the unweighted
  claim, a two-dimensional arithmetic orbit supplies quadratically many
  orthogonal source vectors in only linearly many bounded-width log bins.
  Norm-continuity of translations makes one bin's images nearly parallel,
  contradicting boundedness. For weighted synthesis, local harmonic sums
  bound the map exactly at exponent `1/2`, and source blocks refute every
  smaller exponent. These are genuine scoped transport/obstruction theorems;
  they do not improve the authenticated four-mode Schur lower bound.

The latter no-go proof uses only a strongly continuous one-parameter unitary
group in the target. Thus the same argument applies to such a target group
`U_t`, whenever the proposed bounded intertwiner obeys
`J V_p=U_(log p) J` and `J V_q=U_(log q) J` for multiplicatively independent
p,q. This scope observation does not rule out weighted covariance, additional
independent target actions, distribution spaces or unbounded source-core maps.

No load-bearing error remains in the audited arguments after the stated
radix-one and categorical corrections. This is a provisional audit judgment
within the displayed source contracts, not a certificate of academic novelty,
physical applicability, or the unresolved Weil sign.

## 11. Final memory/resolvent and receipt pass

A final read checked RM1–RM9 against the actual Bloch weights, reciprocal
bounds and independent two-residue source inverse. The all-alpha resolvent
estimate and bounded-alpha memory estimate have different valid uniformity
scopes; the alpha=h^-4 control separates them. No load-bearing error was found.
The final growing-radix sentence had its implication reversed: a^3 h^2→0
implies ah→0, while ah→0 alone does not force the current sufficient memory
error bound to vanish. It was corrected; a≈h^(-3/4) separates the conditions.
This is a counterexample to the proposed implication, not to an optimal bound.

The deterministic receipt's finite/universal, analytic/Lean, physical,
passive-cyclicity and signed-source authority flags were reviewed. Legacy
mathematical helpers were added to its hash list, and the success message now
says **listed** executable fingerprints rather than asserting a full dependency
closure. The root also corrected an M3/M4 subsection reference. These editorial
and receipt corrections change no theorem or source arithmetic.
