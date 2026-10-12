# Source-relative SUCC precision transport theorem

**Date:** 2026-10-11. **Origin:** maintainers' proposal to promote proto-SUCC's variable-unit gauges into a theorem distinguishing reversible coordinate changes, recoverable precision losses and true source interventions. **Branch:** research/source-relative-precision-transport-2026-10-11, stacked on the variable-D proto-SUCC research PR #18. **Status:** CLASSICAL algebra / PROVED LOCAL by elementary derivation, with finite exact code, explicit witnesses and hostile independent tests. No assertion of priority for a new theorem; the genuinely SUCC-specific contribution is its **typed application and evidence obligations**. No physical measurement, adelic Gamma completion or RH claim.

## 1. Typed objects, partial maps and the first mathematical trap

Fix an **actual prime** p, integer r >= 1 and nonzero integer step d. Write v=v_p(d)>=0. Our input clock is the additive group A_r = Z/p^r Z. An output with p-adic resolution s>=1 would be

\[
F_d^{r,s}:A_r\longrightarrow A_s,\qquad [x]_{p^r}\longmapsto[dx]_{p^s}.
\]

**Representative independence (the first gate):**

\[
\boxed{F_d^{r,s}\text{ is a well-defined group map }\iff s\le r+v.}\tag{T1}
\]

Indeed, x and x+p^r represent the same input, whereas their outputs differ by dp^r. The outputs agree modulo p^s precisely when s <= v_p(dp^r)=r+v. This is *not* a claim that multiplying an arbitrary chosen integer representative and reducing at arbitrarily high resolution is a lawful map from the original quotient. Such a construction reads extra source digits not present in the declared input. For d=0 every s is lawful, but the output is always zero.

Whenever 1<=s<=r+v, set

\[
k=\max(0,s-v)\quad (0\le k\le r).
\]

By p-adic divisibility,

\[
F_d^{r,s}(x)=F_d^{r,s}(y)
\iff p^s\mid d(x-y)
\iff x\equiv y\pmod{p^k}.\tag{T2}
\]

