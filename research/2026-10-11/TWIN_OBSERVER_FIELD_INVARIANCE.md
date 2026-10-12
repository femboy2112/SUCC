# Twin observers in one field: mathematical frame invariance and focus-only SUCC

**Date:** 2026-10-11. **Status:** maintainer-originating calibration assumptions; classical mathematics, elementary proved-local lemmas and exact finite tests; universal physical/categorical consequences UNVERIFIED.

**Dependencies:** the verified algebra–trig circle research in the stacked draft PR #10, and the earlier relative knowledge-SUCC architecture. The pinned historical import and main branch remain unchanged.

## 1. Original proposal, precisely preserved

A and B are **twins** in every respect other than mathematical field specialization. Both inhabit the **same actual field**. They possess equal baseline semantic knowledge, the **same available empirical probes**, including time-indexed positions, velocities/tangents and trajectories, and equal reasoning capabilities. The mathematical laws underlying the actual structure do not change with the observer's presentation.

A specializes in polynomials/algebra, B in trigonometry/geometry. This difference determines their chosen **focus, representation and finite investigative path**, never their intrinsic mathematical truth or their physical instrumentation.

An admissible cross-language benchmark cannot give B a tangent sensor A lacks, nor suppose B receives an exact entire trajectory while A receives only a sparse point set. Prior complementary-hardware constructions are valid *other* models but are not tests of this strict twin hypothesis.

**Interpretive distinction:** identical *access* to a future probe is not identical to having *already actualized its outcome*. Instantaneous assimilation of acquired evidence does not imply instantaneous performance of every allowed physical probe.

## 2. Mathematical frame-invariance theorem (elementary)

Fix one underlying interpreted source structure F, one shared set of physical probe descriptions P and sound inference/interpreter basis R. Let L_A and L_B be two presentations with faithful maps I_A, I_B into F and a correctly verified translation T on a declared fragment. Require the evaluation diagram to commute:

\[
\operatorname{Eval}_A(\varphi,H)
=
\operatorname{Eval}_B(T\varphi,H)
\]

for every formula in that fragment and shared source observation record H.

**Twin-symmetry proposition (PROVED LOCAL):** If both observers begin with the same interpreted knowledge, actualize exactly the same sequence of physical probes and outcomes, and perform equivalent deterministic sound inference closure, then at every finite observational SUCC frame they have identical *semantic consequences* and identical possible future physical probes, though formulas and derivations may look different.

**Proof:** Equality holds initially. The next shared probe reads the same actual source, and the faithful interpretation gives corresponding records. Sound equivalent closure yields the same interpreted consequence set. Induction finishes the claim.

This produces a **symmetry-collapse warning**: if one also requires that both observers have the same fully exhaustive probe schedule and instantaneous closure of all relevant justified consequences, different notation ALONE cannot generate a new epistemic delta. The theory needs to distinguish an equal opportunity set P from the potentially different FOCUS maps \(\pi_A,\pi_B\) selecting which experiment to actually run. Those maps may differ without conferring different powers.

Mathematical statements are frame-invariant **under structure-preserving interpretation**. Numeric coordinate values, an uncalibrated signed orientation or syntactically undefinable claims need not remain literally unchanged. Invariance of a law is not a license to assume an arbitrary interpretation map preserves every theorem.

## 3. Same physical circle, different research focus

Let the shared source class be the exactly specified constant-speed paths

\[
X=\{\gamma_1,\gamma_5,\gamma_9\},\qquad
\gamma_k(t)=(\cos(2\pi kt),\sin(2\pi kt)).
\]

The actual source is \(\gamma_1\). Both twins have already observed the identical point positions at

\[
t=0,\ \frac14,\ \frac12,\ \frac34,\ 1.
\]

Those data are identical across the three sources, so both share initial source-compatible model \(K=\{1,5,9\}\).

**Identical empirical opportunities** include:
- A further point-at-time probe at \(t=\frac18\);
- A normalized, oriented tangent-at-time probe at \(t=0\);
- The same mathematical circle, source family and sound inference rules.

A (polynomial focus) chooses the point probe: its result is shared by \(k=1\) and \(k=9\), so its new compatible class is \(\{1,9\}\). B (trig focus) chooses the tangent: under constant-speed uniform rotation, it immediately identifies \(k=1\).

The tangent is also available to A, and the phase probe is also available to B. The difference is purely **investigative choice**.

The exact algebraic-to-trig normalized tangent identity is

\[
\boxed{
k=\frac{x\dot y-y\dot x}{2\pi}
=\frac{1}{2\pi}\frac{d\theta}{dt}.
}
\]

For the uniform path, \(\dot x=-2\pi k y\) and \(\dot y=2\pi k x\). Thus \(x\dot y-y\dot x=2\pi k(x^2+y^2)=2\pi k\). The trig side gives \(\dot\theta=2\pi k\). Both observers infer the **same** \(k\) from the **same normalized physical tangent outcome**.

