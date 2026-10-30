# "3 is anti-normal w.r.t. 2" — precise content and the sharpened ×2×3 formulation

**Author:** Ravel. **Date:** 2026-10-27. **Status:** reformulation note (rigorous facts; open conjecture).

## The precise arithmetic asymmetry (proved, elementary)

For the two generators of the BBP source's carrier, the valuations split into *disjoint* support:

| generator | $v_2$ | $v_3$ | 2-adic role | 3-adic role |
|---|---|---|---|---|
| $16=2^4$ | 4 | 0 | **non-unit** (contracts $\mathbb Z_2$) | unit |
| $3$ | 0 | 1 | unit | **non-unit** (contracts $\mathbb Z_3$) |

So ×16 and ×3 are **anti-normal** in the exact sense: each is a unit exactly where the other is a
non-unit, and their prime supports $\{2\}$ and $\{3\}$ are **disjoint**. This is strictly stronger
than mere multiplicative independence: it is *disjoint-prime-support* opposition.

## What this gives (classical)

This disjoint-support structure is what makes $\langle\times16,\times3\rangle$ a **higher-rank**
(stiff) action on the $\{2,3\}$-solenoid $X_{2,3}$, and it is the mechanism behind:
- Furstenberg (1967): closed ×2/×3-invariant sets are trivial.
- Rudolph–Johnson (1990): ×2/×3-invariant ergodic measures of positive entropy are Lebesgue.
- Einsiedler–Katok–Lindenstrauss; BLMV (2009): effective rigidity.

## The trap (already in the dossier)

Higher-rank rigidity on the *solenoid* does **not** descend to the *real fiber*. A ×16/×3-invariant
solenoid measure can project to a non-Haar real measure (Becher–Slaman rectangular counterexample).
So "anti-normal ⟹ rank-2 stiffness" is real, but normality needs the stiffness *on the real
coordinate of π's specific orbit*, which is not automatic.

## The sharpened conjecture (the genuinely new target this motivates)

**Conjecture (disjoint-prime-support rigidity, descending).** The *disjoint-support* opposition
(×16 contracting $\mathbb Z_2$, ×3 contracting $\mathbb Z_3$, with no shared prime) is a strictly
stronger hypothesis than the Furstenberg ×2×3 *independence*, and it may be strong enough to force
rigidity that **descends** to the real fiber — i.e. to rule out the Becher–Slaman-type
rectangular counterexamples that defeat the generic formulation.

**Status:** UNVERIFIED. It is a sharpened *formulation* of ×2×3, not a proof. It is not obviously
dead (unlike the $D^{(3)}$ defect route, which the universal $O(1/N)$ theorem closed), because the
disjoint-support condition is genuinely more restrictive than what the known counterexamples satisfy.

**Falsification test:** construct a Becher–Slaman rectangular counterexample whose ×16 and ×3
generators have *disjoint* prime support and still fail to be normal in the real fiber. If such a
counterexample exists, the disjoint-support strengthening is insufficient and the conjecture is
REFUTED. If none exists (and a rigidity theorem can be proved), it is the bypass.

## Boundary

This note converts a poetic phrase into a precise, testable conjecture. It does not prove normality,
does not prove ×2×3, and does not claim the disjoint-support condition is sufficient — it *poses*
that as the sharpest live question, with an explicit falsification protocol.
