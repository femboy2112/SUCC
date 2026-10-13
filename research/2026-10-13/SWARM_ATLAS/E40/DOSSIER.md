# E40 — Spectral dynamics: a sharp finite-delay test for projection zeros

Date: 2026-10-13. Branch: `research/swm-e40-2026-10-13`.
Immutable VOYAGER source parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.

**Result:** on a declared stationary linear source of dimension at most `d`,
the common regular zeros of the first `d` delayed resolvent readouts are
exactly the completely unobservable source directions. For a source with
a nonzero observable trace, this family has no common regular zero.
The bound `d` is sharp for this ordered family. This is a short consequence
of classical observability, with a supplied local proof and exact witnesses;
independent principal acceptance remains pending. No academic novelty,
physical measurement, source authentication, or RH result is claimed.

## 1. Original question

The original SUCC question concerns finite embodied observers constructing
knowledge from causal interactions. The existing dynamic Fourier tower asks
what survives a source-observer quotient; the virtual Mellin model asks which
analytic completions remain compatible with a restricted source signature.

The E40 question is more precise: **when a spectral readout vanishes, can
another lawful readout distinguish a missing source from projection
cancellation, and what finite completeness hypothesis pays for that verdict?**

We preserve three separate meanings:

1. A coordinate description changes by a lawful invertible transport.
2. A scalar observation channel is replaced or augmented.
3. An admissible mathematical source model is replaced.

Only the first operation automatically preserves a fixed source-target
response. A zero of a fixed scalar transfer function is a real zero of that
function, even when another channel detects the source. Calling it a
projection zero below means a zero relative to an enlarged probe family;
it never means that its scalar value was false.

The live gap is a **probe-gap** in a specified model. It becomes an
**access-gap** if the extra readouts cannot be physically realized, and a
logical **boundary** if no finite source dimension or stationary source law
is supplied. These labels are not claims about human cognition.

## 2. Existing mathematical context

At the frozen parent, `dynamic_fourier_tower.py` contains finite cyclic
Fourier naturality, projection energy debt and the source-update criterion
`U(ker A) ⊆ ker A`. `virtual_mellin_zeros.py` contains the Gaussian deformation
`C_e(s)` and exact source-class classification. Their preceding dossier is
`research/2026-10-12/DYNAMIC_FOURIER_VIRTUAL_ZERO_FRONTIER.md`.
The current ledger already separates Fourier observer nulls (O347–O359),
analytic shadow common divisors (O369–O372), and Hankel dimension lower
bounds (O379–O380). E40 adds a sharply bounded **temporal probe family**;
it does not repeat those results as new discoveries.

Primary prior art inspected on 2026-10-13:

