# OPERATION ORBIT CLOCK GENESIS — a source-relative threshold for universal SUCC clocks and prime jets

**Research date:** 2026-10-17. **Parent:** `research/source-minimality-clock-carry-renewal-2026-10-17@3512c24bd582f8572d98bc0728d2cf947b7e7d2f`, draft PR #162 (stacked on PR #157). **Status:** elementary classical/conditional paper derivations, an independently coded second incidence route, exact finite executable falsifiers, and a corrected topological-observation boundary. **RH PROVED: NO.** This research does not change original Tate/Gamma/Weil/Suzuki source files, frozen archives, historical claim IDs, or main.

## Abstract and verdict

Within **rooted deterministic unary sources**, the exact existence of every pointed cyclic quotient is equivalent to the root's source orbit never repeating. That is a powerful but severe source premise: **the free ray is already isomorphic to the successor natural numbers as a unary dynamical system**, and no finite trajectory certifies its global injectivity. A mere constructed internal clock cannot replace a source-equivariant factor.

The **finite instrument route** is nevertheless constructive: a single permission to splice one fresh state into the edge returning to the root produces every finite rooted clock `C_m`, without a prime seed or a primality test. Rooted common products give the least period `L_N=lcm(1,...,N)` covering all clocks of size at most N. Its source-indexed capacity increment `L_N/L_(N-1)` equals `p` exactly at `N=p^k`, and equals `1` otherwise. Thus **the new information in a minimal global clock appears exactly at the true prime-power von Mangoldt jets**. This is a classical Chebyshev identity placed into a *lawful-instrument/source-factor* interface; it is NOT a new discovery of Lambda, zeta, or primes. An independent computation via divisor-poset Möbius inversion recovers the same impulses without using lcm or a prime oracle.

The **topological correction** is decisive: if source observations must be *continuous*, an injective infinite orbit is insufficient. A compact contraction gives a nonrepeating orbit approaching one fixed point; any continuous factor to a nontrivial finite clock is impossible. We characterize the exact missing separation condition using disjoint closures of modular residue subsequences. Even when all finite cyclic continuous factors exist, their combined map to `Zhat` need not be injective; a second example exhibits nontrivial hidden source fibers.

## 0. Source inventory and trust types

Source primitives: source state carrier `X`, actual transition `T`, root `x_0`, finite observation target `C_m`, potentially a topology on the orbit closure, and declared capabilities `construct_fresh_state`, `edit_transition`, `replay_from_root`, `combine_rooted_clocks`. These are **not** all consequences of the word SUCC. Only a lawfully authorized subset is available at each observer epoch. A source factor `q:X->C_m` must satisfy `q(x_0)=0` and `q(Tx)=q(x)+1 mod m` on its stated carrier. In the continuous regime it must also be continuous. A counter ticking autonomously is a new instrument, not automatically a source factor.

In the repo, PR #157 supplies the abstract free-word/prime-jet convolution and conditional affine braid; #162 supplies supernatural finite-clock cofinality, carry and CRT clock constructors, and the finite-replay no-ghost discipline. This round resolves a **strictly smaller special case** (rooted unary orbit factors) and builds a second concrete clock generator. The `SOURCE_MINIMALITY` claim supplement is unchanged; new disjoint prefix `OCG` is used to avoid the real `SM.MIN` versus `SM.SUZ` collision repaired in #162.

Classical prior art: finite unary automata and eventual periodicity; cyclic quotient factors and odometers in topological dynamics; Chebyshev `psi(N)=log lcm(1,...,N)`; divisor-poset/Dirichlet Möbius inversion and von Mangoldt function. See *Encyclopedia of Mathematics*, “Chebyshev function”; Wolfram MathWorld “Chebyshev Functions”; Nekrashevych, *Groups and Topological Dynamics* (odometer/inverse-limit chapters); and existing SUCC carrier documentation. No academic originality/priority is claimed without a distinct literature audit and peer review.

## 1. OCG-01: exact factor classification of rooted unary sources

Let `O={T^n x_0:n>=0}` be the **actual root orbit**, with any other unreachable ambient states excluded. For integer `m>=1`, let `C_m=(Z/mZ,+1,0)` be a pointed successor cycle. On a free orbit the *only possible* pointed equivariant map is `q_m(T^n x_0)=n mod m`. This map is well-defined if and only if

```
for all a,b>=0, T^a x_0=T^b x_0  ==>  m divides (b-a).
```

