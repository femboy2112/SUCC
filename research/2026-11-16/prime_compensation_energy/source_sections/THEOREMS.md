# PCE-12–18 — Source-valid sections, observer inertia, and the pointed BBP carry

**Date:** 2026-11-16. **Status:** original finite exact derivations / classical ingredients; zero-seed normality and RH **OPEN**. Additive supplement to the SUCC PCE draft PR #661, based on Main XXVI. The terms *causal energy*, *inertial force* and *curvature* below name declared observer-relative mathematical defects, NOT physical energy or spacetime curvature. No independent academic priority is claimed.

**Motivation.** The author points out that finite prime-insertion zeta(-1) already gives an object invariant under a complete path and nontrivial component motions under constrained observation. A source-valid reconstruction must retain a hidden causal coordinate; it must not conflate *an algebraically valid state*, *an authentically reachable state*, and *the literal zero-seeded historical state*. Here we prove a finite-memory closure for the zeta(-1) observer and a pointed source reconstruction and set-valued fiber continuation for the genuine BBP recurrence.

## PCE-12. The missing zeta(-1) coordinate is exactly one orientation bit (EXACT)

Fix distinct genuine rational primes `S`, `Q=∏_{p∈S}p`, `ω(Q)=|S|`. Retain the exact PCE Euler/Hurwitz registers

\[
E_Q=\prod_{p\mid Q}(1-p)^{-1},\qquad
R_Q=\zeta(-1)\prod_{p\mid Q}(1-p),\qquad E_QR_Q=-\frac1{12}.
\]

In the split chart `u=(E+R)/2`, `v=(E-R)/2`, the canonical orbit lies on `u²-v²=-1/12`, where `v` never vanishes. Since `E_Q` has sign `(-1)^ω(Q)` and `R_Q` has the *opposite* sign,

\[
\boxed{v_Q=(-1)^{\omega(Q)}\sqrt{u_Q^2+1/12}.}\tag{PCE-12.1}
\]

Consequently the reported state `(u_Q, b_Q)` with `b_Q=(-1)^ω(Q)` determines the full pair `(E_Q,R_Q)` exactly by

\[
J_b(u)=(u,b\sqrt{u^2+1/12}),\qquad E=u+v,\ R=u-v.\tag{PCE-12.2}
\]

**Proof:** `v²=u²+1/12` follows from the invariant hyperbola. For `E>0,R<0`, `v=(E-R)/2>0`; for `E<0,R>0`, `v<0`. The sign of `E` is the parity of the number of genuine negative factors `1-p`. No square root approximation is involved: on the authenticated finite orbit its value is the rational `|v_Q|`.

The two values `J_+(u),J_-(u)` are distinct, source-*surface*-valid points for every real u. A lone u cannot reconstruct v on the **whole hyperbola**, and a single bit suffices. This is an information-minimality statement over that two-sheeted observer fiber. It is *not* a lower bound on the computational difficulty of recovering a known finite `Q`.

## PCE-13. Exact reduced dynamics with orientation memory (EXACT)

For an inserted genuine prime p not already in S, put `a_p=p-1`,
\[
c_p=\frac{a_p+a_p^{-1}}2,\qquad s_p=\frac{a_p-a_p^{-1}}2.
\]

The full SUCC/PCE prime map `T_p` acts on `(u,v)` as
\[
(u',v')=(-c_pu+s_pv,\ s_pu-c_pv).
\]

Combining it with PCE-12 gives a source-valid reduced recursion on **one real number plus one bit**:

\[
\boxed{\mathcal T_p(u,b)=\left(-c_pu+s_pb\sqrt{u^2+1/12},\ -b\right).}\tag{PCE-13.1}
\]

For every authentic finite-prime stage, this exactly reconstructs `u_{Qp}, b_{Qp}` and the full Euler/Hurwitz pair. It also defines a closed dynamics on the *entire* augmented source hyperbola, not just the finite canonical stages. Authentic prime-order commutation is inherited from commuting full T_p, with the bit retained. At p=2, `s_p=0` and the coarse u-step happens to close without seeing b, though orientation still flips; for any p>2 the two branches give distinct next u.

**Observer defect:** if the bit is forgotten and an arbitrary sign is reintroduced at intermediate steps, the procedure does **not** compute the canonical source path. The defect is a failure of observer descent, not curvature of the full flat prime-insertion connection. A *correct* source-labelled reinjection uses b and has exactly zero defect.

## PCE-14. A nonzero source-surface-valid but historically wrong inertial cost (EXACT)

Start at the genuine empty-prime state `E=1,R=-1/12`, thus `(u,v)=(11/24,13/24)` with b=+1. Insert the genuine p=3. The authentic intermediate point is

