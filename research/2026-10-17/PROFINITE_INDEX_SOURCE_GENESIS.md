# PRIME GENESIS II — derive the prime jets from finite clock indices instead of assuming an affine braid

**Research date:** 2026-10-17. **Scope:** classical procyclic-group and Haar mathematics with an exact bounded finite cyclic observer. **Status:** conditional structural theorem, exact finite countermodels, independently preserved source assumptions. **RH proved: NO.**

## 1. Why this is a different proof route

The first PRIME GENESIS dossier shows a precise theorem: a collision-free free prime-jet source becomes the natural-number ordered multiplicative monoid if its **global uniform-dilation-count (UDC)** law holds, and one separately normalized additive-real unit cell fixes logarithmic scale. But UDC is equivalent to the affine braid and is **not** a consequence of abstract Euler/prime jets. The finite countermodel `q_3=9/2` even has the first real unit cell correctly calibrated but breaks affine rank transport.

A stronger **existing SUCC source candidate** is not an arbitrary jet system. It is the finite-clock/Pontryagin tower of a single additive successor-group loop, culminating in the **full** procyclic profinite group:

\[
 G=\widehat{\mathbb Z}=\varprojlim_{m\ge1}\mathbb Z/m\mathbb Z\cong\prod_{p}\mathbb Z_p.
\]

This is already in `research/2026-10-15/EDGE_CARRIER_RECONSTRUCTION_LAB.md`, `research/2026-10-15/ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md`, and `observational_succ/pontryagin_source_duality.py` / `edge_carrier_reconstruction.py`.

**Declare the source map carefully.** The inverse system of *every finite cyclic quotient* is stronger than a finite observer and already carries much ordinary integer group arithmetic in its construction. This is therefore a **relative reconstruction of multiplicative natural-number arithmetic from a profinite source**, not a foundational derivation of set-theoretic naturals without any integer metatheory. It must not be represented as independent evidence for RH or as a physical completion accomplished in finite time.

## 2. PIG-01 — every open subgroup of universal procyclic G is nG

**Theorem (CLASSICAL / proved here from the source presentation).** Every open subgroup `U` of `G=Zhat` is uniquely `nG` for an integer `n≥1`, with finite quotient `G/nG ≅ Z/nZ` and index `[G:nG]=n`.

**Proof.** The ordinary integer subgroup `Z` is dense in the profinite group. For open U, its pullback `U∩Z` is a subgroup of Z, necessarily `nZ` for some n≥0. Openness gives a finite-index condition, hence n≥1. An open subgroup is closed, and the density of Z implies `U=closure(U∩Z)=closure(nZ)=nG`. The canonical projection to `Z/nZ` is onto with kernel `nG`, so `[G:U]=n`. Distinct n give distinct indices. QED.

Notice the quantitative source commitment: **all** moduli are required, not merely `p^k` for one fixed p, nor finitely many selected moduli.

## 3. PIG-02 — abstract primitive quotient species are exactly ordinary primes

Define a primitive jet label to be a **maximal proper open subgroup** `U<G`. Such a subgroup gives a finite simple quotient `G/U`, which is abelian because G is abelian. Every finite simple abelian group has prime order. Conversely, `pG` is maximal proper open for every prime p since `G/pG≅Z/pZ` has no proper nontrivial subgroup. Uniqueness of the subgroup of each index proves the bijection

\[
 \boxed{\{\text{maximal proper open }U<G\}\longleftrightarrow
 \{p:\ p\text{ is a positive rational prime}\},\quad U=pG.}
\]

**Crucially:** The primitive label is *selected by quotient simplicity*, not by running an integer prime oracle in the source reconstruction. The metatheoretic identification of finite simple cyclic quotient orders as primes is the classical theorem behind the construction. The finite `CyclicObserver` implementation enumerates genuine additive subgroups and chooses maximal proper ones by inclusion.

A fake independent `V_6` is rejected: the subgroup `6G` exists and has index six, but `G/6G≅C_6` is **not simple**, since `6G⊊2G⊊G` and `6G⊊3G⊊G`. The source can distinguish a composite subgroup from a primitive label before constructing its prime-power jet.

