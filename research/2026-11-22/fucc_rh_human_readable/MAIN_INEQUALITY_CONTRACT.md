# The exact (M) bottleneck: a theorem-by-theorem humanization contract

**Reference snapshot:** M. O. Rubinstein et al., *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, working draft 21 November 2026, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf ; specifically Part II §§3–6 and Part III §§4–9. Also see Slijepcevic, *Outline of Alpöge’s proof of the generalised Riemann hypothesis*, https://hexagonmath.org/pdf/2611.00812v1, §§2–9. The public Lean proof is verified externally; this packet has **not** rebuilt or inspected its 175,187 modules.

## Target definitions

For every x in selected long windows `[Y,Y^(3/2)]`, auxiliary odd primes q and d are chosen with `q≡3 (mod 8)`, `d≡7 (mod 16)` and `q|(d+1)`. Define quadratic characters χ_q, χ_d, and η=χ_qχ_d. Define

```
S_{q,d}(x)=sum_{r<=x} Lambda(r) (1+χ_q(r)) (1-χ_d(r)) (x/r-1),
R_{q,d}(x)=S_{q,d}(x)-x log x+(1+gamma+c_χq-c_χd-c_η)x,
G_χ(x)=sum_{r<=x} Lambda(r)χ(r)(x/r-1)+c_χ x,
c_χ=L'(1,χ)/L(1,χ).
```

Then algebraic expansion yields exactly

```
R_{q,d}(x)=G(x)+G_χq(x)-G_χd(x)-G_η(x).
```

The auxiliary character estimates (B) and (C) give small bounds on the twisted three terms on the selected intervals. These estimates are **imported** from the working guide and its cited theorems; they do not follow from SUCC's prime clock or generic Haar invariance.

## Formal statement of the arithmetic main inequality (M)

Rubinstein Part II §4 constructs:

- a finite column group `H` of order n (odd-residue pair classes modulo 4n);
- source-labelled subsets `T,T_2⊂H`, normalized density δ=|T_2|/n;
- for each column and each of m theta-lift maps, positive prime-power sums `P_(u,t,j)` and real-side main terms `M_(u,t,j)` depending on the map's weight system;
- parameters `b=exp(x^ε)`, with scale `B=|T| m b δ/2`;
- an error `E≥0` with the bounds below.

The release proves, in the precise definitions of that guide,

```
(1/n)sum_(u∈H) sum_(t∈T) sum_(j=1)^m (P_(u,t,j)-M_(u,t,j)) ≤ E,

E/B ≤ x^(Cε) * (x/m + x*m/k + m + k/n²),
```

where C is absolute, and the auxiliary construction permits

```
m = x^(1/2+O(ε)), k=x^(9/2+O(ε)), n=x^(2+O(ε)).
```

**This is a precise paraphrase of (M) with its named source variables; it is not a fully defined/independently proved substitute.** The shapes, exact weight formulas and quantifier ordering have to be reconstructed from Part II §§4–6 and the Lean declarations before claiming a complete conventional proof.

## Proof dependency inventory

| Slot | Required proposition in conventional mathematics | Current external status | SUCC/FUCC status | Verdict-changing test |
| --- | --- | --- | --- | --- |
| M0 | Genuine Λ(p^k)=log p, no fake 6, correct Euler logarithm normalization | Classical | **PROVED** via finite FUCC commutator | Insert fake composite 6 or remove 1/k; must fail |
| M1 | Exact Riesz kernel and its Mellin normalization to G(x) | Classical | **PROVED** via FUCC vacuum amplitude | Change sign of gamma correction; must leave pole at 1 |
| M2 | Primitive auxiliary characters, positive combination and uniform window selection | In working guide, Estimates B/C proved from cited analytic number theory | **IMPORTED, not proved by SUCC** | Wrong q,d residues and short windows |
| M3 | Formal height-two inverse-logarithm local p-adic jet valuation | Elementary local model in working guide | **PROVED** in `TECHNICAL_PROOFS.md`, under formal model hypotheses | Use p-height-one mutant or nonintegral f |
| M4 | Actual CM theta-kernel *integrality* in the formal-logarithm coordinates | In checked Lean proof; *not fully human-proved* by current working guide | **UNVERIFIED/ACCESS GAP** | Exact input lattice/coefficient model and basis-change denominators |
| M5 | Period maps assembled from repeated theta lifts; compatible orientations and local factors | In checked Lean; prose guide quotes | **UNVERIFIED** | Type-check diagram and compare every local factor |
| M6 | Divisibility of nonzero lattice minors after all lifts, including exceptional places and losses | In Lean; guide partially conditional | **UNVERIFIED** | Original integral minors with positive valuations; fake six/denominator mutations |
| M7 | Archimedean Petersson/CM period norm formula and index/covolume/slope budget *for same maps* | In Lean; partially modelled in guide | **UNVERIFIED** | Nonzero determinant and bounded row/covolume norm in same lattice |
| M8 | Trace-formula rank, large-span and overlap estimates for many period maps | In Lean; quoted in guide | **UNVERIFIED** | Rank drop/same-line copies must fail rank claim |
| M9 | Galois cohomology and denominator control, uniform in conductor/rank | In Lean; quoted | **UNVERIFIED** | Track all denominators under repeated lift and character moduli |
| M10 | Assemble arithmetic side (M), including averaging across maps/characters, and obtain all error terms | In Lean; the hard human-exposition gap | **UNVERIFIED** | Reconstruct exactly the E/B inequality and constants |
| M11 | (M) + B/C => upper G(X) bound on arbitrarily large windows => RH | Proved in Rubinstein Parts I–II with classical Landau/window criterion | **IMPORTED** | Source-independent proof of each analytic implication |

Status vocabulary: **PROVED** here is a paper derivation with bounded computational verification; **IMPORTED** is an external theorem stated with its provenance; **UNVERIFIED** means SUCC has no proof. The fact that external Lean has checked M4–M10 does not magically create an independent SUCC derivation.

## The humanization strategy in its legitimate order

**Round A: integrality.** Reconstruct M4 from the Lean source precisely, with the height-two local log's integral coordinate choice and denominators. Our formal model M3 is not enough.

**Round B: global arithmetic constraint.** Construct the *same* normalized theta period maps at all places; verify the local valuation lower bounds for their nonzero determinants and the real norm/covolume upper bounds. This produces the SUCC observer-gluing theorem with actual algebraic content, not merely diagrammatic commutativity.

**Round C: rank.** Translate the trace formula and spanning estimate M8; distinguish algebraic independence from repeated same-line observations. A large-collection source need not yield large rank.

**Round D: quantitative inequality.** Assemble the exact error budget with m,k,n and field/conductor costs. Choose `m~√x` only *after* all constants and quantifiers are controlled. The balance `x/m+m` by itself is elementary and proves nothing about the arithmetic left side.

**Round E: conclusion.** Reproduce Part II's deductions of the selected G windows from (M) and B/C, then use the stated sparse-window one-sided theorem and the zeta functional equation. This is the legible RH proof's top part, already available externally.

## The specific false shortcut to avoid

It is tempting to assert "FUCC has prime labels, SUCC has differential depth, therefore accumulated hidden information must exceed capacity." This has no numerical content until M4–M10 provide a *common nonzero integral matrix coefficient*, lower bounds on actual valuations, upper bounds on its actual real size, adequate rank, and conductor-uniform error control. The unit-coefficient shift `(V_p)^a e_1=e_(p^a)` is the concrete counterexample to equating support depth with p-adic multiplicity.

No claim of global priority, self-authored RH proof, or source-equivalence with CM theta machinery is made here.