If some source state repeats, determinism makes the orbit eventually periodic. Let `a` be its first transient index and `d>=1` its least eventual period. Then the complete set of allowable quotient indices is **exactly the divisors of d**, since all returns eventually differ by multiples of d, and the minimal eventual relation `T^(a+d)x_0=T^a x_0` requires `m|d`. Conversely, when `m|d`, the phase function above is well-defined on all orbit states and equivariant.

If **no source state ever repeats**, every `q_m` is mathematically well-defined. Thus:

> **Theorem (rooted unary source threshold).** For a rooted deterministic unary system on the root orbit considered as a *set*, a pointed equivariant factor onto `C_m` exists for every finite `m` **iff** the root orbit is injective (free). When a finite eventual period `d` exists, only `m|d` occur.

This is classical elementary dynamics. The proof uses the *actual infinite law* when the orbit is free, not an extrapolation from a finite trajectory. For a physically finite-state deterministic source, eventual periodicity is inevitable, so a single finite source cannot itself have every finite cyclic factor.

**Causal/epistemic debt:** the free orbit `x_0,Tx_0,T²x_0,...` is itself already isomorphic to `(N_0,+1)`. Hence this is an exact structural answer **inside the rooted-unary grammar**, not a foundation for `N` from fewer than a genuine unending successor source. Neither a source label nor a hundred successful finite no-return tests pays the infinite premise.

## 2. OCG-02: finite data and free-ray shadows

For every finite observed prefix of length `H`, the finite cycle `C_(H+2)` has exactly the same `H+1` distinct chronological state labels before its later first return. Therefore a finite positive transcript cannot prove the global free-orbit hypothesis unless it includes a separately proved source invariant. The classifying witness may be a global strict order-valued monotone source potential `V(Tx)>V(x)` for **every reachable state**, but finitely sampled monotonicity does not verify that quantifier.

**No-ghost example:** an external true source `C_4` and a newly constructed independent instrument `C_5` have joint synchronized orbit length `20`, yet no pointed equivariant factor `C_4->C_5` exists (`5` does not divide `4`). The internal clock's period-five event is real *instrument state* and invalid as evidence that the external source had prime-five behavior. Merely renaming `C_4 x C_5` as the external carrier would be a source-map substitution.

## 3. OCG-03: a new finite-clock generator with zero prime seeds

Begin with the pointed one-state loop `C_1` whose sole arrow returns to root. For a connected pointed cycle `C_m`, let `v` be the unique predecessor of root. Authorize a **fresh-state splice**:

```
old edge:     v -> root
new edges:   v -> new ; new -> root
```

All other arrows remain unchanged. The new rooted orbit has exactly `m+1` distinct states before returning to root, so by induction `C_m` is constructible for every finite `m`. This is a finite-state machine theorem under the two declared operations: (1) allocate a fresh state, (2) rewire a return edge. The *new observer must be replayed* from the common source root; it is not claimed to be a quotient of the old clock.

**Critical obstruction:** For `m>=2`, neither `C_(m+1)->C_m` nor `C_m->C_(m+1)` is pointed successor-equivariant, because one period does not divide the other. At `m=1`, only `C_2->C_1` exists. Thus the splice builds **new independent clock instruments**; it does NOT create a nested inverse-limit tower by illegal consecutive reduction maps. The tower is assembled later through lcm-composite clocks, whose periods do divide one another.

Fresh-state allocation, editable arrows, root replays and unbounded repetition of this schema are **additional observer capabilities**. This is not an assumption that some finite E has already physically completed infinitely many splices.

## 4. OCG-04: minimal common clock and source-indexed jets

Suppose the observer has separately constructed and certified each period `m=1,...,N`. A single rooted cyclic observer `C_M` has pointed factor maps to **all** of them iff `m|M` for every `m<=N`. Thus the smallest possible `M` is

\[
 L_N=\operatorname{lcm}(1,2,\ldots,N),\qquad L_1=1.
\]

The root orbit of the simultaneous product of the clock observations has period precisely `L_N`. Unlike the full Cartesian product of all state sets, this rooted orbit is the minimal **synchronized** cycle. Its compatible reduction maps to `C_(L_(N-1))` are now honest quotient morphisms because `L_(N-1)|L_N`. The chain `C_(L_N)` is cofinal in all finite cyclic clocks (`m|L_m`), and its inverse limit is the universal procyclic `Zhat`, as a *mathematical object under the full construction schema*. This says nothing about an observer running infinity of machines in finite time.