## 4. PIG-03 — multiplicative dynamics and scale from actual finite-place Haar

Normalized Haar measure `m_G(G)=1` gives for each open subgroup U

\[
 m_G(U)=[G:U]^{-1}.
\]

This follows from the disjoint partition of G into exactly `[G:U]` equal-mass cosets. Therefore the prime log clocks can be assigned from **measured subgroup mass**:

\[
 \boxed{q(U):=m_G(U)^{-1}=[G:U],\qquad
 \lambda(U):=-\log m_G(U)=\log [G:U].}
\]

This is a stronger *source law* than arbitrary positive frequencies. It rejects the global scale mutant `q_p=p^c` for `c≠1`: a primitive subgroup of index p has Haar mass exactly `1/p`, not `1/p^c`.

For finitely supported nonnegative primitive exponents α, form the subgroup

\[
 H_\alpha=\bigcap_{p} p^{\alpha_p}G.
\]

By Chinese remainder compatibility, `H_alpha=(∏p^{α_p})G`, with index

\[
 [G:H_\alpha]=\prod_p p^{\alpha_p}.
\]

The index map is injective on free primitive words and ranges over all positive integers. Injectivity is equivalent to unique factorization of the finite cyclic-quotient indices; it is not inferred from a bounded experiment. It follows that the prime-jet convolution exponential from PRIME GENESIS I produces the exact measure

\[
 \mu=\sum_{n\ge1}\delta_{\log n}.
\]

The rank-successor S on its ordered atoms is ordinary `n↦n+1`, and for each primitive subgroup of index p,

\[
 \boxed{V_p S=S^p V_p.}
\]

**This time the affine braid has been derived from group-index/CRT/Haar source laws**; it is not independently postulated as UDC. The log scale is fixed by the normalized finite Haar reciprocal-index law. Matching to the **separately** normalized real additive Haar `dx=e^t dt` yields every unit-cell measure equal to 1.

### What has been imported?

The source is the *universal* procyclic group  with the complete system of finite cyclic quotients , together with normalized Haar and its identified primitive quotient subgroups. It has enough inherent arithmetic structure to determine —rather than guess— the prime indices. Building this source from the original SUCC one-loop carrier uses an already available additive integer group completion and its full family of moduli. Therefore it does not prove that bare free FUCC jets force this structure. It supplies a **genuinely different sufficient hypothesis** whose arithmetic is explicitly licensed by prior carrier reconstructions.

## 5. PIG-04 — why finite cyclic observers cannot substitute for G

The finite cyclic source `C_m=Z/mZ` has one subgroup of each index dividing m. Its maximal proper subgroups have indices precisely the distinct primes dividing m. As a result, the source-produced generalized integer spectrum contains products of exactly those primitive indices (with unconstrained powers in the *abstract* FUCC completion), not all natural numbers.

Examples, exact in `tests/test_profinite_index_genesis.py`:

| Finite source | Primitive quotient indices | What it cannot infer |
|---|---|---|
| `C_64` | `{2}` | It sees only the 2-prime FUCC ladder, not all positive integers |
| `C_30` | `{2,3,5}` | No prime-7 source; value 7 absent even though 1 through 6 may appear |
| `C_210` | `{2,3,5,7}` | Reconstructs exact atoms 1..10, but 11 is invisible at next rank |
| Full inverse-limit `Zhat` | All ordinary primes | The full primitive spectrum is mathematically determined, **not physically traversed at any finite epoch** |

**Source-limit warning:** The abstract powers of a primitive at finite stage m should not be misconstrued as all actual distinct subgroups *inside C_m*: for instance, in C_64 the `2` subgroup powers eventually collapse. The infinite source has distinct `2^kG` for every k, while a finite chart tracks only those powers visible at its modular depth. The code constructs a free jet-system candidate from finite primitive indices, **not** a faithful infinite subgroup tower from one finite group.

**Negative-control theorem:** An observer sampling a cofinal-but-finite stage with modulus m cannot certify all later primitive indices. An unobserved prime q coprime to m is invisible. Absence of q within its current horizon is a probe-gap, not a proof of its global absence.

