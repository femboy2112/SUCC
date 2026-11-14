# Addendum: A-priori inflation, finite causal separation and delta-like observer sectors

**Origin:** Leah's 2026-11-14 proposal: inflation preceding observation may itself be an *analytic defect from a finite observer's perspective*, making different realizable mathematical frames cease to be fully equivalent. The "Dirac delta for frames" and "more categories in a CCC type one-category" are author metaphors; below is their strongest explicit mathematical reconstruction, not an established physical identification.

**Status:** Exact discrete finite/limit witness and smooth-FLRW nonidentifiability lemma (**PROVED in the stated toy classes**); category/CCC and physical inflation interpretation **CONJECTURED / UNVERIFIED**. No assertion that SUCC observer axioms produce a physical Big Bang, an actual metric, Einstein dynamics, QFT vacuum or gravitational entropy.

## A. The distinction: a source origin is not ongoing causal contact

A source root at time 0 is a **past common ancestor**, not a guarantee that all descendants can subsequently exchange messages. Actual contact depends on propagation and on the time-dependent metric/access graph. To speak of two observers comparing histories, retain the emission/arrival times and the provenance of the comparison. Untimed "can contact" relations between worldlines need not compose: a signal from A might reach B only *after* B's last opportunity to contact C. Use a time-labelled event path category, not an untyped reachability relation, to avoid SUCC's PAP-04 invented-path defect.

The mathematical marker for causal reach in a flat FLRW model is the comoving light travel integral:
\[
\Delta\chi(t_0,t_1)=c\int_{t_0}^{t_1}\frac{dt}{a(t)}.
\]
For fixed \(t_0\), a finite total future conformal interval \(\int_{t_0}^\infty dt/a(t)<\infty\) provides a future event-horizon bound. For a finite beginning \(t_i\), the past communication bound \(\int_{t_i}^{t_\ast}dt/a(t)\) can depend on expansion before \(t_\ast\), even if every later local metric observation agrees. A Hubble radius alone is not an event horizon. Finite-duration inflation does not by itself imply a permanent event horizon.

## B. DISCLOSED exact toy theorem: finite arrival versus limit-only boundary

Consider two sequences of positive rational scale factors, in synchronous unit-duration ticks \(n\in\mathbb N_0\), with discrete signal travel capacity \(1/a_n\) per tick. This is a declared communication carrier, not a discretization proven to satisfy physical Einstein equations:
\[
\begin{array}{c|ccc|c}
n&0&1&2& n\ge3\\ \hline
a_n&1&2&4&3^n\\
b_n&1&3&9&3^n
\end{array}
\]
where the common continuation starts at \(n=3\), with \(3^3=27\). For a comoving separation \(d=3/2\), cumulative reach after \(N\) ticks is \(D_a(N)=\sum_{n=0}^{N-1}a_n^{-1}\), analogously \(D_b(N)\).

**Theorem.** These two carriers have identical late-time scale readouts for every \(n\ge3\), but finite-time contact across \(d\) exists in carrier \(a\) and does not exist in carrier \(b\). Their total analytic reaches are
\[
D_a(\infty)=1+\frac12+\frac14+\sum_{n=3}^\infty3^{-n}
=\frac{65}{36}>\frac32,
\]
\[
D_b(\infty)=1+\frac13+\frac19+\sum_{n=3}^\infty3^{-n}
=\frac{13}{9}+\frac1{18}=\frac32.
\]
Moreover \(D_a(2)=3/2\), hence a signal arrives at a finite event after two ticks; \(D_b(N)<3/2\) for *every finite* \(N\), because all omitted tail summands are strictly positive. Thus B attains the boundary only as \(N\to\infty\). No arrival event at infinite clock time exists in the declared finite-event category.

**Proof.** The common tail is geometric: \(\sum_{n=3}^\infty3^{-n}=(1/27)/(1-1/3)=1/18\). The displayed finite sums and strictly positive missing tail prove all claims. \(\square\)

**Observer-target consequence.** Let \(E_{\ge3}\) be the entire sequence of scale readings at epochs \(n\ge3\). Let \(P\) answer whether a source signal at epoch 0 can reach separation \(3/2\) in finitely many ticks. Then \(E_{\ge3}(a)=E_{\ge3}(b)\) but \(P(a)\ne P(b)\), so there is **no** \(\bar P\) with \(P=\bar P\circ E_{\ge3}\) on the two-source model class. This is the inherited SUCC target-descent obstruction instantiated by a new finite-versus-limit causal pair. A sensor retaining earlier pulses, early-time clocks, or authenticated source action laws can break the equivalence; those are **different toolkits**.

Do not silently call the limit equality \(D_b(\infty)=d\) a physical causal contact. The asymptotic equality and finite reachability have distinct quantifiers.

## C. Smooth accelerating analogue and its precise source class

