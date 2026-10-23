# Carry the Truth: source-faithful renormalization

**Research date:** 2026-10-23. **Verdict:** exact carry repairs, sharp information
and norm obstructions, quantitative retained-memory heat renormalization, and a
critical half-density transport theorem. The original signed Weil four-mode
Schur bound did **not** improve. RH and named passive arithmetic cyclicity remain
open. No physical experiment or academic-priority claim is made.

This is the final research report for the supplied *Operation Carry the Truth*
plan. Complete theorem statements and proofs live in the linked manuscripts;
this report records their dependencies, authority, failures and consequences.

## Repository and validation state

The research parent is draft [#244](https://github.com/femboy2112/SUCC/pull/244),
head `5e2ba04c8b4ab627b6b0add588609c347346a1a2`. Main was checked at
`b116841f12b41aaf7600da39bbb40577f25b6295` and was not changed. Work uses
`research/source-faithful-renormalization-carry-2026-10-23`, stacked on #244.
The [live baseline](SOURCE_FAITHFUL_LIVE_BASELINE.json) records actual PR heads,
ancestry, source fingerprints and parent workflow evidence. #239 and #241 were
inspected as sibling comparison branches, not silently treated as ancestors or
merged. The other required source ancestors were checked. Historical imported
sources and their 72-entry provenance manifest are unchanged.

The untouched parent passed **6,825 tests**, as well as the required provenance,
observer-foundations and ordinal probes. Parent hosted CI had nine successful
workflows. New focused controls cover six modules: carry (38), limits (22),
memory (6), observers (15), resolvent memory (7), and Weil transport (24):
**112 exact tests**. The integrated candidate passed **6,937 tests** in the
full suite. Candidate validation is recorded separately in the
[validation receipt](SOURCE_FAITHFUL_VALIDATION.json), with raw logs and
executable hashes. Do not infer a hosted pass from local execution; exact-head
hosted results are linked in the draft PR.

The finite formal core consists of **22 Lean declarations** and **five rejected
false mutations**, checked with pinned Lean 4.14.0. The checker exports actual
theorem expressions and axiom dependencies; no `sorryAx` or unearned analytic
certification is used. The [local receipt](SOURCE_FAITHFUL_CARRY_LEAN_RECEIPT.json)
discloses the host's `/proc` path workaround, including its source and hashes.
The dedicated CI job reruns on a clean host without that shim and publishes its
own receipt. This formal core is not automatically admitted into any older
trusted claim registry. The analytic theorems below remain paper proofs.

Six research/audit lanes and a root integration pass were used. Agreement among
agents is not independent mathematical evidence. Independent algebraic routes,
source-preserving counterexamples, exact arithmetic, theorem-expression review
and actual compiler/test results provide the stated evidence instead.

## A. Theorems and exact scope

### Carry, norm and future information

[Carry manuscript](SOURCE_FAITHFUL_CARRY.md), §§1–8, proves on
`H=ell²(N>=1)` that `W_a e_[a(m-1)+r+1]=e_m tensor e_r` is unitary, transports
successor to the controlled carry action, and sends genuine multiplication to
`W_a V_a e_n=e_n tensor e_(a-1)`. Adjoints include the one-based zero boundary.
The residue isometries satisfy the Cuntz relations and
`U_(a,r) U_(b,s)=U_(ab,r+a s)`. Source-labelled regrouping is coherent for every
finite radix word; naive digit swapping is not that regrouping. These are
classical algebraic mechanisms with authenticated source labels.

For the uniform block isometry `J_a` and `A_a=J_a*`, every f satisfies

`A_a V_a f=a^(-1/2) f`,
`||(I-J_a A_a)V_a f||²=(1-1/a)||f||²`,
`||(V_a-J_a)f||²=2(1-a^(-1/2))||f||²`.

Keeping the complementary **coherent** environment gives a lossless map.
Measuring its sectors is a different channel. A complete instrument conserves
probability, while a postselected uniform amplitude alone does not. Under the
explicit step embeddings into `L²(R_+)`, genuine V_a converges weakly to
`a^(-1/2)D_a`, with limiting norms `||f||`; for a>1 there is no strong limit on nonzero
f. Position-probability probes can nevertheless converge. Uniform interpolation
`J_a` has the separate strong dilation limit. Every topology and embedding is
part of the statement.

The [observer manuscript](SOURCE_FAITHFUL_OBSERVERS.md), OBS-SF1–3, constructs
the coarsest stable refinement of a deterministic observation for arbitrary
carriers and total authorized action alphabets: two states agree exactly when
all future finite words give the same observation. Every sufficient stable
observation factors through it in the declared direction. For quotient
`q_a(n)=floor((n-1)/a)+1` and successor, full future equivalence is equality;
a fixed quotient requires a residual register of at least a states. At horizon
h it requires `min(a,h+1)` classes. The optimal carry protocol uses at most
`a-1` successor actions and `a` reads, with explicit calibration and cost.
Partial, probabilistic and quantum generalizations require separately stated
hypotheses; they are not consequences of a deterministic quotient alone.

For any contraction A, the closure of the range of
`D_A=(I-A*A)^(1/2)` is the minimal defect factorization. Composition of A then B
retains `(D_B A,D_A)`. The actual category is defined modulo environment-unitary
equivalence, and does not silently discard unused environmental sectors. It
supplies coherent defect bookkeeping; it does not equate physical access,
deterministic behavioral quotients and quantum instruments.

### Exact future memory and its quantitative heat effect

The [memory manuscript](SOURCE_FAITHFUL_MEMORY.md), M1–M3, proves for the
unilateral source, n=aq+r with `0<=r<a`,

`A_a S^n J_a=(1-r/a)S^q+(r/a)S^(q+1)`.

Thus `F_2-F_1²=-(S-I)²/a²`. For any bounded T and projection P, eliminating
`Q=I-P` gives the exact memory kernel `PTQ(QTQ)^jQTP`, with the explicit
initial-hidden-state term when needed. In the **bilateral/formal phase fiber**
`T_a(z)`, z≠0,1, the all-time scalar response of the uniform residue vector has
reduced generating-function denominator of degree a. Every finite-dimensional
time-invariant linear realization therefore needs at least a states; the carry
matrix attains a. At z=1 the minimum is one. This is not a theorem about arbitrary
nonlinear encodings, nor a spectral decomposition of unilateral successor.

[Clock/heat manuscript](SOURCE_FAITHFUL_LIMITS_HEAT.md), LH-09 and its
[resolvent supplement](SOURCE_FAITHFUL_RESOLVENT_MEMORY.md), prove a concrete
noncommuting limit and calculate the missing term. For bilateral nearest-neighbor
heat, `J_a*L_hJ_a=aL_(a h)`: compressing the generator then exponentiating gives
continuum `H_(a t)`, while compressing the evolved source gives `H_t`.
For fixed a≥2, coarse phase `theta=a h xi`, let

`r_h=u*(alpha+L_h(theta))^(-1)u`, `C_a=(a²-1)/12`.

For all alpha>0, h>0, xi real,

`|r_h-(alpha+xi²)^(-1)| <= h²[C_a xi²/alpha+xi⁴/(12alpha²)]`.

Writing the source fiber in visible/hidden blocks `[A_h B_h; B_h* D_h]`,
its exact Schur correction is `C_h=B_h(alpha+D_h)^(-1)B_h*`. If `|xi|<=R`,
`alpha in [alpha_0,alpha_1]`, `a h R<=pi` and `C_a h²R²<=1/2`, then

`|C_h-(a-1)xi²| <= h²[(a³+1)R⁴/12+2C_a R²(alpha_1+R²)]`.

The retained memory removes precisely the extra diffusivity. This is a complete
paper calculation for fixed radix, with independent exact two-residue matrix
and Schur checks. The bounded upper-alpha hypothesis for the memory conclusion
is essential; it is not needed for the preceding resolvent estimate.

### Two completions, heat density and classical Gamma recovery

The [clock/heat manuscript](SOURCE_FAITHFUL_LIMITS_HEAT.md), LH-01–09, gives
explicit local charts for factorial cycles. With epsilon=(k!)^(-1/2), radius-R
balls embed without distance wrap when `k! epsilon>4R`, with mesh error at most
epsilon. This proves pointed Gromov–Hausdorff convergence to R and controlled
finite words of rescaled translations and multiplier point maps. General
scales have line, circle, lattice or point subsequential limits as classified
there. Finite cyclic multiplication has norm `sqrt(gcd(p,N))` in the counting
representation, and is not genuine injective V_p.

The inverse-limit profinite topology uses different maps from these varying
geometric charts. Fixed discrete labels collapse in the blow-up; real
translations require varying successor powers. There is still no continuous
successor-equivariant map from compact Zhat to R with unchanged successor.
The diagonal rational source supports compatible character bookkeeping without
asserting such an impossible map.

For even N, L=N epsilon, c=4/pi² and heat density `h=P/epsilon`, the manuscript
proves the explicit local estimate

`|h(t,n)-g_t(x)| <= epsilon²/[32 sqrt(pi)c^(5/2)t^(3/2)]`
` + epsilon exp(-pi²t/epsilon²)/(2pi²t)`
` + [2/c+|x|sqrt(pi/(ct))]/L`.

It also supplies a rational conservative bound. Embedded semigroups converge
strongly by kernel convergence and a norm identity; Laplace integration yields
generalized embedded strong resolvent convergence. No operator-norm conclusion
is claimed. With Fourier convention `exp(2pi i x xi)` and freely chosen
`t=1/(4pi)`, the heat Gaussian is `exp(-pi x²)` and its Mellin integral gives
`Gamma_R(s)=pi^(-s/2)Gamma(s/2)` for Re(s)>0. This recovers classical mathematics;
it does not authenticate a physical unit or supply the completed signed Weil
source. Fixed nontrivial profinite conductor instead has diverging heat energy.

### Source-sensitive logarithmic transport and arithmetic calibration

The [Weil audit](SOURCE_FAITHFUL_WEIL_AUDIT.md), W-01–03, proves that a bounded
map J satisfying both `J V_p=U_(log p)J` and `J V_q=U_(log q)J` into any strongly
continuous one-parameter unitary group must be zero when p,q are multiplicatively
independent integers. Crowding of `(L+1)²` distinct addresses into O(L) logarithmic
bins supplies the contradiction. It applies to unweighted real translations
and normalized real dilations. One-generator and weighted targets evade those
hypotheses; the theorem is not a refutation of adelic trace constructions.

For nonzero compactly supported phi in L²(R), with support width L, the map

`J_(alpha,phi)a = sum_n a_n n^(-alpha) tau_(log n)phi`

extends boundedly from ell² exactly when `alpha>=1/2`. At the endpoint,
`||J||²<=(1+L)||phi||²`; there is no uniform lower bound on source norms. Genuine
commutators at prime powers recover `(log p)p^(-r/2) tau_(r log p)phi`.
The reflected contribution is included with the seed convention made explicit.
For a smooth unit-integral approximate identity `phi_epsilon`, this reconstructs
the authentic prime distribution in D', locally on test functions, while

`||phi||²/epsilon <= ||J_(1/2,phi_epsilon)||²`
` <= (1+epsilon L)||phi||²/epsilon`.

Thus the exact-resolution Hilbert cost diverges sharply. This is a source map
for the prime contribution, with its cost exposed; Gamma, poles, contact and
signed positivity are separate obligations.

The [observer manuscript](SOURCE_FAITHFUL_OBSERVERS.md), OBS-SF5, proves an
active parameter pin for the actual arithmetic K with sigma>1 under
`M=gK+bI`, g>0. From
`x=M_23=g lambda`, `y=M_13=g 3^(-sigma)`, `z=M_15=g 5^(-sigma)`,

`sigma=log(y/z)/log(5/3)`, `g=y 3^sigma`, `lambda=x/g`.

Six polarized energy expectations cancel the shared energy offset and extract
the entries; rational enclosures and unused prime-7/11 holdouts are supplied.
The offset b remains undetermined by these entries. Exact-mean mathematical
access is a premise, not a finite-shot experiment. Passive spectral cyclicity
at `(lambda,sigma)=(1,2)` remains open.

## B. Counterexamples and their receipts

| False identification | Smallest or decisive witness | Evidence |
|---|---|---|
| Present quotient predicts next successor | a=2, source addresses 1 and 2 | Carry basis proof; Lean finite core |
| One-step compression predicts every future | a=2,z=-1: moments 1,0,-1,0,... | Three exact memory routes |
| Fine sampling makes genuine V_a a smooth dilation | Norm defect `2(1-a^(-1/2))` on every unit f | Paper embedding theorem |
| Same character magnitude authenticates the source | Nontrivial phase/origin and broken mixed-radix twiddle | Exact cyclotomic controls |
| Affine law selects genuine primes | Composite 6 and fake primitive 4 | Source-generator and Dirichlet-log controls |
| A 2R circumference threshold makes radius-R charts isometric | Antipodal local pairs | 4R threshold and wrap control |
| Cyclic FUCC equals genuine injective FUCC | p divides N; colliding source basis vectors | Exact counting matrix |
| Compression commutes with heat evolution | Naive diffusivity a versus true 1 | Heat proof; explicit Schur repair |
| Memory limit uniform for all alpha>=alpha_0 | a=2, theta=2 arctan h, alpha=h^-4 | Rational formula; memory tends 0, target tends 1 |
| Two unweighted FUCCs fit one bounded real flow | Logarithmic crowding of p^a q^b | Universal no-go proof |
| A fixed half-density map stays bounded at exact resolution | Norm² asymptotic `||phi||²/epsilon` | Upper and lower proof |
| Same high norms imply same Schur sign | D=[[2,1],[1,2]], B=(1,±1): S=1/3 or -1 | Independent exact inverse |
| Prime support alone is positive | Genuine negative prime-two atom on declared autocorrelation | Exact signed-source interval |
| Every probe authenticates every mutant | Radius 1/2 activates no prime atom | Exact zero null control |
| Calibrated energy pin tolerates arbitrary entry offsets | Shared post-extraction entry-bias alias | Explicit parameter countermodel |

Inherited fully cyclic path/triangle aliases, source mirror domain failures,
nonstationary old Gibbs state and hidden thermal-sector obstructions remain
regression controls. They are not resolved by retaining a residue register.

## C. Source-preservation ledger

| Map | Preserved | Changed or lost | Topology / authority |
|---|---|---|---|
| Full W_a and labelled regrouping | Addresses, norm, all transported actions; histories when retained | No loss | Hilbert unitary; mathematical access only |
| Uniform A_a | Visible block response | Residues, future Markov closure, phase sectors | Contraction plus explicit defect |
| Full coherent defect pair | Norm and reconstructible source | Environmental encoding may change | Minimal factorization; unitary environmental equivalence |
| Measured residue instrument | Total probability, declared outcome records | Inter-outcome coherence generally lost | CP instrument, not the coherent map |
| Factorial blow-up charts | Fixed-radius geometry and finite-word action estimates | Fixed-label and inverse-limit topology | Pointed metric/strong embedded operator limits |
| Low heat fiber with exact Schur memory | True visible resolvent and low-frequency diffusivity | Source environment encoded as memory | Explicit fixed-radix error bounds |
| Half-density log synthesis | Genuine weighted addresses and prime coefficients | Norm fidelity and uniform inverse stability | Bounded at fixed resolution; distributional zero-scale limit |
| Original high-sector unitary change | Completed inverse correction and S4 exactly | No automatic tighter bound | Original domains/source required |
| Dropped high sector | Selected visible data | Positive inverse defect, phase-sensitive coupling | Wrong inequality direction for a lower Schur certificate |
| Three-entry arithmetic pin | Parameters within declared source/calibration family | Physical authority and passive cyclicity | Conditional exact/interval inverse theorem |

## D. Which hidden assumptions failed?

The principal failed assumption is that an exact present-time observation is
sufficient for every future lawful operation. The missing state can be stored
as a carry register or as a memory kernel; it cannot be deleted without changing
the process. A second failed assumption is that correct arithmetic addresses
imply a bounded, norm-faithful continuum transport. Unweighted log crowding
forbids that transport, and critical damping repairs only boundedness. A third
is that taking a valid continuum limit commutes with forgetting the environment:
the computed diffusivity defect shows exactly where it does not.

These are mathematical failures of particular equations, not claims that all
remaining obstacles are representational illusions. The original completed
signed source still poses an independent sign problem.

## E. Scholarly significance

Cuntz/polyphase identities, contraction defect dilation, behavioral equivalence,
minimal linear realization, projection memory, Bloch decomposition, classical
heat limits, Tate's Mellin normalization and Schur complements have established
prior art. The manuscripts link primary references and disclose retrieval
limits. This round supplies explicit source-specific formulations, proofs,
quantitative bounds, sharp counterexamples and executable controls. Priority
for the log-address threshold, common-flow obstruction and combined framework
has **not** been established; no new foundation of number theory is claimed.

The strongest project-level advance is that the formerly vague phrase “retain
the microscopic source” now has calculable costs and exact repair laws: sharp
future-state size, a nonvanishing norm defect, a reduced-denominator minimality
proof, a quantified heat-memory correction, and critical-resolution synthesis
cost. No broad category has been asserted to unify all seven research lanes.
The proved defect category and behavioral factorization have their own narrower
universal properties.

## F. What remains blocked?

The signed source file remains SHA256
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`.
No nontrivial zeta zeros were construction inputs. Genuine prime powers,
one-real-Gamma completion, both poles, contact and source conventions remain
authoritative. Seven signed mutants were actively separated where support
permits; support null controls prevent false authentication claims.

Unitary transport alone leaves `B D^(-1)B*` unchanged. Dropping an environment
omits a nonnegative inverse correction, which gives an upper Schur estimate,
not the lower estimate needed for positivity. The critical log synthesis has
not been mapped with all endpoint, moment, domain and completion conditions
into the original primitive high space. **No original S4 bound improved.**
Named passive cyclicity, physical preparation/measurement access, absolute
length and heat-time calibration, optimal growing-radix error bounds and
academic priority are separate open questions with different evidence needs.

## G. Single next verdict-changing theorem

The strongest next target is an actual improvement of the original directional
inverse bound, not another carrier analogy. In the original high space let
`D>=kappa I`, kappa>0, and use the existing low-source coupling convention
`B:C^4 -> H_high`. Construct from the regularized arithmetic source a finite
family `W_epsilon:C^k -> Dom(D)` satisfying the original endpoint and moment
constraints, set `Z_epsilon=(D-kappa I)W_epsilon`, and prove
`W_epsilon*(D-kappa I)W_epsilon>0`. Then certify on at least one declared original
low direction a strict, error-paid improvement over the #181 lower bound using

`kappa^(-1) B* Z_epsilon`
` [kappa W_epsilon*(D-kappa I)W_epsilon+Z_epsilon*Z_epsilon]^(-1)`
` Z_epsilon* B`.

This expression lower-bounds `B*(kappa^(-1)I-D^(-1))B`, the positive
inverse improvement over the scalar majorant, and hence improves a lower
Schur bound when its source/domain premises are met.
The general auxiliary-Gram inequality is inherited; constructing admissible
source columns with useful overlap and paid errors is the missing content.
Do not add #181 and #182 alternative corrections without a joint inequality.
The cheapest legitimate falsifier is an original low residual whose certified
overlap with the proposed Z columns vanishes, or whose source/domain/tail error
budget consumes the entire proposed improvement. This target is smaller than
first-window S4 positivity, which is smaller than the all-support Weil criterion.

[Claim supplement and authority map](../../docs/CLAIM_SUPPLEMENT_SOURCE_FAITHFUL_RENORMALIZATION.md)
· [hostile audit](SOURCE_FAITHFUL_HOSTILE_AUDIT.md)
· [deterministic exact receipt](SOURCE_FAITHFUL_EXACT_RECEIPT.json)
· [initial frontier contract](SOURCE_FAITHFUL_FRONTIER_CONTRACT.md).
