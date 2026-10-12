# An arithmetic source, not merely a toy: prime-clock operational Yoneda descent

**2026-10-11. Branch:** research/operational-yoneda-policy-descent-2026-10-11 (stacked draft PR #22). **Status:** classical finite modular ring quotient plus earlier certified source/claim/coaction and Yoneda functor transport. All statements elementary and PROVED LOCAL; no priority or RH proof claim.

## 1. Independent arithmetic source object

Choose a TRUE finite prime place p, precision r>=2, strictly smaller positive k<r, an integer primitive shift d, and a TRUE prime q defining an authentic prime-indexed FUCC dilation. Work in

\[
R_r=\mathbf Z/p^r\mathbf Z,\quad
R_k=\mathbf Z/p^k\mathbf Z,\quad
h([x]_{p^r})=[x]_{p^k}.
\]

The operations are actual modular arithmetic:

\[
S_d(x)=x+d,\qquad V_q(x)=qx.
\]

The hardware/software observation menu is DECLARED to contain two low-information state-changing instruments SHIFT and DILATE (each reports a public sentinel -1, then applies the corresponding state map) and, optionally, READ (reports x mod p^k and leaves the carrier unchanged). There is no access to exact original-source x except through these instruments. A claimed true original-source target is precisely t_r(x)=str(x mod p^k) on R_r and t_k(y)=str(y) on R_k.

**Algebraic source derivation, not fitted lookup tables:**

\[
\boxed{
h\circ S_d=S_d\circ h,\qquad
h\circ V_q=V_q\circ h,\qquad
\mathrm{READ}_r(x)=\mathrm{READ}_k(h(x)).
}\tag{A1}
\]

Proof: ring reduction is a well-defined surjective additive and multiplicative homomorphism because p^k divides p^r. Both maps are integer polynomials, so substitution and reduction commute. The artificial -1 non-data outcomes agree and public action enabledness is identical. The original target is the pullback t_r=t_k∘h. Therefore A1 supplies the Y5–Y6 source/claim/instrument commuting squares from the operational Yoneda policy-descent theorem, **without postulating their transition lookup entries independently**. The resulting functor on finite legal observation path categories is also mechanically checked.

This is a genuinely mathematical arithmetic source family, but still entirely CLASSICAL. The model imports actual prime verification, not proof of the complex Euler product, analytic continuation, Tate's Gamma place, or RH.

## 2. The nonflat-to-flat quotient (address commutator, NOT physical curvature)

The integer address defect of the ordered SUCC/FUCC actions is

\[
\boxed{
(S_dV_q-V_qS_d)(x)=d(1-q)\mod p^r.
}\tag{A2}
\]

Here S,V are actual maps on residue addresses. On a Hilbert basis, the ket operator commutator is a DIFFERENCE OF TWO KETS, not the scalar A2. The defect is visible at precision r precisely when p^r does not divide d(1-q); it becomes zero at precision k iff p^k divides d(1-q).

Take the smallest compelling calibrated source:

\[
p=2,\ r=2,\ k=1,\ d=1,\ q=3.
\]

Then

\[
d(1-q)=-2\equiv2\pmod4,\qquad
-2\equiv0\pmod2.
\]

**Both arithmetic maps really do not commute on the fine four-state source**, and DO commute on the two-state observed quotient. Yet the coarse ORIGINAL parity claim requires only one bit. READ decides that claim in one operation on either carrier; with READ removed, both carriers lose all source target decodability and have no finite winning strategy. The certified h map is noninjective 4→2, preserves all relevant source/claim/observation morphisms, and maps legal observation paths to legal observation paths by an actual strict functor.

The observed "flatness" does NOT prove fine source actions commute, and a nonzero fine commutator does NOT prevent proof of a quotient-invariant source claim. This is a rigorous source-relative analogue of a geometrical defect disappearing under insufficient resolution, but NO claim of an actual spacetime curvature tensor, transportable quantum phase, nontrivial Chern class or gravity is made.

Independent positive examples with p=3,r=2,k=1,d=1,q=7 and p=5,r=2,k=1,d=1,q=11 have authentic prime q, fine nonzero defects divisible by p and coarse zero defect.

## 3. An essential adversarial trap: source arithmetic is NOT identified by observed action tables

A true prime q and a DIFFERENT true prime q' may satisfy q≡q' (mod p^k). Then their coarse dilations produce identical observable maps on R_k:

\[
V_q(x)\equiv V_{q'}(x)\pmod {p^k}.
\]

For p=2,k=1, q=3 and q'=5 are different ACTUAL primes, yet both give multiplication by one on R_1. The previously proved general coalgebra morphism (which sees only allowed public outcomes/effects) can therefore **legitimately** certify behavioral/proof-policy equivalence of these two coarse descriptions even though they do not share the same arithmetic prime-jet identity.

This is a **sigma/source-provenance failure** for any inference that the coarse operator reveals which exact Euler prime produced it. The mathematical equivalence is correct; the extra source-identity claim is false. The implementation now includes an INDEPENDENT arithmetic-signature gate that checks the declared p, primitive SUCC d, true prime jet q, report precision and quotient relation. It rejects q=3↔5 and d=1↔3 aliases even when the observer-level map passes.

This gate checks DECLARED source parameters, not cryptographic signatures or externally measured data. It cannot certify that the real world generated those parameters. Such external provenance is the next access/source-map gap. It prevents us from laundering a prime-insensitive finite category into an "authentic Euler" identity.

**Deliberately broken q=6 control:** multiplication by 6 obeys the SAME algebraic affine semidirect identity as multiplication by a prime. Hence the algebraic shift–dilation defect alone cannot distinguish a genuine Euler prime from a composite. The constructor rejects q=6 using an independent actual-prime predicate; it does NOT claim primality follows from SUCC/Yoneda.

## 4. Exact proof-scope status and follow-up

- **CLASSICAL/PROVED LOCAL:** Quotient ring map h and polynomial action commute; A2 affine address discrepancy, nonzero vs kernel-vanishing defect condition, exact source/target/action preservation for quotient-invariant claims.
- **TESTED MODEL:** Exhaustive finite x on p=2/3/5 source clocks, authentic/changed prime witnesses, source coaction/induced path-functor receipts, abstract/concrete finite adaptive policy ranks with and without a read instrument.
- **REFUTED:** A coarse faithful proof system reveals the fine source commutator; a nontrivial fine commutator forbids all source-relative proofs; a valid observation-coalgebra morphism uniquely identifies the Euler prime; the affine identity alone excludes composite multipliers.
- **UNVERIFIED:** Real physical source generation; externally authenticated arithmetic-source parameters; global analytic co-Yoneda/adelic transport; nontrivial ζ Gamma factor; Weil distribution positivity; RH; universal cost/proof speedup.

**Next decisive experiment:** replace this modular family with truly source-derived prime-power jet distributions across every precision and verify a PROJECTIVELY compatible family of source/measurement transport maps. A p-adic measure requires independently proved **uniform boundedness and source-specific moments**; finite congruence and passing Yoneda tests are insufficient. Cross-check with false Euler prime/composite, wrong Teichmüller branch, p=2 edge cases and conductor/half-density before any RH handoff.

**Artifacts:** \`observational_succ/prime_clock_yoneda.py\`, \`tests/test_prime_clock_yoneda.py\`, \`scripts/prime_clock_yoneda_probe.py\`; operational Yoneda source-policy theorem and roadmap/claim ledger. Primary mathematical background: elementary quotient-ring arithmetic, prior SUCC proto-SUCC variable-unit/ax+b and Mahler prime-clock research; ring reduction is a standard homomorphism, not a new number-theoretic theorem.
