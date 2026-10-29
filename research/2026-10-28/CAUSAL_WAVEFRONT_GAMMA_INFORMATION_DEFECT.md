# Operation SUCC — One-step causal frontier, Pisot null frames and the Euler/Gamma information defect

**Research date:** 2026-10-28. **Integration target:** draft `research/pisot-hopf-arithmetic-relativity-2026-10-28`, branched from Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`. **Scope:** exact finite-speed 1+1 causal model; declared discrete/continuous clock pair; KL information comparisons of authentic positive Oily endpoint source; finite rational and high-precision controls; no source modification, no physical experiment, no new π-normality or RH theorem.

## 0. Motivation and corrected mathematical reading

The user proposes: an ideal observer who maximizes causal acquisition, beginning one step behind a universally advancing wavefront, cannot access the frontier or exceed the speed of causality; an Euler–Mascheroni/Oily-like normalization defect may survive at the knowledge boundary, with structural analogies to uncertainty and causal horizons. In a fixed observer frame, one may compare other frames through legal transformations, while causal ancestry stays invariant.

**Steelman:** construct an observer-relative *causal/epistemic boundary* and ask whether an unavoidable nonzero numerical invariant survives (i) changes of reference frame, (ii) changes of clock discretization, (iii) causally permissible adaptation, and (iv) source-preserving countermodels. **Do not identify a null coordinate with measured proper time, entropy with a spacetime metric, a temporary wavefront with a black-hole event horizon, or an SU(2) Hopf gauge curvature with Riemann curvature.**

### Existing SUCC foundations recovered (do not duplicate)

- `research/2026-10-12/COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md`: exact Lorentz examples, invariant causal ancestry, observer-specific simultaneity cuts (CV1–CV2), causal evidence downsets (CV7), and frame-dependent receipt rates (CV9). This already handles the noncommutativity of epistemic frames separately from physical boosts.
- `research/2026-10-13/SUZUKI_FIRST_PRIME_WAVEFRONT.md`: genuine first prime-power interaction threshold at `2a=log 2`, with compact Hilbert–Schmidt norm tending to zero but a source-derivative operator norm remaining nonzero. An independently derived boundary regularity cost grows like inverse window squared. This is a *spectral* prime wavefront, distinct from the causal-front metaphor below. It should not be silently conflated with light cones.
- `research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md`: lawful quotient/descent requires fiber congruence and preservation of source-labelled action sequences, not a purely pictorial map.
- `research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md`: authentic Oily kernel `R(x)=(1-x)L(x)` and Gamma(2) endpoint scaling; center dependence of proposed golden/Gamma offsets is explicit. Original signed BBP source and zero seed are separate and immutable.
- `research/2026-10-28/pisot_relativistic_geometry/ARITHMETIC_RELATIVITY_DOSSIER.md`: harmonic/log mixed-frame square has nonzero sampling defect but closes under a common clock potential; Hopf SU(2) curvature is mathematical gauge curvature, not gravity; compact S4 is not globally Lorentzian.

## 1. Causal boundary: exact 1+1 order and one-step observer

Set units with maximal causal propagation `c=1`. Events are integer pairs `(t,x)`; `(s,x)\preceq(t,y)` if and only if `t>=s` and `|y-x|<=t-s`. This **declared** poset is a sampled Minkowski light-cone order; it is not SUCC's actual physical spacetime. Let the rightmost frontier at time t be `f_t=(t,t)`.

Take ideal frontier-following tracker `o_t=(t,t-1)` for `t>=1`. It obeys:

`f_t \not\preceq o_t`; `f_(t-1)\preceq o_t`; `f_t\preceq o_(t+1)`.

Thus a current frontier innovation cannot have been observed at the same instant, although the previous frontier can have been received. It follows that **current inaccessibility is not a permanent horizon**: frontier information is obtainable at later events. A true event horizon is a boundary defined relative to the entire future of a declared worldline (or future null infinity in the black-hole case), not a snapshot visibility cut.

For any tracker with initial coordinate gap >=1 and at most one cell of outward progress per tick, the gap never decreases. Constant gap exactly 1 requires outward speed exactly 1 **at every tick**. In continuum Lorentz geometry, such a path is *null*, not a timelike worldline of a massive observer, and it has no physical proper-time clock. The null tracker is a useful extremal observer *model*, not a physical ideal consciousness. If speed is bounded by `v<=1-epsilon`, the gap grows at least `epsilon*t`. This is the essential `c` boundary; `c` is not “infinite speed” in a unit-free sense.

## 2. Knowledge defects: what can and cannot be universal

Fix a source law for frontier values `Z_t`, a causally accessible observation history `\mathcal F_(t-1)` and an adaptive probe/report budget. A natural, *model-relative* uncertainty is

`K_t=H(Z_t | \mathcal F_(t-1),\text{all lawful reports})`.

If `Z_t` is a fresh independent fair bit, `K_t=1` bit even for the maximally informed past observer. If `Z_t` is perfectly predictable from the known source dynamics/past, `K_t=0`. With an independent biased Bernoulli(p), `K_t=h_2(p)` for any value in [0,1]. Therefore the universal proposal `K_t >= gamma` (or any positive fixed constant) for *every* causal source is **REFUTED** by the deterministic model. A horizon separates *available evidence* from *unreceived evidence*, not necessarily known from unknown outcomes.

For a fresh uniformly distributed `m`-bit frontier and **at most `k` binary bits** of lawful report, the information budget implies the exact Shannon inequality

`H(Z|report) >= m-k` (clipped at zero),

with equality when the report reveals k independent source bits. This bound is an information-theoretic analogue of limited observation capacity. It is **not** a Robertson/Heisenberg uncertainty inequality: such a claim would require specified noncommuting self-adjoint observables in a genuine quantum state, not merely a noncommuting SU(2) gauge product.

## 3. One source of Euler's gamma: a concrete asymptotically lightlike pursuit law

Start at the same declared time/position: wavefront `F(0)=0`, observer `O(0)=-1`. Set the smooth comparison velocity

`v(t)=1-alpha/(1+t)`, for `0<alpha<=1` and `t>=0`.

It remains strictly subluminal at every finite t, but approaches c=1. The continuously integrated lag is

`ell_cont(t)=F(t)-O_cont(t)=1+alpha log(1+t)`.

Now sample the **same** velocity law at the left endpoint of each unit interval: the kth discrete observer step has `v(k-1)=1-alpha/k`. The exact discrete lag becomes

`ell_disc(N)=1+alpha H_N`.

Both observer protocols begin at precisely the same event and both obey the causal speed limit. Their clock/frontier defects differ by the exact expression

`Delta_alpha(N) = ell_disc(N)-ell_cont(N) = alpha[H_N-log(N+1)]`,

hence

`lim_(N->infinity) Delta_alpha(N)=alpha*gamma`.

For `alpha=1`, Euler–Mascheroni appears *exactly* as the residual discrepancy of a discrete near-null pursuit clock against its integrated continuous counterpart, with the same original position. Both individual lags diverge logarithmically, but their difference converges. This is a source/clock-dependent **Euler discretization defect**, **not** physical time dilation. For general alpha the constant is `alpha gamma`; alternative speed profiles, sampling conventions, and continuous clock potentials give different defects. There is no unique maximally timelike tracker with speed strictly less than c, since velocities arbitrarily near c have no greatest member.

## 4. A second mathematically exact gamma: KL between neighboring Oily endpoint orders

The **authentic original positive Oily source** on `0<=x<=1` is

`R(x)=(1-x)L(x)`,
`L(x)=1/[(2-x²)(x²-2x+2)]`, with `L(1)=1>0`.

Construct two explicitly declared, normalized endpoint laws at `a=8n` (or any real `a→infinity`):

`dP_(1,a)(x) = x^a (1-x)L(x) dx / Z_(1,a)` (authentic Oily order-one source),
`dP_(0,a)(x) = x^a L(x) dx / Z_(0,a)` (one-order-deflated **comparison**, not the authentic BBP forcing).

Scale the endpoint coordinate `Y=a(1-X)`. Standard Laplace/Beta asymptotics plus positivity and smoothness of L yield

`P_(0,a)(Y∈dy) -> e^(-y)dy = Gamma(1,1)`;
`P_(1,a)(Y∈dy) -> y e^(-y)dy = Gamma(2,1)`.

Both limits hold not just weakly but with the necessary logarithmic moment convergence for the following KL divergences. The densities differ by `g(y)/f(y)=y`. Thus

`D_KL(Gamma(1,1) || Gamma(2,1)) = E_Exp[-log Y] = gamma`,

`D_KL(Gamma(2,1) || Gamma(1,1)) = E_Gamma2[log Y] = 1-gamma`,

and their symmetric Jeffreys divergence is exactly **1 nat**. These are classical Gamma/digamma identities applied to the *authentic source's endpoint order*, and they supply a **coordinate-invariant information-theoretic constant** once both comparison distributions are declared. KL is invariant under one-to-one common change of variable, unlike differential entropy. **Neither KL direction by itself is a lower bound on the observer's current-future conditional entropy.** No causal identification of P0 as an actual observer's posterior and P1 as actual frontier outcomes has been established.

### Exact finite-a certificate, and a higher-order tower

For the simple *L≡1* control, the finite laws are Beta(a+1,1) and Beta(a+1,2), and (integer `a>=0`):

`D_KL(P0||P1)=H_(a+1)-log(a+2)`;
`D_KL(P1||P0)=1+log(a+2)-H_(a+2)`;
`J(P0,P1)=(a+1)/(a+2)` **exactly**.

All three follow by differentiating the ordinary beta integral; they are separately tested by exact Fraction harmonic sums (for J) and high-precision numerical calculations (for the logarithms). They tend to gamma, 1-gamma, 1.

For consecutive Gamma shape parameters `k,k+1`, the general formulas are:

`D(Gamma(k)||Gamma(k+1))=log k-psi(k)`;
`D(Gamma(k+1)||Gamma(k))=psi(k+1)-log k`;
`J=1/k` **exactly**.

With integer k, `psi(k)=H_(k-1)-gamma`. Hence Euler's gamma is a special but *not unique* endpoint-order remainder. This provides a testable generalization if SUCC exposes other vanishing source orders. It does not assert all arithmetic horizons have integer Gamma shape.

### Independent numerical check on the actual L(x), not merely L=1

`python scripts/oily_wavefront_kl_oracle.py` evaluates the ORIGINAL rational L(x) with mpmath precision 55 decimal digits. At a=256:

`D(deflated || authentic)=0.57533279763792581785...`,
`D(authentic || deflated)=0.42090342287291080694...`,
`J=0.99623622051083662479...`.

Errors to the predicted `(gamma,1-gamma,1)` are each decreasing in the sampled sequence a=8,16,64,256; numeric evidence is recorded, but the limiting theorem is from Laplace asymptotics, **not** from extrapolation of these four numbers. The comparison L is a deliberately mutated source order, so the agreement is structural, not evidence that the original BBP has a second physically realized causal observer.

### Golden and Oily–Macaroni remain one more selection step away

In the existing Oily endpoint branching grammar `G(z)=(2-z)^(-2)`, Galton–Watson extinction is `q=phi^-2` and survival is `phi^-1`. Combining this *model-specific* probability with the new source-endpoint KL constant gives the legitimate numerical equality

`Omega_OM = phi^-1 - gamma = P(branching survival) - D_KL(Exp(1)||Gamma(2,1))`.

It is a declared contrast between a probability and a logarithmic divergence (both dimensionless but semantically distinct), **not** an intrinsic universal law of horizons or original π carries. The source-to-real-causal-observer bridge remains unknown. Golden and KL use the same broader packet source, but the synthetic extinction model and the deflated baseline are additional choices.

## 5. An exact Lorentzian *frame* generated by a quadratic Pisot unit (not a gravitational field)

For `m>=1`, let `beta=(m+sqrt(m²+4))/2` be the quadratic Pisot unit solving `beta²=m beta+1`; its inverse is `(sqrt(m²+4)-m)/2`. Declare rapidity `chi=log beta`. Set `c=cosh chi=sqrt(m²+4)/2`, `s=sinh chi=m/2` and

`(t',x')=(c t - s x, -s t + c x)`.

The exact identity `c²-s²=1` preserves Minkowski norm `t²-x²` and causal order. In null coordinates `u=t-x`, `v=t+x`:

`u'=beta u`, `v'=beta^-1 v`.

Therefore the *wavefront* u=0 is invariant under the Pisot-labelled Lorentz frame map, but the coordinate separation of the observer from that wavefront, u=1, rescales by beta. For beta=phi, `c=sqrt5/2`, `s=1/2`, velocity `s/c=1/sqrt5`; for silver beta=1+sqrt2, `c=sqrt2`, `s=1`, velocity `1/sqrt2`. All are standard Lorentz boosts *parameterized by chosen algebraic constants*. SUCC has **not** derived such boost parameters from its BBP source or a physical observer, and the compact Hopf S4 remains an **observer/gauge fiber**, not a global Lorentzian event manifold.

## 6. Falsification / claim ledger

| ID | Precise claim | Status / boundary | Verdict-changing probe |
|---|---|---|---|
| WF-01 | In declared c=1 event poset one-step tracker cannot receive current frontier event | Exact elementary theorem; tracker is null-speed idealization | Allow faster/teleport edge: verify it breaks premises |
| WF-02 | Every lawful observer must have a positive current-frontier information defect | **REFUTED** by deterministic predictable frontier (zero conditional entropy) | Propose a restricted source axiom forcing innovations |
| WF-03 | Independent fair bit at every new frontier contributes one bit unknown to all causally lagged observers | Exact within stochastic source axiom, not BBP | Change to deterministic or biased bits and observe residual change |
| WF-04 | Harmonic pursuit vs same-start continuous integral yields `alpha gamma` | Exact classical asymptotic, source-defined clock law | Shift alpha/profile/integration to expose nonuniversality |
| WF-05 | Original Oily order-one endpoint vs deflated order-zero comparator has limiting reverse KL=gamma and forward KL=1-gamma | Classical Gamma KL + positive-source Laplace theorem | Change kernel endpoint order; KL shape changes |
| WF-06 | Quadratic Pisot rapidities yield exact Lorentz boosts and rescale null wavefront separation | Classical Lorentz algebra; chosen rapidities | Compare with non-Pisot rapidity: same Lorentz algebra, no privileged physical link |
| WF-07 | Hopf SU2 curvature supplies gravitational event-horizon curvature | **UNVERIFIED**, no metric/Einstein equation or event-to-fiber physical identification | Construct an independent Lorentz metric and curvature measurements |
| WF-08 | These laws imply the authentic BBP signed Weyl cancellation or π normality | **UNVERIFIED** (no source-selected phase estimate) | Prove all fixed-h signed sums o(N), rejecting changed-seed controls |

**Source tests:** `tests/test_causal_wavefront_gamma.py` has 13 focused standard-library tests. `scripts/causal_wavefront_gamma_probe.py` emits a JSON finite sample. `scripts/oily_wavefront_kl_oracle.py` is an independent mpmath numerical oracle using the exact authentic positive kernel. No Lean theorem/hosted CI authority is claimed here.

## 7. Recommended transport after PR review

Keep the *physical/categorical* types separate:

`CausalEventPoset -> Future/receipt downsets -> Observer evidence`,

`CausalEventPoset (optional local Lorentz coordinates) -> frame cuts`,

`Authentic BBP (r(n), U0=0) -> phase/carry histories`,

`Chiral Q(i)^2 -> quaternionic Hopf S4 observer fiber (NOT quantum matter)`,

`Oily R(x) -> Gamma2 endpoint KL vs declared Gamma1 deflation`.

There is **no current arrow** from `causal event poset` to Oily `x` that would make the KL a literally necessary causal-information gap. This is the highest-value next mathematical probe. Attempt to construct a source-labelled Markov/observation kernel whose observer past conditional law is the declared deflated P0 and whose frontier conditional law is the authentic P1, with a lawful causal action and correct initial seed. It should fail on the deterministic-frontier model and the same-forcing changed-zero-seed BBP control unless extra true source data are used. A visually persuasive sphere/lightcone diagram is not sufficient evidence.

### Literature and exact prior art

- Leslie Lamport, *Time, Clocks, and the Ordering of Events in a Distributed System* (1978), DOI 10.1145/359545.359563; causal partial orders and observer-relative clock cuts are classical. https://lamport.org/pubs/pubs.html
- NIST DLMF §5.4(ii), digamma identities `psi(1)=-gamma`, `psi(n+1)=H_n-gamma`. https://dlmf.nist.gov/5.4
- Matt Visser, *Physical observability of horizons*, Phys. Rev. D 90 (2014) 127502, https://doi.org/10.1103/PhysRevD.90.127502 . Finite-lag wavefront is **not** a black-hole event horizon.
- SUCC main: `research/2026-10-12/COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md`, `research/2026-10-13/SUZUKI_FIRST_PRIME_WAVEFRONT.md`, `research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md`, `research/2026-10-28/pisot_relativistic_geometry/ARITHMETIC_RELATIVITY_DOSSIER.md` (proposed in same research branch).