\[
(u_3,v_3)=(-1/6,-1/3),\qquad b_3=-1.
\]

The wrong choice `J_+(u_3)=(-1/6,+1/3)` **still lies on** the exact source hyperbola, but it is not the genuine p=3 path. After inserting genuine q=5:

\[
\boxed{u_{\rm actual}=-13/48,\quad
u_{\rm right\ branch}=-13/48,\quad
u_{\rm wrong\ branch}=47/48,\quad
u_{\rm actual}-u_{\rm wrong}=-5/4.}\tag{PCE-14.1}
\]

This is an exact calibration on a *source-surface-valid* reinjection and two authentic primes. It should not be called a genuine zero-defect-preserving **history-valid** reinjection: the reset broke prime ancestry by dropping b. Preserving that one bit restores zero defect. Contrast the earlier PCE-11 `45/32`, which used the ambient section `(u,0)` **outside** the hyperbola.

The earlier value also admits an exact provenance: `45/32=(3/4)(15/8)=sinh(log2)sinh(log4)` for p=3 and q=5. **Numerical correction:** `45=3²·5`, NOT `2³·5`; `32=2⁵`. Similar-looking rational defects (such as `17/16`) are not identified without a typed transport/normalization map.

## PCE-15. Exact pointed BBP carry/fractional compensation, at every finite horizon (EXACT)

The original source is fixed, with no replacement forcing or seed:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Let `n>=1`, `C_n=floor(U_n)`, `u_n={U_n}`, and write the authentic finite forcing block

\[
R_{n,h}=\sum_{j=1}^h16^{h-j}r(n+j),\qquad h\in\mathbb N_{>0}.
\]

The exact lifted future is `U_{n+h}=16^hU_n+R_{n,h}`. Define the coarse-observer apparent source response

\[
K_{n,h}=C_{n+h}-16^h C_n
=\left\lfloor16^h u_n+R_{n,h}\right\rfloor.
\]

Its hidden-fiber compensation is

\[
F_{n,h}=u_{n+h}-16^hu_n-R_{n,h}.
\]

**Exact zero of the full source:**

\[
\boxed{K_{n,h}+F_{n,h}=0\qquad\text{for every }n\ge1,h\ge1.}\tag{PCE-15.1}
\]

Both pieces can be nonzero, but they sum to zero *before* any averaging, analytic continuation, or speculative Gamma identification. This is a source-authenticated, time-directed additive compensation, **not** the same quadratic pairing as `ER=-1/12`. The comparison is structural, not a claim of literal isomorphism.

Since `0<r(n+1)<1` for n>=1, write `j_n=floor(16u_n)`, `epsilon_n=1_{ {16u_n}+r(n+1)>=1 }`. Then

\[
C_{n+1}=16C_n+j_n+\epsilon_n,\quad
u_{n+1}=16u_n+r(n+1)-j_n-\epsilon_n.
\]

For the Main XXVI selected carry sign `sigma(c)=1-2 1_{c mod4 in {1,2}}`,

\[
\boxed{\sigma(C_{n+1})=\sigma(j_n)
  (1-2\epsilon_n1_{j_n\text{ even}}).}\tag{PCE-15.2}
\]

The last factor is the *genuinely joint*, oriented source-seam term. Its time-average is **not** proved positive; for fixed seed it may vary with n. The authentic source wrap `epsilon_n` has the separately established logarithmic refractory bound in GCT-06. This source identity alone gives neither R0 nor normality.

## PCE-16. Exact zero-seed reinjection exists only with the missing history supplied (EXACT boundary)

The canonical rational state at time n is explicitly

\[
U_n^0=\sum_{j=1}^n16^{n-j}r(j),\qquad u_n^0=\{U_n^0\}.
\]

The source-labelled lift of an integer carry `c` at time n is

\[
\boxed{J_n^{\rm src}(c)=c+u_n^0.}\tag{PCE-16.1}
\]

It reproduces the **literal zero-seeded history** only for `c=C_n^0`. For any other c it is a legal state of the *same forced recurrence with the explicitly changed rational seed*

\[
\boxed{s(c,n)=\frac{c-C_n^0}{16^n}.}\tag{PCE-16.2}
\]

Thus a source passport makes the pointed reconstruction deterministic, and any claimed novel 'force' from resetting its exact hidden coordinate vanishes. By contrast `P(C,u)=C` does **not** admit a global one-step descent map on the source-allowed all-seed domain: at a fixed n>=1, `(C,0)` and `(C,1/16)` share the same carry but their next carries are `16C` and `16C+1`. They are lawful same-forcing continuations from *different seeds*, not two possible states of the **same pointed zero seed**. This exact obstruction is Principia CG-02/07, not an unproven assertion about epistemic causation.