This corrects one earlier completion classification: with an exact tangent probe in the full common opportunity set, the unrestricted integer *uniform-rotation* class is finitely identifiable. The previous omega-only classification applied only to a **restricted sequence of point-at-rational-time probes**. The apparent disagreement was about the allowed probe family, not either mathematical language.

## 4. Knowledge transfer and the two separate synchronization contracts

B communicates its newly actualized tangent fact to A using a finite relative probe-and-value delta. A absorbs it in one knowledge-aided SUCC and has the same compatible source \(k=1\) and the same set of mathematical predictions, same source interpretation, same available instruments and same reasoning rules as B. The event remains labeled as testimony from B, not as an observation physically performed by A.

Yet A also physically measured the extra \(t=\frac18\) phase sample. B did not. If the observer dynamics tracks *already-used one-shot probes*, one knowledge transfer gives **equal semantic knowledge** but not identical past measurement sets or remaining *unperformed* empirical actions. A second return delta, carrying A's now-predictable point sample as an A-origin record, aligns the stronger future single-use observation frontier. The two observer histories retain their distinct original event origins.

The exact finite program distinguishes:
- **Semantic knowledge equality**: same source-compatible fiber, universally agreed predictions, shared empirical opportunity set and inference language;
- **History-sensitive operational equality**: same above plus identical sets of already performed probes and identical remaining single-use measurement frontiers;
- **Causal provenance**: who actually performed which source measurement.

The receiver uses a shared response table and external trust in source testimony. Software hashes and source-consistency checks are not physical source authentication. The transmitted probe token is interpreted as an index among the receiver's presently unperformed shared probes; its value code is omitted when already deducible from the recipient's current compatible source class. This is a relative delta, not a dump of the source's global state. The module does NOT claim globally bit-optimal coding.

## 5. A stronger hostile regime: arbitrary smooth paths

Equal ability to probe a finite set of point positions **and derivatives** does not imply ability to identify the winding of an arbitrary \(C^\infty\) loop.

Let \(t_1,\dots,t_n\) be finitely many sample times in [0,1] and choose an open interval (a,b) containing none. Define the flat smooth-step function by

\[
\eta(u)=
\begin{cases}e^{-1/u},&u>0,\\0,&u\le0,\end{cases}
\qquad
h(u)=\frac{\eta(u)}{\eta(u)+\eta(1-u)}
\]

for 0<u<1, extended by 0 before u=0 and 1 after u=1. Let \(g(t)=h((t-a)/(b-a))\), and modify a smooth closed path \(\gamma\) by

\[
\widetilde\gamma(t)=\gamma(t)e^{2\pi i g(t)}.
\]

The multiplier equals 1 at every sampled time, and is infinitely flat at the two transition endpoints. Consequently \(\gamma\) and \(\widetilde\gamma\) have exactly the same full derivative jet at **every sampled time**, but

\[
\operatorname{wind}(\widetilde\gamma)
=
\operatorname{wind}(\gamma)+1.
\]

This is a classical smooth-step/covering-space argument, not a numerical infinite-derivative test. The finite software verifies a rational sample-free insertion interval and returns a symbolic witness with explicit limits.

**Crucial scope distinction:** if the entire oriented continuous trajectory has actually been supplied as an exact mathematical function, not merely available for finite sampling, the winding number is determined. The counterexample concerns finitely many localized observations from the unrestricted smooth source class. It affects both twins identically.

## 6. What the test proves—and does not

The executable tests compare exact rational polynomial and independent Fourier interpretations at shared cardinal probes; validate the one-form/tangent normalization on rational circle points; construct two field specialists with the exact same physical probe tuple and reasoning signature but different focus order; and verify reciprocal testimony-based synchronization, stale-source rejection and provenance separation.

**PROVED LOCAL:** equal shared data plus semantically faithful inference implies equal interpreted knowledge by induction; a finite trusted delta merges compatible evidence and may align semantic conclusions; one reciprocal delta can align otherwise differing one-use probe records.

**CLASSICAL:** circle polynomial/trig identities and angular tangent transport; a constant-speed rotation's integer winding is one exact normalized tangent coefficient; smooth flat-step insertions change winding without changing finite sampled jets.

**UNVERIFIED:** an empirical theory of human specialization or cognition; equal physical access in actual humans; full source authentication; infinite-precision physical tangent measurement; general categorical language equivalence; all-orders effective infinite SUCC completion; any arithmetic Weil-sign or RH proof.

**Highest-value next research:** Represent field specialization as a typed **focus/proof-search policy over identical source, probe and inference capabilities**. Compare proof and communication costs only after counting translation, shared basis and verification. Build a continuation-preserving cross-language delta for trajectories and derivative probes, with an actual semantics-preserving map between the two proof presentation systems. Test arbitrary smooth-path hostile cases and noisy empirical tangent data before claiming the same finite recoverability in physical systems.

**Verdict:** different observer frames need not imply different worlds, different instruments or different laws. Under the user's twin idealization they are **different coordinated mathematical descriptions and investigative priorities inside one shared source structure**. An epistemic SUCC difference can arise from choosing different lawful investigations, and a correct relative delta can reconcile it while respecting both original causal histories.
