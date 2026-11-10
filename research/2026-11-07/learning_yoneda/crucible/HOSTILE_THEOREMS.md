# Hostile independent crucible

Status: classical specializations, one source-specific extension of a known
finite-observation obstruction, exact finite receipts, and a small Lean kernel.
No new original-zero signed cancellation estimate is established here. These
are a separate same-model reasoning bearing and an independent implementation
path, not independent scholarly verification.

## C-1. Transcript-only memory with later side information

Let H be a finite declared family of histories, t:H→T the accessible transcript,
p:H→P the later projected physical state, and a:H→A the requested answer. The
memory encoder must be m:T→M: it cannot inspect unobserved history or future
physical state. A decoder is d:P×M→A with

    d(p(h), m(t(h))) = a(h) for every h in H.

This exists exactly when a is constant on each fiber of (p,m∘t). Necessity is
substitution. For sufficiency choose any history representing each realized
(p,m) pair and return its answer; fiber constancy makes this well defined.
Nothing is required on unrealized pairs unless a total extension is requested.
If two histories have equal t and p but different a, no transcript-only memory
can work, regardless of its size.

After rejecting this last obstruction, join transcript values u,v when some
histories with these transcripts have the same p and different a. Exactly the
proper colorings of this graph are valid memory encodings. Thus the minimum
number of memory states is its chromatic number; fixed-width bits are its
ceiling binary logarithm. This is the **existing classical O65 theorem**, already
implemented in `observational_succ/interobserver_channels.py`, not a new theorem
or a new category. This dossier reuses that solver.

### Original-forcing C5 realization

For e=0,…,4 and j=0,1 let the candidate initial seed be

    s_(e,j) = (e/5+j)/16 = (e+5j)/80.

All ten seeds are distinct, one is zero, and each follows the unchanged four
BBP poles. A declared finite lookup probe at time zero returns t=e+j mod 5.
At time one the source-corrected circle state is

    p={U_1(s)-U_1(0)}=e/5.

The target is j. Each physical fiber contains exactly two histories. Nevertheless
adjacent vertices e and e+1 must get different memory codes, giving C5: two
codes are impossible, while (0,1,0,1,2) works. The exact memory requirement is
three states/two bits, not one bit inferred from the size-two physical fibers.

This is a declared finite source family and lookup probe. It does not supply a
physical sensor. Only one member is the authenticated literal-zero source; the
other nine are changed-seed controls. If the initial seed is already known to
be exactly zero and the full dynamics are known, its history is mathematically
fixed and this finite identification problem disappears. Computational access
to consequences is a separate resource.

`ConditionalMemory.lean` proves fiber consistency iff a decoder on realized
pairs exists, the hidden-conflict obstruction, and the explicit C5 binary
impossibility/three-symbol witness. It does not formalize BBP, arbitrary graph
chromatic optimality, asymptotic analysis, or π normality.

## C-2. Adaptive finite bounded-noise protocols admit periodic counterfeits

This extends #542 APH-02 from a fixed finite pin scan to arbitrary finite adaptive
protocols. It is an **instrument-identifiability obstruction**, not an arithmetic
normality advance. Assume the unchanged four-pole recurrence, candidate family
all real seeds, and α=π/16. The known Green identity is

    U_n(s)+T_n=16^n(s+α),       T_n→0.

Fix any deterministic policy. Along its truthful zero-source branch it makes
finitely many observations j=1,…,m, at finite times t_j. At step j its chosen
probe is f_j with values in a normed vector space and a known finite Lipschitz
constant L_j for either the real lifted coordinate U_(t_j) or the circle phase.
The admissible readout error has norm at most ε_j>0. Probe choice and memory
updates may depend arbitrarily, even discontinuously, on the preceding reports.
No continuity of the policy is assumed. An exact independent seed-attestation
channel is **not** included in this observational model.

Choose p such that, for every j,

    L_j 16^(t_j) / (2(16^p−1)) < ε_j.                 (C2)

Let β_p=k_p/(16^p−1) be a nearest grid point to α, and set s_p=β_p−α.
Then |s_p|≤1/[2(16^p−1)], hence

    ||f_j(U_(t_j)(s_p))−f_j(U_(t_j)(0))|| < ε_j.

