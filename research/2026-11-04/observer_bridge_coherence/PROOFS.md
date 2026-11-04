# Observer bridges, expanding counterexample searches, and Busy Beaver coherence debt

**Date:** 2026-11-04. **Scope:** SUCC observer/source/probe closure, and finite precursor to the selected π-current front. **Status:** classical computations, elementary exact rational theorems, and separately imported undecidability/compactness theorems. No RH or π-normality theorem.

## Source and proof access

The mathematical *metaresearcher* may know the real additive line `L=(R,+)` and an abstract topological circle group `C` as preloaded objects. To **avoid backdooring the desired bridge**, the embodied observer is **not** supplied a named quotient map `R -> R/Z`, an externally selected winding number, a hidden tag, or a true source identity. The metatheory may choose the standard chart `C ≅ R/Z` only to build and independently check candidate countermodels. If the observer is handed `C=R/Z` **together with its canonical quotient map**, it has been supplied part of the bridge as an axiom; this must be declared, not rediscovered from finite probes.

The original selected BBP arithmetic source remains unchanged:

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U0=0, U_n=16 U_(n-1)+r(n).`

All finite certificates here are exact Fraction/modular computations. Source observations are actual r(n) and original rational phase `{U_n}`. The true full real-circle selected current estimate and π base-16 normality are **OPEN**.

## OBC-01: finite line–circle probes cannot determine the global continuous group bridge

**Theorem (exact, universal finite rational probe sets).** Let `Q={a_i/d_i}` be any nonempty FINITE set of rational points, in lowest terms and with `d_i>0`, and put `M=lcm(d_1,...,d_s)`. Define two continuous additive group maps, in a metatheoretic circle chart:

\[
b_0(x)=[x]\in\mathbb R/\mathbb Z,\qquad
b_M(x)=[(M+1)x].
\]

For every `q_i` in the declared observations, `b_M(q_i)=b_0(q_i)` because `M q_i ∈ Z`. Both are continuous homomorphisms for **all real** `x`, and both intertwine the bare radix-16 dynamics:

\[
b(16x)=16b(x).\]

But at the explicit *new* probe `q_*=1/(2M)`, one has

\[
b_M(q_*)-b_0(q_*)=[1/2]\ne0.\]

The maps are genuinely different. They have different kernels (`Z` versus `(1/(M+1))Z`), so any theorem selecting the correct scale/kernel must pay an additional source-specific premise or a distinguishing probe. Testing homomorphism law, continuity, and commute-with-16 alone is insufficient even with unbounded algebraic verification: BOTH obey those laws identically.

This is a **probe gap** for a fixed finite observation language, not an infinite nonidentifiability theorem if the observer later probes *every* rational. In fact for each fixed wrong integer winding `c ≠ 1`, `q=1/(2|c-1|)` refutes it. The moving rivals `c_N=1+M_N` are allowed to change with `N`; this is the quantifier distinction.

**Important premise firewall:** Supplying the exact kernel `Z`, orientation, or a primitive winding of degree one as a *prior* would remove this rival. That could be a legitimate mathematical axiom, but claiming to have inferred it from finite experiments would be a backdoor.

### Original four-pole source supplies a genuine falsifying probe

For any fixed source horizon `N≥1`, take `Q_N` to be all original `r(j)` and `{U_j}` for `1≤j≤N`, and `M_N=lcm` of their reduced denominators. Both `b_0` and `b_(M_N)` agree on every actual **source** and **phase** observation through `N`, including every tested affine BBP arrow and all rational circle group laws.

To distinguish them within the *original* source (not an invented external test), take any prime `p≡1 (mod 8)` with `p>8N-2`; primes in this progression exist arbitrarily far by classical Dirichlet. Set `n=(p+7)/8>N`. The authentic source injection is

\[
r(n)=\frac4p-\frac2{p+3}-\frac1{p+4}-\frac1{p+5}.
\]

Every denominator through source time `N` has prime factors smaller than `p`, so `p∤M_N`. The new source has `v_p(r(n))=-1`, since the other three denominators are p-units for `p>5`. Consequently `M_N r(n)` is nonintegral and

\[
b_{M_N}(r(n))\ne b_0(r(n)).
\]

Thus **a lawful future source observation refutes the false bridge**. A computable search for a new prime `p≡1 (mod 8)` supplies a source-attested discriminator. This particular bridge search is NOT Busy Beaver hard; its falsifier is constructible by an effective algorithm. The exact test at `N=12` selects `p=97`, `n=13`, with no π digits as inputs. A source label alone is not the proof: both the first pole and the absence of other p-poles are essential.

## OBC-02: moving haystack and quantifier reversal

Fix true observed data consisting of all zeros. Restrict the **declared alternative source class** to one-time switch programs `H_s`, `s∈N`, which report zero before time `s` and one at/after `s`. For each finite horizon `N`, `H_(N+1)` matches all observations through `N`; however, NO member of that finite-switch model class produces the infinite zero history. Hence

\[
\forall N\;\exists s>N:\;H_s\text{ matches through }N,
\quad\neg\exists s\;\forall N:\;H_s\text{ matches through }N.
\]

This is a direct FuckedField/noncompact escape or a model-class misspecification, not a paradox in compactness. Adjoining `s=∞` changes the class and adds one global zero model. The haystack **may grow as a declared model language is enriched**, but for a fixed hypothesis universe with truthful accumulating observations, the version spaces `V_(N+1)⊆V_N` shrink monotonically. Failing to distinguish *ever* needs a different proof: an actual fixed hidden-tag pair invariant under the whole permitted probe closure (already proved in main's `field_limit_trichotomy.py`).

## OBC-03: genuine Busy Beaver counterexample latency

Choose a fixed effective programming-machine description convention and let `H_p` denote `"program p never halts"`. The finite observation `O_p(t)` executes p for t steps and reports whether a halt occurred. If the program actually halts at first time `T_p<∞`, then `H_p` is false, and the first falsifying observation is `t=T_p`. Each `O_p(t)` is decidable and honest; no apparent earlier agreement implies the machine never halts.

Define `BB_time(m)` as the **maximum finite halting time** among programs of description size at most `m` under the fixed encoding, when such programs halt. This is the busy-beaver-runtime variant (do not confuse it with the maximum-symbol-score variant). There can be false `H_p` whose first counterexample costs `BB_time(m)` steps within the bounded class. There exists NO total computable `B(m)` that bounds the first counterexample for every false `H_p` of size at most `m`.

**Proof (classical undecidability reduction).** If such a computable B existed, to decide whether arbitrary p halts: compute `m=|p|`; simulate p for `B(m)` steps; if it halted, answer yes, otherwise answer no. The promise of the bound would make the negative answer correct. This would decide the halting problem, contradiction. This proof is *not* a finite Busy Beaver computation. The code deliberately never says `UNVERIFIED_AFTER_BUDGET` implies nonhalting.

Standard primary reference: Tibor Radó (1962), *On Non-Computable Functions*, Bell System Technical Journal 41(3), 877–884, https://doi.org/10.1002/j.1538-7305.1962.tb00480.x . A recent independent formalization of the upper-bound principle is `https://isa-afp.org/entries/Busy_Beaver.html` (2026).

