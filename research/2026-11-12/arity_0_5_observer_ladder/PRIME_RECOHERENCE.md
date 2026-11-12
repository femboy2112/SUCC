# Prime-indexed entropy sinks? A bidirectional-twin crucible and source-map firewall

**2026-11-12 · draft research continuation of SUCC PR #604 · parent `83e4f4505efc9d0e702bb3230adeaaac8b2053af` (Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`).** New observer model only: frozen original four-pole BBP source and `U_0=0` untouched. No physical realization, independently checked novelty, completed Weil positivity, RH, Goldbach, R0 or π-normality claimed.

## 0. Steelman — two boundary roots, entropy gradient, middle rendezvous

The user proposes two initially separated and relationally entangled observers rooted at a source (0) and an ideal completion (infinity). Their causal paths through a larger mathematical/physical carrier may entangle their registers with the ambient environment, losing **relative coherence**; prime-sensitive transport might reverse distinguishability and allow the separated observers to regain one calibrated pure state when their **present outputs** meet in one transported frame. A schematic negative sign on the genuine prime-power contribution to the signed completed Weil form suggests seeking an *effective recoherence mechanism*, not automatically a physical reservoir or a positive theorem.

A source-faithful reconstruction must distinguish:

1. **Local purity of one observer** `Tr rho_A²`; **joint purity of the twin pair** `Tr rho_AB²`; total purity of the complete `ABE` closed state; and von Neumann entropy `S(AB)`. These are different quantities.
2. **Geometry and entropy:** distance or the position labels 0 and infinity do not force entropy. The nonnormalizable infinity boundary must be approached through declared finite cutoffs, not treated as a physically occupied endpoint.
3. **Prime source vs physical environment:** source coefficients `Lambda(p^k)/sqrt(p^k) = log(p)/p^(k/2)` with one completed Gamma, poles/contact and correct tests are arithmetic data. They are not physically calibrated quantum channels, negative thermodynamic temperatures, or energy sinks.
4. **Recoherence vs provenance:** a pure Bell return does not certify two correct source paths (`(U ⊗ conj U)|Phi_d> = |Phi_d>` from PR #604). Separate source and frame gates remain necessary.

## PRC-01 — zero-purity boundary cannot be literal for a normal state

For every density operator `rho` on `C^d`, `Tr rho² >= 1/d` by Cauchy–Schwarz on its nonnegative eigenvalues `lambda_i`, since `(sum lambda_i)^2 <= d sum lambda_i²`. Equality holds for the maximally mixed state. In any finite dimension, normalized density matrices **never** have zero purity; in an arbitrary separable infinite-dimensional Hilbert space a nonzero positive trace-one operator has at least one strictly positive eigenvalue and hence `Tr rho²>0`. Zero can be an **infimum or limit**, not the purity of a normal state.

The cutoff-entangled states `|Phi_d> = d^(-1/2) sum_(j=1)^d |j,j>` make the intended limit precise:

- `Tr rho_A² = Tr rho_B² = 1/d -> 0` and `S(A)=log d`, while
- `Tr rho_AB² = 1` and `S(AB)=0` for **every** d.

Thus taking a large completion cutoff can maximize local uncertainty *without* any joint loss of coherence. Mere separation has no effect in a tensor-factor model. No theorem identifies cutoff `d` with geometric distance or with arithmetic proof hardness.

## PRC-02 — independent prime buckets obstruct recoherence

For the balanced twin/environment state

`|Psi> = (|00>|e_0> + |11>|e_1>)/sqrt(2)`

with normalized branch environment states, set `gamma=<e_0|e_1>`. Direct partial trace gives

`P_AB=(1+|gamma|²)/2`, `F_(Phi+)=(1+Re gamma)/2`.

Suppose environment factors as independent prime-power sectors `E=⊗_(p^k) E_(p^k)` *and both conditioned branch states factor in that same tensor decomposition*:

`|e_a> = ⊗_(p^k) |e_(a,p^k)>`, so `gamma=Π_(p^k) gamma_(p^k)`,

where `gamma_(p^k)=<e_(0,p^k)|e_(1,p^k)>`. The product law is a direct consequence of the tensor-product inner product. If any factor has `gamma_(p^k)=0`, all other sector phases, signs and independent unitary rotations cannot revive the product overlap **while that orthogonal record remains**. Full revival `|gamma|=1` requires every factor to have unit-modulus overlap (for finitely many factors), and Bell target fidelity `F_(Phi+)=1` further requires the *total calibrated phase* to be +1.

**Verdict:** independent entropy sinks do not cancel which-path information; a **shared** environment, error correction with protected extra systems, conditional erasure/postselection, or a joint unitary uncomputing the record is needed. This no-go is conditional on tensor-factorized branch markers; it does not prohibit correlated cross-prime memory.

## PRC-03 — coherent shared environment can recohere without measurement

Use exactly rational unnormalized pure-state rays on three qubits `A B E`. Initialize `|000>+|110>`. Apply `R|0>=|1>`, `R|1>=-|0>` on E conditioned on A=1, where `R=[[0,-1],[1,0]]` (orthogonal). The resulting GHZ-like state has reduced twin purity `1/2` with zero branch overlap. Apply `R^(-1)` to E conditioned on B=1 (A and B agree within this code subspace); this **uncomputes** the environmental record and restores `(|00>+|11>)|0>` exactly, without any projective measurement, with twin purity 1 and target Bell fidelity 1.

Repeated identical R pulses give:

| Number of controlled R pulses | Branch overlap gamma | Joint AB purity | Phi+ fidelity |
|---:|---:|---:|---:|
| 0 | +1 | 1 | 1 |
| 1 | 0 | 1/2 | 1/2 |
| 2 | -1 | 1 | 0 |
| 3 | 0 | 1/2 | 1/2 |
| 4 | +1 | 1 | 1 |

**Key discriminant:** purity 1 at pulse 2 is **not** the calibrated Phi+ return. Coherence revival and correct phase selection require distinct tests. The *global* ABE pure state remains pure throughout. As ABE is pure, `S(AB)=S(E)` at every time; during this uncomputation both subsystems' reduced entropies decrease together as their mutual entanglement disappears. There is no negative-energy ledger or absorption of entropy by the environment inferred from this example.

## PRC-04 — positive-rate Markov sinks cannot effect revival

For an ordinary single-qubit Pauli-Z dephasing channel, `D_q(rho)=(1-q)rho+q Z rho Z` with `0<=q<=1/2`, the off-diagonal coefficient obeys `gamma -> (1-2q)gamma`; therefore `|gamma|` does not increase. Successive such channels cannot lift `gamma=0`. In the time-local GKSL dephasing model `dot gamma = -2 sum_j kappa_j(t) gamma`, where **all** `kappa_j(t)>=0`, `|gamma(t)|` is nonincreasing. An apparent negative *time-local dephasing rate* along a revival may indicate non-CP-divisible dynamics and environmental memory, not negative Hamiltonian energy. Our shared 3-qubit unitary is a constructive memory model. It does not extract negative entropy from any prime.

In particular, putting an arbitrary negative number into a positive-rate dissipator is not a legal quantum operation; even if its algebraic update temporarily reverses decoherence for a restricted input, one must verify complete positivity on **all** density matrices and the complete system–environment dynamics.

## PRC-05 — genuine prime-power support and the signed Weil firewall

For the authentic zeta Euler source, `Lambda(n) = log p` iff `n=p^k, k>=1`; otherwise 0. In one common completed explicit-formula convention the prime-power term enters as a **subtracted** weighted signed distribution, schematically

`Q_zeta(f) = (pole/contact/Gamma terms)(f) - sum_(p,k>=1) (log p)/p^(k/2) * (test values at +/- k log p)`,

where actual test domains, half-density, archimedean regularization and the entire Weil/symmetric form are essential. This should **not** be called a sum of physical negative energies. Sign conventions shift depending on which side of the explicit formula is named positive (SUCC `docs/CLAIM_SUPPLEMENT_COMPLETED_WEIL.md` and `docs/CLAIM_SUPPLEMENT_ARITHMETIC_META_WEIL.md`). Negative *quadratic contributions* can appear even if a total positive-form criterion holds. A negative form term alone is not a GKSL decay coefficient, a Hamiltonian energy eigenvalue, or an entropic sink. For RH, one still requires all-test completed Weil positivity, not an example of positive Gram or local Bell recovery.

Executable code checks **only** honest prime-power support, storing the authentic coefficient as the symbolic expression `log(p)/p^(k/2)` (no floating-point approximation). A freely chosen R pulse at n=2 and an identical pulse artificially labelled n=6 cause **identical quantum effects**; the fake-6 source gate rejects the latter only because the genuine Euler source is an additional arithmetic contract. The quantum operation itself cannot authenticate which event label was used. Four selected prime-power kicks (2,3,4,5) happen to return Phi+, exactly as any four identical kicks would. This is a **negative control** against claiming the source is responsible for the toy recoherence.

## PRC-06 — the specific missing bridge to SUCC/RH

A successful bridge would need **all** of:

1. A justified, preferably canonical, functor or fully declared interface from SUCC's source-labelled arithmetic path category (genuine prime-power `Lambda`, exact origin 0, phase/basis provenance) to admissible quantum channels/conditioned environments. No source-blind fitted rates or preinserted nontrivial zeta zero coordinates.
2. A causal, frame-aware two-observer rendezvous model that compares **present** outputs after transport; unknown past histories cannot be read directly across separated spacetime patches.
3. An actual recovery/retrodiction statement with positive/negative/null/mutation controls, accounting for **every** relevant environment record and allowing twin-correlated path errors (`U⊗conj U` stabilizer), not merely a single Bell click.
4. An exact identity between a source-derived signed functional and the completed Weil distribution on the *full admissible test-function domain* with correct pole, Gamma, contact, half-density, and physical/semantic type distinctions. Need demonstrate that the proposed overlap mechanism reproduces the **sign-indefinite** terms, not merely a positive surrogate.
5. A new valid global sign estimate beyond the all-test RH-equivalent positivity criterion, or a new source-selected signed π-normality/R0 bound, with hostile source controls. A quantum toy recovery that works for composite-6 or a nonnormal BBP counterseed cannot discharge either gate.

**Next highest-information probe:** try to construct a **single shared-reservoir environment** whose generator is forced by real prime-power source data, while the Archimedean/pole completion supplies independently calibrated boundary behavior; prove or refute that its source-first signed response equals the actual Weil/Suzuki form on two disjoint test supports. Use fake-6, wrong Gamma, wrong phase, wrong half-density, and coherent wrong-seed controls. If two supports already disagree, the bridge is REFUTED for that proposed map. If both agree, do not extrapolate from finite supports to an all-test theorem.

## Provenance and authority

Model and 19 exact stdlib hostile tests: `observational_succ/prime_recoherence.py`, `tests/test_prime_recoherence.py`. Existing SUCC controls: PR #604 `TWIN_RENDEZVOUS.md`, `RENDEZVOUS_CLAIMS.md`; `docs/CLAIM_SUPPLEMENT_COMPLETED_WEIL.md`; `docs/CLAIM_SUPPLEMENT_ARITHMETIC_META_WEIL.md`; `docs/CLAIM_SUPPLEMENT_PRIME_FORM_HEAT.md`; `research/2026-11-05/unit_pair_bell/THEOREMS.md` and `COUNTERMODELS.md`. Mathematical source convention checked against Weil positivity discussion in `openmaths.org/courses/NT-EXPF/NT-EXPF-02.html` (sign conventions depend on the formulation) and the classical Lagarias review; neither is a source for physical prime energy.
