# Focused runtime audit — prime fixed-point observer

2026-11-12. Same-model read-only audit, no repository edits. Targets: `prime_observer.py`, `test_prime_observer.py` in the new dossier. This is a finite audit of this implementation, not formal proof certification.

## Verdict

Arithmetic formulas, midpoint ranges, ordinary and transported proper-factor counts, sum-energy trace, floor cutoff, Haar coefficients, and CRT interior bounds are correct under their declared domains. One exact-type source-authentication issue was found and repaired by the root. One genuine source-coherence limitation in the marginal counterfeit was found; root has elected to strengthen the certificate and constructive model rather than merely weaken its description.

## Issue A — source label equality hooks

The initial pair-receipt verifier checked membership of `source` in two strings without requiring its exact type. A custom object whose `__eq__` returns True can masquerade as the transported source and pass all arithmetic fields of a genuine transported receipt. Thus a non-string source could be accepted.

Root added `type(source) is str` before membership/equality checks and a regression. I verified that the repaired function rejects an equality-hook source. I also independently compiled a scratch mutation omitting only that exact-type guard: it accepts the equality-hook receipt. Both behaviors were executed; repository bytes were not modified by this audit.

## Issue B — a shared midpoint is one source value

`minimum_overlap_model` originally optimizes separately assignable left/right masks, but displacement zero corresponds to the SAME integer n on both sides. A coherent integer indicator requires a(0)=b(0).

Exact counterexample to unrestricted single-source sharpness: at n=9,z=2,width=4, first-cell admissible displacements are {0,2}; capacity D=2 and marginals A=B=1. The independent-mask Fréchet lower bound is 0, attained by a=[1,0], b=[0,1]. These masks disagree at d=0 and cannot come from a single integer indicator. Every coherent single-source realization of these marginals has one overlap in this cell.

The existing n=1024,z=2,width=128 hostile source is unaffected, because d=0 is excluded by parity.

Root's chosen repair is mathematically sound: retain c=1_P(n) and center presence, remove the center slot and c from each marginal, optimize the remaining slots, then restore (c,c). The sharp coherent lower bound is

c + max(0, (A-c)+(B-c)-(D-1)),

and the upper bound remains min(A,B). For d>0, the plus side occupies integers strictly greater than n and the minus side integers strictly smaller than n; both are injective in d. Therefore there are no other shared-label constraints across positive displacements or cells. The repair is sharp among arbitrary single integer indicators retaining these marginals and the center value. It does not impose authentic multiplication/primality on the counterfeit.

## Independently executed checks

- Existing runtime suite at the checked instant: **20 test methods, all passed**.
- **147 arithmetic checks:** proper-factor energy from a direct double multiplication scan for n=2,…,100, then exact Fraction sum-energy traces and floors for even N=4,…,98. All passed.
- **98 transported factor-count checks:** map proper factorizations of σ(n) back under σ; verify every transported product equals n, both factors are nonunits, and counts equal transported_energy(n), for n=2,…,99. All passed.
- Equality-hook source: repaired verifier rejects; exact-type-guard omission mutant accepts.
- n=9 shared-center counterexample explicitly reproduced.

These are separate algorithms/checks within the same model family. They are not independent human review or a proof assistant run. Later root edits require appropriate targeted replay.

## Formula and scope notes

1. The executable pair receipt uses the **sum-energy** resolvent 1/(1+d(k)+d(N-k)), not the tensor-product resolvent 1/[(1+d(k))(1+d(N-k))]. Both share their zero modes and the stated 1/2 gap, but finite trace values differ. Current runtime docstring correctly distinguishes them.
2. Default r=(N-3).bit_length() is exactly a valid strict cutoff 2^r>N-3, including N=4.
3. r=0 is deliberately permitted and correctly marked uncertified when relevant. A positive trace is not mistaken for a pair witness.
4. `midpoint_masks` includes d=0,…,n-2. For n>2, its parity quotient keeps d≡1-n mod2; n=2 is handled separately. The finest Haar parity law is tested only after explicitly removing the exceptional prime2, which is correct.
5. CRT positions satisfy 0≤d<n-z, so both prime candidates lie above the screening cutoff. If z≥n, the interior is empty. The reported upper bound applies to the **interior count**, not the full Goldbach count.
6. Haar padding and per-scale coefficient denominator are correct; size1 has no detail bands and is handled.
7. Reflection `eigen_plus/eigen_minus/eigen_zero` concern PJP, not the skew commutator [P,J]. The theorem note should identify the operator whenever these keys are explained.
8. Finite source receipt verification replays divisibility against the currently imported implementation; provenance hashes must carry code identity. The receipts are not a general theorem kernel.