Define the exact per-epoch dilation factor and information increment:

\[
 R_N=L_N/L_{N-1},\qquad \Delta I_N=\log R_N.
\]

For each ordinary metatheoretic prime `p`, the exponent of `p` in `L_N` is `e_p(N)=max{k>=0:p^k<=N}`. Comparing `N-1` and `N`, exactly one exponent increases by one if `N=p^k`; no exponent increases otherwise. Hence

\[
 R_N=\begin{cases}p&N=p^k,\\1&\text{otherwise},\end{cases}\qquad
 \boxed{\Delta I_N=\Lambda(N).}
\]

This is the **classical Chebyshev identity** `log L_N=psi(N)` and its elementary discrete difference. Its SUCC-specific application is to treat `R_N` as a **minimal superobserver's source-licensed incremental capacity**, rather than assume prime jets at input. It reproduces a zero at composite-six and a new logarithmic pulse at the prime-power eight; it does *not* assert a source-physical detector of `Λ` has already been operated.

## 5. OCG-05: categorical join-irreducibility isolates exactly prime powers

In the complete divisor lattice of `L_N`, arrows represent actual finite rooted clock quotients; the join is the lcm, and the bottom is the trivial period-one clock. A non-bottom period `d|L_N` is **join-irreducible** iff it cannot be written as `d=lcm(a,b)` with both `a,b` proper divisors of `d`.

Every `p^k` is join-irreducible: a proper divisor has p-adic order `<k`, and the lcm of two such proper divisors still has order `<k`. If `d` has at least two different prime factors, write `d=p^a u` with `u>1` coprime to p; then `p^a` and `u` are proper divisors whose join equals `d`. Therefore **the join-irreducible periods are exactly the prime powers**.

Their lowest-level instances are the genuinely primitive prime clocks. Higher levels are the *jet depth* and are not mistaken for new prime species. This is a categorical, source-indexed description of what the lcm capacity increments are detecting.

The finite Python engine determines join-irreducibility by exhaustive divisor/lcm comparisons, **not by a primality oracle**. It agrees with an independent calibration oracle over all periods through 120. A non-prime-power `C_6` can supply a direct new instrument but creates no new **joint observational distinctions** after `C_2` and `C_3` have been combined. An unobserved `C_8`, by contrast, loses one depth of 2-adic resolution and halves the minimal period for a horizon ending at eight.

## 6. OCG-06: independently recover exactly the same current by Möbius inversion

The rooted quotient category of finite cyclic clocks has Hom(`C_m`,`C_n`) singleton iff `n|m`, and no arrow otherwise (with pointed equivariance). Its incidence algebra has zeta element `1_{d|n}`, whose Dirichlet-convolution inverse is the classical arithmetic Möbius function `mu`:

\[
 \mu(1)=1,\qquad \mu(n)=-\sum_{d\mid n,\ d<n}\mu(d).
\]

With `log` interpreted as the additive logarithm of the *observed finite clock index*, the Möbius-transformed coefficient is

\[
 (\mu*\log)(n)=\sum_{d\mid n}\mu(d)\log(n/d)
 =\log\left(\prod_{d\mid n}(n/d)^{\mu(d)}\right).
\]

The usual divisor formula `log n=sum_(d|n) Lambda(d)` (prime-factor expansion, or telescope over the divisor-clock irreducibles) implies by Möbius inversion that the left side is `Lambda(n)`. Thus

\[
 \boxed{\prod_{d\mid n}(n/d)^{\mu(d)}=R_n,}
\]

**two differently implemented paths to the same exact finite observable**: (1) growth of lcm superclocks; (2) incidence inversion on the quotient diagram. The code performs the second route with only exact rational products and dynamically recovered Möbius coefficients, not `lcm`, Euler products or a prime oracle. The methods are mathematically dependent on the same divisor/order source; they are **not independent empirical witnesses** or a proof of source availability.

The derived finite Dirichlet polynomial is an exact symbolic logarithmic current:

\[
 \sum_{n=2}^{N}\frac{\log R_n}{n^s}
 =\sum_{p\le N}\biggl(\sum_{k:p^k\le N}\frac1{p^{ks}}\biggr)\log p.
\]

