# Cross-audit of sibling PR #416: original four-pole BBP as a multiplicative logarithmic jet

**Research status: classical algebra specialized to original BBP; local exact independent corroboration of a SIBLING theorem.** PR #416 head `725377a64748ab0c442d16a61509b99687412505` is on a different, unmerged branch descended from #414. The present main-based universal N/Z carrier branch does **not** merge or silently claim ownership of its original result. This addendum independently reconstructs and tests its source-specific construction. No pi-normality or RH claim.

## 1. One universal multiplicative functor, one selected derivative

Let b>=2 be an integer and V_n(u) positive real-analytic near u=0 with nonzero rational V_n(0). Define B_0(u)=g(u)>0 near zero and

`B_(n+1)(u)=B_n(u)^b V_(n+1)(u)`.

Define the *logarithmic first-jet observation* `L(B)=B'(0)/B(0)` (a real derivative), and the rational-value prime-place observations `v_p(B(0))`.

The exact product/chain rules are

`L(FG)=L(F)+L(G)`, `L(F^b)=b L(F)` and `v_p(F(0)G(0))=v_p(F(0))+v_p(G(0))`.

Therefore the first jet always obeys an affine source recurrence

`u_(n+1)=b u_n+r_(n+1),  u_0=L(g),  r_n=L(V_n)`.

In parallel each prime valuation obeys

`v_p(B_(n+1)(0)) = b v_p(B_n(0))+v_p(V_(n+1)(0))`.

This is a fully typed **joint finite carrier**: same multiplicative object, Archimedean infinitesimal response plus finite-place discrete valuations. The two observations are compatible with multiplication but are NOT mutually recoverable: many analytic deformations have identical rational value at u=0 but different first jet.

**Do not differentiate v_p with respect to real u.** Its topology and discreteness differ from the analytic first jet. Cross-place common-basis transport would require an additional defined map, not merely naming both observations.

## 2. Authentic BBP realization; all finite identities exact

Use the original signed four-pole rational source, with integer a>=1:

`R(a) = 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5)`.

The exact rational potential from sibling #416 is

`V(a)=a^4/[(a+3)^2(a+4)(a+5)]`;

indeed `d/da log V(a)=R(a)`. At the original clock a_n=8n-7, define

`B_0(u)=1`, `B_n(u)=prod_(j=1)^n V(a_j+u)^(16^(n-j))`.

Then `d/du log B_n(u)|_(u=0) = U_n(0)` with

`U_0=0`, `U_n=16U_(n-1)+R(8n-7)`.

This is a genuinely source-faithful multiplicative realization of the original signed BBP orbit as the infinitesimal response of a rational finite product. It does not introduce a random digit law.

Let `P_n(u)=prod_(j=1)^n V(a_j+u)`. The exact Abel rearrangement

`B_N(u)=P_N(u) prod_(j=1)^(N-1) P_j(u)^(15*16^(N-j-1))`

shows how the unweighted Gamma product and the full exponentially extruded BBP time form fit within one carrier. A shifted Gamma quotient is obtained from P_N using the ordinary Gamma recurrence; no analytic continuation is required for the finite rational B_N itself.

## 3. All places: a source-specific nontrivial test

For each native a_n=8n-7, the four integer denominator/numerator factors have 2-adic valuations `(0,2,0,1)` at shifts `(0,3,4,5)`. Their signed weighted sum gives

`v_2(V(a_n))=4*0-2*2-1*0-1*1=-5`.

Therefore

`v_2(P_N(0))=-5N`, and `v_2(B_N(0))=-5*(16^N-1)/15=-(16^N-1)/3`.

Every B_N(0) is positive rational, so the exact finite product formula also gives

`log B_N(0) = sum_p v_p(B_N(0)) log p`.

This is a real archimedean/prime constraint on one concrete rational value, though its first derivative remains an additional, independent jet datum.

The Gamma-rank-two, positive first-jet-matched mutant c'=(5,-5,0,0) instead uses

`V_mut(a)=(a/(a+3))^5`, so `v_2(V_mut(a_n))=-10`

and `v_2(B_N^mut(0))=-2(16^N-1)/3`. This source mutant shares the leading Gamma rank and first source jet but differs in original second jet and arithmetic prime slopes. The prime-place signature therefore distinguishes sources *within this declared family*, not the selected orbit's normality.

## 4. Boundary ambiguity is precisely a missing function jet

Fix any real seed s and put g_s(u)=1+s u, restricting u to a neighborhood of0 where it is positive. The changed B_N^s satisfies the same source/update and obeys

`B_N^s(0)=B_N^0(0)` for every N,

`L(B_N^s)=L(B_N^0)+16^N s`.

Thus **every** prime-place valuation of the pointwise potential is blind to a change of the real initial seed. The authentic zero seed is not just the point value B_0(0)=1 but the **marked first jet** B'_0(0)=0, equivalent here to B_0(u) identically1. The coherent s*=-pi/16 counterseed reproduces the same entire sequence of rational point values, while its selected real phases tend to1; any proposed prime-values-only normality theorem fails this exact control.

## 5. What changed in the next-round priorities

Sibling #416 adds a more operational source-to-observer contact than a bare Gamma interpolation: the actual original BBP **signed recurrence** is a first-jet observable of an explicitly arithmetic finite multiplicative carrier, and the 2-adic places read source-specific slopes of the *same* carrier point values. It is worth building a reusable N/Z **jet-valued object with discrete valuation places**, then testing path composition and observation in that richer category.

But the core normality target remains open. Neither the exact potential, its all-place product formula, its Gamma quotient, nor the marked zero first jet supplies a source-selected estimate for the full complex real-circle character e(hU_n), finite-band Fejér energy, or cylinder visits. A new inequality must use the additional data, survive the coherent seed and normal/non-normal calibration, and not simply restate the already known Weyl/entropy gate.

## Validation

- **10/10 new exact stdlib tests** PASS. The code computes both original and mutant rational potentials, all-prime valuation vectors, direct B_N products through N4, Abel product, original first jets, and changed-seed response.
- **Separate SymPy/mpmath oracle** PASS: independent symbolic derivative and recurrence through N8, all-N exact 2-adic formula checked through N9, 65-dps Gamma quotient asymptotic at four N values.
- `logjet_probe.py`, `test_logjet_probe.py`, `logjet_independent_oracle.py`, `logjet_tests.log`, `logjet_independent_receipt.json` retained. These are independent implementations sharing the known theorem, not a blind external proof referee.
- Full root SUCC suite/new Lean formalization not claimed by this addendum. Original remote parent and historical theorem contracts untouched.