Fix \(0<t_\ast<\infty\), \(H>0\), and a nonnegative, nonzero smooth function \(h\in C^\infty_c((0,t_\ast))\). For \(\epsilon\ge0\) define
\[
a_\epsilon(t)=\exp(Ht+\epsilon h(t)),\qquad t\ge0.
\]
The metric \(g_\epsilon=-c^2dt^2+a_\epsilon(t)^2d\chi^2\) is a smooth 1+1 FLRW-type test geometry. All \(a_\epsilon\) and **all their late-time derivatives** equal \(e^{Ht}\) for \(t\ge t_\ast\). On the compact support of \(h\),
\[
\frac{\ddot a_\epsilon}{a_\epsilon}=(H+\epsilon h')^2+\epsilon h'',
\]
which remains positive for sufficiently small \(\epsilon>0\). Thus these are two genuinely accelerating early histories, not one inflated history versus a static one.

Their past null-reach target is
\[
L(\epsilon)=c\int_0^{t_\ast}e^{-Ht-\epsilon h(t)}dt,\qquad
L'(0)=-c\int_0^{t_\ast} e^{-Ht}h(t)dt<0.
\]
Hence for sufficiently small \(\epsilon>0\) the histories have **different causal past reach** even though their late-time local metric jets are exactly identical. For any \(d\) strictly between their reaches, a signal emitted at \(t=0\) arrives by \(t_\ast\) in one model and not the other.

This is a rigorous *smooth-model source nonidentifiability* result under the restricted late-time observation toolkit. The defect \(L(\epsilon)-L(0)\) is nonzero for every small \(\epsilon>0\) and tends to zero as \(\epsilon\to0\); \(L\) is real analytic in **the parameter \(\epsilon\)**, not necessarily in time \(t\).

**Hostile source restriction:** If we demand that \(a(t)\) be *real analytic in time on one connected domain* and exactly known on an open late-time interval, then the identity theorem defeats this bump construction: two such analytic functions agreeing on that open interval agree throughout the domain. Likewise, source-faithful deterministic gravitational field equations plus adequate complete Cauchy data may rule out arbitrary histories with the same later state. The strong indistinguishability result therefore depends on the chosen **smooth** source class and restricted accessible toolkit, not on an unavoidable feature of every physical cosmology.

## D. Delta-like separation: a correct mathematical analogy, not a physical law

For a finite collection of distinct source-marked frames \(F_i\) with a metric \(d(i,j)\) and parameter \(q\in(0,1)\), define a dimensionless model coupling kernel
\[
K_q(i,j)=q^{d(i,j)}.
\]
For a discrete frame metric with positive separation off diagonal,
\[
\lim_{q\downarrow0}K_q(i,j)=\delta_{ij}.
\]
At every finite \(q>0\), cross-frame couplings are nonzero; at the limiting kernel they vanish exactly. This is a **Kronecker delta** on a discrete set of frames; on a continuous space a normalized approximate identity converges distributionally to a **Dirac delta**, which is a different mathematical object. No connection between \(q\) and the physical FLRW scale factor is derived.

This model captures the author's "realizable frames, not completely equivalent": finite measurements may identify them under an accessible quotient, although a source-relative target or future intervention separates them. The limiting diagonal kernel is not itself a category creation theorem.

**Categorical reconstruction.** Let \(\mathcal E\) be a category of *time-labelled* source events and lawful causal processes, with composition permitted only for temporally composable paths. For an observer toolkit \(\mathcal T\), let \(E_\mathcal T\) send source states/processes to accessible transcripts where this is a genuine functor. Then one may examine (i) the observable quotient and its fibres, (ii) time-dependent accessible subcategories or slices, (iii) their connected components, and (iv) idempotent sector projectors **when they are actually constructed**. Different observational fibres need not be equivalent as **source-marked** structures even if late-time readouts agree.

If "CCC" means **Cartesian closed category**, the construction requires extra categorical checks: arbitrary accessible subcategories and quotients need not remain Cartesian closed. In particular, a bare one-category is not forced to split into multiple distinct categories when metric connectivity changes. A family of indexed observational categories, or a Grothendieck construction over time/toolkit, is the more faithful candidate. If CCC has another SUCC-specific meaning, keep the acronym unresolved until its source contract is supplied.

## E. Steelman–crucible–verdict

**DISLOSED within the declared carrier:** rational exact finite/limit contact theorem; target non-descent; smooth pre-observation expansion family with different past conformal reaches and identical post-observation metric jets; delta-kernel limit on finite frames.

**CONJECTURED:** pre-observation inflation may act as a generator of observer-relative sectors in a source-typed categorical description; analytic-defect operators could compare their past access structures.

**UNVERIFIED:** that the mathematical zero/initial source in SUCC authenticates a physical cosmological initial state; that the specific BBP/Oily branching prior implements FLRW expansion or Einstein dynamics; that a causal sector split implies fundamentally different ontology.

**Hostile controls:** static common past without continued communication; same late metric but differing early histories; smooth versus analytic-in-time source class; finite threshold versus exact zero coupling; correlation without signaling; untyped worldline composition inventing causal paths; a finite inflation period followed by a decelerating expansion without a future event horizon.

**Next verdict-changing probe:** source-authenticate an inflation/clock map from the actual finite observer carrier; predeclare a later observable sensitive to an earlier horizon difference; test against the same late metric but different pre-observer expansion, plus matched-source noninflation and different-source inflation controls. If the future observable cannot distinguish within the declared closure, report **target nonidentifiability**, not proof of physical infinity.

## Provenance

- [Founding causal-relevance proposal PR #618](https://github.com/femboy2112/SUCC/pull/618), §9 finite-versus-limit defect.
- [Second Forge PR #620](https://github.com/femboy2112/SUCC/pull/620): weighted observation quotients, timed causal horizons and source/path-lifting controls.
- [Operational GR PR #623](https://github.com/femboy2112/SUCC/pull/623): cone and calibration boundaries.
- [Source/entropy GR PR #624](https://github.com/femboy2112/SUCC/pull/624): no-go for uncalibrated physical source identification.
- [Prior Field/Inflation PR #345](https://github.com/femboy2112/SUCC/pull/345) and [#346](https://github.com/femboy2112/SUCC/pull/346): pre-observation expansion as a declared causal/information model, with no physical-inflation claim.

No literature priority claim, new empirical measurement, or physics theorem from the SUCC source is made.