On the classical genuine integer source, in the **strict half-plane `Re s>1`**, standard convergence gives its limit `-zeta'(s)/zeta(s)`. We explicitly do NOT substitute this divergent prime Dirichlet series at the critical line. This is a way to source the authentic arithmetic *input tape*, not a way to prove the completed **signed** Weil form positive.

## 7. OCG-07: exact observational state/memory lower bound

Any single connected rooted cyclic instrument simultaneously representing every clock `C_m` for `m<=N` needs at least `L_N` recurrent states. More generally, if a deterministic finite machine has compatible readouts for all these clocks on one recurrent orbit, the joint output has period `L_N`, so that orbit must have period divisible by `L_N`: at least `L_N` distinct recurrent states. A symbolic program can of course describe this instrument with fewer **stored program bits**; the bound is about distinct dynamical states, not the Kolmogorov complexity of its description or a universal thermodynamic work cost.

There is an elementary quantitative lower bound, requiring no prime-number theorem. For `0<=k<=N-1`, use Legendre's valuation formula to write

\[
 v_p\binom{N-1}{k}
 =\sum_{j\ge1}\left(
  \left\lfloor\frac{N-1}{p^j}\right\rfloor
  -\left\lfloor\frac{k}{p^j}\right\rfloor
  -\left\lfloor\frac{N-1-k}{p^j}\right\rfloor\right).
\]

Every summand is either 0 or 1 and only `p^j<=N-1` can contribute. Hence `v_p(binomial(N-1,k))<=floor(log_p N)=v_p(L_N)`, so **every** coefficient `binomial(N-1,k)` divides `L_N`. The largest is at least the average of all N coefficients; their sum is `2^(N-1)`:

\[
 \boxed{L_N\ge\max_k\binom{N-1}{k}\ge\frac{2^{N-1}}{N}.}
\]

Therefore an exact finite physical/simulated joint clock requires at least `ceil(log_2 L_N)` bits of state capacity, and that is at least `N-1-log_2 N`. This is a **state complexity** bottleneck, not a blanket impossibility proof for mathematical construction, approximation, compression of *descriptions*, or human cognition. It explains why increasingly complete clock observation is exponentially costly in explicit state capacity even though each fresh clock is finitely constructible.

## 8. OCG-08: topological factor correction — free orbit is NOT enough

Let `(K,T,x_0)` be a **compact Hausdorff** rooted topological dynamical system: `T` continuous and the forward orbit of `x_0` is dense in `K`. For each `m>=1` define residue subsequences and their closures

\[
 K_r^{(m)}=\overline{\{T^n x_0:n\equiv r\pmod m\}},\qquad 0\le r<m.
\]

**Theorem (continuous cyclic-factor criterion).** There is a continuous pointed successor-equivariant surjection `q_m:K->C_m` iff the `m` closed sets `K_r^(m)` are pairwise disjoint.

**Proof.** If `q_m` exists, on the dense root orbit it must equal `n mod m`, so continuity places each `K_r^(m)` inside the disjoint closed fiber `q_m^{-1}(r)`. Conversely, if the closures are pairwise disjoint, their finite union is `K`, so they are a disjoint clopen partition. Declare `q_m(x)=r` on `K_r^(m)`. This is continuous, surjective and correct at the root; by continuity of `T` and density of the orbit, the equivariance equation holds on all `K`. Uniqueness follows from density. QED.

If this holds for every `m`, uniqueness ensures every divisor bonding square commutes. The universal continuous map

\[
 \pi:K\to\varprojlim_m C_m=\widehat{\mathbb Z}
\]

is surjective: its compact image contains the dense nonnegative-integer orbit in `Zhat`. It is a **homeomorphic conjugacy** iff these finite quotient maps **jointly separate every pair of source points**. A **factor** is not the same as an isomorphism of the source.

**Hostile contraction:** Take ambient `[0,1]` with `T(x)=(1+x)/2`, root `0`, and let **`K={1-2^{-n}:n>=0} union {1}` be the compact orbit closure**, not the entire ambient interval. The root orbit `1-2^{-n}` is strictly increasing, injective and converges to the fixed point `1`. For every `m>=2`, every `K_r^(m)` contains `1`. Hence no nontrivial continuous cyclic factor exists even though the abstract root orbit is free. The finite engine gives arbitrary exact close pairs with different residues; the global no-factor theorem is analytic, not a conclusion from those finite pairs.