**No unjustified transfer:** This proves uncomputable universal time bounds for halting-encoded claims. It does NOT prove that distinguishing the genuine SUCC line–circle bridge, finding a counterexample to a particular mathematical conjecture, or proving/nonproving π normality requires Busy Beaver time. A reduction from the relevant mathematical problem to such a machine, preserving directions of implications, would be needed.

## OBC-04: permanent source nonidentifiability is a separate obstruction

Let the source state be `(x,t)` with visible bit `x∈{0,1}` and hidden tag `t∈{0,1}`. The allowed action flips x and never touches t. The allowed observation reads only x. The two fixed states `(0,0)` and `(0,1)` have identical reports for **every finite action history, of every length**, despite differing in the hidden target t. A newly permitted tag probe separates them immediately.

This is *permanent toolkit-relative observational equivalence* until the toolkit changes, not merely a late Busy Beaver witness. Neither infinite waiting nor a better search scheduler can reveal an invariant, hidden coordinate through the same nonseparating tools.

## OBC-05: compact gluing and effective selection are distinct

If a source carrier is compact and every observation fiber is closed with the finite-intersection property, then one global compatible source exists (classical compactness). If reports separate sources, it is unique. But (i) proving all finite intersections are nonempty is an infinite mathematical premise, not a consequence of checking one long finite list; (ii) compact existence alone does not imply an effective global selector. Main's explicit computable Kleene tree has paths, none computable. Under a unique-path promise and effective finite branching, a path is computable, possibly with no known resource bound. These are established SUCC calibrations, not new results claimed from the current tests.

