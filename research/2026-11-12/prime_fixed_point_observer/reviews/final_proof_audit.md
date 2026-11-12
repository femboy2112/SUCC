# Hostile proof audit of THEOREMS.md

Audited file: `SUCC/research/2026-11-12/prime_fixed_point_observer/THEOREMS.md`.

Read SHA-256: `0f56f924b9ddc92fa708e1db20f1ed34616bbe07e04b86388a7d3fe61fd68716`.

Scope: every displayed construction and PFO-01 through PFO-13, including maps, domains, units, count conventions, spectral bounds, finite cutoffs, sharpness and reformulation labels. This is a same-model written-proof audit. No repository edits, full native-suite run or Lean verification were performed.

**Verdict: the main constructions and PFO-12 proof are sound under their intended domains. Correct the four items below before freezing the dossier. No stronger theorem needs to be withdrawn.**

## Required corrections

### A. Alternative filter paragraph conflates a resolvent fixed space with zero modes

Location: section 5, immediately after the N=6 floor counterexample.

The text introduces `T_single J T_single J`, then calls its trace a formula containing an unstated power r, and says it has the same zero modes. The filter is positive and invertible on this finite space, so its own zero-mode space is zero. The relevant eigenspace has eigenvalue 1.

Use explicit definitions:

    T_single=(I+D_N)^(-1),
    Q_N=T_single J_N T_single J_N,
    Tr(Q_N^r)=sum_k[(tau(k)-1)(tau(N-k)-1)]^(-r).

Then state that `Fix(Q_N)=ker(Hpair_N)` (and equals `Fix(T_N)`), with the same error bound and sufficient floor cutoff. This makes the alternative product filter distinct from the implemented sum-energy resolvent.

The asserted bound is correct: if either input is composite, the product of the two denominators is at least 2. No mathematical change beyond the missing power and fixed-space wording is needed.

### B. Finite relabelling does not preserve every eventual statistic

Location: section 8, the sentence beginning “Since f is a finite permutation”.

The statement “preserves every eventual statistic unchanged after all modified labels have passed” is too broad. Tail pointwise agreement of the prime mask does not preserve additive sum statistics: a changed small label can pair with a large unchanged label.

Exact counterexamples from independent direct trial division:

| Target N | Ordinary ordered pairs | Transported ordered pairs |
|---|---:|---:|
| 200 | 16 | 20 |
| 256 | 16 | 18 |
| 1000 | 56 | 52 |

All these targets exceed the largest modified label, 97; N=200 also exceeds twice that label.

Replace with the exact statement: the transported prime indicator agrees pointwise with the ordinary prime indicator for every label greater than 97, and its cumulative prime count agrees at every cutoff at least 97. Consequently properties invariant under finite modifications agree. Do not assert equality of arbitrary later fixed-sum correlations. This repair strengthens the point of the hostile control: abstract multiplicative equivalence and even tail mask agreement do not supply a universal all-input additive guarantee.

### C. State the integer cutoff domain in PFO-07

The cutoff statement requires `b` to be an integer. Without that condition, b=5/2 and n=9 give a literal counterexample: 9<(b+1)^2, but the only tested proper divisor is 2 and 9 is falsely accepted.

Declare `b in Z_{>=1}` and, for the window corollary, `M in Z_{>=2}`. These domains also cover M=2,3, for which floor(sqrt(M))=1. The implementation already validates integer cutoffs at least 1.

The threshold is sufficient; no necessity claim should be added. For some cutoffs the first hidden composite occurs later than (b+1)^2, and the text correctly avoids claiming otherwise.

### D. Cells must exhaust the screened interior for the upper bound

Location: section 7, “Within disjoint cells I define capacities ...”.

PFO-11 bounds the whole interior witness count, so the cells must form an exhaustive partition of the screened displacement set (or be a partition of the ambient displacement range, then intersected with that set). Mere disjointness is insufficient: omitting a cell containing a witness can make the displayed sum of upper bounds smaller than the full interior count.

Replace “Within disjoint cells” by an explicit finite exhaustive partition assumption. The sharpness and refinement proofs are then correct, including the distinction between the interior and full G(n).

## Small precision edits

- In the Haar parity statement, say “zero out the prime-2 endpoint while retaining the original displacement slots and dyadic padding” rather than simply “remove”. Deleting and reindexing is a different operation. At n=3, deleting the last slot and choosing a length-1 transform leaves no width-2 band, whereas the asserted half-overlap law concerns the retained length-2 transform. The current tests correctly zero the entries while retaining coordinates.
- Say “positive odd powers” and “positive even powers” of A_N. The r=0 power has trace N-3, not R(N), and nonnegative powers were explicitly allowed earlier in the dossier.
- In the W_G beta equation, state that the bound variable x is chosen fresh for G, or explicitly adopt the usual capture-avoiding convention. For closed program functionals this is already automatic; the literal phrase “any functional G” should not silently allow free-x capture.

## PFO-12: no blocker

The shared-center formula is correct for one globally coherent binary source:

    lower = c + max(0,(A-c)+(B-c)-(D-1)),
    upper = min(A,B).

The center bit must be feasible for the given marginals, as it is for actual source-derived counts. Off-center positive labels n+d and negative labels n-d are distinct both within and across disjoint displacement cells; hence there is no further global binary-source consistency constraint. Removing the center gives independently assignable off-center masks, and restoring it proves both endpoints sharply.

I exhaustively enumerated binary off-center assignments for capacities D=1 through 6 and both center bits. All 182 feasible (D,c,A,B) cases attained exactly the stated minimum and maximum. This finite enumeration is a diagnostic; the disjoint-label argument supplies the universal proof.

The n=9,z=2,width=4 example checks exactly: admissible positions are d=0,2; c=0; both marginal counts equal 1, so overlap is forced at d=2 and the coherent lower bound rises from 0 to 1. The n=1024 control does not share the center because parity excludes it, so this correction does not invalidate that control.

## Other claims: no additional blockers found

- PFO-01's Div endofunctor and natural transformation, including F(1), are valid; the composite expansion example is correct.
- PFO-02's no-retraction argument and radical divisibility condition are valid.
- PFO-03's adjunction directions, computability and literal fixed points are correct. The separate traversal category pays the absence of distinct-prime arrows in Div.
- PFO-04's productivity proof is valid with the declared lazy beta/delta semantics and n>=2 trial precondition. It does not assume finite state or completed infinity.
- PFO-05 correctly attributes the classical coalgebra and distinguishes the unit, prime basis vectors and arbitrary primitive linear combinations.
- PFO-06's Hilbert domain treatment, non-strict global contraction, norm equality and prime-square sharpness are correct. Ambient H membership is understood in the weighted-domain formulas.
- PFO-08's implemented sum-energy trace, ordered count and sufficient strict cutoff are correct, including r=0 and N=4. The subsequent Z>=1 criterion is Goldbach-equivalent only at the stated sufficient cutoff, as the text says.
- PFO-09 and PFO-10 have the correct reflection eigenvalue multiplicities, parity law, commutator sign and norm factor 2. The even-sector exception and the two vacuous commuting identities are handled correctly.
- The Haar Parseval constants and the relaxed Fréchet inequalities are correct under the partition/coordinate clarifications above.
- PFO-13's explicit transported source, same-count/parity profile, ordinary six unordered pairs at 100, squared commutator values and failed SUCC/FUCC braid are all correct. Its transported-addition explanation does not confuse categorical equivalence with arithmetic preservation.

No audit claim above should be read as external peer review or a proof of Goldbach, pi normality or RH.