**Hostile hidden-fiber:** Take `X=Zhat x [0,1]`, `T(z,u)=(z+1,(1+u)/2)`, root `(0,0)` and `K` its orbit closure. Each projection `q_m(z,u)=z mod m` is continuous and equivariant, so `K` has all finite clocks as a **factor**. But the limit point `(0,1)` lies in `K` because `j! ->0` in `Zhat` and `1-2^(-j!) ->1`. It is distinct from root `(0,0)` yet every clock factor assigns both residue 0. Thus the canonical `K->Zhat` is not injective. The code keeps `2^(-j!)` *symbolic* so astronomical powers never masquerade as executed finite arithmetic.

**Source consequences:** Abstract clock existence, continuous observation and faithful source reconstruction are **three different claims**. The proof-access vector must keep source law, availability of a continuous readout, observer resolution, and faithfulness distinct. An infinity of nominal moduli does not certify the source has no additional hidden coordinates.

## 9. Falsifiers, exact runs, and bounded evidence

Modules are standalone stdlib, source-gated and fail closed:

- `observational_succ/orbit_clock_genesis.py` — rooted graph trace, actual factor law, fresh-state splice, minimal lcm clock, prime-power jet clocks, exact symbolic current and state-cost lower bound.
- `observational_succ/clock_incidence_inversion.py` — source quotient incidence Möbius algorithm, independent product reconstruction, malformed quotient-arrow control.
- `observational_succ/topological_clock_factors.py` — rational contraction finite precision adversary and profinite-factor/hidden-coordinate witness (global topology is paper proof).
- `tests/test_orbit_clock_genesis.py`, `test_clock_incidence_inversion.py`, `test_topological_clock_factors.py` — exact targeted controls.
- `scripts/orbit_clock_genesis_probe.py --verify` — deterministic pinned finite source result with explicit `RH_proved=false`.
- `research/2026-10-17/ORBIT_CLOCK_GENESIS_RECEIPT.json`, this paper, claim supplement, and dedicated workflow.

**Local focused run:** 45/45 stdlib tests, including exhaustive 1,728 tiny source/morphism instances; independent lcm and incidence agreement through 300 and an exact source budget check. Full repository CI status depends on the exact pushed commit and must not be represented green unless verified on GitHub. Exact finite checks do not prove the infinite topological/source claims; the proofs above do.

Negative controls: source `C4` vs new internal `C5`; malformed eight-state machine with true period four; false clock quotient `C_(m+1)->C_m`; absent period `C8`; redundant period `C6`; non-prime-power injection; deleted `C6->C2` quotient arrow; missing divisor coefficient; topological contraction despite injective orbit; profinite factor with hidden fiber; finite source budget; forged rank/precision; no zero-reading.

## 10. Acceptance ledger, remaining debt, and the next verdict-changing probe

| Question | Verdict | Precise remaining source debt |
|---|---|---|
| Can a rooted unary source admit every **set-level** finite cyclic factor? | **CLASSICAL / conditional** iff no state ever repeats on the root orbit | Global no-return, not finitely observed |
| Can one fresh-state clock-splice compiler generate all finite **instrument** clocks without prime labels? | **PAPER PROVED** inductively; EXACT FINITE TESTED | Permission, memory/cost, independent source replay; does not certify source factors |
| What exact new primitive information is needed at period N? | `Lambda(N)=log(L_N/L_(N-1))`, **CLASSICAL / PAPER PROVED** | Full actual period schema; not an observed physical arithmetic field |
| Can two distinct mathematical routes reconstruct the same prime current without a prime oracle? | **PAPER PROVED + EXACT TESTED** (LCM and divisor incidence) | Shared quotient lattice; not independent source evidence |
| Does free orbit force every finite **continuous** factor? | **REFUTED** by compact contraction | Need disjoint residue closures for each m |
| Do all continuous clock factors force source to be `Zhat`? | **REFUTED** (hidden fiber) | Need joint point separation |
| Does the source-constructed Lambda tape prove RH? | **NO** | Need original full signed Weil form and source-derived positivity; open |

**Next discriminator:** Replace the *declared* free-ray or full clopen-factor law with an **independent source invariant** available to a finite observer that proves global no-return or global modular residue separation, with explicit error/probe and causal budget. A bounded monotone witness is possible (the contraction!), but must be evaluated together with observation continuity. If no such verifiable source invariant exists for the proposed environment, classify an **access-gap / contextually saturated** finite-observer boundary, not a logical impossibility of mathematics. Keep any claims of novel RH positivity completely separate.