For a circle probe use the circle-distance bound instead; it is no larger than
the lifted displacement. At the first observation choose the allowed error on
the counterfeit so that it returns the zero-source report. The policy therefore
chooses the same second probe/time. Repeat inductively: every report, every
policy choice, every memory update and every terminal output is identical.
This proof uses the finitely many probes actually selected on that shared
branch; it does not need a uniform Lipschitz bound over the entire policy tree.

The completed counterfeit orbit is periodic because 16^p β_p=β_p mod 1. Its
raw forced orbit has the same limiting finite atomic orbit measure since T_n→0,
so it is nonnormal. Its initial seed is nonzero because π is irrational.
Consequently no finite terminal normality certificate based solely on this
positive-error transcript can be sound for every admitted real seed while
accepting the authentic transcript. This does **not** obstruct a proof using
the exact formula and literal zero boundary: that exact extra input excludes
s_p. It also does not apply to arbitrary discontinuous exact sensors, a finite
candidate family that excludes s_p, infinite observation, or a statistical
confidence claim with a specified noise law. The errors here may be adversarial
and correlated; independent random errors are not assumed.

For coherent circle oscillators f(x)=exp(2πihx), L=2π|h|. Thus the theorem covers
phase-preserving adaptive Fourier measurements, not just passive scalar pins.
Unlimited classical memory cannot remove the common-transcript obstruction.

### Authentic-source finite receipt

The oracle uses seven adaptively selected unwrapped linear probes, each with a
positive rational error budget, and the **actual** α interval from the original
BBP Green tail. It certifies the nearest integer k_p by an interval strictly
inside one rounding cell. It then bounds the irrational seed difference by the
interval endpoints. It never substitutes a rational approximation for α or for
the counterfeit seed. The receipt proves existence of one bounded-error common
transcript. No randomized experiment or physical observation is claimed.

## C-3. Ranked surviving claims and refuted shortcuts

1. **Survives, source-specific obstruction:** C-2, including adaptive policy and
   arbitrary finite memory, under its precise positive-error and access model.
2. **Survives, classical finite learning:** source-correct transcript filtering,
   target descent, C-1 conditional memory, strict adaptive advantage under the
   existing finite two-step resource contract. The old implementation's replay
   is credited to `adaptive_proof_policy.py`, not claimed as new.
3. **Survives, existing exact source transport:** unwrapped source identities,
   Green-tail enclosure, temporal alias and original-forcing recurrence tests.
4. **Refuted:** closed source-corrected loops select the seed. For every seed,
   U_(n+d)−16^d U_n is the same forcing sum. The coherent seed s*=−π/16 obeys
   all these identities, while |W_A(h)−1|≤2π|h|/[15(A+1)^2] for fixed h.
   Its limiting law is δ_0. The oracle uses the completed β=0 model and rigorous
   tail bounds; it never calls a rational seed a numerical version of s*.
5. **Refuted:** finite phase resolution plus adaptation certifies normality.
   C-2 supplies same-forcing periodic completions. The counterfeits change the
   seed and do not refute the literal-zero target.
6. **Refuted:** Fourier magnitudes reconstruct the law. Uniform measures on
   {0,1,4,6}/12 and {0,1,3,7}/12 have identical integer autocorrelation counts,
   hence identical Fourier magnitudes at every integer mode, but differ and
   are not translates or reflections. Complex phase remains load-bearing.
7. **Refuted:** a rotating-gauge marginal reflects source mixing. For x_n=0
   and gauge a_n=n/M, each complete M-step observation grid is uniform while
   the source-decoded joint character exp(2πih(y_n−a_n)) is identically one.
   #525 supplies the stronger all-horizon irrational block-rotation example.
8. **Refuted:** 2-adic Haar and a zero boundary imply real Haar. The inherited
   shadow H(n)=n/(2n−1)^4 has zero initial value, is a 2-adic isometry, and tends
   to zero in the real topology. Its forcing H(n)−16H(n−1) is **changed** and
   the suite explicitly checks that mismatch. The genuine four poles remain
   indispensable; no cross-place real-character estimate is inferred.
