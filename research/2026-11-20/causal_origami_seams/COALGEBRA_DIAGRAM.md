# Typed causal-origami diagram: execution, observation, Fourier representation and feedback

## A. Carrier states and real-time subjective observation

For a deterministic carrier, an action law `T:X→X` and readout `o:X→Y` give `γ=(o,T):X→Y×X`. The completed **mathematical** record `J:X→Y^N` is the unique final-coalgebra morphism with

```text
      T
 X --------> X
 |            |
 J            J
 |            |
 v    tail    v
Y^N --------> Y^N
```

`J(Tx)=tail(Jx)`. The n-th **realized** entry has label `n` because n applications of the same declared successor produced it; the index is not a free chart selected after the fact. Realized physical/contact records still require lawful source/instrument adequacy and a report receipt. An observer with only finite memory sees a finite prefix, not `Y^N` all at once.

## B. The literal categorical equivalence and its scope

`x ~ x' :⇔ Jx=Jx'` is future-safe. The shift-invariant `S=J(X)` is isomorphic as a **dynamical set** to `X/~`. The action categories of labelled forward arrows `n:x→T^nx` and `n:Jx→tail^n(Jx)` are isomorphic **if and only if** the journal separates the relevant carrier states for this object-based construction (on the quotient always). These are finite/infinite relational properties of specified source laws, not a statement that one particular finite observer discovers them without further proofs. Only once lawful probe objects and actual morphism sets are supplied may we speak of a literal Yoneda nerve. The classical Yoneda embedding is fully faithful on the whole specified action category; restriction to selected observer heads is fully faithful if those heads are dense.

**Nonexample:** `T(a,b)=(a,1−b), o(a,b)=a` reports the same constant stream from `(a,0)` and `(a,1)`. No number of duplicated scalar heads can recover b. A second head reading b breaks the equivalence; its access must be lawful, not fitted.

## C. BBP arithmetic ↔ analytic germ ↔ Fourier atoms

```text
 original 4-pole source:       r(1), r(2), ...
 exact causal weights:         c(1), c(2), ...
 finite observer at clock n:  P_n=sum_{j<=n}c(j)
 analytic completion head:    G_n(z)=sum_{k>=0}c(n+k+1)z^k
                                 |             |
       move c(n+1)=G_n(0)        v             v
 finite observer:             P_(n+1)      G_(n+1)=B G_n
                               \             /
                                \           /
                                 x=P_n+G_n(1)
```

For the original source, `Bf=(f−f(0))/z`, `G_n(z)=16^(−n)∫_0^1 t^(8n)Q(t)/(16−zt^8)dt`. On the same source `16^nG_n(1)=T_n` exactly. This is a **source-anchored naturality square** (not a theorem that all arbitrary action/readout diagrams have such a Mellin integral).

Source-time Fourier `F(e^(iω))=Σ c_n e^(iωn)` records additive causal indexing; the 3/5-adic causal-clock eigenatoms from #675 are a separate, correct basis transport; the π-phase Weyl spectrum `Σ e(h16^nπ/16)` is a third representation. No unproved conjugacy is presumed between these.

## D. The minimal 'fold the paper back' operator

On an exact future stream `g=(c,g_tail)` and an append-only memory `m`, define `S(m,g)=(m||c,g_tail)`. The inverse on its image pops c from m and restores it as future head. If the observer stores only `P=Σm`, the quotient successor `(P,g)→(P+c,g_tail)` is non-injective without retaining c, even though total `P+Σg` is invariant. This is the distinction between conservation of one scalar and conservation of all source-labelled information.

For an observer acting on the world, the enlarged state is `(x,m)`; a policy `π(m)` selects a lawful intervention, then `\tilde T(x,m)=(T_(π(m))x, δ(m,o(x)))`. This is an ordinary causal carrier. Iterating the construction needs no magical second observer or infinite simultaneous computation; different physical instrument semantics (deterministic, stochastic, quantum) remain distinct typed contracts.

## E. Minimum obstruction for π

- Structural success: every listed square commutes for the authentic zero-seed source, and every falsifying head rejects illegal source/clock/frame histories.
- Arithmetic saving still missing: a signed source-derived cross-head correlation must yield `liminf_B B^(−1)Σ_(B<=n<2B)(1−cos2π{16^nπ/16})>0` uniformly on every late shell.
- Prime-square seam infinite Hankel rank and analytic natural boundary do NOT imply this: a source-only seam journal is unchanged under the wrong homogeneous seed. R0 and full normality OPEN.