## OBC-06: why a finite π digit prefix is qualitatively different

Every FINITE base-16 word `w` admits both a base-16 normal infinite continuation (append a known normal base-16 Champernowne-style digit tail; finite prefix edits preserve normality) and a nonnormal continuation (append only zeros). Therefore finite digit observations ALONE do not refute or prove normality. A proof for the fixed π source may still be finite, by deriving a valid universal estimate using its exact four-pole source and zero seed. The alternative continuations are NOT accepted as source-compatible replacements for π.

For computable source phases `U_n`, failure of fixed-h Weyl decay has the form

\[
\exists h\in\mathbb Z\setminus\{0\}\;\exists\varepsilon\in\mathbb Q_{>0}\;\forall K\;\exists N\ge K:\quad
\bigl|N^{-1}\sum_{n=1}^N e(hU_n)\bigr|>\varepsilon.
\]

An isolated large finite Fourier coefficient cannot certify that `∀K∃N` tail assertion. Conversely an arbitrarily long coherent or apparently uniform prefix cannot certify its limit. This is **limit-quantifier proof debt**, distinct from the Π1 Busy Beaver hypothesis `"p never halts"`. Avoid claiming either π normality or nonnormality from finite observations.

## OBC-07: operational coherence and zero-knowledge scope

Record the distinct axes, never collapse them into a single truth probability:

- observed finite contact / κ: which *actual* source reports have been checked, with their exact index and tool;
- φ: toolkit-relative indistinguishability among the surviving hypotheses;
- σ: source-map adequacy—whether all allowed models are genuine authentic sources and the bridge preserves actual operations;
- μ: available discriminating probe; Busy Beaver latency, a missing probe, and permanent observational equivalence are different reasons for missing refutation;
- ρ: identity/commitment coupling, which calls for adversarial blinding, not a vote for truth;
- mathematical quantifier status: one finite proof, conditionally all horizons, proven effective impossibility, or unverified limit.

A zero-knowledge protocol could allow a prover to establish a **specific finitely checkable statement** without disclosing its witness, under appropriate soundness assumptions. It cannot by itself generate a proof of an infinite mathematical claim or certify an unverified source identity. A finite proof of an all-horizon theorem can of course be checked in finite time if its formal proof system and axioms are accepted; privacy of its witness is a separate concern.

## OBC-08: next verdict-changing SUCC observer probe

**Preload only the two abstract carriers**, including lawful internal operations, then withhold the named bridge. Provide the observer with its **actual source-labelled BBP finite observations**. It must propose a bridge, predict a source-born new-prime observation, and exhibit the correct distinguishing certificate before claiming it has identified any bridge. The theoretical metachecker is permitted exact rational arithmetic, but must not feed the answer into the observer as part of its model language.

Then use the same discipline for the π-current research: source-carry observational identities, inverse-path transfer, Euler/Gamma cancellation and shifted-bin energy are **known**, but `J_(A,q)=o(K_A)` is a still-unproved assertion. Preloading the line and circle does not license preloading a uniformly mixed selected source. Seek a source-selected all-horizon bound and attack it with wrong-seed, cofactor-locked, finite-shadow, and moving-source adversaries.

### Claim ledger

| Claim | Status | Scope |
|---|---|---|
| OBC-01 rational bridge ambiguity / exact probe | DISCLOSED paper exact | finite rational observations; both maps globally continuous |
| Original BBP future p≡1 mod8 source discriminator | DISCLOSED paper conditional on classical infinite primes in progression | every fixed finite original source horizon; not Busy Beaver-hard |
| OBC-02 moving-switch phantom | DISCLOSED elementary | a deliberately noncompact finite-switch model class |
| OBC-03 no computable uniform falsification bound | CLASSICAL imported theorem | general TM nonhalting claims; no π transfer |
| OBC-04 permanent hidden-tag pair | CLASSICAL / SUCC inherited | declared visible-only toolkit |
| OBC-05 compact inverse-limit existence / Kleene | CLASSICAL / SUCC inherited | stated compactness and effective branching hypotheses |
| OBC-06 finite-prefix normal/nonnormal extensions | CLASSICAL | arbitrary extensions, not source-faithful π worlds |
| SUCC original J current decay / π normality | UNVERIFIED / OPEN | zero-seeded actual π source |