- [R. E. Kalman, *Mathematical Description of Linear Dynamical Systems*,
  JSIAM Control 1(2), 1963, 152–192](https://people.duke.edu/~hpgavin/SystemID/References/Kalman-JSIAM-1963.pdf),
  DOI `10.1137/0301010`. §§3–5 distinguish state-coordinate equivalence
  from input/output structure; §§6–8 develop observability, irreducible
  realizations and rational transfer functions. The finite-delay criterion
  below belongs to this classical theory, rather than a new spectral theory.
- [John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*,
  Princeton dissertation, 1950, original scan](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf),
  §§2.2–2.4. The additive character, self-dual Haar normalization,
  multiplicative measure and quasi-character domain are genuine source
  data. A chosen test integral is not automatically a canonical L-function.

These are literature bearings from original works. The proof and program
below share one reasoner and model coefficients; their different
representations are checks, not independent principal reviews. Broader
mathematical priority has not been established.

Provenance manifest inspected: source repository `femboy2112/FuckingRH`,
originating commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`, 72 entries.
Neither E40 anchor is an imported entry. Their latest source commits are
`c17538418aed8bfe84876f0014acbbf421ede513` (dynamic Fourier) and
`fa2c76f9c9d2e587324603897388480fb445bb37` (virtual Mellin).
No imported theorem, archive, runtime path or historical default is modified.

## 3. Proposed SUCC objects

Fix the mathematical source specification
`(V,T,C,b)` with `V=C^d`, `d≥1`, a stationary endomorphism `T:V→V`,
a readout `C:V→C^m`, `m≥1`, and one original-source vector `b∈V`.
The probe uses the scalar case `m=1` with rational coefficients.

For `s∉spec(T)`, define

\[
 R_s b=(sI-T)^{-1}b,\qquad
 G_k(s)=C T^k R_s b,\qquad h_k=C T^k b.
\]

`G_k` is the mathematical spectral response of the composite readout
`C∘T^k`; `h_k` is the source's finite time trace. The resolvent computation
is made from a complete declared model, not from a claimed physical event.
No spectral `s` is identified with a zeta zero.

The temporal observation map and stable unobservable subspace are

\[
 O_d v=(Cv,CTv,\ldots,CT^{d-1}v),\qquad N=\ker O_d.
\]

A **projection cancellation at `s`** means `G_0(s)=0` and `b∉N`.
A **trace blackout** means `b∈N`: every allowed time readout vanishes,
although the original source vector may be nonzero.
These are source-, law-, and probe-family-relative notions.

A source identity/epoch/basis tag is only a declared consistency condition.
Combining readouts from different original vectors, unverified resets or
changing dynamics is outside the theorem. Finite observed prefixes do not
prove the dimension bound or stationary model law.

## 4. Candidate theorem

**E40-T1 (CLASSICAL / PROVED LOCAL; supplied derivation, principal review pending).**
For every `d,m≥1`, every `(V,T,C,b)` as above and every
`s∈C\spec(T)`, the following are equivalent:

\[
\boxed{
 G_k(s)=0\ (0\le k<d)
 \iff b\in N
 \iff h_k=0\ (k\ge0)
 \iff G_k\equiv0\ (k\ge0).
}
\]

Thus any one nonzero observable source trace excludes common regular
zeros of the first `d` delayed readouts. Full state observability is a
sufficient special case, not a necessary hypothesis for this conclusion.
For fixed `b`, the cyclic subspace
`span{b,Tb,T²b,…}` may replace `V`, improving the bound to its dimension.

**E40-T2 (PROVED LOCAL, sharpness).** For every `d≥2` and real `a≠0`,
there is a minimal `d`-dimensional rational-response realization whose
first `d−1` members `G_0,…,G_(d−2)` all vanish at the regular point `a`,
while `G_(d−1)(a)=−1`. The theorem therefore cannot uniformly discard
the final member of this ordered family.

**E40-T3 (CLASSICAL / PROVED LOCAL, covariance).** Under
`T'=STS⁻¹`, `b'=Sb`, `C'=CS⁻¹` for any `S∈GL(V)`, every `G_k` is
unchanged and `N'=SN`. A fixed-target zero cannot be removed by a lawful
coordinate change.

**E40-T4 (CLASSICAL, analytic comparison criterion).** Let `F` and a
finite nonempty family `m_j` be holomorphic on a connected open domain, with
`F` non-identically-zero and at least one non-identically-zero `m_j`.
Suppose the **same-source factorization** `Y_j=m_j F` has been proved.
Then at every interior point `s_0`,

\[
 \min_j\operatorname{ord}_{s_0}Y_j
 =\operatorname{ord}_{s_0}F+\min_j\operatorname{ord}_{s_0}m_j.
\]

The family recovers exactly the target zero multiplicity iff at least one
multiplier is nonzero at `s_0`. Without the same-source factorization,
response agreement supplies no such source-invariant interpretation.

## 5. Proof attempt

The proof closes in finite-dimensional linear algebra; no numerical
precision or inference from finite search is used.

**T1.** Cayley–Hamilton expresses `T^d` as a linear combination of
`I,T,…,T^(d−1)`. Hence `N` is `T`-invariant: for `v∈N`, the first
`d−1` coordinates of `O_d(Tv)` vanish directly, and the final one
vanishes by that relation. Induction gives `CT^k v=0` for all `k≥0`.

If all `G_k(s)` for `k<d` vanish, `r=R_s b∈N`. Invariance gives
`b=(sI−T)r∈N`. Conversely, `sI−T` maps `N` into itself and is injective
there; finite dimension makes its restriction surjective. Its inverse
therefore maps `N` into `N`, so every delayed response vanishes for every
regular `s`. Membership in `N` is exactly vanishing of the first `d`
trace terms, and Cayley–Hamilton extends this to every term.
Finally, if every `G_k` is identically zero, the expansion
`G_k(s)=h_k/s+O(s⁻²)` at infinity yields every `h_k=0`.
This establishes all equivalences. Apply the same argument to the
`T`-invariant cyclic subspace for the smaller bound.

**T2.** Let `T e_i=e_(i+1)` for `i<d`, `T e_d=0`, `b=e_1`, and
`C=e_(d−1)^T−a e_d^T`. Then

\[
 R_s b=\sum_{i=1}^d s^{-i}e_i,\qquad
 G_0(s)=(s-a)/s^d.
\]

For `0≤k≤d−2`, `G_k(s)=(s−a)/s^(d−k)`; the last member is
`G_(d−1)(s)=−a/s`. All claims follow at `s=a`, which is regular because
`spec(T)={0}`. The trace has only `h_(d−2)=1` and `h_(d−1)=−a`
nonzero. The `d×d` Hankel block `H_ij=h_(i+j)` (`0≤i,j<d`) has

\[
 \det H=(-1)^{d(d-1)/2}(-a)^d\ne0.
\]

Since `H=O_d [b,Tb,…,T^(d−1)b]`, every compatible linear realization
has dimension at least `d`. Our realization attains it. This proves
sharpness with a minimal source rather than an artificially padded one.

**T3.** Substitute `(sI−T')⁻¹=S(sI−T)⁻¹S⁻¹` and `(T')^k=ST^kS⁻¹`.
All `S⁻¹S` factors cancel. The observation map satisfies `O'_d S=O_d`.

**T4.** Holomorphic vanishing orders add under multiplication. Take
the minimum over the finite family; its zero-order gap is precisely the
common multiplier divisor. At a point where `m_j≠0`, `F=Y_j/m_j`
is a local analytic reconstruction. If only the `Y_j` are supplied,
their cross-identities `m_iY_j=m_jY_i` are an additional coherence gate.
No bounded global inverse follows from these local divisions.

## 6. Crucible

Predictions before the probe: a projection-zero rival permits a nonzero
delayed response; a trace-blackout rival predicts zeros for the full
`d`-family; a coordinate-artifact rival predicts that a lawful similarity
can remove a fixed-target zero. Exact nonzero responses are decisive;
a singular resolvent is excluded rather than silently counted as a pass.

**Minimal mutation.** Fix
`T=[[0,0],[1,0]]`, `b=(1,0)`, `s=1`. The original channel `C=(1,0)`
reports `1`. Mutating just its second coefficient to obtain `C=(1,−1)`
gives `R_1b=(1,1)` and readout family `(0,−1)`.
The scalar zero is genuine for the mutated target and is invariant under
all fully transported similarities. It is not a source-vector zero or
an unavoidable common zero. The Hankel minor is
`[[1,−1],[−1,0]]` with determinant `−1`, forcing dimension at least two.
In dimension one, `Cb/(s−T)` has no regular zero when `Cb≠0`; 320
exact one-dimensional calibrations check this minimality boundary.

**Sharp horizon and blackout controls.** The saved receipt instantiates
T2 at `a=3/2` for `d=2,…,6`, including raw source matrices, resolvent
vectors and nonzero Hankel determinants. A different source
`T=diag(1,2)`, `C=(1,0)`, `b=(0,1)` at `s=3` has nonzero source
resolvent `(0,1)` and two zero readouts: the theorem identifies a real
unobservable direction rather than incorrectly certifying source absence.

**Fresh configurations.** Seed `401310` generates 360 independent model
declarations of dimensions 2–5: 331 regular solves pass the stated
equivalence and kernel-invariance check; 29 singular cases are excluded.
Every regular case is separately transported by an invertible shear,
with all 331 response vectors and source-resolvent transports equal
exactly. These are fresh seeded controls, not blind independent witnesses.

**Complete factorial.** Independently toggle the source dynamics
`T=0` versus the nilpotent `T`, and channel `(1,0)` versus `(1,−1)`,
while fixing `b` and `s=1`. In the order `(00,01,10,11)`, the responses
are `(1,1,1,0)`, giving mixed difference `−1`. This is exact
non-additivity in a complete design. The formula supplied above explains
the cancellation; the cross-term alone is not a mechanism or quantum claim.

**Analytic controls.** Exact polynomial `F=(s−2)^2(s+1)` with
`m_1=s−3`, `m_2=s−5` has response gcd exactly `F`. Repeating `m_1`
as a second channel retains the extra factor `s−3`; duplicate routes do
not supply an independent source check. Substituting a different source
factor in one channel gives a nonzero cross-square defect and is rejected.
This is an algebraic calibration of T4, not a constructed arithmetic source.

**Stability adversary.** For the minimal mutation,
`(G_0(s),G_1(s))=((s−1)/s²,−1/s)` has no common regular zero, but its
squared norm tends to zero as real `s→+∞`. The receipt includes exact
values at `10,100,1000`. More generally the resolvent Neumann bound
`||R_s||≤1/(|s|−||T||)` for `|s|>||T||` proves decay of every fixed
delayed channel. Exact discrimination does not imply a uniform lower
frame bound or noise-stable source recovery.

## 7. Verdict

| Claim | Status and receipt | Scope and next falsification opportunity |
|---|---|---|
| Complete delayed readouts distinguish isolated scalar cancellation from trace blackout | CLASSICAL / PROVED LOCAL, T1 proof and exact controls | Known finite stationary linear source; principal proof audit next |
| `d` members are necessary in the worst case for this ordered family | PROVED LOCAL, T2 and nonzero Hankel determinant | Search any omitted `G_(d−1)` witness; preserved at every `d≥2` |
| Lawful invertible coordinates remove a fixed scalar target zero | REFUTED, T3 plus the two-state witness | A changed channel or changed source is a different operation |
| Common zero-free channels imply globally stable decoding | REFUTED, norm decay at infinity | Seek an explicit compact-domain lower bound with an honest norm |
| A finite unknown-source prefix establishes the dimension upper bound | REFUTED AS INFERENCE, arbitrarily large T2 source | Supply a complete independent recurrence/model law |
| Common analytic divisor equals the target divisor | CLASSICAL conditional T4 | Prove the common source factorization and absence of joint auxiliary zeros |

T1 and T2 **survive** the stated crucible. The overclaims above fail with
preserved receipts. The productive residual is a **source-law-and-probe
closure certificate**, rather than an interpretation of every scalar
zero as either canonical arithmetic data or a removable coordinate defect.
No shared project ledger or status promotion is performed here.

## 8. Remaining obstruction

The matrices and dimension bound are complete model premises. A finite
Hankel rank is a dimension **lower** bound; it supplies no unknown-source
upper bound. Given any finite delay budget, T2 with larger `d` leaves
all tested channels zero and a later channel nonzero. This is a concrete
countermodel to an unrestricted finite-horizon completeness claim.

For an infinite-dimensional transfer operator there is no automatic
Cayley–Hamilton cutoff. Domains of `CT^k` and the resolvent, closedness,
cyclic density, unobservable subspace closure and spectral singularities
require separate hypotheses. An interval/norm certificate would also be
needed to make finite precision into a proof. No such extension is proved.

The next useful lamp is a source-certified compact-domain quantitative
bound for an authorized finite probe family, or a bounded-operator
counterexample separating finite Krylov visibility from an infinite
spectral target. Physical readout/reset availability remains separate.

Diagnostics: κ is contact with complete mathematical declarations only;
φ is the exact stated proof/probe pathway; σ is pinned code/model lineage,
not physical authenticity; ρ is not a truth weight; μ includes only the
declared delayed readouts. Seeded configurations share one implementation
family. The lawful transport is the similarity formula, and no semantic
phase or truth probability is assigned.

## 9. Cross-domain connection with actual maps

**Finite quotient dynamics.** A cyclic Fourier source can be represented
as `V=C^M`, with shift `T`, and fiber report `C=A_q`. Then the very same
observation map `O_M=(A_q,A_qT,…,A_qT^(M−1))` is defined. If the source
shift descends, `A_qT=V_qA_q`, every `ker A_q` direction remains dark
and time alone does not reveal the omitted Fourier modes. If the descent
square fails, delayed probes can expose hidden directions. This connects
DF5 to T1 through actual linear maps, not a visual analogy. It does not
assert that every failed descent makes the system fully observable.

**Hankel map.** The source-to-history factorization is explicitly
`K_d:α↦Σ_j α_jT^j b`, followed by `O_d`. Their composition has matrix
`H_ij=CT^(i+j)b`. Rank is an observable linear dimension constraint,
not ontology, carrier identification or physical source provenance.

**Mellin/Fourier transport.** On `L²((0,∞),dx)`, define the unitary
log-coordinate map `(Uf)(t)=e^(t/2)f(e^t)`. For
`f∈C_c^∞(0,∞)` and unitary Fourier convention
`F g(τ)=(2π)^(-1/2)∫g(t)e^(−iτt)dt`, substitution gives

\[
 \mathcal M f(1/2+i\tau)=\sqrt{2\pi}\,\mathcal F(Uf)(-\tau).
\]

The scale action `R_a f(x)=e^(a/2)f(e^a x)` satisfies
`UR_a f(t)=Uf(t+a)` and
`M(R_a f)(s)=e^{a(1/2−s)} M f(s)` on this test domain.
This is an invertible transport with an everywhere nonzero multiplier;
it cannot create or destroy a fixed function's zeros. A weighted mixture
of scale actions can have multiplier zeros and changes the test source.
This is the precise distinction needed for the virtual Mellin model.

For the normalized self-Fourier Gaussian scale-pair test at scale `p`,
its existing multiplier is
`C_p(s)=(p^(−s)+p^(s−1))/(1+p⁻¹)`.
At true distinct prime scales 2 and 3, a joint zero would force
`t log2` and `t log3` both to be odd multiples of `π/2`, hence an equality
of nonzero odd integer powers of 2 and 3, impossible by unique
factorization. These inputs are source scales, not zeta-zero positions.
Replacing 3 by composite 8 breaks this control: with
`u=2^(s−1/2)`, the auxiliary equations have polynomials `u²+1` and
`u⁶+1`, whose exact gcd is `u²+1`. Composite and duplicate routes must
retain their common provenance, even if their outputs agree.

Matched non-Euler control: keep `a(2)=a(3)=1`, but change `a(6)`
from 1 to 2. Then the primitive mixed residual
`b(6)=a(6)−a(2)a(3)` changes from 0 to 1 while the same Archimedean
test multipliers remain available. Neither dynamic observability nor
the multiplier test authenticates the arithmetic source.

The conditional use of T4 in RH requires an independently derived
factorization from authentic prime-power/Euler data and the actual
completed Gamma/pole contribution, with conductor, additive phase,
half-density and test-space normalization. The log-coordinate half-density
above is a general analytic isometry; it is not that completed arithmetic
identification. These source/operator contracts and the separate
Weil-positivity sign theorem are absent here. No nontrivial zero positions
are read, no canonical zeta zero is located, and no RH conclusion follows.

## 10. Deliverables

- `DOSSIER.md`: quantified statements, complete local proofs, sharp
  countermodels, provenance, primary prior art and scope.
- `probe.py`: independent native stdlib-only scratch implementation;
  rational Gaussian elimination, row-span audit, a separate Leibniz
  determinant oracle, polynomial Euclidean gcd and a complete factorial.
- `RECEIPT.json`: deterministic raw exact outputs, source-anchor hashes,
  script hash, bounded resource contract, exclusions and nonclaims.

Reproduction from the assigned worktree root:

```sh
timeout 25s python research/2026-10-13/SWARM_ATLAS/E40/probe.py > research/2026-10-13/SWARM_ATLAS/E40/RECEIPT.json
timeout 25s python research/2026-10-13/SWARM_ATLAS/E40/probe.py --verify research/2026-10-13/SWARM_ATLAS/E40/RECEIPT.json
git diff --check
```

The probe imposes a 20-second CPU cap and a 256-MiB address-space cap.
The first executed probe completed with exit 0 in under one second.
Saved receipt verification and scoped diff validation are recorded in the
commit delivery report. Full repository validation/CI and independent
principal review are outside this bounded mission and are not claimed.

Only the new E40 directory is staged. Frozen archives, shared docs,
claim ledger, atlas registry and runtime modules retain their parent state.