The true original source is a singleton at each fixed n if *all* its equations and the seed are given. Calling a reset with a different fraction 'still zero-seeded' is therefore invalid. The meaningful nontrivial cost is a cost of limited observational access to u or of replaying the authenticated source journal.

## PCE-17. Set-valued, source-lawful reinjection and its precision debt (EXACT)

For a radix depth `k>=1`, let `M=16^k`. A coarse observer reads the true time n, `C_n`, and the first k hexadecimal cells of the fractional coordinate, `a_n=floor(M u_n)`. Reinject **the entire reported cylinder**

\[
\boxed{\mathcal J_{n,k}(C_n,a_n)=
[C_n+a_n/M,\ C_n+(a_n+1)/M).}\tag{PCE-17.1}
\]

This set contains the original authentic state and never chooses a fictitious single 'zero seed'. Other points in the set are explicit *changed-seed* counterfactuals; the literal zero seed remains one distinguished member. Every point evolves by the **same authentic four-pole forcing**. The exact set of possible future carries at horizon h is the consecutive integer interval

\[
\boxed{\left[
\left\lfloor16^h(C_n+a_n/M)+R_{n,h}\right\rfloor,
\left\lceil16^h(C_n+(a_n+1)/M)+R_{n,h}\right\rceil-1
\right]\cap\mathbb Z.}\tag{PCE-17.2}
\]

This result is a theorem of monotone affine maps and the floor operation; the high endpoint is excluded, hence the ceiling-minus-one convention. The genuine zero-seeded future carry belongs to this interval.

**Sharp one-digit ambiguity:** for every n>=1 and **every** of the sixteen first-hex-digit bins, the one-step future carry has exactly two possible values, because `0<r(n+1)<1` shifts a unit-length interval across one integer threshold. For two digits (M=256), at most 16 out of the 256 possible bins have an ambiguous one-step carry, since the floor map has exactly 16 source-dependent threshold points in `(0,1)`.

**Temporal precision debt:** a k-digit cylinder expands to width `16^(h-k)` after h source steps. For `h>k`, its set of possible future carries has at least `16^(h-k)` members. Coarse bits without authentic history cannot predict arbitrary far-future carries from a fixed finite-precision report. This is a source-model-relative observability statement, **not** complexity-theoretic hardness or evidence for a density asymptotic. A source-complete observer can compute `U_n^0` by its exact finite recurrence.

## PCE-18. Why these two compensations are not yet a prime↔BBP dynamical theorem (OPEN)

The prime coordinate pair `E_Q,R_Q` has an *exact invariant endpoint* `ER=-1/12` and a one-bit orientation section at s=-1. The BBP real state has a *forced affine time law*, with integer winding and fractional state compensating at every step. Their apparent observer defects share the structure 'projected history loses the coordinate needed for exact composition', but the product invariant and additive forced law live in distinct types.

The classical reflected identity `xi(-1)=xi(2)=pi/6=(8/3)x_BBP`, with `x_BBP=pi/16` from the literal four-pole source, transports a completed scalar **only**. It does not map finite prime insertion time or `omega(Q)` to chronological BBP time n, nor supply a lower bound on the Main XXVI carry density. A source-authenticated map must preserve real integer winding, odd denominators, fractional fibers, complete source labels, the zero seed, and correctly transported Gamma/Weil signs. Otherwise a coherent wrong seed shares all prime scalar readouts yet has a locked completed circle phase.

**Falsifiers/controls:** (i) discard parity at the genuine Q=3 stage then insert 5: wrong-branch gap `-5/4`; (ii) retain parity: gap zero; (iii) p=2 orientation flips even though its boost coefficient `s_p` vanishes; (iv) fake composite 6 rejected as new prime; (v) zero-seed vs changed-rational-seed typing; (vi) s=1/16 circle alias after n>=2; (vii) integer seed shift preserves fractional states and mod-four winding for n>=1; (viii) polynomial coboundary g(n)=2n² changes source presentation but preserves completed circle with transformed tail; (ix) one hex digit is always insufficient to determine the next carry on the all-seed source fiber; (x) finite certificates do not prove an eventual all-shell law. Controls are not silently intersected into a nonexistent common carrier.

**Verdict:** PCE-12–17 are exact mathematical statements on their declared source and observer spaces. The orientation-bit compression is a genuine finite-memory closure of the zeta(-1) hyperbola. The BBP cylinder is a genuine source-containing set-valued reinjection. Neither solves R0, normality, RH, nor supplies physical causal force. The next potentially decisive lemma is a **zero-ancestry-sensitive all-shell constraint** on the signed `j_n,epsilon_n` joining that cannot hold for the rational prescribed-carry shadows.