This includes s<=v (k=0): *every* source address has the same output. Thus the kernel is p^k A_r, the image has p^k elements and every image fiber has exactly p^(r-k) elements. These are exact finite algebraic assertions, not estimates from sampling. The quotient-to-image factorization is the classical First Isomorphism Theorem (e.g. [Jeffries, Algebra I, Theorem 4.4.3](https://jack-jeffries.github.io/F25/817text.html)); the displayed valuation refinement is proved directly here.

**Full precision recovery (second gate):**

\[
\boxed{s_{\min}^{\rm full}=r+v,\quad
F_d^{r,r+v}:A_r\xrightarrow{\sim}p^v A_{r+v}.}\tag{T3}
\]

The codomain on the right is the **additive subgroup/image ideal**, not the whole enlarged clock. Given y in this image, the source is recovered by

\[
x \equiv (d/p^v)^{-1}(y/p^v) \pmod{p^r}.
\]

Multiplication by the unit d/p^v is invertible modulo p^r. If s<r+v, then k<r and some distinct source states collide; the lift is not faithful on the whole clock. If s>r+v, F is not well-defined. For d=0 no finite output resolution restores arbitrary source distinctions.

**Operational definition (not a physical law):** the exact *arithmetic precision debt* of this nonzero multiplication channel is v_p(d) **additional output base-p digits**. It is neither a universally lost number of bits nor a thermodynamic dissipation law. Multiplication by nonunit d is not a full-clock automorphism, but it can remain a *faithful embedding into an appropriately finer clock's subgroup*. At p=5, r=2, d=5:

- output mod 25 has 5 distinguishable values, 5 sources per fiber;
- output mod 125 has 25 distinguishable values, 1 source per fiber;
- a proposed output mod 625 from only a mod-25 source is representative-dependent: 0 and 25 are the same source, but 5*0 and 5*25 differ mod 625.

At d=0, output remains constant at every resolution. **No recovery from this particular channel** does not imply no other valid carrier measurement exists.

## 2. The source-relative transport theorem for mathematical claims

Now add the missing *source and proof* semantics. Fix an actual, explicitly declared finite compatible-source set X subset A_r, and a function t:X->Y representing a claim's answer/value on each compatible source. We do NOT assume this table was physically measured or independently justified. A receiver sees only F_d^{r,s}(x), plus the shared basis, declared context and legal decoder.

**Theorem (finite source-relative exact transport):**

\[
\boxed{\exists\,g:F(X)\to Y\text{ with }t=g\circ F|_X
\iff \forall x,y\in X,\ F(x)=F(y)\implies t(x)=t(y).}\tag{T4}
\]

If a decoder exists, the implication follows immediately. Conversely, define g(F(x))=t(x); the fiber condition makes this well-defined, and it is the *unique* decoder on the actual observed image. If the condition fails, a witness (x,y) with one observed address and two different t-values is an exact **no-decoder certificate for the declared observation protocol**. This proves failure of that proposed channel, NOT that the mathematical statement is unprovable by another method.

Define the **separation depth** of t relative to X:

\[
k_*(t,X)=
\begin{cases}
0& t\text{ is constant on }X,\\
1+\max\{v_p(x-y):x,y\in X,\ t(x)\ne t(y)\}&\text{otherwise}.
\end{cases}
\]

For distinct residues x,y, v_p(x-y)<r, independent of chosen representatives, so k_* is an integer from 0 to r. Equation (T2) and the maximal conflicting pair give the **exact minimal resolution**:

\[
\boxed{s_{\min}(t,X;d)=
\begin{cases}
1& t\text{ constant},\\
\text{no finite resolution}&d=0,\;t\text{ nonconstant},\\
v_p(d)+k_*(t,X)&d\ne0,\;t\text{ nonconstant}.
\end{cases}}\tag{T5}
\]

Proof: at s>=v+k_* every observation fiber is also a constant-t class by definition; at s<v+k_* the maximizing unequal-labeled pair collides. When t is constant, a decoder exists even for zero output. **Context and conclusion matter:** total source recovery may need r+v digits, while one particular theorem may need only k_*+v.

Example p=5, r=2, d=5, all 25 compatible source residues:
- t_low(x)=x mod 5 has k_*=1, so mod 25 output suffices (s_min=2);
- t_high(x)=floor(x/5) has k_*=2, so mod 25 output **cannot** support it; mod 125 output does (s_min=3).
- The program emits an explicit same-output/different-claim source pair for the failed high-digit transport.
- A narrowing source law can lower k_*; an unlicensed source enlargement can raise k_* and invalidate an old decoder.

This is a **theorem about finite source-indexed predicates and observation channels**. It makes no claim about minimum transmission bits, computational complexity, automatic derivation of t, actual physics or independence in formal proof systems. In the implementation, a context includes full source, basis, claim and table equality checks. These prevent accidental stale-certificate reuse against a *different supplied context*; identifiers are self-declared metadata, not signatures or independent verification of the premises.

## 3. Composition: debt is additive, but proof transport is conditional

For d,e nonzero let v=v_p(d), w=v_p(e). Two maximum-lawful faithful lifts compose:

\[
A_r\xrightarrow{F_d^{r,r+v}}p^v A_{r+v}
 \xrightarrow{F_e^{r+v,r+v+w}}p^{v+w}A_{r+v+w}.
\]

The second arrow is understood as the restriction of the corresponding full-clock map to the first image. It sends x to edx at the final resolution, and

\[
\boxed{F_e\circ F_d=F_{ed},\qquad v_p(ed)=v_p(e)+v_p(d).}\tag{T6}
\]

Associativity follows from integer multiplication; d=1 is the identity at fixed precision. **Do not silently call every nonzero d a reversible arrow of the entire target clock.** A nonunit faithful lift is an embedding into an image subgroup; an inverse is defined only on that image. A modular unit is an automorphism of the whole input clock. These are different types.

The exact code has a typed full-lift constructor, composition witness, and inverse restricted to the image. The p=5 changing-unit example from PR #18 is now resolved: the step 1 -> 5 ceases to be a unit **of Z/25**; that does not destroy the 25 source distinctions if the receiver is allowed to use the correctly declared 5 Z/125 image. It says nothing about whether such increased precision is physically accessible or justified.

## 4. Third gate: a change of source cannot be disguised as a gauge

Let h:X->X' be a *declared source intervention*, t:X->Y the original target and t':X'->Y the post-intervention target. Let the receiver observe F' on X'. Two independent obligations are needed:

\[
\boxed{\text{semantic/source preservation:}\quad t=t'\circ h}\tag{T7a}
\]

\[
\boxed{\text{observational support:}\quad
t'|_{h(X)}\text{ factors through }F'|_{h(X)}.}\tag{T7b}
\]

Together these yield t=g\circ F'\circ h with the *same source-dependent claim meaning*. If (T7a) fails, no amount of output precision can make the post-intervention claim equal the original; if only (T7b) fails, higher lawful precision may restore a decoder. This is a strong and testable distinction between **changed truth conditions** and **insufficient observational resolution**.

Positive: h(x)=x+5 mod 25 preserves x mod 5; a post-source observation at d=5, s=2 recovers the low-digit claim.

Negative control A (probe gap): h is identity but output precision s=2 aliases high-digit claims; s=3 repairs it.

Negative control B (genuine source change): h(x)=x mod 5 erases the original high digit and t'(h(x))=floor(h(x)/5)=0. The pre-source high-digit claim changes, so even injective post-source output at s=3 cannot certify that ORIGINAL claim. The actual physical existence and provenance of any h remain external assumptions.

The diagram is meaningful *only* with typed source semantics and a verified commuting claim law. Untyped equality of two coordinate formulas is insufficient.

## 5. Reproduction, adversarial controls and limits

Code: observational_succ/precision_transport.py. Tests: tests/test_precision_transport.py. CI receipt: scripts/precision_transport_probe.py.

Controls include: 0 multiplier and constant/nonconstant claim; false prime p=6; representative independence failure at s=r+v+1; negative d and p=2; exact orbit/kernel/cardinality; full inverse and two/three lift composition; all 2^8 Boolean claim tables on Z/8 against a separately implemented group-by-output oracle; 100 deterministic seeded multi-label/subset holdouts; unchanged-vs-expanded source set; stale source/basis/claim metadata; source-truth-changing intervention; and the PR #18 (0,1,4)->(1,5,4) unit-crossing benchmark.

The pure mathematical statements T1-T7 are proved by finite group/valuation algebra and explicit factorization, rather than proved by code exhaustions. Tests are calibration, mutation controls and reproducibility. **No arbitrary infinite source, unknown physical instrument, unbounded proof certificate, categorical Yoneda equivalence, noncommutative holonomy, adelic transport or completed Weil positivity is established.**

### Claim status and the next *verdict-changing* experiment

- **PROVED LOCAL/CLASSICAL:** T1-T6 and the conditional T7; exact minimal claim-specific p-adic resolution is a specialization of finite fiber-factorization and valuation algebra.
- **REFUTED:** “a nonunit step destroys distinctions at every precision”; “one extra output digit is always enough regardless of v_p(d)”; “all source claims require the full source precision”; “post-intervention proof truth is recovered solely by increasing precision.”
- **UNVERIFIED:** physical feasibility of higher precision or independently certified original sources; genuine source-dependent nonlinear gauge connections; a transport functor across adelic real/p-adic places; any new RH theorem.

**Next** build finite *source-attested* proof-support diagrams and compare algebraically faithful transport with physically realizable measurements. Then use independently constructed p-adic cylinder distributions with bounded all-level norms and Euler source mutations. Nontrivial arithmetic transport will have to reproduce real Gamma/Poisson source compatibility and ultimately a correct zero-blind Weil identification; this theorem alone cannot do that.

**Sources/prior art:** First Isomorphism Theorem, finite quotient group algebra, p-adic valuations, exact deterministic sufficiency/fiber factorization. Basic p-adic Newton/Mahler interpolation and prime clock facts are tracked separately in MAHLER_SUCC_CLOCK_KUMMER.md. These foundations are classical; the new research question is how to type and verify their passage through observational and proof-bearing SUCC processes.
