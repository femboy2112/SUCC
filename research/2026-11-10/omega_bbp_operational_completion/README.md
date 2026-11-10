# Ω arrows, productive BBP, and the exact carry cocycle

**10 November 2026 · source-attested research note · follow-up to [draft #579](https://github.com/femboy2112/SUCC/pull/579).**

**Question:** Why can't an infinite BBP expression simply be beta-reduced to beta normal form? Could the nonterminating Ω paths be the arrows that hold the arithmetic and its parity together?

**Verdict:** The question has no representation-independent negative answer. A real series is not a lambda term until it is encoded. The raw `Ω_k` in SUCC has **no finite beta normal form and no head normal form**. A *guarded productive stream* of BBP terms can expose every finite prefix; under the usual recursive unfolding it has no *finite fully unfolded list* even though every finite query can terminate. A closed procedure may even be syntactically beta-normal when unapplied; this is not an evaluated infinite digit list. Infinitary lambda calculi can assign certain streams infinite tree normal forms. None of those facts implies digit equidistribution.

This note isolates two **proved** generic arithmetic/computation facts, their **source-specific missing premise**, and a proposed (not yet constructed) proof-relevant lambda compiler.

## 1. Three different infinities, not one obstruction

1. **Arithmetic:** `P_∞ = Σ_(j≥1)16^{-j}r(j) = π/16` is a limit of rational partial sums. Its equality to pi is the authenticated classical BBP identity.
2. **Computational:** a lazy stream may have a head constructor and all finite observations while recursive unfolding never ends. In an infinitary calculus its Böhm/Levy–Longo tree can represent an infinite result, provided the reduction semantics is explicitly chosen.
3. **Unguarded raw Ω:** set `ω_k=λx.x x ... x` (k left-associated copies), `Ω_k=ω_k ω_k`, k≥2. The unique head redex regenerates a head redex after every contraction; for `k=3`, `E_3(m)→β E_3(m+1)`. There is no head normal form. The syntax carries an infinite *reduction path*, but its ordinary Böhm-tree observation is bottom, not the BBP digit stream. This is [the verified scope of the existing omega interpreter](../../2026-11-09/scott_omega_causal_weld/OMEGA_INTERPRETER.md), not a source compiler.

A pure beta-normal form is defined by the absence of a subterm `(λx.M)N`. The statement “the infinite BBP has no beta normal form” requires a chosen term encoding, observer, and reduction rules. In particular, **head productivity**, **weak-head normalization**, **full beta normalization**, **infinitary normal forms**, and **Scott-domain convergence** are distinct predicates.

The existing literature on *clocked Böhm trees* gives a rigorous analogue of the proposed operational pinbed: reduction-step clocks can distinguish terms with the same ordinary infinite Böhm tree. It does **not** provide a BBP-specific digit theorem.

References: [SEP, Lambda Calculus](https://plato.stanford.edu/entries/lambda-calculus/); [Endrullis–Hendriks–Klop–Polonsky, *Discriminating Lambda-Terms Using Clocked Böhm Trees*, LMCS 10(2:4), 2014](https://lmcs.episciences.org/880); [Severi–de Vries, infinitary lambda calculus](https://www.cs.le.ac.uk/people/ps56/lcttnl05.pdf).

## 2. Proved: a contractive coinductive BBP tail, unlike raw Ω

Keep the exact four poles and literal zero seed from [Main XXII](../../../docs/PI_NORMALITY_FRONTIER.md):

```math
r(j)=4/(8j-7)-2/(8j-4)-1/(8j-3)-1/(8j-2),
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
```

For each `n≥0`, define `T_n=Σ_(j≥1)16^{-j}r(n+j)`. On the Banach space `ℓ∞(ℕ₀)`, define the *backwards-in-horizon* tail operator
```math
(\mathcal F t)_n=(r(n+1)+t_{n+1})/16.
```
Because `0<r(j)<4`, it preserves bounded sequences and
```math
\|\mathcal F t-\mathcal F v\|_\infty\le\tfrac1{16}\|t-v\|_\infty.
```
Hence it has a **unique bounded fixed point** `T`, with
```math
\|T\|_\infty<4/15, \qquad
\|\mathcal F^{k}(0)-T\|_\infty\le (4/15)16^{-k}.
```
Indeed, `(\mathcal F^k0)_n=Σ_(j=1)^k16^{-j}r(n+j)`. This is a direct geometric-series/Banach fixed-point proof. It is **generic for bounded forcing**, not a π-normality theorem.

**Interpretation:** the backwards horizon computation contracts by `1/16`, while forward source time multiplies both finite state and tail by `16` and transfers the new forcing between them. There are two different computational clocks; their coexistence is algebraically exact.

## 3. Proved: the causal weld is a source-labelled commutative square

For *any* rational seed `s`, let `U_0(s)=s`. Then
```math
U_{n+1}=16U_n+r(n+1),\qquad
T_{n+1}=16T_n-r(n+1).
```
Addition `Y_n=U_n+T_n` produces the exact commutative square
```math
Y_{n+1}=16Y_n,\qquad
Y_n=16^n(s+\pi/16).
```
The forcing is an **exact arithmetic transfer/coboundary** between the computable prefix and its unresolved future. The square is source-labelled and seed-marked. The same *shape* exists for other bounded forcing sequences, so the commutative square alone cannot exclude a biased orbit.

**Finite scope:** fix `L`, set `P_L=Σ_(j=1)^L16^{-j}r(j)`, `T_n^{(L)}=Σ_(j=n+1)^L16^{n-j}r(j)`. For all `0≤n≤L`, `Y_n^{(L)}=U_n+T_n^{(L)}=16^n(s+P_L)`. These are **exact rational** equalities. Scott/metric completion takes the real limit at fixed `n`; a simultaneous growing-frequency or growing-digit-index assertion requires the paid source-clock coupling already established in [CAYLEY_PROOFS](../../2026-11-09/cayley_source_observer/CAYLEY_PROOFS.md).

## 4. Proved: the integer-carry observer contributes a genuine cocycle

Write, for the completed orbit (or any finite common horizon `L`),
```math
C_n=\lfloor U_n\rfloor,\quad
\kappa_{n+1}=C_{n+1}-16C_n,\quad
\varepsilon_n=\lfloor\{U_n\}+T_n\rfloor\in\{0,1\}.
```
The bound `T_n<4/15` ensures only one possible future-induced integer crossing. Then `floor(Y_n)=C_n+ε_n`. Define the true completed radix-16 digit by
```math
d_n=\lfloor Y_{n+1}\rfloor-16\lfloor Y_n\rfloor.
```
Subtracting the two floor identities gives the **exact carry coboundary**
```math
\boxed{d_n=\kappa_{n+1}+\varepsilon_{n+1}-16\varepsilon_n.}
```
It is not an asymptotic approximation and remains valid on every finite rational common-horizon slice. The term `-16ε_n` is invisible to parity but **not** to the full integer carry; therefore
```math
(-1)^{d_n}=(-1)^{\kappa_{n+1}}(1-2\varepsilon_{n+1}).
```
For an epoch `[A,2A)`, write `Q_A=A^{-1}Σ(-1)^{κ_(n+1)}` and `B_A=A^{-1}Σ(-1)^{κ_(n+1)}ε_(n+1)`. The exact first-digit parity mean is
```math
P_A^{\mathrm{digit}}=Q_A-2B_A,\quad |P_A^{\mathrm{digit}}-Q_A|\le 2A^{-1}\sum_{n=A}^{2A-1}\varepsilon_{n+1}.
```
The future-crossing event `ε_n=1` lies in the narrowing strip `{U_n}≥1-T_n`, whose width is `O(n^{-2})`. **The strip width does not bound its deterministic occupation frequency.** Neither `Q_A→0` nor sparse crossings is proved for the original zero seed.

If `s_n=(-1)^floor(Y_n)`, then `(-1)^{d_n}=s_(n+1)`, and the old/observer epoch difference is the exact telescope `(s_(2A)-s_A)/A`. This is the one-step Scott-boundary payment in [the current frontier](../../../docs/PI_NORMALITY_FRONTIER.md).

## 5. Which arrow is actually missing?

The mapping of the `Ω₃` growth step `E₃(n+2)→E₃(n+3)` to the BBP edge `(n,U_n,T_n)→(n+1,U_(n+1),T_(n+1))` can be made **as an externally labelled path map**. That is not yet a lambda-calculus compiler. Its labels could equally well carry zero forcing and a constant nonnormal orbit.

A source-faithful *operational* compiler must:

- encode and compute the exact four-pole `r(n+1)`, prefix `U_n`, seed and future-tail evidence, not merely print the `Ω₃` path count;
- prove simulation and reflection of the intended reductions and of the typed `(n,U,T)` arithmetic transition;
- retain the integer lift, all carry/winding events, and the future `ε_n` event under the observer; a circle-only quotient aliases different integer histories;
- supply guarded productivity for each finite observation while refusing the false claim that raw `Ω_k` has a head normal form.

Even that would be a **semantic soundness theorem**, not parity balance. The first source-selective *analytic* obligation remains an infinite-epoch signed saving for the original zero seed, rejecting the coherent wrong-seed controls. A constant stream via zero forcing obeys every generic square and contraction above yet has parity (+1) always.

## 6. Discriminating probe and falsifiers

1. **Positive:** independent exact rational finite-horizon computation verifies every `d_n=κ_(n+1)+ε_(n+1)-16ε_n`, each two-register update and 16-invariance.
2. **Adversarial positive:** choose a *rational* seed that forces `ε_n=1` at a specified finite step; verify the correction is necessary, rather than relying on a zero-crossing sample.
3. **Negative:** zero forcing, zero seed, all completed digits 0; shows that the generic reduction clocks, coboundary and Scott completion cannot by themselves force balance.
4. **Normalization classifier:** distinguish raw `Ω₃` (no head NF), a guarded digit stream (finite prefix productive, global unfolding infinite), and a terminating finite rational digit request. Test only after defining concrete lambda encodings and their operational semantics; no such compiler is claimed here.
5. **Asymptotic target:** prove both `Q_A→0` and `A^{-1}Σ ε_(n+1)→0` for the authenticated zero seed, **or** obtain cancellation directly in `Q_A-2B_A`. Any claimed improvement must reject the PPP-08 prime-preserving wrong-seed shadow.

**Claim ledger:** contraction and carry cocycle = **DISCLOSED within bounded-forcing/finite-slice models**; independent finite checks = **OBSERVED**; clocked-Böhm/source compiler = **UNVERIFIED**; original-zero signed estimate and π base-16 normality = **OPEN**. An arrow-level computational semantics is promising, but no correspondence between raw Ω reduction and source-selected digit statistics has yet been proved.