9. **Refuted:** calibration at a source lattice alone supplies Haar. With
   p_d=1/16 except p_2+=1/64,p_3−=1/64, the Bernoulli CDF obeys
   F_p(1/[2·16^k])=1/[2·16^k] for all k, but repeated-digit probability is
   129/2048>1/16. This is a finite exact ingredient of the inherited CB-3
   mechanism, **not an independent proof of its whole nonstationary theorem**.
   The actual #524 CB-3 proof requires a varying calibrated p(τ) and a uniform
   concentration argument. It remains an inherited read-only paper theorem.
10. **Refuted:** Haar-seed ensemble L² estimates select zero. The character
    polynomial W_(A,h)(s)=A^(-1)Σ e(hU_n(0))e(h16^ns) has L² norm A^(-1/2)
    for every forcing by orthogonality. Point evaluation on its A-dimensional
    frequency space has norm √A; the gains cancel. The coherent same-forcing
    seed supplies a nonvanishing point evaluation. Learning the exact selected
    source does not alter this operator fact or establish its arithmetic sum.
11. **Refuted:** mutated source equations authenticate the original source.
    Replacing coefficient 4 by 5 keeps a valid affine recurrence and its own
    corrected loops but fails the original equation already at n=1. The exact
    source signature must be checked independently from generic naturality.

Seed 1/5 itself is **not** used as a known nonnormal BBP counterexample. A
rational seed shift can preserve all Weyl magnitudes. Periodic controls here
are specified in the completed β coordinate and therefore have seed β−π/16.

## C-4. Infinite extension: four separate failure receipts

Compatible finite source certificates yield an infinite source only under a
valid compactness/closedness theorem (or an appropriate finitely branching
history theorem). Main already contains these results as O650–O652 and
`formal/EODCS_CambrianRealization.lean`; this dossier does not recreate them.

- **Noncompact source:** on discrete H=ℕ, the closed conditions h≥N have every
  finite intersection nonempty and total intersection empty.
- **Missing closedness/continuity:** on compact H=[0,1], the sets (0,1/N] have
  the same failure. They can be observational fibers for discontinuous probes;
  continuity to Hausdorff report spaces is one sufficient closed-fiber condition.
- **Inadequate original source class:** eventually-zero binary tapes realize
  every finite prefix of an alternating infinite tape, but that limit is not
  eventually zero. Compactifying the ambient tape space proves existence in a
  larger class, not source correctness in the declared original class.
- **Wrong target quantifiers:** an arbitrarily long uniform finite digit prefix
  has an eventually-zero nonnormal continuation. Even a valid global-history
  realization theorem does not turn existence of a source into a uniform bound
  on all its future Weyl epochs. Such an asymptotic property needs its own proof.

The oracle's finite examples check witness arithmetic only. The empty infinite
intersections and eventual-zero limits are established by the arguments above,
not by finite enumeration.

## Provenance and audit boundary

`source_reads.json` records exact commits and SHA-256 digests of inspected source
files. Primary read-only inputs: #518 countermodels; #522 history/ensemble proofs;
#524 CB-3/LS/H2* proof; #525 gauge proofs; #527 2-adic shadow; #542 learning and
anchored paths with code/tests. Existing main O65 and adaptive/proof-access
machinery are dependencies, not independent new discoveries. The Lean file is
newly checked here with exact axiom output. The graph solver and source engine
are independently cross-checked by exhaustive binary assignments and a literal
four-fraction unwrapped recurrence respectively.

κ is mathematical formula contact; φ is finite-toolkit survival or the stated
paper proof; σ includes source/seed/phase tags; ρ risk is controlled by retaining
explicit failures. Same-model agent agreement is not counted as scholarly
independence. No physical measurement, all-epoch source cancellation, LS, H2*,
π normality or RH proof is claimed.

Next useful discriminating theorem: a source-selected signed estimate that
requires the exact zero boundary and cannot be reproduced by the periodic
bounded-error clones. Better observation alone leaves this estimate unpaid.