## 6. Exact implementation and falsification suite

New **additive** files:

- `observational_succ/profinite_index_genesis.py`: actual subgroup enumeration in a bounded cyclic group, inclusion-based maximal-subgroup discovery, reciprocal-index Haar check, and transfer to the independently implemented free-jet engine.
- `tests/test_profinite_index_genesis.py`: 10 focused exact tests across `C_64`, `C_30`, `C_210`, composite index six, altered Haar scale and finite horizon omissions. The model has no arithmetic-prime test inside its subgroup-discovery path.

Local isolated run: **10/10 tests passed (Python 3.13.5)**. The previous PRIME GENESIS tests (17) and their 56-source probe are separate evidence. No repository-wide suite is asserted to pass until the exact-head hosted checks are inspected. Executable finite tests do not prove all open subgroups of Zhat have the stated structure; the paper proof does that using the explicitly declared source.

## 7. Critical source-map dependency graph

```text
single additive successor loop
  -> group completion (classical Z)
  -> ALL finite cyclic quotient clocks (not one finite snapshot)
  -> full procyclic inverse limit G=Zhat
  -> maximal proper open subgroup U_p=pG
  -> p=[G:U_p]=1/m_G(U_p) (canonical finite Haar)
  -> λ_p=log p (declared reciprocal-Haar-to-real transport)
  -> free subgroup-index composites, CRT/unique factorization
  -> μ=exp_*(J/t) has atoms log 1,log 2,...
  -> rank-S and affine braid, now consequences
  -> normalized real additive Haar dx=e^t dt and unit gaps
```

**Potential circularity audit:** The first step's group completion already contains all signed successor exponents; the finite cyclic clock diagram indexes moduli using integer arithmetic. The last arrow is therefore a *structural recovery of multiplication and arithmetic measure*, not creation of Peano naturals ex nihilo. An independent physical empirical source for the full quotient system has not been supplied.

## 8. Next genuine moonshot

The open new mathematics is to **weaken the universal procyclic source axioms while still forcing the same index-to-log-to-rank coherence**, perhaps by reconstructing a full finite quotient spectrum from a lawful network of finite observers without presupposing all positive integer moduli as known labels.

Promising exact instruments:

1. A directed family of finite cyclic clocks with **cofinality certificate**: characterize when their observed primitive-index union exhausts *all* primes, and what finite evidence can or cannot certify cofinality.
2. A no-ghost causal inverse-limit theorem: show finite subgroup compatibility and source-preserving bonding maps give the correct completed G; reject a phantom full system assembled from inconsistent finite charts.
3. A source-indexed Haar comparison: derive real-place unit scale from the genuine adelic Poisson normalization without independently inserting `dx=e^t dt` as a numerical calibration after the fact. Keep additive and multiplicative Haar measures distinct.
4. Test transport through the genuine `StandardTateSource`; **do not** treat its positive Mellin source as the original signed completed Weil form. RH stays open.

### Claim labels

- **PIG-01/02:** Open subgroup and simple quotient classification — CLASSICAL / PROVED PAPER under the full procyclic source.
- **PIG-03:** Haar index, CRT subgroup-index multiplication and emergent braid — CLASSICAL / PROVED PAPER with explicit complete-source hypotheses.
- **PIG-04:** Finite subgroup experiment — TESTED EXACT FINITE; no global cofinality from finite controls.
- **PIG-05:** Bare prime jets force the full profinite source — REFUTED by altered collision-free Beurling primes.
- **PIG-06:** Empirical observer supplies physically certified all-cyclic quotient tower — UNVERIFIED.
- **PIG-07:** This route proves RH / Weil sign — NO, OPEN.

**Sources:** Existing SUCC carrier/profinite modules above; J. Neukirch, *Algebraic Number Theory*, Chap. II and classically standard profinite/Pontryagin/CRT mathematics; MIT 18.785 Number Theory I, lecture on profinite completions; Diamond–Zhang, *Beurling Generalized Numbers*, Ch. 3. Academic priority claims: none.
