# Operation PRIOR FIELD — a causal inflation model with source priors, Oily Bayesian selection, and original-BBP counterexample

**Date:** 2026-10-28. **Repository:** `femboy2112/SUCC`. **Parent research head initially checked:** `f10632ee4c922c95256f80245284c752162dbe2d` (PR #344, Main XIII ancestor `b763ba8ef375fbac221e29e4396989a635a6ef36`). **Status:** classical mathematics and exact model-specific derivations; source-specific original signed BBP identities; independent Python/SymPy finite tests. **NOT:** a new cosmological prediction, demonstrated quantum field, universal epistemic defect, π-normality proof, RH proof, or proof that an ideal physical observer is compelled to use these priors. Original BBP forcing and U0=0 remain immutable.

## 0. The steelman and the missing pre-observation object

The user's proposal is an *ontologically modest* expansion of SUCC: model a virtual background as a rigorously defined probability law **before** any observer selects a history, allow the domain of source events to expand faster than the physical distance light could cross in one clock tick, and enforce finite-speed propagation along declared causal edges. An observer is itself a source/relay of causal reports. A realized path updates its **posterior distribution**; any *physical* alteration of the future probability kernel requires a declared intervention or feedback rule. Conditioning is not itself superluminal signalling or wavefunction collapse.

Define a source contract `(V,E,pi_0,K,a(t),O,F_t,sigma)` where `V` is a source-labelled directed acyclic graph of spacetime events, `E` its permitted local causal edges, `pi_0` the prior on initial source states, `K` a normalized parent-to-child stochastic channel, `a(t)` the declared metric scale factor, `O` calibrated source observation/probe laws, `F_t` an observer's sigma-field of *actually delivered* evidence, and `sigma` the immutable source identifier/initial-condition contract. These structures MUST NOT be conflated: growth of V, coordinate recession speed, local null speed, entropy of pi, observer receipt lag, and actual BBP signed phases are different observables.

### IPC-01: a genuine pre-observation probability measure

Fix the complete b-ary rooted tree; at root assign spin `Z_∅ ∈{-1,+1}` with `P(Z_∅=+1)=q`. Each edge, independently conditional on its parent, sends a binary symmetric channel with `P(child=parent)=(1+theta)/2` and `P(child≠parent)=(1-theta)/2`, `0<=theta<=1`. For any finite complete rooted subtree `V_≤n`, define the *full cylinder*:

`P_n(z_{V_≤n}) = pi_0(z_∅) product_(v→w in E_≤n) K_theta(z_w|z_v)`.

All probabilities are positive/nonnegative and normalize to one. Marginalizing all generation-(n+1) labels returns P_n exactly, because each edge channel sums to one. The consistent cylinder family therefore extends by Kolmogorov's theorem to a unique probability measure on the countable infinite rooted tree's product sigma-field (for the specified prior/channel). **This is a legitimate virtual-field prior**, not a fitted random replacement for the actual deterministic BBP source. The geometry alone does not determine q or theta. Setting q=1/2 is a maximum-entropy initial prior only relative to a declared binary reference grammar.

For a frontier observation `y` consisting of all leaves of depth n, the optimal posterior is the exact finite Bayes fraction:

`P(root=+|y)=q L_+(y)/[q L_+(y)+(1-q)L_-(y)]`.

The recursively evaluated likelihoods are defined at a leaf as `(1,0)` or `(0,1)`. For an internal parent with child-subtree likelihood pairs `(L_i^+,L_i^-)`, its own likelihood pair is

`L_+ = product_i [(1+theta)L_i^+/2+(1-theta)L_i^-/2]`,

`L_- = product_i [(1-theta)L_i^+/2+(1+theta)L_i^-/2]`.

This inference respects the source chronology; evidence not received cannot be used. Exact rational implementation and positive/negative controls in `observational_succ/causal_inflation_prior.py` and `tests/test_causal_inflation_prior.py`.

**No canonical prior theorem:** same tree, same K and observed leaf + with q=1/2 yields posterior 3/4 (theta=1/2, b=1); q=3/4 yields posterior 9/10. A causal diagram never uniquely selects the prior. More importantly, source labels and actual U0=0 cannot be replaced by an ensemble choice.

## 1. IPC-02: an exact legitimate Bayesian *observation* that creates the authentic Oily endpoint law

This is a source-specific improvement over merely juxtaposing Gamma(1) and Gamma(2). The authentic positive Oily source (already proved in Main XIII / PR #340) is

`R(x)=(1-x)L(x)`, `L(x)=1/[(2-x²)(x²-2x+2)]`, `0≤x≤1`, `L(1)=1`.

Use `m=8n≥0` for the source-time exponent (not to be confused with the cosmological scale a(t)). Choose **before receiving evidence** the normalized comparison prior

`p_(0,m)(x) = x^m L(x) / Z_(0,m)`, `Z_(0,m)=int_0^1 x^m L(x)dx`.

Define a *genuine binary observation event* `A` with source likelihood

`P(A | x)=1-x`, which lies in [0,1] for all x in the source domain.

Then Bayes' rule has the *exact* normalized posterior

`p_(1,m)(x|A)=x^m (1-x) L(x)/Z_(1,m)=x^m R(x)/Z_(1,m)`, 

where `Z_(1,m)=int x^m(1-x)L(x)dx`. The event probability is `P(A)=Z1/Z0`. By the change of variable `Y=m(1-X)` and Watson/Laplace localization at x=1, the prior tends to `Gamma(1,1)` and the posterior to `Gamma(2,1)`; `m P(A)→1`. The corresponding logarithmic moments converge, so

`D_KL(prior || posterior)→gamma`, `D_KL(posterior || prior)→1-gamma`, and symmetric Jeffreys divergence tends to **1 nat**.

These limiting KL identities are classical Gamma/digamma computations, but the exact Bayesian likelihood on the ORIGINAL rational L(x) is source-matched, bounded and testable. At m=256, independent high-precision quadrature on the actual L yields

`P(A)=0.00384681183247272693...`,
`D_KL(prior||posterior)=0.57533279763792581785...`,
`D_KL(posterior||prior)=0.42090342287291080694...`.

The limiting theorem is analytic, **not** a fitted extrapolation. A calibration source L≡1 gives *exact finite* `P(A)=1/(m+2)`; the time-dependent original L matters for finite values.

**Crucial unpaid premise:** The source's factor `1-x` is genuinely present, and the above event is a valid Bayesian observer. Nevertheless nothing yet forces a real ideal observer's sensor to implement `P(A|x)=1-x`, or selects the deflated prior among all admissible pre-observation priors. Alternative calibrated event kernels yield different posteriors. This construction proves *existence of a source-faithful prior-to-Oily posterior bridge*, not uniqueness or physical necessity. The original signed real BBP orbit is a DIFFERENT information type.

### The two-bit entropy law explains the *signed value* of this likelihood, but not the sensor itself

The earlier wavefront-oscillator work independently maximized entropy for **two** Bernoulli emitter microchannels with total mean occupancy x. This forces each to have activation probability `p=x/2`, under those declared constraints. For occupancy `B∈{0,1,2}`, the authentic Oily loop rates are the size-biased positive contributions

`1·P(B=1)=2p(1-p)=u=x−x²/2`, `2·P(B=2)=2p²=v=x²/2`.

There is also an **exact signed vacancy contrast**

`P(B=0)-P(B=2)=(1-p)²-p²=1-2p=1-x`.

Thus the same source grammar naturally produces the numerical function selected as the Bayesian likelihood in IPC-02. This is better structural evidence than an unrelated fitted shape. **However a signed expectation is not automatically an event probability.** Indeed suppose one tries to obtain the event solely by a fixed deterministic predicate on the two raw bits, with acceptance probabilities `a00,a01,a10,a11∈[0,1]` (the same contradiction also holds for fixed randomized acceptances). Then its conditional event probability is

`P(A|p)=a00(1-p)²+(a01+a10)p(1-p)+a11 p²`.

Matching `1-2p` as a polynomial for all `0≤p≤1/2` forces `a00=1`, `a01+a10=0`, **and `a11=-1`**, contradicting admissible nonnegative acceptance probabilities. Hence **no x-independent fixed two-bit sensor** can generate this precise event likelihood merely from the emitted bits. A lawful sensor of `P(A|x)=1-x` must use x/calibrated side information, additional randomness with a suitable joint source, or some other explicitly constructed mechanism. A separate uniform-auxiliary detector `A=[U≤1−x]` is valid but is *additional structure*. This is a concrete **probe gap**, and it marks the remaining physical/epistemic optimization cost. Exact exhaustive 16-event check and an independent symbolic coefficient proof are preserved in tests/oracle.

## 2. IPC-03: inflation with local c respected, distinct from superluminal signalling

Use the declared flat FLRW metric (in units c=1), in 3+1 dimensions:

`ds²=-dt²+a(t)²(dchi_1²+dchi_2²+dchi_3²)`.

In a radial direction a null signal obeys `|dchi/dt|=1/a(t)`. For a de Sitter-like exponential epoch `a(t)=exp(Ht)`, H>0,

`D(t)=a(t)|Δchi|`, `dD/dt=H D` for comoving observers.

Hence two distant comoving sources can recede at `HD>1` without any local particle/information moving superluminally. The **comoving null reach** between 0 and t is

`η(t)=int_0^t dt'/a(t')=(1-e^(-Ht))/H`, and `η(infinity)=1/H` if the exponential law continues forever.

This is a genuine kinematic horizon in an *eternal* idealized exponential geometry. If the inflationary epoch **ends** at finite T and a(t) remains finite constant thereafter, `∫_T^infinity dt/a(t)=infinity`: there is no such permanent event horizon purely from the finite episode. Nor is the Hubble sphere `D=1/H` generally identical to a causal event horizon in arbitrary evolving cosmologies. A sharp stop of a(t) is a piecewise kinematic control, not claimed to satisfy smooth Einstein equations without junction matter.

There is a separately declared **exact rational discrete approximation**: `a_n=g^n` for integer growth g≥2, with local tick reach `|Δchi_n|<=1/a_n`. Its horizon budget is

`η_N^disc=sum_(n=0)^(N-1)g^-n=(1-g^-N)/(1-g^-1)`.

This discrete sum is NOT the same as the continuous `η(t)=(1-g^-t)/ln g` (the difference is a sampling convention, not new physics). A causal b-ary tree can be *embedded in the declared discrete reach* by giving each child k of a source at chi the displacement `(2k-b+1)/(2b g^n)`, strictly under the speed bound; the number of descendants grows as b^n while each source edge remains local. For b=g=2 at depth 5, extremes are physical distance 31 apart in units a5=32, although each of the 62 root-to-leaf edges satisfies its local causal budget. That globally large separation does NOT prove faster-than-c transmission.

For a Pisot-labelled geometry, take `a(t)=phi^t`, `H=ln phi`. Its integer shadow is the Lucas recurrence `L0=2,L1=1,L_(n+2)=L_(n+1)+L_n`. With phi'=-1/phi, `L_n=phi^n+(phi')^n` and `L_n/phi^n-1=(-1)^n phi^(-2n)`. This connects a finite recursive integer scale to an exponentially expanding continuum scale, but the choice `a(t)=phi^t` remains an *assumption*, not a dynamical prediction of SUCC or Einstein's field equations. The earlier compact Hopf S4 is a distinct observer/gauge fiber, not a globally Lorentzian spacetime.

## 3. IPC-04: exact source-branching information inflation and threshold

The binary broadcast tree's b branches expand the number of latest-frontier reports as `b^n`. Each causal edge retains source spin correlation theta (`E[child|parent]=theta*parent`). The classical reconstruction transition for symmetric binary channel is governed by

`b theta² > 1` (reconstruction possible), versus `b theta² <= 1` (asymptotic frontier-only reconstruction impossible).

Source: Evans–Kenyon–Peres–Schulman (2000), and later binary symmetric critical refinements. This is **a classical theorem applied to a declared tree channel**; it is not a theorem about BBP digit statistics. At `theta=1/2`, b=2 has `b theta²=1/2`, and b=5 has `5/4`. For b=2, exact optimal Bayesian success from *only* current frontier leaves is:

| generation | leaves | optimum success probability | I(root;frontier), bits (numerical from exact finite likelihoods) |
|---:|---:|---:|---:|
| 1 | 2 | 3/4 | 0.3318777540066993 |
| 2 | 4 | 43/64 | 0.1411418037091551 |
| 3 | 8 | 10155/16384 | 0.06540117590045764 |

For census estimator `Z_n=sum_(depth n) leaf spins` and `C_n=Z_n/(b theta)^n` (theta>0), `E[C_n|root]=root`, and direct conditional-variance recursion gives

`Var(C_n|root)=(1-theta²) sum_(j=1)^n (b theta²)^(-j)`.

For b theta²>1, this is bounded; for b theta²<1 it diverges, and at equality it grows linearly. The finite variance is one explicit estimator criterion, not the whole below-threshold impossibility proof; that proof uses the cited broadcasting theorem. The equality case for arbitrary *nonregular* trees requires extra care; the threshold as stated is for the regular symmetric binary model.

**The observer-memory fork:** Let F_n be all receipts through generation n and G_n only generation-n leaves. `F_n` is nested; optimal Bayesian knowledge about the root cannot degrade as evidence is retained. But `G_n` is not nested, and root → G_n → G_(n+1) is Markov: current-frontier information can and does decay even as its cardinality explodes. Thus any thesis that ideal E1/E2 necessarily loses root information requires a **memory/receipt-discarding resource rule**. Geometry and branching alone do not supply it. If theta=1, descendants are exact copies and knowledge persists; if theta=0, no frontier descendants contain root information.

## 4. IPC-05: SUCC-authenticated Oily transfer has a distinct linear inflation threshold

Do NOT identify the binary channel theta with the Oily loop retention u,v without a separate proof. Here is a second, independent exact model that genuinely uses the source-authentic transfer matrix

`M(x)=[[u(x),1],[0,v(x)]]`, `u=x−x²/2`, `v=x²/2`.

At the authenticated endpoint x=1:

`M(1)^n = 2^(-n) [[1,2n],[0,1]]`, for all integers n>=0.

Declare an inflationary **replica** of this four-real-parameter linear response into b^n independent output slots, each carrying the same M^n response. The total squared Frobenius response is

`E_b(n)=b^n ||M(1)^n||_F²=(b/4)^n(2+4n²)`.

Therefore `E_b(n)→0` for b<4, `E_4(n)=2+4n²` grows polynomially at criticality because of the Jordan collision, and `E_b(n)` grows exponentially for b>4. This is a **new-to-SUCC exact source-based linear-amplitude comparison**. It is NOT a statistical tree-reconstruction threshold: M is not a binary stochastic transition kernel, and replicating outputs does not automatically grant independent data or create Fourier cancellation.

For actual binary replication b=2, even exponential creation of slots fails to preserve this linear response energy in the limit. The polynomial n² resonance cannot defeat the (1/2)^n decay.

## 5. IPC-06: an honest source-phase prior and finite receipt completion

The *actual* first eight chiral BBP source taps are signed `(4,0,0,-2,-1,-1,0,0)` and the full original source contracts each eight-shell by 1/16. Define a finite **epistemic prior** on which of the eight source phases an observer has not yet identified, without changing the original source phase zero. With the declared activity observation `1[tap!=0]` and ideal zero/nozero detection, the 8 cyclic activity patterns are distinct after five consecutive chronological receipts. Uniform prior over the eight hypotheses collapses to the correct phase after five lawful, exact source reports; other priors lead to the same identification when they give the true phase positive weight.

If each observation is further passed through a declared independent binary symmetric sensor with error `0<epsilon<1/2`, all eight phases remain statistically identifiable. The expected one-period log likelihood ratio favoring the true phase over a distinct phase at Hamming distance d is exactly `d(1-2epsilon) log((1-epsilon)/epsilon)>0`; by the strong law for repeated calibrated independent sensor errors, the posterior concentrates almost surely on the true finite phase. This is a genuine **Bayesian observer steady-state completion theorem**, not a BBP digit normality result.

**Measurement cost:** the *unpowered* source tap at index 8k+j is `c_(8k+j)=tap_j/16^k`. A sensor with fixed **absolute** detection floor delta>0 eventually reports zero under **all** phase hypotheses; it cannot indefinitely acquire fresh phase evidence. The noiseless/constant-error activity sensor at arbitrarily late times implicitly assumes infinite precision, continually scaling threshold, or a separately powered periodic oscillator. This is a hard observer-resource distinction the earlier waveform analogy could conceal. The pumped oscillator from PR #344 explicitly changes the source representation; do not conflate it with the genuine contracting coefficient sequence.

## 6. IPC-07: the original signed BBP reveals a decisive **prior-induced false positive**

Preserve the literal forcing

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`

and the genuine zero-seeded recurrence `U_n(0)=16 U_(n−1)(0)+r(n)`, `U_0=0`. To ask about *virtual* alternative initializations without changing the forcing, write `U_n(s)=16^n s+U_n(0)`. Put a declared **Haar prior** on initial phase `s mod 1`, without claiming it is the genuine original prior. Then for all n≥0 and fixed nonzero integer h,

`E_s[exp(2πi h U_n(s))]=exp(2πi h U_n(0)) int_0^1 exp(2πi h16^n s)ds=0`.

**This is cancellation across the ensemble (annealed), not along any specified path (quenched).** A fatal counterfeit to any claim that a prior-average zero proves normality is the exceptional same-forcing seed `s=−π/16` (mod 1). The literal BBP identity implies

`U_n(−π/16)=−sum_(j>=1)16^(−j)r(n+j)`.

The exact combined rational forcing passport is

`r(k)=(120k²−89k+16)/[(2k−1)(4k−1)(8k−7)(8k−3)]`.

For k>=2, the numerator is at most `120k²`, while the four denominator factors are individually at least `k,3k,4k,6k`, hence

`0<r(k)<=5/(3k²)`.

Therefore, for **every n>=1**,

`|U_n(−π/16)| <= [5/(3(n+1)²)] sum_(j>=1)16^(−j)=1/[9(n+1)²]`.

The phase then satisfies `|exp(2πihU_n(−π/16))−1| <=2π|h|/[9(n+1)²]`, and its normalized Weyl averages converge to **1**, not 0. Indeed the unnormalized sum differs from N by an absolute O_h(1) bound, because `sum_(n>=1)1/(n+1)²<1`. Thus **Haar ensemble phase cancellation coexists with a coherent nonnormal source path under the SAME forcing**. This is a rigorous named counterexample to promoting a “prior on possible wavefronts” into π-normality.

### Comoving original-BBP arithmetic inflation and source completion

The actual arithmetic successor also has expansion factor 16. Define the comoving state `A_n(s)=16^(−n)U_n(s)`. Then

`A_n(s)=s+sum_(k=1)^n16^(−k)r(k)`, so `A_n(s)−A_(n−1)(s)=16^(−n)r(n)>0`, and by the authentic BBP identity

`A_n(s)→s+π/16` with `0<π/16−A_n(0)<=1/[9·16^n(n+1)²]` for n>=1.

The companion *source* chiral transfer from Main XIII obeys `T^8=I/16` on all four rational dimensions. Hence

`16^n T^(8n)=I` for all n>=0.

This is an **exact source-derived comoving scale compensation**: macro BBP expansion 16 is dual to the eight-tap chiral contraction 1/16. It is a useful, rigorous arithmetic analogue of comoving rescaling and completion. It is NOT a physical FLRW metric, not a new theorem of signed Weyl cancellation, and no stochastic prior forces the actual original U0=0 source.

## 7. IPC-08: instantaneous *posterior* changes without causal signaling

Let root Z be uniform ±1 and two distant child reports A and B be conditionally independent binary symmetric copies with correlation theta. Prior `P(B=+1)=1/2`. After a local observer records `A=+1`, its posterior for the unobserved remote report changes to

`P(B=+1 | A=+1)=(1+theta²)/2` (for theta=1/2, this is 5/8).

That is a lawful information update from an initially correlated source. It sends no influence to B and does not change B's unconditional distribution. Physical transmission of the local result to a remote observer still requires a permitted causal message. This is an operationally important separation between *conditioned virtual possibilities* and *dynamical changes to the field*.

## 8. Claim ledger and hostile controls

| ID | Exact statement | Status | Falsifier / restriction |
|---|---|---|---|
| IPC-01 | Normalized, projectively consistent binary prior over expanding source tree; exact Bayes posterior | CLASSICAL / EXACT MODEL | Change prior q without changing geometry: posterior changes |
| IPC-02 | A legitimate event likelihood `1−x` transforms deflated original Oily prior into authentic positive Oily conditioned kernel; Gamma1/Gamma2 KL limits | PAPER-PROVED source-specific construction / classical KL | Not proof observer's actual sensor uses this likelihood; alternate prior/likelihood mutates result |
| IPC-03 | de Sitter-type global recession HD>1 coexists with local null `dχ/dt=1/a`; finite inflation alone creates no eternal horizon | CLASSICAL FLRW, declared kinematics | Treat physical recession as a local faster-than-c signal: refuted |
| IPC-04 | Regular tree binary symmetric frontier reconstruction phase transition bθ²=1 | CLASSICAL (EKPS and binary refinements) | Retained ancestors make evidence fields nested, so frontier-only loss inference fails |
| IPC-05 | Exact Oily endpoint replicated linear signal `E_b=(b/4)^n(2+4n²)` | PAPER-PROVED / exact rational probes | E_b is not mutual information, nor an original BBP Fourier estimate |
| IPC-06 | Original eight-tap activity has 5-receipt source-phase identification, with finite-resolution obstruction | EXACT FINITE / classical finite Bayesian consistency | Constant sensor fidelity at arbitrarily small source amplitudes requires declared gain |
| IPC-07 | Haar prior over original BBP seed gives ensemble Fourier zero, while seed −π/16 produces coherent circle path under same source | PAPER-PROVED exact source / counterexample | Discloses prior-vs-selected-Weyl gap; no original U0=0 normality proof |
| IPC-08 | Original BBP comoving `16^(-n)U_n(s)→s+π/16`; chiral compensation `16^n T^(8n)=I` | PAPER-PROVED authentic source and classical BBP identity | No physical metric inferred from arithmetic scaling |
| IPC-09 | Conditioned remote marginal shifts by θ² without causal transmission | CLASSICAL exact probability model | If no common latent source / θ=0, update disappears |
| IPC-10 | Causal geometry and maximum entropy uniquely determine original Oily observer retention and physical inflation | **UNVERIFIED** | Independent sensor calibration, source-induced scale factor, seed selection and full evidence budget still missing |

All claims explicitly inherit the least authoritative source premise. The source root prior, the channel theta, branching count b, event likelihood 1−x, sampling clock and metric scale factor are model choices. No physical source authentication or publication priority claim is made. In particular neither **S4 Hopf gauge curvature** nor compact circle/Pisot trace contraction is identified with Lorentzian spacetime curvature.

## 9. Validation / provenance / next verdict-changing probe

**Exact modules (stdlib Fraction):** `observational_succ/causal_inflation_prior.py`, `observational_succ/bbp_virtual_seed_prior.py`, `observational_succ/chiral_virtual_phase_prior.py`. **Tests:** `tests/test_causal_inflation_prior.py`, `tests/test_bbp_virtual_seed_prior.py`, `tests/test_chiral_virtual_phase_prior.py`, `tests/test_inflation_prior_source_bridge.py`. Source bridge checks compare to existing original Main XIII / PR #344 modules by exact values, not copied source-normality claims. **Independent symbolic:** `scripts/inflation_prior_sympy_oracle.py`, explicit modular BBP Haar integrals and rational forcing reconstruction. **Independent high precision:** `scripts/oily_bayesian_inflation_oracle.py`; analytic limit established separately by standard endpoint Laplace asymptotics. **Deterministic receipt:** `scripts/inflation_prior_exact_probe.py` / JSON receipt. Saved logs give actual local runs; never claim hosted CI until seen.

**Controls:** biased versus uniform root prior; θ=0 and θ=1; b=2/b=5 at θ=1/2; current frontier versus archived parent receipts; finite versus endless inflation; local edge-bound versus distant global recession; original L versus L=1 calibration; actual original U0=0 versus identical-forcing coherent U0=−π/16; independent source phase ideal sensor versus finite-resolution dropout; linear Oily transfer vs a probabilistic channel. Each tests a different assumption; no same-model Monte Carlo can replace independent authority.

**Next verdict-changing probe:** Derive the likelihood `P(A|x)=1−x` and deflated original prior `p0∝x^(8n)L(x)` from *independently calibrated causal probe and resource constraints* (not from simply reverse-engineering R), then identify a lawful, source/seed-retaining map to the expanding original BBP real carry phases. Show a signed cross-time discriminator that rejects the coherent changed seed, or retain the explicit UNVERIFIED boundary. Use a separately defined finite-memory budget if proposing an *unavoidable* causal knowledge deficit. The Pisot/FLRW geometry is a productive coordinate model but does not uniquely imply either of those remaining assumptions.

### References / attribution

- Davis and Lineweaver (2004), *Expanding Confusion*, PASA 21, 97–109, DOI 10.1071/AS03040: https://doi.org/10.1071/AS03040
- David Tong, *Cosmology*, §1 (FLRW and conformal horizons): https://www.damtp.cam.ac.uk/user/tong/cosmo/cosmohtml/S1.html
- NASA Cosmic Times, inflation and superluminal recession vs propagation: https://imagine.gsfc.nasa.gov/educators/programs/cosmictimes/educators/guide/1993/inflation.html
- Bass, *Stochastic Processes*, Kolmogorov extension theorem: https://doi.org/10.1017/CBO9780511997044.048
- Evans, Kenyon, Peres, Schulman (2000), *Broadcasting on Trees and the Ising Model*: https://www.cs.ubc.ca/~will/papers/noisytrees.pdf ; Ann. Applied Probab. 10, 410–433
- Jain, Peres et al., binary symmetric broadcasting threshold near criticality (original theorem quoted): https://people.lids.mit.edu/yp/homepage/data/isit2023_uniqbp.pdf
- NIST Digital Library of Mathematical Functions, Gamma/digamma/ζ identities: https://dlmf.nist.gov/5.4
- Baumann, *TASI Lectures on Inflation*, Bunch–Davies initial conditions (external quantum comparison only): https://ned.ipac.caltech.edu/level5/Sept19/Baumann/Baumann_contents.html
- Main XIII SUCC source: `research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md`, `observational_succ/rank_two_chiral_towers.py`, `observational_succ/bbp_natural_carrier.py`. PR #344: `research/2026-10-28/WAVEFRONT_OSCILLATOR_COMPLETION_AND_CAUSAL_INVERSE.md` and `observational_succ/wavefront_oscillator_completion.py`.
